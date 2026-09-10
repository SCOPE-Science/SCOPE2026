"""Bounded partial probe for lane-631 fallback ratio (finite-vector half only).

Finite ratio fact (exact, no floats needed for lower bound):
  f(t)=log2(t+1); f(7)=3, f(63)=6 exactly.
  yAvg = (f(7)/7) * sum_{k=1..7} z_k, z_k = (f(63)/63)*1_{F_k}, |F_k|=63 disjoint.
  coeff per coordinate = (3/7)*(6/63) = 18/441 = 2/49 on 441 coords.
  Singleton partition lower bound: ||yAvg|| >= 441*(2/49)/f(441) = 18/log2(442).
  442 < 512 = 2^9  =>  log2(442) < 9  =>  ||yAvg|| > 18/9 = 2 (strict).
  zAvg = (f(7)/7)*sum_{k=1..7} e_{j_k} (7 singletons): support-partition gives
  ||zAvg|| >= 1; interval-DP identity (verify_target_block.py, n=7) gives == 1.
  Hence ||yAvg|| > 2 = 2*||zAvg|| on these finite vectors.

NOT proved (hence fallback criterion unmet): embedding in infinite RIS
sequences with growth integers + canonical block-projection norms <= 6
(averaging-projection bound on S needs uniform Ramsey estimate; absent).
Run: python3 ratio_finite_cert.py -> prints certificate lines.
"""
import math


def main():
    f7 = math.log2(8)
    f63 = math.log2(64)
    assert abs(f7 - 3.0) < 1e-12 and abs(f63 - 6.0) < 1e-12
    coeff_num, coeff_den = 2, 49  # (3/7)*(6/63) = 18/441 = 2/49
    total = 7 * 63
    assert total * coeff_num == 18 * coeff_den  # 441*(2/49) = 18
    assert 442 < 512  # log2(442) < 9
    lb = total * (coeff_num / coeff_den) / math.log2(442)
    print(f"RATIO_FINITE_CERT: f7={f7:.12f} f63={f63:.12f}")
    print(f"RATIO_FINITE_CERT: per-coord coeff=2/49 on {total} coords; "
          f"singleton-partition lower bound ||yAvg|| >= 18/log2(442) = {lb:.6f}")
    print(f"RATIO_FINITE_CERT: 442<512 => bound > 2 strictly: {lb > 2}")
    print(f"RATIO_FINITE_CERT: ||zAvg||(7 singletons) = 1 by DP identity "
          f"(see verify_target_block.py n=7 line)")
    print(f"RATIO_FINITE_CERT: ratio > 2 on finite vectors: {lb > 2.0}")
    print("RATIO_FINITE_CERT: SCOPE = finite vectors only; "
          "infinite RIS + projection<=6 NOT certified")


if __name__ == "__main__":
    main()
