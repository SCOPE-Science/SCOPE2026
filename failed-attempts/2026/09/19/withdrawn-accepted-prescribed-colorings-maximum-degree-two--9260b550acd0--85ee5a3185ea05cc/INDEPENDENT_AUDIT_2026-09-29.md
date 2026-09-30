# Independent audit — Exact prescribed-coloring feasibility at maximum degree two

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/prescribed-colorings-maximum-degree-two--9260b550acd0`  
**Audited tree:** `d091e85f1ae31012099b96c2a1cc35a4eafdd861`

## Disposition

**FAILED.** The mathematics is correct, but originality and standalone scientific value fail because decisive earlier repository coverage already contains the result. The record should be relocated to its assigned failed-attempt path.

## Correctness

**PASS.** The universal characterization is correct. Necessity follows from sK_3 disjoint union K_m: each color can occur at most once in each triangle and once in K_m, and every size-(s+1) class consumes a distinct K_m vertex. For sufficiency, every maximum-degree-two graph has an independent set S of size ceil(n/3) meeting every cycle: choose one vertex in each cycle component, extend componentwise to an independent set of size at least ceil(n/3), then retain the cycle representatives while trimming to the desired size. Removing S leaves a linear forest. A linear forest embeds in a spanning path, and prescribed multiplicities are realizable on a path exactly when the largest is at most ceil(N/2). The m=1 and m=2 residual bounds match this threshold, while the no-large-class case is covered by Birken's theorem. Edge cases n=1,2 are immediate.

## Originality

**FAIL.** The assigned theorem is already subsumed by earlier SCOPE work. On 2026-09-17, `prescribed-colorings-max-degree-two--9aaf81e2ad5d` proved the strictly stronger graph-by-graph characterization for every Delta<=2 graph: exact feasibility iff each class size is at most alpha(G) and every two class sizes sum to at most n-o(G), and it explicitly derived Birken's r=2 remainder-sensitive conjecture as a corollary. A second 2026-09-17 record, `skewed-hajnal-szemeredi-maximum-degree-two--2b89b837f418`, also already proves the r=2 conjecture. Because those records predate and imply the assigned universal theorem, the assigned finding fails originality.

## Scientific value

**FAIL.** The proof here is valid and somewhat simpler at the universal level, but the scientific claim is weaker than a two-day-earlier repository theorem that already classifies prescribed profiles for each individual maximum-degree-two graph and derives this universal condition. As a separate validated research finding it therefore adds insufficient standalone scientific value.

## Independent checks

- Verified the independent cycle-hitting set construction component by component.
- Checked the sharp multiset no-equal-adjacencies criterion used for the linear-forest remainder.
- Checked the sK_3 disjoint union K_m necessity argument and small n edge cases.
- Compared against both 2026-09-17 SCOPE records; the first contains a strictly stronger per-graph theorem and explicitly derives the same r=2 universal corollary.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.18629 — Mathis Birken, A Hajnal–Szemerédi Theorem for Skewed Colorings; proves the floor-bound prescribed-coloring theorem and states the remainder-sensitive extension as future conjectural direction.
- https://arxiv.org/abs/2603.08259 — Kuchukova–Perkins–Povill, Sampling Colorings with Fixed Color Class Sizes; background for the prescribed-coloring setting.
- Repository prior art: `2026/09/17/prescribed-colorings-max-degree-two--9aaf81e2ad5d/RESULT.md` (blob `c2d4e4bd1b4f60d0b85b1dd19e890d324fde9c80`) — Strictly stronger exact graph-by-graph feasibility theorem for Delta<=2; explicitly derives Birken r=2 as a corollary.
- Repository prior art: `2026/09/17/skewed-hajnal-szemeredi-maximum-degree-two--2b89b837f418/RESULT.md` (blob `6883d47f311973ac2b9cf50e1c75b73d0576981f`) — Earlier independent SCOPE proof of Birken Conjecture 5 for r=2, with a stronger bipartite auxiliary theorem.

## Limitations

- The failure concerns originality and standalone value, not correctness.
- The assigned proof may still be useful pedagogically as a short universal-feasibility argument, but it should not occupy the validated research inventory as a new theorem.

## Repository identity

The assigned source-tree SHA `d091e85f1ae31012099b96c2a1cc35a4eafdd861` matched the current tree at the audited path after comparison at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`, source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`, and current `main`. GitHub was read only during this audit.
