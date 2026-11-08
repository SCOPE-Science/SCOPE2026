# Review: sharp universal temporal-order boundary

## Correctness — PASS

The construction applies for every integer nesting depth \(i\ge3\), not just the checked samples. For any \(q\in[\nu_i,1)\), the explicitly listed points in the initial history are distinct, permitting disjoint slope-setting neighborhoods with unchanged values. The resulting history is exactly \(2\)-Lipschitz and uniformly small; with \(\eta=q/2\), \(c=1\), and zero forcing, the global reference trajectory satisfies \(|g|\le1+\|\varphi\|_\infty\), so all strict hypotheses of the cited invisibility theorem hold. Differentiating the affine nesting steps gives \(d_i'=1-\sum_{k=1}^{i-1}q^k\) on a genuine interval, establishing flatness at equality and reversal above it. The universal positive direction for \(q<\nu_i\) is the cited Theorem 5.1, not a new result. The exact-rational checker passed 345 representative checks; the all-order proof is analytic.

## Originality — PASS within inspected evidence

The relevant source, Bolduc-St-Aubin, Subramanian and Krauskopf (arXiv:2610.39281v1), supplies \(\nu_i\) as a sufficient TOR boundary, notes the condition is only sufficient, and illustrates TOR failure at one much larger parameter. It does **not** assert exact universal optimality for each depth or a plateau at equality. A distinct clipped-history calculation at the contraction boundary \(q=1\) addresses failure of dynamic invisibility; the present examples remain strictly below \(q=1\) and keep all trajectories identical. Walther's 2009 algebraic-delay study concerns implicit temporal ordering; its abstract gives no finite-depth universal \(\nu_i\) theorem, but the full text could not be inspected. Search absence is not a proof of novelty.

## Mathematical value — PASS

The motivating study distinguishes invisible changes in delayed arguments from actual loss of temporal-order preservation, and leaves the sharpness of its proposed finite-depth thresholds unresolved. The finding settles that exact naturally arising threshold simultaneously for every nesting depth, including the boundary behavior, within the stated model class. It also rigorously separates failure of reaction ordering from a failure of the trajectory-invisibility theorem. The construction is structural rather than a small numerical improvement.

## Sources and limitations

Primary source inspected in HTML: arXiv:2610.39281v1, especially Theorems 1.1 and 5.1, Lemma 3.1, Proposition 5.2, Figure 2 discussion and proof of the invisibility theorem. Related source: H.-O. Walther, J. Dynam. Differential Equations 21 (2009), DOI:10.1007/s10884-009-9129-6; abstract inspected, full text unavailable. The theorem is about universal strict temporal ordering of finite nested delays under the documented contraction and amplitude hypotheses, not smooth-feedback dynamics or ordering for every individual above-threshold history. Independent scientific validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
