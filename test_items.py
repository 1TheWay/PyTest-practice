link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

def test_guest_should_see_garbage(browser):
    browser.get(link)
    browser.find_element_by_class_name("btn-add-to-basket")
