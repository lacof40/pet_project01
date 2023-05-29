from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:

        def test_new_tab(self, browser):
            browser_windows_page = BrowserWindowsPage(browser, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "the new tab has not opened or not an incorrect tab has " \
                                                           "opened"

        def test_new_window(self, browser):
            browser_windows_page = BrowserWindowsPage(browser, "https://demoqa.com/browser-windows")
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "the new window has not opened or an incorrect window has " \
                                                           "opened"

    class TestAlertsPage:

        def test_see_alert(self, browser):
            alert_page = AlertsPage(browser, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert did not show up"

        def test_alert_appear_5_sec(self, browser):
            alert_page = AlertsPage(browser, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Alert did not show up"

        def test_confirm_alert(self, browser):
            alert_page = AlertsPage(browser, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', "Alert did not show up"

        def test_prompt_alert(self, browser):
            alert_page = AlertsPage(browser, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            # assert alert_text == f'You entered {text}'
            assert text in alert_text, "Alert did not show up"
