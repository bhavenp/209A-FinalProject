---
title: EDA
notebook: EDA_for_final.ipynb
nav_include: 2
---




We began by looking at the accepted loan data from the years 2013 and 2014. We did not look at loan data prior to 2013 because Lending Club [changed its underwriting policy in late 2012](https://www.lendacademy.com/lending-club-underwriting-changes/), which "removed the highest risk borrowers that were previously being approved and... added back in the best borrowers from previously declined populations." Thus, we did not want the loan acceptance policies/strategies from 2012 and before to influence our models, since they are not representative of the way Lending Club accepts loans today.

When we looked through the 2013-2014 data, we noticed that many columns included forward-looking information regarding whether or not a borrower had defaulted on his/her loan. These columns included "total_pymnt" (total payments received to date for total amount funded), "total_rec_prncp" (principal received to date), "last_pymnt_d" (the last month a payment was received), and "last_pymnt_amnt" (last total payment amount received). Other future-looking columns began with words such as "hardship," "debt_settlement," and "settlement." We ignored these columns for the rest of our analysis since this information would not be available to an investor at the time of investment.

Lastly, we ignored columns that might implicitly discriminate against individuals of certain socio-economic classes. Such features include "zip_code" and "addr_state" since important information regarding a person can be inferred from the location of his/her residence.

After selecting features that we thought could help us predict whether or not an individual will default on a loan, we explored the associations between many of the features and the defaulted loans. Below we show our some of our exploratory data analysis of features that would eventually be used to model whether an individual would default on a loan.

























<hr>

## Does loan amount differ between loans that paid back and those that are defaulted on?








![png](EDA_for_final_files/EDA_for_final_7_0.png)




The distributions of loan amounts for both paid and defaulted loans overlap quite a bit. However, there is a slight left shift in the distribution for loan amounts that were paid back, indicating that loans with lower amounts have a good chance of being paid back. This could possibly be exploited for higher rates of return.
<hr>

## Do interest rates differ between loans that paid back and those that are defaulted on?






















![png](EDA_for_final_files/EDA_for_final_12_0.png)




Interest rate could also be a good predictor of defaulted loans since the distribution of interest rates for paid-back loans is slightly shifted to the left compared to the distribution of interest rates for defaulted loans. The means of the two distributions show some separation as well. We would expect that borrowers, who are given a lower interest rate, pay back their loans more often, most likely because it presents less of a financial burden on them. 
<hr>

## How does loan grade relate to default rate?

We can look at the default rate of loans (percentage of loans that default for a given category) with different loan grades (the result of a [formula](https://www.lendingclub.com/foliofn/rateDetail.action) that takes into account not only credit score, but also a combination of several indicators of credit risk from the credit report and loan application). Since the grade of a loan is tied with its interest rate, we would expect that high grade loans (A & B loans) have lower default rates than lower grade loans.















![png](EDA_for_final_files/EDA_for_final_16_0.png)




As expected, we see that higher grade loans (A & B) have much lower rates of default than lower grade loans (E, F, G). Thus, loan grade should be a strong feature in predicting whether a future borrower will default on a loan.
<hr>

## Is years of employment related to defaulting on a loan?

We will investigate if the number of years a borrowers has been employed has a relationship with whether a borrower paid back or defaulted on a loan.












![png](EDA_for_final_files/EDA_for_final_20_0.png)




For the most part, number of years employed does not differentiate between borrowers that paid back their loan and those that defaulted. However, we do see that a large number of borrowers that have been employed for 10+ years pay back their loans. Thus, this could be a useful feature for predicting whether a borrower will default.

Let's see if the rate of default really differs for borrowers with 10+ years of employment.








<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Years employed</th>
      <th>Average Interest Rate</th>
      <th>Default Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th></th>
      <td>1 year</td>
      <td>0.139343</td>
      <td>0.211387</td>
    </tr>
    <tr>
      <th></th>
      <td>10+ years</td>
      <td>0.141005</td>
      <td>0.221191</td>
    </tr>
    <tr>
      <th></th>
      <td>2 years</td>
      <td>0.139434</td>
      <td>0.212185</td>
    </tr>
    <tr>
      <th></th>
      <td>3 years</td>
      <td>0.139317</td>
      <td>0.210105</td>
    </tr>
    <tr>
      <th></th>
      <td>4 years</td>
      <td>0.139589</td>
      <td>0.210993</td>
    </tr>
    <tr>
      <th></th>
      <td>5 years</td>
      <td>0.140833</td>
      <td>0.209720</td>
    </tr>
    <tr>
      <th></th>
      <td>6 years</td>
      <td>0.141017</td>
      <td>0.215693</td>
    </tr>
    <tr>
      <th></th>
      <td>7 years</td>
      <td>0.141247</td>
      <td>0.217224</td>
    </tr>
    <tr>
      <th></th>
      <td>8 years</td>
      <td>0.140500</td>
      <td>0.222300</td>
    </tr>
    <tr>
      <th></th>
      <td>9 years</td>
      <td>0.140685</td>
      <td>0.230964</td>
    </tr>
    <tr>
      <th></th>
      <td>&lt; 1 year</td>
      <td>0.139052</td>
      <td>0.220092</td>
    </tr>
  </tbody>
</table>
</div>




Default rate does not actually seem to vary with how long a borrower has been employed. It is possible that combined with other features that employment length could be a predictive of default.
<hr>

## Does default rate vary with purpose of the loan?















![png](EDA_for_final_files/EDA_for_final_26_0.png)




For the most part, the default rates for loan purpose hover between 15-20%. The default rates for 'debt consolidation' and 'moving' are slightly higher, while the default rate for 'small business' is slightly over 30%. These loan purpose categories could be useful predictors of whether or not a borrower will default on his/her loan.
<hr>

## Can total credit utilization predict defaulted loans?

Let's see if 'revol_util' (the amount of credit the borrower is using relative to all available revolving credit) has any relationship with whether borrowers will default on their loans. We will call this 'total credit utilization'. Individuals with higher credit utilization rate could be riskier individuals to lend to, since they are already carrying a high debt.






















![png](EDA_for_final_files/EDA_for_final_31_0.png)




The distributions of 'total credit utilization' for borrowers that paid back their loans versus borrowers that defaulted overlap quite a bit. The distribution for borrowers than paid back their loans is a bit left shifted, indicating that borrowers with lower total credit utilization tend to pay back their loans more often. However, it is unclear if total credit utilization is a good predictor.
<hr>

## Is debt-to-income ratio (dti) predictive of defaulted loans?

Let's see if 'dti' (a ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income.) has any relationship with whether borrowers will default on their loans.








![png](EDA_for_final_files/EDA_for_final_34_0.png)




Similar to 'interest rate' and 'total credit utilization', we see that the distribution of 'dti' for borrowers that paid back their loans is shifted to the left slightly when compared to the distribution of 'dti' for borrowers that defaulted. This predictor could also be useful in identifying future borrowers that will default on their loans.
<hr>

## Is home ownership status associated with default rate?

We would also like to see if there is any relationship between the 'home owenership status' of borrowers and defaulting on a loan. 'Home owenrship status' tells us whether a borrower owns, rents, or has a mortage for a home.





























![png](EDA_for_final_files/EDA_for_final_40_0.png)




Default rates do not vary between the different categories of 'home owenership status' all that much, so it does not seem to have strong predictive power on whether a borrower will default on a loan.
<hr>

## Conclusion

Our EDA analysis shows that there are some helpful features, such as loan grade, purpose, and interest rate, for predicting whether or not a borrower will default on his/her loan. Our next step is to use all of the features described above and several others to train different models for prediciting whether or not a borrower will default on a loan. 
