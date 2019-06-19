# Impact of Manhattan Congestion Surcharge on For-Hire Vehicles
This is our Capstone project which spans across 2 semesters as a part of our Masters in Urban Data Science at NYU CUSP. The team members are Katie Voorhees, Rufei Sheng, Sam Manzi, Soham Mody and Xiaoning He and our sponsors are Prof. Stan Sobolevsky and Arcadis NV. 

We are evaluating the effectiveness of the congestion surcharge policy implemented in Manhattan(from February 2019) that is, whether the current congestion price is appropriate or should it be lower or higher. We are also assessing the urban transportation pattern under this new policy using a choice model between private transportation,public transportation, taxis and for-hire-vehicles in order to find if there has been a mode shift due to this change in pricing.

In order to do these, we are creating simulations of the transportation choices made by commuters for each origin-destination pair and we are assuming that these choices depend on the value of utility of that mode for the commuter while choosing a mode. The utility function here is: 

Utility = Lambda * (Time taken * Wages per hour + Total cost of the commute)

Where Lambda is a constant parameter that needs to be tuned.

The modes chosen by us for this model are walking, subway, taxis, for-hire vehicles and shared for-hire vehicles. We decided to use a nested multinomial logit model instead of the traditional multinomial logit model to predict the transportation choice proportions as the choices between taxis and for-hire vehicles is extremely correlated and that would create an unfair imbalance towards those when the model predicts the probability of choosing each mode.

The current surcharge policy has already been implemented but, talks of a bigger surcharge policy that will be applicable to all vehicles in NYC (not just taxis) is underway and this research hopes to also help in making a data-driven decision on whether that policy should be introduced or not. 
