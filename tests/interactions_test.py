from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:
    class TestSortablePage:

        def test_sortable(self, browser):
            sortable_page = SortablePage(browser, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the grid has not been changed"


class TestSelectablePage:
    def test_selectable(self, browser):
        selectable_page = SelectablePage(browser, 'https://demoqa.com/selectable')
        selectable_page.open()
        item_list = selectable_page.select_list_item()
        item_grid = selectable_page.select_grid_item()
        assert len(item_list) > 0, "no elements were selected"
        assert len(item_grid) > 0, "no elements were selected"