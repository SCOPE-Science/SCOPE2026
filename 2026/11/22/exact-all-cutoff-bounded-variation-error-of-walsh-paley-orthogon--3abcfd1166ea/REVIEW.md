# Scientific review

## Correctness — PASS

For each \(N\ge1\), write \(N=M+r\) with \(M\) a power of two and \(0\le r<M\). The first \(M\) Walsh modes are the conditional expectation on \(M\) dyadic cells; the next \(r\) modes are products of the next Rademacher sign with low-level characters. These facts give the exact residual identity for a single step at fractional location \(q\). Completing a square yields the exact maximum \(1/(4N)\) and all maximizing positions. The distributional derivative representation reduces arbitrary interval \(BV\) data to a signed superposition of steps, and the Hilbert-space triangle inequality gives the sharp global estimate. For equality, derivative support lies in the finite argmax set, and distinct maximizing jump residuals are not collinear because their jumps occur off the grid of the corresponding Walsh subspace. Endpoints, the case \(N=1\), and powers of two are included. The extracted exact-rational checker passed 1,658 assertions. Computations are corroboration only.

## Originality — PASS, qualified

A targeted search compared joint Walsh-tail error, sharp Jackson constants, binary cutoff identities, alias statements in coefficient/Dirichlet-kernel language, exact tables, and nearby dyadic/finite Walsh results. Fine [1] gives individual coefficients and dyadic conditional expectations, but neither entails the *sharp all-cutoff joint residual energy* by its stated coefficient bounds alone. Móricz [2] has coefficient-sequence variation hypotheses and limiting convergence, not an exact interval-variation operator norm. Vyas–Darji [3] bounds individual multiple Walsh coefficients, rather than this one-dimensional projection error. Hytönen–Lacey–Parissis [4] proves a variational Carleson theorem with a different operator/norm output. Relevant prior findings on finite Walsh soft thresholding and Haar variation concern other operators or error norms; none of the inspected statements includes this exact claim or a stronger general theorem implying it. Residual risk: unindexed classical approximation results and the inaccessible full text of Gogoladze–Tsagareishvili [5]; the latter's available abstract describes coefficient decay, not a decisive covering theorem. This is a best-knowledge comparison, not proof of global priority.

## Value — PASS

The Paley basis is computationally natural but its non-dyadic partial-sum kernels are nonpositive and have different geometry from uniform-cell averaging. Nevertheless **every** rank has precisely the same sharp variation-normalized integrated error as an \(N\)-equal-cell projection. The exact best constant and complete jump-location classification identify the sensitivity of all digital spectral cutoffs to discontinuities, without requiring an arbitrary parameter slice or asserting unproved universal optimality among all subspaces. Fine's single-coefficient bound alone supplies only a weaker generic tail estimate, so the exact joint energy exploits a genuine cross-coefficient structure. The result supplies a natural complete classification and a reproducible best-constant benchmark.

## Boundaries and historical uncertainty

The claim is for unweighted \(L^2\), ordinary (not periodic) interval variation, and Paley order. It does not classify nonlinear filters, other Walsh orderings or multivariate cuts. Known analogues for Haar detail energies or other Fourier systems do not imply this result. An unindexed historically stronger theorem remains possible; no independent audit has been done.

Self-review: passed. Independent audit: not yet performed.
