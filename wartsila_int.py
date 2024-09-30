import csv

def calculate_soc(hour: float, power: int, current_soc: float) -> float:
    # constants given
    capacity = 100
    efficiency = 0.90
    energy = power * hour

    if power < 0:
        # efficiency when battery charging
        energy *= efficiency
    else:
        # efficiency when battery discharging
        energy /= efficiency

    # SOC conversion to energy
    current_energy = current_soc * capacity
    new_energy = current_energy + energy
    # here prgram calculating the new SOC
    new_soc = new_energy / capacity
    return max(0, min(1, new_soc))  # SOC should remain between 0 and 1


def read_data_and_calculate_soc(filename):
    with open("power_over_time.csv", mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # this should skip first/header row
        current_soc = 0.80
        print("Time,Power,SOC")

        for row in reader:
            time = row[0]
            power = int(row[1])
            # 30-minutes interval = 0.5 hours
            current_soc = calculate_soc(0.5, power, current_soc)
            #print final result set
            print(f"{time}, {power}, {round(current_soc, 2)}")


read_data_and_calculate_soc('power_over_time.csv')