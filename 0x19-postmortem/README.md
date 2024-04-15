## Issue Summary
Apr 9, 2024 5:00 AM EET, the apache server running wordpress website started responding with a 500 internal server error, it was affecting 100% of the users querying any page in the server.
the reason was that there was a typo in the last deployment, resulting to a runtime error while running the php code in the server. and the problem was solved after 6 hours of the notification.

## Timeline
Apr 9, 2024 05:00 AM EET - The issue was send to the intranet.  
Apr 9, 2024 10:00 AM EET - A customer complained they are not able to visit the website
Apr 9, 2024 10:30 AM EET - Dev X strated by running the php scripts at the server, assuming it is the root cause
Apr 9, 2024 10:40 AM EET - There was a typo in a file import statement, the Dev Y typed file.phpp instead of file.php
Apr 9, 2024 10:50 AM EET - Dev X resolved the issue completily

## Preventative Measures
In order to prevent facing the same issue in the future, we made a Puppet manifest that correct such typos in all the php files, this file could be run before any deployment to make sure it is typo free.
