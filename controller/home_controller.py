import sys
from view import display
from controller import students_controller
# aici a modificat luca

def choose():
    option = display.get_inputs(["Please enter a number: "], "")[0]
    if option == '1':
        students_controller.submenu()
    elif option == '2':
        display.print_message("Not implemented yet.", True)
    elif option == '0':
        display.print_message("I ruining your code and there is nothing you can do to stop me!!!!!!")
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    display.print_message("Welcome to 'Universidad Técnica de Buenas Maneras y Pistoleros!'")
    main_options = ["Exit program",
                    "School Students",
                    "Statistics"]
    display.print_menu("Main Menu", main_options)


def menu():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            display.print_message(str(err), True)
