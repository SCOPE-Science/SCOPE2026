# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Linear 3/2 chi bound for even-hole-free long-prism-free graphs
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1499
- **Disposition:** NO_RESULT
- **Domain:** hereditary graph coloring
- **Method:** decomposition plus chi-boundedness

## Problem

Let G be a finite simple graph with no induced even hole (no induced cycle of even length at least 4) and no induced long prism, where a long prism means two vertex-disjoint triangles {a1,a2,a3} and {b1,b2,b3} together with three pairwise vertex-disjoint paths Pi joining ai to bi, each Pi of length at least 3 edges, with no edges between distinct paths except the triangle edges. Let chi(G) denote chromatic number and omega(G) clique number. Prove or disprove that every such G satisfies chi(G) <= max{3, ceil(3*omega(G)/2)}. A complete answer is either a proof of this inequality for all such G or an explicit graph G0 with verification that G0 contains no induced even hole and no such induced long prism and satisfies chi(G0) > max{3, ceil(3*omega(G0)/2)} with certified clique and chromatic numbers.

## Attempted claim

Let G be a finite simple graph with no induced even hole (no induced cycle of even length at least 4) and no induced long prism, where a long prism means two vertex-disjoint triangles {a1,a2,a3} and {b1,b2,b3} together with three pairwise vertex-disjoint paths Pi joining ai to bi, each Pi of length at least 3 edges, with no edges between distinct paths except the triangle edges. Let chi(G) denote chromatic number and omega(G) clique number. Prove or disprove that every such G satisfies chi(G) <= max{3, ceil(3*omega(G)/2)}. A complete answer is either a proof of this inequality for all such G or an explicit graph G0 with verification that G0 contains no induced even hole and no such induced long prism and satisfies chi(G0) > max{3, ceil(3*omega(G0)/2)} with certified clique and chromatic numbers.

## Research outcome

Target neither proved nor disproved: bisimplicial induction failed, long-prism hypothesis shown redundant via parity, and a certified exact search (structured families plus 400 even-hole-free random graphs) found zero violations but is too narrow to settle the bound; honest clean exit with matching target_exit.json.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

Exact certification (subset/chordless-cycle even-hole tests, DSATUR chromatic numbers, clique branch-and-bound) reaches only n<=16, so the negative search over blowups, joins, wheels, 400 random even-hole-free graphs, and famous graphs cannot certify the universal bound; the bisimplicial induction proof attempt collapsed and the prism-redundancy parity observation was left as a worklog remark rather than a claimed result.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: Exact certification (subset/chordless-cycle even-hole tests, DSATUR chromatic numbers, clique branch-and-bound) reaches only n<=16, so the negative search over blowups, joins, wheels, 400 random even-hole-free graphs, and famous graphs cannot certify the universal bound; the bisimplicial induction proof attempt collapsed and the prism-redundancy parity observation was left as a worklog remark rather than a claimed result.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
