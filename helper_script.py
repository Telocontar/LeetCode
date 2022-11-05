from typing import List, Dict, Union

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def generate_test_cases(examples: List[str], function_name: str) -> str:

    print("Generating test cases...")

    # holds the variable initializations for the test cases
    var_inits = []
    test_cases = []

    for i, example in enumerate(examples, start=1):
        _input = example.split("Input: ")[1].split("\n")[0]
        var_values = [var_def.split(" = ")[1] for var_def in _input.split(", ")]
        output = example.split("\nOutput: ")[1].split("\n")[0]

        var_list = []
        for j, var_value in enumerate(var_values):
            # pattern: test_input_1a, test_input_1b, ...
            var_init = f"test_input_{i}{chr(97+j)} = {var_value}"
            var_inits.append(var_init)
            var_list.append(f"test_input_{i}{chr(97+j)}")

        test_case = f"assert {function_name}({', '.join(var_list)}) == {output}"
        test_cases.append(test_case)

    test_case_str = "\n".join(var_inits) + "\n\n" + "\n".join(test_cases)

    return test_case_str


def get_problem_definitions(page_content: str) -> Dict[str, Union[str, List[str]]]:

    print("Getting problem definitions...")

    if "To view this question you must subscribe to premium." in page_content:
        raise ValueError(f"Error: {'To view this question you must subscribe to premium.'}. Rerun script.")

    try:
        problem_text = page_content.split("Add to List\nShare\n")[1].split("\nAccepted\n")[0]
    except IndexError:
        problem_text = page_content.split("Add to List\n")[1].split("\nAccepted\n")[0]

    description = problem_text.split("  Example 1:\n")[0]

    examples = problem_text.split("Example ")[1:]
    # cut the constraints from the last example
    examples[-1] = examples[-1].split("\n  Constraints:")[0]
    constraints = problem_text.split("\n  Constraints:\n")[1]

    result_dict = {
        "problem_text": problem_text,
        "description": description,
        "examples": examples,
        "constraints": constraints
    }

    return result_dict


def parse_webpage(url: str) -> str:

    print("Preparing webdriver...")

    # do not open browser window
    options = webdriver.ChromeOptions()
    options.add_argument("headless")

    # access the url
    print("Downloading webpage...")
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
                              options=options)
    driver.get(url)

    # get the body
    page_content = driver.find_element(By.TAG_NAME, "body").text

    return page_content


def print_problem_definition_and_test_cases(url: str, function_name: str):

    page_content = parse_webpage(url=url)

    problem_def_dict = get_problem_definitions(page_content=page_content)
    problem_text = problem_def_dict["problem_text"]
    examples = problem_def_dict["examples"]

    test_case_str = generate_test_cases(examples=examples, function_name=function_name)

    print(f'\n"""\n{problem_text}\n"""\n\n')
    print(test_case_str)
    print(f'\nprint("Tests successful.")')


if __name__ == "__main__":

    # contains all problems for category "algorithms"
    leet_code_api_url = "https://leetcode.com/api/problems/algorithms/"
    leet_code_api_url = "https://leetcode.com/problems/reverse-linked-list/"

    print_problem_definition_and_test_cases(url=leet_code_api_url, function_name="reverseList")

