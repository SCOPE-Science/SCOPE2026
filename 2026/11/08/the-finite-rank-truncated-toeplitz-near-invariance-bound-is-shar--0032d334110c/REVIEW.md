# Scientific assessment

## Correctness — PASS

All operators are bounded finite matrices in the monomial basis of the model space. The independent coordinate ranges of \(U\) and \(Q\) give \(QU=0\), making \(I-UQ\) explicitly invertible. The calculation \(\ker(A(I-UQ))=(I+UQ)\ker A\) determines the entire kernel without dimension heuristics. The exact quotient identity (1) has \(2n+1\) independent input coefficients, its output spans \(W\), and \(W\cap\mathcal M_n=\{0\}\). Since every kernel function vanishes at zero, this is the intrinsic minimum nearly invariant defect. The algebra works for every integer \(n\ge1\); an exact-matrix checker independently confirms examples through eight.

## Originality — PASS (best-knowledge)

The closest published theorem is [1, Theorem 5.4], which gives the upper bound but not an attaining family in every perturbation rank. Its full text was inspected, including the theorem, section 5 examples, and the tabulated defect bounds. The full accessible treatments [2], [3], and [4] were compared: [2] treats structural finite-defect theory and unperturbed truncated kernels, while [3] and [4] concern ordinary Toeplitz kernels on (possibly vector-valued) full Hardy spaces. They do not state this explicit rank-\(n\) scalar compressed-kernel lower bound. Searches for sharpness, near-invariance defect, finite Blaschke monomial models, and the exact numeric bound did not identify an equivalent proof. Publication priority remains qualified by the possibility of a differently formulated older example.

## Mathematical value — PASS

The target is the exact optimality of a central quantitative bound in a newly introduced finite-rank perturbation theorem, not an arbitrary finite-dimensional value. Showing \(2n+1\) is necessary at **every** rank rules out any uniform improvement of the theorem, including an improved linear coefficient or additive term. The witnesses have a simple analytic monomial symbol, a finite model of dimension linear in the perturbation rank, and an explicitly described kernel graph; these structural features make the obstruction reproducible and useful when assessing refined hypotheses.

## Closest prior work and limitations

[1] is primary and already owns the upper bound; only the lower-bound sharpness family is claimed here. [2] is the finite-defect structural framework. [3] and [4] concern related nontruncated Toeplitz perturbations. No optimality of model-space dimension or exhaustive classification is claimed. More broadly indexed older work could still contain an equivalent construction. Independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
