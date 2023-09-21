import matplotlib.pyplot as plt

class The_Carbon_Calculator:
    def __init__(self):
        self.constant = 12

    def obtain_valid_positive_float_value(self, prompt, error_message):
        # """Determines how much energy is consumed by input from the user.
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                else:
                    print(error_message)
            except ValueError:
                print(error_message)

    def Utilize_energy_calculator(self):
        # """Determines how much energy is consumed by input from the user.
        Electricity_bill = self.obtain_valid_positive_float_value("\nElectricity bill on average per month: ",
                                 "There is an error with the input. A valid number must be entered.") 
        gas_usage_bill = self.obtain_valid_positive_float_value("Gas bill average for a month: ",
                                "There is an error with the input. A valid number must be entered.")
        Expenses_for_fuel= self.obtain_valid_positive_float_value("Fuel bill on average per month: ", 
                                "There is an error with the input. A valid number must be entered.")

        #Calculate separately
        Electricity_bill_calc = Electricity_bill * 0.0005 * self.constant
        gas_usage_bill_calc = gas_usage_bill * 0.0053 * self.constant
        Expenses_for_fuel_calc = Expenses_for_fuel * 2.32 * self.constant

        # Calculation final
        result = Electricity_bill_calc + gas_usage_bill_calc + Expenses_for_fuel_calc
        return round(result, 2)

    def Waste_emissions_calculation(self):
        # Validate the user's input values
        Quantity_of_waste = self.obtain_valid_positive_float_value("\nAvg Wast per month: "
                                                     ,"There is an error with the input. A valid number must be entered.")
        while True:
            Recycling_percentage_of_waste = self.obtain_valid_positive_float_value("Avg Monthly  Recycled Percentage: "
                                                            , "There is an error with the input. A valid number must be entered.")
            if Recycling_percentage_of_waste <= 100:
                break
            print("There is an error with the input. The input value should be between 0 and 100.")

        # Perform separate calculations
        Quantity_of_waste_calc = Quantity_of_waste * self.constant
        Recycling_percentage_of_waste_calc = 0.57 - (Recycling_percentage_of_waste / 100)

        # Final calculation
        result = Quantity_of_waste_calc * Recycling_percentage_of_waste_calc
        return round(result, 2)

    def Travel_for_business_calculation(self):
         # Get input values from the user and check for valid input
        Annual_kilometers_traveled  = self.obtain_valid_positive_float_value("\n The number of kilometers traveled for business purposes each year: " 
                                                            ,"There is an error with the input. A valid number must be entered.")
        Typical_fuel_efficiency = self.obtain_valid_positive_float_value("An average of how much fuel a car uses per 100 kilometers: "
                                                         , "There is an error with the input. A valid number must be entered.")
        if Typical_fuel_efficiency == 0:
            raise ValueError("There is an error with the input. The input value should not be between 0.")

        #Calculate separately 
        Typical_fuel_efficiency_calc = 1 / Typical_fuel_efficiency

        # # Final calculation
        result = Annual_kilometers_traveled * Typical_fuel_efficiency_calc * 2.31
        return round(result, 2)


def genpie_char(Utilize_energy, waste_emissions, Travel_for_business):

    # Make a pie chart with the data you created
    labels = ['Utilize_energy', 'Waste Emissions', 'Travel_for_business']
    sizes = [Utilize_energy, waste_emissions, Travel_for_business]

    # Find the index of the highest value
    max_index = sizes.index(max(sizes))

    # Generate the pie chart
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    # Set the font size for the labels
    plt.rcParams['font.size'] = 14
    plt.title('Carbon Emission', fontsize=16)

    
    plt.text(0.3, -1.8,[max_index], wrap=True, horizontalalignment='center', fontsize=15)

    plt.show()


def main():
    carbon_calculator = The_Carbon_Calculator()

    while True:
        print('\nThe Carbon Footprint Monitoring Tool is here to help you monitor your carbon footprint')
        print('1. Calculate your energy consumption')
        print('2. Emissions from waste can be calculated')
        print("3. The carbon emissions associated with business travel are")
        print('4. An overview of all calculations with a pie chart')
        print("5. Exit")

        choice = input("'Choose one of the following (1-5): ")

        if choice == '1':
            Utilize_energy = carbon_calculator.Utilize_energy_calculator()
            print("\nCalculate your energy consumption:", Utilize_energy, "KgCO2")

        elif choice == '2':
            waste_emissions = carbon_calculator.Waste_emissions_calculation()
            print("\nEmissions from waste can be calculated:", waste_emissions, "KgCO2")

        elif choice == '3':
            Travel_for_business = carbon_calculator.Travel_for_business_calculation()
            print("\nThe carbon emissions associated with business travel are", Travel_for_business, "KgCO2")

        elif choice == '4':
            Utilize_energy = carbon_calculator.Utilize_energy_calculator()
            print("Calculate your energy consumption::", Utilize_energy, "KgCO2")
            waste_emissions = carbon_calculator.Waste_emissions_calculation()
            print("Emissions from waste can be calculated:", waste_emissions, "KgCO2")
            Travel_for_business = carbon_calculator.Travel_for_business_calculation()
            print("The carbon emissions associated with business travel are:", Travel_for_business, "KgCO2")

            # The pie chart should be generated and displayed
            genpie_char(Utilize_energy, waste_emissions, Travel_for_business)

        elif choice == '5':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


#The main function needs to be run
if __name__ == '__main__':
    plt.show()
    main()

