# Independent mathematical audit

## correctness

PASS

Exact collocation differentiation is similar to differentiation on the degree-2r polynomial space; its exponential on that space terminates. Its center row has reflection symmetry and unit sum by constant reproduction; N≥2r+1 ensures weights are not aliased. Independent exact reconstruction from Lagrange polynomials verified the 3/5/7-node weights, symbols and endpoints in RESULT.md lines 37–85. At three nodes the symbol is 1−4μt for t=sin²(θ/2). At five nodes the outer weights impose [1/6,2/3] for μ>0; below 1/6 the symbol decreases in t but remains ≥1/3, and beyond 2/3 the Nyquist symbol exceeds one. At seven nodes the second-neighbor weight imposes [(5−√10)/10,(5+√10)/10]; the first and third are strictly positive and the decreasing center weight is still positive at the upper endpoint. The square decomposition of −15∂tG₃/(4μ) is bounded below by 3 for t∈[0,1], so Nyquist is the minimum. The condition G₃(1,μ)≥−1 is exactly the stated increasing cubic's nonpositive region, with positive root 0.841360228011148…; at the upper positivity endpoint the symbol is −(13+8√10)/45>−1. Even admissible grids realize Nyquist, as needed for necessity under the uniform-over-grids quantifier. The zero step is the identity. For all r≥2, direct differentiation gives ℓ₂''(0)=−r(r−1)/(2(r+1)(r+2)), and the leading coefficient of ℓ_{r−1} is −1/(2r−1)!, giving the stated negative large-step term. The finite algebraic reconstruction supports, but does not replace, this proof. The supplied verify.py was inspected rather than run and covers the first three sizes, not all-r asymptotics.

## originality

PASS

Credit prior local-exponential methodology, conventional Fourier-symbol analysis, standard derivative weights and the classical three-point CFL bound. On the evidence available, the distinct finding is the exact joint positivity and uniform contractivity classification at five and seven nodes, with the universal two-end sign obstruction as supporting structure. Neither the different global exponential findings nor the material available on localized exponentials shows prior coverage of this distinct claim. The central Bayona full-text comparison remains limited by access.

## value

PASS

Users of local exponential heat updates need both a norm stability guarantee and a maximum-principle/positivity guarantee; they are not interchangeable. In particular, reducing an already stable step can produce undershoots even for arbitrarily small positive steps, and the seven-node spectral limit allows steps beyond the positivity window. Exact thresholds at two higher-order stencil sizes and the two-end obstruction for every centered order explain when this numerical distinction matters. This is not a claim of new Fourier analysis or a new three-point CFL result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
