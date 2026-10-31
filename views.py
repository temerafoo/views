import random, sys, time
from playwright.sync_api import sync_playwright

URL   = "https://guns.lol/temeraf.xo"
VIEWS = int(sys.argv[1]) if len(sys.argv) > 1 else 100

print(f"{URL} x{VIEWS}\n")
ok = 0
try:
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        for i in range(VIEWS):
            ctx = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                           "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
                viewport={"width": 1440, "height": 900},
            )
            page = ctx.new_page()
            try:
                page.goto(URL, wait_until="domcontentloaded", timeout=45000)
                page.wait_for_timeout(random.randint(7000, 12000))
                ok += 1
            except Exception:
                pass
            finally:
                ctx.close()
            print(f"{i+1}/{VIEWS}  ok={ok}")
            time.sleep(random.uniform(1, 3))
        browser.close()
except KeyboardInterrupt:
    pass

print(f"finished: {ok}/{VIEWS}")
