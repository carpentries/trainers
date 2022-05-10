import pandas as pd
from datetime import date



def get_links():
    '''
    generate md links for the trainer repo
    '''

    # URL to use GH API and query trainer repository for all issues, both open and closed up to the maximum (100)

    trainer_issues_url = 'https://api.github.com/repos/carpentries/trainers/issues?per_page=100&state=all'

    # read them into a dataframe
    df_r = pd.read_json(trainer_issues_url)

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

    # the label columns are still objects, unpack those more

    label_cols = ['labels_0','labels_1']
    #
    label_cols = [df[l].apply(pd.Series).rename(columns=lambda c: '_'.join([l,str(c)])) for l in label_cols]

    df = pd.concat([df]+label_cols,axis=1)

    # create filters
    approved = df['labels_1_name']=='approved'
    proposal = df['labels_0_name']=='Proposal'

    # create filtered dataframes
    df_approved = df[approved]
    df_proposal = df[proposal]

    mdlink = lambda r: '['+ r['title'] + ']('+ r['html_url'] + ')'
    df_approved['md'] = df_approved.apply(mdlink,axis=1)


    # create file name
    date_stamp = date.today().isoformat()
    # will output like YYYY-MM-DD
    file_name = date_stamp[:8] + 'report-to-ec.md'

    # begin file with prelude
    prelude_sections = ['# '+date_stamp, '## summary', '## approved', '']
    # empty to make space
    prelude = '\n\n'.join(prelude_sections)
    with open(file_name,'a') as f:
        f.write(prelude)

    # draft report with md link list by writing each line to the file opened
    #    in append mode
    approved_links = '\n - '.join(df_approved['md'].to_list())
    with open(file_name,'a') as f:
        f.write(approved_links)


if __name__ == '__main__':
    get_links()
