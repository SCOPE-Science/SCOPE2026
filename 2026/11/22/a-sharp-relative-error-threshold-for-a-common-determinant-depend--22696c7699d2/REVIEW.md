# Self-review

**Claim reviewed.** For finite distinct-triple teams with named alphabets \(r,s\ge2\), the least universal relative-error tolerance of \(=_p(x,y)\lor =_0(x,z)\) is \((r-1)(s-1)/(rs-r+1)\); each team's exact decision criterion is a fiberwise weighted maximum, and the sharp cases are exactly unions of whole nonempty \(x\)-fibers. The complete proof and reproduction code are in `RESULT.md` and `verify.py`.

## Correctness — PASS

The denominator is the cardinality of the approximate **subteam**, not of the input team; the normal-form argument explicitly covers possible overlap and empty sides. Every candidate split normalizes to one row-and-column cross per \(x\)-fiber, yielding the exact inequality. Uniform averaging proves the universal bound, and equality of all cross scores forces every nonempty fiber to be a full rectangle. Proof calculations and normalization were reconstructed directly, and the checker compared the original full lax semantics against an independent formula on 848 finite teams with exact rational arithmetic. Finite enumeration is corroboration, not a general proof.

## Originality — PASS within inspected evidence

Closest primary literature: Fröhlich–Häggblom–Hirvonen–Hirvonen, arXiv:2608.16570 (2026), Definition 2.1 and Theorem 5.1; Fröhlich–Kolaitis–Meier, arXiv:2508.16146 (2025), Theorem 21. The former studies exactly the relative-error convention but proves hardness for a different-determinant mixed split. The latter establishes four-coherence for \(p=0\), which is a boundary case and does not imply the sharp positive-error threshold. A published exact-size enumerator for the same zero-error split counts satisfying teams, not individual minimum error tolerances or all full-rectangle extremizers. Searches for shared determinants, weighted row-column crosses, relative split budgets, parameter equivalences and implication coverage did not identify a dominating claim. Specific residual risks: inaccessible full text of the closest enumerator and incomplete historical priority coverage; searches are not a proof of historical priority.

## Value — PASS

The result gives a natural and exact structural island inside a recently shown computationally difficult approximate-dependence setting. It supplies an efficient decision test for arbitrary teams, the sharp universal alphabet-dependent tolerance, and a complete classification of inputs that force that tolerance. This quantifies an interpretable robust database-splitting phenomenon beyond the previously known zero-error coherence property. The claim is scoped to one approximate and one exact atom and makes no complexity assertion for arbitrary approximate formulas.

## Independent status and limits

The proof is a finite combinatorial argument for every named alphabet size; checker data alone cannot certify the universal statement. Historical priority has only been compared to inspected public literature and searchable records, without independent adjudication. No independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
