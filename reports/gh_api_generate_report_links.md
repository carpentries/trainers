---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
import pandas as pd
from datetime import datetime, timezone
```

URL to use GH API and query trainer repository for all issues and PRs, both open and closed up to the maximum (100)

```{code-cell} ipython3
trainer_issues_url = 'https://api.github.com/repos/carpentries/trainers/issues?per_page=100&state=all'
trainer_pr_url = 'https://api.github.com/repos/carpentries/trainers/issues?per_page=100&state=all'
```

read them into a dataframe

```{code-cell} ipython3
df_r = pd.read_json(trainer_issues_url)
```

```{code-cell} ipython3
df_r.head()
```

unpack the columns that have json objects in them still

```{code-cell} ipython3
unpack_cols = ['user','pull_request','reactions','labels']
#
final_col = {True: lambda col,ser: ser.apply(pd.Series).rename(columns=lambda c: '_'.join([col,str(c)])),
            False: lambda col,ser: ser}
df_pieces = [final_col[col_i in unpack_cols](col_i,df_r[col_i]) for col_i in df_r.columns]
df = pd.concat(df_pieces,axis=1)
```

```{code-cell} ipython3
df.shape
```

```{code-cell} ipython3
df_r.shape
```

```{code-cell} ipython3
df.columns
```

the label columns are still objects, unpack those more

```{code-cell} ipython3
label_cols = ['labels_0','labels_1']
#
label_cols = [df[l].apply(pd.Series).rename(columns=lambda c: '_'.join([l,str(c)])) for l in label_cols]

df = pd.concat([df]+label_cols,axis=1)
```

```{code-cell} ipython3
df.columns
```

create filters for the proposals and approved

```{code-cell} ipython3
approved = df['labels_1_name']=='approved'
proposal = df['labels_0_name']=='Proposal'
```

create subsets of the issues

```{code-cell} ipython3
df_approved = df[approved]
df_proposal = df[proposal]
```

add a column to the approved dataframes with a link to their page

```{code-cell} ipython3
mdlink = lambda r: '['+ r['title'] + ']('+ r['html_url'] + ')'
df_approved['md'] = df_approved.apply(mdlink,axis=1)
```

add a column with teh body of the proposal

```{code-cell} ipython3
mdlink_body = lambda r: '['+ r['title'] + ']('+ r['html_url'] + ')\n' +r['body']
df_approved['md_body'] = df_approved.apply(mdlink_body,axis=1)
```

print them out for use in the report

```{code-cell} ipython3
for approved_t in df_approved['md']:
    print(approved_t)
```
