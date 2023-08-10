import os
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(base_url="https://www.airbnb.com.ro/")
    api_request_context = context.request
    page = context.new_page()
