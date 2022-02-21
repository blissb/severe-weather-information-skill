'''
List of service for Severe Weather Information skill

taken from following resources as of 2019-08-13:
https://severeweather.wmo.int/v2/sources.html
https://alerting.worldweather.org/atom.xml
http://meteoalarm.eu/ATOM/root.xml

Some services were excluded for one or more of the following reasons:
- providing test information only
- use not properly signed certificates
- send bogus http responses
- return malformed RSS, AtomPub or CAP data
- last entry is older than one year
- does not work at all
'''

SWI_SERVICES = {

    # USA original url value: https://alerts.weather.gov/cap/us.php?x=0 new url value:https://alerts.weather.gov/cap/wwaatmget.php?x=VTC023&y=1
    # US1 updated to only my area since nothing else seemed to work...
    'US1:en': {'country': 'USA', 'lang': 'en', 'title': 'USA - United States of America (en)', 'url': 'https://alerts.weather.gov/cap/wwaatmget.php?x=VTC023&y=0', 'hdr_feed': {'Accept': 'application/atom+xml'}, 'hdr_atom': {'Accept': 'application/cap+xml'}},
    'US2:en': {'country': 'USA', 'lang': 'en', 'title': 'USA - USGS Volcano (en)', 'url': 'https://volcanoes.usgs.gov/hans2/cap/rss/', 'hdr_feed': {'Accept': 'application/atom+xml'}, 'hdr_atom': {'Accept': 'application/cap+xml'}},
    'US3:en': {'country': 'USA', 'lang': 'en', 'title': 'USA - USGS Volcano (en)', 'url': 'http://feeds.enviroflash.info/cap/aggregate.xml', 'hdr_feed': {'Accept': 'application/atom+xml'}, 'hdr_atom': {'Accept': 'application/cap+xml'}},

    # ZZZ Custom
    'ZZZ:zz': {'country': 'ZZ', 'lang': 'zz', 'title': 'Custom configuration', 'url': 'custom', 'hdr_feed': '', 'hdr_atom': ''}
}
