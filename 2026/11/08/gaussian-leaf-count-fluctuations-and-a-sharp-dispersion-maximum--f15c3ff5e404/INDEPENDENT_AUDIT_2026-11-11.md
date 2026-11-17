# Independent mathematical audit

## correctness

PASS

For trees n>=3, every leaf has leaf-degree zero, total leaf-neighbor weight is L_n, and the leaf count increments by one exactly when a nonleaf is selected. Hence P(delta L=1 | L_n)=1-a L_n/(a n+L_n). The unique drift fixed point r in (1/2,1), exact deviation recursion with contraction b_n=a^2/[(a+L_n/n)(a+r)], and L2/L4 estimates justify replacing it in L2 by linear contraction kappa=a²/(a+r)². Bounded-increment triangular martingale CLT yields V=r(1-r)/(1+2kappa) and moment convergence; derivative of V as function of r gives unique maximizing root of 6r³-15r²+16r-6 and threshold crossing 1/12. Independent rational finite-chain mass conservation, fixed-point algebra, and symbolic derivative checks passed. Finite enumeration does not prove the asymptotic normal law.

## originality

PASS

Hartle and Krapivsky define the same leaf-neighbor-driven attachment mechanism and the fixed-point leaf fraction r(a), and already find the a=1 degree-tail transition. Their accessible paper content gives total leaf-count variance 1/12 for the distinct uniformly attaching random recursive tree. No inspected result supplies V(a), this fixed-a CLT, its sharp maximum or finite crossing for leaf-PA(a). The later ordinary-degree PA joint degree/leaf-degree paper uses a different selection rule. Priority is qualified because the entire 2026 original article could not be accessed despite OA and authorized attempts.

## value

PASS

An exact dispersion curve and sharp unique maximizer for a natural recently introduced leaf-driven attachment model is a meaningful stochastic-growth classification. The maximum lies away from the known leaf-degree tail transition a=1, providing a non-obvious separation of two model features.

The dated certificate retains the supplied scientific assessment, sources and limitations.
