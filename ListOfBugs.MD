# Bug Fixes

## 1. Session Loading Bug

**Symptom:** Session loading issue.  
**Solution:** Added functionality to hash incoming token before comparing with token in DB.

## 2. Incorrect URLs in Frontend

**Symptom:** Frontend contains incorrect URLs.  
**Solution:** Correct the URLs in the frontend code.

## 3. Commit Transaction in users.py (Line 38)

**Symptom:** Missing transaction commit in users.py at line 38.  
**Solution:** Add the necessary code to commit the transaction and update the User entity.

## 4. Syntax Error in users_db.py (Line 54)

**Symptom:** Missing ")" in users_db.py at line 54.  
**Solution:** Add the missing ")" at line 54.

## 5. CORS Policy on Backend

**Symptom:** CORS policy issue on the backend.  
**Solution:** Implement proper CORS policy handling.

## 6. Missing "Password" in SQL Query (Line 16 of users_db.py)

**Symptom:** SQL query in users_db.py at line 16 is missing "password."  
**Solution:** Include "password" in the SQL query at line 16.

## 7. Incorrect Field in SQL Query (users_db.py - Line 76)

**Symptom:** Incorrect field "fav_colour" in SQL query at line 76 in users_db.py.  
**Solution:** Correct the SQL query to include the right field.
