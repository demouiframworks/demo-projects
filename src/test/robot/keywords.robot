*** Settings ***
Library         SeleniumLibrary
Resource        variables.resource

*** Keywords ***
Open browser to login page
    open browser    ${URL}      ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}