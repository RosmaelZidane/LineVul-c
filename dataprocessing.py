import pandas as pd
import os
from sklearn.model_selection import train_test_split


path = "/home/rz.lekeufack/Rosmael/Imbaldata/Seq/LineVul-c/data/big-vul_dataset"

df = pd.read_csv(f"{path}/projectkb_input_training_full.csv")

df = df.sample(2000)

df['func_before'] = df['Code']
df['processed_func'] = df['Code']
df['index'] = df['id']
df['target'] = df['isVulnerable'].map({True: 1, False: 0, 'True': 1, 'False': 0})# 
df['flaw_line_index'] = ""
df['flaw_line'] = ""


print("PBK target\n", df['target'].value_counts())

train_df, temp_df = train_test_split(df, test_size=0.2, random_state=42)  
val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)  




train_df.to_csv(os.path.join(path, 'train.csv'), index=False)
val_df.to_csv(os.path.join(path, 'val.csv'), index=False)
test_df.to_csv(os.path.join(path, 'test.csv'), index=False)


# print(df.columns)

# dff = pd.read_csv("/home/rz.lekeufack/Rosmael/Imbaldata/Seq/LineVul-c/data/big-vul_dataset/processed_data.csv")
# print(dff['target'])



# Index(['Unnamed: 0', 'index', 'Access Gained', 'Attack Origin',
#        'Authentication Required', 'Availability', 'CVE ID', 'CVE Page',
#        'CWE ID', 'Complexity', 'Confidentiality', 'Integrity',
#        'Known Exploits', 'Publish Date', 'Score', 'Summary', 'Update Date',
#        'Vulnerability Classification', 'add_lines', 'codeLink', 'commit_id',
#        'commit_message', 'del_lines', 'file_name', 'files_changed',
#        'func_after', 'func_before', 'lang', 'lines_after', 'lines_before',
#        'parentID', 'patch', 'project', 'project_after', 'project_before',
#        'target', 'vul_func_with_fix', 'processed_func', 'flaw_line',
#        'flaw_line_index'], 
#       dtype='object')




