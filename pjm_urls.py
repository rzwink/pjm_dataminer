import datetime


def last_day_of_month(date):
    if date.month == 12:
        return date.replace(day=31)
    return date.replace(month=date.month + 1, day=1) - datetime.timedelta(days=1)


yesterday = datetime.datetime.now().replace(hour=0, minute=0, second=0) - datetime.timedelta(days=1)
startofmonth = datetime.datetime.now().replace(day=1, hour=0, minute=0, second=0)
endofmonth = last_day_of_month(datetime.datetime.now())

startoflastmonth = (startofmonth - datetime.timedelta(days=1)).replace(day=1)
endoflastmonth = last_day_of_month(startoflastmonth)

urls = {
    'ops_sum_prev_period': 'https://api.pjm.com/api/v1/ops_sum_prev_period?sort=datetime_beginning_utc&order=Desc&startRow=1&isActiveMetadata=true&fields=actual_load,area,area_load_forecast,datetime_beginning_ept,datetime_beginning_utc,datetime_ending_ept,datetime_ending_utc,dispatch_rate,generated_at_ept&format=csv&download=true&datetime_beginning_ept=' + yesterday.isoformat(),
    'pnode': 'https://api.pjm.com/api/v1/pnode?sort=pnode_id&startRow=1&isActiveMetadata=true&fields=effective_date,pnode_id,pnode_name,pnode_subtype,pnode_type,termination_date,voltage_level,zone&termination_date=12/31/9999%20exact&format=csv&download=true',
    'hrl_load_metered': 'https://api.pjm.com/api/v1/hrl_load_metered?sort=datetime_beginning_utc&startRow=1&isActiveMetadata=true&fields=datetime_beginning_ept,datetime_beginning_utc,is_verified,load_area,mkt_region,mw,nerc_region,zone&datetime_beginning_ept=' + startoflastmonth.isoformat() + '%20to%20' + endoflastmonth.isoformat() + '&format=csv&download=true',
    'solar_gen': 'https://api.pjm.com/api/v1/solar_gen?sort=datetime_beginning_utc&order=Desc&startRow=1&isActiveMetadata=true&fields=area,datetime_beginning_ept,datetime_beginning_utc,solar_generation_mw&format=csv&download=true&datetime_beginning_ept=' + startofmonth.isoformat() + '%20to%20' + endofmonth.isoformat() + '',
}
