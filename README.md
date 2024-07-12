# Stock
A web stock about products with PostgreSQL linked in Supabase

The website has the functions to add products, remove, edit products and a button to view the details of each item.
A basic design.

It has 6 columns for each product: Id, Name, Description, Value, Available and Added moment.

Columns:\
ID - The IDs are ordered from the most expensive product to the least expensive.\
Name - name of the product added.\
Description - a few words about the item, it's not required.\
Value - a float number, only 2 decimal places, in reais.\
Available - a boolean condition where True(Yes) means available for selling and False(No) means not.\
Added moment - it records the moment you registered that item (yyyy/mm/dd/ - hour/minute/seconds).\

There is a env file in the .gitignore that contains the URL connection string and environment variables for my app.
So I won't expose the database to everyone in my GitHub.
