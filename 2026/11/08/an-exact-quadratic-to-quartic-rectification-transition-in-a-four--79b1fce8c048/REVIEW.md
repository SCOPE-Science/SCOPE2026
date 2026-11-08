# Scientific review: exact quadratic-to-quartic rectification transition

## Correctness — PASS

The object is a four-site, two-particle continuous-time exclusion ring with strictly positive site-departure rates \((a,b,1,1)\) and analytic bias \(|\varepsilon|<1\). Its six-state generator and current row are explicit in `RESULT.md`. Irreducibility ensures the unique stationary law. At zero bias, the detailed-balance distribution is proportional to \((1,b,b,a,a,ab)\). Recursive exact solution of the normalized stationarity equations gives the displayed factored quadratic coefficient, while direct rational elimination after \(b=3/a\) gives the fourth-order coefficient. The sign and zero classifications follow because all denominators are strictly positive. Exact reflection symmetries account for the three remaining zero components. The program `verify.py` reconstructs the matrices and passes exact symbolic and independent determinant calculations. No finite experiment is used as an infinite-system proof.

## Originality — PASS, qualified

The original 2025-12-03 exclusion-ring preprint states a conjecture about nonzero quadratic rectification absent two symmetries. A public independent mathematical result already disproves that general claim using a four-site, two-particle ring with all four trap rates different. That isolated existence result is prior art and is **not** counted as the contribution here. The specific newly assessed statement is the complete two-contrast parameter classification: exact sign formula, four zero components, and a non-reflective surface with a strictly nonzero **quartic** leading even response at every nonsymmetric point. Neither the original paper nor the inspected independent witness states or implies those exact parametric formulas. The later boundary-driven paper studies a distinct open-system protocol; its abstract was read, but its full text could not be inspected, leaving a limited publication-priority risk. No universal classification beyond this four-site family is claimed.

## Value — PASS

Rectification is an experimentally meaningful sign-sensitive transport observable, and the first nonzero even response determines its weak-bias scaling. The calculation resolves whether missing quadratic response necessarily signals an exact reflection: it does not. Moreover, it separates three distinct behaviors in the smallest nontrivial half-filled ring: exactly symmetric response, quadratic rectification, and quartic rectification on an algebraic parameter curve. This continuous classification and its sign map are mathematically more informative than an arbitrary isolated counterexample. The specific adjacent-contrast family is natural because it introduces the minimum two nonbaseline trap rates capable of breaking a reflection on a four-cycle.

## Scope, literature and remaining risks

Primary sources: Sakai–Akimoto, arXiv:2512.03316, main text and Appendix C; the public four-rate counterexample dossier and linked result; Sakai–Akimoto, arXiv:2609.03560 (abstract available); and earlier current-fluctuation background, arXiv:2408.11364. The already-known general refutation is a substantial limitation to novelty, but does not subsume the factorization and sharp quartic-onset classification. The present result is finite-state, local in the applied bias and specific to a periodic two-particle system. Independent literature-priority validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
