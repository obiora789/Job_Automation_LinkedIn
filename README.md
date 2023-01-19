<h1>Job Automation</h1>
A bot that automates job application processes on LinkedIn.<br>

This code uses Selenium to drive a bot that automates job application processes on LinkedIn<br>

<h2>Requirements</h2>
<ul>
  <li>Python 3.8 or higher.</li>
  <li>Selenium Webdriver(Chrome)</li>
  <li>Install and import Selenium Web driver.</li>
</ul>
<hr>
<h3>What to do</h3>
<ol>
  <li>Fork this Git and clone to your local PC.</li>
  <li>Download the webdriver for your browser(I use Chrome).</li>
  <li>Copy the path of the Chrome Webdriver and save it as an environment variable.</li>
  <li>Populate the environment variable with the actual path of your Webdriver.</li>
  <li>Please select "Easy Apply" option when filtering your job search to ensure all the application is done on LinkedIn</li>
  <li>Add the url link as an environment variable</li>
  <li>Also, set your LinkedIn login details (Username and Password) as separate environment variables</li>
  <ul>
    <li>CHROME_PATH=pathToChromeDriverOnYourPC</li>
    <li>LINKEDIN_URL=urllinkContainingAllJobSearchCriteria</li>
    <li>EMAIL=linkedInUsername</li>
    <li>PASSWORD=linkedInPassword</li>
    <li>MOBILE_NUMBER=mobileNumber</li>
  </ul>
  <li>That's all you need to do for now.</li>
</ol>
<p>Simply put, complex applications involving multiple stages (beyond the first 3 stages) are ignored and the bot exits the job application process which takes it back to the list of available jobs to allow the bot apply for other simpler ones.</p>
<hr>
<h3>Results</h3>
<img src="https://raw.githubusercontent.com/obiora789/Portfolio/obiora789-patch-1/bot2.jpg" alt="listOfAvailableJobs.jpg">
<img src="https://raw.githubusercontent.com/obiora789/Portfolio/obiora789-patch-1/bot.jpg" alt="successfulApplication.jpg">
<img src="https://raw.githubusercontent.com/obiora789/Portfolio/obiora789-patch-1/bot3.jpg" alt="unsuccessfulApplication.jpg">

<hr>
<h3>Bugs</h3>
<p>None as at the time of this report.</p>
