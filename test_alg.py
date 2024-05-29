matrix = {'V1': {'V6', 'V7', 'V8'},
          'V2': {'V5', 'V7', 'V8'},
          'V3': {'V5', 'V6', 'V8'},
          'V4': {'V5', 'V6', 'V7'},
          'V5': {'V2', 'V3', 'V4'},
          'V6': {'V1', 'V3', 'V4'},
          'V7': {'V1', 'V2', 'V4'},
          'V8': {'V1', 'V2', 'V3'}
          }


all_graphs = set(matrix.keys())
temp_graphs = set()
vivod = {'V1'}
proverka = all_graphs - matrix['V1'] - {'V1'}
temp_graphs.update(matrix['V1'])
print(proverka)
for ver in proverka:
    pass