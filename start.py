from anonymizer.loader import confidential_file_tree_generator
from anonymizer.rules.makerules import make_template_rules_file


files = confidential_file_tree_generator()
rules = make_template_rules_file(files)
print(rules)
