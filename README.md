# slackPurge
Fixes free slack to stop it overrunning file limits.

## Use

### Get a slack api token
Legacy tokens will work fine:   
 https://api.slack.com/custom-integrations/legacy-tokens  
Or an app token:   
 https://api.slack.com/slack-apps  

### Put it in an environment variable
```
export SLACK_TOKEN=yourslacktokenhere
```

### Configure days_old
This variable in the code specifies how stale files should be before deletion.

### Put it in a Crontab
Call purgeSlack.py in a crontab nightly.
