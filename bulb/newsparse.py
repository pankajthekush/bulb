from newspaper import Article
from loadpage import selenium_page_source

def process_article(url):
    dict_data = dict()
    dict_sel_data = selenium_page_source(url=url)
    
    current_url = dict_sel_data['current_url']
    page_source = dict_sel_data['page_source']
   
    if current_url == 'error':
        dict_data['is_error'] = True
        return dict_data

    article = Article(url)    
    article.download(input_html=page_source)
    article.parse()
    article.nlp()

    dict_data['title'] = article.title
    dict_data['text'] = article.text
    dict_data['url'] = current_url 
    dict_data['authors'] = article.authors
    dict_data['top_image'] =article.top_image
    dict_data['images'] = list(article.images)
    dict_data['tags'] = list(article.tags)
    dict_data['movies'] = article.movies
    dict_data['meta_data'] = article.meta_data
    dict_data['meta_lang'] = article.meta_lang
    dict_data['meta_site_name']= article.meta_site_name
    dict_data['article_html'] = article.html
    dict_data['summary'] = article.summary
    dict_data['keywords'] = article.keywords
    return dict_data


    

if __name__ == "__main__":
   d =  process_article('https://zeenews.india.com/india/bus-pickup-collision-in-up-s-pilibhit-cm-yogi-adityanath-announces-ex-gratia-of-rs-5-lakhs-2318035.html')
   print(d)



