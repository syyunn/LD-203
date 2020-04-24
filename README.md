# LD-203

## Goal 
Collect/Parse/Build Lobbying Contribution table on current lobby_database with proper relational linkage which enables uniquely identification of lobbyists and PAC's senate/house ID

## Reference Database Url
[Lobbying Contribution Database (hosted on ***house.gov***)](https://disclosurespreview.house.gov/?index=%22lobbying-contributions%22&size=10&sort=[{%22_score%22:true},{%22field%22:%22organizationName%22,%22order%22:%22asc%22}])

### Required Knowledge to Understand the Data
####  Related Forms
##### LDs
- LD-1 : First registration of lobbyists/registrants

- LD-2 : Regular Reporting Form

    - Either one of LD-1 or LD-2 must be preceded before filing the first LD-203 report.

    - Lobbyist ID numbers, like the registrant ID number, is unique to each individual lobbyist and will stay assigned to that lobbyist though they become employed by another registrants.

### Data Attributes(Columns)
    filerType: { "O", "L" }
    organizationName: str
    _lobbyistName:
        lobbyistPrefix
        lobbyistFirstName
        lobbyistMiddleName
        lobbyistLastName
        lobbyistSuffix
    zipext
    contactName
    senateRegID
    houseRegID
    reportYear
    reportType
    amendment
    comments
    signedDate
    certifiedcontent
    noContributions
    pacs
    contributions

### Data Constraints
1. There's no lobbyist name if filerType is "O"
```python
    if filerType == "L":
        lobbyistName is not None
    elif filerType == "O:
        lobbyistName is None
```

2. senateRegID & houseRegID are Organization's, not Lobbyist's (even if filerType = "L")

