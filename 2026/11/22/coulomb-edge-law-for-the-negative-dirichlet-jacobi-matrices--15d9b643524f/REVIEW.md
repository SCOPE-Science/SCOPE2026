# Scientific assessment

## Correctness — PASS
The exact operator uses positive Jacobi hoppings \(a_n=((n+2)/(n+1))^{s/2}\) and fixed \(s>0\). The free Jacobi tail is a compact perturbation, so exterior eigenvalues are discrete. Deleting block interfaces changes counts only by bounded rank; within each block the exact constant-hopping cosine spectrum controls the count. The initial dyadic region contributes at most \(C_s\sqrt{\eta/\varepsilon}+o(\varepsilon^{-1/2})\), the terminal region contributes zero, and the interior has limiting count \(\pi^{-1}\int_0^s\sqrt{s/x-1}\,dx=s/2\). Monotone inversion yields the full eigenvalue asymptotic, and alternating-sign conjugacy gives the negative-edge statement. No finite experiment is substituted for an infinite proof. The standalone checker passed 23 numerical and exact-block consistency checks.

## Originality — PASS, best-knowledge
The original optimal-approximants paper (arXiv:1606.08615v1) identifies the Jacobi family and its relation to extremal zeros, but its inspected Jacobi/operator discussion gives no full \(\varepsilon^{-1/2}\) eigenvalue-count law. The 2021 survey (arXiv:2102.01725v1) presents the unresolved *largest-eigenvalue norm* problem; that question differs from the new tail asymptotic. Zlatoš's Coulomb Jacobi Szegő paper studies sufficient Szegő/eigenvalue constraints, without the count coefficient for these hoppings in the inspected material. Webb–Olver's Jacobi spectral-computation framework concerns effective computations for compact perturbations and does not state this law. Other orthogonal-polynomial special-function Jacobi operators concern different coefficients/spectral regimes. A general discrete semiclassical theorem might subsume the result; priority is not certified, and the scope-specific computation should not be presented as solving the norm problem.

## Value — PASS
The same Dirichlet orthogonal-polynomial recurrence previously motivated a difficult extremal eigenvalue problem. This classification shows an infinite exterior spectrum and gives its **sharp universal Coulomb counting coefficient**, determining all high-index levels to relative first order. It distinguishes two different analytic questions—top eigenvalue versus global spectral tail—and supplies a reproducible reference asymptotic, including both spectral edges, for the natural negative-Dirichlet family. This is not a parameter rename, a finite sample, or a one-off numerical constant.

## References and risks
The five sources are identified in RESULT.md. Potential subsumption by broad semiclassical eigenvalue-counting theory and incomplete historical coverage are explicit remaining risks; no independent audit has been done. Limitations of parameter uniformity, finite corrections, and the unresolved norm are also explicit.

Self-review: passed. Independent audit: not yet performed.
