# Review of split-graph two-token maximum cuts

## Correctness: PASS
The four possible token-edge classes are counted exactly and exhaust the graph. The displayed mixed-versus-pure cut realizes \(rn(n+r-2)\). Three explicit families of triangles are assigned nonnegative rational weights for every \(n\ge r-1\), including the \((r,n)=(2,1)\) boundary case. Their exact edge loads prove that at least all \(AA\) and \(BB\) edges must remain uncut. The strict slack of \(AB\) edges when \(n\ge r\) forces the unique optimal partition. A parity-lift identity proves the boundary multiplicity and strict subthreshold failure. Finite exhaustive comparisons corroborate these arguments, but are not substituted for them.

## Originality: PASS, with priority risk
The motivating 2026-11-04 token-graph study concerns a different token model and different structural and metric invariants. The closely related 2026-11-18 maximum-cut preprint develops parity-lift and projection inequalities. Together they imply the value formula when \(n\ge r\), so the formula in that interior range is already mathematically covered as a corollary. However, at \(n=r-1\), the projection upper bound is greater than the asserted sharp cut by \(r-1\); the boundary equality certificate, above-boundary uniqueness, and transition to strictly larger cuts below the boundary are not implied as stated. The preprint postdates the earlier motivating paper. Focused literature searches and a comparison with nearby published mathematical findings found no equivalent statement or strictly stronger theorem implying the full claim. This is evidence against coverage, not proof of priority; older unnamed special-family results might exist.

## Value: PASS
The maximum cut is a natural graph-frustration and token-configuration invariant. An explicit weighted fractional triangle packing closes the nontrivial remaining gap at the sharp parameter boundary (a gap not resolved by the later generic upper bound), while strict capacity slack classifies the unique optimizer above the boundary. The threshold's two distinct equality regimes are not numerical coincidence and remain relevant to further token-graph cut questions.

## Scope and limitations
No exact subthreshold values or complete boundary optimizer count are claimed. Only unweighted two-token graphs of complete split parent graphs are covered. No independent mathematical verification has been performed.

Self-review: passed. Independent audit: not yet performed.
