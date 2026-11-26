# Independent mathematical audit

## correctness

PASS

Orthogonalizing against 1 gives K(s,t)=1+(u(s)-m)(u(t)-m)/v with u(t)=exp(-lambda t). Convexity in u(s) reduces the absolute row integral to the two endpoints; a sign test attains it there. The strictly positive mean of (1-u)(u-q) gives v<(1-m)(m-q), so the monotone endpoint rows cross once with the asserted root ordering and opposite signs at t=0. Their primitives give the displayed branches. Since the signed row mass is 1, an indicator of the negative part attains the most negative output over data in [0,1]; this is the sharp lower value meant by the negative-overshoot wording. For the small-rate check, the equivalent basis function g=(1-u)/lambda has mean 1/2-lambda/6+O(lambda^2) and variance 1/12-lambda/12+O(lambda^2). Substitution gives the frozen endpoint-row corrections 3t^2-4t+1 and 2t-3t^2; integrating with the signs at the simple limiting zeros 2/3 and 1/3 gives derivatives 4/27 and -4/27. The shifted sign intervals affect the expansions only at O(lambda^2). At large rate k_+=2lambda+2+O(1/lambda), 1-k_+m=-1-2/lambda+O(lambda^-2), and z_+=1/(2lambda)+O(lambda^-2). Thus the zero is at log(2lambda)/lambda+O(lambda^-2) and (k_+/lambda)(1-z_+)=2+1/lambda+O(lambda^-2), yielding exactly the stated norm correction. The other row is 1+O(1/lambda), so only the first row matters in this limit. No all-rate branch dominance is needed.

## originality

PASS

The inspected comparisons establish the general Lebesgue-kernel framework and an antecedent for the constant 3, not prior coverage of this real finite-interval two-mode rate-dependent calculation and its corrections. The strongest related catalogue results change the domain, the sampling law, or the observable. The narrow pass is for the exact rate dependence and asymptotic layer for this projector, not for least-squares norm methods or the envelope 3 in general.

## value

PASS

The exact amplification of uniformly bounded data and the exact loss of positivity concern a natural two-mode least-squares model. The comparison of nearly coalescing modes with rapid decay separates a polynomial-limit sensitivity from a logarithmic correction and locates the row sign change. These are quantitative facts unavailable from just a generic kernel estimate or the limiting constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
