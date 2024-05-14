*** Settings ***
Documentation       Test for launching URL
Resource            resource.robot
Resource            keywords.robot
Test Teardown       Close Browser

*** Test Cases ***
Valid Login
    Open browser to login page

