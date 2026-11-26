# Independent mathematical audit

## correctness

PASS

PASS applies to repairs/2/RESULT.md, not to the literal universal velocity-completion sentence of the original. Originally w0=0 satisfied the homogeneous displayed moment equation but adjoined no direction: take X=(1,1)^T, V=(1,0)^T, unit weights, velocity nodes 0,1 and M=J=1. The mean 1 is physically attainable, while the second column of XSV^T is identically zero and the momentum is always zero. The replacement requires w0 nonzero and nonnegative; b>0 then implies positive mass, and normalization proves w0 is outside W if its target mean was missing. For the main theorem, the weighted marginals Fb and F^Ta are nonzero in their respective factor spaces; conversely the normalized product gives the target mass and momentum and exact rank one. Normalizing the spatial marginal gives the two independent r-variable LPs. The closed convex feasible core set gives existence and uniqueness of its squared-distance minimizer by coercivity and strict convexity. The velocity slice is compact; at a vertex its positive-support columns must be independent in the stacked constraint matrix of rank n-r+1. For codimension one, singleton zero-coefficient supports and opposite-sign pairs exhaust vertices (a pair of zero coefficients gives a nonextreme mixture). The support bound is sharp: take the first n-r+1 entries constrained equal and the rest free, with b all ones, and use the normalized constant block with all free entries zero. Both completion obstructions are independent; once both are absent the same product witness works, also for rectangular cores. Independently checked 240 weighted opposite-sign-pair balances exactly and the zero-vector obstruction; replay: python3 /workspace/independent_checks.py 2. The frozen verifier was read, not run; finite checks do not establish the theorem.

## originality

PASS

The distinct contribution is a complete arbitrary-fixed-space feasibility classification for this correction problem, including the spatial obstruction, global vector momentum with arbitrary positive quadratures, the codimension-one image hull, and minimal target-specific completion. The product witness and basis-feasible support argument are classical ingredients, not claimed as new. A distinct same-day polynomial-grid record contains the marginal/product reduction in its restricted setting and the three-node numerical interval, so neither is treated as a separate new result here. Its assumptions and theorem do not cover the final arbitrary-space claim. No priority ordering is inferred from the shared publication date.

## value

PASS

For the exact, practically motivated S-correction with otherwise unspecified feasibility, one can diagnose which factor space blocks prescribed moments before attempting the squared-distance problem, replace a joint r²-variable decision by separate r-variable feasibility tests, and construct an exactly minimal per-side direction when necessary. The result is useful as an arbitrary-space structural criterion, not as discovery of rank-one coupling, a three-node table entry, a runtime bound, or a guarantee for dynamical corrections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
