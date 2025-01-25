import random

MAX_LINES=3
MIN_TOKEN=1
MAX_TOKENS=50

ROWS=3
COLS=3
symbols_count = {
    "♠️":5,
    "♥️":4,
    "♦️":6,
    "♣️":8,
}

symbol_value={
    "♠️":6,
    "♥️":8,
    "♦️":4,
    "♣️":2
}

def check_winnings(columns,lines,tokens,values):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check= column[line]
            if symbol!= symbol_to_check:
                break
        else:
            winnings+=values[symbol]*tokens
            winnings_lines.append(line+1)
    return winnings,winnings_lines


def slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbols_count in symbols.items():
        for _ in range (symbols_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")
        print()

def deposit():
    while True:
        amount = input("Enter No of tokens to deposit:🃏  ")
        if amount.isdigit():
           amount = int(amount)
           if amount>0:
               break
           else:
               print("enter a valid no of tokens(greater than 0)")
        else:
            print(" Numbers only" )
    return amount


def Num_of_Lines():
    while True:
        Lines = input("Enter No of Lines You Choose To Put Tokens(1 - 3):")
        if Lines.isdigit():
           Lines = int(Lines)
           if 1<=Lines<=MAX_LINES:
               break
           else:
               print("Enter a valid no of lines")
        else:
            print(" Numbers only" )
    return Lines

def No_of_tokens_Placed():
        while True:
            amount = input("Enter No of tokens you chose to place for each line:🃏  ")
            if amount.isdigit():
                amount = int(amount)
                if MIN_TOKEN<=amount<=MAX_TOKENS:
                    break
                else:
                    print(f"enter a no.of.tokens between {MIN_TOKEN}🃏 and {MAX_TOKENS}🃏:")
            else:
                print(" Numbers only" )
        return amount
    

def spin(Balance):
    lines = Num_of_Lines()
    tokens = No_of_tokens_Placed()
    
    if Balance == 0:
        print("Your Balance Is 0...So See You Later!!")
        return 0  
    
    while True:
        if tokens > Balance:
            print(f"You don't have enough tokens. Your current balance is {Balance}🃏.")
        elif Balance == 0:
            break
        else:
            break
    
    print(f"You are placing {tokens}🃏 tokens on {lines} lines.")
    
    slots = slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    
    winnings, winnings_line = check_winnings(slots, lines, tokens, symbol_value)
    if winnings>0:    
        print(f"You won {winnings}🃏 tokens.")
        print(f"You won those tokens on lines {winnings_line}.")
    else:
        print("you won nothing this time!!")
    
    return winnings - tokens  



def main():
    while True:
        answer= input("Press Enter To Play Or Type 'q' to quit ")
        if answer=="q":
            print("See You Later👋👋")
            break    
        else:
            Balance = deposit()
            while True:
                print(f"Current 🃏Token Balance is: {Balance}")
                if Balance==0:
                    break 
                else:
                    answer= input("Are You Sure Want To Play !! If Not Press 'q' to Quit With Current Balance ")
                    if answer=="q":
                        print("See You Later👋👋")
                        break
                    else:
                        Balance+=spin(Balance)
        if Balance==0:
            print("Ouch you Lost Everything!! See You Later")
            break
        else:
            print(f"You left With {Balance}🃏 Tokens")
            break
        

main()
