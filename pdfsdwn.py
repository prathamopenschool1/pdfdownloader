import os
import requests
import pandas as pd



def downloader_pdf():

    file_name = "schoolmarathidb.xlsx"
    sheet_name = 'URL'

    df = pd.read_excel(file_name, sheet_name=sheet_name)

    df = pd.DataFrame(df)
    ext = '.pdf'
    df = df.dropna()
    df['cont_dwurl'] = df['cont_dwurl'].astype(str)
    df['subject'] = df['subject'].astype(str)

    for i, j in df.itertuples(index=False):
        if i.endswith(ext):
            end_name = os.path.basename(i)
            request_url = requests.get(i, stream=True)
            if not os.path.exists(j):
                os.makedirs(j)
            with open(os.path.join(j, end_name), 'wb') as smart:
                smart.write(request_url.content)

    
    
downloader_pdf()

