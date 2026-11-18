"""Regenerate figs/arena.pdf for the talk: the two experimental scenarios.

Element positions were recovered by pixel analysis of the TFG figures
(mapa_experimento_individual.png and mapa_experimento_multiagente.png).
Fonts are set larger than in the paper, for projection.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "font.size": 9,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.linewidth": 0.7,
})

COL = 5.6  # inches: wider than the paper column, for a slide

C_ROBOT, C_RED, C_BLUE, C_YEL = "#21426b", "#c0392b", "#2980b9", "#d4a017"
C_PICK, C_DROP = "#cfcfcf", "#7f7f7f"

fig, axes = plt.subplots(1, 2, figsize=(COL, 2.75))

# ---- (a) scenario 1: single robot, 10 x 10 m -------------------------
ax = axes[0]
for x, y in [(2.26, 2.40), (-1.71, 0.20), (2.26, -2.41)]:
    ax.add_patch(plt.Circle((x, y), 0.43, fc=C_PICK, ec="none", zorder=1))
ax.add_patch(plt.Circle((1.0, 0.0), 0.48, fc=C_DROP, ec="none", zorder=1))
for x, y in [(0.20, 2.14), (2.25, -1.60), (-2.10, -2.10)]:
    ax.plot(x, y, marker="*", ms=9, color=C_YEL, mec="k", mew=0.3, zorder=3)
ax.plot(-2.59, 2.70, marker="*", ms=9, color=C_BLUE, mec="k", mew=0.3, zorder=3)
ax.plot(1.0, 0.0, marker="*", ms=9, color=C_RED, mec="k", mew=0.3, zorder=3)
ax.plot(0, 0, marker="o", ms=6, color=C_ROBOT, mec="k", mew=0.3, zorder=4)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xticks([-4, 0, 4])
ax.set_yticks([-4, 0, 4])
ax.set_title("(a) scenario 1: single robot", pad=4, fontsize=9)

# ---- (b) scenario 2: fleet exploration -------------------------------
ax = axes[1]
ax.add_patch(plt.Circle((0, 0), 0.9, color=C_BLUE, alpha=0.15, zorder=1))
for x, y in [(-4.4, 4.4), (4.4, 4.4), (4.4, -4.4)]:
    ax.plot(x, y, marker="*", ms=9, color=C_RED, mec="k", mew=0.3, zorder=3)
ax.plot(0, 0, marker="*", ms=9, color=C_BLUE, mec="k", mew=0.3, zorder=3)
for i in range(5):
    y = -2 + i
    ax.plot(-4, y, marker="o", ms=5, color=C_ROBOT, mec="k", mew=0.3, zorder=4)
    ax.annotate("", xy=(-3.0, y), xytext=(-3.7, y),
                arrowprops=dict(arrowstyle="->", lw=0.7, color=C_ROBOT))
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_xticks([-5, 0, 5])
ax.set_yticks([-5, 0, 5])
ax.set_title("(b) scenario 2: fleet exploration", pad=4, fontsize=9)

for ax in axes:
    ax.set_aspect("equal")
    ax.set_xlabel("x [m]", labelpad=1)
    ax.grid(alpha=0.3, ls=":")
    ax.set_axisbelow(True)
axes[0].set_ylabel("y [m]", labelpad=1)

fig.tight_layout(pad=0.3, w_pad=1.0)

# shared legend, placed clear of the axes
fig.canvas.draw()
_r = fig.canvas.get_renderer()
_inv = fig.transFigure.inverted()
_y = min(a.get_tightbbox(_r).transformed(_inv).y0 for a in axes)
handles = [
    plt.Line2D([0], [0], ls="none", marker="o", ms=5.5, color=C_ROBOT, mec="k", mew=0.3),
    plt.Line2D([0], [0], ls="none", marker="*", ms=9, color=C_BLUE, mec="k", mew=0.3),
    plt.Line2D([0], [0], ls="none", marker="*", ms=9, color=C_RED, mec="k", mew=0.3),
    plt.Line2D([0], [0], ls="none", marker="*", ms=9, color=C_YEL, mec="k", mew=0.3),
    plt.Line2D([0], [0], ls="none", marker="o", ms=6, color=C_PICK),
    plt.Line2D([0], [0], ls="none", marker="o", ms=6, color=C_DROP),
]
labels = ["e-puck robot", "blue light / beacon", "red light / target",
          "yellow lights", "collection zone", "deposit zone"]
fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, _y - 0.02),
           ncol=3, fontsize=7.5, frameon=False, handlelength=1.0,
           columnspacing=1.4, handletextpad=0.4, labelspacing=0.35)

fig.savefig("figs/arena.pdf", bbox_inches="tight", pad_inches=0.02)
plt.close(fig)
print("figs/arena.pdf written (two scenario layouts)")
