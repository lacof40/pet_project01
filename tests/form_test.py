from pages.form_page import FormPage


class TestForm:
    class TestFormPage:

        def test_form(self, browser):
            form_page = FormPage(browser, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            p = form_page.fill_form_fields()
            result = form_page.form_result()
            assert [p.firstname + " " + p.lastname, p.email] == [result[0], result[1]], "the form has not been filled"
