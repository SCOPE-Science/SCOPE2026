"""Fallback audit for lane-605: critical-time relaxation gap + index-window scale.

F1: Standard edge-relaxation needs t >> n^{-1/3} (supercritical, omega>0) for a
    polynomial improvement kappa ~ c*omega over rigidity. At fixed critical
    t1=n^{-1/3} (omega=0) the contraction factor is O(1): no kappa>0.
    Quantifies t_needed/t1 = n^{omega} with omega>=kappa/c (c=1 schematic).
F2: Cusp quantile scale gamma_i ~(i/n)^{3/4}; uniform absolute bound
    n^{-3/4-1/36} over i<=n^{1/2} log n demands vanishing relative error far
    beyond the edge (gamma_{imax} >> bound). Table.
stdlib only.
"""
import math

KAPPA = 1.0 / 36.0

print("== F1: critical vs supercritical time ==")
print(f"{'n':>12} {'t1=n^-1/3':>12} {'t_need=n^-11/36':>14} {'ratio':>10}")
for n in [10**6, 10**9, 10**12, 10**15]:
    t1 = n ** (-1.0 / 3.0)
    tneed = n ** (-1.0 / 3.0 + KAPPA)  # omega=kappa at c=1
    print(f"{n:>12} {t1:>12.3e} {tneed:>14.3e} {tneed/t1:>10.3f}")
print("ratio = n^{1/36} -> inf (1.47, 1.78, 2.15, 2.61). "
      "Fallback demands relaxation in time shorter by a divergent factor.")
print("At omega=0 the homogenization contraction factor (n^{1/3} t)^c = 1: O(1), "
      "no n^{-kappa} gain. Closing kappa=1/36 at critical t needs a threshold")
print("improvement over the standard t>>n^{-1/3} theory: open, not a 1h lemma.")
print()
print("== F2: cusp quantile vs uniform bound ==")
print(f"{'n':>12} {'imax':>12} {'gamma_imax':>12} {'bound':>12} {'rel':>12}")
for n in [10**6, 10**9, 10**12]:
    imax = int(n ** 0.5 * math.log(n))
    gamma = (imax / n) ** 0.75
    bound = n ** (-0.75 - KAPPA)
    print(f"{n:>12} {imax:>12} {gamma:>12.3e} {bound:>12.3e} "
          f"{bound/gamma:>12.3e}")
print("bound/gamma -> 0 far beyond edge (relative error must vanish to "
      "n^{-1/36}(log n)^{-3/4}(i/n)^{-3/4} uniformly): needs bulk-cusp input, "
      "not one-scale eta0.")
