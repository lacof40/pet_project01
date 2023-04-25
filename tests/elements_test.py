import time

from pages.elements_page import TextBoxPage


class TestElement:
    class TestTextBox:

        def test_text_box(self, browser):
            text_box_page = TextBoxPage(browser, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_perm_address = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name doesn't match"
            assert email == output_email, "the email doesn't match"
            assert current_address == output_cur_address, "the current address doesn't match"
            assert permanent_address == output_perm_address, "the permanent address doesn't match"
