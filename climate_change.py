import sys
import requests
from lxml import html

def crawler1():
    url = 'https://www.nature.com/nclimate/research'
    page=requests.Session().get(url) 
    tree=html.fromstring(page.text)
    titles = tree.xpath('//h3[@class="mb10 extra-tight-line-height word-wrap"]//a/text()')
    titles = [each.strip() for each in titles]
    #print(titles)
    #print(len(titles))

    article_pages = tree.xpath('//h3[@class="mb10 extra-tight-line-height word-wrap"]//@href')
    #print(article_pages)
    #print(len(article_pages))

    extract(article_pages)

def crawler2(num):
    url = 'https://www.nature.com/search?order=relevance&journal=nclimate&date_range=last_5_years&page=' + str(num)
    page=requests.Session().get(url)
    tree=html.fromstring(page.text)
    article_pages = tree.xpath('//h2[@role="heading"]//@href')
    #print(article_pages)
    
    extract(article_pages)

def crawler3(month,day):
    url = 'https://www.theguardian.com/environment/2020/'+ month + '/' + str(day) + '/all'
    page=requests.Session().get(url)
    tree=html.fromstring(page.text)
    article_pages = tree.xpath('//div[@class="fc-item__container"]//@href')
    #print(article_pages)

    for each in article_pages:
        u = each
        p = requests.Session().get(u)
        t = html.fromstring(p.text)
        content = t.xpath('//div[@class="content__article-body from-content-api js-article__body"]//p/text()')
        text = '\\n'.join(content)
        #print(text)
        output_file.write(text+'\n')

def crawler4():
    #url = 'https://www.skepticalscience.com/argument.php?f=percentage'
    url = 'https://www.skepticalscience.com/print.php?r=8'
    print(url)
    page=requests.Session().get(url)
    print(page)
    tree=html.fromstring(page.text)

def extract(pages):
    for each in pages:
        u = 'https://www.nature.com' + each
        p = requests.Session().get(u)
        t = html.fromstring(p.text)
        content = t.xpath('//div[@class="c-article-section__content"]//p/text()')
        ab = content[0].strip()
        if len(ab) > 600:
            #print(ab)
            output_file.write(ab+'\n')


if __name__ == '__main__':
    '''
    output_file = open('extra_info.txt','w')
    for i in range(1,32):
        print('processing page',i,'...')
        crawler2(i)
    '''
    '''
    output_file = open('extra_info.txt','w')
    month_list = ['feb','mar','apr']
    for month in month_list:
        print('for month:',month)
        for i in range(1,30):
            print('processing page',i,'...')
            crawler3(month,i)
    output_file.close()
    '''

    crawler4()





