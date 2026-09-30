# Independent audit — 2026-09-29

**Record:** `2026/09/18/near-maximum-connected-mutual-visibility--1935030c73b8`
**Disposition:** **FAILED**

## Correctness

**PASS** — For S=V(G)\{x}, mutual visibility of a nonadjacent pair u,v in S forces the unique allowed internal vertex of an S-avoiding geodesic to be x, hence ux,vx are edges; conversely that condition supplies the length-two geodesic u-x-v for every nonedge in S, while G-x connected supplies the connectedness requirement. The complement-star reformulation and the co-connected 2n-4 and (n-2)^2 bounds follow. The stated sharp family was independently checked for small orders.

## Originality

**FAIL** — The primary September 2026 paper already derives the decisive near-maximum condition inside its Nordhaus--Gaddum proof: when a connected mutual-visibility set has size n-1, every nonedge among the retained vertices must have both endpoints adjacent to the omitted vertex. The record turns that already-used condition into an iff by adding the immediate converse and then rewrites it as a star component in the complement. The co-connected improvement is then a direct corollary. This is too close to an explicit argument in the source to support a distinct accepted research claim.

## Scientific value

**FAIL** — Although correct, the result is a short repackaging and immediate specialization of the source paper’s own near-extremal reasoning. The sharpened co-connected Nordhaus--Gaddum bounds and the exhibited equality family do not add enough conceptual or technical content, beyond the newly introduced source theory, to justify a standalone accepted record.

## Independent checks

- Reconstructed both directions of the n-1 characterization directly from the definition of connected mutual visibility.
- Translated the condition to the complement: each complement-neighbor of x has no complement-neighbor except x, so the complement component containing x is a star centered at x.
- Brute-force checked the stated equality construction K_{2,n-3} with one leaf, and its complement, for n=5,6,7,8; both have connected mutual-visibility number n-2.

## Findings

- The graph-theoretic statements themselves are correct.
- The decisive n-1 structural implication is already present in the proof of the source paper’s Nordhaus--Gaddum theorem; the record’s converse is immediate from the definition.
- Because the scientific failure is originality/value rather than correctness, the complete original package should be relocated to the assigned failed-attempt path with a substantive failure notice.

## Literature evidence

- https://arxiv.org/abs/2609.18877 — Tonny K B and Shikhi M, Connected Mutual-Visibility in Graphs. This is the primary source introducing the parameter, proving Nordhaus--Gaddum inequalities and the block theorem. Its Nordhaus--Gaddum proof already contains the decisive implication used by the audited n-1 characterization.

## Limitations

- The failure verdict concerns originality and standalone scientific value, not mathematical correctness.
- The parameter and source paper are extremely recent, so the literature comparison is necessarily concentrated on the directly motivating primary source; that source is already decisive here.

## Publication consequence

The mathematical statements checked here are not rejected for correctness. The record is rejected as an accepted finding because the directly motivating primary source already contains the decisive near-maximum implication and the remaining converse/reformulation/corollaries do not clear the originality and standalone-value threshold. The complete package should be relocated atomically to `failed-attempts/2026/09/18/withdrawn-accepted-near-maximum-connected-mutual-visibility--1935030c73b8--3ce4056057d8d8ca` and retained as a failed attempt.
