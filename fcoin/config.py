
#!-*-coding:utf-8 -*-
#@TIME    : 2018/6/11/0011 10:17
#@Author  : Nogo


#秘钥
key = 'b05a718a05ab450a97967e974cfd2938'
secret = '274e5492286e4c06a46edc303ada7aa2'


#精度和最小挂单量
btc = {'name': 'btcusdt', 'coin': 'btc', 'price_precision': 2, 'amount_precision': 4, 'min_amount': 0.001}
bch = {'name': 'bchusdt', 'coin': 'bch', 'price_precision': 2, 'amount_precision': 4, 'min_amount': 0.001}
ltc = {'name': 'ltcusdt', 'coin': 'ltc', 'price_precision': 2, 'amount_precision': 4, 'min_amount': 0.001}
eth = {'name': 'ethusdt', 'coin': 'eth', 'price_precision': 2, 'amount_precision': 4, 'min_amount': 0.001}
etc = {'name': 'etcusdt', 'coin': 'etc', 'price_precision': 2, 'amount_precision': 4, 'min_amount': 0.001}
ft = {'name': 'ftusdt', 'coin': 'ft', 'price_precision': 6, 'amount_precision': 0, 'min_amount': 5}
btm = {'name': 'btmusdt', 'coin': 'btm', 'price_precision': 4, 'amount_precision': 1, 'min_amount': 5}

#交易对，仅支持以上USDT交易对
symbol = ft

#抱团模式：固定价格刷单(等于0就是市价，大于0固定该价格)
fix_price = 0

#当固定价格有效时,买入前判断市价与固定价的差价，在范围帐内则下单
diff_price = 0.02

#★买卖深度前3挂单数量总和
total_amount = 0

#当★满足时的买入挂单量,如果梭哈刷设置个很大的值
max_amount = 6

#当★不满足时的买入挂单量
min_amount = 6

#持仓币种最大量
limit_amount = 10

#暂时无用
ft_base_amount = 0

#买单超时(s)
delay = 20


