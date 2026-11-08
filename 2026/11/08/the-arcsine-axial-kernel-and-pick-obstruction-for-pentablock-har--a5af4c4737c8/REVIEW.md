# Scientific review: arcsine axial kernel and Pick obstruction

## Correctness — PASS

The canonical boundary measure is the pushforward of three-torus Haar measure by the pentablock parametrization. Independently rotating the torus fibre and the two base variables makes each axis monomial \(a^n\) orthogonal to every other coordinate monomial. The remaining diagonal moment is exactly a central-binomial arcsine moment; this yields the quotient norm and reproducing kernel, with no unstated approximation assumption. The binomial recurrence gives the closed analytic kernel. The positive-coefficient transform \((1-t)^{3/2}S(t)\) has nonconstant coefficient mass \(\pi/2-1<1\), establishing the zero-free bound for every complex \(|t|<1\). The negative coefficient of \(t^2\) in \(1-1/S(t)\) excludes the complete Pick property for the restricted kernel, hence for the full kernel. The boundary metric asymptotic follows by differentiating the explicit formula and controlling the endpoint derivative. A standalone checker passed 734 independent finite consistency assertions. None of the infinite assertions rests on those finite tests alone.

## Originality — PASS relative to checked literature

Su and Tomar, arXiv:2610.17729, §§2–3 and Propositions 2.2, 3.5, 3.6, provide the boundary Hardy construction, its general orthogonal decompositions, an abstract projected reproducing kernel and general diagonal growth. The inspected material does not provide the explicit axial quotient, identify the arcsine measure, or decide zero-freeness, the complete Pick property and the axial sharp constant. The new statement is not a different presentation of their Toeplitz and commutant results. Pal and Tomar, arXiv:2606.00850, use admissible kernels for a Toeplitz corona theorem, not the canonical Hardy kernel evaluated here. Alpay and Jorgensen's binomial RKHS lives on nonnegative integers and has kernel \(\binom{x+y}{x}\), rather than a disk kernel with reciprocal central-binomial coefficients. Sprugnoli's reciprocal-binomial generating series is classical and expressly not asserted as original. The normalized complete Pick characterization is likewise standard. Relevant published mathematical records about zero-free radial Bergman kernels concern different radial weights and do not imply the pentablock axis identification or the global complete Pick obstruction. Earlier mathematical statements checked for substantive overlap did not include this pentablock axial claim.

**Residual risks:** A differently named pre-2026 weighted kernel paper could have the same arcsine kernel, and a different proof of non-Pick behavior could be known. Priority of the classical generating-series identity is not claimed. Full publication-priority certification has not been performed.

## Value — PASS

The original pentablock Hardy construction provides only an abstract kernel projection. Here a geometrically distinguished embedding of the disk is identified isometrically with a concrete arcsine-weighted Bergman model. That yields usable exact evaluation norms, a global quantitative axial zero-free estimate, the sharp fractional boundary growth exponent and a definite obstruction to complete Pick interpolation on the **whole** space. These are intrinsically motivated structural properties of the canonical space, rather than an arbitrary parameter slice or a routine numerical recomputation. They distinguish geometric kernel nonvanishing from the substantially stronger Pick condition.

## Scientific limitations

Zero-freeness is proved only along the first-coordinate axis; nothing here decides all off-axis kernel zeros. The boundary asymptotic is axial, and other pentablock Hardy norms or measures may behave differently. The work does not prove a full interpolation theorem or a global metric asymptotic. This is a self-review, not an independent audit.

Self-review: passed. Independent audit: not yet performed.
