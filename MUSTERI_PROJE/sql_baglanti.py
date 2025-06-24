import pypyodbc

db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=.;'
    'Database=MUSTERI_TAKIP_SISTEMI;'
    'Trusted_Connection=True;'
)
cursor = db.cursor()

