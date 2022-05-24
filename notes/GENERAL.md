### File Verification
- Might be useful to have a way for others to verify that the input files we use match ones they can get from public data
- Checksum might work, but doesn't allow flexibility in minor data transformations (like changing column names, normalizing data etc)

### File organization
- How do we want to order rows? Date of incident? Incident number? By officer?
- For records with multiple officers (eg: Stops), do we want to append all officer info to the same record, or expand vertically (create an additional record for the second officer)
- Datatypes: do we want to format numbers in a certain way?

### Stops
- Stops file doesn't have an id column. Need to add one before merging
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
- The `time` column is scalar, and probably represents the hour of the day (in 24 hr format)
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
