# Trainer Leadership Reports to EC


Per the Carpentries [Committee Policy]()
the trainer leadership submits reports twice annually to the Carpentries
Executive Committee.

## Helper Notebook
This folder also contains a markdown jupyter notebook that generates the links
for that report. It is a markdown notebook for reasons of versioning, so it
does not show the results in browser, but will run offline. It requires `pandas`
and `jupytext`.


## Helper Script + Action
There is also a script file, that has an accompanying github action in
`.github/workflows/initialize_report.yml`.  The action is set to be run
manually. To run it:

- Go to the Actions tab of the repository
- Select this action in the Workflows panel on the left
- On the right of the center panel choose "Run Workflow" on 'main' in the "Run Workflow" menu

[GitHub Instructions to manually run an action](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow)

All together the action file with the script will:
- checkout the repo on GitHub
- install python and pandas
- run the script:
    - use the github api to pull the list of the last 100 issues & PRs to the trainer repo
    - put them into a DataFrame
    - clean up the Dataframe
    - select only the approved proposals (based on the label)
    - generate a markdown link to the html page of approved proposal
    - write those to a file
- open a pull request with the initialized report file


Then you can manually continue editing that pull request to complete the report.
