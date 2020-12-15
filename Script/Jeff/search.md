
# Splunk Rule
windows host="labuser-pc" source="wineventlog:security" EventCode= "4740"

# SNORT Rule
 alert tcp $EXTERNAL_NET any -> $HOME_NET 135 (msg:"Possible SMB brute forcing!"; flags: S+; threshold: type both, track by_src, count 5, seconds 30; sid:10000001; rev: 1;)