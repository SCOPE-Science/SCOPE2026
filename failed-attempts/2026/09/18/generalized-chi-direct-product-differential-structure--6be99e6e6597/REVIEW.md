# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Disposition: **failed**.

Correctness: **PASS**. Reindexing the coordinates of the displayed map by the cycles of addition by \(v\) gives exactly \(d=\gcd(n,v)\) independent blocks of length \(\ell=n/d\). For odd \(\ell\), the direct-product map is a permutation. The derivative equation therefore factors blockwise, and a difference supported in one block attains the ordinary-\(\chi_\ell\) maximum differential probability \(1/4\), while additional active blocks only multiply smaller factors. Thus the \(n\)-bit differential uniformity is \(2^{n-2}\). Direct products preserve the order of identical factors, inverse degree, inverse monomial counts under coordinate relabeling, and the track partition under iteration. The repository verifier checks representative finite cases, but the acceptance of these statements rests on the direct-product proof, not on finite enumeration.

Originality: **FAIL**. The final claim is mechanically implied by prior ingredients. Feng–Wang–Yu–Zhang define the generalized map; the residue-class decomposition by \(\gcd(n,v)\) follows immediately from its indices, and their later v2 explicitly records the stretching/equivalence viewpoint. Schoone–Daemen already give the ordinary odd-\(\chi\) inverse monomial formula and differential formula, while the ordinary order is established in the state-diagram literature. Once the map is recognized as a direct product, the claimed order, inverse degree, Kronecker DDT factorization, differential uniformity and no-cross-track iteration are routine direct-product consequences. Under the required implication standard, absence of the exact combined sentence does not make those inherited invariants original.

Scientific value: **FAIL**. The generalized family is motivated, and an exact invariant summary can be useful in practice, but the final surviving content is only the immediate transport of already known invariants through a coordinate direct-product decomposition. It does not establish a new structural boundary, classification, counterexample or nonmechanical exact invariant. The record itself describes the contribution as straightforward deductions from the now-published track decomposition. That is below the required scientific-value threshold for an accepted finding.

Detailed evidence, source inspections, originality comparisons, checked sources and residual risks are in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

The original same-model review remains historical evidence and is not relabeled as independent.
