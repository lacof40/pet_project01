from pages.alerts_frame_windows_page import BrowserWindowsPage


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
