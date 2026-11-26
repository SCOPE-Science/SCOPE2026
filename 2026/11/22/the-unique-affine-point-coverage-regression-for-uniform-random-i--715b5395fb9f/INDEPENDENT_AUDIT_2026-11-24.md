# Independent mathematical audit

## correctness

PASS

Condition first on the labels of the covering intervals. Conditional on those labels, the intervals remain independent, and the noncovering intervals fall left/right with probabilities t^2/s and (1-t)^2/s. The unordered pair overlap probabilities are 1 for two covering intervals, 2/3 for mixed pairs (three iid endpoint ranks on the side of contact), and q=(2/3)(t^4+(1-t)^4)/s^2 for two noncovering intervals. Summing gives the same conditional mean for every label choice of size k. Its second difference is 1-4/3+q=(s^2-c^2)/(3s^2)=(2t-1)^2/(3s^2). Since K_t is Bin(n,c) with c in (0,1/2], every k is attainable and for n=2 the single second difference already tests affineness. At the midpoint the mean is n(n-1)/6+(n-1)k/3. For a vertex-edge incidence, the difference between pair-overlap probabilities when that vertex covers and when it does not is c/3+s(2/3-q)=c/(3s). Hence its covariance with the coverage indicator is cs*c/(3s)=c^2/3; there are n(n-1) incidences and all other pairs are independent. For edges sharing a vertex, put L=left endpoint and U=one minus right endpoint of the shared interval. The conditional overlap is g=1-L^2-U^2. Under the density 2 on L,U>=0, L+U<=1, the moments of L^2, L^4 and L^2 U^2 are respectively 1/6,1/15,1/90. These give E[g]=2/3, E[g^2]=22/45 and Var(g)=2/45. Each edge has variance 2/9; disjoint edges are independent; the 3 binom(n,3) unordered shared-vertex pairs each contribute twice. This gives Var(E_n)=n(n-1)(2n+1)/45. Substitution verifies the exact squared correlation. The factor c^3/(1-c) is strictly increasing, and c has its unique maximum at the midpoint. There the affine conditional mean is the unrestricted L^2 projection as well, and the ratio tends to 5/8. No maximization of the unrestricted ratio off the midpoint is needed or attributed to the record. Continuous strictly increasing endpoint CDF transport preserves the endpoint order and coverage. The finite rational source checker was read, not executed; the analytic reconstruction, not its finite sample cases, covers all t and n.

## originality

PASS

The distinct claim supported by comparison is the whole finite fixed-point regression, its unique affine point and the exact all-t linear-prediction formula. The older verified overlap is the uniform model, first-order edge and clique statistics, and midpoint-maximal single-interval coverage. The joint-Gaussian catalogue record overlaps on midpoint moments and the value 5/8 but treats the adaptive maximum and expressly does not claim the finite midpoint regression as new. The whole original 1988 paper remained unavailable; this is not a historical-priority certification.

## value

PASS

A single fixed-point depth count is a simple natural local statistic and the total edge count is global. The exact curvature obstruction distinguishes the midpoint from every competing fixed location, and the finite efficiency curve measures the quality of a one-statistic linear predictor, with the midpoint predictor additionally optimal among all functions of its count. This goes beyond the already known midpoint coverage maximum and is not a claim about adaptive clique size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
