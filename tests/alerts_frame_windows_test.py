from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


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

    class TestFramesPage:

        def test_frames(self, browser):
            frame_page = FramesPage(browser, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    class TestNestedFrames:

        def test_nested_frames(self, browser):
            nested_frames_page = NestedFramesPage(browser, 'https://demoqa.com/nestedframes')
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    class TestModalDialogsPAge:

        def test_modal_dialogs(self, browser):
            modal_dialogs_page = ModalDialogsPage(browser, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            # print(small)
            # print(large)
            assert small[1] < large[1], 'text from large is less than text from small dialog'
            assert small[0] == 'Small Modal', 'The header is not "Small modal"'
            assert large[0] == 'Large Modal', 'The header is not "Large modal"'
