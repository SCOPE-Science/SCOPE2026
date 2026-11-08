# Mathematical review

## Correctness — PASS

A local automorphism is determined by its lower-triangular matrix because genuine automorphisms preserve the radical-power filtration and have nonzero leading coefficients. The three scalar interpolation equations in RESULT.md are necessary and sufficient, partitioned by the first nonzero coefficient of a tested element. In characteristic two, the uniqueness of a square root and vanishing of the mixed \(2uv\) term force the same parameter to govern the square and cube entries; in odd characteristic the mixed term lets the coefficients be adjusted separately. Counting parameter choices proves the finite-field formulas; the explicit examples and \(\mathbb F_2\) normal form settle the iff assertion. Exhaustive direct finite-field checks in the attached source code agree for four fields, including \(\mathbb F_4\). No finite sample is used as an all-field proof.

## Originality — PASS, with residual priority risk

The closest primary source is Arzikulov–Karimjanov–Umrzaqov (arXiv:2305.13720, 2023; DOI:10.13069/jacodesmath.v11i3.279, 2024). Their genuine-automorphism substitution form is known, and their local-automorphism theorem describes lower-triangular matrices in the setting treated there. The published proof divides by integer coefficients and takes roots (journal pp. 156–158); these operations are not generally available over finite fields or characteristic two. The present full arbitrary-field classification, coupled characteristic-two condition, exact finite-field group sizes, and sharp \(\mathbb F_2\) local-to-global criterion are not provided by those inspected passages and cannot be obtained from the characteristic-zero lower-triangular form by specialization alone. Published record searches and accessible earlier claim comparisons did not reveal a covering theorem. Nonindexed or unexamined field-dependent classifications remain a publication-priority risk.

## Mathematical value — PASS

A local automorphism is a pointwise symmetry that need not preserve multiplication globally. The question of when local symmetries are genuine is a structural local-to-global problem. The theorem supplies a complete arbitrary-field answer for the minimal three-dimensional null-filiform example where the mixed-square coefficient appears, identifies the exact obstruction at characteristic two, and shows that \(\mathbb F_2\) is uniquely rigid among all fields for this algebra. The finite-field group-order formulas distinguish residue-subgroup constraints from the characteristic-two coupling; they are not merely a recomputation of the known automorphism order. The claim does not extend to higher-dimensional or non-linear local maps.

Self-review: passed. Independent audit: not yet performed.
