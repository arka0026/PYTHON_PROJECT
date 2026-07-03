def validate_email(email):
    # Check if there is exactly one '@'
    # it is not at the start or end
    if email.count('@') != 1 or email.startswith('@') or email.endswith('@'):
        return False
    # Split the email into 'name' and 'domain.extension'
    name, domain_extension = email.split('@')
    # Ensure 'name' is not empty
    if not name:
        return False
    # Ensure 'domain.extension' has a dot
    # It is not at the start or end
    if '.' not in domain_extension or domain_extension.startswith('.') or domain_extension.endswith('.'):
        return False
    return True


result = validate_email("test@example.com")
print(result)