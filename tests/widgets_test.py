from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, browser):
            accordian_page = AccordianPage(browser, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0, "Incorrect title or missing text"
            assert second_title == 'Where does it come from?' and second_content > 0, "Incorrect title or missing text"
            assert third_title == 'Why do we use it?' and third_content > 0, "Incorrect title or missing text"

    class TestAutoCompletePage:

        def test_fill_multi_autocomplete(self, browser):
            autocomplete_page = AutoCompletePage(browser, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            # print(colors)
            # print(colors_result)
            assert colors == colors_result, "the added colors are missing in the input"

        def test_remove_value_from_multi(self, browser):
            autocomplete_page = AutoCompletePage(browser, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after, "value was not deleted"

        def test_fill_single_autocomplete(self, browser):
            autocomplete_page = AutoCompletePage(browser, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            # print(color)
            # print(color_result)
            assert color == color_result, "the added colors are missing in the input"

    class TestDatePickerPage:

        def test_change_data(self, browser):
            date_picker_page = DatePickerPage(browser, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after, "the date has not been changed"

        def test_change_data_and_time(self, browser):
            date_picker_page = DatePickerPage(browser, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            # print(value_date_before)
            # print(value_date_after)
            assert value_date_before != value_date_after, "the date and time have not been changed"


class TestSliderPage:
    def test_slider(self, browser):
        slider = SliderPage(browser, 'https://demoqa.com/slider')
        slider.open()
        before, after = slider.change_slider_value()
        # print(before)
        # print(after)
        assert before != after, 'the slider value has not been changed'


class TestProgressBarPage:
    def test_progress_bar(self, browser):
        progress_bar = ProgressBarPage(browser, 'https://demoqa.com/progress-bar')
        progress_bar.open()
        before, after = progress_bar.change_progress_bar_value()
        assert before != after, 'the progress bar value has not been changed'
