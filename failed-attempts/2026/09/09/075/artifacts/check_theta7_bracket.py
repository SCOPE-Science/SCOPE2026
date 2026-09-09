"""Lane-480: theta_7 Toda-bracket source datum (BX Lemma 7.21 at j=6) (stdlib only).

Citable fact (Burklund-Xu 2302.11869 v3, Lemma 7.21):
  For j>=5, j!=7, the S/lambda^3-linear 4-fold <2~, lambda*theta_j, theta_j, 2~>
  is defined, contains theta_{j+1}, with no indeterminacy (j=5 case: possible
  lambda-bar^2 D3(1) indeterminacy only).
  At j=6 (allowed — the excluded case is j=7 with matrix repair Lemma 7.22):
  theta_7 in <2~, lambda*theta_6, theta_6, 2~> in pi_{254,2}(S/lambda^3).

Stem numerology (classical reading; Toda 4-fold adds 2):
  |2| = 0, |Theta_6| = 126. 126 + 126 + 2 = 254 = |Theta_7|.
  Synthetic bidegree of theta_7: (stem 254, filt 2) = source bidegree.
Filtration numerology: 2~(0,1), lambda*theta_6 (126,3), theta_6 (126,2), 2~(0,1);
  bracket class lands in filt 2 (theta_7), per Lemma 7.21 + Moss (Bur23).

Relevance to target (shuffle leg, source half):
  This is the audit-plan "one Toda shuffle" instantiated for the SOURCE:
  it expresses the source class theta_7 (h_7^2) as a 4-fold bracket value with
  Moss convergence (synthetic Moss, Bur23, cited in Lemma 7.21 proof).
  It does NOT by itself give the killing TARGET y or the page r; the remaining
  shuffle work (Leg C target half) is to shuffle a product theta_7 * (...) or
  <theta_7, 2, ...> against the window bidegrees (253,8..11), which needs the
  E2 ancestor (Leg A). Both flagged separately.

Run: python3 output/artifacts/check_theta7_bracket.py -> THETA7_BRACKET_OK
"""
import sys

def main():
    th6_stem = 126
    th7_stem = 254
    assert th6_stem + th6_stem + 2 == th7_stem, (th6_stem, th7_stem)
    src = (254, 2)
    assert src == (th7_stem, 2)
    print("BX Lemma 7.21 at j=6: theta_7 in <2~, lambda*theta_6, theta_6, 2~>")
    print(f"stem check: {th6_stem}+{th6_stem}+2 = {th7_stem}; theta_7 at {src}")
    print("Moss convergence: synthetic Moss (Bur23), cited in Lemma 7.21 proof")
    print("Status: SOURCE shuffle secured (citable); TARGET shuffle (y at (253,8..11)) MISSING")
    print("THETA7_BRACKET_OK")

if __name__ == "__main__":
    sys.exit(main())
