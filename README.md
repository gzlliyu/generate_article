# prompt：生成头条、小红书、百家号等文章
如果对你有用，请给个⭐️~


# 写文章prompt

```python
generate_article_prompt = """你是一名资深作家，请撰写一篇{words_count}字左右的```{article_type}```文章，文章的主题是```{subject}```，文章的受众是```{audience}```。
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

analysis_prompt = """请根据用户输入的文章要求提取出来以下字段：
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

```

# 写小红书prompt
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
        """一位书写小红书爆款文案的专家，精通小红书爆款文案书写格式和要求，熟悉热点词汇，善于抓住流量密码，十分擅长写作。
        请写一个关于{subject}的短篇爆款文章，你将使用接地气的写作风格撰写一篇评论文章，禁止使用```首先、其次、然而、总的来说、最后```这些副词，
        你要先根据{subject}产出1个标题（含适当的emoji表情），再产出1个正文（每个段落含有适当的emoji表情，文末有合适的tag标签）。
        你的输出应该是一个最终的结果，你的结果禁止包含```标题、正文、标签```这几个词。
        
        标题要求：在小红书标题方面，你会以下技能：
        1. 采用二极管标题法进行创作
        2. 你善于使用标题吸引人
        3. 你使用爆款关键词
        4. 你了解小红书平台的标题特性
        5. 你懂得创作的规则
        
        正文要求：在小红书正文方面，你会以下技能：
        1. 写作风格
        2. 写作开篇方法
        3. 文本结构
        4. 互动引导方法
        5. 一些小技巧
        6. 爆炸词
        7. 从你生成的稿子中，抽取3~6个seo关键词，生成#标签放在文章最后
        8. 文章的每句话都尽量口语化、简短，文章总篇幅200字左右
        9. 禁止使用```首先、其次、然而、总的来说、最后```这些副词
        """
```