from countrycode import countrycode

def test_default():
    assert countrycode() == ['ALGERIA', 'CANADA']

def test_cown_iso3c():
    assert countrycode(codes=['666', '31'], origin='cown', target='iso3c') == ['ISR', 'BHS']

def test_cn_iso3c():
    assert countrycode(['United States', 'India', 'Canada', 'Dem. Repu. Congo'], 
            'country_name', 'iso3c') == ['USA', 'IND', 'CAN', 'COD']

def test_iso3c_cn_single():
    assert countrycode('DZA', 'iso3c', 'country_name') == 'ALGERIA'

print countrycode('georgia', 'country_name', 'country_name')
print countrycode('south georgia', 'country_name', 'country_name')
print countrycode('serbia', 'country_name', 'country_name')
print countrycode('serbia and montenegro', 'country_name', 'country_name')
print countrycode('st. kitts and nevis', 'country_name', 'country_name')
print countrycode('st. christopher and nevis', 'country_name', 'country_name')
print countrycode('st. maarten', 'country_name', 'country_name')
print countrycode('sint maarten', 'country_name', 'country_name')
print countrycode('saint maarten', 'country_name', 'country_name')
print countrycode('south korea', 'country_name', 'country_name')
print countrycode('guinea', 'country_name', 'country_name')
print countrycode('guinea bissau', 'country_name', 'country_name')
print countrycode('equatorial guinea', 'country_name', 'country_name')
print countrycode('niger', 'country_name', 'country_name')
print countrycode('nigeria', 'country_name', 'country_name')
print countrycode('west bank', 'country_name', 'country_name')
print countrycode('korea', 'country_name', 'country_name')
print countrycode('korea, dem. rep.', 'country_name', 'country_name')
