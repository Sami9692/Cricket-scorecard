from tkinter import*
from tkinter import simpledialog, messagebox

def show_input_summary(num_wickets, partnerships):
    input_summary = f"Number of wickets: {num_wickets}\n"
    input_summary += "\nPartnerships:\n"
    for wicket, partnership in enumerate(partnerships, start=1):
        input_summary += f"Wicket {wicket}: {partnership['runs']} runs, {partnership['fours']} fours, {partnership['sixes']} sixes, gi{partnership['dot_balls']} dot balls\n"

    messagebox.showinfo("Input Summary", input_summary)

def calculate_partnerships(wickets):
    partnerships = []

    for wicket in wickets:
        partnership = {}
        partnership['runs'] = simpledialog.askinteger("Partnership Input", f"Enter runs for wicket {wicket}: ")
        partnership['fours'] = simpledialog.askinteger("Partnership Input", f"Enter fours for wicket {wicket}: ")
        partnership['sixes'] = simpledialog.askinteger("Partnership Input", f"Enter sixes for wicket {wicket}: ")
        partnership['dot_balls'] = simpledialog.askinteger("Partnership Input", f"Enter dot balls for wicket {wicket}: ")

        partnerships.append(partnership)

    return partnerships

def find_highest_partnership(partnerships):
    highest_partnership = max(partnerships, key=lambda x: x['runs'])
    return highest_partnership

def display_output(num_wickets, partnerships, highest_partnership):
    input_summary = f"Number of wickets: {num_wickets}\n"
    input_summary += "\nPartnerships:\n"
    for wicket, partnership in enumerate(partnerships, start=1):
        input_summary += f"Wicket {wicket}: {partnership['runs']} runs, {partnership['fours']} fours, {partnership['sixes']} sixes, {partnership['dot_balls']} dot balls\n"

    output_message = f"\nHighest partnership: Runs {highest_partnership['runs']}, Fours {highest_partnership['fours']}, Sixes {highest_partnership['sixes']}"

    messagebox.showinfo("Input and Output", input_summary + output_message)

def main():
    root = Tk()
    root.withdraw()

    root.configure(background='black')
   
    
    num_wickets = simpledialog.askinteger( "Cricket Scorecard", "Number of wickets: ")
    wickets = list(range(1, num_wickets + 1))

    partnerships = calculate_partnerships(wickets)

    show_input_summary(num_wickets, partnerships)

    highest_partnership = find_highest_partnership(partnerships)

    display_output(num_wickets, partnerships, highest_partnership)

if __name__ == "__main__":
    main()

