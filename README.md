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

- **Data Collection & cleaning** 
    * After obtaining the medal data [1](#data:medals), the GDP data [2](#data:gdp), country codes [3](#data:codes), and population [4](#data:population), I merged these datasets the country code as the main key.
    * To ensure consistency, minor discrepancies in country codes between the datasets were manually corrected based on the Alpha-3 format (e.g., "US" vs. "USA").
    * After merging, the combined dataset was checked for missing or erroneous values, ensuring a clean and ready-to-use dataset for analysis (note: I dropped the Refugee Olympic Team data, since it is out of our focus in this analysis).
    * The final dataset is available on [Kaggle](https://www.kaggle.com/datasets/mohamedyosef101/2024-olympics-medals-and-economic-status) now.
- **Exploratory Data Analysis**: 


## Results


## Challenges Faced
- **Merging Datasets**: the `country_code` in the Olympics data doesn't follow the standard Alpha-3 code --I found it a mix between Alpha-2 and abbreviation of the English names-- so I changed all the names to match Alpha-3 code. 
- **No available GDP data**: the world bank data that I have right now doesn't include any information about Taiwan or North Korea. I searched for Taiwan GDP data and found it easily. But for North Korea data, I didn't find anything--North Korea’s GDP data is quite limited and often estimated due to the country’s isolated nature and lack of transparent economic reporting-- so, I searched for GDP estimate and used it.


## Conclusion


## How to use the code 


## Acknowledgement
**Data Sources**
[<span id="data:gdp">1</span>] [GDP per capita (current US$)](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD), World Bank. <br>
[<span id="data:medals">2</span>] Berkay Alan. [Paris 2024 Olympics Medals](https://www.kaggle.com/datasets/berkayalan/paris-2024-olympics-medals), Kaggle. <br>
[<span id="data:codes">3</span>] [Country Codes Alpha-2 & Alpha-3](https://www.iban.com/country-codes), IBAN. <br>
[<span id="data:population">4</span>] [World Population Prospects: 2022 Revision](https://data.worldbank.org/indicator/SP.POP.TOTL), World Bank. <br>

## License 
This project is licensed under the MIT License (see [`LICENSE`](https://github.com/mohamedyosef101/[repo_name]/blob/main/LICENSE) for details).