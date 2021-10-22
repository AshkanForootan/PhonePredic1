import requests 
from bs4 import BeautifulSoup
import re
import numpy as np
from sklearn import tree
import locale
import streamlit as st
locale.setlocale(locale.LC_ALL, 'en_US')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


st.title('Live Web Scarping & Machine Learning Project for Predicting Phone Price by Ashkan Forootan')
st.write ("")
st.write ("")

myURL_xiaomi="https://www.technolife.ir/product/list/69_70_79/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-xiaomi?keywords=&only_available=1&sort=price-desc&page=1"
myURL_apple="https://www.technolife.ir/product/list/69_70_73/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%BE%D9%84-apple?keywords=&only_available=1&sort=price-desc&page=1"
myURL_samsung="https://www.technolife.ir/product/list/69_70_77/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-samsung?keywords=&only_available=1&sort=price-desc&page=1"
myURL_huawei="https://www.technolife.ir/product/list/69_70_798/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D9%87%D9%88%D8%A7%D9%88%DB%8C-huawei?keywords=&manufacturer_id=&only_available=true&sort=price-desc"
myURL_LG="https://www.technolife.ir/product/list/69_70_781/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%84-%D8%AC%DB%8C-lg?keywords=&manufacturer_id=&only_available=true&sort=price-desc"


expander_bar_About = st.expander("About")
expander_bar_About.markdown("""
* **Python libraries:** requests, BeautifulSoup, streamlit, numpy, re, sklearn, locale
* **Data source:** [www.technolife.ir for xiaomi](https://www.technolife.ir/product/list/69_70_79/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B4%DB%8C%D8%A7%D8%A6%D9%88%D9%85%DB%8C-xiaomi?keywords=&only_available=1&sort=price-desc&page=1).
* **Data source:** [www.technolife.ir for apple](https://www.technolife.ir/product/list/69_70_73/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%BE%D9%84-apple?keywords=&only_available=1&sort=price-desc&page=1).
* **Data source:** [www.technolife.ir for samsung](https://www.technolife.ir/product/list/69_70_77/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-samsung?keywords=&only_available=1&sort=price-desc&page=1).
* **Data source:** [www.technolife.ir for huawei](https://www.technolife.ir/product/list/69_70_798/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D9%87%D9%88%D8%A7%D9%88%DB%8C-huawei?keywords=&manufacturer_id=&only_available=true&sort=price-desc).
* **Data source:** [www.technolife.ir for LG](https://www.technolife.ir/product/list/69_70_781/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%A7%D9%84-%D8%AC%DB%8C-lg?keywords=&manufacturer_id=&only_available=true&sort=price-desc).
* **Credit:** Web scraper adapted by BeautifulSoup & Machine Learning by sklearn (DecisionTreeClassifier)).
* **by:** [Ashkan Forootan](http://ashkanforootan.com)).
""")


def myOperation(brandName):
    # Begin of xiaomi
    URL_b=globals()['myURL_%s' % brandName]
    page = requests.get(URL_b)
    #st.write (page)
    if page.status_code == 200:
        st.write ("Web Scraping is Successfull for <%s> !" % brandName)
        #st.write ("===========================================================")


    soup = BeautifulSoup(page.text, "html.parser")

    results1 = soup.find_all('span', attrs={''})
    results2 = soup.find_all( attrs={'class' : 'ProductComp_main_price__1duzX'}) + soup.find_all( attrs={ 'class' : 'ProductComp_offer_price__2V-ls'})

    arr1 = np. array(["Camera"])
    arr2 = np. array(["Memory"])
    arr3 = np. array(["Screen"])
    arr4 = np. array(["Battery"])
    arr5 = np. array(["Price"])

    counter=0
    for Item1 in results1:
        if counter % 4 == 0:
            res1=re.sub(r'<span class="">', '', Item1.text )
            res1.strip()
            arr1 = np. concatenate( (arr1, [res1]) )
        
        counter += 1


    counter=0
    for Item1 in results1:
        if counter % 4 == 1:
            res1=re.sub(r'<span class="">', '', Item1.text )
            res1.strip()
            arr2 = np. concatenate( (arr2, [res1]) )
                
        counter += 1

    counter=0
    for Item1 in results1:
        if counter % 4 == 2:
            res1=re.sub(r'<span class="">', '', Item1.text )
            res1.strip()
            arr3 = np. concatenate( (arr3, [res1]) )
            
        counter += 1


    counter=0
    for Item1 in results1:
        if counter % 4 == 3:
            res1=re.sub(r'<span class="">', '', Item1.text )
            res1.strip()

            arr4 = np. concatenate( (arr4, [res1]) )
            
        counter += 1
            



    for Item5 in results2:
        res5=re.sub(r'<div class="ProductComp_main_price__1duzX"><span>', '', Item5.text)
    # st.write(res5)
        res5=re.sub(r'تومان', '', res5)
        #st.write(res5)

        res5.strip()
    # st.write(res5)

        arr5 = np. concatenate( (arr5, [res5]) )


    expander_bar = st.expander(brandName)

    for i in range(arr1.size-1):
        if i!=0:
            expander_bar.write("%i - <%s> Phone with <%s> MegaPixels Camera, <%s> GB Memory, <%s> inches Screen, <%s> mAh Battery \nFound at <%s> Tomans Price !!!" % (i, brandName.upper(), arr1[i], arr2[i], arr3[i], arr4[i], arr5[i]))
            expander_bar.write ("===========================================================")
    #st.write ("===========================================================")
            
    arr1 = arr1.reshape((-1, 1))
    arr2 = arr2.reshape((-1, 1))
    arr3 = arr3.reshape((-1, 1))
    arr4 = arr4.reshape((-1, 1))
    arr5 = arr5.reshape((-1, 1))

    array=arr1
    array=np.c_[array,arr2]
    array=np.c_[array,arr3]
    array=np.c_[array,arr4]
    array=np.c_[array,arr5]

    headers=array[0]
    data=np.delete(array,0,0)


    x=(data[:,0:4]).astype(np.float64).tolist()
    y=(np.char.replace((data[:,-1]),",","")).astype(np.float64).tolist()

    globals()['clf_%s' % brandName] = tree.DecisionTreeClassifier()
    globals()['clf_%s' % brandName] =globals()['clf_%s' % brandName].fit(x,y)

    return globals()['clf_%s' % brandName]


myOperation("xiaomi")
myOperation("apple")
myOperation("samsung")
myOperation("huawei")
myOperation("LG")

st.write ("*******************************************************************")
st.header ("*** ATTENTION : dar hangame takhfif gheymat ha eshtebah hastand ***")
st.write ("*******************************************************************")
st.write ("")
st.write ("")
st.header ("*** Predictions: ***")


st.sidebar.header('Select your Desirable Parameters:')

inputCamera  = st.sidebar.slider("Please Select Camera in pixels: ", 10, 200, 64)
inputRAM     = st.sidebar.slider("Please Select Memory in GB: ", 2,2048, 256)
inputScreen  = st.sidebar.slider("Please Select Screen in inches: ", 3.0, 10.0, 6.7)
inputBattery = st.sidebar.slider("Please Select Battery in mAh: ", 1000, 10000, 7000)

newData = [[inputCamera,inputRAM,inputScreen,inputBattery]]


def finalOperation(brandName):
    answer = (globals()['clf_%s' % brandName]).predict(newData)
    answer = locale.format_string("%d", answer, grouping=True)

    #st.write ("*******************************************************************")
    #color = 'orange'
    st.write ("Prediction Price for your <<%7s>> Phone is <<%10s>> Tomans !!! " % (brandName.upper().center(8), answer.center(13)) )
    #st.write ('<span style="Prediction Price for your <<%s>> Phone is <<%s>> Tomans !!! ">%s</span>' % (brandName.upper().center(8), answer.center(13), color), unsafe_allow_html=True )
    #st.write('<span style="color:%s">%s</span>' % (color, color), unsafe_allow_html=True)
    # ====================================

finalOperation("xiaomi")
finalOperation("apple")
finalOperation("samsung")
finalOperation("huawei")
finalOperation("LG")
st.write ("*******************************************************************")
















