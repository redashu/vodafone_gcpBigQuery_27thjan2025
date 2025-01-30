# 📌 BigQuery User-Defined Functions (UDFs)

Google BigQuery **User-Defined Functions (UDFs)** allow you to create **custom functions** using **SQL or JavaScript**, extending BigQuery's built-in capabilities.

---

## **🔹 Why Use UDFs?**
✅ **Reusable Code** – Avoid repeating complex SQL logic.  
✅ **Custom Business Logic** – Implement logic not available in built-in functions.  
✅ **Data Transformation** – Perform advanced string manipulations, cleansing, or calculations.  
✅ **Integration with External Systems** – Call external APIs using JavaScript UDFs.  

---

# **1️⃣ SQL-Based UDF**

### **🛠️ Use Case: Extract Domain from Email**
```sql
CREATE OR REPLACE FUNCTION my_dataset.extract_domain(email STRING) 
RETURNS STRING 
AS (
  SPLIT(email, "@")[SAFE_OFFSET(1)]
);

-- ✅ Usage Example:
SELECT extract_domain('john.doe@example.com');  -- Output: 'example.com'
```

---

# **2️⃣ JavaScript-Based UDF**

### **🛠️ Use Case: Check If a Number is Even or Odd**
```sql
CREATE OR REPLACE FUNCTION my_dataset.is_even(n INT64) 
RETURNS STRING 
LANGUAGE js 
AS """
  return (n % 2 === 0) ? 'Even' : 'Odd';
""";

-- ✅ Usage Example:
SELECT is_even(10);  -- Output: 'Even'
SELECT is_even(7);   -- Output: 'Odd'
```

---

# **3️⃣ JavaScript UDF for Data Cleaning**

### **🛠️ Use Case: Standardize Phone Numbers**
```sql
CREATE OR REPLACE FUNCTION my_dataset.clean_phone(phone STRING) 
RETURNS STRING 
LANGUAGE js 
AS """
  return phone.replace(/[^0-9]/g, ''); // Remove all non-numeric characters
""";

-- ✅ Usage Example:
SELECT clean_phone('(123) 456-7890');  -- Output: '1234567890'
```

---

# **4️⃣ SQL UDF for Complex Calculations**

### **🛠️ Use Case: Calculate Compound Interest**
```sql
CREATE OR REPLACE FUNCTION my_dataset.compound_interest(principal FLOAT64, rate FLOAT64, years INT64) 
RETURNS FLOAT64 
AS (
  principal * POW(1 + rate / 100, years)
);

-- ✅ Usage Example:
SELECT compound_interest(1000, 5, 10);  -- Output: 1628.89
```

---

# **5️⃣ JavaScript UDF to Format Dates**

### **🛠️ Use Case: Convert Date Format (YYYYMMDD → YYYY-MM-DD)**
```sql
CREATE OR REPLACE FUNCTION my_dataset.format_date(ymd STRING) 
RETURNS STRING 
LANGUAGE js 
AS """
  return ymd.slice(0, 4) + '-' + ymd.slice(4, 6) + '-' + ymd.slice(6, 8);
""";

-- ✅ Usage Example:
SELECT format_date('20250129');  -- Output: '2025-01-29'
```

---

# **🔹 When to Use UDFs vs. Built-in Functions**
| **Scenario**            | **Use UDF?** |
|-------------------------|-------------|
| Simple transformations  | ❌ No, use built-in functions (e.g., `SUBSTRING()`) |
| Complex logic with conditions | ✅ Yes, UDFs are useful |
| Custom calculations     | ✅ Yes, UDFs help reuse logic |
| Loops and external calls | ✅ Yes, use **JavaScript UDFs** |

---

# **📌 Limitations of UDFs**
⚠️ **Performance Overhead** – UDFs run row-by-row, which may be slower than built-in functions.  
⚠️ **No DML Operations** – UDFs cannot modify data (`INSERT`, `UPDATE`, etc.).  
⚠️ **No External API Calls** (in SQL UDFs) – Only **JavaScript UDFs** can perform external API requests.  

---

# **🔹 When to Use UDFs in Real Projects**
✔ **Log Data Processing** – Cleaning log files with regex.  
✔ **Customer Segmentation** – Classifying customers based on spend patterns.  
✔ **Data Standardization** – Converting phone numbers, addresses, etc.  
✔ **Financial Calculations** – Loan amortization, risk scores, etc.  

---

