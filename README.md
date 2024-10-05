# Economic status impact on performance in 2024 Olympics
The goal of this project is to (1) get a visually and deep analysis of what happened in Pairs 2024 Olympics (2) see if there a correlation be economic status and the number of medals that a country got.

## Table of Contents
- [Methodology](#methodology)
- [Results](#results)
- [Challenges Faced](#challenges-faced)
- [Conclusion](#conclusion)
- [How to use the code](#how-to-use-the-code)
- [Acknowledgement](#acknowledgement)
- [License](#license)


## Methodology

- **Data Collection** 
    * After obtaining the medal data from [Kaggle](https://www.kaggle.com/datasets/berkayalan/paris-2024-olympics-medals), the GDP data from the [World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD), and the country codes from [IBAN](https://www.iban.com/country-codes), these datasets were merged using the country names as the main key.
    * To ensure consistency, minor discrepancies in country codes between the datasets were manually corrected based on the Alpha-3 format (e.g., "US" vs. "USA").
    * After merging, the combined dataset was checked for missing or erroneous values, ensuring a clean and ready-to-use dataset for analysis (except for the Refugee Olympic Team, I left the GDP and GDP year columns as `null` since they already have a bronze medal which I cannot ignore).
    * The final dataset is available on [Kaggle](https://www.kaggle.com/datasets/mohamedyosef101/2024-olympics-medals-and-economic-status) now.
- **Data Cleaning & Preprocessing**:
- **Exploratory Data Analysis**: 


## Results


## Challenges Faced
- **Merging Datasets**: the `country_code` in the Olympics data doesn't follow the standard Alpha-3 code --I found it a mix between Alpha-2 and abbreviation of the English names-- so I changed all the names to match Alpha-3 code. 
- **No available GDP data**: the world bank data that I have right now doesn't include any information about Taiwan or North Korea. I searched for Taiwan GDP data and found it easily. But for North Korea data, I didn't find anything--North Korea’s GDP data is quite limited and often estimated due to the country’s isolated nature and lack of transparent economic reporting-- so, I searched for GDP estimate and used it.


## Conclusion


## How to use the code 


## Acknowledgement
**Data Sources**
- [GDP per capita (current US$)](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD), World Bank
- Berkay Alan. [Paris 2024 Olympics Medals](https://www.kaggle.com/datasets/berkayalan/paris-2024-olympics-medals), Kaggle
- [Country Codes Alpha-2 & Alpha-3](https://www.iban.com/country-codes), IBAN.

## License 
This project is licensed under the MIT License (see [`LICENSE`](https://github.com/mohamedyosef101/[repo_name]/blob/main/LICENSE) for details).