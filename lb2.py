import matplotlib.pyplot as plt
import pandas as pd
import csv
from datetime import datetime


filename = 'country_vaccinations.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for i, column_header in enumerate(header_row):
        print(i, column_header)

    daily_vac, daily_vac_r, dates, vac, num_vac = [], [], [], [], []
    for row in reader:
        if row[0] == 'Italy':
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            dates.append(current_date)
            if row[7] == '':
                daily_vac.append(0)
            else:
                daily_vac.append(float(row[7])/1)
            if row[6] == '':
                daily_vac_r.append(0)
            else:
                daily_vac_r.append(float(row[6])/1)
        for el in row[12].split(','):
            for elem in el.split('/'):
                nelem = elem.replace(' ', '')
                if nelem not in vac:
                    vac.append(nelem)
                    num_vac.append(1)
                else:
                    ind = vac.index(nelem)
                    num_vac[ind] += 1


fig = plt.figure()
plt.plot(dates, daily_vac, c='red')
plt.plot(dates, daily_vac_r, c='blue')

plt.title('Number of daily vaccinations in Italy', fontsize=20)
fig.autofmt_xdate()
plt.ylabel('Number of vaccinations', fontsize=10)


fig=plt.figure()
ax=fig.add_axes([0 ,0 ,1 ,1 ])
ax.axis('equal')
explode = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
ax.pie(num_vac, labels=vac, autopct='%1.2f%%', explode=explode, shadow=True, wedgeprops={ 'edgecolor':'k'})
plt.title('Popularity of vaccines', fontsize=20)

plt.show()