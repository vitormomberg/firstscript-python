import json

def formatRow(row={}, prefixToOverwrite=None, keyArray=None, keyItem=None, keyValueItem=None):
  
  if(not len(row.items())): 
    return None

  rowFormatted = {
    keyArray: []
  }

  for key, value in row.items():
    keyLower = key.lower()
    prefixToOverwriteLower = prefixToOverwrite.lower()

    if (prefixToOverwriteLower in keyLower):
      keyFormatted = keyLower.replace(prefixToOverwriteLower, '')

      rowFormatted[keyArray].append({
        keyItem: keyFormatted,
        keyValueItem: value
      })
    else:
      rowFormatted[keyLower] = value

  print(json.dumps(rowFormatted))
  return rowFormatted

row = {
  "id": '123',
  "FIRSTNAME": 'Vitor',
  "LASTNAME": 'Momberg',
  "PRODUTO-X": "X-123",
  "produto-Y": "Y-123",
  "produto-Z": "Z-123"
}

prefixToOverwrite = 'produto-'
keyArray = 'produtos'
keyItem = 'nome-produto'
keyValueItem = 'value-produto'

formatRow(
  row=row,
  prefixToOverwrite=prefixToOverwrite,
  keyArray=keyArray,
  keyItem=keyItem,
  keyValueItem=keyValueItem
)

archivesNamesToFormat = ['teste1.csv', 'teste2.csv']

print('teste1.csv' in archivesNamesToFormat)