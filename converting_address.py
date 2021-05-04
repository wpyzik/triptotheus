path = 'C:\\Users\\weronika\\Desktop\\coding\\wycieczka\\stronka\\static\\images\\'
file=open(path, "r")

rename= pandas.open('C:\\Users\\weronika\\Desktop\\coding\\wycieczka\\stronka\\static\\images\\images1')
for i in enumerate(rename):
    if table['lon'].isnull().values[i]:
        name=table["addresses"][i]
    else:
        pass
table.to_csv("miejsca.csv")
