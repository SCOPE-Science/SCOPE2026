# Scientific review: central-junction quantum capture on finite gaskets

## Correctness

**PASS.** The claim concerns the combinatorial Laplacian on the level-\(g\) gasket and three positive-loss top-level *internal* junctions. The proof starts from the exact Schur reduction of a triangle of copies, including the necessary \(+z\) correction for shared vertices, and obtains two scalar junction resolvents. Its polynomial recurrence is checked algebraically, and three exact Bézout identities together with algebraic-integrality exclusions rule out every possible numerator/denominator cancellation. The scalar resolvents are Stieltjes transforms of finite real-symmetric matrices, so their reduced denominator degrees count distinct observable poles; these give the dimension \(13\cdot 2^{g-2}+1\) for all \(g\ge2\). The no-jump dissipation argument handles any three strictly positive rates. Independent finite-field Krylov reconstructions cover the first five nontrivial graph levels under two moduli; numerical rank tests corroborate but do not establish the infinite result. Risk: no independent human proof assessment has occurred.

## Originality

**PASS on examined evidence, with historical-priority risk.** The main closest source is Darázs et al. (arXiv:1405.5078), whose Section V and Table IV already report the first finite central-junction trapping values; those exact finite-level values are not claimed as new. The examined article treats this problem numerically rather than deriving the all-generation central-junction rank polynomial. Burgarth et al. (arXiv:1111.1475) provide general controllability and zero-forcing criteria, not the rank of this non-zero-forcing three-junction set. A known all-generation exterior-corner absorption law involves a different three-vertex support and does not determine the internal-junction spectral measure. Related gasket spectral-projector literature, including Allan–Barany–Strichartz, may provide a route to the result; the complete text of that particular article was not accessible, so historical priority is not guaranteed. No relevant inspected source implies the explicit central-junction formula on its face.

## Mathematical value

**PASS.** The existing finite numerical table posed a concrete spectral transport question: its internal-junction trapping values suggested a recurrence, but finite tables cannot establish one. The result gives an exact infinite-family law, a structural two-channel proof, and the asymptotic captured fraction \((13/6)(2/3)^g\). In contrast with exterior-corner capture, the central triplet accesses roughly 30 percent more modes at large generation, a physically motivated placement difference rather than an arbitrary slice. A precise finite-scale law remains useful independently of finite-time relaxation estimates.

## Sources and limitations

Closest primary source: Darázs et al., *Transport properties of continuous-time quantum walks on Sierpinski fractals* (2014), https://arxiv.org/abs/1405.5078, Section V and Table IV. General method: Burgarth et al., *Zero forcing, linear and quantum controllability for systems evolving on networks* (2011), https://arxiv.org/abs/1111.1475. Plausible historical competitor: Allan, Barany and Strichartz, *Spectral operators on the Sierpinski gasket I* (2009), https://doi.org/10.1080/17476930802272978 (abstract available, full text inaccessible during this review). The result requires unweighted finite graphs, uniform real hopping, and strictly positive absorption at all three junctions; it does not cover arbitrary detector sets or absorption times.

Self-review: passed. Independent audit: not yet performed.
