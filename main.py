from datetime import datetime
from dateutil import relativedelta
import pandas as pd
import numpy_financial as npf

installment_bnp = 1483.95
left_ammount_bnp = 156831.44
percentage_bnp = 0.0662
last_installment_date_bnp = '05dec2037'

# no_of_installments = datetime.strptime(last_installment_date_bnp, '%d%b%Y').date() - datetime.today().date()
last_installment_date_bnp = datetime.strptime(last_installment_date_bnp, '%d%b%Y').date()
today = datetime.today().date()
no_of_installments = relativedelta.relativedelta(last_installment_date_bnp,today)
no_of_installments = (no_of_installments.years * 12) + no_of_installments.months
npf.pmt(0.0662/12, no_of_installments, 156831, 0)

installments = []
num_of_installments = []
total_payments = []
total_interests = []

for i in range(1, no_of_installments+1):
    installment = abs(npf.pmt(percentage_bnp/12, i, left_ammount_bnp, 0))
    installments.append(installment)
    num_of_installments.append(i)
    total_payments.append(i*installment)
    total_interests.append((i*installment)-left_ammount_bnp)

df = pd.DataFrame({'installment': installments, 'num of installments': num_of_installments,
                   'total payments': total_payments, 'total interests': total_interests})
