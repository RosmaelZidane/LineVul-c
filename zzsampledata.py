import pandas as pd


path = "/home/rz.lekeufack/Rosmael/Imbaldata/Seq/LineVul-c/data/big-vul_dataset"

df = pd.read_csv(f"{path}/processed_data.csv")

# df = df.sample(2000)
# print(df.columns)

# df.to_csv(f"{path}/processed_data.csv")


# sys:1: DtypeWarning: Columns (20,22,23,27,28,29,37,38) have mixed types.Specify dtype option on import or set low_memory=False.
# Index(['index', 'Access Gained', 'Attack Origin', 'Authentication Required',
#        'Availability', 'CVE ID', 'CVE Page', 'CWE ID', 'Complexity',
#        'Confidentiality', 'Integrity', 'Known Exploits', 'Publish Date',
#        'Score', 'Summary', 'Update Date', 'Vulnerability Classification',
#        'add_lines', 'codeLink', 'commit_id', 'commit_message', 'del_lines',
#        'file_name', 'files_changed', 'func_after', 'func_before', 'lang',
#        'lines_after', 'lines_before', 'parentID', 'patch', 'project',
#        'project_after', 'project_before', 'target', 'vul_func_with_fix',
#        'processed_func', 'flaw_line', 'flaw_line_index'],
#       dtype='object')




dft = pd.read_csv(f"{path}/train.csv")
dfpkb = pd.read_csv(f"{path}/projectkb_input_training_full.csv")


print("Bigvul \n", df['target'].value_counts())

print("sample PKB data \n", dft['target'].value_counts())



print("full PKB data \n", dfpkb['isVulnerable'].value_counts())



# Bigvul 
#  0    177736
# 1     10900
# Name: target, dtype: int64