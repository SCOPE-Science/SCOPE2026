# Self-review

## Correctness — PASS
The family, Walsh normalization, set of all length vectors, operator norm and equality cases are fixed explicitly. The Gram identity follows from the nested orthogonality of Walsh prefix columns and is independently checked directly from the signed Walsh matrix. The complete \(4^8=65{,}536\)-case enumeration uses no floating point: integer Bareiss elimination tests the eight leading principal minors of \(68I-5H\). Precisely eight survivors are separately checked by exact characteristic polynomials, and the cubic sign crossing proves they all exceed the strict \(17/10\) threshold. The argument establishes an exhaustive finite theorem only; it does not infer the general conjecture from testing.

## Originality — PASS within inspected published evidence
Lakey (arXiv:2602.17627, 19 February 2026), notably Conjecture 6, Proposition 7, and the discussion of the standard complete branch, gives a proposed global optimal truncation and qualitative/numerical evidence, but no exact eight-column all-truncations equality census or \(17/10\) separation. Hogan–Lakey (Mathematics 14(5):829, 2026) studies the standard compressed matrix and an eigenvector asymptotic, rather than enumerating every dyadic truncation. Related indexed Hadamard discrepancy and Walsh Fourier-support work concerns distinct invariants; neither yields the exact matrix-norm optimization. Direct searches for characteristic polynomial, eight-by-eight truncated Walsh norms and equivalent branch descriptions did not demonstrate coverage. Older or unindexed finite matrix calculations and unlocated forthcoming work remain possible; searches alone are not a proof of novelty.

## Mathematical value — PASS
The verified case is the full depth-three instance of a specifically published harmonic-analysis extremality question over many competing branches, not an arbitrary submatrix. It classifies **all** eight extremizers among \(65{,}536\) discrete choices and proves a strict uniform gap separating the remaining \(65{,}528\) cases. Its reproducible integer certificate is a sharply delimited benchmark for proposed general branching/monotonicity arguments. No downstream infinite-level assertion is claimed.

Self-review: passed. Independent audit: not yet performed.
