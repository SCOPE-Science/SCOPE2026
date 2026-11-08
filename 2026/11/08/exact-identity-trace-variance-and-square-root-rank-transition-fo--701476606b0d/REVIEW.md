# Scientific review: identity-trace risk of Gaussian tensor trains

## Correctness (C): PASS

The claim is an exact variance identity for the independent Gaussian-core tensor-train distribution and its two asymptotic phase classifications. The proof reconstructs the full normalization, uses two sufficient Gram invariants, derives their conditional Gaussian fourth-moment recurrences entry by entry, and contracts the terminal core. The square-root rank transition follows from the leading eigenvalue of a positive two-state matrix, including the second-eigenvalue remainder; the fixed-order large-mode transition follows from its small-parameter expansion and an independent first-core conditional-variance lower bound. The normalizing denominators distinguish relative trace risk from Frobenius-scale risk. Exact rational identities, monotonicity checks and independent seeded core contractions were run by `verify_tt_identity.py`. Risks: no floating-point guarantee or arbitrary-matrix extension is claimed; random simulations alone would not prove either infinite family.

## Originality (O): PASS, qualified

The primary Gaussian-TT source, Bujanović–Kressner–Olić, arXiv:2606.15679v1 (2026), defines the same distribution and proves general moment bounds, a sufficient rank for trace-scale concentration, and a first-core lower bound for the identity's Frobenius-scale variance. The source does not supply the exact two-invariant finite-order recursion or the critical square-root-rank relative-variance law. Meyer–Avron, arXiv:2309.04952 (2023), gives an exact formula for independent Kronecker-product Gaussian probes, which covers bond rank one but not correlated contractions at bond ranks above one. Related random matrix-product-state work concerns alternative ensembles or statistics. Searches in publicly available mathematical sources, research records, and accessible previous claims revealed no equivalent or stronger result. Searches cannot prove uniqueness. Residual risk remains from earlier Gaussian tensor-network norm-moment literature, including material not inspected in full.

## Value (V): PASS

The identity is an unavoidable positive-definite benchmark for Gaussian TT trace estimation, and the originating numerical-analysis paper singles it out as a Frobenius-scale obstruction. Exact risk replaces an order-only lower bound with finite-parameter selection data. The square-root bond-rank boundary identifies a substantially different requirement for this specific test matrix than the sufficient rank linear in tensor order used for uniform trace-scale concentration. The complementary large-mode limit identifies a nonvanishing exact excess over Gaussian-probe variance at the critical Frobenius-rank scale. The claim is motivated by a natural estimator and metric, rather than an arbitrary parameter slice. It does not assert the same threshold for all input matrices or a matching probability tail bound.

## Closest sources and uncertainties

- Bujanović, Kressner, Olić (2026), *Stochastic trace estimation with tensor train random vectors*, https://arxiv.org/html/2606.15679, Definition 1 and Sections 3–4: same law, upper moment estimates and identity lower bound; no exact displayed transfer or critical law found in reviewed material.
- Meyer, Avron (2023), *Hutchinson's Estimator is Bad at Kronecker-Trace-Estimation*, https://arxiv.org/abs/2309.04952, Theorem 1: full product-Gaussian risk (bond rank one) but not multibond Gaussian TT.
- Garnerone et al. (2010), *Statistical properties of random matrix product states*, https://doi.org/10.1103/PhysRevA.82.052312: related statistical ensemble; only abstract-level inspection was available, so an equivalent hidden norm formula cannot be excluded.

The practical limitation is that variance is not, by itself, a nonasymptotic failure-probability theorem. The priority limitation is not a mathematical defect in the proof but a risk of equivalent earlier moment-transfer calculations.

Self-review: passed. Independent audit: not yet performed.
