# Scientific review

## Correctness (C): PASS

For \(f=f^{-1}\), source and target affine subspaces coincide. The proof reduces each map to \(f(x)=(I+N)x+b\) with \(N^2=0\), \(b\in\ker N\), and classifies the fixed-point equation \(Nx=b\). It separately establishes the rank-\(r\) square-zero operator count by image/kernel/quotient choices, then counts all affine domains. The normalizations in the asymptotic passage are explicit. The Euler product is used with both parity projections; dominated convergence is justified by a summable Gaussian tail. The code verifies literal finite compositions and the exact table through ambient dimension four, then independently checks asymptotic values numerically through dimension twenty. The proof, not the finite tests, establishes the infinite result.

## Originality (O): PASS relative to checked material

The closest primary results are [1], whose category-equivalence theorem defines the affine partial inverse monoid, and [2, Proposition 3.1], which already counts linear involutions by their rank parameters. The latter is an ingredient, not a new claim. It does not specify the present joint domain-and-fixed-point spectrum or the global half-density and parity-codimension mixing law. No matching claim was located in the queried indexed findings or relevant web searches. These negative searches alone do not establish uniqueness or priority. A broader counting theorem for the affine general linear groups, combined with Gaussian domain counting, could cover the fixed-point formula or yield the half-density; this is the principal residual publication-priority risk.

## Mathematical value (V): PASS

The self-inverse elements of the binary affine-partial inverse monoid are a canonical family of reversible partial operations, directly related to the inverse categorical semantics of controlled-not circuits. The theorem gives a complete natural joint invariant (domain size and number of fixed inputs) in every ambient dimension, including fixed-point gaps, not an arbitrary finite sample. Its asymptotic statement identifies a non-obvious symmetry: separate affine dimensions have two unequal limiting fixed-point-free proportions, while the natural ensemble of partial maps tends to exactly one-half because domain codimensions asymptotically equilibrate parity. This global cancellation is not merely the general-linear involution count. It does not require a claimed downstream theorem.

## Evidence and limits

Primary papers inspected in relevant sections: Cockett–Comfort–Srinivasan, arXiv:1707.02348, original PDF pages 1, 5–8, and 33–36; Fulman–Guralnick–Stanton, arXiv:1602.03611, original PDF pages 1–2 and 12–15. Exact direct computations are reproduced by `verify.py`; the proof covers every \(d\ge0\). Priority over unlocated general affine-involution literature is unconfirmed, and there has been no independent audit.

Self-review: passed. Independent audit: not yet performed.
