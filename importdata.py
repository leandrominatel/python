from sqlite3 import *

def convert(value):
	if value.startswith('~'):
		return value.strip('~')
	if not value:
		value = '0'
	return float(value)
	
conn = connect('food.db')
curs = conn.cursor()
curs.execute('''
	CREATE TABLE food (
	id TEXT PRIMARY KEY,
	desc TEXT,
	water FLOAT,
	kcal FLOAT,
	protein FLOAT,
	fat FLOAT,
	ash FLOAT,
	carbs FLOAT,
	fiber FLOAT,
	sugar FLOAT,
	calcium FLOAT,
	iron FLOAT,
	magnesium FLOAT,
	phosphorous FLOAT,
	potassium FLOAT,
	sodium FLOAT,
	zinc FLOAT,
	copper FLOAT,
	manganese FLOAT,
	selenium FLOAT,
	vit_c FLOAT,
	thiamin FLOAT,
	riboflavin FLOAT,
	niacin FLOAT,
	panto_acid FLOAT,
	vit_b6 FLOAT,
	folate_tot FLOAT,
	folic_acid FLOAT,
	food_folate FLOAT,
	folate_DFE FLOAT,
	vit_b12 FLOAT,
	vit_a_iu FLOAT,
	vit_a_rae FLOAT,
	retinol FLOAT,
	vit_e FLOAT,
	vit_k FLOAT,
	alpha_carot FLOAT,
	beta_cartot FLOAT,
	beta_crypt FLOAT,
	lycopene FLOAT,
	lut_zea FLOAT,
	fa_sat FLOAT,
	fa_mono FLOAT,
	fa_poly FLOAT,
	cholestr FLOAT,
	gmwt_1 FLOAT,
	gmwt_desc1 TEXT,
	gmwt2_2 FLOAT,
	gmwt2_desc2 TEXT,
	refuse_pct FLOAT
	)
''')

field_count = 50
markers = ', '.join(['?']*field_count)
query = 'INSERT INTO food VALUES (%s)' % markers
for line in open('ABBREV.txt'):
	fields = line.split('^')
	vals = [convert(f) for f in fields[:field_count]]
	print query
	print vals
	curs.execute(query, vals)
	
conn.commit()
conn.close()
