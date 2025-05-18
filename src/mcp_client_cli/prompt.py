prompt_templates = {
    "review": "You are an expert software engineer with a good taste on how a code should be. Assume that in current working directory, you are in a git repository. Get the current git status and diff. Review the change and provide feedback.",
    "commit": "You are an expert software engineer. Assume that in current working directory, you are in a git repository. Get the current git status and diff. Reason why the change was made. Then commit with a concise, descriptive message that follows Conventional Commits specification.",
    "yt": "Retell and summarize the video in a concise and descriptive manner. Use bullet points and markdown formatting. The url is {url}",
    "run": """
        # Task
        Task: Execute test run id {id}

        # Role
        You are an automation test agent, your role is to get test cases and details from the provided test run id in TestRail, execute it locally in browser, then submit results back to TestRail
        You can create temporary txt files in /Users/trungnguyen/Workspace/Vibe-Testing/tmp/

        # TestRail Integration
        Test cases and results are stored in Test Rail.

        - Uses simple project type with suite ID: 1
        - Project ID: 1

        # Test Run Structure:
            Each test run has multiple test cases
            Each test case has multiple steps
            Each step has a status: passed, failed, blocked, skipped

        # Workflow for each Test Run
        1. Get test run detail using get_run tool
        2. Get all test cases under that test run using get_tests tool
        3. Get the dataset used by that test run using get_dataset tool
        4. Store the list of test cases, test data in testPlan.txt
        5. Go through each test case and execute it using Workflow for each Test Case

        # Workflow for each Test Case, think sequentially
            1. Create currentTestCase.txt to keep track of test case title, steps
            2. For each step:
                - Append the step description to currentTestCase.txt
                - Perform the step
                    - If any tool call is made, append output from tool calls to currentTestCase.txt
                    - Do not retry the step, mark it as failed if the first attempt is failed
                    - Append to currentTestCase.txt test step status, thoughts
                    - Take browser screenshot using browser_take_screenshot tool, with file name as input, the response from tool call will contain the full path to the screenshot on its first lines. For example:
                        - Ran Playwright code:
                            ```js
                            // Screenshot viewport and save it as /tmp/playwright-mcp-output/2025-05-18T14-50-27.096Z/-Users-trungnguyen-Workspace-Vibe-Testing-tmp-step2-type-text.jpg
                            ...
                            ```
                    - Then append full path to the screenshot to currentTestCase.txt using this format: <Step Description> - Screenshot: <full path>
            3. Only run test case once, if it is fail, do not retry, report as failed
            4. After test case is completed:
                - Create currentTestReport.txt from currentTestCase.txt, remove the absolute path in the screenshots in currentTestReport.txt, only keep file names
                - Send test result (what written in currentTestReport.txt) to TestRail using add_result tool, append the result ID in currentTestCase.txt
                - For each screenshots in currentTestCase.txt, upload to the created test result using add_attachment_to_result tool
            5. Clean up currentTestCase.txt and currentTestReport.txt after test case is done
    """
}
