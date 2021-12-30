create table if not exists CryptoCurrency(
    id int primary key,
    name varchar(20) not null
);


delete from CryptoCurrency;

insert into CryptoCurrency values (1, 'BTC');

create table if not exists btc_price(
    time_period_start timestamptz,
    time_period_end timestamptz,
    time_open timestamptz not null,
    time_close timestamptz not null,
    price_open float not null,
    price_high float not null,
    price_low float not null,
    price_close float not null,
    volume_traded int not null,
    trades_count int not null,
    currency int references CryptoCurrency (id),
    primary key (time_period_start, time_period_end)
);

CREATE INDEX btc_price_start_time_idx 
    ON btc_price 
 USING BRIN (time_period_start, time_period_end ) 
  WITH (pages_per_range = 10);

create table if not exists btc_volatility(
    day date primary key,
    price_close_std float not null,
    price_open_std float not null,
    price_low_std float not null,
    price_high_std float not null,
    price_diff_per_day_std float not null
);


CREATE INDEX btc_volatility_day_idx 
    ON btc_volatility 
 USING BRIN (day ) 
  WITH (pages_per_range = 30);