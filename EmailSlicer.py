email_id = input("Enter Email Address - ").strip()

username = email_id[:email_id.index('@')]

domain = email_id[email_id.index('@')+1:]

print(f"Username - {username}")
print(f"domain - {domain}")