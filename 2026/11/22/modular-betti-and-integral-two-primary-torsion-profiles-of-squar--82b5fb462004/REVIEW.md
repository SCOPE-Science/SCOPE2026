# Self-review

## Correctness — PASS
The Lie bracket is alternating and two-step nilpotent. Splitting the alternating Chevalley–Eilenberg complex by the distinguished covector yields a degree-preserving square-zero derivation of an exterior algebra in characteristic two. The tensor-factor homology computation and the rational characteristic-zero kernel comparison prove the Betti and integral two-primary cyclic-summand rank formulas for all stated integers. The local finite calculation and exact low-rank Smith checks are corroborating, not a proof by extrapolation. The statement does not determine the orders of the even torsion factors.

## Originality — PASS relative to inspected sources
Armstrong–Cairns–Jessup (1997), DOI:10.1090/S0002-9939-97-03607-1, treats exactly the no-extra-central-generator family in characteristic zero and records restrictions on extending to positive characteristic; at the first exceptional rank the two profiles actually differ. Armstrong–Sigg (1996), DOI:10.1017/S0004972700021936, similarly studies complex Lie algebra cohomology. Arroyo et al., arXiv:2406.06819, concerns real almost-abelian geometric structures. Targeted mathematical searches found no exact modular Betti or two-primary summand-rank formula. The closest indexed positive-weight integral almost-abelian result has a semisimple, rather than nilpotent square-zero, adjoint. Some potentially relevant indexed content and earlier unindexed works remain uninspected; no absolute priority or independent certification is claimed.

## Value — PASS
The first exceptional rank reveals a genuine modular cohomology jump and integral two-primary torsion absent from rational cohomology; the complete uniform formulas quantify the entire exceptional family. This is a structural all-dimensional invariant, not a routine numerical increment or a claim about a single small case. The stated boundaries are mathematically important: ordinary alternating cohomology only and torsion multiplicities rather than exponents.

## Verification and limitations
The standalone Python standard-library verifier constructs full CE differentials and compares computed ranks and polynomial coefficients, while separate finite exact integer Smith checks corroborated the first torsion cases. The proofs are algebraic and cover all dimensions; the finite checks do not themselves prove that coverage. Independent external verification, historical completeness and stronger integral invariant factors remain open.

Self-review: passed. Independent audit: not yet performed.
