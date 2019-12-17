from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
  result = die_1.roll() + die_2.roll()
  results.append(result)
print(results)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
  frequency = results.count(value)
  frequencies.append(frequency)
print(frequencies)

#可视化结果
hist = pygal.Bar()

hist.title = "results of rolling one d6 50000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '12', '13', '14', '15', '16']
hist.x_title = "result"
hist.y_title = "frequency of result"

hist.add("d6 + d6", frequencies)
hist.render_to_file('die_visual.svg')
