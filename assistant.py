class ChoosePriority:
    def choose(self):
        while True:
            try:
                choice = int(input("Your priority: "))
            except ValueError:
                print("Please enter a number.")
                continue

            if choice == 1:
                return "Low"
            elif choice == 2:
                return "Normal"
            elif choice == 3:
                return "High"
            elif choice == 4:
                return "Urgent"
            else:
                print("Invalid choice.Try Again.")


class GetNumber:
    counter = 1001

    def __init__(self):
        self.service_number = "SRV-" + str(GetNumber.counter)
        GetNumber.counter += 1


class ChooseWarranty:
    def choose(self):
        while True:
            choice = input("Is the device under Warranty? (yes/no): ").lower()

            if choice == "yes" or choice == "no":
                return choice
            else:
                print("Invalid Choice.Try Again.")


class ServicePrinter:
    def print_service(self, service):
        print("-----------------------------------")
        print("Service No: " + service.service_number)
        print("Customer: " + service.device.name)
        print("Device: " + service.device.device)
        print("Problem: " + service.breakdown)
        print("Priority: " + service.priority)
        print("Status: " + service.status)
        print("Operations: ")
        for act in service.actions:
            print("-" + act)
        print("Costs: ")
        for cost in service.costs:
            print("- " + cost["description"] + ": " + str(cost["amount"]))
        print("Total: " + str(service.total_cost()))
