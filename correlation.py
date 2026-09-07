import numpy as np
from scipy import signal

# Find the exact horizontal shift (lag) between the two signals
correlation = signal.correlate(blue_y - np.mean(blue_y), orange_y - np.mean(orange_y))
lags = signal.correlation_lags(len(blue_y), len(orange_y))
time_shift = lags[np.argmax(correlation)]

print(f"Alignment: Shifted by {time_shift} samples")
# Ideal result: 0 (they are perfectly aligned in time)
