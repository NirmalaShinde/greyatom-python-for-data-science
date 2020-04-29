# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include='number')
print(numerical_var)




# code ends here


# --------------
# code starts here
banks=bank.drop(['Loan_ID'],inplace=False,axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode()
banks = banks.fillna(bank_mode.iloc[0])
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here

avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount)

# code ends here



# --------------
# code starts here

loan_approved_se=banks[((banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y'))].count()
print(sum(loan_approved_se))

loan_approved_se = banks[(banks['Self_Employed'].values == "Yes") & (banks['Loan_Status'].values == "Y")]

print(len(loan_approved_se))

loan_approved_nse = banks[(banks['Self_Employed'].values == "No") & (banks['Loan_Status'].values == "Y")]
print(len(loan_approved_nse))

percentage_se = (len(loan_approved_se)/len(banks['Loan_Status'])) * 100

percentage_nse = (len(loan_approved_nse)/len(banks['Loan_Status'])) * 100

print(f"The percentage of self employeed's loan approval is : {percentage_se} %")
print(f"\nThe percentage of not self employeed's loan approval is : {percentage_nse} %")


# code ends here




# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x:x/12)
# type is series
# print(loan_term)


big_loan_term = len(loan_term[loan_term>=25])
print(big_loan_term)
# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


