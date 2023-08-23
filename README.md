# finstar_test
Test task for Finstar

Install libraries
pip install -r requirements.txt

Run postgresql docker-compose
docker-compose up -d

Run ./init_db.py

## Connect Power BI to PostgreSQL:

Get PostgreSQL Connection Information:
You will need the connection details for your PostgreSQL database:

Hostname or IP address
Port number (default is usually 5432)
Database name
Username and password
Open Power BI Desktop:
Launch Power BI Desktop on your computer.

Connect to PostgreSQL:

Click on "Home" in the top menu.
Click on "Get Data" and then select "Database."
Choose "PostgreSQL" from the list.
Enter Connection Details:

In the PostgreSQL database window, enter the server (hostname or IP address) and database details.
Select the appropriate authentication method: "Database" (username and password) or "Windows" (if you're using integrated Windows authentication).
Click on "Connect."
Enter Database Credentials:

Enter your PostgreSQL username and password.
You might also need to select the privacy level for your data. Choose the appropriate option for your needs.
Import Data:

After successfully connecting, you will see a Navigator window. Choose the tables/views you want to import into Power BI.
You can also write custom SQL queries if needed.
Transform Data (Optional):

Use Power BI's data transformation capabilities to clean, reshape, or combine data from different tables.
Load Data:

Once you've selected and transformed the data as needed, click the "Load" button to import the data into Power BI.