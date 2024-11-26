import pandas as pd
import numpy as np
import os

#set current folder and filename.
current_folder = os.getcwd()
file = 'bank_marketing.csv'


''' Functions to Extract, transform and Load the data'''


def extract_data():
    df = pd.read_csv(os.path.join(current_folder,file))
    print(df)
    df.set_index('client_id')
    return df 


def transform_client_data(df):
    

    #Transform client data
    
    df_client = df.loc[:,['client_id','age','job','marital','education','credit_default','mortgage']]

    df_client['job'] = df_client['job'].str.replace('.','_')
    df_client['education'] = df_client['education'].str.replace('.',',')
    df_client['education'] = df_client['education'].replace('unknown',np.nan)
    df_client['credit_default']=df_client['credit_default'].apply(lambda x:1 if x=='yes' else 0 ).astype(bool)
    df_client['mortgage'] = df_client['mortgage'].apply(lambda x:1 if x=='yes' else 0).astype(bool)
        
    return df_client
    
    
def transform_campaign_data(df):
    #Transform campaign data

    df_campaign = df.loc[:,['client_id','number_contacts','contact_duration','previous_campaign_contacts','previous_outcome','campaign_outcome']]
    df_campaign['previous_outcome'] = df_campaign['previous_outcome'].apply(lambda x:1 if x == 'success' else 0).astype(bool)
    df_campaign['campaign_outcome'] = df_campaign['campaign_outcome'].apply(lambda x:1 if x=='yes' else 0).astype(bool)

    df['year'] = 2022

    df_campaign['last_contact_date'] = pd.to_datetime(df['year'].astype(str)+ '-' +df['month'].astype(str)+ '-' +df['day'].astype(str)).dt.strftime('%Y-%m-%d')

    return df_campaign
    

def transform_economics_data(df):
    #Transform economics data
    df_economics = df.loc[:,['client_id','cons_price_idx','euribor_three_months']]

    return df_economics

    

def load_data(df_client,df_campaign,df_economics):
    df_client.to_csv('client.csv',index=False)
    df_campaign.to_csv('campaign.csv',index=False)
    df_economics.to_csv('economics.csv',index=False)



def main():
    df = extract_data()
    df_client = transform_client_data(df)
    df_campaign =  transform_campaign_data(df)
    df_economics = transform_economics_data(df)
    load_data(df_client,df_campaign,df_economics)

if __name__=='__main__':
    main()
