# Independent mathematical audit

## correctness

PASS

The frozen scalar profile follows by writing |a+be^(it)|^2 as (|a|-|b|)^2 plus 4|a||b| times the squared half-angle sine measured from the opposite-phase point. The greatest circular distance is min(pi,d+psi), and the ratio of the two squared sines decreases strictly until the denominator saturates. Independently, interpolate the affine pencil from the two nodes z_+=e^(i theta), z_-=e^(-i theta). For theta<|t|<=phi the sum of the moduli of the two interpolation coefficients is [sin((|t|+theta)/2)+sin((|t|-theta)/2)]/sin(theta)=sin(|t|/2)/sin(theta/2); for |t|<=theta the inner arc bound applies directly. This proves the same upper bound for values in any complex normed space, hence operators and all matrix levels. The pencil A=-B attains it. For a nonzero scalar pair a maximum attaining the bound must occur at |t|=phi by strict sine monotonicity; both interpolation coefficients there are nonzero. Equality forces equal endpoint moduli and phase alignment of the two weighted values. At t=phi the coefficient ratio has phase -e^(i theta) for the negative-node coefficient divided by the positive-node coefficient, so p(z_+)=-e^(i theta)p(z_-), equivalently (1+e^(i theta))(a+b)=0. The negative endpoint is symmetric by conjugation. Thus for nonzero pairs exactly a=-b gives equality. Restriction is contractive at every matrix level and fixes constants, so the reverse norm and cb norm are one. The result concerns only the marked map.

## originality

FAIL

Although the direct marked-map wording was not found, the exact sharp coefficient is a corollary of the earlier Resultary Lebesgue-function formula, not merely of a neighboring optimized sampling norm. In 71dc11a952c3 equation (2), use outer half-width phi, midpoint m=0 and half-separation parameter d=theta/2. Its exterior branch is exactly sin(|t|/2)/sin(theta/2) for theta<=|t|<=phi. Every affine polynomial is its own interpolant. Bound the node data by the smaller arc norm and bound the remaining interior interval directly by that same norm. This immediately gives the claimed transfer and the standard 1-z witness (also identified for the exterior term in 993d6ac7ac17). The same interpolation identity is vector-valued with the same bound, and reverse restriction is trivial. Scalar equality adds just equality in the two-term interpolation triangle inequality.

## value

FAIL

A quantitative comparison of marked arc planes is a natural question, but this coefficient is already obtained by plugging the two endpoints of the inner arc into a prior pointwise interpolation formula on the outer arc. The sharp witness, operator-space step and equality condition require only the affine identity, triangle equality, or restriction. No new optimization or useful unknown sharp fact remains beyond that mechanically implied result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
