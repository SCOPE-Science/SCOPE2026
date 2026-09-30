# FAILED ATTEMPT — NOT A VALIDATED FINDING

**Record:** `2026/09/18/strictly-convex-no-exponential-riesz-basis--e64ec22ab4da`  
**Independent audit date:** 2026-09-29 (UTC)  
**Task:** `04ce824cc366c919805f0d39532afdea`

This package is preserved for provenance, but the independent audit does **not** validate it as a distinct publishable research finding.

## Correctness retained

PASS. The geometric argument is correct. For a translation te_n, strict convexity makes the lower section endpoint strictly convex, the upper endpoint strictly concave, and the width strictly concave. A common boundary point with its translate must lie over an interior projection point and correspond to a positive width level. That level is null in the (n−1)-dimensional base, and local Lipschitz regularity of the endpoint graph lifts nullity to H^{n−1}. The full-boundary surface measure therefore satisfies Ortega-Cerdà’s translate non-overlap criterion, while the two-sided neighborhood condition follows from interior points and supporting hyperplanes.

## Decisive originality finding

FAIL. The repository already contains `2026/09/18/strict-convexity-riesz-basis-obstruction--f3a7cf0b8ac6`, whose RESULT.md states the same theorem—no exponential Riesz basis on any bounded strictly convex body without boundary regularity—and proves the same boundary-translate lemma by the same vertical-fiber/strict-width-concavity argument before invoking the same Ortega-Cerdà criterion. This is not merely overlapping background: it is the same research claim and proof architecture already represented as a separate SCOPE record. External literature comparison still supports that the theorem itself goes beyond Ortega-Cerdà’s C^2 result, but this assigned record is not an original independent contribution relative to the existing archive.

## Scientific-value finding

FAIL AS A SEPARATE VALIDATED RECORD. The theorem is mathematically valuable, but that value is already carried by the existing `strict-convexity-riesz-basis-obstruction--f3a7cf0b8ac6` package. Validating a second near-duplicate package would add no distinct scientific content and would create duplicate repository claims rather than a new result.

## Preservation note

The complete original package should be relocated atomically to the assigned failed-attempt destination. No original evidence file should be selectively deleted. A future submission must contain substantively distinct research content and be audited as a new record.
