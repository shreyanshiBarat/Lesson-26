class Account:
    def __init__(self, owner, pin):
      self.owner = owner
      self.__pin = pin
    def show_pin_status(self):
       print("Owner: ", self.owner)

    def set_pin(self, new_pin):
       if len(new_pin) == 4 and new_pin.isdigit():
          self.__pin = new_pin

          print("Successful") 
       else:
          print("PIN should be for 4 digits")
    def check_pin(self, entered_pin):
       if entered_pin == self.__pin:
          print("Access granted.")
       else:
          
          print("Access denied.")

    def __str__(self):
       return self.owner

account = Account("Lisa", "6007")

print(account)

account._pin = "3894"
print("Changed Pin?")
account.check_pin("6007")
account.check_pin("3894")

account.set_pin("6007")

account.check_pin("3894")