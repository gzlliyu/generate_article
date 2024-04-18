import re
import time

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def generate_article(subject: str, reference_content: str, article_type: str, audience: str, words_count,
                     url_content) -> str:
    """
    生成文章
    """

    reference_content_all = ''
    url_content_all = ''
    if reference_content:
        reference_content_all = f"文章需要扩写的大纲是：```{reference_content}```"
    if url_content:
        url_content_all = f"附加参考资料为（注意可作为参考润色，不可原样抄袭）：```{url_content}```"

    prompt_template = """你是一名资深作家，请撰写一篇{words_count}字左右的```{article_type}```文章，文章的主题是```{subject}```，文章的受众是```{audience}```。
        {reference_content_all}。
        {url_content_all}。
        要求：
        1、使用倒金字塔风格介绍文章的主题和目的，并在开头提出文章的关键问题和目的；
        2、引入故事情节，例如：xx的历史和传说；
        3、在合适的地方引经据典；
        4、掌握推出数字的艺术，例如：桑皮的药效和剂量；
        5、偶尔采用互动式写作，例如：提出问题让读者思考或进行小测试
        6、内容需贴合主题，体现你的个人特色和见解，语气亲和友好,给人以信任感；
        7、请尽量结构化、分段落，不要说无用重复的废话；
        8、偶尔使用一些口语化的表达是可以的,这样会让文章听起来更加自然、友好；
    """

    prompt = ChatPromptTemplate.from_template(
        template=prompt_template
    )

    model = ChatOpenAI(model_name='gpt-4')
    parser = StrOutputParser()

    chain = prompt | model | parser

    return chain.invoke(
        {"subject": subject,
         "reference_content_all": reference_content_all,
         "article_type": article_type,
         "audience": audience,
         "words_count": words_count,
         "url_content_all": url_content_all
         }
    )


def ai_analysis_param(query: str):
    analysis_prompt = ChatPromptTemplate.from_template(
        """请根据用户输入的文章要求提取出来以下字段：
        subject:[文章主题]
        article_type:[文章类型，默认：科普文章]
        audience:[文章受众，默认：普通读者]
        words_count:[文章字数，默认1000]
        reference_content:[大纲]
        url_link:[网页参考资料]

        要求：仅返回json格式，禁止解释

        用户输入的文章要求如下：

        {query}
        """
    )
    model = ChatOpenAI(model='gpt-4')
    json_parser = JsonOutputParser()
    chain = analysis_prompt | model | json_parser
    analysis_res = chain.invoke({"query": query})
    url_link = analysis_res.get("url_link")
    if url_link:
        # 网页不为空，提取网页内容，判断文本大小，如果不超过2000字，直接使用，超过2000字，进行截断
        url_content = summary_url_content(url_link)
        analysis_res['url_content'] = url_content
    else:
        analysis_res['url_content'] = ''

    del analysis_res['url_link']
    return analysis_res


def summary_url_content(url_link: str) -> str:
    dd = ''
    try:
        loader = WebBaseLoader(url_link)
        docs = loader.load()
        dd = "\n".join([d.page_content for d in docs])
        dd = re.sub(' +', ' ', dd)
        dd = re.sub('\n+', '\n', dd)
    except Exception as e:
        print(e)
    if len(dd) > 4000:
        return dd[:4000]
    else:
        return dd


def generate_article_by_language(user_input):
    params = ai_analysis_param(user_input)
    return generate_article(**params)

