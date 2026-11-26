# Independent mathematical audit

## correctness

PASS

The frozen claim FAILS: its Finding incorrectly says that beyond H only the hub diagonal is negative. For m=2,k=1,h=6>H=2, the diagonals are −1/5,−1/20,−1/20. Direct exact multiplication (I+3L)C=I−3L verifies this witness; the frozen checker only compares the diagonal ordering and misses the inference from ordering to sign. The corrected files in /workspace/repairs/4/ retract that assertion and give both thresholds. In the repaired proof, the mutually orthogonal projections for star eigenvalues 0,1,m+1 give the four entry formulas. The scalar divided difference strictly decreases on 0<z<1 by strict convexity; for z>1 the even numerator decreases, and for odd k the derivative test holds because z(t^k)'=(k/2)(1−t²)t^(k−1)≤k(1−t)t^(k−1)≤1−t^k<1+t^k, t=(z−1)/(z+1). Continuity at 1 joins the intervals, proving strict leaf off-diagonals; hub off-diagonals are positive from |b|<1. Even diagonal positivity follows directly. For odd k, the leaf diagonal exceeds the hub by (m−1)(a^k−b^k)/m>0, so the hub crossing gives the exact nonnegativity horizon and is the sole zero there. The leaf diagonal is continuous and strictly decreasing (positive weights on a^k and b^k, with odd k) from 1 to (1−m)/(m+1), so there is a unique later leaf crossing and all diagonals are negative afterward. The coth formula gives strict growth and the O_m(k^(−1)) expansion for the first threshold. `python3 /workspace/repairs/4/verify.py` passed 693 exact-rational star-power cases, two exact hub crossings (including k=3), a rational bracket at steps 4 and 5 for the leaf crossing at m=2,k=1, the failure witness at step 6, and the four-path even-power counterexample. Those checks are finite; the analytic proof establishes the unrestricted repaired result. The original failed evidence is preserved.

## originality

PASS

The surviving distinct result is the sharp completed-map positivity and entry-sign classification for repeated odd powers k≥3 on unweighted stars, in particular the exact first horizon. The raw spectral entry formulas, unconditional even-power consequence, and one-step horizon are covered ingredients. The repaired leaf crossing does not on its own constitute an independent novelty claim. The nontrivial step beyond the known filter criterion is control of the strict divided-difference sign for the signed odd filter, which allows the exact first diagonal crossing to determine the positivity of the entire completed map.

## value

PASS

The surviving classification gives the precise allowable step for a repeated odd-step diffusion output map, distinguishes the first loss of positivity from negativity of all diagonals, and quantifies the increasing tolerance with completed odd power. It explains how a completed even map can be positive despite negative intermediate iterates, while the four-path witness bounds transfer to other trees. This is a sharp, natural completed-output invariant and not a stagewise SSP, damping or accuracy guarantee. The known even and one-step facts alone are not a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
