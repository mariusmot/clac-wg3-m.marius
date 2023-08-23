import asyncio
import re
from playwright.async_api import async_playwright
from playwright.async_api import Page, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--start-maximized"])
        page = await browser.new_page(no_viewport=True)
        # browser = await p.chromium.launch(headless=False)
        # page = await browser.new_page()
        await page.goto("https://www.airbnb.com.ro/")     

        #Accept Cookies - Locate by role
        await page.get_by_role("button", name=re.compile("OK")).click()
        await expect(page).to_have_title("Închirieri de case de vacanță și apartamente în complexuri rezidențiale - Airbnb")
        print('Cookies Accepted')

        #Click little Search icon - Locate by test id
        littlesearchicon = page.get_by_test_id("little-search-icon")
        await littlesearchicon.click()
        await expect(page.get_by_test_id("little-search-icon")).to_be_attached()
        print('Click little search icon')

        #Search destinations 
        await page.get_by_test_id("structured-search-input-field-query").fill("Philip")
        await expect(page.get_by_test_id("structured-search-input-field-query")).to_have_value("Philip")
        await page.get_by_test_id("option-0").click()
        await expect(page.get_by_test_id("structured-search-input-field-query")).to_have_value("Philippines")
        print("Option Philippines selected")

        #Check in
        await page.get_by_role("button", name=re.compile("Înainte pentru a trece la luna următoare.")).click()
        await expect(page.get_by_role("heading", name="septembrie 2023")).to_have_text("septembrie 2023")       
        await page.get_by_test_id("calendar-day-22.09.2023").click()
        await expect(page.get_by_test_id("calendar-day-22.09.2023")).to_have_text("22")
        print("Select Check In date")
        
        #Check out
        await page.get_by_test_id("calendar-day-29.09.2023").click()
        await expect(page.get_by_test_id("calendar-day-29.09.2023")).to_have_text("29")
        print("Select Check Out date")

        #Add guests
        await page.get_by_test_id("structured-search-input-field-guests-button").click()
        await expect(page.get_by_test_id("structured-search-input-field-guests-button")).to_have_text("Cine?Adaugă numărul de oaspeți")
        await page.get_by_test_id("stepper-adults-increase-button").click()
        await expect(page.get_by_text("1 oaspete")).to_have_text("1 oaspete")
        await page.get_by_test_id("stepper-adults-increase-button").click()
        await expect(page.get_by_text("2 oaspeți")).to_have_text("2 oaspeți")
        await page.get_by_test_id("stepper-children-increase-button").click()
        await expect(page.get_by_text("3 oaspeți")).to_have_text("3 oaspeți")
        await page.get_by_test_id("stepper-children-increase-button").click()
        await expect(page.get_by_text("4 oaspeți")).to_have_text("4 oaspeți")
        print("Add 4 guests")

        #Search
        await page.get_by_test_id("structured-search-input-search-button").click() 
        await expect(page.get_by_text("Search results")).to_have_text("Search results")       
        print("Search Results Returned")

        #Select option
        await page.get_by_role("button", name=re.compile("Cabană în Cuenca, 226 lei")).click() 
        #await page.get_by_test_id("listing-card-title")
        await expect(page.get_by_text("Statiunea tropicala TJM - Cabina 4")).to_have_text("Statiunea tropicala TJM - Cabina 4")

        #await page.get_by_role("button", name=re.compile("Insulă în El Nido")).click() 
        #await page.screenshot(path="Rezervare.png")
        
        #await page.wait_for_timeout(5000)
        await browser.close()

asyncio.run(main())  