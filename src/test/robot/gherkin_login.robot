*** Settings ***
Documentation       Test for launching URL
Resource            resource.robot

*** Test Cases ***
Valid Login
    Open browser to login page
    [Teardown]    Close Browser

