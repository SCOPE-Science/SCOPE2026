# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Facet census of stable-set polytopes for connected non-perfect graphs on at most 7 vertices with maximal integrality-gap witness
- **Round:** 2026-09-07-first-light-01
- **Lane:** 312
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Polyhedral Optimization
- **Method:** double-description facet enumeration with clique and odd-cycle separation and integer-vertex tightness replay

## Problem

Produce a replayable facet census of stable-set polytopes STAB(G) over all connected non-isomorphic non-perfect graphs G with n<=7 vertices: for each G, the complete irredundant facet list obtained by double-description from the enumerated stable-set vertices, classification of each facet (nonnegativity/clique/odd-hole/other), fractional-versus-integral vertex table with Chvatal-rank residuals, and identification of the maximal integrality-gap extremal graph with certificate.

## Attempted claim

For every connected non-isomorphic non-perfect graph G with n<=7, STAB(G) has the explicitly tabulated complete irredundant facet description obtained by double-description from its stable-set vertices, and the maximal fractional-versus-integral gap over the slice is attained at an explicit extremal graph G* with stated gap value, fractional vertex, and separating odd-hole inequality.

## Research outcome

Certified complete irredundant facet description of STAB(C5) (5 nonnegativity + 5 edge + 1 odd-hole facets) with exact-rational tight-vertex, irredundancy, and vertex-completeness replay plus fractional-vs-integral gap witness (5/2 vs 2). All scripts rerun cleanly printing VERIFY_OK.

## Why this attempt failed

Failed axes: originality, value.

originality: The mathematical content of the headline is classical and admitted as such in DRAFT.md line 39-41. The H-description of STAB(C5) as 5 nonnegativity + 5 edge/clique + sum<=2 odd-hole facet, and the fractional value 5/2 at (1/2)^5 vs alpha=2 (gap 1/2), is the textbook odd-hole example originating in Chvatal (1975) 'On certain polytopes associated with graphs' and Padberg (1973) 'On the facial structure of set packing polyhedra', reproduced in every integer-programming textbook (e.g. Nemhauser-Wolsey, Schrijver, Grotschel-Lovasz-Schrijver). Nearest prior results substantively contain the claim: Chvatal 1975 introduces odd-hole inequalities including C5; Padberg 1973 gives clique/odd-hole facet conditions; Strong Perfect Graph Theorem work gives the integrality boundary. The only delta is a stdlib exact-rational replay script (tight-vertex logs, witness points, vertex tables) for this single 5-vertex instance. That is a mechanical re-derivation, not a new theorem, classification, residual, extremal-maximality proof, or method. The draft disclaims the originally-admitted novel scope (full n<=7 census, Chvatal-rank residuals, maximal-gap table over slice) and proves no maximality of C5 over any slice. A timestamp or fresh script does not establish priority over a 50-year-old textbook fact. value: Textbook restatement even if correctly re-certified. Under the exact-invariant clause, a narrow datum is independently valuable only when motivated before computation, not known or mechanically implied, and reasonably needed later as a precise fact. Here all three fail: the C5 facet list and 5/2-vs-2 gap were known since the 1970s, are mechanically implied by standard odd-hole/clique theory, and are already retrievable from textbooks and surveys. The certificate bundle (tight indices, witness coordinates, JSON vertex lists) is verification packaging, which per standard does not rescue an otherwise known number: 'certification alone does not rescue an arbitrary object or an unexplained number,' and a fortiori does not rescue a textbook fact. No new benchmark need is demonstrated: C5 as a cut example is already the canonical benchmark. No downstream theorem, hierarchy separation, or classification uses the bundle beyond what the textbook statement provides. Hence independently worth finding later = no.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Fallback-scope result only: single extremal C5, not the full connected non-perfect n<=7 census in the topic target. C5 odd-hole inequality is classical; novelty is the replayable certificate bundle, not the inequality. No cddlib double-description binary used; completeness proved by exact basic-point enumeration (C(11,5) systems), equivalent at this scale.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
