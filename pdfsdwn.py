from operator import index
import os
import requests
import pandas as pd



def downloader_pdf():

    file_name = input("Enter The File Name: ")
    sheet_name = input("Enter Sheet Name: ")

    df = pd.read_excel(file_name, sheet_name=sheet_name)

    df = pd.DataFrame(df)
    df = df.dropna()

    df = df.applymap(str)

    if {'cont_dwurl', 'subject'}.issubset(df.columns):
        _extracted_from_downloader_pdf_14(sheet_name, df)
    elif 'cont_thumburl' in df:
        data_series = df.squeeze()
        _create_sheet_dir(sheet_name=sheet_name)
        for i in data_series:
            # if i.endswith(extension):
            end_name = os.path.basename(i)
            request_url = requests.get(i, stream=True)
            with open(end_name, 'wb') as smart:
                smart.write(request_url.content)


# TODO Rename this here and in `downloader_pdf`
def _extracted_from_downloader_pdf_14(sheet_name, df):
    extension = input("Enter Extension To Download: ")
    if extension:
        new_dir = extension.split('.')

    _create_sheet_dir(sheet_name)

    if not os.path.exists(new_dir[1]):
        os.makedirs(new_dir[1])

    os.chdir(new_dir[1])

    for i, j in df.itertuples(index=False):
        if i.endswith(extension):
            end_name = os.path.basename(i)
            request_url = requests.get(i, stream=True)
            if not os.path.exists(j):
                os.makedirs(j)
            with open(os.path.join(j, end_name), 'wb') as smart:
                smart.write(request_url.content)
    

def _create_sheet_dir(sheet_name):

    if not os.path.exists(sheet_name):
        os.makedirs(sheet_name)

    os.chdir(sheet_name)


downloader_pdf()

