# -*- coding: utf-8 -*-
import requests, json
import mimetypes, os
import wget
import pandas as pd
from pandas.io.json import json_normalize
from pathlib import Path
from woocommerce import API
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts


" Connect and consume external rest api
token = 'TGHFVZbSBxPoAF-4_al6NU-h47fzcvyQ'
hotdealrest_url = 'https://api.accesstrade.vn/v1/offers_informations?scope=expiring'
campainrest_url = "https://api.accesstrade.vn/v1/campaigns"
headers = { 'Authorization' : 'Token ' + token }
r = requests.get(hotdealrest_url, headers=headers, verify=False)

campainList = json.loads(requests.get(campainrest_url, headers=headers, verify=False).text)

for item in campainList["data"]:  
    topproducts = "https://api.accesstrade.vn/v1/top_products?date_from=01-01-2019&date_to=30-10-2019&merchant=adayroi"
    topproductRequest = requests.get(topproducts, headers=headers, verify=False)
    jtopProducts = json.loads(topproductRequest.text)
    print(jtopProducts)
    dfTopProducts = json_normalize(jtopProducts["data"])
    dfTopProducts.columns()
    dfTopProducts["category_name"] = "Top sản phẩm bán chạy > Top bán chạy shopee.vn >" + dfTopProducts["category_name"]
    dfTopProducts["desc"] = dfTopProducts["name"] + " Giá rẻ"
    dfTopProducts["short_desc"] = dfTopProducts["name"] + " Giá rẻ"
    dfTopProducts["tags"] = dfTopProducts["name"] + " Giá rẻ"
    dfTopProducts.to_csv("topshopee.vn.csv", encoding='utf-8', index=False)
    print(dfTopProducts)
" load data
jhotdeal = json.loads(r.text)


print(jhotdeal)




# define site variables
wpUrl='https://www.sangiare24h.com/xmlrpc.php' 
#WordPress Username
wpUserName='admin'
#WordPress Password
wpPassword='Danghungit@85'
client = Client(wpUrl,wpUserName,wpPassword)

def post_article(wpUrl,wpUserName,wpPassword,articleTitle, articleCategories, articleContent, articleTags,PhotoUrl):
		path=os.getcwd()+"\\0001.jpg"
		articlePhotoUrl=PhotoUrl
		wpUrl=wpUrl
		wpUserName=wpUserName
		wpPassword=wpPassword
		#Download File
		#f = open(path,'wb')
		#f.write(urllib2.urlopen(articlePhotoUrl).read())
		#f.close()
		#Upload to WordPress
		client = Client(wpUrl,wpUserName,wpPassword)
		#filename = path
		# prepare metadata
		#data = {'name': 'picture.jpg','type': 'image/jpg',}
		
		# read the binary file and let the XMLRPC library encode it into base64
		#with open(filename, 'rb') as img:
		#	data['bits'] = xmlrpc_client.Binary(img.read())
		#response = client.call(media.UploadFile(data))
		#attachment_id = response['id']
		#Post
		post = WordPressPost()
		post.title = articleTitle
		post.content = articleContent
		post.terms_names = { 'post_tag': articleTags,'category': articleCategories}
		post.post_status = 'publish'
		#post.thumbnail = attachment_id
		post.id = client.call(posts.NewPost(post))
		#print ('Post Successfully posted. Its Id is: %s',post.id)
        
#########################################
# Creating Class object & calling the xml rpc custom post Function

#On Post submission this function will print the post id

for row in jhotdeal['data']:
    print(row['domain'],row['name'],row['content'],row['aff_link'],row['image'],row['end_time'])
    articleTitle = row["name"]
    articleTags=[row['name'], 'ma giam gia ' + row['domain'],'khuyến mại '+row['domain']]
    articleCategories=['Khuyến Mại', row['domain']]
    ariclePhotoUrl = row["image"]
    #articleContent = "<p>" + row["content"]+"""</p></br><a href='"""+row["aff_link"]+"""'class='button product_type_external'></a>"""
    articleContent = """
    <div class="excoupon">
      <div class="excontainer">
        <h3>%s</h3>
      </div>
      <a href='%s'>
        <img class='alignnone size-full' src='%s' />
      </a>
      <div class="excontainer" style="background-color:white">
        <h2><b>%s</b></h2>
        <p>%s</p>
      </div>
      <div class="excontainer">
        <p class="exexpire">Expires: %s</p>
         </br>
         <a href='%s'class='buttonproduct_type_external' target="_blank">Xem Chi Tiết</a>
      </div>
    </div>
   """%(row["name"],row["aff_link"],row["image"],row["name"],row["content"],row["end_time"],row["aff_link"])
    #post to wp
    post_article(wpUrl,wpUserName,wpPassword,articleTitle, articleCategories, articleContent, articleTags,ariclePhotoUrl)
###########################
# load data from csv######
##########################
productsData = pd.read_csv('cookeddhcvietnam.com.vn.csv')
productsData.columns

# Woocommerce add products
wcapi = API(
    url="https://sangiare24h.com",
    consumer_key="ck_1c04362c3cd5e5178ac30a4b61959ef42f5cde5c",
    consumer_secret="cs_8c3575f42d9feb9c132358a15a4867b5eeb4a35d",
    wp_api=True,
    version="wc/v3",
    #query_string_auth=True
    )
## loop json top products
jtopProducts['data']
for row in jtopProducts['data']:
    text = row["name"] + " Giá rẻ"
    external_url = "https://go.isclix.com/deep_link/4725587962428837650?url=" + row["link"]
    data = {
        "name": row["name"],
        "type": "external",
        "regular_price": str(row["price"]),
        "sale_price": str(row["discount"]),
        "description": text,
        "short_description": text,
        "external_url": external_url,
        "categories": [
            {
                "name": "Top sản phẩm bán chạy"
            },
            {
                "name": "Top bán chạy Tiki"
            }
        ],
        "images": [
            {
                "src": row["image"]
            }
        ],
        "tags": [{"name":text}],
        "status": "publish"
        
    }
    print(wcapi.post("products", data).json())
## loop csv products     
for index,row in productsData.iterrows():
    text = row["name"] + " Giá rẻ"
    external_url = "https://go.isclix.com/deep_link/4725587962428837650?url=" + row["link"]
    data = {
        "name": row["name"],
        "type": "external",
        "regular_price": str(row["price"]),
        "sale_price": str(row["discount"]),
        "description": text,
        "short_description": text,
        "external_url": external_url,
        "categories": [
            {
                "name": "Top sản phẩm bán chạy"
            },
            {
                "name": "Top bán chạy Tiki"
            }
        ],
        "images": [
            {
                "src": row["image"]
            }
        ],
        "tags": [{"name":text}],
        "status": "publish"
        
    }
    print(wcapi.post("products", data).json())
