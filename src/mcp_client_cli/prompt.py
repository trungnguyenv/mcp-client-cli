prompt_templates = {
    "review": "You are an expert software engineer with a good taste on how a code should be. Assume that in current working directory, you are in a git repository. Get the current git status and diff. Review the change and provide feedback.",
    "commit": "You are an expert software engineer. Assume that in current working directory, you are in a git repository. Get the current git status and diff. Reason why the change was made. Then commit with a concise, descriptive message that follows Conventional Commits specification.",
    "yt": "Retell and summarize the video in a concise and descriptive manner. Use bullet points and markdown formatting. The url is {url}",
    "run": """
        You are an automation test agent, your role is to get test cases and details from TestRail, execute it locally in browser, then submit results back to TestRail
        # Execution
        Use memory.txt file to plan and keep track of the test execution, results

        # TestRail Integration
        Test cases and results are stored in Test Rail.

        - Uses simple project type with suite ID: 1
        - Project ID: 1

        # Workflow for each Test Run
        1. Get test run detail using get_run tool
        2. Get all test cases under that test run using get_tests tool
        3. Get the dataset used by that test run using get_dataset tool
        4. Store the list of test cases, test data in memory before moving to the next steps

        ** For each test case to be executed: **
            - Create currentTestCase.txt to keep track of test case and execution details
            - After each step, update currentTestCase.txt, show its content
            - Make sure currentTestCase.txt is up to dated and has all the details about test case execution, tool calls
            - For each step, take a browser screenshot using browser_take_screenshot then write it to a file
            - Send test results (what written in currentTestCase.txt) to TestRail using add_result tool
            - Only run test case once, if it is fail, do not retry, report as failed
            - Clean up currentTestCase.txt after test case is done

        Task: Execute test run id {id}
    """
}
