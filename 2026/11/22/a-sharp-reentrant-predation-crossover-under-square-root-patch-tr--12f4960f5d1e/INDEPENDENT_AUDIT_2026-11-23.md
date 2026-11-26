# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 5–66 including d=0, d=m and m=K. The weight denominator is nonzero on the closed interval. With a=√(m+d), b=√(m−d) and t=ab, the intake deficit 1−F is K(K+t)/[(K+a²)(K+b²)]=K(K+t)/(K²+2Km+t²). On 0<d<m its intake derivative has the sign of H(t)=K²+2Km−2Kt−t². H is strictly decreasing in t, H(m)=K²−m², H(0)>0, and t decreases with d. This gives strict increase for m≤K (including the flat endpoint when m=K), and a unique decrease–increase turning point otherwise. H(t*)=0 gives F(d*)=1−K/(2t*), with K<t*<m when m>K. Subtraction of F(0) gives the signed factor (m−t)(K−t) with positive multiplier, proving the sole nonzero baseline crossing and its ordering after the minimum. At d=m, F=f(2m)>f(m). For general γ the quadratic term is f″(m)/2+γf′(m)/m, giving exactly K[γK−(1−γ)m]/[m(K+m)³], and analyticity and evenness give remainder O(d⁴) near zero. An initial dip and a larger endpoint give an interior minimum and crossing by continuity, not uniqueness or necessity outside the square-root case. No behavioral dynamics are claimed. Inspected VERIFICATION.md and checker.py; did not execute the submitted checker.

## originality

PASS

Credit predator-weighted spatial functional responses and their qualitative patchiness effects. The supported distinction is the exact fixed-mean two-patch response for Holling II with imposed square-root tracking: full monotonicity/minimum classification and the unique positive contrast at which it returns to homogeneous intake. This is a best-of-knowledge statement based on specific verified catalogue comparisons and bounded literature access, not a historical priority determination.

## value

PASS

Separates two competing effects in a motivated assay holding total prey fixed: local saturation can lower intake from moderate clumping even with positive tracking, while increased predator concentration in the richest patch dominates at extreme concentration. The criterion m=K, unique minimum and explicit return contrast provide an exact reference case for sublinear tracking, and the power-law expansion identifies cases where the qualitative reversal persists under changing the exponent. It is not evidence that actual species follow the posited allocation or that the intake switch controls long-term population dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
