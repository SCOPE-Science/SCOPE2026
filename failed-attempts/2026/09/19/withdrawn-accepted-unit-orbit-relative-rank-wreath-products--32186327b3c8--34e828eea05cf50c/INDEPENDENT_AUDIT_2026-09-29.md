# Independent Audit — Unit orbits determine relative rank in finite transformation wreath products

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `0e551ac1dfc6dda7d0c2d92cb41760acf9a862e5`  
**Audited current source tree:** `0e551ac1dfc6dda7d0c2d92cb41760acf9a862e5`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree equals the assigned source tree. GitHub was used only as read-only evidence. The UTC-dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. The relative-rank proof is correct. In a finite monoid, a product is a unit only if each factor is a unit; therefore a word ending with unit top coordinate cannot use a generator with nonunit top coordinate. For unit-top factors the singular support in the base evolves by transported unions and cannot cancel. To generate a singleton defect at x, one therefore needs singleton-support relative generators in the G-orbit of x, and their coordinate values must generate S modulo H. This forces c generators per G-orbit in addition to rank(R:G) top generators. The converse construction localizes c generators at one representative of each G-orbit and transports them with units, proving the exact formula and the iterated orbit-weighted version. This is the same valid mathematics as the earlier archive record.

## Originality — FAILED

FAIL. The record substantively duplicates the earlier SCOPE record `2026/09/18/unit-orbits-control-wreath-product-relative-rank--1d4bcdcec1ba`. That earlier package already states and proves the identical formula rank(S wr_X R : H wr_X G)=rank(R:G)+(# G-orbits on X) rank(S:H), the ordinary-rank corollary, the orbit-weighted iterated formula, the identification of unit-group rather than whole-monoid transitivity, and explicit counterexamples correcting Lu's Lemmas 3.2 and 3.8. The assigned record was published on 2026-09-19T15:29:47Z, after the earlier 2026-09-18 archive entry. Differences in the small counterexample and notation do not create a distinct research claim.

## Scientific value — FAILED

FAIL AS A DISTINCT ARCHIVE FINDING. The theorem is mathematically useful, but all substantive scientific coverage is already provided by the earlier SCOPE record, including the general and iterated formulas and the correction to the same source paper. Retaining this later record as separately validated research would add duplicate coverage rather than new value.

## Independent checks

- Reconstructed the lower and upper relative-rank arguments independently and found the mathematics sound.
- Fetched and compared the earlier SCOPE record `2026/09/18/unit-orbits-control-wreath-product-relative-rank--1d4bcdcec1ba` in full; its headline formula, proof mechanism, iterated theorem and source correction are the same.
- Verified the earlier record's metadata places it in the 2026-09-18 archive, while the assigned record metadata gives 2026-09-19T15:29:47Z.
- Compared against Lu arXiv:2609.20521 and older partition/wreath-product rank literature; the failure is internal archive duplication, not a mathematical error.
- Verified via GitHub compare that the assigned record path did not change from the dispatcher source-check commit to current main; the dated audit pair and FAILED_ATTEMPT.md are absent and VERIFICATION.md is unchanged.
- Verified the designated failed-attempt destination is vacant on current main (GitHub returned 404).

## Limitations

- The failure is an originality/scientific-value determination only; the theorem and proof are correct.
- The complete assigned package should be retained at the designated failed-attempt location for provenance.
- No claim is made that Lu's specialized main theorem for full transformation/symmetric-group factors is invalid; both SCOPE records explain why that specialization survives.

## Evidence and references

- https://arxiv.org/abs/2609.20521
- https://arxiv.org/abs/0807.1214
- https://doi.org/10.1007/s00233-023-10340-7
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/unit-orbits-control-wreath-product-relative-rank--1d4bcdcec1ba
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/unit-orbit-relative-rank-wreath-products--32186327b3c8

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
