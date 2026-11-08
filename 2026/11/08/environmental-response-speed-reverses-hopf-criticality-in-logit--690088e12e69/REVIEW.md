# Review of the environmental-response Hopf-criticality theorem

## Correctness (C): PASS

The equilibrium follows from a logit inverse, the trace and determinant yield a simple positive-frequency Hopf crossing, and the crossing slope is explicitly positive. Third derivatives of the logistic rule and the bilinear payoff are differentiated in physical time. Transforming the local linear part to a rotation and applying the planar cubic radial formula gives the exact coefficient. Its algebraic reduction and positivity inequalities are shown in RESULT.md. The standalone standard-library checker reproduces the reduced coefficient from the full derivative formula at the explicit parameter witness, which is interior and nondegenerate. The assertion about small periodic solutions uses the nondegenerate planar Hopf theorem. No inference of higher-order criticality at the zero-cubic point is made.

## Originality (O): PASS on available evidence, with material residual risk

The source paper arXiv:2311.02745v1, sections III–IV (including its stated future-work paragraph), establishes the interior Hopf location but explicitly leaves the first Lyapunov coefficient unresolved. The result here gives a parameter-space sign classification and an explicit sign reversal under changes of environmental speed alone; these do not follow merely from the already known positive trace crossing. The 2024 logit r-Lambert paper studies a scalar fixed-payoff model and does not include the coupled environmental variable. published-finding corpus searches for the sign reversal, logit environmental feedback, Hopf coefficient, and generalized Hopf produced no identified same-model covering claim. Accessible previous local titles and claims were compared, especially those on adaptive game equilibria and environmental oscillations, with no implication to this two-dimensional cubic calculation.

A 2026 article by Gavin, Paarporn and Cao describes a broad characterization of the stability of feedback-evolving logit games. Its abstract is not enough to conclude either that it covers or does not cover this exact cubic-sign phase boundary. The full text remained inaccessible after arXiv/open-access and authorized institutional-access attempts. This is a material publication-priority limitation, documented rather than treated as evidence of uniqueness. The 2023 source's open question and the mathematical difference from verified full-text sources support a best-knowledge originality assessment, not a certified first-publication claim.

## Value (V): PASS

The initial paper explicitly identifies the sign of the Hopf Lyapunov coefficient as a missing analysis. The theorem closes that local dynamical gap over a large natural parameter region, proves a sharp biological replenishment condition for the possibility of subcritical onset, and constructs a counterintuitive sign reversal caused solely by the speed of environmental feedback. The exact threshold separates locally attracting post-onset oscillations from locally repelling pre-onset oscillations, a structural distinction relevant to hysteresis questions without claiming global hysteresis. This is not a numerical parameter sweep or an arbitrary slice.

## Closest work, scope, and risks

- Paarporn (2023), arXiv:2311.02745v1: same differential equations and Hopf equilibrium; cubic coefficient uncomputed in accessible version.
- Gavin, Cao and Paarporn (2024), arXiv:2409.05044: scalar, no dynamic environment; cannot imply the two-dimensional Hopf sign.
- Gavin, Paarporn and Cao (2026), DOI:10.1109/TAC.2026.3685548: close subject and broad abstract; full text inaccessible, so equivalent coverage is not definitively excluded.
- The zero-cubic-speed equality is not asserted to be a generic Bautin point; all cycle assertions are local and nondegenerate.

Self-review: passed. Independent audit: not yet performed.
