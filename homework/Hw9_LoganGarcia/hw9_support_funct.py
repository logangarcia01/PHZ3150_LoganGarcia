def my_circuit(conf, r, rs, vi):
    tot_r = 0
    if conf == 'series':
        for i in range(r):
            tot_r += rs[i]
        print('The total resistance of this series circuit is:', tot_r, ' Ohms, and its voltage is:', tot_r * vi, 'V.')
    elif conf == 'parallel':
        for i in range(r):
            tot_r += (1 / rs[i])
        print('The total resistance of this parallel circuit is:', tot_r, ' Ohms, and its Amperage is:', tot_r * vi, 'A.')