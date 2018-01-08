import spynner

#we have to wait for the page to be rendered, so DOM items exist
def wait_for_render(browser,secs):
    try:
        browser.wait_load(secs)
    except:
        pass
    return

def login(browser, username, password):
    browser.wk_fill('input[class="required login-username"]',username)
    browser.wk_fill('input[class="required login-password"]', password)
    browser.click('button[data-domselect="sign-in"]')

#main
browser = spynner.Browser(debug_level=spynner.INFO)
browser.create_webview()
browser.show()
browser.load("https://localhost:8834")
wait_for_render(browser,1)

#logging in
login(browser, 'testuser', 'testpassword')
wait_for_render(browser,5)

#start scan, by name
print ("\n\nbrowsing to scan\n\n")
browser.click('td[data-order="test"]')
wait_for_render(browser,5)
print ("\n\nTrying to launch\n\n")
browser.click('span[id="launch-dropdown"]')
wait_for_render(browser,1)
browser.click('li[id="launch-default"]')
wait_for_render(browser,5)
browser.browse()
