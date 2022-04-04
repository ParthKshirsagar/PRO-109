import statistics as stats
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

file = 'data.csv'
df = pd.read_csv(file)
writing = df["writing score"].to_list()

mean = stats.mean(writing)
median = stats.median(writing)
mode = stats.mode(writing)

std_dev = stats.stdev(writing)

first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)

list_of_data_within_1_std_deviation = [result for result in writing if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_std_deviation = [result for result in writing if result > second_std_dev_start and result < second_std_dev_end]
list_of_data_within_3_std_deviation = [result for result in writing if result > third_std_dev_start and result < third_std_dev_end]

print("Mean of the writing score: " + str(mean))
print("Median of the writing score: " + str(median))
print("Mode of the writing score: " + str(mode))
print("Standard deviation of the writing score is: " + str(std_dev))

percentage_within_first_std_dev = (len(list_of_data_within_1_std_deviation)/len(writing))*100
percentage_within_second_std_dev = (len(list_of_data_within_2_std_deviation)/len(writing))*100
percentage_within_third_std_dev = (len(list_of_data_within_3_std_deviation)/len(writing))*100

print(str(percentage_within_first_std_dev) + '% of data is within First Standard Deviation')
print(str(percentage_within_second_std_dev) + '% of data is within Second Standard Deviation')
print(str(percentage_within_third_std_dev) + '% of data is within Third Standard Deviation')

fig = ff.create_distplot([writing], ['Result'], show_hist=False)
fig.add_trace(go.Scatter(x=[first_std_dev_start, first_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_dev_end, first_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_dev_start, second_std_dev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_dev_end, second_std_dev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17], mode='lines', name="Mean"))

fig.show()