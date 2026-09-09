"""Lane-480: conditional eta-valuation reformulation of the killing window (stdlib only).

Conditional Lemma L2 (proof by direct transport of BX Prop 7.19, 2302.11869 v3,
from (theta_5,h6^2) to (theta_6,h7^2); transport details flagged TO-VERIFY):
  Let theta_6 in pi_{126,2}(S/lambda^8) be the lift afforded by h6^2 -> E9
  (BX Thm 7.20; LWX gives Theta_6). The bottom-two-cell/total-Bockstein argument
  in BX Prop 7.19 uses only the Thm-7.15 final-diagram shape, hence is
  j-independent wherever theta_j, theta_{j+1} both exist. theta_6, theta_7 both
  exist in S/lambda^4 (BX Prop 7.17); theta_6 lifts to S/lambda^8 (E9 h6^2).
  Therefore, for 1 <= r <= 8:
      h7^2 survives to E_{r+3}  <=>  eta*theta_6^2 = 0 in pi_{253,5}(S/lambda^r).
  Bidegree: theta_6 at (stem 126, filt 2); square at (252,4); x eta(1,1) -> (253,5).

Corollary (window arithmetic): dying via d_k (k>=6) <=> survives E_k, fails E_{k+1}
  <=> vanishes in S/lambda^{k-3}, fails in S/lambda^{k-2} <=> v_lambda = k-3 exactly,
  where v_lambda = max{r : eta*theta_6^2 = 0 in S/lambda^r} (capped at 8 by lift range).
  Hence, WITHIN lift range:
      Target window d_6..d_9  <=>  v_lambda(eta*theta_6^2) in {3,4,5,6}.
  - v >= 7 would push survival to E10+ (window fails upward; cf. BX Thm 7.20
    pattern where eta*theta_5^2 had v>=6 giving h6^2 E9).
  - v <= 2 would kill at E5 or earlier (window fails downward; v=2 <=> d5 != 0,
    i.e. failure of hypothesis H).
  This reformulation selects the PAGE from a single fixed bidegree (253,5) but
  does NOT produce the nonzero target y (Leg A still needed for y).

Status: conditional lemma (transport TO-VERIFY); valuation UNKNOWN; y UNKNOWN.

Run: python3 output/artifacts/check_eta_reformulation.py -> ETA_REFORMULATION_OK
"""
import sys

def main():
    th6 = (126, 2)
    sq = (2*th6[0], 2*th6[1])
    assert sq == (252, 4), sq
    eta_th62 = (sq[0] + 1, sq[1] + 1)
    assert eta_th62 == (253, 5), eta_th62
    print(f"theta_6 at {th6}; theta_6^2 at {sq}; eta*theta_6^2 at {eta_th62}")
    for r in range(1, 9):
        print(f"r={r}: h7^2 -> E_{r+3} <=> eta*theta_6^2 = 0 in S/lambda^{r} (conditional L2)")
    for k in (6, 7, 8, 9):
        print(f"d_{k} kill <=> v_lambda = {k-3} exactly (conditional L2)")
    print("Target window [6,9] <=> v_lambda(eta*theta_6^2) in {3,4,5,6} (conditional L2)")
    print("v_lambda=UNKNOWN; y=UNKNOWN; L2 transport details TO-VERIFY")
    print("ETA_REFORMULATION_OK")

if __name__ == "__main__":
    sys.exit(main())
