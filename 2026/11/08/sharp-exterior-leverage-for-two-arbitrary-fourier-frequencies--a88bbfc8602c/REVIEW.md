# Mathematical review: sharp exterior leverage for two arbitrary Fourier frequencies

## Correctness — PASS

The evaluation Gram matrix is positive definite for each nonzero real gap and yields the exact squared fixed-gap functional norm \(K_d(x)=(1-s\cos(dx))/(1-s^2)\). For gaps at least two, \(|s|\le1/d\) gives a strict bound by two. For smaller gaps, the endpoint certificate \(h''(d)=4\sin(d)(\sin(d)-d\cos(d))>0\), together with the exact derivative certificate \(3(1-u^2)-d^2u=d^4(160-d^4)/4800>0\), establishes the global exterior inequality and strictness. Convergence to the affine evaluation representer gives sharpness, and analytic Taylor expansion gives the nonzero quadratic gap. Exact rational symbolic verification and numerical checks are in `CHECK.py`. Boundary cases \(|x|=1\), large gaps, and the nonattained collision limit are separately addressed. Finite experiments supplement but do not replace the proof.

## Originality — PASS relative to inspected material

R. Zhang's arXiv:2607.10501, Theorem 1.1 and Section 8.2, provides general frequency-uniform exterior leverage bounds and a Gram representation but does not state the sharp \(k=2\) envelope, nonattainment or quadratic spectral-collision correction. Erdélyi–Musco–Musco arXiv:2006.07340 provides general Fourier-sparse leverage estimates; the same exterior two-frequency extremal claim was not found in the inspected portions. Borwein–Erdélyi's 2000 treatment focuses on real exponents and has a different pointwise geometry. Kós's classical endpoint bounds are relevant and the endpoint alone is not asserted to be novel. Exact alias and broader-coverage comparisons were carried out against accessible historical claims and mathematical record results; no dominating result was located. A specialized equivalent in older nonharmonic Fourier analysis remains possible, and Kós's complete article was not available for full-text comparison. Search absence is not proof of novelty.

## Value — PASS

The precise worst-case exterior amplification for the smallest nontrivial off-grid Fourier-sparse class is an interpretable sharp invariant for extrapolative sparse regression: it replaces unspecified constants by the exact \(x\)-profile, identifies the only extremizing mechanism (frequency coalescence), and quantifies loss from a nonzero gap to second order. These quantify stability uniformly over the unrestricted frequency parameter, which a fixed-frequency Gram computation alone would not establish. This is a natural exact endpoint of the open-frequency extrapolation framework, not a gratuitous numerical slice.

## Limits and remaining risks

The sharp bound concerns single-point exterior evaluation, exactly two distinct frequencies, and unaveraged Lebesgue \(L^2\) norm on \([-1,1]\). It does not solve the \(k\ge3\) or integrated prediction-transfer problems. External priority is not independently certified; endpoint-related precedents and inaccessible specialized texts remain originality risks. No independent correctness audit has been performed.

Self-review: passed. Independent audit: not yet performed.
