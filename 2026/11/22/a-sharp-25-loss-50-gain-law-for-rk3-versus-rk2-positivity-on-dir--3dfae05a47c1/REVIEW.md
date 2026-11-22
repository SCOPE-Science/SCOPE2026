# Review: sharp RK3 versus RK2 Markov-cycle positivity comparison

## Correctness — PASS

The claim concerns final step matrices on directed cycles with at least four sites and strictly positive heterogeneous exit rates. For both degree-two and degree-three exponential Taylor stability polynomials, the proof enumerates every matrix-entry type using the fact that no three-step path can wrap around a cycle of length four or more. The degree-two one-hop entry gives the exact cutoff \(2/A\). In degree three, the diagonal scalar is strictly decreasing with one positive root \(\rho\), the one-hop quadratic has negative discriminant, the two-hop term changes sign once at \(3/C\), and the three-hop term is positive. These facts prove necessity, sufficiency and no reentry, not only a numerical observation. The inequalities \(M<A<C<2A\) imply the strict ratio bounds; two explicit four-cycle rate families approach them. For the single-defect family the switching condition is algebraically equivalent to \(R=\rho/(2-\rho)\). The standalone checker independently reconstructs exact rational matrix powers (52,032 entry comparisons and 7,488 row-sum comparisons) and tests horizons and extremal families. Risks: finite testing cannot replace proof; proof is restricted to constant-rate-in-time autonomous cycle generators and completed steps.

## Originality — PASS (provisional historical priority)

The directly relevant published finding *Exact RK4 positivity on heterogeneous directed cycles and a sharp CFL gain* (2026) classifies degree-four steps for at least five vertices. Its local-walk expansion has some reusable method, but its fourth-order one-/three-hop obstructions and its single-order gain constant do not entail the exact degree-two/degree-three pair/triple cutoff, four-cycle boundary cases or the sharp two-sided RK3/RK2 comparison. The published *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs* (2026) establishes a third-order disadvantage on a different, undirected uniform-weight graph family, rather than this directed variable-rate frontier. Full relevant texts were compared. Blanes–Iserles–Macnamara (2021/2022) present positivity methods for graph differential equations, Horváth–Song–Terlaky (2014/2015) offer general invariance and polynomial-root bounds, Horváth (2005) establishes uniform positive-IVP class thresholds, and Gerisch–Weiner (1999/2003) optimize positivity of low-order explicit schemes for splitting problems. They do not give the claimed universal two-method ratio and rate-defect reversal on directed cycles in the inspected material. Search and comparison do not prove global historical uniqueness: undocumented or differently indexed specialist results remain a residual risk.

## Value — PASS

Selecting between commonly used second- and third-order explicit integrators for conservative transition networks is a natural design problem because a negative transition probability renders a completed numerical step physically inadmissible. The result proves a sharp all-size, all-positive-rate comparison with both a genuine 25% asymptotic loss and 50% asymptotic gain, and a natural one-site rate-defect switch. It supplies exact decision criteria without searching high-dimensional matrix entries or estimating a generic SSP lower bound. The observed gain is a positivity-step comparison, not a claim about total computational work, long-time accuracy or nonlinear methods.

## Primary literature and proximity

- S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models* (2021), https://arxiv.org/abs/2102.08242.
- Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron* (2014), https://arxiv.org/abs/1406.6755.
- Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods* (2005), https://doi.org/10.1016/j.apnum.2004.08.026.
- A. Gerisch and R. Weiner, *On the positivity of low order explicit Runge–Kutta schemes applied in splitting methods* (1999), https://www2.mathematik.uni-halle.de/reports/sources/1999/99-35report.pdf.
- *Exact RK4 positivity on heterogeneous directed cycles and a sharp CFL gain*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-rk4-positivity-on-heterogeneous-directed-cycles-and-a-shar--36d0a038ee0c.
- *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-positivity-radii-and-an-order-three-reversal-for-taylor-ru--0aa3ec090e79.

Self-review: passed. Independent audit: not yet performed.
