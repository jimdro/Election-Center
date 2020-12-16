"""
Created by Dimitrios Drosos
email: dimitriss.drosos@gmail.com

"""
class Voter:
    """
    At this class i initiate voters name and age and some ohter parameters
    """

    def __init__(self, name,age, address = 0, identity=0):
        self.name = name
        self.address = address
        self.identity = identity
        self.age = age

        print("Welcome to our election center: " + self.name + ' ' + str(self.age))

    def name_eligibility(self):
        while True:
            if self.name == str:
                print("You gave a valid name")
                break
            elif self.name == '':
                print("Please try again")


    def age_eligibility(self):
        max_tries = 3
        while max_tries < 0:
            max_tries += 1
            if self.age == '' or self.age < 0:
                try:
                    if int(self.age < 18) or int(self.age > 65):
                        return False
                    else:
                        return True
                except Exception as error:
                    error_string = str(error)
                    print(error_string)
                    continue
                else:
                    break
                # finally:
                #     print("Please try again!")
            break
        else:
            print("Wrong, you have 3 tries in total\mPlease try again.")
        print("Please try again!")


    def identity(self):
        pass





