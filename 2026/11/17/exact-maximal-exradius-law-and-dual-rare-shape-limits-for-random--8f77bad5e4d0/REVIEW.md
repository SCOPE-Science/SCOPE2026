# Independent mathematical audit

## correctness

PASS

Anchoring at a named sample point and ordering two independent uniform relative angles gives constant normalized density 2/π² in two angle coordinates. From Δ/(s−a_i), the sine law and half-angle identities, the exradius is 4 sin(A_i/2) cos(A_j/2) cos(A_k/2); pairwise ratios are tan(A_i/2)/tan(A_j/2), so the largest angle picks the largest exradius. With A largest, set u=B+C and v=B−C. Positivity and B,C≤A give |v|≤min(u,2π−3u), and the inverse Jacobian |∂(B,C)/∂(u,v)| is 1/2. The source's phrase naming the Jacobian direction is reversed, but the density 3/π² counting all three labels uses the correct inverse factor. Product-to-sum gives L=2cos(u/2)[cos(u/2)+cos(v/2)]. Its fixed-u sections give the asserted CDF with total mass one. Section minima decrease from 4 to 3/2 with equality at the equilateral point only; four is attained on the closed simplex only at the vertices. Fixed-u level sections have measure zero, proving no atoms by Fubini. Continuity on the connected open simplex and its positive density give strict increase between endpoints. At the minimum the linearization is sqrt(3) max_i δ_i, dominating a constant times the norm on the zero-sum plane; the uniform quadratic error and uniqueness localize the event to O(ε). Rescaling by ε gives a triangular limit of two-coordinate area 3/2, mapped affinely to the uniform Dirichlet simplex. At a corner the deficit is B²+BC+C²+O((B+C)^4); the event is bounded on the sqrt(ε) scale and the quadrant ellipse has area π/(3sqrt(3)), via the stated 60-degree sector map. The density and three corners give the upper coefficient, with constant labeled weights. For both tails the normalized indicators converge in L¹ on bounded rescaled domains, giving TV for the specified shape vectors. The scalar limits follow from 1−3 min_i D_i and squared radius respectively, in distribution. Independent split-interval quadrature using roots of the minimum and maximum section values gave F(2)=0.095449527761, F(3)=0.597104810021, F(3.8)=0.925231523525; the last displayed digits of the frozen approximations differ at about 10^−9, not in the exact CDF.

## originality

PASS

The supported distinct result is the evaluated maximum-exradius CDF under the full circumference-uniform model, the two sharp endpoint constants, and the conditional angle laws. The deterministic sharp lower bound, exradius identities, angular simplex law and incircle distribution are not credited as new. No accessible distinct statement or dominating evaluation of this maximum and both marked limits was identified.

## value

PASS

This is a natural maximum with a classical sharp deterministic lower bound. The full CDF quantifies proximity to both extremes; the distinct powers arise from different local geometry (a maximum of linear forms at the equilateral triple and a quadratic deficit at three corners). The uniform Dirichlet and labeled sector limits identify the actual rare shapes rather than only giving another scalar moment or restating the support inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
