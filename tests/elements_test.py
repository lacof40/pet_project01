import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


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

    class TestCheckBox:
        def test_check_box(self, browser):
            check_box_page = CheckBoxPage(browser, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(output_result)
            print(input_checkbox)
            assert input_checkbox == output_result, "checkboxes haven't been selected"

    class TestRadioButton:

        def test_radio_button(self, browser):
            radio_button_page = RadioButtonPage(browser, "https://demoqa.com/radio-button")
            radio_button_page.open()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"
