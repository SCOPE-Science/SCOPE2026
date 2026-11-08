# Scientific review: two-clock permutation quadratic map

## Correctness — PASS

The source's equation (4) is the precise dynamical system treated here. Substitution proves the conjugacy \(u\mapsto u^2\) and the normalized recurrence \(p\mapsto[\alpha I+(1-\alpha)P]p\) without approximations. Cycle Fourier modes of an orthogonal permutation matrix prove the exact sharp Euclidean norm with the longest-cycle exponent. Matrix logarithm expansions prove both endpoint windows, and invertibility of the limiting semigroups establishes their noncollapse for every finite scaled time whenever the initial distribution is not cycle-constant. The accompanying checker directly reproduces these identities and checks convergence on a four-cycle, with all runs passing. No finite experiment substitutes for the general analytical proof. Scope excludes the absorbing boundary states and does not claim orbitwise attainment of the operator norm.

## Originality — PASS within inspected evidence

U. U. Jamilov's 2022 preprint (arXiv:2210.05107, equation (4), Proposition 3.2 and Theorem 3.5) proves fixed-point and omega-limit structure but not the exact normalized transient, the optimal Euclidean relaxation rate, or the two parameter-dependent Poisson critical windows. The 2026 Jamilov–Ladra arXiv:2601.17494 uses a genuinely different quadratic combination with additional pure quadratic interactions; its equation (5.1) is not the present operator. Classical permutation-chain diagonalization and the Poisson-limit matrix exponential are background methods, not standalone originality claims. Relevant research-record searches concerning this operator, rate and boundary windows showed no identical claim among their closest returned records; these negative searches do not establish universal uniqueness. A closely titled Jamilov–Khudoyberdiev 2023 article reports fixed and periodic points and omega-limit sets in its accessible abstract, but its full text could not be inspected, leaving a real priority risk. The inspected literature does not show a stronger theorem implying the exact result for this particular nonlinear map.

## Mathematical value — PASS

A qualitative limit-set classification does not describe how rapidly populations approach their stationary type proportions or how nearly nonmixing permutation cycles persist at small positive mixing strengths. The exact factorization separates a doubly exponential population-mass clock from a slower mode controlled sharply by the longest permutation cycle. The singular window \(n\alpha=O(1)\) retains a residue-class phase, whereas \(n(1-\alpha)=O(1)\) produces an unphased forward Poisson semigroup. These exact boundary profiles resolve a motivated transition between periodic and convergent populations; they are not a parameter-renaming or a numerical increment. The construction does not claim novelty for general finite-state Markov spectral theory.

## Closest literature and limitations

The principal source is arXiv:2210.05107 / DOI 10.46298/cm.10135. The most directly overlapping later title is DOI 10.1080/10236198.2023.2284827, with accessible abstract but inaccessible full text. Jamilov–Ladra, arXiv:2601.17494, concerns a different operator. The result is restricted to this permutation quadratic family, fixed nonabsorbing initial data and the stated parameter scaling; general perturbative robustness and any independently verified priority claim remain open.

Self-review: passed. Independent audit: not yet performed.
