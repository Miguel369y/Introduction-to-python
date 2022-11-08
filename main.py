reservoir_volume = 4.445e8
rainfall = 5e6
rainfall *= 0.9   #rainfall decreases by 10% due to runoff
reservoir_volume += rainfall  #adding the reservoir_volume to the rainfall

# let stormwater = reservoir_volume * 1.05
reservoir_volume *= 1.05

#let evaporation = reservoir_volume * 0.5
reservoir_volume *= 0.95

#accounting for pipedwater to arid areas
reservoir_volume -= 2.5e5
print(reservoir_volume)
