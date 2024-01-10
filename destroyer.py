import os
import time

def create_and_delete_file(filename, data, num_iterations):
    for _ in range(num_iterations):
        with open(filename, 'w') as f:
            f.write(data)
        time.sleep(1)  # pause for 1 second
        os.remove(filename)

# usage
create_and_delete_file('garbage.txt', 'garbage data garbage data garbage data garbage data garbage data garbage data garbage data garbage data garbage data garbage data garbage data garbage data', 1000000)
