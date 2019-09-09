from sqlalchemy.orm import sessionmaker
from models import engine, Consultants, Departments, Diagnoses, Patients, SickLists, Reasons

import pandas as pd
import datetime

Session = sessionmaker(bind=engine)
session = Session()

df = pd.read_excel('./data.xlsx')

# add consultant
for n, item in enumerate(set(df['Консультант'])):
    session.add(Consultants(consultant_name=item, consultant_password=str(n)))

for n, item in enumerate(set(df['Отделение'])):
    session.add(Departments(department_name=item))

for n, item in enumerate(set(df['Диагноз'].append(df['Причина']))):
    session.add(Diagnoses(diagnose_name=item))

for n, item in enumerate(set(df['Диагноз'].append(df['Причина']))):
    session.add(Reasons(reason_name=item))


for item in df[['Имя больного', 'Возраст']].drop_duplicates().itertuples():
    session.add(Patients(patient_sur_name=item[1],
                         patient_age=item[2]))

session.commit()

df = pd.read_excel('./data.xlsx')
for item in df.iterrows():
    try:
        session.add(SickLists(
            sl_date=datetime.datetime.strptime(item[1][1], '%d.%m.%Y'),
            consultant_id=session.execute(session.query(Consultants.id).filter_by(consultant_name=item[1][0])).fetchone()[0],
            number_of_sl=item[1][2],
            number_of_consultation=item[1][3],
            patient_id=session.execute(session.query(Patients.id).filter_by(patient_sur_name=item[1][4])).fetchone()[0],
            correction=1 if item[1][6] == 'Частичная' else 0,
            department_id=session.execute(session.query(Departments.id).filter_by(department_name=item[1][7])).fetchone()[0],
            diagnose_id=session.execute(session.query(Diagnoses.id).filter_by(diagnose_name=item[1][8])).fetchone()[0],
            reason_id=session.execute(session.query(Diagnoses.id).filter_by(diagnose_name=item[1][9])).fetchone()[0],
            comment=item[1][10]))
    except Exception as err:
        print(err)

session.commit()


