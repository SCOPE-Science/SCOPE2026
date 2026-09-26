"""Closed-form forcing-stage bound J(g) (exact arithmetic).

Claim: for normalized gap g>0, let j*(g) = ln(2/g)/ln(4/3).
Then J(g) <= ceil(j*(g)) + 1, where J(g) = least j>=3 with
g*N_j >= (D_j+1)/2, N_j = 2*4^{j-1}, D_j = 2(3^j-1).

Proof idea (checked here): g*N_j - (D_j+1)/2 >= g*2*4^{j-1} - 3^j
(= dropping the -1/+... constants against us: D_j+1 = 2*3^j-1 <= 2*3^j,
so (D_j+1)/2 <= 3^j; hence g*N_j-(D_j+1)/2 >= g*2*4^{j-1}-3^j).
The RHS >= 0 iff (4/3)^j >= 2/g... times constants: g*2*4^{j-1}>=3^j
<=> g*(4^{j}/2)>=3^j <=> (4/3)^j >= 2/g <=> j >= ln(2/g)/ln(4/3).
So at j1 = ceil(ln(2/g)/ln(4/3)), RHS>=0 hence forcing holds up to the
dropped constants (which only helped us: we replaced (D+1)/2 by the LARGER
3^j... check direction: (D_j+1)/2 = (2*3^j-2+1)/2 = 3^j-1/2 <= 3^j. Yes, so
g*N_j >= 3^j implies g*N_j >= (D_j+1)/2. Hence J(g) <= j1; the +1 in the
claim is pure slack. Assert the tighter J(g) <= j1 here, plus the slack form.

Certifies for a grid of g (exact Fractions for J, float log only for the
closed-form bound — bound direction verified by exact re-check at j1):
 g in {1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/100, 1/1000}.

Also verifies monotonicity: smaller g -> larger J (exact, no floats).

Prints VERIFY_OK. Stdlib only (math used only for the candidate bound).
"""
from fractions import Fraction
import math

def N(j): return 2 * (4 ** (j - 1))
def D(j): return 2 * (3 ** j - 1)

def Jof(g):
    j = 3
    while True:
        if g * N(j) >= Fraction(D(j) + 1, 2):
            return j
        j += 1
        assert j < 1000

def main():
    print("closed-form bound J(g) <= ceil(ln(2/g)/ln(4/3)) [+1 slack]:")
    prevJ = None
    for gnum, gden in [(1, 1), (1, 2), (1, 4), (1, 8), (1, 16), (1, 32),
                       (1, 100), (1, 1000)]:
        g = Fraction(gnum, gden)
        J = Jof(g)
        # candidate from floats
        jstar = math.log(2 / float(g)) / math.log(4 / 3)
        j1 = math.ceil(jstar)
        # exact re-check that forcing holds at j1 (no float trust):
        assert g * N(j1) >= Fraction(D(j1) + 1, 2), (g, j1)
        assert J <= j1, (g, J, j1)
        assert J <= j1 + 1
        print(f"  g={g}: J={J}, ceil-bound={j1}, slack-bound={j1+1} OK")
        if prevJ is not None:
            assert J >= prevJ  # smaller gap -> later-or-equal forcing
        prevJ = J
    # key instance
    assert Jof(Fraction(1, 4)) == 8
    # dominance inequality direction re-verified exactly on samples:
    for j in (3, 5, 8, 12):
        assert Fraction(D(j) + 1, 2) <= 3 ** j, j
    print("  dominance (D+1)/2 <= 3^j exact OK; monotonicity OK")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
