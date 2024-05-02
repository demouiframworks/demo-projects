*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${BROWSER}  CHROME
${URL}      https://www.saucedemo.com/
${DELAY}    30

*** Keywords ***
Open browser to login page
    open browser    ${URL}      ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

