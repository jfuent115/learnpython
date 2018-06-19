data = ("John", "Doe", 53.44)
message_template = ' Hello {} {}. Your current balance is ${}.'
message = message_template.format(*data)
print (message)