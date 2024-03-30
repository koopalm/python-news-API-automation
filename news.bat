@echo off
rem Change directory to where your Python script for news_automator is located relative to your home directory and save this 'news.bat' file to your home directory
cd "Code\python-news-API-automation"

rem Execute Python script with command-line argument
python news_automator.py %1
