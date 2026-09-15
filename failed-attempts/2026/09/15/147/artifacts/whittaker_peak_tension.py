"""Whittaker-newvector size check (depth aspect, Casselman theory sanity).

Casselman's theory: for a depth-n newvector in an unramified-principal-series
type representation of GL(2,Q_p), the normalized Whittaker function W(g)
satisfies: W is supported with max at a = p^{-n} shift; at the peak
  |W(diag(p^{-n},1))| ~ p^{n/2} x (fixed factor ~ (1-p^{-1})^{-1} etc.)
under the standard normalization W(1)=1-side conventions; equivalently the
L^2-normalized form has a Whittaker coefficient of size ~ p^{n/2} at the
ramified cusp, up to fixed Satake factors.

This script prints the implied lower bound on sup (prob-measure convention):
  sup_prob >= c * p^{n/2} / sqrt(Vol_factor...)
and compares with local bound p^{n/4}: the Whittaker value EXCEEDS the
supposed generic sup bound p^{n/4} at large n. It also shows: any improvement
delta'>0 (sup << p^{n(1/4-d')}) is contradicted -- at face value -- by this
peak value, UNLESS the peak lies outside the truncated domain / the
normalization convention differs. That is exactly the ambiguity the target's
method (adelic Whittaker at cusps) must resolve; the Hu-Saha filtration
controls the bulk, but the cusp-peak forces a max over cusps, and published
depth-aspect sup results in fact phrase bounds as growth in the LEVEL/VOLUME
aspect with different normalization (sup << N^{1/4} relative to fixed-volume
reference, gaining only in eigenvalue/level-mixed ranges), not as a genuine
p^{n(1/4-delta')} scaling at fixed arch parameter on vol-1 Y_0(p^n).

We compute the tension ratio R = peak / claimed_sub-local_bound.
"""
p = 3
dprime = 1/24  # benchmark-implied under optimistic scenario (A)
print(f"{'n':>3} {'peak~p^{n/2}':>14} {'local p^{n/4}':>12} {'subloc p^{n(1/4-dp)}':>18} {'R=peak/subloc':>14}")
for n in [2, 4, 6, 8, 10, 12]:
    peak = p ** (n / 2)
    local = p ** (n / 4)
    subloc = p ** (n * (0.25 - dprime))
    R = peak / subloc
    print(f"{n:>3} {peak:>14.1f} {local:>12.2f} {subloc:>18.3f} {R:>14.1f}")
print()
print("R = p^{n(1/4+d')} grows exponentially: cusp-peak >> any sub-local bound.")
print("Hence ||.||_inf over the FULL Y_0(p^n) (all cusps, vol 1) cannot beat")
print("p^{n/4} without excluding/renormalizing cusp neighborhoods -- but the")
print("TORIC period in Waldspurger (split torus ~ cusp directions) samples")
print("precisely the region where the Whittaker peak lives. The two halves of")
print("the target (sub-local sup + period bound by sup) pull in opposite")
print("directions: shrinking the sup domain breaks the period estimate.")
