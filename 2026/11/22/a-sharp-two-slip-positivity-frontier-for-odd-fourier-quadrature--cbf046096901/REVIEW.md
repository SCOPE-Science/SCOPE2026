# Independent mathematical audit

## correctness

PASS

Distinct nodes give unique interpolation and thus unique normalized weights. Equating old uniform cardinal coefficients at the two reflected shifted nodes forces w_0=w_1=1/S and gives the displayed signed csc expression for all other weights. Its denominator is positive. Odd unchanged indices have positive corrections; among even indices the two endpoints j=2,n−1 maximize the csc sum by strict convexity and reflection. Thus the first sign loss is exactly H_n(α)=1, at those two and no others. The sine ratios increase strictly in α, start at zero, and give H_n(1/2)>1 by the limiting first ratio and the two positive remaining terms. For fixed α each ratio increases strictly with x=π/n by monotonicity of t cot t; hence the odd-size crossing increases to a_*=(√3−1)/2. In the expansion, H_∞−1=(4a²+4a−2)/[(1−a²)(2+a)] and the x² coefficient of H_n at a_* is 2a_*/3. Dividing by H_∞'(a_*) gives √3/24, so the crossing has the stated negative n⁻² correction. For n=3 the moved-node gap equals π at α=1/4, giving just one zero; at n=5 and α=1/3 the three surviving nodes form a uniform three-point degree-two rule. For the noise formula, subtract the two shifted cardinal rows from the original two unit rows. Their sum is orthogonal to uniform weights, their squared norm is 4+2Q−4S/n, and the scalar coefficient is 1/S. It is nonzero for α>0 by the sign correction in an unchanged weight. An independent real sin/cos moment-system solve at (n,α)=(3,1/4),(5,1/3),(7,0.34),(7,0.36),(11,0.21),(11,0.41) matched the sign checks and squared norms to floating precision. Read VERIFICATION.md, verify.py and verify-output.txt without executing the supplied verifier; all-size correctness follows from the analytic identities, not the finite checks.

## originality

PASS

The supported distinct result is the exact odd-size threshold, first-zero pair, finite-size correction and noise law for the outward adjacent-pair path. The strongest inspected comparisons involve inward motion, other shift/erasure patterns, or worst-case guarantees rather than an exact statement on this path. The exact match cbf046096901 is the same record, not another result. The n=3 degeneracy and broad perturbation framework are not the novelty claim.

## value

PASS

For an ordinary interpolatory circle rule, the result identifies exactly which unchanged samples first require negative quadrature weights when adjacent timing errors push two nodes apart. It quantifies the gap between this local path and general grid perturbation guarantees, gives its odd-size limiting law, and measures independent sample-noise variance even on the positive side. This does not improve worst-case jitter guarantees or certify a deterministic discretization error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
