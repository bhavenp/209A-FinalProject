---
title: EDA
notebook: EDA_for_final.ipynb
nav_include: 3
---




We began by looking at the accepted loan data from the years 2013 and 2014. We did not look at loan data prior to 2013 because Lending Club [changed its underwriting policy in late 2012](https://www.lendacademy.com/lending-club-underwriting-changes/), which "removed the highest risk borrowers that were previously being approved and... added back in the best borrowers from previously declined populations." Thus, we did not want the loan acceptance policies/strategies from 2012 and before to influence our models, since they are not representative of the way Lending Club accepts loans today.

























<hr>

## Plot distribution of loan amounts for Paid and Defaulted loans








![png](EDA_for_final_files/EDA_for_final_7_0.png)




There is a slight left shift in the distribution for loan amounts that were paid back, which could possibly be exploited for higher rates of return.
<hr>

## Plot distribution of interest rates for Paid and Defaulted loans






















![png](EDA_for_final_files/EDA_for_final_12_0.png)




Interest rate could also be a good predictor of defaulted loans since the distribution of interest rates for paid-back loans is slightly shifted to the left compared to the distribution of interest rates for defaulted loans. The means of the two distributions show some separation as well. We would expect that borrowers who are given a lower interest rate pay back their loans more often, most likely because it present less of a financial burden on them. 
<hr>

## How does loan grade relate to default rate?

We can look at the default rate of loans with different grades (the grade of the loan assinged by Lending ClubWe would expect loan grade (the result of a formula that takes into account not only credit score, but also a combination of several indicators of credit risk from the credit report and loan application (from Lending Club website)). Since the grade of a loan is tied with its interest rate, we would expect that high grade loans (A & B loans) have lower default rates than lower grade loans.








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
      <th>int_rate</th>
      <th>Default</th>
      <th>funded_amnt</th>
    </tr>
    <tr>
      <th>grade</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>0.075609</td>
      <td>0.057356</td>
      <td>14765.524662</td>
    </tr>
    <tr>
      <th>B</th>
      <td>0.114474</td>
      <td>0.133106</td>
      <td>13580.172747</td>
    </tr>
    <tr>
      <th>C</th>
      <td>0.146564</td>
      <td>0.243030</td>
      <td>14619.361694</td>
    </tr>
    <tr>
      <th>D</th>
      <td>0.176240</td>
      <td>0.329321</td>
      <td>15310.466717</td>
    </tr>
    <tr>
      <th>E</th>
      <td>0.207821</td>
      <td>0.406546</td>
      <td>17369.291467</td>
    </tr>
    <tr>
      <th>F</th>
      <td>0.241303</td>
      <td>0.427656</td>
      <td>17778.409947</td>
    </tr>
    <tr>
      <th>G</th>
      <td>0.257392</td>
      <td>0.504119</td>
      <td>20738.681836</td>
    </tr>
  </tbody>
</table>
</div>











![png](EDA_for_final_files/EDA_for_final_16_0.png)




As expected, we see that higher grade loans (A & B) have much lower rates of default than lower grade loans (E, F, G). Thus, loan grade should be a strong feature in predicting whether a future borrower will default on a loan.
<hr>

## Plot distribution of employment years for Paid and Defaulted loans

We will investigate if the number of years employed has a relationship with whether a borrower paid back or defaulted on a loan.












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
      <th>Mean Interest Rate</th>
      <th>Default Rate</th>
    </tr>
    <tr>
      <th>emp_length</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1 year</th>
      <td>0.139343</td>
      <td>0.211387</td>
    </tr>
    <tr>
      <th>10+ years</th>
      <td>0.141005</td>
      <td>0.221191</td>
    </tr>
    <tr>
      <th>2 years</th>
      <td>0.139434</td>
      <td>0.212185</td>
    </tr>
    <tr>
      <th>3 years</th>
      <td>0.139317</td>
      <td>0.210105</td>
    </tr>
    <tr>
      <th>4 years</th>
      <td>0.139589</td>
      <td>0.210993</td>
    </tr>
    <tr>
      <th>5 years</th>
      <td>0.140833</td>
      <td>0.209720</td>
    </tr>
    <tr>
      <th>6 years</th>
      <td>0.141017</td>
      <td>0.215693</td>
    </tr>
    <tr>
      <th>7 years</th>
      <td>0.141247</td>
      <td>0.217224</td>
    </tr>
    <tr>
      <th>8 years</th>
      <td>0.140500</td>
      <td>0.222300</td>
    </tr>
    <tr>
      <th>9 years</th>
      <td>0.140685</td>
      <td>0.230964</td>
    </tr>
    <tr>
      <th>&lt; 1 year</th>
      <td>0.139052</td>
      <td>0.220092</td>
    </tr>
  </tbody>
</table>
</div>




Default rate does not actually seem to vary with how long a borrower has been employed. It is possible that combined with other features that employment length could be a predictive of default.
<hr>

## Does default rate or interest rate vary with purpose of the loan















![png](EDA_for_final_files/EDA_for_final_26_0.png)




For the most part, the default rates for loan purpose hover between 15-20%. The default rates for 'debt consolidation' and 'moving' are slightly higher, while the default rate for 'small business' is slightly over 30%. These loan purpose categories could be useful predictors of whether or not a borrower will default on his/her loan.
<hr>

## Revol util distribution for paid/defaulted loans

Let's see if 'revol_util' (the amount of credit the borrower is using relative to all available revolving credit) has any relationship with whether borrowers will default on their loans. We call this 'total credit utilization'. Individuals with higher credit utilization rate could be riskier individuals to lend to since they are already carrying a high debt.






















![png](EDA_for_final_files/EDA_for_final_31_0.png)




The distributions of 'percentage of total credit used' for borrowers that paid back their loans versus borrowers that defaulted overlap quite a bit. The distribution for borrowers than paid back their loans is a bit left shifted, but it is unclear if percentage of total credit is a good predictor.
<hr>

## DTI distribution for paid/defaulted loans

Let's see if 'dti' (a ratio calculated using the borrower’s total monthly debt payments on the total debt obligations, excluding mortgage and the requested LC loan, divided by the borrower’s self-reported monthly income.) has any relationship with whether borrowers will default on their loans.








![png](EDA_for_final_files/EDA_for_final_34_0.png)




Similar to 'interest rate' and 'total credit utilization', we see that the distribution of 'dti' for borrowers that paid back their loans is shifted to the left slightly when compared to the distribution of 'dti' for borrowers that defaulted. This predictor could also be useful in identifying future borrowers that will default on their loans.
<hr>

## Home ownership status compared to default rate

We would also like to see if there is any relationship between 'home owenership status' and defaulting on their loans. 'Home owenrship status' tells us whether a borrower owns, rents, or has a mortage for a home; there is also a 'ANY' category, but it is unclear what this exactly refers to.















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
      <th>Count</th>
      <th>Default Rate</th>
      <th>Average Interest Rate</th>
    </tr>
    <tr>
      <th>home_ownership</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ANY</th>
      <td>1</td>
      <td>0.000000</td>
      <td>0.116700</td>
    </tr>
    <tr>
      <th>MORTGAGE</th>
      <td>192002</td>
      <td>0.208045</td>
      <td>0.137207</td>
    </tr>
    <tr>
      <th>OWN</th>
      <td>34258</td>
      <td>0.223101</td>
      <td>0.141891</td>
    </tr>
    <tr>
      <th>RENT</th>
      <td>144182</td>
      <td>0.233580</td>
      <td>0.144476</td>
    </tr>
  </tbody>
</table>
</div>


















![png](EDA_for_final_files/EDA_for_final_40_0.png)




Default rates do not vary between the different categories of 'home owenership status' all that much.
