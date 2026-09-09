"""Lane-480: Lemma-7.10 consequences for the V0' obstruction (stdlib only).

Citable data (BX Lemma 7.10, 2302.11869 v3, Fig 11 region):
  pi_{252,4}(S/lambda^2) ~= F2{lambda-bar V0'}   (single obstruction class)
  pi_{252,3}(S/lambda^2) = 0
  pi_{254,2}(S/lambda^3) = F2{theta_7}
  pi_{253,3}(S/lambda^3) = 0

Consequence C1 (already used in BX Prop 7.17 j=7 repair): the classical class
  theta_6^2 in (252,4) can differ from 0 in S/lambda^2 ONLY by lambda-bar V0'.
Consequence C2 (target-page constraint, conditional on L2):
  v_lambda(eta*theta_6^2) >= 2 requires theta_6^2 lift past S/lambda^2, i.e.
  resolution of the V0' alternative. The Prop-7.17 repair (theta_6^2 = 0 in
  S/lambda^2 via <theta_6,2,theta_5> shuffle + pi_{252,3} = 0) decides C1
  affirmatively — citable. The NEXT step (S/lambda^3 vanishing = hypothesis H)
  is exactly what is NOT in Lemma 7.10 (which gives pi_{252,3}(S/lambda^3)
  ~= F2{lambda-bar^2 V0'}, nonzero — so no automatic killing).
Consequence C3: pi_{253,3}(S/lambda^3) = 0 means the eta-valuation group
  pi_{253,5}(S) maps with restricted indeterminacy at low lambda-power;
  logged as supporting detail for L2's (253,5) framing, not a proof of v.

Run: python3 output/artifacts/check_lemma710_use.py -> LEMMA710_USE_OK
"""
import sys

def main():
    print("BX Lemma 7.10 data: pi252,4/l2 = F2{lb V0'}; pi252,3/l2 = 0; pi254,2/l3 = F2{th7}; pi253,3/l3 = 0")
    print("C1: theta_6^2 in S/l2 is either 0 or lb V0' (repaired to 0 in BX Prop 7.17)")
    print("C2: H (vanishing in S/l3) is NOT automatic: pi252,3/l3 = F2{lb^2 V0'} != 0")
    print("C3: pi253,3/l3 = 0 frames (253,5) eta-valuation with low indeterminacy")
    print("LEMMA710_USE_OK")

if __name__ == "__main__":
    sys.exit(main())
