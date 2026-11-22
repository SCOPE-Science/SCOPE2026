# Review of the complement-cycle identifying-code polynomial

## Correctness — PASS

The statement fixes the ordinary closed-neighborhood identifying-code convention and all labelled cycle lengths \(n\ge5\). The key bijection sends every code to a selected set in the distance-two auxiliary two-regular graph: identifying traces are distinct exactly when chosen vertices have no isolated vertex in the selected subgraph and the omitted subgraph has at most one edge. Pairwise distinctness also forces at least three chosen vertices, making nonempty traces automatic. The proof converts that characterization into zero-run restrictions and uses marked cyclic gaps to count the zero-defect and one-defect cases without rotational quotienting. It explicitly handles the even/odd component split. Two ordinary generating identities yield the asymptotic by simple-pole analysis. An independent closed-neighborhood exhaustive check for all sets at orders 5–16 agreed with a separate transfer model and the binomial expressions, and the transfer determinant factorization was verified in exact symbolic algebra. The finite tests are corroboration, not the infinite proof.

## Originality — PASS, provisional

The minimum identifying-code number of cycle complements was studied by Nikandish, Khani Nasab and Dodonge (2020), while Gravier, Moncel and Semri (2006) gave an equivalent odd-cycle radius-code minimum case. These scalar extremal facts do not specify the number of codes at every size. A directly relevant already published ordinary-cycle open locating-dominating polynomial gives the zero-defect term \(A\); it does not include codes with exactly one auxiliary unchosen edge, which are counted by \(B\) and dominate asymptotically. The existing published crown-graph and corona code polynomials concern structurally different graphs. Full-text access to the 2020 minimum-code paper was unavailable, so prior work with a stronger count remains the main priority risk; the published abstract alone is not treated as exhaustive negative evidence.

## Mathematical value — PASS

This is a complete cardinality distribution, not a renaming of a minimum: the one-defect correction can lower the minimum degree and contributes the leading \(cn\lambda^n\) term, exceeding the zero-defect family by a factor growing linearly in the circumference. The natural object is the complement of a cycle, which is already studied for identifying-code minima. The explicit binomial defect classification both explains all code sizes and transfers to the extremal-radius odd-cycle incidence representation. The simple common-parity exponential growth is another independently useful consequence.

## Sources and limitations

Relevant comparisons: Nikandish, Khani Nasab and Dodonge, DOI 10.1142/S1793830920500469; Gravier, Moncel and Semri, DOI 10.1016/j.ejc.2004.09.005; the published exact OLD-cycle census, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-census-of-open-locating-dominating-codes-on-cycles--2cf44e5818fe; Cappelle et al., arXiv:1507.05083. The theorem covers neither graph-complement families beyond simple cycles nor optimal-code movement. A more exhaustive publication-priority search and independent mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
