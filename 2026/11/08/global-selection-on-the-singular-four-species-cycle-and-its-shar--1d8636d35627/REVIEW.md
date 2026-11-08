# Scientific review

## Correctness

PASS. The model reduces to a singular four-by-four interaction matrix with a verified rank-three kernel; the exact diagonal multiplier and all leading minors are established symbolically. Strict positivity of the quadratic form away from the equilibrium line supplies a proper decreasing relative entropy, allowing LaSalle's invariance argument to apply globally in the positive orthant. The conserved logarithmic level intersects the positive equilibrium segment exactly once, and transversality of its level set establishes exponential convergence. The converse for diagonal certificates follows from the forced relation between left and right kernels, not from a numerical search. `verify.py` repeats the pivotal algebra and limited finite integrations.

## Originality

PASS under inspected evidence. Murdie et al. (arXiv:2609.28833, Sections 2–3 and Appendix D) already give the equations, singular coexistence line, conserved quantity and local stability-with-shift description; none of those is claimed new. The examined full-text sections do not state the all-positive global exponential-selection theorem, or the unique-diagonal-certificate computation and its exact algebraic cutoff. General Volterra–Lyapunov literature (Hong and Pego, arXiv:2102.00611, Sections 2–3) supplies the traditional relative entropy method for nonsingular strictly stable matrices, not the computed singular-matrix threshold here. Searches for exact parameter equivalents and related indexed findings returned no covering assertion. Further historical-priority confirmation remains appropriate.

## Value

PASS. A critical line of ecological equilibria poses a nontrivial selection question: local zero-eigenvalue stability alone does not preclude excursions to boundary attractors or cycles. The new theorem identifies a sizable exact parameter interval of fully positive global convergence, gives each initial condition an explicit unique limit, upgrades to exponential convergence, and establishes the optimal boundary of a natural diagonal entropy technique. The polynomial boundary is a certificate threshold rather than a conjectured global bifurcation.

## Sources and limitations

Primary: Murdie et al., arXiv:2609.28833, first submitted 2026-09-23. Classical matrix/entropy framework: Hong and Pego, arXiv:2102.00611. Full-text comparisons were made for the source model, its coexistence and conservation appendix, and the general stability framework. Remaining risk: an older treatment of the same singular family might give an equivalent exact multiplier cutoff; no exhaustive historical survey is claimed. The convergence theorem excludes the certificate endpoint and all larger parameters, despite the certificate having a well-defined endpoint.

Self-review: passed. Independent audit: not yet performed.
