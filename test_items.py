import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_basket(browser):
    browser.get(link)
    #time.sleep(5)
    item = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(item)!=0, "There isn't the basket"
