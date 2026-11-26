# Independent mathematical audit

## correctness

PASS

The circular-gap layers partition the pairs. In each ordinary layer the potential values are (k−1)n+1 through kn; the even diametrical top layer has h instead of n entries. Letter a reduces the potential by one except at the layer heads, where the start index wraps. Letter b is the identity off pairs containing n−1. On {r,n−1} it reduces the potential by one for r=0 through h−1 (the first case merges); for the remaining r it raises it by n, except at the odd midpoint r=h where it raises it by h. Thus exactly one letter reduces the potential by one, neither can reduce it faster, and all minimal words follow the forced path down through the layers. This proves the formula, the suffix labels and both master words, including n=2 (the unique word is b). Fresh time-layer tabulation of all states and shortest word multiplicities at n=2..25 in /workspace/reproductions/34_pairs_and_rings.py agreed exactly. Frozen VERIFICATION.md and verify.py were inspected, not run.

## originality

FAIL

The weighted indexed theorem 261334d3d0c0 already gives the same pair labels, unique optimal paths and common suffix structure by setting both costs to one, and the displayed master word is the block form of its forced policy. The sole additional n=2 case is a direct one-step merge. A distinct indexed result fe81919abba1 gives even the exact master expression over all n≥2. No bibliographic priority or dependence is inferred from the catalogue path dates; the mathematical coverage is explicit.

## value

FAIL

A canonical pair geodesic and exact label can be useful, but those are already supplied by the exact force-letter classification and its weighted extension. The remaining simpler notation for U_n is a direct block expansion of the known policy, and n=2 is one merging letter. Neither is an independently useful new invariant or classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
