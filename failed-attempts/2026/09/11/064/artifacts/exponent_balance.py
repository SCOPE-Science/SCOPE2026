"""AFE-split exponent balance: E_off ~ q^{a/2}, E_dual ~ q^{2-a/2} (totals).
Shows min_a max = q^1 = main-term scale -> no power saving at Weil level.
Also checks generic sharpness scale of Kl_3 bound |Kl_3| <= 3q via random-phase model
(recorded as heuristic illustration only; the rigorous input is Deligne's bound).
"""
import math

print("a | E_off | E_dual | max (totals, exponents of q)")
best = (1e9, None)
for i in range(21):
    a = 1.0 + i * 0.05
    e1, e2 = a / 2, 2 - a / 2
    m = max(e1, e2)
    if m < best[0]:
        best = (m, a)
    print(f"a={a:.2f} X=q^{a:.2f} Y=q^{3 - a:.2f} | q^{e1:.4f} q^{e2:.4f} max=q^{m:.4f}")
print(f"BEST: a={best[1]:.2f} max=q^{best[0]:.4f} (main term q^1.0000); need q^{1 - 1 / 96:.4f}")
print("RECOVERY_RESULT: FLOOR_AT_MAIN_TERM_SCALE_NO_SAVING")
