# PJM data miner scripts to make exporting data easier

## Install

### Install Python3 + Pip + Virtualenv
```
virtualenv venv -p python3
. ./venv/bin/activate
pip install -r requirements.txt
```

### Look at the pjm_urls.py script for valid urls
This file contains a key:value mapping of "url" to the actual url.  These urls come from the data that populates the 
Explore Data link found on these pages:
http://dataminer2.pjm.com/feed/hrl_load_metered/definition
Go to the page, click on explore data.  In google chrome 

1. launch the "inspect" tool, 
2. select the network tab, 
3. Click download csv
4. Copy the link to the pjm_urls.py 

### Run the data collection script, examples
```
python fetch_pjm_csv.py --list
python fetch_pjm_csv.py -u pnode
python fetch_pjm_csv.py -u pnode -o pnode.csv
python fetch_pjm_csv.py -u ops_sum_prev_period
python fetch_pjm_csv.py -u hrl_load_metered
python fetch_pjm_csv.py -u solar_gen
```
optionally add -o output.csv to override filename

### Available URLs
|url|description|
|---|---|
|act_sch_interchange|Hourly actual, scheduled, and inadvertent flows by tie line for each hour. Positive Values represent an import into PJM and Negative Values represent and export from PJM|
|ancillary_services|This feed contains hourly ancillary services pricing (LMP) data. RSS Notification for this feed contains Market Day.|
|reserve_market_results|Hourly Ancillary service market results including MW quantities and prices. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|ancillary_services_fivemin_hrl|This feed contains five minute granular ancillary services pricing (LMP) data. RSS Notification for this feed contains Market Day.|
|bal_trns_cong_prelim_billing|This feed contain hourly billing rates for Balancing Transmission Congestion Credit allocation.� These values are for information purpose only and are subject to change through the fifth business day of the following month. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|day_inc_dec_utc|Daily cleared virtual transactions in the Day Ahead Energy Market|
|day_gen_capacity|PJM available generation capacity including total economic and emergency maximum MW offered and total generation committed via the PJM RPM Capacity Market|
|uplift_by_zone|This data shows daily uplift credits by zone. Data is posted monthly after the closing of the monthly settlement. Data for a given month is initially computed at that time, and is updated in the following two months. THIS FEED IS RETIRED from August 10th, 2019 onwards as part of FERC Order 844. The uplift credits information can be found in Daily Uplift Credits by Zone feed|
|uplift_charges_by_zone|This data shows daily uplift charges by zone. The data is posted monthly after the closing of the monthly settlement. Data for a given month is initially computed at that time, and is reposted the following four months to reflect settlements adjustments. Data will be posted on a monthly basis starting August 10th 2019 as required by FERC Order 844. Because this data became public as a result of Order 844, data for months prior to July 2019 cannot be published.|
|uplift_credits_by_zone|This data shows daily uplift credits by zone. The data is posted monthly after the closing of the monthly settlement. Data for a given month is initially computed at that time, and is reposted in the following four months to reflect settlements adjustments. This feed will have substantively the same information as retired Uplift by Zone feed but the Credit Type pivoted into one single column to better correlate with other data required by FERC Order 844. Data will be posted on a monthly basis starting August 10th 2019 as required by FERC Order 844. Because this data became public as a result of Order 844, data for months prior to July 2019 cannot be published.|
|da_interface_flows_and_limits|This feed contains the hourly Day Ahead Flow MW and Limit MW for each Interface Limit Name|
|da_hrl_lmps|This feed contains hourly Day-Ahead Energy Market locational marginal pricing (LMP) data for all bus locations, including aggregates. RSS Notification for this feed contains Market Day.|
|da_marginal_value|This feed contains dates and times for binding constraints along with the marginal value, also called the shadow price, for those constraints in the Day-Ahead Energy Market|
|dasr_results|This feed contains hourly billing data for the Day Ahead Scheduling Reserve Market. These values are for informational purposes only and are subject to change once actual settlement calculations are performed. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|da_tempset|This feed contains the zonal temperature sets for Day-Ahead Market.|
|da_transconstraints|Start and End times for constraints in the Day-Ahead Energy Market|
|energy_market_offers|This data contains detail on offers by generators into the PJM Day-Ahead Energy Market. Generator identification is masked to prevent revealing of confidential information, and the masked codes are changed annually. Data is posted on a four-month delay.|
|mnt_efor|Equivalent Forced Outage Rates (EFORd) by unit type and size|
|very_short_load_frcst|This feed contains the Five-minute load forecast data showing forecast amounts every five minutes for a two hour window by area. This forecast is updated every five minutes. The data is presented for 25 areas to maintain consistency with the seven day load forecasts - PJM�s market clearing engine uses EKPC, MID_ATLANTIC_REGION, AP, COMED, AEP, DOMINION, DUQUESNE, ATSI, DEOK, DAYTON. Missing intervals data for this feed will be made available at the end of the calendar day.|
|agg_definitions|This feed contains the bus distribution factors used in settlements for aggregates with static definitions effective as of the date indicated in Last Updated date. Includes static definitions for hub, interface, load, generation, EHV and FTR apportionment zone|
|frcstd_gen_outages|This data contains the megawatt totals of forecasted generation outages for the next ninety days. An expected megawatt total is listed for each day for the next ninety days and broken down by sub-regions in PJM. These values are forecasts based on available information. It is provided for informational purposes only and should not be relied upon by any party for actual billing values.|
|ftr_bids_annual|This feed contains data for all bids into the PJM Annual Financial Transmission Rights Auctions. This data is posted on a four month delay.|
|ftr_bids_long_term|This feed contains data for all bids into the PJM Long Term Financial Transmission Rights Auctions. This data is posted on a four month delay.|
|ftr_bids_mnt|This feed contains data for all bids into the PJM Monthly Financial Transmission Rights Auctions. This data is posted on a four month delay.|
|ftr_cong_lmp|This feed presents data for the Congestion Locational Marginal Prices used in the FTR credit calculator. Adjusted cLMPs are the historical cLMPs adjusted by PROMOD production cost simulation, which considers certain transmission upgrades. This adjustment is different for annual and long term auctions, and the values will be reflected by pulling data through different time periods|
|gen_ehv_losses|This data contains the hourly PJM generation and extra high voltage (EHV) loss data for each day. This is informational data only|
|gen_by_fuel|This data shows the fuel mix of generation resources operating under PJM direction for each hour|
|gen_outages_by_type|This data contains the actual and scheduled megawatt generation outages for today and the next six days. In addition to providing total outages, the data show subtotals for each of the following outage types: unplanned (forced), maintenance, and planned. In order to provide a perspective on outages that are actually occurring or are scheduled to occur during the operating days, only outages with a status of active or approved are included.|
|gen_specific_uplift_credit|This data shows monthly uplift credits by generator. Data is posted monthly with a one month lag. (For example, January data would be posted around March 10th.) Data for a given month is initially computed at that time, and is reposted in the following three months to reflect settlements adjustments. Data will be posted on a monthly basis starting September 10th 2019 as part of FERC Order 844. Because this data became public as a result of Order 844, data for months prior to July 2019 cannot be published.|
|load_frcstd_hist|This feed provides forecasted load, grouped by the date and time the forecast was created. Forecasts are provided every six hours starting one day prior to the Effective Date|
|hrl_da_demand_bids|Aggregated hourly demand bids submitted to the Day-Ahead Energy Market. For each hour, the total MW amount of demand bids are shown summed by the price point of the demand bid. This data is made available on a six month delay|
|hrl_da_incs_decs|This feed contains the virtual bid data for the Day-Ahead Energy Market. The bids are aggregated by pricing point, by bid type, by hour, and by day. This data is posted on four month delay|
|hrl_dmd_bids|This feed lists the hourly data ahead bid data for each market day|
|hrl_load_estimated|This feed contains estimated integrated hourly loads that are calculated from meter data. Estimated loads reflect revenue-quality meter information but have not yet been verified by the electric distribution companies and are subject to later adjustment. This information is provided for informational purposes only and should not be relied upon by any party for the actual billing values|
|hrl_load_metered|This feed summarizes the MW-hour net energy for load as consumed by the service territories within the PJM RTO. Data is supplied by the respective electric distribution companies within PJM, and represents the best quality level of metered load within their zones. This data contains company submitted values or PJM generated estimated values substituted where company data is unavailable. The Company Verified flag indicates whether the value has been verified by the electric distribution company. There will be a lag in updated data availability due to wait time for possible corrections. Data adjustments can occur up to 90 days after the actual date. The mapping representation between Control Areas, NERC Regions, Market Regions, Zones and Load Areas from the legacy posting is available here:https://pjm.com/-/media/etools/data-miner-2/hourly-loads-area-mapping.ashx?la=en. This reference document is for informational purposes only and will not be updated.|
|hrl_load_prelim|This feed contains preliminary integrated hourly loads that are calculated daily from raw telemetry data and are approximate for informational purposes only. These loads do not reflect confirmed transaction information with the market participants and the external control areas|
|inst_dispatch_rates|This feed contains the PJM instantaneous dispatch rates. The following dispatch rate information includes both the PJM electronic dispatch signals and manual dispatch signals. The electronic rates are updated every 15 seconds. The manual rates are updated with a frequency of 1 to 5 minutes and reflect individual generator dispatch. This data is provided for informational purposes ONLY and should not be relied upon by any party for the actual billing values. Missing interval data will not be backfilled due to the nature of the data. This data will be retained for 15 days only.|
|inst_load|This feed contains the load MW for four regions. Loads are calculated from raw telemetry data and are approximate. The displayed values are NOT official PJM Loads.|
|load_recon_bill_deter_daily|This feed contains the billing determinants that are used by PJM to reconcile past months billings between electric distribution companies and Retail Load Aggregators for certain allocations that are based on real-time load ratio shares. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|load_recon_bill_deter_hrly|This feed contains the billing determinants that are used by PJM to reconcile past months billings between EDCs and Retail Load Aggregators (Electric Generation Suppliers) for certain allocations that are based on real-time load ratio shares. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|demand_response_uplift_credit|This data shows monthly uplift credits by Demand Response resources. Data is posted monthly with a one month lag. (For example, January data would be posted around March 10th.) Data for a given month is initially computed at that time, and is reposted in the following four months to reflect settlements adjustments. Data will be posted on a monthly basis starting September 10th 2019 as part of FERC Order 844. Because this data became public as a result of Order 844, data for months prior to July 2019 cannot be published.|
|m2m_rt_ffe|This feed provides the hourly real time firm flow entittlement for non-monitoring rto flowgates. FFE is posted each morning for the previous day.|
|mnt_ftr_zonal_lmps|This feed contains the monthly financial transmission rights zonal and residual aggregate locational marginal prices and are based on peak load apportionments. FTR zonal, residual aggregate, and DA Zonal  LMPs are subject to change before the fifth PJM business day of the following month|
|nodal_ref_prices|This feed provides the export nodal reference prices for different interface points. The higher of these reference prices or the IT SCED price is used to calculate the amount of credit that is needed to be set aside for exports.  The reference prices change every two months.|
|nodal_refe_prices_incdec|Reference prices for the different pricing nodes in the Day-Ahead Energy Market. These prices are used when performing credit screening for virtual bids in the Day-Ahead Energy Market|
|non_sync_reserve|This feed contains hourly billing data for the Non-Synchronized Reserve Market. These values are for informational purposes only and are subject to change through the fifth business day of the following month. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|off_cost_ops|This feed gives the location, time and reason for off-cost or reactive operations to maintain the voltages needed for system stability|
|ops_sum_prev_period|This data shows daily information after each day's actual operations for the PJM footprint and areas within PJM. Data is refreshed on top of the hour from 5 a.m. to 8 a.m. Note: Prior to the implementation of Data Miner, PJM's Operations Summary included values for the day and evening peaks and the overnight valley only. Historical data prior to Data Miner will include only these rows in the data. Newer data includes values for all hours of the day.|
|ops_sum_frcstd_tran_lim|This data is prepared each morning and shows the forecasted transfer limits for the projected peak of the day. Data is refreshed on top of the hour from 5 a.m. to 8 a.m.|
|ops_sum_frcst_peak_area|This data is prepared each morning and contains information for the projected peak of the day for areas within the PJM footprint. Data is refreshed on top of the hour from 5 a.m. to 8 a.m.|
|ops_sum_frcst_peak_rto|This data is prepared each morning and contains information for the projected peak of the day for the entire PJM footprint. Data is refreshed on top of the hour from 5 a.m. to 8 a.m.|
|ops_sum_prjctd_tie_flow|This data is prepared each morning and shows scheduled tie flows at the projected peak of the day. Data is refreshed on top of the hour from 5 a.m. to 8 a.m.|
|ops_init_commit|This feed presents economic max and reason for the Operator Initiated Commitments by zone|
|reg_zone_prelim_bill|This feed contains hourly billing data for the PJM Regulation Market. These values are for informational purposes only and are subject to change through the fifth business day of the following month. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|pnode|This data contains master information on pnodes. A pnode is a single pricing node or subset of pricing nodes where a physical injection or withdrawal is modeled and for which a Locational Marginal Price is calculated and used for financial settlements.|
|rt_default_mv_override|The default marginal value override data contains effective and termination dates for constraints that use a different transmission constraint penalty factor from the default setting, for those constraints in the Real-Time Energy Market. By default all PJM internal M2M constraints coordinated with MISO have a transmission constraint penalty factor of $1000. By default all PJM internal M2M constraints coordinated with NYISO and all PJM internal non-M2M have a transmission constraint penalty factor of $2000. This data is being posted as part of FERC Order 844.|
|rt_fivemin_hrl_lmps|This feed contains five minute granular Real-Time Energy Market locational marginal pricing (LMP) data for all bus locations, including aggregates. Load-weighted average transmission zone and residual aggregate prices are estimates only. RSS Notification for this feed contains Market Day.|
|rt_hrl_lmps|This feed contains hourly Real-Time Energy Market locational marginal pricing (LMP) data for all bus locations, including aggregates. Load-weighted average transmission zone and residual aggregate prices are estimates only. RSS Notification for this feed contains Market Day.|
|rt_marginal_value|The marginal value data contains dates and times for binding constraints along with the transmission constraint penalty factor, limit control percentage, and marginal value, also called the shadow price, for those constraints in the Real-Time Energy Market. The shadow price data will be at a five minute granular level from April 1st, 2018 onwards as part of five-minute settlements initiative. The transmission constraint penalty factor and limit control percentage data will be at a five minute granular level from January 29th, 2019 onwards as part of FERC Order 844. Voltage surrogates and closed loop interface type constraints will have a null value in the limit control percentage column. Data prior to April 1st, 2018 will remain hourly.|
|rt_scheduled_interchange|This data contains the hourly net tie schedule for each day, as of Last Updated Date. The data uses the following conventions: .Positive values (+) are into PJM .Negative values (-) are out of PJM .Blank values signify no scheduled tie flow|
|rt_tempset|This feed contains the zonal temperature sets used to determine limits on transmission facilities during the operating day.|
|rt_transn_constraints|Start and End times for constrains in the Real-Time Energy Market. THIS FEED IS RETIRED from April 1st, 2018 onwards as part of five-minute settlements initiative. The constraints information can be found in Real-Time Marginal value feed|
|bill_deter_mnt_load|This feed contains the reconciliation billing determinants that are used by PJM to reconcile past months billings between electric distribution companies and Retail Load Aggregators for certain allocations that are based on real-time load ratio shares. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|prelim_or_rates|Daily billing rates for PJM operating reserves. These values are for informational purposes only and are subject to change through the fifth business day of the following month. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|reg_market_results|The amount of Regulation that needs to be carried in the hour, adjusted by the effective MW.  This data includes mileage ratios and overall performance scores. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|sync_reserve_prelim_bill|Hourly billing data for the Synchronized Reserve Market for each day. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|transfer_limits_and_flows|Hourly transfers and transfer limits by transfer limit area|
|rt_and_self_ecomax|This feed contains the load and reserve megawatts as well as the megawatts of generation resources that self-schedule. The load and reserve megawatts are units called on in real time to meet load and/or reserve requirements. Self-scheduled generation resources can impact PJM�s real-time dispatch operations and locational marginal pricing resulting in uplift charges.|
|ancillary_services_fivemin_mnt|This feed contains the verified five minute Ancillary Service Market prices used in settlements. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|rt_fivemin_mnt_lmps|This feed contains the verified five minute Real-Time LMPs for aggregate and zonal pnodes used in settlements. The load weighted average transmission zone and residual aggregate prices provided in the daily LMPs are estimates only. Transmission zone prices and residual aggregate prices used in PJM accounting are not final until five PJM business days after the end of the month. This is due to the differences between the State Estimator load bus distributions and the final Real-Time load bus distributions required for the actual calculation of the Real-Time Zonal and Residual aggregate LMPs which are posted in the monthly LMP files.  While individual pnode LMPs do not change during the verification process, but the transmission zone and residual aggregate prices may. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|ancillary_services_monthly|This feed contains the verified hourly Ancillary Service Market prices used in settlements. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|rt_da_monthly_lmps|This feed contains the verified hourly Real-Time LMPs for aggregate and zonal pnodes used in settlements and final Day-Ahead LMPs. Note that while Data Miner 2 will make available any data that has been calculated by PJM Settlements, there are occasionally delays in the settlements process that may cause a delay in data availability.|
|load_frcstd_7_day|PJM hourly load forecast for the next seven days by area. This data is updated twice per hour and replaces the previous forecast. As such, only a single set of forecast values is available at any given time. Snapshots of historical data for certain points of the day are preserved in the Historical Load Forecast data feed|
|solar_gen|This feed provides the hourly solar generation amounts in PJM.  The "Other" area includes external units and other units where the original regional location is not known|
|sync_reserve_events|Historical account of the date/time of an event going back to 2002.|
|transfer_interface_infor|This feed contains the actual flow MW and transfer limits information for the Transfer Interfaces.|
|transmission_limits|This feed contains the current PJM transmission limits. This feed will be populated with data only when there are transmission constraints for that five minute interval.|
|unverified_five_min_lmps|This feed contains the unverified real-time LMP data for a subset of pnodes which are zonal, aggregate, interface, hub and 500 Kv bus.|
|utc_bid_screening|This feed contains all the reference prices used for virtual credit screening when up-to-congestion bids are being submitted.|
|wind_gen|This feed provides the hourly wind generation amounts in PJM.  The "Other" area includes external units and other units where the original regional location is not known|