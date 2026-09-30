# Independent Audit — Strictly convex bodies admit no exponential Riesz bases

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `68e2f61a858a2e562db78091a304755210b4203d`  
**Audited current source tree:** `68e2f61a858a2e562db78091a304755210b4203d`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used read-only as evidence; this is a guarded publication-plan payload and is not claimed to be already published.

## Correctness — PASSED

PASS. The geometric argument is correct. For a translation te_n, strict convexity makes the lower section endpoint strictly convex, the upper endpoint strictly concave, and the width strictly concave. A common boundary point with its translate must lie over an interior projection point and correspond to a positive width level. That level is null in the (n−1)-dimensional base, and local Lipschitz regularity of the endpoint graph lifts nullity to H^{n−1}. The full-boundary surface measure therefore satisfies Ortega-Cerdà’s translate non-overlap criterion, while the two-sided neighborhood condition follows from interior points and supporting hyperplanes.

## Originality — FAILED

FAIL. The repository already contains `2026/09/18/strict-convexity-riesz-basis-obstruction--f3a7cf0b8ac6`, whose RESULT.md states the same theorem—no exponential Riesz basis on any bounded strictly convex body without boundary regularity—and proves the same boundary-translate lemma by the same vertical-fiber/strict-width-concavity argument before invoking the same Ortega-Cerdà criterion. This is not merely overlapping background: it is the same research claim and proof architecture already represented as a separate SCOPE record. External literature comparison still supports that the theorem itself goes beyond Ortega-Cerdà’s C^2 result, but this assigned record is not an original independent contribution relative to the existing archive.

## Scientific value — FAILED

FAIL AS A SEPARATE VALIDATED RECORD. The theorem is mathematically valuable, but that value is already carried by the existing `strict-convexity-riesz-basis-obstruction--f3a7cf0b8ac6` package. Validating a second near-duplicate package would add no distinct scientific content and would create duplicate repository claims rather than a new result.

## Independent checks

- Reconstructed the translate-intersection proof from section fibers and strict width concavity.
- Checked the level-set nullity and Lipschitz graph lift.
- Compared against Ortega-Cerdà’s current arXiv statement, which reaches bounded convex sets with C^2 boundary rather than arbitrary rough strictly convex bodies.
- Fetched and compared the existing SCOPE record `strict-convexity-riesz-basis-obstruction--f3a7cf0b8ac6`; its theorem, key lemma, and proof mechanism coincide with this assigned record.
- Verified the current main tree equals the assigned tree and that dated independent-audit files are absent.

## Limitations

- The failure is an originality/archive-value determination, not a claim that the theorem or proof is false.
- The two SCOPE records are not byte-identical, but their theorem, key geometric lemma, and proof architecture are substantively the same.
- The audit does not determine which same-day generation occurred first; duplication alone is decisive for validating this package as a distinct finding.

## Evidence and references

- https://arxiv.org/abs/2609.18426
- https://arxiv.org/abs/2609.16674
- https://github.com/SCOPE-Science/SCOPE2026/blob/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/strict-convexity-riesz-basis-obstruction--f3a7cf0b8ac6/RESULT.md
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/strictly-convex-no-exponential-riesz-basis--e64ec22ab4da

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
