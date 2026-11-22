# Self-review

## Correctness — PASS

The cyclic piecewise-linear hat Grams have unshifted symbol \(h(2+\cos\omega)/3\) and cross symbol \(h(z^{-2}+23z^{-1}+23+z)/48\). The positive Gram matrices and circulant diagonalization give the exact full positive spectrum of \(P_NQ_NP_N\), with zeros on the orthogonal complement. The principal cosine reduces to \(x(5+x^2)/(2(1+2x^2))\), whose derivative is \((1-x^2)(5-2x^2)/(2(1+2x^2)^2)>0\) for \(0\le x<1\). The fourth-order Taylor coefficient is \(1/192\), giving the sharp \(\pi^4/(12N^4)\) spectral gap. Nodal interpolants of each fixed Fourier mode converge in \(L^2\), while \(1-\mu\ge c\operatorname{dist}(\omega,2\pi\mathbb Z)^4\) gives a uniform summable spectral tail at positive macroscopic time. These two independent ingredients rigorously upgrade mode convergence to trace norm. The supplied rational checker passed 236 supplementary assertions. This is an analytic proof, not a finite enumeration extrapolation.

## Originality — PASS (best-knowledge, with risk)

The full-text 2021 periodic-spline stability work of Antonopoulos–Dougalis treats **one** orthoprojector, not the product of two half-shifted orthoprojectors or its power semigroup. The full-text 2021 variational alternating-projections work of De Bernardi–Miglierina treats general set convergence rather than the exact mesh-dependent trace-class limit. Related published calculations for single spline projectors, shifted histogram projections, and periodic biharmonic resolvents were examined in full: none establishes this claim or a stronger statement entailing it. The 2019 successive-projection B-spline paper was only abstract-accessible; its described time-discretization target differs, but complete priority remains uncertain. Classic Fourier, B-spline and principal-angle tools are not asserted to be original.

## Value — PASS

The natural question is the spectral cost of alternating projections between nearly coincident finite-element spaces. The result unexpectedly yields a **fourth-order**, rather than ordinary second-order, continuum generator, identifies its exact coefficient and proves convergence in the stronger trace-class topology. This provides both a sharp convergence-time scale and an entire limiting heat trace, information inaccessible from elementary alternating-projection convergence alone. It is not a mere index substitution or restatement of one-space stability.

## Closest literature and limitations

Antonopoulos–Dougalis (arXiv:2106.09060v1), De Bernardi–Miglierina (doi:10.1007/s10898-021-01025-y), and Ueda–Saito (doi:10.1016/j.cam.2019.03.026, abstract only) are the closest external material inspected. Additional primary scientific statements in the published periodic-spline, histogram-shift and biharmonic-resolvent results were compared at full-result level. The theorem does not address general offsets, higher spline degrees, nonuniform knots, or trace-norm convergence at zero time. A related inaccessible full paper remains a residual literature risk.

Self-review: passed. Independent audit: not yet performed.
