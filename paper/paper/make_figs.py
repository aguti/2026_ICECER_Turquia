import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif"],
    "font.size": 8,
    "axes.titlesize": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "axes.linewidth": 0.6,
    "lines.linewidth": 1.0,
    "grid.linewidth": 0.4,
})

COL = 3.4  # single-column width in inches


def legend_below(fig, axs, handles, labels, gap=0.020, xc=0.5, **kw):
    """Place a shared legend clear of the axes, tick labels and axis labels."""
    fig.canvas.draw()
    _r = fig.canvas.get_renderer()
    _inv = fig.transFigure.inverted()
    _y = min(ax.get_tightbbox(_r).transformed(_inv).y0 for ax in axs)
    return fig.legend(handles, labels, loc="upper center",
                      bbox_to_anchor=(xc, _y - gap), **kw)

# ---------------------------------------------------------------- Fig. arena
fig, axes = plt.subplots(1, 2, figsize=(COL, 1.75))
ax = axes[0]
reds = [(-4.4, 4.4), (4.4, 4.4), (4.4, -4.4)]
for i, (x, y) in enumerate(reds):
    ax.plot(x, y, marker="*", ms=8, color="#c0392b", mec="k", mew=0.3, zorder=3)
ax.plot(0, 0, marker="*", ms=8, color="#2980b9", mec="k", mew=0.3, zorder=3)
ax.add_patch(plt.Circle((0, 0), 0.9, color="#2980b9", alpha=0.15, zorder=1))
for i in range(5):
    y = -2 + i
    ax.plot(-4, y, marker="o", ms=4.5, color="#2471a3", mec="k", mew=0.3, zorder=3)
    ax.annotate("", xy=(-3.0, y), xytext=(-3.75, y),
                arrowprops=dict(arrowstyle="->", lw=0.7, color="#1b4f72"))
ax.text(-4.9, 2.9, "fleet", fontsize=7.5, color="#1b4f72")
ax.text(0.45, 0.5, "charging\nbeacon", fontsize=6.6, color="#1b4f72")
ax.text(-4.4, 3.6, "targets", fontsize=6.6, color="#7b241c")
ax.set_xlim(-6, 6); ax.set_ylim(-6, 6); ax.set_aspect("equal")
ax.set_xticks([-5, 0, 5]); ax.set_yticks([-5, 0, 5])
ax.set_xlabel("x [m]", labelpad=1); ax.set_ylabel("y [m]", labelpad=1)
ax.grid(alpha=0.3, ls=":")
ax.set_title("(a) scenario layout", pad=3)

ax = axes[1]
ax.imshow(mpimg.imread("figs/scenario.png"))
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values():
    s.set_visible(False)
ax.set_title("(b) simulator view", pad=3)
fig.tight_layout(pad=0.25, w_pad=0.6)
fig.savefig("figs/arena.pdf", bbox_inches="tight", pad_inches=0.01)
plt.close(fig)

# ------------------------------------------------- Fig. success + deployment
fig, axes = plt.subplots(1, 2, figsize=(COL, 1.44))

ax = axes[0]
n = [1, 2, 3, 4, 5]
succ = [18 / 20, 1.0, 1.0, 1.0, 19 / 20]
lab = ["18", "20", "20", "20", "19"]
bars = ax.bar(n, succ, color="#2471a3", width=0.68)
for b, t in zip(bars, lab):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.025, t,
            ha="center", fontsize=6.8)
ax.set_ylim(0, 1.18); ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_xticks(n)
ax.set_xlabel("requested explorers (label = successes / 20)", labelpad=1,
              fontsize=6.6)
ax.set_ylabel("mission success rate", labelpad=1)
ax.set_title("(a) mission success", pad=3)
ax.grid(axis="y", alpha=0.3, ls=":")
ax.set_axisbelow(True)

ax = axes[1]
dep = [
    dict(med=7300, q1=5000, q3=13000, whislo=2000, whishi=16000, fliers=[]),
    dict(med=12700, q1=10200, q3=19400, whislo=4000, whishi=23500, fliers=[]),
    dict(med=24000, q1=21500, q3=31000, whislo=8400, whishi=32800, fliers=[]),
    dict(med=34500, q1=30000, q3=41200, whislo=22600, whishi=47200, fliers=[]),
    dict(med=45000, q1=38200, q3=49500, whislo=32300, whishi=56000, fliers=[69000]),
]
for d, p in zip(dep, n):
    d["label"] = str(p)
bp = ax.bxp(dep, showfliers=True, patch_artist=True, widths=0.55)
for box in bp["boxes"]:
    box.set(facecolor="#d6eaf8", edgecolor="k", lw=0.6)
for k in ("whiskers", "caps"):
    for e in bp[k]:
        e.set(lw=0.6)
for m in bp["medians"]:
    m.set(color="#c0392b", lw=1.0)
for f in bp["fliers"]:
    f.set(marker="o", ms=2.4, mfc="none", mec="k", mew=0.5)
ax.set_xlabel("requested explorers", labelpad=1)
ax.set_ylabel("deployment step", labelpad=1)
ax.set_title("(b) time to deployment", pad=3)
ax.grid(axis="y", alpha=0.3, ls=":")
ax.set_axisbelow(True)
ax.ticklabel_format(axis="y", style="sci", scilimits=(4, 4))
ax.yaxis.get_offset_text().set_fontsize(7)

fig.tight_layout(pad=0.25, w_pad=1.0)
fig.savefig("figs/success.pdf", bbox_inches="tight", pad_inches=0.01)
plt.close(fig)

# --------------------------------------------------------------- Fig. RMSE
fig, axes = plt.subplots(1, 2, figsize=(COL, 1.44))

ax = axes[0]
rm = [
    dict(med=0.160, q1=0.152, q3=0.164, whislo=0.137, whishi=0.173, fliers=[]),
    dict(med=0.135, q1=0.124, q3=0.142, whislo=0.106, whishi=0.160, fliers=[0.091]),
    dict(med=0.134, q1=0.118, q3=0.151, whislo=0.084, whishi=0.184,
         fliers=[0.216, 0.223, 0.236]),
    dict(med=0.106, q1=0.098, q3=0.117, whislo=0.072, whishi=0.127, fliers=[0.150]),
    dict(med=0.095, q1=0.088, q3=0.102, whislo=0.070, whishi=0.120, fliers=[0.125]),
]
for d, p in zip(rm, n):
    d["label"] = str(p)
bp = ax.bxp(rm, showfliers=True, patch_artist=True, widths=0.55)
for box in bp["boxes"]:
    box.set(facecolor="#d5f5e3", edgecolor="k", lw=0.6)
for k in ("whiskers", "caps"):
    for e in bp[k]:
        e.set(lw=0.6)
for m in bp["medians"]:
    m.set(color="#c0392b", lw=1.0)
for f in bp["fliers"]:
    f.set(marker="o", ms=2.4, mfc="none", mec="k", mew=0.5)
ax.set_xlabel("requested explorers", labelpad=1)
ax.set_ylabel("triangulation RMSE [m]", labelpad=1)
ax.set_title("(a) accuracy vs. fleet size", pad=3)
ax.grid(axis="y", alpha=0.3, ls=":")
ax.set_axisbelow(True)

ax = axes[1]
k = np.array([1, 2, 3, 4, 5])
r = np.array([0.1531, 0.0983, 0.0870, 0.0811, 0.0789])
lo = np.array([0.1531, 0.0945, 0.0838, 0.0782, 0.0752])
hi = np.array([0.1531, 0.1025, 0.0905, 0.0844, 0.0822])
ax.plot(k, r, marker="o", ms=3, color="#2471a3")
ax.fill_between(k, lo, hi, color="#2471a3", alpha=0.18, lw=0)
ax.set_xticks(k)
ax.set_xlabel("reports fused per target", labelpad=1)
ax.set_ylabel("triangulation RMSE [m]", labelpad=1)
ax.set_title("(b) accuracy vs. redundancy", pad=3)
ax.grid(alpha=0.3, ls=":")
ax.set_axisbelow(True)

fig.tight_layout(pad=0.25, w_pad=1.0)
fig.savefig("figs/rmse.pdf", bbox_inches="tight", pad_inches=0.01)
plt.close(fig)

# ----------------------------- Fig. single-robot: battery spread + timeline
# Panel (b) is digitized from Fig. 5.1 of the TFG
# (bateria_decisiones_robot_0.png). Replace figs/fig51_timeline.csv with the
# original run log to plot the exact data.
import csv as _csv

with open("figs/fig51_timeline.csv") as _f:
    _rows = list(_csv.DictReader(_f))
_step = np.array([float(r["step"]) for r in _rows])
_bb = np.array([float(r["battery_blue"]) for r in _rows])
_br = np.array([float(r["battery_red"]) for r in _rows])
_lo = np.array([float(r["lights_off"]) for r in _rows])

EVENTS = {
    "forage": ([2220, 6542, 8037, 24579, 27103, 30794, 39393], "#2e8b57"),
    "light mission": ([10257, 12593, 15514], "#d4a017"),
    "charge red": ([19299, 21799], "#c0392b"),
    "charge blue": ([33131, 37570], "#2471a3"),
}

fig, axes = plt.subplots(1, 2, figsize=(COL, 1.50),
                         gridspec_kw=dict(width_ratios=[0.86, 2.54]))

# ---- (a) minimum battery per run
ax = axes[0]
bat = [
    dict(med=0.215, q1=0.202, q3=0.234, whislo=0.170, whishi=0.265,
         fliers=[0.414, 0.133, 0.043, 0.019], label="blue"),
    dict(med=0.226, q1=0.203, q3=0.242, whislo=0.150, whishi=0.275,
         fliers=[0.142, 0.000], label="red"),
]
bp = ax.bxp(bat, showfliers=True, patch_artist=True, widths=0.5)
for box, c in zip(bp["boxes"], ["#d6eaf8", "#fadbd8"]):
    box.set(facecolor=c, edgecolor="k", lw=0.6)
for kk in ("whiskers", "caps"):
    for e in bp[kk]:
        e.set(lw=0.6)
for m in bp["medians"]:
    m.set(color="#c0392b", lw=1.0)
for f in bp["fliers"]:
    f.set(marker="o", ms=2.2, mfc="none", mec="k", mew=0.5)
ax.axhline(0.3, ls="--", lw=0.6, color="grey")
ax.set_ylabel("min. battery level", labelpad=1)
ax.set_title("(a) minima over 36 runs", pad=3, fontsize=7.8)
ax.tick_params(labelsize=7)
ax.grid(axis="y", alpha=0.3, ls=":")
ax.set_axisbelow(True)

# ---- (b) representative run
ax = axes[1]
ax.axvspan(12593, 15514, color="0.5", alpha=0.18, lw=0, zorder=0)
for _name, (_xs, _c) in EVENTS.items():
    for _x in _xs:
        ax.axvline(_x, color=_c, ls="--", lw=0.55, alpha=0.85, zorder=1)

ax2 = ax.twinx()
ax2.step(_step, _lo, where="post", color="#8e6bb5", lw=1.1, zorder=3)
ax2.set_ylim(-0.12, 3.30)
ax2.set_yticks([0, 1, 2, 3])
ax2.set_ylabel("lights off", labelpad=1.5, color="#6c4f8a", fontsize=6)
ax2.tick_params(axis="y", colors="#6c4f8a", length=2, labelsize=7)

ax.plot(_step, _bb, color="#2471a3", lw=1.1, zorder=4)
ax.plot(_step, _br, color="#c0392b", lw=1.1, zorder=4)
ax.text(3100, 0.80, "blue battery", fontsize=6.4, color="#2471a3", zorder=6)
ax.text(3100, 0.505, "red battery", fontsize=6.4, color="#c0392b", zorder=6)
ax.axhline(0.3, color="grey", ls=":", lw=0.7, zorder=2)

# marker 2 (third light off) has no dashed line of its own: give it a
# thin purple guide, and stagger it vertically so it clears marker 1,
# which is only ~600 steps away.
ax.axvline(13213, color="#8e6bb5", ls=":", lw=0.6, alpha=0.9, zorder=1)
for _n, _x, _y in [("1", 12593, 0.09), ("2", 13213, 0.22), ("3", 15514, 0.09)]:
    ax.text(_x, _y, _n, fontsize=6.4, ha="center", va="center",
            color="0.05", zorder=6,
            bbox=dict(boxstyle="circle,pad=0.2", fc="white", ec="0.25",
                      lw=0.45))

ax.set_xlim(0, 40000)
ax.set_ylim(0, 1.05)
ax.set_xlabel("simulation step", labelpad=1)
ax.set_ylabel("battery level", labelpad=1)
ax.ticklabel_format(axis="x", style="sci", scilimits=(4, 4))
ax.xaxis.get_offset_text().set_fontsize(6.6)
ax.tick_params(labelsize=7)
ax.grid(alpha=0.25, ls=":")
ax.set_axisbelow(True)
ax.set_title("(b) representative run", pad=3, fontsize=7.8)

fig.tight_layout(pad=0.2, w_pad=0.9)

# skill legend placed outside the axes, below the whole figure
_rh = [plt.Line2D([0], [0], color=_c, ls="--", lw=0.8)
       for _, (_, _c) in EVENTS.items()]
legend_below(fig, axes, _rh, list(EVENTS.keys()), xc=0.55, ncol=4,
             fontsize=6.6, frameon=False, handlelength=1.3,
             columnspacing=1.0, handletextpad=0.4, title="skill ordered",
             title_fontsize=6.6)
fig.savefig("figs/singlerobot.pdf", bbox_inches="tight", pad_inches=0.01)
plt.close(fig)
print("single-robot figure written")
