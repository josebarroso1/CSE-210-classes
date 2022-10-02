class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)


    def print_parachute(self, lives):
        parachute = [" ___","/___\\","\\  /", "\\ /", "   O", "/ | \\", "/ \\" ]

        if lives== 3:
            parachute.pop(0)
        
        elif lives== 2:
            for i in range(2):
                parachute.pop(0)

        elif lives== 1:
            for i in range(3):
                parachute.pop(0)

        elif lives== 0:
            for i in range(4):
                parachute.pop(0)
            parachute[0] = "   x"

        for i in parachute:
            print[i]

    def print_puzzle(self, puzzle):
        word=""
        for i in puzzle:
            word += i
        print(f"\n{word}\n")

    def validate_answer(self, answer):
        valid_characters= "abcdefghijklmnopqrstuvwxyz".upper()
        if answer not in valid_characters:
            print("invalid, try again")
            return False
        elif len(answer) > 1:
            print("Invalid input")
            return False
        return True
