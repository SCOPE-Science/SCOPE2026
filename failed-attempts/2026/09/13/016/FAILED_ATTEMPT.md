# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Polynomial chi-boundedness with C4 allowed and long prisms banned
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1504
- **Disposition:** NO_RESULT
- **Domain:** hereditary graph coloring
- **Method:** parity-changing paths and chi-boundedness

## Problem

Let G be a finite simple graph with no induced even hole of length at least 6 (the 4-cycle C4 is allowed) and no induced long prism, where a long prism means two vertex-disjoint triangles joined by three pairwise vertex-disjoint paths each of length at least 3 edges, with no edges between distinct paths except the triangle edges. Let chi(G) and omega(G) be chromatic and clique numbers. Prove or disprove that there exist absolute constants C and d such that chi(G) <= C*omega(G)^d for every such G. A complete answer is either a proof of such a polynomial bound with explicit C and d for all G in this class or an explicit infinite family {Gk} in this class with verified membership and with chi(Gk)/omega(Gk)^d unbounded for every fixed d.

## Attempted claim

Let G be a finite simple graph with no induced even hole of length at least 6 (the 4-cycle C4 is allowed) and no induced long prism, where a long prism means two vertex-disjoint triangles joined by three pairwise vertex-disjoint paths each of length at least 3 edges, with no edges between distinct paths except the triangle edges. Let chi(G) and omega(G) be chromatic and clique numbers. Prove or disprove that there exist absolute constants C and d such that chi(G) <= C*omega(G)^d for every such G. A complete answer is either a proof of such a polynomial bound with explicit C and d for all G in this class or an explicit infinite family {Gk} in this class with verified membership and with chi(Gk)/omega(Gk)^d unbounded for every fixed d.

## Research outcome

Target blocked on both horns: every classical triangle-free high-chi candidate was proved by exact search to contain an induced even hole >=6, the decision-phase Burling recovery test failed (wrong chi profile), and no proof skeleton with explicit constants exists; clean exit with NO_RESULT.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No proof of a polynomial chi-bound with explicit constants was obtained, and no infinite counterexample family was constructed; the polynomial chi-boundedness question for graphs with no induced even hole of length at least 6 remains fully open. Computational screens covered only small members of classical families (Mycielski to M5, shift graphs to S_9, small Kneser/sporadic graphs, an unverified Burling implementation) and cannot rule out an exotic hole-free high-chi family. The long-prism redundancy lemma is proved but is only a hypothesis simplification, not progress toward the bound itself.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No proof of a polynomial chi-bound with explicit constants was obtained, and no infinite counterexample family was constructed; the polynomial chi-boundedness question for graphs with no induced even hole of length at least 6 remains fully open. Computational screens covered only small members of classical families (Mycielski to M5, shift graphs to S_9, small Kneser/sporadic graphs, an unverified Burling implementation) and cannot rule out an exotic hole-free high-chi family. The long-prism red…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
