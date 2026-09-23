# Independent audit — 2026-09-22 campaign

**Source path:** `2026/09/08/004`  
**Audited repository state:** `253a0fe5d0217455660a277f9adb940030e567ad`  
**RESULT.md blob:** `82d3a092da0c075755f71b8e8e79492d23d8c761`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean verification or expert attestation is claimed.

## Claim audited

The formula reg(S/I(L_n)) = ceil(n/2) = nu(L_n) for open ladder graphs L_n, with a deletion-recursion proof and pendant auxiliary family.

## Correctness — PASSED

The proof strategy and formula are sound. Independent finite Hochster checks reproduced the small-n bases, the induced matching number is ceil(n/2), and the stated vertex-deletion recursion closes the induction. No mathematical error in the formula itself was found.

## Originality — FAILED

The formula is already published. Rohit Verma, Communications in Algebra 50 (2022), DOI 10.1080/00927872.2021.2006206, proves in Theorem 4.6 that the regularity of the ladder graph L_n is ceil(n/2), and Lemma 4.4 gives the same induced-matching formula. The decisive theorem pages were read in full text during the prior audit via authorized institutional access after ordinary OA/arXiv routes failed. Thus RESULT.md's context saying the ladder formula was open is false and the main theorem is not original.

## Scientific value — FAILED

Once Verma's exact theorem and induced-matching computation are acknowledged, the record contributes an alternative elementary proof plus small computational base checks of an already-solved formula. That does not constitute a sufficiently substantial new theorem, algorithmic improvement or regime under this campaign's value criterion.

## Search and independent checks

Independent checks:

- independent verification of the induced-matching formula and deletion recurrences
- independent small-n Hochster/base checks
- full-text comparison with Verma 2022, Theorem 4.6 and Lemma 4.4

Literature/search queries:
- `ladder graph edge ideal regularity ceil n/2`
- `Rohit Verma ladder regularity induced matching`
- `regularity ladder graph L_n Communications in Algebra`

Sources:
- https://doi.org/10.1080/00927872.2021.2006206

## Repair / salvage attempt

A citation/context correction would leave the main theorem wholly known. The remaining alternative proof and finite checks do not rescue originality/value, so no bounded repair yields an accepted finding.

## Final disposition

**FAILED.** The record is withdrawn from the accepted findings tree because at least one of originality or scientific value fails after decisive prior-art comparison.
