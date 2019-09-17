from models import *

PATIENTS_FIELDS =\
[
    dict(
        key=f'{Patients.__tablename__}_id',
        label='Id пациента',
    ),
    dict(
        key=f'{Patients.__tablename__}_patient_first_name',
        label='Фамилия',
        sortable=True,

    ),
    dict(
        key=f'{Patients.__tablename__}_patient_sur_name',
        label='Имя',
        sortable=True,

    ),
    dict(
        key=f'{Patients.__tablename__}_patient_age',
        label='Возраст',
        sortable=True,

    ),
]

CONSULTANTS_FIELDS=\
[
            dict(
                key='value',
                label='Id консультанта',
            ),
            dict(
                key='text',
                label='Фамилия',
                sortable=True,

            ),
        ]

DEPARTMENTS_FIELDS =\
[
            dict(
                key='value',
                label='Id отделения',
            ),
            dict(
                key='text',
                label='Название',

            ),
        ]

DIAGNOSES_FIELDS =\
[
            dict(
                key=f'{Diagnoses.__tablename__}_id',
                label='Id диагноза',
            ),
            dict(
                key=f'{Diagnoses.__tablename__}_diagnose_name',
                label='Название',
                sortable=True,

            ),
        ]

SICKLIST_FIELDS =\
[
            dict(
                key=f'{SickLists.__tablename__}_id',
                label='Id',
            ),
            dict(
                key=f'{SickLists.__tablename__}_sl_date',
                label='   Дата   ',
                sortable=True,

            ),
            dict(
                key=f'{Consultants.__tablename__}_consultant_name',
                label='Консультант',
                sortable=True,

            ),
            dict(
                key=f'{SickLists.__tablename__}_number_of_sl',
                label='#',
                sortable=True,

            ),
            dict(
                key=f'{SickLists.__tablename__}_number_of_consultation',
                label='№',
                sortable=True,

            ),
            dict(
                key=f'{Patients.__tablename__}_patient_sur_name',
                label='Пациент',
                sortable=True,

            ),
            dict(
                key=f'{SickLists.__tablename__}_correction',
                label='Коррекция',
                sortable=True,

            ),
            dict(
                key=f'{Departments.__tablename__}_department_name',
                label='Отделение',
                sortable=True,

            ),
            dict(
                key=f'{Diagnoses.__tablename__}_diagnose_name',
                label='Диагноз',
                sortable=True,

            ),
            dict(
                key=f'{Reasons.__tablename__}_reason_name',
                label='Причина',
                sortable=True,

            ),
            dict(
                key=f'{SickLists.__tablename__}_comment',
                label='Комментарий',
                sortable=True,

            ),
        ]