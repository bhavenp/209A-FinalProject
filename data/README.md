# Data Folder

This folder contains the [Lending Club data](https://www.lendingclub.com/info/download-data.action).

* `LoanStats3a.csv` - Data on loans issued (2007-2011)
* `RejectStatsA.csv` - Data on loans declined (2007-2012)
* `LCDDataDictionary.xlsx` - Data dictionary
* `census_zipcode_level.csv` - Census data for 5-digit zipcodes (from course staff)
* `census_zip3.csv` - Census data aggregated at 3-digit zipcode (from Anthony)
	* When loading, use this: `pd.read_csv('../data/census_zip3.csv', dtype={'zip_3':str})`. This ensures that the zip gets read in as a string and not as an integer.