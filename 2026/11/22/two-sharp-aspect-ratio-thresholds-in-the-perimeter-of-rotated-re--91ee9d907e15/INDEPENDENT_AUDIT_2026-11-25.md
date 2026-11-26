# Independent mathematical audit

## correctness

PASS

Independent angular-bisector derivation: rotating the axes by θ/2, write α=cos(θ/2), β=sin(θ/2). In the first quadrant the intersection is αx+βy≤a and βx+αy≤1, with the other quadrants obtained by reflection. For 0<θ<π/2 the first inequality is redundant exactly when a≥α/β; the single perimeter segment in the quadrant then has length 1/(αβ). Otherwise the two segments meet at (x*,y*), and their lengths, measured from the axis-intercepts, sum to (x*+y*)/α=(a+1)/(α(α+β)). Multiplying by four and setting t=β/α gives the asserted profile, with agreement at the join and the direct endpoint perimeters 4(a+1) and 8. The sign of the first derivative is that of t²+2t−1; the second branch is strictly decreasing up to t=1. Thus the strict interior pair exists precisely at 1<a<1+sqrt(2), with the square case's maximum at the endpoint and coalescence yielding strict decrease, not a plateau. The sole competing minima when the diagonal candidate is attained are its value 8(sqrt(2)−1)(a+1) and 8, tying only at a=sqrt(2). Read the packaged VERIFICATION.md and scripts/check_rectangles.py: the recorded 21,344 comparisons include independent clipping checks but are finite; the analytic argument establishes equality and all real parameters. The script was not executed.

## originality

PASS

No distinct inspected statement covers the rectangular Euclidean perimeter profile or its two thresholds. The identical indexed record is not independent prior evidence. The strongest adjacent indexed angular-perimeter theorem is for ellipses, and classical equal-rectangle results concern area. Priority remains best-of-knowledge.

## value

PASS

The intersection perimeter is a natural geometric observable distinct from overlap area. The substantive result is the full landscape: a global optimizer jumps before the losing strict local minimum disappears. The sharp coexistence and distinct contact and local-extremum behavior go beyond a clipping recipe or computing a single rectangular configuration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
