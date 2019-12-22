import csv
from collections import defaultdict, Counter

with open('data/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    # count = defaultdict(int)
    count = Counter()

    lang_counter = Counter()

    dev_type_info = {}

    for line in csv_reader:
        count[line['Hobbyist']] += 1

        dev_types = line['DevType'].split(';')

        for dev_type in dev_types:
            dev_type_info.setdefault(dev_type, {
                'total': 0,
                'lang_counter': Counter()
            })

        languages = line['LanguageWorkedWith'].split(';')
        dev_type_info[dev_type]['lang_counter'].update(languages)
        dev_type_info[dev_type]['total'] += 1

    total = count['Yes'] + count['No']
    yes_pct = (count['Yes'] / total) * 100
    yes_pct = round(yes_pct, 2)
    no_pct = (count['No'] / total) * 100
    no_pct = round(no_pct, 2)

print(f'Hobbyist coders: {yes_pct}%')
print(f'Not Hobbyist: {no_pct}%')
print()

for dev_type, info in dev_type_info.items():
    print(dev_type)

    for language, value in info['lang_counter'].most_common(5):
        lang_pct = (value / info['total']) * 100
        lang_pct = round(lang_pct, 2)

        print(f'\t{language}: {lang_pct}%')
