# Scientific review: sharp Bessel-zero law for the SEP current–density resolvent

## Correctness — PASS

The claim concerns the \(L^2(0,t)\) operator \(A_t\) with kernel \(e^{-(u+v)}I_1(2\sqrt{uv})\), its largest eigenvalue \(\Lambda(t)\), and the analytically continued one-body current–density resolvent. The positive Gram decomposition gives compactness, positivity and the simple Perron eigenvalue; a positive source vector proves the leading negative real pole is not removable. The explicit Feller branching Laplace transform identifies the semigroup; the finite-interval cutoff proves \(\Lambda(t)<1\); the rank-one expansion proves \(\Lambda(t)=t^2/2-2t^3/3+O(t^4)\). The nontrivial large-time step is checked through sampled-to-continuous killing, with kernel domination in Hilbert–Schmidt norm, and the Dirichlet eigenvalue \(j_{1,1}^2/4\). The supplied verifier passed 89 deterministic assertions. Mathematical proof, not finite sampling, covers all \(t>0\).

## Originality — PASS (qualified)

The 2026 parent paper establishes the microscopic one-body equation and exact Bessel transition kernel (arXiv:2610.18626, equations (14)–(22)), but the inspected material does not give the closest complex pole or the two-sided short-/long-time convergence-radius theorem. Earlier current statistics (arXiv:0902.2364) and large-scale macroscopic fluctuations (arXiv:2202.05213) do not imply the stated finite-microscopic-time expansion as a quoted result. Bessel spectral theory and killed branching diffusions are established tools, so novelty is confined to their exact use in the SEP transformed current–density resolvent and its sharp analyticity boundary. Published-result databases and relevant earlier scientific claims were searched for aliases, resolvent poles, principal eigenvalues and Bessel roots; relevant related but noncovering mathematical records are identified in the structured audit. The parent's appendices were not fully retrievable; this leaves a genuine publication-priority risk, not proof of uniqueness.

## Value — PASS

The perturbation series in the current-tilt parameter is an actual analytic method for the exact interacting-particle current–density profile. The principal-eigenvalue identification gives the precise convergence disk for every finite microscopic time, proves all singularities lie on a negative real axis, and quantifies the singular approach of the nearest one to the physical boundary using a non-obvious Bessel-zero constant. This sharp cross-scale limit requires distinguishing discrete sampling from continuous absorbing dynamics and is not a routine re-expression of the source's known current cumulants. It helps determine when current-tilt expansions can legitimately be used near large observation times.

## Closest literature and limitations

Bénichou–Grabsch 2026 (arXiv:2610.18626) is the essential parent kernel; Derrida–Gerschenfeld 2009 (arXiv:0902.2364) establishes current statistics; Mallick–Moriya–Sasamoto 2022 (arXiv:2202.05213) covers macroscopic fluctuations; Grebenkov's Bessel spectral review (arXiv:1904.11190) supplies general background. The present result concerns analyticity in \(\omega\), not necessarily the physical \(\lambda\)-plane; it assumes step Bernoulli data, an infinite symmetric exclusion lattice, and positive microscopic time. A closed-form exact finite-\(t\) eigenvalue is not claimed. Independent priority and formal audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
