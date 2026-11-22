# Scientific review

## Correctness
PASS. The fixed stability polynomial yields explicit expressions for all nine entries, and exact row stochasticity follows from \(Q\mathbf1=0\). The forward-entry quadratic has a strictly negative discriminant; reverse entries have the single sign cutoff \(3/S\). Strict monotonicity of \(r\) locates the limiting diagonal at the largest departure rate. A positive Bernstein basis on the full reverse-safe interval and the one-sign-change cubic after substitution \(t=u/(1+u)\) establish the precise single-crossing alternative, including endpoints. The one-parameter transition is derived by exact algebra. `verify.py` supplies 11,797 exact checks over 343 integer-rate triples but does not replace the analytical proof.

## Originality
PASS on inspected material, with residual historical priority uncertainty. Gottlieb–Shu–Tadmor supply a universal SSP sufficient bound, not the all-rate exact endpoint classification. Horváth's complete 16-page paper addresses positivity thresholds uniformly over IVP classes and specialized cones, not this rate-dependent three-cycle. The adaptable-weight three-state pure-birth result concerns a different scheme with different quantifiers; a published heterogeneous directed-cycle Crank–Nicolson frontier uses a different rational update. Complete multipartite RK3 results use undirected diffusion and do not contain these cyclic cubic transition formulas. Searches for equivalent directed-triangle/RK3 positivity statements revealed no dominating theorem; that absence is not a proof of uniqueness in all literature.

## Value
PASS. A three-cycle is the smallest nontrivial irreducible one-way circulating Markov network. The exact family-wide positivity frontier gives a sharp algorithm-design rule, distinguishes reverse-edge and diagonal failures, reveals a genuine rate-imbalance phase boundary, and identifies a strict end-step benefit over the established universal SSP CFL bound in every nonuniform case. This is a natural complete classification for an unbounded continuous family of positive rates, rather than a single numerical example.

## Limitations and nearby work
The claimed improvement is for the completed linear step only, not for internal stages or general SSP theory; the result excludes more states and networks with reverse arcs. The historical literature on positivity polynomials could contain an unindexed equivalent specialization. Publication priority should be assessed independently.

Self-review: passed. Independent audit: not yet performed.
