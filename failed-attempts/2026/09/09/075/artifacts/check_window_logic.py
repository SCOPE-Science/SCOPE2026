"""Lane-480: killing-window logic decomposition (stdlib only).

Formalizes what the admitted target claim needs, with status flags.
No mathematics beyond bookkeeping + cited implications is claimed.

Target T: exists r in [6,9] with d_r(h7^2) = y != 0 at (253, 2+r).
Decomposition:
  (E6)  d2=d3=d4=d5=0 on h7^2 (entry into window).
        d2..d4 known zero for ALL j (BX Cor 1.14). So (E6) <=> d5(h7^2)=0.
  (WIT) exists r in [6,9] with nonzero d_r(h7^2)=y with E2 ancestor + nonzero cert.
T <=> (E6) AND (WIT).

(E6) reduction (BX Thm 7.15 at (j,r)=(6,5) + LWX Theta_6 existence):
  (E6) follows from H: theta_6^2 = 0 in pi_{252,4}(S/lambda^3).
  Status H: UNKNOWN (blocking bidegree; classical reading = Adams filtration
  of Theta_6^2 at stem 252, Q1.7-analogue one octave above LWX Q1.7).
(WIT) reduction: needs, for some r in [6,9], BOTH
  (WIT-E2)  Ext_A^{2+r, 255+r}(F2,F2) [=(s,t) at stem 253 filt 2+r] has a
            citable nonzero generator (E2 ancestor of y), AND
  (WIT-D)   Moss-convergent shuffle (or comparison) identifying d_r(h7^2)=y.
  Status: all four (WIT-E2) UNKNOWN; all four (WIT-D) MISSING.
Upper-edge note: the bound r<=9 is part of the existential claim; no cited
vanishing at stems 253-254 above filt 11 has been located, so (WIT) must
produce its witness at r<=9 rather than exclude r>=10 a priori.

Narrowings secured (do not imply T): (N1) h0-torsion of any y (Leibniz from
d2(h8)=h0 h7^2, i.e. BX Ex 1.23(1) at j=7 / Adams Thm 1.2);
(N2) h0-tower on h6^2*h7 E2-zero in-window (Lemma L1 from h6*h7=0).

Run: python3 output/artifacts/check_window_logic.py -> WINDOW_LOGIC_OK
"""
import sys

def main():
    e6 = {"d2": "ZERO (BX Cor 1.14)", "d3": "ZERO (BX Cor 1.14)",
          "d4": "ZERO (BX Cor 1.14)", "d5": "UNKNOWN <=> H: theta_6^2=0 in pi_252,4(S/lambda^3)"}
    for k, v in e6.items():
        print(f"(E6) {k}(h7^2) = {v}")
    for r in (6, 7, 8, 9):
        print(f"(WIT) r={r}: E2 ancestor at (s,t)=({2+r},{255+r}) nonzero=UNKNOWN; shuffle=MISSING")
    print("(N1) h0*y=0 on E_r secured (conditional on survival); (N2) h6^2*h7 tower E2-zero secured")
    print("T = (E6) AND (WIT): NOT CERTIFIED — blocking data: H at (252,4)/lambda^3; E2 ancestor + shuffle at one r in [6,9]")
    print("WINDOW_LOGIC_OK")

if __name__ == "__main__":
    sys.exit(main())
