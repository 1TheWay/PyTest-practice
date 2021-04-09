import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_garbage(browser):
    browser.get(link)
    #time.sleep(5)
    item = browser.find_element_by_class_name("btn-add-to-basket")
    assert item!=None, "There isn't the garbage"
