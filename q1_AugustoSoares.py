SUC = "Success"
ERR = "Error"
CHK = "Checked"
WTD = "Witdraw completed."
DPS = "Deposit completed."

client = {
    "name": "Augusto",
    "email": "augusto@email.com",
    "password": "123",
    "balance": 50,
    "allowWithdraw": False
}

client_check = lambda name, password : SUC if name == client.get("name") and password == client.get("password") else ERR
withdraw = lambda client_checked, value: client.update({"balance": client.get("balance")-value}) if client_checked == SUC and client.get("allowWithdraw") == True else ERR
deposit = lambda client_checked, value: client.update({"balance": client.get("balance")+value}) if client_checked == SUC else ERR


print(client.get("balance"))
print(withdraw(client_check("Augusto", "123"), 50))
print(client.get("balance"))
print(deposit(client_check("Augusto", "123"), 120))
print(client.get("balance"))