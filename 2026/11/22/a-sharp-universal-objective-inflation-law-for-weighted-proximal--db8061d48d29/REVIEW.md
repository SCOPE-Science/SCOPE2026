# Independent mathematical audit

## correctness

PASS

The finite sublinear penalty is the support function of a compact convex C containing zero and having a nonzero point. With A=1+r, B=r+κ, D=r+κ(2−κ), p=Π_C(κb) and q=κb−p, the projection inequality gives p·q≥0 and H(q)=p·q; weighted stationarity then gives xκ=q/B. The true optimal value is ||b||²/2−dist(b,C)²/(2A), bounded below by L=||b||²/2−||b−p||²/(2A). Direct evaluation and B²−D(r+κ²)=κ²(1−κ)² give (A/D)L−f_b(xκ)=(1−κ)²(B p·q+r||q||²/2)/(DB²). Equality thus needs q=0 and tightness of the projection lower bound, giving exactly κb=Π_C(b)∈C. For a norm-maximizer p in C, p·(c−p)≤0 for every c in C, so b=p/κ realizes that equality and is nonzero. A direct scalar check with H=|x| and b=1/κ gives xκ=0 and denominator D/(2Aκ²). The general denominator is positive for b≠0 by the ridge-only lower bound. Completing the square in the proximal step and using nonexpansiveness gives contraction factor (1−κβ)/(1+rβ) with the stated fixed point. The claimed strong-quasar parameter also checks directly against Definition 2.1: the quadratic terms cancel after substitution and leave (1−κ)tH(x). Supplied verification code was inspected, not run; finite box examples do not establish the all-gauge statement.

## originality

PASS

The weighted proximal iteration, its distinction from optimization of the unweighted target, and the projection/thresholding tools are existing material. The distinct supported claim is the exact objective-value worst case, with same-factor attainment for every admissible geometry and a full equality criterion. The closest inspected primary result and matching catalogue candidates do not cover that comparison.

## value

PASS

This quantifies a documented algorithm/objective mismatch by a dimension-free, sharp performance benchmark rather than a bound on displacement. Attainment for every gauge distinguishes the result from a bad scalar counterexample and shows the gap cannot be improved merely by knowing the gauge geometry. The projection criterion also gives an exact diagnostic of extremal data; simple convex tools do not by themselves supply that sharp calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
