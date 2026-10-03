from assistant import ChooseWarranty
from assistant import ChoosePriority
from assistant import GetNumber
from assistant import ServicePrinter


class Devices:
    def __init__(self, name, phone_number, device, brand, model, warranty):
        self.name = name
        self.phone_number = phone_number
        self.device = device
        self.brand = brand
        self.model = model
        self.warranty = warranty


class ServiceRecord:
    def __init__(self, service_number, device, breakdown, priority):
        self.service_number = service_number
        self.device = device
        self.breakdown = breakdown
        self.priority = priority
        self.status = "Pending..."
        self.actions = []
        self.costs = []

    def total_cost(self):
        total = 0
        for cost in self.costs:
            description = cost["description"].lower()
            if not (self.device.warranty == "yes" and "işçilik" in description):
                total += cost["amount"]
            else:
                print("Cihaz garanti kapsamında.\nİşçilik ücreti eklenmedi.")
        return total


class TechnicalServices:
    def __init__(self):
        self.services = []

    def add_service(self):
        customer_name = input("Customer Name: ")
        phone = input("Phone Number: ")
        device_type = input("Device Type: ")
        brand = input("Brand: ")
        model = input("Model: ")
        warranty = ChooseWarranty().choose()
        problem_description = input("Problem Description: ")
        priority = ChoosePriority().choose()
        device = Devices(customer_name, phone, device_type, brand, model, warranty)
        service_number = GetNumber().service_number
        service_record = ServiceRecord(
            service_number, device, problem_description, priority
        )
        self.services.append(service_record)

    def list_services(self):
        if (
            not self.services
        ):  # liste boş mu diye kontrol için eğer liste boşsa false döndürür.
            print("No service records found.")
        else:
            for service in self.services:
                ServicePrinter().print_service(service)

    def search_service(self):
        num = input("Service Number: ")

        for service in self.services:
            if service.service_number == num:
                return service

    def update_status(self):
        service = self.search_service()
        if not service:
            print("Service record not found.")
        else:
            print("1-Pending")
            print("2-Under Review")
            print("3-Waiting for Parts")
            print("4-Being Repaired")
            print("5-Completed")
            print("6-Delivered")
            while True:
                try:
                    choice = int(input("Your status: "))
                except ValueError:
                    print("Please enter a number.")
                    continue
                if choice == 1:
                    service.status = "Pending"
                    break
                elif choice == 2:
                    service.status = "Under Review"
                    break
                elif choice == 3:
                    service.status = "Waiting for Parts"
                    break
                elif choice == 4:
                    service.status = "Being Repaired"
                    break
                elif choice == 5:
                    service.status = "Completed"
                    break
                elif choice == 6:
                    service.status = "Delivered"
                    break
                else:
                    print("Invalid choice.Try again.")

    def add_operation(self):
        service = self.search_service()
        if not service:
            print("Service record not found.")
        else:
            operation = input("What is your new operation?")
            if operation in service.actions:
                print("Operation already exists.")
            else:
                service.actions.append(operation)
                print("Operation added succesfully.")

    def add_cost(self):
        service = self.search_service()
        if not service:
            print("Service record not found.")
        else:
            description = input("Description: ")
            try:
                amount = int(input("How much did it cost: "))
            except ValueError:
                print("Please enter a valid amount.")
                return

            cost = {"description": description, "amount": amount}
            service.costs.append(cost)
            print("Cost added successfully.")

    def list_by_status(self):
        print("1-Pending")
        print("2-Under Review")
        print("3-Waiting for Parts")
        print("4-Being Repaired")
        print("5-Completed")
        print("6-Delivered")
        try:
            choice = int(input("The situation you want to list: "))
        except ValueError:
            print("Please enter a number.")
            return

        if choice == 1:
            status = "Pending"

        elif choice == 2:
            status = "Under Review"

        elif choice == 3:
            status = "Waiting for Parts"

        elif choice == 4:
            status = "Being Repaired"

        elif choice == 5:
            status = "Completed"

        elif choice == 6:
            status = "Delivered"

        else:
            print("Invalid choice! Try again.")
            return

        found = False

        for service in self.services:
            if service.status == status:
                ServicePrinter().print_service(service)
                found = True
        if not found:
            print("No service records found with this status.")

    def statistics(self):
        pending = 0
        under_review = 0
        waiting_for_parts = 0
        being_repaired = 0
        completed = 0
        delivered = 0
        for service in self.services:
            if service.status == "Pending":
                pending += 1
            elif service.status == "Under Review":
                under_review += 1
            elif service.status == "Waiting for Parts":
                waiting_for_parts += 1
            elif service.status == "Being Repaired":
                being_repaired += 1
            elif service.status == "Completed":
                completed += 1
            elif service.status == "Delivered":
                delivered += 1

        print("Service Statistics")
        print("------------------")
        print("Total Services:", len(self.services))
        print("Pending:", pending)
        print("Under Review:", under_review)
        print("Waiting for Parts:", waiting_for_parts)
        print("Being Repaired:", being_repaired)
        print("Completed:", completed)
        print("Delivered:", delivered)
