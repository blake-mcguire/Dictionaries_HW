# TASK 1 Add new category called beverages with at least 2 items update the price of steak and remove brushetta


restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Soda": 1.99, "Water": 0.00}
restaurant_menu["Main Course"]["Steak"] = 20.99
del restaurant_menu["Starters"]["Bruschetta"]


# TASK 2 Customer Tickets

open_tickets = {}

def open_ticket(tickets, ticket_id):
    name = input("Enter the customer's name: ")
    issue = input("Enter the issue description: ")
    status = "Open"
    tickets[ticket_id] = {"Customer Name": name, "Issue Description": issue, "Status": status}
    return tickets

def close_ticket(tickets):
    ticket_id = int(input("Enter the ticket ID: "))
    if ticket_id in tickets:
        if tickets[ticket_id]["Status"] == "Open":
            tickets[ticket_id]["Status"] = "Closed"
            print(f"Ticket ID: {ticket_id} has been closed.")
        else:
            print("Ticket is already closed.")
    else:
        print("That ticket does not exist")
    return tickets

def display_tickets(tickets):
    ticket_display = input("Would you like to see open or closed tickets or all tickets? ").lower()
    if ticket_display in ["open", "closed", "all"]:
        for ticket_id, ticket in tickets.items():
            if ticket_display == "all" or ticket["Status"].lower() == ticket_display:
                print(f"Ticket ID: {ticket_id} | Customer Name: {ticket['Customer Name']} | Issue Description: {ticket['Issue Description']} | Status: {ticket['Status']}")
    else:
        print("Please enter 'open', 'closed', or 'all'")

def main(tickets):
    ticket_id = 1
    while True:
        response = input("""
                         
                        Whataburger Customer Tickets
                        
                         1. Open a new ticket
                         2. Close a ticket
                         3. Display tickets
                         4. Quit
                         
                         What would you like to do? """)
        
        if response == '1':
            open_ticket(tickets, ticket_id)
            ticket_id += 1
        elif response == '2':
            close_ticket(tickets)
        elif response == '3':
            display_tickets(tickets)
        elif response == '4':
            break
        else:
            print('Please enter a valid input')


main(open_tickets)