# Independent scientific audit — SCOPE-20260915-003

Audited at: 2026-10-01T04:13:22.005211Z

Disposition: **failed**

## Correctness — FAIL

The full final claim is not established. First, Bönicke's twist-homotopy theorem used for the evaluation step is an ample-groupoid theorem, while stable and unstable Ruelle groupoids of a general irreducible Smale space need not be ample; the record assumes an applicability bridge that is not proved. Second, the asserted uniform theta-summability under a merely continuous compatible twist family requires uniform holonomy-Lipschitz control that is neither a hypothesis nor derived; the committed numerical script explicitly models such a bound rather than proving it. Third, the claimed identification of the Proietti-Yamashita spectral-sequence page with twisted Putnam homology using Fell-line coefficients is asserted without a cited theorem or a complete chain-level construction.

## Originality — FAIL

The portion that is justified abstractly—transporting an existing KK-duality pair along actual KK-equivalences—is formal category theory and mechanically follows once such equivalences are available. The stronger summability and twisted-homology additions are not validated mathematics, so they cannot supply originality for the final claim.

### Equivalent formulations

The abstract duality-transport component is equivalent to standard transport of a dual pair through KK-equivalences; the extra components remain unsupported.

### Broader coverage

No single broader theorem covers the record's full claim, but the correctly justified abstract core is already formal from prior work.

### Exact database or table

The absence of an exact match does not cure the correctness gaps.

### Claim versus prior implication

The valid core is mechanically implied; the nontrivial strengthened parts require additional hypotheses or proofs not present in the package.

## Value — FAIL

A genuinely proved twisted summability or twisted Putnam-homology extension would be worthwhile, but this package does not establish those statements. The surviving formal transport of a duality pair along assumed KK-equivalences is too routine by itself to validate the published combined claim.

## Sources inspected

- K-theoretic duality for hyperbolic dynamical systems — https://arxiv.org/abs/1009.4999. COVERING_INGREDIENT: Supplies the untwisted duality classes but no twist-family extension.
- K-theory and homotopies of twists on ample groupoids — https://arxiv.org/abs/1901.09441. INSUFFICIENT_FOR_GENERAL_CLAIM: The theorem is not stated for arbitrary non-ample Ruelle groupoids.
- Spectral triples and finite summability on Smale spaces — https://arxiv.org/abs/2205.13395. NOT_COVERING_TWIST_UNIFORMITY: Does not prove that arbitrary continuous compatible twist homotopies preserve the required uniform Lipschitz estimates.
- Groupoid homology and K-theory for Smale spaces — https://arxiv.org/abs/2207.03118. NOT_COVERING_TWISTED_PAGE: No inspected theorem supplies the asserted Fell-line local-coefficient version.

## Residual risks

- A narrower theorem for zero-dimensional Smale spaces or for twist families with explicit uniform Lipschitz control may be repairable, but such a narrowed claim was not proved here.
- The repository's summability script explicitly describes itself as a one-dimensional model and cannot certify the analytic theorem.
- The original artifact inventory uses obsolete output/artifacts paths; actual inspected files are under artifacts.

## Limitations

- Scientific failure is due to unresolved hypotheses/proofs in the published final claim, not a transport or access error.
- No corrected narrowed theorem is asserted in this audit.
- The original package is to be preserved intact in the designated failed-attempt archive together with the audit evidence.
