import time
from bs4 import BeautifulSoup
from selenium import webdriver
from flask import Flask, request, jsonify
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


app = Flask(__name__)


def search_on_imdb(movie_name):
    # put that searching url into chrome browser with the help of selenium
    imdb_link = "http://www.imdb.com"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    browser.get(imdb_link)
    search_bar = browser.find_element_by_name("q")
    search_bar.clear()
    search_bar.send_keys(movie_name)
    search_bar.send_keys(Keys.RETURN)
    video_links = []
    movie_page_html = browser.page_source
    browser.quit()
    soup = BeautifulSoup(movie_page_html, "lxml")
    tds = soup.find_all('td', class_='result_text')
    number_of_results = 0
    for td in tds:
        _name = td.find('a').get_text()
        page_suffix = td.find('a').get('href')

        if page_suffix:
            _url = 'https://www.imdb.com{}'.format(page_suffix)
            number_of_results += 1
            video_links.append(_url)

    return {
        "videoLinks": video_links
    }


def search_on_youtube(movie_name):
    # on the basis of search text...search on youtube
    url = "https://www.youtube.com/results?search_query={}".format(movie_name.replace(' ', '+'))
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    browser.get(url)
    time.sleep(1)

    #Fetch Video Links::
    video_data = browser.find_elements_by_xpath('//*[@id="video-title"]')
    video_links = []
    for video in video_data:
        video_link = video.get_attribute('href')
        if video_link:
            video_links.append(video_link)

    while True:
        browser.execute_script("window.scrollBy(0,100)", "")
        video_sections = browser.find_elements(By.ID, "video-title")
        print("Total Video Sections :: {}".format(len(video_sections)))
        if len(video_sections) >= 100 or len(video_sections) >= len(video_links)-4:
            break
        time.sleep(0.2)

    browser.quit()
    return {
        "videoLinks": video_links
    }


@app.route('/movie-details', methods=['POST'])
def fetch_movie_page():
    if request.method == 'POST':
        try:
            movie_name = request.form['movieName']
            site_domain = request.form['siteDomain']
        except Exception as e:
            return jsonify({
                    "error": "Invalid Input"
                })

        movie_details = dict()
        if "youtube" in site_domain.lower(): 
            movie_details = search_on_youtube(movie_name)
        elif "imdb" in site_domain.lower():
            movie_details = search_on_imdb(movie_name)

        return jsonify(movie_details)


if __name__ == '__main__':
    app.run(debug=True)

