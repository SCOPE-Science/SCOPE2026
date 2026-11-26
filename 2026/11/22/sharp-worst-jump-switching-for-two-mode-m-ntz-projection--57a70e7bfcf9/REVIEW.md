# Independent mathematical audit

## correctness

PASS

For h_s=1_(s,1), subtract the mean and project onto v_q=x^q−1/(q+1). The variance s(1−s), covariance (s−s^(q+1))/(q+1) and v_q variance q²/[(2q+1)(q+1)²] give F_q exactly. The signed distributional derivative represents f modulo constants as an L²-valued integral of h_s; its total variation gives the sharp norm upper bound by the triangle inequality, with attainment at a maximizing point. Any equality measure is supported on maximizers. Two distinct step residuals cannot be proportional since their jumps are at distinct points and the projection is continuous, excluding mixed equality even at q=1. Reflection compares the positive secants G_q(s)=(1−s^q)/(1−s), which strictly increase/decrease as q is above/below 1. At the midpoint F'_q has the negative sign of 1−(q+1)2^(−q), so the midpoint is excluded by strict convexity of 2^q relative to its chord through q=0 and q=1 (with extrapolation for q>1). For q>1 F''_q is quadratic in s^q, hence at most two positive zeros and F'_q at most three; signs at 0,1/2,2^(−1/q),1 are +,−,+,−. The third evaluation follows from strict concavity of 2^z−1−(z+z²)/2 on 0≤z≤1 and its zero endpoint values. For q<1, F'_q(s)/s as a function of v=s^q on the right half has second derivative (q+1)/q² times [v^(−1/q−2)−4(2q+1)]<0: its first term is bounded above by 2·4^q≤2(1+3q)<4(2q+1). Opposite boundary signs and strict concavity give exactly one right root. At q=1 write u=s(1−s); u−3u² has maximum 1/12 at u=1/6 exactly. Compactness on the favored halves gives the two optimizer limits; the two variational squeeze inequalities for the maximum give slopes ∂_qF_q(s±)|_1=1/9+s±² log s±. Indeed at s+ the negative log is at least 1−s+, and .788²·.211>1/9; at s− it is less than log 5<2 and 2·.212²<1/9. This verifies both signs and the strict local minimum/cusp without relying on the finite root grids.

## originality

PASS

Pass is confined to the sharp positive-exponent family with optimizer switching, equality rigidity and cusp; the classical affine q=1 calculation and orthogonal projection machinery are not independent novelty. Closest accessible statements address other error/smoothness quantities or other spaces. The plausibly close Cui–Xu paper remains a named full-text risk, not established absent coverage or a priority certificate.

## value

PASS

The power family is the elementary nonpolynomial deformation of linear least-squares fitting. Its exact worst variation-normalized residual is useful for discontinuous data; the two separated best knots at the linear exponent turn into persistent unique one-sided worst knots, with a nonsmooth optimal norm and exact slopes. The structural transition and equality cases go beyond a single classical constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
