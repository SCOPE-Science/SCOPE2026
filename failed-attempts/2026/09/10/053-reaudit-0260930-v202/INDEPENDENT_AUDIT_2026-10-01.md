# Independent mathematical audit — No multiplicity-2 nodal bitangent class on the central-parallelogram tropical quartic (seven classes of multiplicity one)

Outcome: **FAILED**.

## Correctness
**PASS** — For the named unit square, Pick's theorem gives no interior lattice point and all four sides have lattice length one. Area and incidence counting force 14 remaining unimodular triangles, 15 dual vertices and 17 bounded dual edges, hence genus 3. Lee–Len Theorem 4.4 then gives seven bitangent classes of multiplicity one and no multiplicity-two class. The package's explicit lower-hull witness is consistent with these counts.

## Originality
**FAIL** — Lee–Len Theorem 4.4 already states that every genus-3 tropical plane quartic has seven equivalence classes of bitangent lines, each of multiplicity one. Once the elementary genus-3 count for this unit-square subdivision is made, the headline nonexistence claim is a direct specialization of that published theorem.

## Value
**FAIL** — The final claim is a premise/normalization check obtained by combining Pick/Euler counting with an existing general multiplicity theorem. It corrects the stated target setup but does not add a new structural lemma, classification, or motivated invariant beyond the already-published genus-3 case.

## Originality comparison
- Equivalent formulations: For genus g=3, Lee–Len's multiplicity formula gives 2^(3-g)=1 for each nonzero bitangent class.
- Broader coverage: Lee–Len Theorem 4.4 covers every genus-3 tropical plane quartic, strictly broader than the named central-unit-square subdivision.
- Exact database or table: A special-case table is unnecessary because the general theorem already fixes all multiplicities.
- Claim versus prior implication: After the elementary genus computation, the record's headline follows immediately from the published theorem and is therefore covered.

## Sources inspected
- **Lee and Len, Bitangents of non-smooth tropical quartics, Port. Math. 75 (2018), 67–78** (https://doi.org/10.4171/PM/2011) — Full-text Theorem 4.4 and surrounding proof. The theorem explicitly gives multiplicity one for all seven bitangent classes when genus is 3, so it dominates the final claim once genus 3 is established.
- **Resultary mathematical research index** — Semantic search for central unit-parallelogram tropical quartics and genus-3 bitangent multiplicity. No distinct exact record was needed for the originality verdict because Lee–Len's general theorem is decisive.

## Residual risks
- The conclusion is scoped to the stated unit-square subdivision; other genus-dropping nodal quartics are not covered.
- The exact height vector for this particular regular subdivision may be new as data, but it does not rescue originality of the final claim.
- The correction is operationally useful for avoiding a false target, but that utility is not the same as a substantive new mathematical result.
