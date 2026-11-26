# Independent mathematical audit

## correctness

PASS

The gamma mixture gives L(t)=theta^r(theta+s t)/(theta+t)^(r+1) and G(z)=L(1-z). For s>0 the positive Lévy kernel is (r+1)e^(-theta x)-e^(-theta x/s); after dividing its derivative by theta e^(-theta x), the positive term is bounded above by, and tends at zero to, 1/s. Thus continuous self-decomposability holds exactly at s=0 or s>=1/(r+1). The count intensities lambda_n=((r+1)q^n-a^n)/n with q=1/(theta+1), a=s/(theta+s), are positive and summable since 0<=a<=q<1. The standard discrete criterion requires b_n=n lambda_n nonincreasing, and its differences are (r+1)(1-q)q^n-(1-a)a^n. The n=1 inequality dominates every subsequent one because a/q<=1. Simplifying at n=1 gives precisely (1), with equality allowed; taking square roots recovers the positive threshold and all-rate regimes, including the separate s=0 endpoint and s=1. In the quotient G(z)/G(1-c+cz), each logarithmic coefficient is (b_n(1)-b_n(c))/n in the rate-scaled notation. Its nonnegativity under the criterion follows from the derivative bound in the repair; if the criterion fails the linear ordinary coefficient is negative for c close enough to one. The frozen proof used the falling-factorial symbol in its differentiation identity, which would give zero for the v=1 derivative when m>=2. The corrected proof uses the rising product for derivatives and the falling product for the distributional factorial bias. Normalized derivatives therefore give weights m! and (m+1)! and land exactly at s=1/(m+2), r=m+1. The analytic separation example r=1,s=1/4,theta=1/4 has first canonical difference 7/100 and fails the continuous cutoff. Finite scripts were inspected but not executed.

## originality

PASS

The repaired result credits the standard continuous and discrete criteria, the established PNXL distribution, and exact separate catalogue coverage of the PGL curve. The full region with free mixing weight, its continuous-versus-thinning separation, and the explicit critical PNXL residual sequence are not covered by the strongest inspected statements. No separate novelty is attributed to the distributional definitions or the PGL restriction.

## value

PASS

An independently varying component weight is the natural full adjacent-shape mixture, not an arbitrary numeric slice. Its exact count frontier gives both a family of explicit witnesses separating continuous and discrete decomposability and an innovation law on the admissible side, rather than just a sign computation. The critical all-order PNXL residual identification gives a concrete structural invariant that cannot be read off from the original PNXL PGF without computing the changed weights. It is useful even with the known PGL curve and general canonical tests credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
