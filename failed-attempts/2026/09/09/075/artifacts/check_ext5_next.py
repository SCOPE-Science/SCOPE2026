"""Lane-480: next Ext^5 obstruction bidegrees for the Thm-7.15 climb (stdlib only).

BX Prop 7.17 induction (2302.11869 v3): to propagate theta_j one needs
  theta_j^2 = 0 in pi_{2^{j+2}-4, 4}(S/lambda^2),
and for j != 7 this follows from Ext_A^{5, 2^{j+2}+1} = 0
(Figures 10-12; the j=7 case needs the Lemma-7.21 Toda repair at (252,4)).

Bidegree check: Ext^{s=5, t} has stem t-s. For t = 2^{j+2}+1, stem = 2^{j+2}-4.
  j=6: Ext^{5,257}, stem 252 (theta_6^2 obstruction; known zero per Lemma 7.10
       region / Fig 11, except the j=7-adjacent repair already handled).
  j=7: Ext^{5,513}, stem 508 (theta_7^2 obstruction for any theta_8 step).
       Status UNKNOWN in cited charts (Fig 10 covers j>=10 i.e. stems >=2044
       for the source; stem-508 filt-5 is outside Lemmas 7.9/7.10 and LWX App).
Hence the induction as published stops being citable exactly at the step that
would constrain d(h7^2) via theta_8. This is Door 2 of the obstruction tower,
restated as an Ext^5 non-vanishing-unknown.

Run: python3 output/artifacts/check_ext5_next.py -> EXT5_NEXT_OK
"""
import sys

def main():
    for j in (5, 6, 7, 8):
        t = 2**(j+2) + 1
        stem = t - 5
        sqstem = 2**(j+2) - 4
        assert stem == sqstem, (j, stem, sqstem)
        status = "ZERO (cited Figs 10-12, j!=7 repair if needed)" if j in (5, 6) else "UNKNOWN (outside cited charts)"
        print(f"j={j}: Ext^(5,{t}) stem {stem} = theta_{j}^2 obstruction in S/lambda^2: {status}")
    print("Door 2 = Ext^(5,513) stem 508: UNKNOWN — blocks theta_8 step / upper-window climb")
    print("EXT5_NEXT_OK")

if __name__ == "__main__":
    sys.exit(main())
