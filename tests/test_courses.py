import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):

    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_text = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text("Courses")

    no_result_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_result_text).to_be_visible()
    expect(no_result_text).to_have_text("There is no results")

    no_result_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(no_result_icon).to_be_visible()

    no_result_desc = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(no_result_desc).to_be_visible()
    expect(no_result_desc).to_have_text("Results from the load test pipeline will be displayed here")










