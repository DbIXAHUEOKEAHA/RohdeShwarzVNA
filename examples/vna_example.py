"""
Python rohdeschwarz VNA example
"""

import sys

if __name__ != "__main__":
    print("'{0}'\nis a script. Do not import!".format(__file__))
    print('Exiting...')
    sys.exit()
from rohdeschwarz import *
from rohdeschwarz.instruments.vna import *

vna = Vna()

vna.open('TCPIP', '169.254.82.39')

#print(vna.reverse_sweep(100000, 500000, 500))
vna.set_start_freq(10000)
vna.set_stop_freq(11000)
vna.set_num_points(50)
vna.start_sweep()
print(f'Real trace is {vna.trace_real()}')
print(f'Imag trace is {vna.trace_im()}')
vna.display_screen()

vna.set_bandwidth(100)

print(f'Bandwidth is {vna.bandwidth()}')

#print(vna.trace_im())

#print(vna.power())

# Close Log
vna.close_log()

# Close connection
vna.close()
