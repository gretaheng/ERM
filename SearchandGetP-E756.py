from bookops_worldcat import WorldcatAccessToken
import pandas as pd
from bookops_worldcat import MetadataSession
import json
import sys


f=open("credential.txt.txt","r")
lines=f.readlines()
clientID=lines[0]
secret=lines[1]
principal_id=lines[2]
principal_idns=lines[3]
f.close()
problem_l = []
error_l=[]
d = {}

with open('credential.txt') as f:
    for line in f:
        content = line.strip().split("=")[1].strip()
        lead = line.strip().split("=")[0].strip()
        if 'client_ID' in lead:
            clientID = content
        elif 'secret' in lead:
            secret = content
        elif 'principal_id' in lead:
            principal_id = content
        elif 'principal_idns' in lead:
            principal_idns = content

def search_go(poclctxt):
    if clientID == '' or secret == '' or principal_id == '' or principal_idns == '':
        print("Please fill out information in the credential.txt first.")
        return
    else:
        df = open('finalp-e.txt', 'w')
        df.write("pnumber,enumber\n")
        poclcall = open(poclctxt, "r")
        data = poclcall.read()
        ponel = data.replace('\n', ' ').split(".")
        poclcall.close()
        pbigl = [ponel[x:x+100] for x in range(0, len(ponel),100)]
        for i in pbigl:
            token = WorldcatAccessToken(
                key = clientID,
                secret = secret,
                scopes=["wcapi", "WorldCatMetadataAPI"],
                principal_id= principal_id,
                principal_idns= principal_idns
            )
            session = MetadataSession(authorization=token)
            for p in i:
                print("working on ", p)
                results = session.get_full_bib(p)
                tree = ET.fromstring(results.text)
                if tree.find(".//*[@tag='776']"):
                    f776 = tree.find(".//*[@tag='776']")
                    if not f776.find(".//*[@code='w']"):
                        eoclcnum = f776.find(".//*[@code='w']").text.strip("(OCoLC)").strip()
                        if p not in d:
                            d[p] = eoclcnum
                            print("matched")
                            dfline = p+","+eoclcnum + "\n"
                            df.write(dfline)
                    else:
                        print(p, "+++")
                        for child in f776:
                            print(child.text)
                        print("problem found")
                        problem_l.append(p)
                else:
                    print("not matched")
                    error_l.append(p)
                print("********************")
        df.close()
    with open(r'problem_p_oclc.txt', 'w') as fp:
        for item in problem_l:
            # write each item on a new line
            fp.write("%s\n" % item)
    with open(r'error_p_oclc.txt', 'w') as fp1:
        for item1 in error_l:
            # write each item on a new line
            fp1.write("%s\n" % item1)
    return

if __name__ == "__main__":
    search_go(sys.argv[1])
