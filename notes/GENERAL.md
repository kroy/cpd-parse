### File Verification
- Might be useful to have a way for others to verify that the input files we use match ones they can get from public data
- Checksum might work, but doesn't allow flexibility in minor data transformations (like changing column names, normalizing data etc)

### File organization
- How do we want to order rows? Date of incident? Incident number? By officer?
- For rows/records with multiple officers (eg: Stops), do we want to append all officer info to the same record, or expand vertically (create an additional record for the second officer)
- Datatypes: do we want to format numbers in a certain way?

### Issues w/ Names
- What happens when a female officer gets married and changes her last name? a potential example is:
```
---- In officer_profile
"26063","DAISY","ROMERO","","","",1990,"HISPANIC","FEMALE","8/31/15",""
---- In UOF file
10510,2017-00381,2017-11-12 10:09:00,71XX EMERALD AVE,19562711,DAISY,CRUZ,7,,502.0,125.0,FEMALE,HISPANIC,1990.0,723,True,True,FEMALE,BLACK,2000.0,2017-11-12,10,,,,,,,,,,,,,,,,,
```
- We might need to fuzz names at times, especially in cases such as O'Brien or O Boyle, where the name might appear with or without an apostrophe etc
- Sometimes, such as in the UOF data, suffixes are appended to the last name

### Arrests
- Officer data in this file is a little more sparse than others. Will probably need to use a number of tricks to 
- Looks like officers involved in a number of arrests are duplicated by `fbi_code`. EG:
```
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,ROBERT,FARANO,18799,04A,720 ILCS 5.0/12-2-C-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,MARK,SHARKS,18687,04A,720 ILCS 5.0/12-2-C-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,First Arresting Officer,RICHARD,MOSTOWSKI,12898,04A,720 ILCS 5.0/12-2-C-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Second Arresting Officer,DARNELL,MAGNY,12870,04A,720 ILCS 5.0/12-2-C-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,JUSTIN,PETERS,10103,04A,720 ILCS 5.0/12-2-C-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,ROBERT,FARANO,18799,26,720 ILCS 5.0/19-4-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,MARK,SHARKS,18687,26,720 ILCS 5.0/19-4-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,First Arresting Officer,RICHARD,MOSTOWSKI,12898,26,720 ILCS 5.0/19-4-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Second Arresting Officer,DARNELL,MAGNY,12870,26,720 ILCS 5.0/19-4-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,JUSTIN,PETERS,10103,26,720 ILCS 5.0/19-4-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,ROBERT,FARANO,18799,08B,720 ILCS 5.0/12-3.2-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,MARK,SHARKS,18687,08B,720 ILCS 5.0/12-3.2-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,First Arresting Officer,RICHARD,MOSTOWSKI,12898,08B,720 ILCS 5.0/12-3.2-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Second Arresting Officer,DARNELL,MAGNY,12870,08B,720 ILCS 5.0/12-3.2-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,JUSTIN,PETERS,10103,08B,720 ILCS 5.0/12-3.2-A-1,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,ROBERT,FARANO,18799,WRT,725 ILCS 5.0/110-3,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,MARK,SHARKS,18687,WRT,725 ILCS 5.0/110-3,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,First Arresting Officer,RICHARD,MOSTOWSKI,12898,WRT,725 ILCS 5.0/110-3,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Second Arresting Officer,DARNELL,MAGNY,12870,WRT,725 ILCS 5.0/110-3,MALE,BLACK,21
2020-12-25T19:09:00Z,19,2020-12-25,65XX S DR MARTIN LUTHER KING JR DR,Assisting Arresting Officer,JUSTIN,PETERS,10103,WRT,725 ILCS 5.0/110-3,MALE,BLACK,21
```
- Can we dedupe over `fbi_code` for a given arrest incident?
- What is `fbi_code`? Is it [UCR Code](https://ucr.fbi.gov/nibrs/2011/resources/nibrs-offense-codes/at_download/file)
  - More likely this one [CPD crime details](https://gis.chicagopolice.org/pages/crime_details)
- How do we identify an "arrest incident"?

### Stops
- Stops file doesn't have an id column. Need to add one before merging
- Each stop might have multiple entries, one for each person stopped, eg:
```
2012-01-01T00:08:00Z,31XX LAWRENCE AVE,17,1713,Dispersal,BARNETT,THOMAS,M,WHITE,34,PRINTZ,DANIEL,M,WHITE,48,M,HISPANIC,18,2012-01-01,0,NA,NA,NA,NA,NA
2012-01-01T00:08:00Z,31XX LAWRENCE AVE,17,1713,Dispersal,BARNETT,THOMAS,M,WHITE,34,PRINTZ,DANIEL,M,WHITE,48,M,HISPANIC,26,2012-01-01,0,NA,NA,NA,NA,NA
2012-01-01T00:08:00Z,31XX LAWRENCE AVE,17,1713,Dispersal,BARNETT,THOMAS,M,WHITE,34,PRINTZ,DANIEL,M,WHITE,48,M,HISPANIC,25,2012-01-01,0,NA,NA,NA,NA,NA
```
- Stop types:
  - Gang / Narcotics Related
  - Suspicious Person
  - Disperal
  - Traffic Related
  - Other
- The issue w/ the second officer fields is that, for our first pass, we can't just drop rows with missing second officer fields, cause there might have just been one officer involved
  - We can either select out records with second-officer fields, apply the same filters to them as we do for the first officer, then merge them back into the original dataframe
  - or we can expand out the data to be more like the uof data, meaning a record per officer involved, but we need to indicate what precedent they were in the original data. This is more flexible, but feels like it's a bit too complicated/we're mangling the data a bit

### Use of Force
- The first UOF record w/ an officer name attached seems to be around 10192 (record number 10191), which occured on `2017-10-16`
  -  Related to John Gianopulos, born 1971, started on the force 9/11/2000
- First-pass filter seems like it should be `[off_first_name, off_last_name, off_race, off_sex, off_birth_year]`
- Multiple officers involved in (what seem to be) the same use of force incident are included in separate rows. eg:
```
"10192","2017-00001",2017-10-16 10:47:00,"31XX HARRISON ST","19550791","DANIELLE","FERLITO",313,NA,506,135,"F","WHITE",1986,"6730c",TRUE,FALSE,"MALE","BLACK",1998,2017-10-16,10,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
...
"10194","2017-00003",2017-10-16 10:47:00,"31XX HARRISON ST","19550791","JOSEPH","DEROSA",313,NA,511,250,"M","WHITE",1983,"6730G",TRUE,FALSE,"MALE","BLACK",1998,2017-10-16,10,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
"10195","2017-00006",2017-10-16 10:47:00,"31XX HARRISON ST","19550791","NICK","BECKMAN",313,NA,509,185,"M","WHITE",1980,"6730E",TRUE,FALSE,"MALE","BLACK",1998,2017-10-16,10,NA,NA,NA,NA,NA,NA,NA,NA,NA,NA
```
- The `off_assigned_beat` column is interesting. In the multi-officer example of uof at 31xx Harrison St, which appears to be [here](https://goo.gl/maps/jZxTn3fzdDqZKecP6) and is in the [11th District 1134 Beat](https://chicagopolicedept-my.sharepoint.com/personal/gisteam_chicagopolice_org/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fgisteam%5Fchicagopolice%5Forg%2FDocuments%2FDistrict%20PDFs%2Fdistrict11%2Epdf&parent=%2Fpersonal%2Fgisteam%5Fchicagopolice%5Forg%2FDocuments%2FDistrict%20PDFs&ga=1), the officers involved were assigned the beat `6730`. I haven't found a corresponding beat for `6730`.
  - More generally, an officer can be assigned a beat and use force in a different beat's area, or not assigned any beat (because they're off duty or something similar), or can be assigned a beat not tied to a specific geographic area.
