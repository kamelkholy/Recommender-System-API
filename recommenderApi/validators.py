def validateAge(age):
    return age if age.isnumeric() else ''
def validateGender(gender, mapping_dict):
    return gender if gender in mapping_dict['sexo'].keys() else ''
def validateCountry(country, mapping_dict):
    return country if country in mapping_dict['pais_residencia'].keys() else ''
def validateSeniority(seniority):
    return seniority if isfloat(seniority) else ''
def validateActiveLevel(level, mapping_dict):
    return level if level in mapping_dict['ind_actividad_cliente'].keys() else ''
def validateSegment(segment, mapping_dict):
    return segment if segment in mapping_dict['segmento'].keys() else ''
def validateIncome(income):
    return income if isfloat(income) else ''  
def validateRelationship(relation, mapping_dict):
    return relation if relation in mapping_dict['tiprel_1mes'].keys() else ''
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

