# Independent Audit — 2026/09/14/023

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `fb008094daddee36d62cfaf85084da13c4eca456`
- Disposition: **FAILED**

## Correctness

**PASS** — The explicit permutations have cycle types (4,2,2,1,1,1,1), (6,3,2,1), and (6,4,2); under the verifier's standard function-composition convention their product is the identity. The generated group has order 12!, is transitive and primitive, so it is S_12, and the total ramification deficit is 22, giving genus zero. This is a complete Riemann-existence certificate for complex realizability. The phrase in RESULT.md about 'left-to-right map composition' is conventionally confusing relative to the verifier implementation, but it does not invalidate the witness itself.

## Originality

**FAIL** — By 2025 Wang et al. reported a complete, non-redundant computational enumeration of all non-realizable branch-data triples through degree 31. The degree-12 realizability status of this passport is therefore already covered by a stronger exhaustive prior classification. The submitted explicit S_12 witness is a convenient certificate, but it does not make the headline realizability decision an original scientific result.

## Scientific value

**FAIL** — The only fully reproducible headline contribution is one explicit permutation triple for a status already covered by the degree<=31 classification. The additional census numbers are secondary and, in this public package, the raw census arrays/scripts needed to reproduce the 532032/831-class claims are not supplied. Without a field-of-moduli, field-of-definition, or explicit Belyi-map computation, the remaining scientific payload is too small.

## Sources

- The Hurwitz existence problem and the prime-degree conjecture: A computational perspective (Yiru Wang; Bingqian Li; Yi Zhou; Zhiqiang Wei; Yu Ye; Yiqian Shi; Bin Xu): https://arxiv.org/abs/2512.06545 — Reports complete non-realizable branch-data enumeration for degrees up to 31, covering this degree-12 existence status.
- A Database of Belyi Maps (Michael Musty; Sam Schiavone; Jeroen Sijsling; John Voight): https://arxiv.org/abs/1805.07751 — Background on computational Belyi passports and explicit map databases; the published database work is not the source of the degree-12 status.

## Limitations

- The explicit transitive S12 witness and genus-zero calculation are independently verified.
- The audit did not independently reproduce the record's full 831-class census because the public artifact inventory contains only the witness verifier rather than the raw census material described in RESULT.md.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
