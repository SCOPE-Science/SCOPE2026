# Mathematical review

## Correctness — PASS

The domain is a Neumann-tipped, symmetric type-I, identical side-resonator quantum graph with positive couplings and irrational pendant/spacing ratio. The precise source Theorem 1(i), equation (4.4), reduces to the stated Chebyshev probability; the source's equation (5.2) gives the normalization \(b=\theta_3^2/(2\theta_1\theta_2)\), hence \(\theta_1=\theta_2=t\) gives the claimed parameter. Irrational torus equidistribution and bounded Riemann-integrability yield the average for fixed finite \(N\). A shifted-cosine integral yields exact \(N=1,2\) values. For fixed \(z>1\), the complement of the Chebyshev band contributes zero by exponential growth, and the band oscillations average by trigonometric approximation/Riemann–Lebesgue; an integrable endpoint majorant yields the stated closed band integral. Dominated convergence then permits the outer phase integral. Its elementary inverse-hyperbolic/inverse-trigonometric evaluations yield the stated logarithmic and inverse-power expansions. This is an infinite proof, separate from the 17 numeric diagnostic checks in CHECK.py. No pointwise in-band limit or simultaneous \(k,N\) limit is proved.

## Originality — PASS (with priority qualifications)

The complete source [1], including Theorem 1, Proposition 2 and Sections 5–7, provides the scattering expression and qualitative pass/gap structure but no finite-\(N\) high-frequency Cesaro average or sequential long-array mean was located. The strongest nearby published formulas, [1] equation (4.3) and the periodic waveguide phase method [3], could imply the result after additional phase integration; [1] is explicitly cited as an input and [3] was accessible only at abstract/metadata level. The older superlattice paper [2] discusses a physically different miniband average. Search of the mathematical-results index under exact source, broadband Cesaro aliases, Chebyshev band averages and logarithmic weak-coupling terms yielded separate spectral-density and quantum-graph results but no exact source-identical statement. This is best-knowledge originality, not a guarantee of publication priority.

## Mathematical value — PASS

The source's persistent high-frequency resonances and gaps raise the natural transport question of total throughput averaged over broadband illumination. The answer is not a routine title substitution: two independent incommensurate phases and an infinite-array oscillatory Chebyshev band/gap limit are required. It yields a strictly positive closed-form throughput despite exponentially suppressed gaps, and a nonanalytic \(b\log(1/b)\) weak-coupling loss contrasting with the linear fixed-one/two-resonator loss. The sequential limit resolves a physically meaningful and previously unquantified operational distinction.

## Relevant literature and limitations

[1] K. Buhrii, Y. Golovaty, R. Hryniv, *Scattering in Quantum Graphs with Scale-Invariant Vertex Couplings: Resonances, Gaps and (Quasi-)Periodic Transmission* (2026), arXiv:2606.14931, Theorem 1 and Sections 5–7, full text examined.

[2] C. N. Veenstra et al., *Time dependence of transmission in semiconductor superlattices* (2004), arXiv:cond-mat/0411118, accessible descriptive material examined; different energy-weighting/model.

[3] L. Rughunanan et al., *On the behaviour of infinite, periodic, mono-coupled waveguides using a transmission coefficient phase method* (2020), DOI:10.1016/j.ymssp.2019.106409, abstract/metadata inspected only. The unexamined full derivation is a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
