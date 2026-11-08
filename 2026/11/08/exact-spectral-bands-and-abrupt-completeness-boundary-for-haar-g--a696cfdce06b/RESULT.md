# Exact spectral bands and abrupt completeness boundary for Haar Gabor systems

## Finding

Let \(g=-\mathbf 1_{[-1/2,0)}+\mathbf 1_{[0,1/2)}\), let the modulation step be \(b\), and let the translation step be \(a=1/(2b)\). For every \(1<b\le 2\), denote by \(S_b\) the bounded, nonnegative frame operator of the Gabor family \(\{e^{2\pi i m b t}g(t-na):m,n\in\mathbb Z\}\) on \(L^2(\mathbb R)\).

**Theorem.** Its entire operator spectrum, not just its frame/nonframe status, is
\[
\operatorname{spec}(S_b)=
\begin{cases}
[1/b,5/b], &1<b\le3/2,\\
[0,8/b], &3/2<b\le2.
\end{cases}
\]
Consequently, for \(1<b\le3/2\) the **optimal squared frame bounds** are \(A_b=1/b\) and \(B_b=5/b\), hence the exact frame-condition number is \(5\). For \(3/2<b\le2\), the family is **complete but not a frame**: \(\ker S_b=\{0\}\), the optimal nonnegative lower spectral bound is \(0\), and the optimal Bessel bound is \(8/b\).

For \(1<b<3/2\), the spectral point \(2/b\) is an eigenvalue of infinite multiplicity embedded in the continuous band; the remaining spectral measures are absolutely continuous. For \(3/2\le b\le2\), the spectrum is purely absolutely continuous. At the included frame endpoint \(b=3/2\), the lower bound is \(2/3\), whereas for every \(b>3/2\) in the stated range it is zero. This exact discontinuous loss occurs while the Gabor family remains complete.

## Assumptions and scope

The Haar window has exactly the stated support, amplitudes, and half-open convention. Inner products and Fourier modulations use the \(e^{2\pi i m b t}\) convention; squared frame bounds are those of the positive operator \(S_b\). The lattice has fixed area \(ab=1/2\), and the parameter range \(1<b\le2\) is the entire first overlap regime in which at most the nearest neighbors in the Walnut representation interact. Spectrum means spectrum as an operator on the full Hilbert space \(L^2(\mathbb R)\), not a spectrum inferred from a finite matrix discretization.

## Proof

**Step 1: exact Walnut formula.** Put \(q=1/b=2a\). By Fourier-series orthogonality (Poisson summation in the modulation index), initially on compactly supported test functions and then by bounded extension,
\[
(S_bf)(t)=\frac1b\sum_{\ell\in\mathbb Z}G_\ell(t)f(t-\ell q),\qquad
G_\ell(t)=\sum_{n\in\mathbb Z}g(t-na)g(t-na-\ell q).
\]
All sums defining the coefficients are finite. Because \(q\ge1/2\) and \(g\) is supported on an interval of length one, \(G_\ell=0\) almost everywhere for \(|\ell|\ge2\); the possible endpoint touching at \(b=2\) has measure zero. The resulting finite-shift formula also proves boundedness on \(L^2\).

**Step 2: exact integer overlap.** Define
\[
M_b(t)=\sum_{n\in\mathbb Z}\mathbf 1_{[q-1/2,\,1/2)}(t-na).
\]
For the \(\ell=1\) overlap, \(g(t-na)\) and \(g(t-na-q)\) always have opposite signs, so \(G_1(t)=-M_b(t)\). Since \(q=2a\), index translation gives \(G_{-1}(t)=-M_b(t)\) as well. Splitting the full support \([-1/2,1/2)\) into a segment of length \(q=2a\), which contains exactly two points of \(a\mathbb Z\) almost everywhere, and the remaining interval \([q-1/2,1/2)\), yields \(G_0(t)=2+M_b(t)\). Thus
\[
(S_bf)(t)=\frac1b\bigl[(2+M_b(t))f(t)-M_b(t)f(t-q)-M_b(t)f(t+q)\bigr].
\]
The coefficient \(M_b\) is \(a\)-periodic, hence \(q\)-periodic. The interval defining it has length \(1-q\); dividing by the lattice spacing gives \((1-q)/a=2b-2\). Therefore its values, on subsets of positive measure whenever both occur, are exactly
\[
\operatorname{essran} M_b=
\begin{cases}
\{0,1\}, &1<b<3/2,\\
\{1\}, &b=3/2,\\
\{1,2\}, &3/2<b<2,\\
\{2\}, &b=2.
\end{cases}
\]
These are exact lattice-count facts, not asymptotic approximations.

**Step 3: a scalar direct-integral diagonalization.** Decompose the real line into \(q\)-spaced fibers over \([0,q)\). On each fiber, Fourier transformation of the \(\ell^2(\mathbb Z)\) shift produces a unitary realization of \(S_b\) as multiplication on \(L^2([0,q)\times\mathbb T)\) by
\[
\sigma_b(t,\theta)=\frac{2+M_b(t)-2M_b(t)\cos\theta}{b}.
\]
For \(M_b=0\) its range is the point \(2/b\); for \(M_b=1\) its range is \([1/b,5/b]\); for \(M_b=2\) its range is \([0,8/b]\). The essential range of this multiplier gives the stated complete spectrum. Since each band-endpoint is approached on a positive-measure set of fibers and angles, both optimal frame bounds really are sharp.

**Step 4: completeness and spectral type.** In \(3/2<b\le2\), \(M_b\) takes values only \(1\) and \(2\), and \(\sigma_b\) can vanish only at \(\theta=0\) on the \(M_b=2\) fibers. This is a null set. Hence multiplication by \(\sigma_b\) has trivial kernel, equivalently the analysis map of the Gabor family has trivial kernel, proving completeness. Nevertheless \(\operatorname{essinf}\sigma_b=0\), ruling out a positive lower frame bound. When \(1<b<3/2\), the positive-measure \(M_b=0\) fibers give an eigenspace at \(2/b\) of infinite multiplicity. On all fibers with \(M_b=1\) or \(2\), the map \(\theta\mapsto\sigma_b(t,\theta)\) is nonconstant and has a derivative vanishing only at finitely many angles; its pushforwards of \(L^1\)-densities are absolutely continuous. This proves the stated spectral type and absence of further eigenvalues.

## Verification

The standalone program `checks/haar_spectrum_check.py` uses exact rational arithmetic. It tests the finite-overlap coefficient identities, the lattice-count possibilities, the disappearance of higher shifts, and the extrema of the scalar multiplier across rational sample spacings. Run with `python checks/haar_spectrum_check.py`; its successful output reads `HAAR_GABOR_RATIONAL_CHECKS_PASS 34228`. The analytical proof above, rather than these finite tests, establishes the theorem for every real \(1<b\le2\).

## Relationship to prior work

Dai and Zhu give a full **qualitative** classification of the Haar-window Gabor frame set (first publicly available 2022-05-13); their principal theorem and accompanying argument characterize which lattices give frames. On the fixed-area curve considered here that classification supplies the frame/nonframe transition but does **not** state this full spectral multiplier, sharp spectral bands, embedded eigenvalue, or completeness-without-a-frame result. The latter conclusions are strictly stronger operator statements than the binary frame set.

The classical Walnut formula and fiber diagonalizations are established techniques: their use here is not presented as an invention. The painless-expansion regime \(b\le1\), in which nonzero Walnut shifts vanish, is deliberately excluded from the new theorem. General Gaussian frame-bound papers concern a different smooth window. Nearby sharp calculations for the **triangular** (hat) B-spline concern a continuous, non-Haar window and have different overlap coefficients.

A potentially relevant broad 1996 paper by Janssen concerns exact bounds for several windows at integer redundancy; its accessible abstract does not enumerate the windows. Its full text could not be inspected through available scholarly-access routes, and whether it implicitly contains this exact Haar specialization remains a specific priority risk.

## Limitations

The assertions are limited to the signed Haar window, area \(ab=1/2\), and \(1<b\le2\). They do not classify all Haar-lattice spectra, do not address nonrectangular lattices, and do not establish numerical stability of reconstruction for \(b>3/2\); in fact, no positive uniform stability bound exists there. The sharp formulas are proved analytically, with finite rational checks only as reproducibility aids. Historical priority is provisional because a sufficiently general earlier frame-bound calculation may entail the special case.

## References

- Xin-Rong Dai and Meng Zhu, *Frame set for Gabor systems with Haar window*, arXiv:2205.06479, first publicly available 2022-05-13; later published in *Applied and Computational Harmonic Analysis*, DOI 10.1016/j.acha.2024.101655. Full open preprint: https://arxiv.org/abs/2205.06479.
- A. J. E. M. Janssen, *Some Weyl-Heisenberg frame bound calculations*, *Indagationes Mathematicae* 7 (1996), 165–183, DOI 10.1016/0019-3577(96)85088-9. Abstract available; specialization not verified from full text.
- Markus Faulhuber, *Minimal Frame Operator Norms Via Minimal Theta Functions*, *Journal of Fourier Analysis and Applications* (2018), DOI 10.1007/s00041-017-9526-x. Gaussian-window comparison, not the present Haar case.
