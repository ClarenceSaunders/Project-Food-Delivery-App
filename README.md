# Food Delivery Dataset Analysis
## 🍕 Live App

👉 [Click here to use the Streamlit App](https://food-delivery-app-icc9dpbcozpz6kqxz2yfit.streamlit.app/)

## Problem Statement
In the rapidly growing food delivery industry, understanding customer order patterns and behaviors is critical for improving service efficiency and satisfaction. This analysis aims to uncover insights from a comprehensive food order dataset.


## Data Dictionary

The dataset consists of the following columns:

1. **order_id**: Unique identifier for each order.
2. **customer_id**: Unique identifier for each customer.
3. **restaurant_name**: The name of the restaurant where the order was placed.
4. **cuisine_type**: The type of cuisine offered by the restaurant.
5. **cost_of_the_order**: The total cost associated with the order, including food, taxes, and delivery.
6. **day_of_the_week**: The day of the week the order was placed.
7. **rating**: Customer rating of the order (from 1 to 5).
8. **food_preparation_time**: Time taken to prepare the food before it was sent for delivery.
9. **delivery_time**: Time taken for the order to be delivered after it was prepared.

## Visualizations

### 1. Distribution of Cost of Order
The Order Cost Distribution visualization depicts the frequency of various order values to understand revenue trends. Based on the graph most of the delivery orders price range fall mostly between $10-$15 dollars while the average price falls at $16.50 dollars.

### 2. Customer Rating vs. Order Value Relationship
This scatterplot shows the correlation between customer ratings and order values, helping identify trends and insights regarding customer satisfaction versus spending. the ratings mostly steer towards 4 and 5-star ratings for orders costing between $10-$20 dollars.

## Business Recommendations

1. **Optimize Delivery Times**:
   - **Action**: Analyze delivery time data to streamline logistics.
   - **Expected Impact**: Reduce average delivery times by 20%, improving customer satisfaction.

2. **Enhance Customer Engagement**:
   - **Action**: Implement a loyalty program based on customer_id.
   - **Expected Impact**: Increase repeat orders by 30%.

3. **Menu Personalization**:
   - **Action**: Tailor restaurant offerings based on popular cuisine_type.
   - **Expected Impact**: Increase sales from popular cuisine categories by 25%.

4. **Pricing Strategy Analysis**:
   - **Action**: Review and adjust pricing based on cost_of_the_order and customer feedback.
   - **Expected Impact**: Improve average order value by 15%.

5. **Improve Food Preparation Efficiency**:
   - **Action**: Train kitchen staff to reduce food_preparation_time.
   - **Expected Impact**: Enhance order turnover rate and customer satisfaction.

6. **Customer Feedback Collection**:
   - **Action**: Introduce a systematic method to gather and analyze customer ratings.
   - **Expected Impact**: Achieve a customer satisfaction rating increase of 10%.

7. **Targeted Marketing Campaigns**:
   - **Action**: Use customer_id data to personalize marketing efforts.
   - **Expected Impact**: Boost marketing response rates by 20%.
