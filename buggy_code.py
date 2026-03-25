def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    result = db.execute(query)
    password = result['password']
    print("User password is: " + password)
    return result

def divide(a, b):
    return a / b  # b=0 hoga toh crash!

print("buggy code")
API_KEY = "sk-1234567890abcdef"  # hardcoded secret
