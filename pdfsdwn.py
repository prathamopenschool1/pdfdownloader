import os
import requests
import pandas as pd
import traceback
import validators



def downloader_pdf():

    file_name = input("Enter The File Name: ")
    sheet_name = input("Enter Sheet Name: ")

    df = pd.read_excel(file_name, sheet_name=sheet_name)

    df = pd.DataFrame(df)

    df = df.dropna(how='all', axis='columns')
    df = df.dropna()


    try:
        whitespace_remover(df)

        # cols  = list(df)
        # for i in cols:
        #     print(i, "cols")

        counts = len(df.columns)
        print("counts", counts)

        if {'cont_dwurl', 'subject'}.issubset(df.columns):
            _extracted_from_downloader_pdf_14(sheet_name, df)
        elif counts == 1 and  'cont_thumburl' in df:
            data_series = df.squeeze()
            # print("data series >>>   ",   data_series)
            _create_sheet_dir(sheet_name=sheet_name)
            for i in data_series:
                # if i.endswith(extension):
                end_name = os.path.basename(i)
                valid_url = validators.url(i)
                print("valid url is ", valid_url, i)
                if valid_url :
                    request_url = requests.get(valid_url, stream=True)
                    with open(end_name, 'wb') as smart:
                        smart.write(request_url.content)
                else:
                    continue
        elif counts == 1 and  'cont_dwurl' in df:
            data_series = df.squeeze()
            # print("data series >>>   ",   data_series)
            _create_sheet_dir(sheet_name=sheet_name)
            for i in data_series:
                # if i.endswith(extension):
                end_name = os.path.basename(i)
                valid_url = validators.url(i.strip())
                print("valid url is ", valid_url, i)
                if valid_url :
                    request_url = requests.get(valid_url, stream=True)
                    with open(end_name, 'wb') as smart:
                        smart.write(request_url.content)
                else:
                    continue
        elif {'cont_dwurl', 'cont_thumburl'}.issubset(df.columns):
            print("in this condition ")
            _create_sheet_dir(sheet_name=sheet_name)
            for index, i in enumerate(df['cont_dwurl']):
                valid_url_i = validators.url(i.strip())
                if valid_url_i == True:
                    # print(valid_url_i, index, i)
                    end_name_i = os.path.basename(i)
                    print("end name is ", end_name_i, index)
                    if end_name_i != '':
                        # print("this is not empty ", index, i)
                        folder_to_create = end_name_i.split('.')
                        print("folder to ====================", folder_to_create, index, len(folder_to_create))
                        if len(folder_to_create) == 3:
                            if not os.path.exists(folder_to_create[2]):
                                os.makedirs(folder_to_create[2])
                            if valid_url_i == True and end_name_i != '':
                                request_url = requests.get(i, stream=True)
                                with open(os.path.join(folder_to_create[2], end_name_i), 'wb') as smart:
                                    smart.write(request_url.content)
                        elif len(folder_to_create) == 2:
                            if not os.path.exists(folder_to_create[1]):
                                os.makedirs(folder_to_create[1])
                            if valid_url_i == True and end_name_i != '':
                                request_url = requests.get(i, stream=True)
                                with open(os.path.join(folder_to_create[1], end_name_i), 'wb') as smart:
                                    smart.write(request_url.content)
                
            for index1, j in enumerate(df['cont_thumburl']):
                valid_url_j = validators.url(j.strip())
                if valid_url_j == True:
                    # print(valid_url_j, index, i)
                    end_name_j = os.path.basename(j)
                    print("end name is ", end_name_j, index1)
                    if end_name_j != '':
                        # print("this is not empty ", index, i)
                        folder_to_create = end_name_j.split('.')
                        print("folder to ====================", folder_to_create, index1, len(folder_to_create))
                        if len(folder_to_create) == 3:
                            if not os.path.exists(folder_to_create[2]):
                                os.makedirs(folder_to_create[2])
                            if valid_url_j == True and end_name_j != '':
                                request_url = requests.get(j, stream=True)
                                with open(os.path.join(folder_to_create[2], end_name_j), 'wb') as smart:
                                    smart.write(request_url.content)
                        elif len(folder_to_create) == 2:
                            if not os.path.exists(folder_to_create[1]):
                                os.makedirs(folder_to_create[1])
                            if valid_url_j == True and end_name_j != '':
                                request_url = requests.get(j, stream=True)
                                with open(os.path.join(folder_to_create[1], end_name_j), 'wb') as smart:
                                    smart.write(request_url.content)




            
    except Exception as e:
        print("shcema invalid ", e)
        traceback.print_exc()


# # TODO Rename this here and in `downloader_pdf`
def _extracted_from_downloader_pdf_14(sheet_name, df):
    extension = input("Enter Extension To Download: ")
    if extension:
        new_dir = extension.split('.')

    _create_sheet_dir(sheet_name)

    if not os.path.exists(new_dir[1]):
        os.makedirs(new_dir[1])

    os.chdir(new_dir[1])

    for i, j in df.itertuples(index=False):
        valid_url_j = validators.url(i.strip())
        if valid_url_j == True and i.endswith(extension):
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

def whitespace_remover(dataframe):

    for i in dataframe.columns:
         
        # checking datatype of each columns
        if dataframe[i].dtype == 'object':
            # applying strip function on column
            dataframe[i] = dataframe[i].map(str.strip)

downloader_pdf()

