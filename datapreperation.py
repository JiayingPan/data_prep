import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel('costa_coffee.xlsx', engine='openpyxl')
    df['Use_of_Hashtag'] = df["text"].str.contains("#")
    bool_cols = df.columns[df.dtypes == 'bool']
    df[bool_cols] = df[bool_cols].replace({True: 'Yes', False: 'No'})
    df.to_excel('Prepared_dataset.xlsx', index=False, header=True)
