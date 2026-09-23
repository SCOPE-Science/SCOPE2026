# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/08/001`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `fdd4b130865cef8a0dd85a8b6203be2a9bc026b1`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

A four-class isomorphism census of clean degree-8 dessins with black passport 2^4 and white passport 3^2 2^1, including face types, automorphism orders and a Belyi witness.

## Correctness — PASSED

An independent S8/centralizer enumeration reproduced exactly four transitive classes with orbit sizes 192,384,192,192, face types (6,1,1), (5,2,1), (3,3,2), (8), and automorphism-group orders 2,1,2,2. The Belyi identity supplied for the (6,1,1) class is also algebraically consistent. The record's finite computation is correct.

## Originality — FAILED

Adrianov, Amburg, Dremov, Mendeleev, Nasretdinova and Shabat, *Catalog of dessins d'enfants with no more than 4 edges* (arXiv:0710.2658; J. Math. Sci. 158 (2009), DOI 10.1007/s10958-009-9373-7), is an exhaustive catalog of all dessins with at most four edges, with Belyi pairs and automorphism-group orders. The degree-8 clean passport here corresponds to four-edge clean dessins, and the catalog already lists the four relevant passport/face classes and their automorphism orders. The record's claim that this low-degree fixed-passport table was missing is therefore false.

## Scientific value — FAILED

After the pre-existing four-edge catalog is taken into account, the record mainly re-enumerates a tiny already-tabulated passport and supplies one of the kinds of Belyi witnesses the catalog already provides. This does not leave a substantial new classification, algorithm or regime satisfying the campaign's value threshold.

## Search and independent checks

Independent checks:

- independent S8 transitivity/centralizer orbit census
- independent automorphism-order and face-type checks
- full-text comparison with arXiv:0710.2658 and its four-edge catalog entries

Literature/search queries:
- `dessins four edges catalog 3 3 2 passport 8`
- `clean dessin degree 8 passport 2^4 3^2 2`
- `Adrianov Shabat catalog dessins no more than 4 edges`

Sources:
- https://arxiv.org/abs/0710.2658
- https://doi.org/10.1007/s10958-009-9373-7

## Repair / salvage attempt

No bounded repair yields a new classification: the exact four classes and automorphism data are already catalogued. A genuinely new invariant or theorem would be separate research.

## Final disposition

**FAILED.** The record is withdrawn from the accepted findings tree because at least one of originality or scientific value fails after decisive prior-art comparison.
