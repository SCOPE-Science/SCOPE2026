# Scientific review

## Correctness — PASS

The statement fixes the unnormalized unit-weight graph Laplacian, the half-step normalization, separate bipartite degree caps and every-positive-step quantifiers. The identity \(C=2R-I\) leaves only diagonal return probabilities to check. A nonnegative Neumann-walk expansion compares the finite graph to its universal cover; a quadratic-form ordering compares the cover to its completion as the biregular tree. The tree cavity Schur equations are reconstructed with the parent-edge contribution retained on the diagonal; their physical solution and the two root types are distinguished. The explicit quadratic has exactly one positive root, and bounded finite balls converge in resolvent to the tree, proving sharpness rather than relying on finite tests. Supplementary checks: `python3 verify.py` passed 45 algebraic parameter identities, 45 two-type threshold cases and 223 rational graph inversions. Risk: numerical checks are not an independent proof, and the result does not address nonunit edge weights.

## Originality — PASS, with specified residual risk

The closest same-scope earlier finding is the maximum-degree-only \(p\)-regular-tree law (claim identifier `01f56608-d0de-4d06-b1f7-31c6d6b77541`), which yields the strictly smaller \((2p-1)/(2p(p-1))\) but **does not imply** the larger \((p,q)\) threshold when \(p>q\). The regular limit \(p=q\) is not presented as new. Faragó–Horváth [1], inspected in its accessible author text through its general-positivity, finite-difference and finite-element sections, contains conditions on standard meshes but no pair-of-degree-caps sharp theorem. Chung–Yau [2], inspected in the accessible full PDF, studies coverings and regular-tree heat kernels but not this positivity boundary. The 2025 biregular-tree Green-function treatment [3] has the same underlying tree Laplacian but studies propagators, not finite-graph Crank–Nicolson positivity. A published general resolvent-return result already gives the positivity criterion; the new material is the tree extremality with the explicit two-cap optimization. Specialist priority beyond inspected material remains possible, and one relevant public general-result description was accessible only as a summary.

## Value — PASS

Separate degree caps on the two sides of a bipartite transport or diffusion network are natural structural information, and ignoring them forces the strictly smaller best possible one-cap positivity step. The new exact two-parameter frontier holds uniformly over every finite graph size and topology in the class, has sharp finite witnesses and gives an algebraic timestep rule without eigensolving the actual graph. The gain is small in some regimes but is mathematically structural and sharp, not an arbitrary small-graph table or a parameter relabeling.

## Unproved scope and independent status

Publication-level priority in all graph-diffusion and Green-function literature remains open to independent checking. The theorem is not a result about nonbipartite graphs, variable conductances or higher-order methods.

Self-review: passed. Independent audit: not yet performed.
