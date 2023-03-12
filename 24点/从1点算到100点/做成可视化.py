from plotly.graph_objs import Bar, Layout
from plotly import offline

x_values = [i for i in range(1, 101)]
frequencies = [0.8928571428571429, 0.8521978021978022, 0.9593406593406594, 0.9010989010989011, 0.8829670329670329,
               0.8648351648351649, 0.8686813186813187, 0.8456043956043956, 0.8423076923076923, 0.8461538461538461,
               0.8461538461538461, 0.8164835164835165, 0.8423076923076923, 0.7736263736263737, 0.7939560439560439,
               0.7868131868131868, 0.7824175824175824, 0.6813186813186813, 0.765934065934066, 0.6576923076923077,
               0.7532967032967033, 0.6873626373626374, 0.682967032967033, 0.6087912087912087, 0.7478021978021978,
               0.5884615384615385, 0.6384615384615384, 0.6225274725274725, 0.6406593406593407, 0.515934065934066,
               0.6494505494505495, 0.48846153846153845, 0.6076923076923076, 0.5664835164835165, 0.4901098901098901,
               0.5565934065934066, 0.695054945054945, 0.4510989010989011, 0.45604395604395603, 0.5197802197802198,
               0.6329670329670329, 0.39725274725274723, 0.5467032967032966, 0.3945054945054945, 0.5384615384615384,
               0.5208791208791209, 0.3989010989010989, 0.371978021978022, 0.6236263736263736, 0.4175824175824176,
               0.460989010989011, 0.3983516483516483, 0.4653846153846154, 0.3478021978021978, 0.5071428571428571,
               0.4346153846153846, 0.5021978021978022, 0.3543956043956044, 0.33406593406593404, 0.3241758241758242,
               0.6027472527472527, 0.30714285714285716, 0.32142857142857145, 0.4307692307692308, 0.43956043956043955,
               0.40054945054945057, 0.4565934065934066, 0.2923076923076923, 0.3412087912087912, 0.32252747252747255,
               0.4582417582417582, 0.27472527472527475, 0.578021978021978, 0.27197802197802196, 0.27307692307692305,
               0.34835164835164834, 0.33681318681318684, 0.3758241758241758, 0.4208791208791209, 0.25054945054945055,
               0.48131868131868133, 0.32857142857142857, 0.2489010989010989, 0.2456043956043956, 0.4785714285714286,
               0.2785714285714286, 0.23296703296703297, 0.256043956043956, 0.3978021978021978, 0.21593406593406594,
               0.4747252747252747, 0.3120879120879121, 0.27307692307692305, 0.23406593406593407, 0.21318681318681318,
               0.24010989010989012, 0.4554945054945055, 0.20494505494505494, 0.28406593406593406, 0.3346153846153846,
               0.3576923076923077]

data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '算的点数'}
y_axis_config = {'title': '有解率'}
my_layout = Layout(title='计算不同点数的有解率', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='result.html')
