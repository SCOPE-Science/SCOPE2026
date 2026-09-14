"""Model of the Airy-transition obstruction for short-window Kuznetsov.

Purpose: bounded recovery test for the target
  sum_{T<t_j<=T+Delta} L(1/2,sym^2(u_j)x phi) << Delta T^{1+eps}, Delta>=T^{1/5+eps}.

Standard short-window Kuznetsov analysis:
- test function h supported in [T,T+Delta], Delta << T;
- off-diagonal kernel H^+(x), x = sqrt(mn)/c, m,n <= T^2 (AFE length);
- J_{2it}(x) has turning point at x ~ 2t with Airy width ~ t^{1/3}.

Model bound used in the literature for the NON-uniform stationary-phase regime:
  OD_model(T,Delta) ~ T^{3/2+eps} * Delta^{-1/2}   (transition-range contribution
  after Weil + GL2 Voronoi with short dual, before uniform Airy analysis).

Main term: MAIN ~ Delta * T.

Threshold from OD_model <= MAIN:
  T^{3/2} Delta^{-1/2} <= Delta T  <=>  Delta^{3/2} >= T^{1/2}  <=>  Delta >= T^{1/3}.

Hence standard tools stop at 1/3; reaching the target 1/5 needs an extra saving of
  GAP(T) = OD_model(T,T^{1/5}) / MAIN(T,T^{1/5}) ~ T^{3/2-1/10-... }/T^{6/5} ~ T^{3/10}/...
in the Airy transition band where the window Delta=T^{1/5} is NARROWER than the
Airy width T^{1/3}. This script quantifies the width mismatch and the gap.

This is a model computation (evidence of block, not a theorem about L-values).
Run: python3 airy_barrier.py
"""
import math

print(f"{'T':>10} {'Airy T^1/3':>12} {'target T^1/5':>14} {'width ratio':>12} {'gap OD/MAIN at d=1/5':>22}")
for logT in [3, 4, 5, 6, 8, 10]:
    T = 10.0 ** logT
    airy = T ** (1/3)
    tgt = T ** (1/5)
    ratio = airy / tgt  # >>1 always; window cannot resolve transition
    # gap exponent: OD_model/MAIN at Delta=T^{1/5}: T^{3/2} D^{-1/2}/(D T) = T^{1/2} D^{-3/2}
    gap_exp = 0.5 - 1.5 * 0.2  # = 0.5-0.3 = 0.2
    gap = T ** gap_exp
    print(f"{T:10.0e} {airy:12.3g} {tgt:14.3g} {ratio:12.3g} {gap:22.3g}")
print()
print("gap exponent at d=1/5: +1/5 => OD_model exceeds MAIN by T^{1/5} (up to eps).")
print("width ratio T^{1/3}/T^{1/5} = T^{2/15} -> infinity: short window sits INSIDE Airy band.")
print("Conclusion: with non-uniform stationary phase the target window is blocked by")
print("the Airy transition; closing the T^{1/5} gap needs uniform Airy asymptotics for")
print("J_{2it} jointly in (t,x) plus extra Voronoi/stationary-phase saving, i.e. new analysis")
print("beyond the standard Kuznetsov+Weil+Voronoi route attempted here.")
