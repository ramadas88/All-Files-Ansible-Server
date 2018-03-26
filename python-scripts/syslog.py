

import syslog
syslog.openlog("TEST")
syslog.syslog(syslog.LOG_NOTICE, "No nonsense found.")
syslog.closelog()
