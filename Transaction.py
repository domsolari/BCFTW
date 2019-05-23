class Transaction:
    """We create a class for our transactions and define that our creditor and debtor should be a string
    and the amount should be an integer"""
    creditor: str
    debtor: str
    amount: int

    # We define the allowed bank institutions for our specific example, we included big swiss financial institutions
    allowed_institutions = ["ubs", "ubs group ag", "cs", "credit suisse group ag",
                            "julius baer", "the pictet", "bank lombard odier & co", "raiffeisen", "postfinance",
                            "alternative bank schweiz", "banque bonhôte & cie sa", "cim bank", "bank cler",
                            "j. safra sarasin", "migros bank", "swissquote", "vontobel", "wir bank",
                            "zurich cantonal bank", "zkb"]

    # Define the chosen central bank, in our case the snb
    central_bank = "snb"

    def __init__(self):
        """The init method can be considered as the constructor of our class, it determines the flow"""
        self.creditor = self.collect_institution("Enter Creditor", True)
        # The collect_institution method is used with arguments:
        # message : "Enter Creditor" and central_bank_is_allowed : TRUE
        if self.is_institution_central_bank(self.creditor):
            # Check whether SNB was entered as creditor input
            self.debtor = self.collect_institution("Enter Debtor", False)
            # If the snb was entered, we ask for the debtor which must be an institution and cannot be the snb again
        else:
            # If an allowed institution is entered as creditor, the debtor must be the snb
            self.debtor = self.central_bank
            print("The Debtor is SNB")
        self.amount = self.collect_amount()
        # Finally, we use the collect_amount method to get amount of the transaction

    def __repr__(self):
        """Defines the string representation of the object"""
        return "(C={0}|D={1}|A={2})".format(self.creditor, self.debtor, str(self.amount))
        # C = Creditor, D = Debtor, A = Amount

    def collect_institution(self, message, central_bank_is_allowed):
        # With this method we want to collect the creditor as well as the debtor. Before we used two
        # different methods, see deprecated below.
        user_input = input("{0}: ".format(message)).lower()
        # ask for input and convert into lower case
        if central_bank_is_allowed:
            # If central_bank_is allowed : TRUE
            is_central_bank = self.is_institution_central_bank(user_input)
            # uses the method is_institution_central_bank delivers TRUE FALSE and stores it
            if is_central_bank:
                # If is_central_bank TRUE, we know that the user_input must be SNB, if not, we continue with
                # checking the validity of the user input
                return self.central_bank
                # Finally, if snb is entered, the method returns snb and it will be stored
        is_valid_institution = user_input in self.allowed_institutions
        # delivers TRUE/FALSE, now we want to check whether the user entered a valid institution
        # We check whether the input is within the list of allowed institutions
        if not is_valid_institution:
            # Here we check the TRUE/FALSE variable is_valid_institution
            print("Invalid Institution, try again")
            # We print this message if is_valid_institution is FALSE
            return self.collect_institution(message, central_bank_is_allowed)
            # We return the function again and ask the user to enter a true input
        return user_input
        # if is_valid_institution is TRUE, the user input will be returned

    def is_institution_central_bank(self, institution):
        """This method checks whether the user_input is the central bank or not, delivers TRUE or FALSE"""
        return institution == self.central_bank

    def collect_amount(self):
        """This method is used to get the amount entered by the user"""
        input_amount = input("Enter Transaction in CHF: ")
        # Store the user input
        try:
            # We check whether the amount is an integer or not
            amount = int(input_amount)
        except ValueError:
            print("Invalid Amount")
            return self.collect_amount()
            # When the user did not enter an integer, and error message appears and the method will be used again
        if amount <= 0:
            # Check whether the entered amount is positive
            print("Amount must be positive")
            return self.collect_amount()
            # Return the function again if the amount is not positive
        return int(input_amount)
        # Return the amount value and store it

    # Deprecated, please do not longer use these methods
    def collect_creditor(self):
        input_creditor = input("Enter Creditor: ").lower()
        # validate creditor
        is_valid_institution = input_creditor in self.allowed_institutions  # delivers TRUE/FALSE
        is_central_bank = input_creditor == self.central_bank  # delivers TRUE/FALSE
        if is_valid_institution or is_central_bank:
            print("Invalid Creditor")
            return self.collect_creditor()  # watch out for the self. !!!
        return input_creditor  # delivers our creditor

    # Deprecated
    def collect_debtor(self):
        input_debtor = input("Enter Debtor: ").lower()
        # validate debtor
        allowed_debtor = self.allowed_institutions
        if input_debtor not in allowed_debtor:
            print("Invalid Debtor")
            return self.collect_debtor()  # Keep the input_creditor value!
        return input_debtor
