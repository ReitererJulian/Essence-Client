import json
import numpy as np
import matplotlib.pyplot as plt

def remove_mean(values: list[float]) -> list[float]:
    arr = np.array(values)
    return (arr - arr.mean()).tolist()

def load_measurement(json_path: str):
    with open(json_path, "r") as f:
        raw = json.load(f)
    return raw["data"]

def plot_compare_sensors(sensor_files: dict[str, str], clean: bool = True):
    fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
    axis_labels = ["X", "Y", "Z"]
    colors = plt.cm.tab10.colors

    for i, (sensor_name, path) in enumerate(sensor_files.items()):
        data = load_measurement(path)
        t = data["T"]
        color = colors[i % len(colors)]

        for row, axis in enumerate(axis_labels):
            values = data[axis]
            if clean:
                values = remove_mean(values)
            axs[row].plot(t, values, label=sensor_name, color=color)

    for row, axis in enumerate(axis_labels):
        axs[row].set_ylabel(f"{axis} (m/s²)")
        axs[row].legend()

    axs[-1].set_xlabel("Zeit (s)")

    title = "Sensor difference"
    fig.suptitle(title)

    plt.tight_layout()
    plt.show()