# Scientific review

## Correctness — PASS

The claim concerns the two-factor Kronecker-sum Laplacian with two positive directionally uniform conductances and the completed two-stage Gauss endpoint only. The tensor spectral projectors give all four matrix-entry orbits. Positivity of the scalar Padé filter proves positive diagonals, an explicitly positive polynomial proves positive two-coordinate transitions, and the two remaining entries reduce to a quartic numerator and its coordinate-swapped partner. Their leading coefficients prove the two *necessary* rate inequalities. Those inequalities are simultaneously feasible only for five unordered factor shapes; in exactly those shapes each lower quartic coefficient is positive or nonnegative, giving *sufficiency* at every finite step, including boundary ratios. An explicit Fraction-arithmetic verifier independently reconstructs whole matrices and confirms the displayed algebra. The proof is for all real positive weights and steps, not an extrapolation from finite checks.

## Originality — PASS (best-knowledge, publication priority unverified)

The previously established unweighted classification covers the specialization \(a=b\), but gives no two-rate feasibility interval and does not imply that the unweighted-failing \(K_2\square K_5\) can be rescued by directional anisotropy. Classical Runge–Kutta and strong-stability-preserving theorems instead quantify conditions across broad classes of problems (and often internal stages); they do not produce this graph-specific completed-endpoint classification. The 2022 graph-Laplacian positivity work introduces different integrators. Searches for the two-rate equivalence, the radical boundary, and the ten-site rescue did not return an exact prior result. This is not proof of publication priority: a specialized historical graph-filter paper may be unindexed, and Butcher's survey was not obtained in full, and one later full-text visual rendering was rate-limited. Horváth's original 2005 full paper was inspected and its general threshold/cone results do not state this graph-specific classification.

## Value — PASS

The classification settles an intrinsic timestep-positivity feasibility question for the natural \(p\times q\) complete-coordinate diffusion grid, not merely a numerical instance. The rate interval is an exact and operational criterion. Its disappearance except for five unordered graph shapes, and the possibility of rescuing ten-state positivity by directional weighting despite failure of the unit-weight network, reveal a qualitative boundary that scalar A-stability and universal SSP guarantees do not decide. There is a concrete reason to require this precise fact: selecting anisotropic diffusion rates without positivity limiters for the fourth-order endpoint map.

## Closest literature and limitations

Butcher's *Practical Runge–Kutta methods for scientific computation* (2009, DOI: 10.21914/anziamj.v50i0.2315) supplies the Gauss-method context. Ketcheson–Macdonald–Gottlieb (2009, DOI: 10.1016/j.apnum.2008.03.034) addresses universal implicit SSP rather than this fixed graph. Blanes–Iserles–Macnamara (2022, DOI: 10.1051/m2an/2022042) treats distinct positivity-preserving schemes. Horváth's (2005, DOI: 10.1016/j.apnum.2004.08.026) full 16-page primary text was inspected: §§2–3 establish general RK threshold results, and §4 studies invariant positive cones, not the matrix-entry classification on a weighted rook graph. The theorem does not characterize finite non-global windows, arbitrary edge heterogeneity, or internal stages. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
