# Independent Audit — 2026/09/10/036

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `65b36c47d5dafd174207a18b018f326148cd7587`
- Disposition: **FAILED**

## Correctness

**PASS** — The special-fiber construction itself is correct. Three nodes chosen as a trigonal fiber make each 3-point evaluation map rank one; after compatible frame normalization, the normalization map for F has one scalar compatibility condition, so h0(F)=3 and E0=F⊕F has h0=6. The arithmetic genus and multidegree are correct. The record's componentwise slope paragraph is not, by itself, a proof of semistability on a reducible curve, but the conclusion can be independently completed: for this stable two-component curve the canonical polarization has weights (1/2,1/2), is a good polarization, and the bidegree-(3,3) line bundle F induces the same polarization; standard good-polarization results make F stable, hence F⊕F polystable and semistable.

## Originality

**FAIL** — Once one chooses two trigonal pencils and glues three points lying over a common P^1 fiber, the h0=3 line-bundle calculation is an immediate normalization-sequence construction; doubling F to F⊕F mechanically gives rank 2, degree 12, and six sections. The record does not establish a new smoothing, stable-bundle phenomenon, or nonstandard degeneration theorem beyond this direct construction.

## Scientific value

**FAIL** — The example is strictly split/polystable on a reducible special fiber and the record itself shows that perturbing the gluing drops h0 from 6 to 5 while generic gluing gives h0=2. With no smoothing to a stable bundle on a smooth Clifford-index-4 curve, it does not resolve or materially advance the genus-10 Mercat boundary; as stated it is a standard special-fiber example rather than a validated research finding.

## Limitations

- The semistability conclusion required an external good-polarization argument not present in the record's componentwise slope proof.
- No statement is made here about existence or nonexistence of a smoothing retaining six sections.

## Sources

- Stability of vector bundles on curves and degenerations: https://arxiv.org/abs/1401.0556 — Shows reducible-curve stability requires an explicit notion; introduces polarization-free limit semistability.
- Nodal curves and polarizations with good properties: https://link.springer.com/article/10.1007/s13163-021-00404-z — Canonical polarization on a stable nodal curve is good; line bundles inducing a good polarization are stable.

This audit is independent of the record's pre-existing AUDIT.json. GitHub was read only as evidence; no repository mutation was performed in this audit chat.
