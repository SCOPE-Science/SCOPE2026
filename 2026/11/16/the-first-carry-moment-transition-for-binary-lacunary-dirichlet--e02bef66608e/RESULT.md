# The first-carry moment transition for binary lacunary Dirichlet kernels

## Finding

For integers \(b\ge2\), \(n\ge1\), and \(r\ge1\), define the binary digit spectrum and its flat Fourier kernel on the normalized circle by
\[
\Lambda_{b,n}=\left\{\sum_{j=0}^{n-1}\varepsilon_j b^j:\ \varepsilon_j\in\{0,1\}\right\},\qquad
D_{b,n}(t)=\sum_{k\in\Lambda_{b,n}}e^{2\pi i kt}
=\prod_{j=0}^{n-1}(1+e^{2\pi i b^j t}),
\]
where \(t\in\mathbb R/\mathbb Z\). Write \(E_{b,r}(n)=\int_0^1|D_{b,n}(t)|^{2r}\,dt\). Then every even moment strictly below the first carry obeys the exact independence law
\[
E_{b,r}(n)=\binom{2r}{r}^{n}\quad(1\le r<b).
\]
At the first possible carry, put \(C=\binom{2b}{b}\), \(K=\binom{2b}{b-1}\), and \(a=2b\). With \(E_{b,b}(0)=1\) for the empty product, the full critical moment sequence satisfies
\[
\boxed{E_{b,b}(n+2)=(C+a)E_{b,b}(n+1)-(aC-2K)E_{b,b}(n)},
\quad E_{b,b}(0)=1,\quad E_{b,b}(1)=C.
\]
In particular, defining
\[
\lambda_{\pm}=\frac{C+a\pm\sqrt{(C-a)^2+8K}}{2},
\quad A_+=\frac{C-\lambda_-}{\lambda_+-\lambda_-},
\quad A_-=\frac{\lambda_+-C}{\lambda_+-\lambda_-},
\]
we have the exact formula and sharp exponential rate
\[
\boxed{E_{b,b}(n)=A_+\lambda_+^n+A_-\lambda_-^n},\qquad
\lim_{n\to\infty}E_{b,b}(n)^{1/n}=\lambda_+>C.
\]
Both coefficients \(A_+\) and \(A_-\) are strictly positive. For every \(n\ge2\), \(E_{b,b}(n)>C^n\); equality holds at \(n=1\). Thus the critical moment \(2b\), unlike every smaller even moment, is not obtained by multiplying independent one-digit moments.

In the middle-fourth case \(b=4\), this specializes to
\[
E_{4,4}(n)=\frac{31+\sqrt{1073}}{2\sqrt{1073}}(39+\sqrt{1073})^n
+\frac{\sqrt{1073}-31}{2\sqrt{1073}}(39-\sqrt{1073})^n.
\]
Its first four positive-depth values are \(70,5012,359576,25801552\). The comparison is specifically with normalized *Lebesgue* measure on the circle, not the associated singular Cantor measure.

## Assumptions and scope

All bases and depths are integers, with \(b\ge2\), \(n\ge1\). The coefficients of the kernel are exactly one; no optimization over arbitrary coefficients is claimed. All integrals are against Haar probability measure \(dt\) on \([0,1)\). For the recurrence only, the empty product is defined at \(n=0\). The full critical theorem includes the boundary case \(b=2\). No assertion is made for moments of order greater than \(2b\), where larger carry states may enter.

## Proof

**1. Fourier orthogonality and digit expansion.** Expand \(D_{b,n}^r\) as a product of binomial sums:
\[
D_{b,n}(t)^r=\prod_{j=0}^{n-1}\sum_{k=0}^r\binom rk e^{2\pi i kb^jt}.
\]
By Fourier orthogonality, \(E_{b,r}(n)\) is the weighted number of pairs of digit vectors \((k_j)\) and \((\ell_j)\) in \(\{0,\ldots,r\}^n\) for which
\[
\sum_{j=0}^{n-1}(k_j-\ell_j)b^j=0,
\]
with weight \(\prod_j\binom r{k_j}\binom r{\ell_j}\). Each representation has an integer carry sequence \(u_0,\ldots,u_n\) with \(u_0=u_n=0\) and
\[
bu_{j+1}=u_j+k_j-\ell_j.
\]
Indeed, the carry is the signed lower-digit sum divided by the corresponding power of \(b\), and divisibility at every step follows from the total zero-sum condition. Conversely, any such carry sequence yields that sum equation by telescoping.

**2. No-carry range.** If \(1\le r<b\), the only integer value available for \(u_1=(k_0-\ell_0)/b\) is zero. Induction gives \(u_j=0\) for every digit, hence \(k_j=\ell_j\) termwise. The one-digit total weight is \(\sum_{k=0}^r\binom rk^2=\binom{2r}r\) by Vandermonde's identity. This proves the exact factorization for all \(n\).

**3. Critical transfer matrix.** Let \(r=b\). By induction from \(u_0=0\), all integer carries satisfy \(|u_j|\le1\): if \(|u_j|\le1\), then \(|u_j+k_j-\ell_j|\le b+1\), so its integral quotient by \(b\) has absolute value at most one for every \(b\ge2\). Ordered as \(-1,0,1\), their weighted transition matrix is
\[
T_{u,v}=\sum_{k-\ell=bv-u}\binom bk\binom b\ell
=\binom{2b}{b+bv-u},\qquad
T=\begin{pmatrix}a&K&0\\1&C&1\\0&K&a\end{pmatrix}.
\]
The binomial coefficient is interpreted as zero outside its natural range. Paths starting and ending at carry zero are enumerated exactly by \(E_{b,b}(n)=(T^n)_{0,0}\), where the \(0,0\) entry means the central carry state. Reflection symmetry decomposes the matrix into a one-dimensional antisymmetric sector with eigenvalue \(a\) and a symmetric two-dimensional sector with characteristic polynomial
\[
\lambda^2-(C+a)\lambda+(aC-2K).
\]
The central state belongs entirely to the symmetric sector, so Cayley–Hamilton gives the stated second-order recurrence and initial values. Solving it gives the exact eigenvalue formula.

**4. Sharpness and strict transition.** Since \(K=C b/(b+1)>0\) and \(C>a\) for \(b\ge2\), the two roots obey \(0<\lambda_-<a<C<\lambda_+\). The displayed formulas therefore give \(A_+>0\) and \(A_->0\), proving the stated exponential rate. For \(n\ge2\) the transfer-path expansion contains all zero-carry paths, whose total is \(C^n\), and in addition the strictly positive closed two-step excursions \(0\to1\to0\) or \(0\to-1\to0\) (with further zero-carry steps). This proves strict inequality at all depths at least two.

## Verification

The accompanying standalone Python checker, `check_first_carry.py`, uses integer-only polynomial convolution to compute the moments from the Fourier coefficients independently of the three-state transfer calculation. It compares all \(b\in\{2,\ldots,8\}\), \(n\in\{1,2,3,4\}\), and \(1\le r\le b\); it also verifies subcritical factorization, the critical recurrence, and the four explicit depth values for \(b=4\). Its 281 exact assertions pass. These finite tests are corroboration; the unbounded-in-\(n\) and unbounded-in-\(b\) results are proved above, not inferred from enumeration.

Run with `python3 check_first_carry.py` from the directory containing the two files. No nonstandard Python packages are needed.

## Relationship to prior work

Tang and Wu (2026, first circulated July 30) use the canonical middle-fourth spectrum and the same factorized Dirichlet kernel to prove almost-everywhere convergence of mock Fourier expansions. Their result is about the maximal operator for the singular Cantor measure, not the exact Haar \(2b\)-th moment or the first-carry spectral rate. Classical carry matrices, including those of Holte and Diaconis–Fulman, establish general carry-transfer methods for ordinary random base expansions; their Markov matrices use unrestricted digits and a different carry constraint. General digit-restricted transfer computations are also available in informal computational accounts. The present precise two-eigenvalue evaluation and the universal first-resonance threshold should therefore be viewed as an explicit structural refinement, not as invention of carry methods. Equivalent evaluations may exist in the older lacunary/Riesz-product literature and require independent bibliographic checking.

## Limitations

The result addresses *flat* binary digit Dirichlet kernels only. It does not establish an extremal \(L^{2b}\) norm over arbitrary complex coefficients, a Cantor-measure moment identity, or convergence of mock Fourier expansions. A general automaton method can obtain an unevaluated recurrence for many digit sets; the claimed specific contribution is the all-base first-carry collapse and evaluated critical growth law. The literature comparison cannot exclude unindexed equivalent formulas. No independent audit has been performed.

## References

1. M.-W. Tang and Z.-Y. Wu, *Almost everywhere convergence of mock Fourier series for the middle-fourth Cantor measure*, arXiv:2607.27796 (initial release July 30, 2026), https://arxiv.org/abs/2607.27796 .
2. P. E. T. Jorgensen and S. Pedersen, *Dense analytic subspaces in fractal \(L^2\)-spaces*, Journal d'Analyse Mathématique 75 (1998), 185–228.
3. P. Diaconis and J. Fulman, *Carries, Shuffling and An Amazing Matrix*, arXiv:0806.3583 (2008), https://arxiv.org/abs/0806.3583 .
4. J. Holte, *Carries, combinatorics, and an amazing matrix*, American Mathematical Monthly 104 (1997), 138–149, https://doi.org/10.2307/2974981 .
