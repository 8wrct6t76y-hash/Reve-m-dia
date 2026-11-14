# uso: python3 render_slides.py slides.html outdir  (cada <section class=s> vira um JPEG 1080x1350)
import sys, asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        await pg.goto("file://"+sys.argv[1]); await pg.wait_for_timeout(400)
        n = await pg.locator("section.s").count()
        for i in range(n):
            await pg.locator("section.s").nth(i).screenshot(path=f"{sys.argv[2]}/{i+1:02d}.jpg", type="jpeg", quality=92)
        await b.close(); print(n,"slides")
asyncio.run(main())
