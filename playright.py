#LOADING THE JSON
import json
import os
with open("data/links.json", "r") as file:
    links = json.load(file)

print("Total Links", len(links))

from playwright.sync_api import sync_playwright

#folder to scrape the text
os.makedirs("data/pages", exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for i, url in enumerate(links):
        print("Scraping", url)

        page.goto(url, timeout=60000, wait_until="domcontentloaded")
        page.wait_for_timeout(300) #wait 3 sec for page load

        content = page.inner_text("MainArticleContent_articleMainContentCss__b_1_R article--viewer_content")

        file_name = f"data/pages/page_{i+1}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(content)

        print("saved", file_name)
        
    browser.close()
