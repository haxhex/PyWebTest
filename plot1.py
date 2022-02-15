import matplotlib.pyplot as plt
# Using -with for closing file at the end
# -r : rea file
with open("data_country.txt", "r") as file:
    # Read lines and put data at each index in list
    # (crate list and put data in 1 space)
    file_data = file.readlines()
    print(file_data[0])
# x axis
countries = []
values = []
# 5 first country
for line_number in range(1, 5):
    # Skip when line number is 0
    # if line_number == 0:
    #     continue
    this_line_str = file_data[line_number]
    # split a string to string
    this_line_list = this_line_str.split(",")
    this_country = this_line_list[0]
    countries.append(this_country)
    if this_line_list[1] == "unKnown":
        continue
    this_total_case = this_line_list[1]
    values.append(int(this_total_case))
plt.figure(figsize=(4, 4))

# 131 -> One row with 3 spaces - Positions
# 1 space in 3 spaces
# Yekan -> Position of our plot
plt.subplot(111)
plt.bar(countries, values)
# plt.subplot(132)
# plt.scatter(countries, values)
# plt.subplot(133)
# plt.plot(countries, values)
plt.suptitle('Categorical Plotting')
# svg -> save image like tag so the quality is stable in zoom
plt.savefig("slick-opl/img/coronavirus-plot.svg", format = "svg")
# plt.show()
