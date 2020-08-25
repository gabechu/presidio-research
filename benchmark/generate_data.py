from presidio_evaluator.data_generator.main import generate

import datetime

EXAMPLES = 500
SPAN_TO_TAG = True  # Whether to create tokens + token labels (tags)
TEMPLATES_FILE = 'presidio_evaluator/data_generator/raw_data/templates.txt'
KEEP_ONLY_TAGGED = False
LOWER_CASE_RATIO = 0.1
IGNORE_TYPES = None

cur_time = datetime.date.today().strftime("%B_%d_%Y")
OUTPUT = "data/generated_size_{}_date_{}.json".format(EXAMPLES, cur_time)

fake_pii_csv = 'presidio_evaluator/data_generator/' \
               'raw_data/FakeNameGenerator.com_3000.csv'
utterances_file = TEMPLATES_FILE
dictionary_path = None

generate(fake_pii_csv=fake_pii_csv,
         utterances_file=utterances_file,
         dictionary_path=dictionary_path,
         output_file=OUTPUT,
         lower_case_ratio=LOWER_CASE_RATIO,
         num_of_examples=EXAMPLES,
         ignore_types=IGNORE_TYPES,
         keep_only_tagged=KEEP_ONLY_TAGGED,
         span_to_tag=SPAN_TO_TAG)
