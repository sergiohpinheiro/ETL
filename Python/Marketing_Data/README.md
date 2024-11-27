#Requisitos de ETL para os arquivos de saída


client.csv


| Column             | Data Type | Description                              | Cleaning Requirements                                                       |
|--------------------|-----------|------------------------------------------|------------------------------------------------------------------------------|
| client_id          | integer   | Client ID                                | N/A                                                                          |
| age                | integer   | Client's age in years                    | N/A                                                                          |
| job                | object    | Client's type of job                     | Change "." to "_"                                                           |
| marital            | object    | Client's marital status                  | N/A                                                                          |
| education          | object    | Client's level of education              | Change "." to "_" and "unknown" to np.NaN                                    |
| credit_default     | bool      | Whether the client's credit is in default | Convert to boolean data type: 1 if "yes", otherwise 0                        |
| mortgage           | bool      | Whether the client has an existing mortgage | Convert to boolean data type: 1 if "yes", otherwise 0                        |


campaign.csv


| Column                    | Data Type | Description                                            | Cleaning Requirements                                                       |
|---------------------------|-----------|--------------------------------------------------------|------------------------------------------------------------------------------|
| client_id                 | integer   | Client ID                                              | N/A                                                                          |
| number_contacts           | integer   | Number of contact attempts to the client in the current campaign | N/A                                                          |
| contact_duration          | integer   | Last contact duration in seconds                       | N/A                                                                          |
| previous_campaign_contacts| integer   | Number of contact attempts to the client in the previous campaign | N/A                                                          |
| previous_outcome          | bool      | Outcome of the previous campaign                       | Convert to boolean data type: 1 if "success", otherwise 0                   |
| campaign_outcome          | bool      | Outcome of the current campaign                        | Convert to boolean data type: 1 if "yes", otherwise 0                       |
| last_contact_date         | datetime  | Last date the client was contacted    


economics.csv


| Column                | Data Type | Description                                             | Cleaning Requirements                                                       |
|-----------------------|-----------|---------------------------------------------------------|------------------------------------------------------------------------------|
| client_id             | integer   | Client ID                                               | N/A                                                                          |
| cons_price_idx        | float     | Consumer price index (monthly indicator)                | N/A                                                                          |
| euribor_three_months  | float     | Euro Interbank Offered Rate (euribor) three-month rate (daily