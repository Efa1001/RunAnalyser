def pace_to_minutes(pace):
 mins,secs = pace.split(':')
 return int(mins)+int(secs)/60

def group_by(column):
  totals = {}
  counts = {}

  for line in lines[1:]:
    if line == '':
      continue
    parts = line.split(',')
    key = parts[column]
    pace = pace_to_minutes(parts[3])

    if key not in totals:
      totals[key] = 0
      counts [key] = 0
    totals[key] += pace
    counts[key] += 1

  for key, t in totals.items():
        print(f'{key}: {t/counts[key]:.2f} min/km over {counts[key]} km')


with open('data.csv') as file:
 lines = file.read().split('\n')

total = 0
count = 0
fastest_pace = 99
fastest_km = None
slowest_pace = 0
slowest_km = None


for line in lines[1:]:
 if line == '':
  continue
 parts = line.split(',')
 total += pace_to_minutes(parts[3])
 count += 1 

 pace = pace_to_minutes(parts[3])
 if pace<fastest_pace:
   fastest_pace = pace
   fastest_km = parts
 if pace>slowest_pace:
   slowest_pace = pace
   slowest_km = parts

print(f'Fastest km: {fastest_pace:.2f} min/km on {fastest_km[0]}, listening to {fastest_km[9]}')
print(f'Slowest km: {slowest_pace:.2f} min/km on {slowest_km[0]}, listening to {slowest_km[9]}')

average = total/count
print(f'Average pace: {average:.2f} min/km over {count} km')

print('---New function---')
group_by(9)
group_by(6)
group_by(7)
  