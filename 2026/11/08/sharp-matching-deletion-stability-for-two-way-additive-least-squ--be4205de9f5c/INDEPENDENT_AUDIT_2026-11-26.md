# Independent mathematical audit

## correctness

PASS

The connected bipartite design has rank 2n−1. Woodbury applied to the full-table hat matrix gives the stated deletion identity. Independently collecting terms, let x_e mark the deleted indices used by observed edge e, m_e be their count, d_e=n−2+m_e, and S be the number of coordinates shared by e,f. The kernel is S/n + (x_e·x_f)/[n(n−2)] − d_ed_f/[n(n−2)T]. Shared-coordinate entries are positive; the limiting unmarked-coordinate bound at n=3,r=1 can be equality only for two once-marked cells with that shared coordinate, forcing e=f and S=2. Disjoint cells with no marked overlap are negative. One overlap is nonnegative exactly when both cells are marked once (zero at r=1). The twice-marked reversed cell is positive since 2T−n²>0 for n≥3,r≥2. Each coordinate line has d-weight T, so disjoint cells have total weight (n−2)T+d_e. For a once-marked row remove the n−r unmarked other-end overlap cells and subtract contributions of r−1 negative overlap cells; for a twice-marked row remove the reversed cell and subtract 2(n−2) negative overlap contributions. This gives negative masses N_0=(n−2)/n+(n−2)/(nT), N_2=(n−2)/n and N_0−N_1=[(r−n/2)²+3(n−2)²/4]/[n(n−2)T]. Row sums equal one, giving the norm and the strict maximizing-type classification; the triangle equality gives the union of maximizing-row sign patterns. Data in [0,1] have sharp signed minimum −(norm−1)/2, the negative of the defect magnitude in the frozen wording. The decrement formulas follow by subtraction; T_(n−2)=(n+1)(n−2) gives the final-step ratio. The repaired proof specifies the small cases, sign convention and unchanged observed-cell scope. An independent exact grounded-Laplacian check (`python3 reproductions/frozen-1-5-reproduction.py deletion`) verified 166 representative rows for six sizes between 3 and 15, also checking the r=1 zero entry. A separate exact regression check agreed on 39 designs and 1370 rows for 3≤n≤8. Neither check substitutes for the general proof; the frozen checker was inspected but not run.

## originality

PASS

This is a pass for the repaired intermediate family, not credit for isolated known cases quoted in the frozen statement. Exact prior indexed results cover intact and one-edge-deleted bicliques (including the r=1 maximizing cells), and the full crown norm. The repaired RESULT.md and SLOGAN.txt distinguish these from the remaining 2≤r<n law and its optimizing cells, and the exact enhanced final decrement. The compared sources do not cover that remainder on the bounded evidence available.

## value

PASS

The maximum uniform amplification of the standard real additive fit is a natural, directly useful invariant, not a diagonal leverage score. For the intermediate family the exact extremizing cells and strict decay under successive deletions quantify what the known one-deletion and crown endpoints do not. The last step loses the only remaining zero-mark target and produces the exceptional exact gain; that structural transition and the signed fitted-value bound survive removal of the known cases as new claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
