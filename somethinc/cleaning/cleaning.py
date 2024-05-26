#%%
import sys
import os
import json
import re
import pandas as pd
import polars as pl
sys.path.append(os.path.join(os.path.dirname(__file__)))
work_dir = os.path.dirname(os.path.dirname(__file__))
# %%
dataset = json.load(open(os.path.join(work_dir, 'dataset', 'product.json')))
clean_dataset = []
for x in dataset:
    for key, value in x.items():
        if key == 'price':
            x[key] = value[0]
        elif key == 'product_name':
            x[key] = value[0]
        else:
            value = [v.replace('\n', '').replace('\t', '').replace(';', ',').replace('Â\xa0', '').replace('xÂ\xa0', '').replace('Â\xa0', '').replace("/", "").replace(",", "").replace("â€¢", "").replace("*", "").replace("-", "").strip() for v in value]
            value = [re.sub('NA.*', '', v) for v in value]
            value = [v for v in value if v.strip() and len(v) > 3]
            x[key] = value if value else None

    clean_dataset.append(x)

df = pd.DataFrame(clean_dataset)
# %%
