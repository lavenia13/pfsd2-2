import random
import string

def generate_random_color_hex():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_random_alphabetical_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def generate_random_value_between(min_value, max_value):
    return random.randint(min_value, max_value)

def generate_random_multiple_of_seven():
    return random.randint(0, 10) * 7

# Example usage:
random_color_hex = generate_random_color_hex()
random_alphabetical_string = generate_random_alphabetical_string(8)
random_value_between = generate_random_value_between(5, 15)
random_multiple_of_seven = generate_random_multiple_of_seven()

print("Random Color Hex:", random_color_hex)
print("Random Alphabetical String:", random_alphabetical_string)
print("Random Value Between 5 and 15:", random_value_between)
print("Random Multiple of 7 between 0 and 70:", random_multiple_of_seven)


#2
import random
from datetime import datetime, timedelta

def generate_random_integer_0_to_6():
    return random.randrange(0, 6)

def generate_random_integer_5_to_10():
    return random.randrange(5, 10)

def generate_random_integer_step_of_3():
    return random.randrange(0, 10, 3)

def generate_random_date(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randrange(time_delta.days)
    return start_date + timedelta(days=random_days)

# Example usage:
random_int_0_to_6 = generate_random_integer_0_to_6()
random_int_5_to_10 = generate_random_integer_5_to_10()
random_int_step_of_3 = generate_random_integer_step_of_3()
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 1, 1)
random_date = generate_random_date(start_date, end_date)

print("Random Integer between 0 and 6 (excluding 6):", random_int_0_to_6)
print("Random Integer between 5 and 10 (excluding 10):", random_int_5_to_10)
print("Random Integer between 0 and 10 with a step of 3:", random_int_step_of_3)
print("Random Date between {} and {}:".format(start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")), random_date.strftime("%Y-%m-%d"))


import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('students.csv')

# Define age groups
bins = [0, 12, 18, 25]
labels = ['0-12', '13-18', '19-25']

# Create a new column 'Age Group' based on the defined bins
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Create separate DataFrames for each age group
df_0_12 = df[df['Age Group'] == '0-12']
df_13_18 = df[df['Age Group'] == '13-18']
df_19_25 = df[df['Age Group'] == '19-25']

# Calculate the average grade for each age group
avg_grade_0_12 = df_0_12['Grade'].mean()
avg_grade_13_18 = df_13_18['Grade'].mean()
avg_grade_19_25 = df_19_25['Grade'].mean()

# Create a bar plot
age_groups = labels
average_grades = [avg_grade_0_12, avg_grade_13_18, avg_grade_19_25]

plt.bar(age_groups, average_grades, color='skyblue')
plt.xlabel('Age Group')
plt.ylabel('Average Grade')
plt.title('Average Grade for Different Age Groups')
plt.show()
