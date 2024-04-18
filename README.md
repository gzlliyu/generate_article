# prompt：生成头条、小红书、百家号等文章

# 核心prompt代码如下

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