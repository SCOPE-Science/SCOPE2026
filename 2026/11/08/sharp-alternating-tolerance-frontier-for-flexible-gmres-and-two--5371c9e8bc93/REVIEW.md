# Independent mathematical audit

## correctness

PASS

For exact-arithmetic Euclidean FGMRES with 0<a,b<1, the established flexible residual projection identity yields R_j <= mu_j/sqrt(1-R_{j-1}^2). The continuant D_j=D_{j-1}-mu_j^2D_{j-2}, D_-1=D_0=1 gives gamma_j^2=mu_j^2 D_{j-2}/D_{j-1}. For the tridiagonal zero-diagonal offdiagonal a,b matrix, Perron strict finite-row bound ensures all D_j>0 when a+b<=1, and Rayleigh quotients establish a first failing minor when a+b>1. The explicit A=I invertible rank-one flexible preconditioners attain the bound at any finite nonterminal index and cause nonzero-residual breakdown at the first failing index. Elimination gives even-continuant recurrence and exact boundary closed form. Two-step restart gives sharp per-cycle factor ab/sqrt(1-a^2) for a^2+b^2<1 and a otherwise, always <1. Independent rational 2-periodic determinant tests verified selected choices. These are worst-case and exact-arithmetic claims only.

## originality

PASS

PASS best-of-knowledge: Güttel and Nyman 2026 Propositions 3.1-3.2 already give the flexible per-iteration residual identity and general recursive inequality with variable inner residuals and a sharp constant-tolerance specialization. The current contribution is NOT that recurrence. The inspected primary paper does not give the two-periodic necessary-and-sufficient frontier a+b<=1, explicit Chebyshev/repeated-root profile, invertible-adversarial sharpness for all finite m, or distinct two-step restart wedge and sharp Phi. Resultary query found same finding and adjacent but non-dominating GMRES phenomena, no stronger prior coverage. Older Saad/Simoncini-Szyld full texts remain a priority risk.

## value

PASS

PASS: choosing alternate inner solve tolerance levels is a natural practical cost/accuracy pattern. The sharp global triangle and restart-rescue wedge are mathematically motivated structural boundaries: they separate a dimension-independent guarantee from explicit admissible nonconvergent Arnoldi cases. The two-stage restart classification is an independent worst-case tradeoff unavailable from fixed-tolerance estimates alone, useful for future preconditioning analysis without claiming solver runtime improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
