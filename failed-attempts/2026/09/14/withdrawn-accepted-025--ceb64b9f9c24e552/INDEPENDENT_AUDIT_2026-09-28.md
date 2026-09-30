# Independent Audit — 2026/09/14/025

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `922c257cdaddddb16a9af1c1e20a74047fbafbbd`
- Disposition: **FAILED**

## Correctness

**PASS** — The explicit arrays have the stated cycle types (4,2,1^6), (5,4,3), and (7,3,2), and under the record's explicit compose(a,b)[i]=b[a[i]] convention the product is the identity. The generated subgroup is transitive, primitive, has order 12!, and vinf^6 has type (7,1^5), so the S12 identification is correct. Riemann-Hurwitz gives genus zero, and the centralizer of S12 in its natural action is trivial. These facts establish complex realizability and trivial cover automorphism group.

## Originality

**FAIL** — The headline realizability decision is already subsumed by Wang et al.'s complete computation of non-realizable branch-data triples through degree 31. The record adds a concrete S12 witness and census for this one passport, but the underlying yes/no Hurwitz-existence result is not new relative to that exhaustive classification.

## Scientific value

**FAIL** — The explicit witness and Nielsen counts are useful computational metadata, but the record stops before the more arithmetically informative questions: field of moduli, field of definition, explicit Belyi map, and Galois orbits. For a realizability status already covered by a complete degree<=31 classification, the added one-passport census does not provide enough independent scientific value.

## Sources

- The Hurwitz existence problem and the prime-degree conjecture: A computational perspective (Yiru Wang; Bingqian Li; Yi Zhou; Zhiqiang Wei; Yu Ye; Yiqian Shi; Bin Xu): https://arxiv.org/abs/2512.06545 — Complete non-realizable branch-data enumeration through degree 31, which already fixes this degree-12 passport's realizability status.
- A Database of Belyi Maps (Michael Musty; Sam Schiavone; Jeroen Sijsling; John Voight): https://arxiv.org/abs/1805.07751 — Context for explicit Belyi maps, passports, automorphism groups and arithmetic data beyond a bare transitive triple.

## Limitations

- The audit independently checked the witness, product, transitivity, primitivity and S12 group order but did not rerun the complete 142/66 Nielsen census.
- No statement is made about the field of definition or Galois orbit of the submitted passport.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
