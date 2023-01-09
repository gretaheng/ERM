# WorldCat_Metadata_API

This python script can search a physical bib record's electronic version's OCLC number that is included in 756 field. For example:

```
776 08 ǂi Online version: ǂa Staubus, George J. ǂt Theory of accounting to investors. ǂd Houston : Scholars Book Co., 1971 ǂw (OCoLC)776097868
```


* You need to request a WorldCat Metadata API. Once confirmed by OCLC, you will receive an email containing your institution's registry ID, your principal ID, and your principal IDNS.
* Log into OCLC WSKey management page (https://platform.worldcat.org/wskey/). See if you have an active WorldCat Metadata API. Click on the API. Client ID and Secret will be needed in the steps below
* Download the repository. Open the credential.txt and fill in clientID, secret, principal_id, and principal_idns
* Run the python code by putting the following line in the command line: python [path to SearchandGetP-E756.py] [path to the credential.txt] 
* The python script will return 
    * a comma-seperated "finalp-e.txt" (physical oclc and its corresponding electronic oclc)
    * Two txt files, 'problem_p_oclc.txt' and 'error_p_oclc.txt'. Those two files include physical oclc numbers that do not have electronic oclc number in the 756 field.
