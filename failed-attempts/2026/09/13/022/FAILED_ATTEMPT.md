# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Quadratic balanced separators for even-hole-free long-prism-free graphs
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1505
- **Disposition:** NO_RESULT
- **Domain:** structural graph theory
- **Method:** treewidth and separator decomposition

## Problem

Let G be a finite simple n-vertex graph with no induced even hole (no induced cycle of even length at least 4) and no induced long prism, where a long prism means two vertex-disjoint triangles joined by three pairwise vertex-disjoint paths each of length at least 3 edges, with no edges between distinct paths except the triangle edges. A balanced separator is a vertex set S such that every connected component of G minus S has at most 2n/3 vertices. Let omega(G) be clique number. Prove or disprove that there exists an absolute constant C such that every such G has a balanced separator S with |S| <= C*omega(G)^2. A complete answer is either a proof of this separator bound for all such G or an explicit infinite family of graphs in this class with verified membership for which every balanced separator has size super-quadratic in omega, with separator lower-bound verification.

## Attempted claim

Let G be a finite simple n-vertex graph with no induced even hole (no induced cycle of even length at least 4) and no induced long prism, where a long prism means two vertex-disjoint triangles joined by three pairwise vertex-disjoint paths each of length at least 3 edges, with no edges between distinct paths except the triangle edges. A balanced separator is a vertex set S such that every connected component of G minus S has at most 2n/3 vertices. Let omega(G) be clique number. Prove or disprove that there exists an absolute constant C such that every such G has a balanced separator S with |S| <= C*omega(G)^2. A complete answer is either a proof of this separator bound for all such G or an explicit infinite family of graphs in this class with verified membership for which every balanced separator has size super-quadratic in omega, with separator lower-bound verification.

## Research outcome

No verified resolution: the layered-wheel disproof route failed at the balanced-separator lower bound (treewidth growth with omega=3 is consistent with O(1) separators given tw=O(log n)), and the proof route via known dominated-separator machinery stops at O(log n)+omega bounds, not C*omega^2. Honest clean exit with verification artifacts retained.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof or disproof of the quadratic separator bound was established. The ehf-layered-wheel separator-growth recurrence is an unverified plausibility bound, not a lemma, and may be false. The prism-implies-even-hole verification reproduces known literature (Sintiari-Trotignon). Literature survey relied on OpenAlex metadata plus two arXiv PDFs (1906.10998, 2402.14211); no new theorems are claimed.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof or disproof of the quadratic separator bound was established. The ehf-layered-wheel separator-growth recurrence is an unverified plausibility bound, not a lemma, and may be false. The prism-implies-even-hole verification reproduces known literature (Sintiari-Trotignon). Literature survey relied on OpenAlex metadata plus two arXiv PDFs (1906.10998, 2402.14211); no new theorems are claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
