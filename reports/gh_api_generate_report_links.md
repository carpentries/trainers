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

## Generate links to Proposals in batch. 

This can be used as a notebook file by having the following installed. 

If you have jupytext installed, then jupyter notebooks can open this markdown file as a notebook. 

- jupyter
- pandas
- jupytext

```{code-cell} ipython3
import pandas as pd
```

URL to use GH API and query trainer repository for all issues and PRs, both open and closed up to the maximum (100)

```{code-cell} ipython3
trainer_issues_url = 'https://api.github.com/repos/carpentries/trainers/issues?per_page=100&state=all'
trainer_pr_url = 'https://api.github.com/repos/carpentries/trainers/issues?per_page=100&state=all'
```

Read them into a dataframe usign pandas

```{code-cell} ipython3
df_r = pd.read_json(trainer_issues_url)
```

Look at the head to determin which columns still have json objects inside

```{code-cell} ipython3
df_r.head()
```

unpack the columns that have json objects in them still

```{code-cell} ipython3
unpack_cols = ['user','pull_request','reactions','labels']
# this dictionary makes it possible to ahve the following more compact. 
#     it will for columns in the above list unpack them into a series and then prepend the name of the 
#     source column to the new column names.  So the label column having {0:Proposed, 1: approved} 
#     will turn into a label_0 column with a value of Proposed 
#     by making it with Series and apply it then returns a DataFrame, by having a Series from each row
final_col = {True: lambda col,ser: ser.apply(pd.Series).rename(columns=lambda c: '_'.join([col,str(c)])),
            False: lambda col,ser: ser}

#  This iterates over columns and makes a list of the Series of the column and 
#      the dataframe produced by expanding the ones that were jsons
df_pieces = [final_col[col_i in unpack_cols](col_i,df_r[col_i]) for col_i in df_r.columns]

#  this takes the list of Series and DataFrame objects and combines them side by side to one dataFrame
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
# same as above but for a smaller subset 
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
df_proposal['md'] = df_proposal.apply(mdlink,axis=1)
```

add a column with the body of the proposal

```{code-cell} ipython3
mdlink_body = lambda r:  '# '+ r['title']+ '\n\n [source]('+ r['html_url'] + ')\n' +r['body']
df_approved['md_body'] = df_approved.apply(mdlink_body,axis=1)
```

## Approved Proposal Titles with Links

Print out approved proposals

```{code-cell} ipython3
for approved_t in df_approved['md']:
    print(approved_t)
```

## Approved Proposal Text

```{code-cell} ipython3
report_name = 'allproposals.md'
for approved_t in df_approved['md_body']:
    with open(report_name,'a') as f:
        f.write(approved_t)
        f.write(' \n \n \n --- \n \n \n')
        
```

## Open Proposals

```{code-cell} ipython3
for open_t in df_proposal['md']:
    print(open_t)
```

```{code-cell} ipython3

```
