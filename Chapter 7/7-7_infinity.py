# This program demonstrates a truly infinite loop.
# The program import time to enter a small delay because we don't want it to flood the console

import time
print("Starting infinite loop (press Ctrl+C to stop)...")

while True: # The condition is always True, so the loop never ends
    print("This message will print forever!")
    time.sleep(0.5) # waits for 0.5 seconds