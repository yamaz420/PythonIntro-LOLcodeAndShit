class Utils:
    
    @staticmethod # Annotation
    def get_int_input(prompt):
        choice = None
        while True:
            try: 
                choice = int(input(prompt))
                return choice
            except:
                print("ERROR only integers allowed")

