Are you tired of continuously going to the AI course page (taught by Soumajit Sir) and checking for the slides to download? then fear not, here is the automated slides downloader which downloads all the slides as they are uploaded so your time is lot more optimized!

So, to run this just download the "scrapey.py" and then follow this:
In Linux Systems with crontab:
 1. Open your terminal.
 2. Enter the command `crontab -e` to open your user's crontab configuration.
 3. Add the following line to the crontab file to run your Python script every hour:
 
	`0 * * * * /usr/bin/python3 /path/to/your/script.py`<br>
			  (Replace `/path/to/your/script.py` with the actual path to your Python script)<br>
If you are a windows user, you have two options:
	1. Get a Linux distro.
	2. Forget this.

JK, just follow this link: [Python Script Automation Using Task Scheduler (Windows) - JC Chouinard](https://www.jcchouinard.com/python-automation-using-task-scheduler/)
