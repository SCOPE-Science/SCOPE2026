# Review of the ten-cycle strong two-window threshold

## Correctness

PASS. The STFT intensity/ambiguity identity recovers all correlation products across visible lags. Connectivity yields injectivity, and the Fourier covariance transfers the criterion to the second window. The 60 disconnected supports are exhaustively enumerated, and all 3,600 possible ordered pairs yield full-column-rank reduced Fourier matrices over the finite field of 1,021 elements, thereby proving the corresponding complex cyclotomic ranks. The explicit factored signal has disconnected time and Fourier support at lag two, with no missing nonzero coefficients. The attached standard-library checker was executed successfully. No asymptotic inference from finite data is needed.

## Originality

PASS relative to the inspected sources and searches. Bartusel (arXiv:2605.31507, 2026) proves the general sufficient composite bound, which in dimension ten needs bandwidth four, whereas the new result shows that bandwidth three is necessary and sufficient. The earlier published prime-period Floquet result only treats each symmetry sector separately; it explicitly excludes the general full-space classification. Bartusel (2023) provides the connectivity reduction but not the order-ten joint Fourier support obstruction. The exact published order-eight/nine support-incidence data concern other orders. Exact historical priority for alternative formulations is not guaranteed.

## Value

PASS. Strong two-window retrieval asks for recovery using either experiment separately, not their pooled data. Ten is a natural first composite case in which an exact strictly better bandwidth than the general bound can be demonstrated by a complete classification. The theorem supplies the sharp acquisition bandwidth for all signals, not just periodic/eigenvector subfamilies, and a concrete nonrecoverable witness below it. The finite scope is a genuine full-space threshold rather than an arbitrary small parameter evaluation.

## Limitations and closest literature

The claim is for complete ten-site STFT arrays; it does not address stability/noise or larger composite orders. The closest prior works are Bartusel (2026), Bartusel (2023), and the published prime-period Floquet-sector result of October 2026. All mathematical correctness checks here are self-review; no independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
