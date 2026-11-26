# Independent mathematical audit

## correctness

PASS

With the 2π STFT convention the usual Weyl displacement has |α|²=π(x²+ξ²)=t. In the Bargmann monomial basis, expanding e^(αz)(z−conj(α))²/√2 and multiplying by the displacement Gaussian gives the h_k coefficient e^(−t/2) α^(k−2) Q_k(t)/√(2k!) up to irrelevant phase or conjugation. This is valid at t>0 for k=0,1 too, taking absent lower monomials as zero. The angular frequency k−2 gives disk diagonalization; normalized planar polar measure becomes dt after angular integration. Independently differentiating the proposed difference produces e^(−a)a^(k−2)[a Q_(k+1)²−(k+1)Q_k²]/(2(k+1)!), by substituting x=a−k, Q_k=x²−k, Q_(k+1)=Q_k−2x. This is the difference of the two densities; both sides vanish at zero, including k=0 after cancellation. For the triple condition, Q_k and Q_(k+2) cannot share a root: subtraction forces a−k=1/2 and k=1/4. The common middle root is a=n+s√n, n=k+1, excluding a=0. There Q_(n−1)=2(1+s√n), Q_(n+1)=−2s√n and Q'_n=2s√n, giving a negative slope for the incoming difference and a positive one for the outgoing difference, hence peak to trough. Adjacent Q's cannot share a positive root since Q_(n+1)−Q_n=−2(a−n). For two distinct middle indices n<m both branches are increasing, so √n+√m=m−n. Isolating and squaring gives rational √n and then integer square roots u,v, with u(u+1)=v(v−1) iff v=u+1. This gives precisely the two stated starts, without asserting that the two triples occupy the same eigenvalue level or that either attains the norm.

## originality

FAIL

A distinct, stronger indexed result, a2df20aeb429, states the same boundary product, complete consecutive triple and no-quadruple classification, and exact paired-triple sequence and indices. Its product also determines the peak-to-trough direction by the signs of the two neighboring factors at a simple root. Thus no mathematically distinct part of the finding survives the coverage comparison. The older generic integrals do not themselves supply the classification. The stronger catalogue record is later-dated; this is a finding of coverage, not a determination of priority or dependence.

## value

FAIL

The boundary product and arithmetic collision locus are well motivated, but they are both already specified by a stronger indexed result that also treats the norm. The one differently worded consequence, the peak-to-trough transition, is a direct sign check on the same simple-root formula; no separate spectral phenomenon or exact invariant not determined by that result remains. The reconstruction has expository value, not a distinct finding on the required standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
