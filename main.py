import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.linspace(0, 10, 300)

    fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharex=True)

    axes[0].plot(x, np.sin(x), color="tab:blue")
    axes[0].set_title("sin(x)")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(x, np.cos(x), color="tab:orange")
    axes[1].set_title("cos(x)")
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(x, np.sin(x) * np.cos(x), color="tab:green")
    axes[2].set_title("sin(x) * cos(x)")
    axes[2].grid(True, alpha=0.3)

    for ax in axes:
        ax.set_xlabel("x")
    axes[0].set_ylabel("y")

    fig.suptitle("Three Plots in One Figure")
    fig.tight_layout()
    fig.savefig("three_plots.png", dpi=150)
    print("Saved: three_plots.png")


if __name__ == "__main__":
    main()
