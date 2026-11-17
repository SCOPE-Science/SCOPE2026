# Scientific review

## Correctness — PASS

The theorem is proved analytically for fixed \(0<a<b\) and \(d>0\). Differentiating the transformed coordinates yields a classical two-dimensional Lotka--Volterra system with the exact original-time clock \(dt=w_*W\,d\tau\). The energy levels are compact periodic curves. Eliminating the other coordinate gives an exact two-branch physical-time density, including the square-root singularities at its two turning points. The global inverse-branch bounds show that its excess mass above unit density is \(O(\log(2+h))\) while its support width is \(h/\lambda+O(\log(2+h))\), yielding both the physical-time period and total-variation Pareto limit. The probability concentration and persistent means follow from branch control and exact logarithmic balance identities. Algebraic identities and illustrative quadratures were recomputed from the attached checker. No numerical extrapolation is used in place of the proof.

## Originality — PASS within inspected evidence

Banaji--Boros--Hofbauer (arXiv:2304.02303v1, Section 5.2) supply the chemical model, center regime and coordinate time change. Boulnois (arXiv:2301.00673v1, Sections 3--4) and Genda--Fidlin--Lenci--Gendelman (DOI:10.1007/s11071-024-10667-y, Appendix C) analyze high-energy periods of the classical Lotka--Volterra oscillator. These prior results cover the reduction and anticipate the period scale, but do not state or give an implication establishing the **original physical-time weighted concentration distribution** and its \(O(\log(2+h)/h)\) total-variation approximation by a Pareto law, or the associated chemical-state concentration/mean contrast. The high-energy period asymptotic alone does not imply a quantitative phase-occupation law. Indexed semantic searches for equivalent formulations, all-parameter stronger theorems, and tables returned related but distinct chemical and center findings. Unindexed equivalent occupational asymptotics remain a publication-priority risk; a general high-energy Lotka--Volterra path formula could potentially be developed into another proof, but the inspected papers do not establish this quantitative theorem.

## Mathematical value — PASS

A globally periodic chemical reaction center has a natural high-energy singular regime: its trajectories come arbitrarily close to a boundary extinction equilibrium while also making rare very large excursions. The theorem supplies a universal one-parameter Pareto law for the **observable concentration in physical time**, not just a period quadrature. In particular it proves that typical concentrations vanish while exact positive time means remain pinned at their interior equilibrium values; the distinction exposes a non-uniform-integrability mechanism and clarifies why averaged concentrations alone misrepresent high-amplitude chemical oscillations. The quantitative total-variation error controls the full event-probability law and is not a normalization or arbitrary finite calculation.

## Closest literature and boundaries

The center and its first integral are derived from the source's time-changed predator--prey system, not presented as novel. The historical large-energy period work is explicitly acknowledged. The new theorem applies only on strictly positive stoichiometric planes \(z-y=d>0\), for fixed \(0<a<b\) and large energy \(h\). No uniformity in parameters, noise robustness, or global off-plane attraction is asserted. The rate upper bound is not claimed optimal. The priority comparison is same-model and bounded to accessible indexed and full-text sources, not independent certification.

Self-review: passed. Independent audit: not yet performed.
