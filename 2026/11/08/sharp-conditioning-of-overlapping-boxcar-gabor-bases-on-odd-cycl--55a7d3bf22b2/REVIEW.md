# Scientific assessment

**Correctness (PASS).** The spectral calculation explicitly tracks normalization and multiplicities through an \(a\)-point modulation DFT and a \(b\)-point translation DFT. The arithmetic criterion \(\gcd(q_u,b)=1\) handles all zero and full-length boundary fibers. The strict sampled Dirichlet-kernel estimate is proved in both parity cases, including the borderline \(b=3\) and \(h=3\) regimes. It forces a strict spectral-condition gap for any admissible length beyond two translation steps. The executable checker is supportive and not substituted for the universal proof.

**Originality (PASS relative to inspected literature).** The closest motivating full text, Asipchuk–De Carli–Rodriguez (arXiv:2605.16139), gives general subgroup-based block equivalence, not this sharp window-length minimization and its complete set of minimizers. Faulhuber–Shafkulovska (arXiv:2204.02917) treats different continuous Gabor designs. Earlier discrete Zak references address spectral calculation but were not fully accessible and may contain special cases. Similar indexed finite-Gabor tomography studies operator-span rank rather than the linear frame bounds. Novelty remains subject to independent historical priority review.

**Value (PASS).** In a critical finite cyclic design, a boxcar may need to overlap translations for support coverage or implementation constraints. The result determines the exact unavoidable stability penalty, proves that making the window longer cannot improve it, classifies all optimal integer lengths, and quantifies the quadratic growth in odd fiber size. Its sampled trigonometric extremal bound is the nonroutine step.

**Limitations.** Odd fibers, unweighted consecutive boxcars, critical rectangular subgroup sampling, and strictly overlapping lengths only. The optimization does not cover even fibers or other window families. Independent audit and exhaustive historic-publication priority certification have not occurred.

Self-review: passed. Independent audit: not yet performed.
