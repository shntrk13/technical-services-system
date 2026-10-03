from models import TechnicalServices
from assistant import ServicePrinter

print("====================================")
print("       Technical Services System")
print("====================================")
print("1 - New Services Record")
print("2 - List All Service Records")
print("3 - Search Service Record")
print("4 - Update Service Record")
print("5 - Add Operation")
print("6 - Add Cost")
print("7 - List Records by Status")
print("8 - Service Statistics")
print("9 - Exit")

technical_services = TechnicalServices()

while True:
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        technical_services.add_service()
    elif choice == 2:
        technical_services.list_services()
    elif choice == 3:
        service = technical_services.search_service()
        if not service:
            print("Service record not found.")
        else:
            ServicePrinter().print_service(service)
    elif choice == 4:
        technical_services.update_status()
    elif choice == 5:
        technical_services.add_operation()
    elif choice == 6:
        technical_services.add_cost()
    elif choice == 7:
        technical_services.list_by_status()
    elif choice == 8:
        technical_services.statistics()
    elif choice == 9:
        break
    else:
        print("Invalid choice!Try again.")
