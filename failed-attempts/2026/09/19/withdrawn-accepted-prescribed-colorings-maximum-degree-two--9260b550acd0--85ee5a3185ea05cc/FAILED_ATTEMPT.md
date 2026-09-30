# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/19/prescribed-colorings-maximum-degree-two--9260b550acd0`  
Independent audit date: 2026-09-29 (UTC)  
Task: `2dc78f4140c1ae514bc56394355e0895`

The underlying mathematics was independently checked and is valid, but the record is not acceptable as a distinct validated research finding because its principal theorem was already present in earlier SCOPE repository work.

## Correctness retained

The universal characterization is correct. Necessity follows from sK_3 disjoint union K_m: each color can occur at most once in each triangle and once in K_m, and every size-(s+1) class consumes a distinct K_m vertex. For sufficiency, every maximum-degree-two graph has an independent set S of size ceil(n/3) meeting every cycle: choose one vertex in each cycle component, extend componentwise to an independent set of size at least ceil(n/3), then retain the cycle representatives while trimming to the desired size. Removing S leaves a linear forest. A linear forest embeds in a spanning path, and prescribed multiplicities are realizable on a path exactly when the largest is at most ceil(N/2). The m=1 and m=2 residual bounds match this threshold, while the no-large-class case is covered by Birken's theorem. Edge cases n=1,2 are immediate.

## Decisive prior-art issue

The assigned theorem is already subsumed by earlier SCOPE work. On 2026-09-17, `prescribed-colorings-max-degree-two--9aaf81e2ad5d` proved the strictly stronger graph-by-graph characterization for every Delta<=2 graph: exact feasibility iff each class size is at most alpha(G) and every two class sizes sum to at most n-o(G), and it explicitly derived Birken's r=2 remainder-sensitive conjecture as a corollary. A second 2026-09-17 record, `skewed-hajnal-szemeredi-maximum-degree-two--2b89b837f418`, also already proves the r=2 conjecture. Because those records predate and imply the assigned universal theorem, the assigned finding fails originality.

## Scientific-value consequence

The proof here is valid and somewhat simpler at the universal level, but the scientific claim is weaker than a two-day-earlier repository theorem that already classifies prescribed profiles for each individual maximum-degree-two graph and derives this universal condition. As a separate validated research finding it therefore adds insufficient standalone scientific value.

## Consequence

This package is relocated as a failed research attempt rather than silently deleted. It may remain useful as an alternative exposition or verification example, but its headline must not be represented as an independently original validated finding.

## Prior repository evidence

- `2026/09/17/prescribed-colorings-max-degree-two--9aaf81e2ad5d/RESULT.md` (blob `c2d4e4bd1b4f60d0b85b1dd19e890d324fde9c80`): Strictly stronger exact graph-by-graph feasibility theorem for Delta<=2; explicitly derives Birken r=2 as a corollary.
- `2026/09/17/skewed-hajnal-szemeredi-maximum-degree-two--2b89b837f418/RESULT.md` (blob `6883d47f311973ac2b9cf50e1c75b73d0576981f`): Earlier independent SCOPE proof of Birken Conjecture 5 for r=2, with a stronger bipartite auxiliary theorem.
