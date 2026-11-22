# Independent mathematical audit

## correctness

PASS

Reconstructed T action off the integer grid as Q(m,n)=(-n-1,m) for n<0 and (-n,m-1) for n>=0, exact ten-case integer rank h, and strict h(Q)=h-1 outside the absorbing labels (0,0),(0,-1); this proves finite entry for every off-grid point without finite extrapolation. In the trap, T exchanges the two squares and T^2 reflects each square, giving T^4=id and exactly two period-two centers. Counting rank cases yields a0=2 and a_{2k-1}=a_{2k}=2k; summation gives 2+2s(1+s)/(1-s^2)^2. Ten cases also establish |h(m,n)-2(|m|+|n|)|<=3; floor-coordinate errors add <=4, so coupling yields W1<=7/R and the triangular density on [0,4]. Inspected RESULT.md blob 3a6d8ee070e26fdc5bbd0ed2953292a8ee4b1d22 and exact-integer check.py f940a870f324e9a3d3636ed8da5c166df1896287. Independently iterated all 2601 square labels in [-25,25]^2 and checked shell counts through k=19; these confirm but do not prove all-index identities.

## originality

PASS

Best-of-knowledge PASS. General piecewise rotations with non-bijective trapping appear in primary literature, but the explicit square-label rank for this particular switch map, complete shell-area generating function, and centered-large-window triangular W1 law are not stated or implied by the checked broad attractor theorems. Highly relevant older Boshernitzan–Goetz full text inaccessible; abstract-only coverage and institutional VPN error are specifically retained, not construed as uniqueness proof.

## value

PASS

A complete first-entry time function, exact Lebesgue shell-area census and quantitative large-window weak limit for a natural non-injective planar piecewise isometry give a coherent global transient-statistics theorem. These exact quantities are independent of a generic qualitative finite-attractor assertion and provide a reusable solvable reference case with provably finite capture and sharp scale normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
