# Independent mathematical audit

## correctness

PASS

Writing t=1−s and Q=(P−alpha 1^T)/t gives P=BQ with B=tI+alpha 1^T. On the zero-sum hyperplane B acts as tI, and on the one-dimensional quotient it acts as 1. Thus det B=t^(n−1); direct multiplication gives B^(-1)=t^(-1)(I−alpha 1^T). Reversing the factors in the polynomial adjugate identity yields the source formula even for singular Q. Each cofactor is affine separately in the stochastic columns; expanding Q as the product of its column mixtures represents the whole adjugate as a convex combination of deterministic-map adjugates, so triangle inequality bounds its norm by a vertex maximum. Ranks <=n−2 contribute zero; permutation vertices give t^(n−2)(1+s−2a). At rank n−1 there are a duplicated column pair u,v and an omitted row k; the right and left kernels are spanned by e_u−e_v and e_k respectively. A unit nonzero cofactor fixes the scalar in adj Q to ±1. The norm becomes 2t^(n−2)max(1−alpha_k,alpha_k), which is bounded by 2t^(n−2)(1−a) since alpha_k<=s−a<1−a, and attains it for alpha_k=a<1/2. Replacing one duplicated column by a mixture with the omitted output gives |det Q| equal to its positive mixing weight and cofactor continuity proves the claimed invertible supremum. All steps include n=2; at s=1 the unique matrix has rank one and gives the stated continuous limit (zero for n>=3, 2(1−a) for n=2). Absolute column sums are the induced norm over either scalar field.

## originality

PASS

The inspected nearest results concern stochastic determinants, unrestricted determinant-weighted inverse asymptotics, or the stationary system I−P. The distinct supported contribution is the exact finite-dimensional norm extremum for P with a fixed nonuniform minorant, including sharpness in the invertible subclass. Common-minorant decompositions and the simplex vertex argument are standard ingredients.

## value

PASS

The fixed common minorant is intrinsic to finite Markov operators, and the adjugate is the continuous extension of the determinant-weighted inverse norm needed in the near-singular regime. The exact dependence on s and the smallest entry, the rank-deficient extremizing geometry, and the explicit invertible approach separate this stability invariant from a stochastic determinant bound or a mixing estimate. The uniform refresh corollary supplies a genuine sharp dimension-dependent suppression law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
