# Self-review

## Correctness

**PASS.** The result is based on the exact first and second derivatives of two moment constraints at the antipodal orthonormal-basis configuration. The orthogonal symmetric/antisymmetric tangent splitting gives the stated Hessian spectrum and multiplicities directly, with the product-sphere normalization explicit. The quartic lower bound is a diagonal projection of the second covariance jet; the displayed analytic second-order correction cancels every off-diagonal jet and the centroid second jet, attaining the bound. The example has an exact, positive rational energy. Checker output: `CROSSPOLYTOPE_EXACT_CHECKS_PASS 1110` (dimensions \(3\)–\(10\) for spectrum, smaller for rank, rational second jets). The infinite-dimensional-index assertion \(d\ge3\) is analytical, not inferred from enumeration.

## Originality

**PASS, provisional.** Xiao–Zhuang (arXiv:2303.05365), inspected at introductory motivation, its general Hessian equations and Platonic examples, provides broad derivative machinery and an octahedral numerical example but not the displayed sharp dimension-uniform local invariants. Needham–Shonkwiler (arXiv:2110.11295, §2.3.2) already provides a general quadratic-cone description of singular complex tight-frame varieties; the qualitative nonintegrability of some infinitesimal modes is therefore prior, not new. Their result does not explicitly calculate the centered-real \(2d\)-point objective's two Hessian bands, balancing ratio, or exact least unavoidable fourth-order residual for fixed first derivatives. The older Benedetto–Fickus frame-potential optimization results concern global minima and general Hessian criteria, not the present joint first/second-moment fixed-velocity coefficient. The regular-simplex \(d+1\)-node Hessian result does not imply the extra nullity and singular quartic behavior at the \(2d\)-node orthoplex. Searches against public mathematical literature and semantic research findings did not expose a statement with this exact implication; historical priority remains uncertain.

## Value

**PASS.** This is a natural optimization defect at a highly symmetric spherical design, not an arbitrary numerical slice: it gives the full local quadratic spectrum, the sole balance of positive curvatures, and a complete sharp fourth-order feasibility test for the entire nonrotational symmetric-pair Hessian kernel. The coexistence of actual design motions and directions with unavoidable quartic cost makes a tangible distinction for trust-region algorithms and for the singular geometry of centered tight-frame configurations. The coefficient is invariant under the allowed second-order corrections, and its nonzero example persists in every dimension. There is no claim of a paper-sized global convergence theorem or of rigidity in all tangent sectors.

## Closest literature and limitations

- Y. Xiao and X. Zhuang, *Spherical Framelets from Spherical Designs*, arXiv:2303.05365, first version 2023-03-09; generic Hessian formulas and octahedral three-design example.
- T. Needham and C. Shonkwiler, *Toric Symplectic Geometry and Full Spark Frames*, arXiv:2110.11295, §2.3.2, first version 2021-10-21; singular cones of complex tight-frame varieties.
- D. G. Mixon, T. Needham, C. Shonkwiler and S. Villar, *Three Proofs of the Benedetto–Fickus Theorem*; general frame-potential minimizers and Hessian methods.

The strict novelty point is the *quantitative, sharp, specific fourth-order coefficient together with the complete Hessian spectrum*, not the generic fact that orthodecomposable frames can be singular. Balanced velocity jets need not integrate to exact designs. No independent expert validation or comparison with every older source has occurred.

Self-review: passed. Independent audit: not yet performed.
