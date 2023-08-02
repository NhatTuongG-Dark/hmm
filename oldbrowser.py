from playwright.sync_api import BrowserContext, sync_playwright

from undetected_playwright import stealth_sync

headless = True

import time
def run(context: BrowserContext):
    page = context.new_page()
    page.goto("https://grafana.ventox.lol/")

    _suffix = "-headless" if headless else "-headful"
    time.sleep(10)
    
    
    page.screenshot(path=f"result/sannysoft{_suffix}.png", full_page=True)


def bytedance():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        stealth_sync(context)
        run(context)


if __name__ == "__main__":
    bytedance()
