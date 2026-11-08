# The arcsine axial kernel and Pick obstruction for pentablock Hardy space

## Finding

Let \(\mathcal P\) be the pentablock and let \(H^2(\mathcal P)\) be the canonical Hardy space defined from the normalized three-torus boundary pushforward described below. The restriction to the distinguished coordinate axis \(\{(a,0,0):|a|<1\}\), equipped with the minimum-extension norm, is exactly the analytic Hilbert space with coefficient norm
\[
\left\|\sum_{n=0}^{\infty}c_n a^n\right\|^2=\sum_{n=0}^{\infty}\frac{\binom{2n}{n}}{4^n}|c_n|^2.
\]
Equivalently, it is the disk Bergman space for the probability measure whose squared-radius variable has the arcsine density \(ds/(\pi\sqrt{s(1-s)})\).

Writing \(t=a\overline b\), its kernel is
\[
K_{\mathrm{axis}}(a,b)=S(t),\qquad
S(t)=\sum_{n=0}^{\infty}\frac{4^n}{\binom{2n}{n}}t^n
=\frac1{1-t}+\frac{\sqrt t\,\arcsin\sqrt t}{(1-t)^{3/2}}.
\]
The right-hand side is understood by its analytic continuation at \(t=0\), with the power-series branch on the open unit disk. It satisfies the global quantitative zero-free estimate
\[
|S(t)|\ge\frac{2-\pi/2}{|1-t|^{3/2}}>0\quad (|t|<1).
\]
Nevertheless the canonical Hardy kernel on the **whole pentablock is not a complete Nevanlinna--Pick kernel**: its restriction to the axis already fails the necessary positivity test. Along the axis the sharp diagonal growth and its induced kernel metric are
\[
S(|a|^2)\sim\frac{\pi/2}{(1-|a|^2)^{3/2}},\qquad
\partial_a\partial_{\overline a}\log S(|a|^2)
\sim\frac{3/2}{(1-|a|^2)^2}\quad(|a|\uparrow1).
\]
Thus a naturally defined three-dimensional Hardy space has an explicit, zero-free arcsine-weighted one-dimensional quotient, but the global kernel cannot have complete Pick interpolation.

## Assumptions and scope

The pentablock is
\[
\mathcal P=\{(A_{21},\operatorname{tr}A,\det A): A\in M_2(\mathbb C),\ \|A\|_{\mathrm{op}}<1\}.
\]
Let \(m_3\) be normalized Haar probability on \(\mathbb T^3\), and let \(\mu=\Psi_*m_3\) for
\[
\Psi(\xi,\lambda,\eta)=\left(\frac{\xi(\lambda-\eta)}2,\lambda+\eta,\lambda\eta\right).
\]
The canonical \(H^2(\mathcal P)\) is the closure of coordinate polynomials in \(L^2(\mu)\), with its holomorphic realization. The axis \((a,0,0)\) belongs to \(\mathcal P\) for every \(|a|<1\), witnessed by the contractive nilpotent matrix with only its \((2,1)\)-entry equal to \(a\). The restriction space is equipped with the quotient norm, i.e., the infimum of the ambient squared norm over all extensions with the same restriction. Every assertion is for the specified canonical measure, not for arbitrary Hardy-space constructions on the same domain.

## Proof

**1. Exact orthogonality and axis moments.** On the boundary parametrization, a coordinate monomial \(a^n s^j p^\ell\) pulls back to
\[
2^{-n}\xi^n(\lambda-\eta)^n(\lambda+\eta)^j(\lambda\eta)^\ell.
\]
The \(\xi\)-Haar integral annihilates its inner product with \(a^m\) unless \(m=n\). When \(m=n\), simultaneous rotation \((\lambda,\eta)\mapsto(e^{i\theta}\lambda,e^{i\theta}\eta)\) annihilates this inner product unless \(j+2\ell=0\). Since \(j,\ell\ge0\), the only surviving monomial is \(a^n\) itself. Consequently the \(a^n\) are pairwise orthogonal and their closed span is orthogonal to the closed span of all remaining coordinate monomials.

Writing \(\lambda/\eta=e^{i\theta}\), we have \(|(\lambda-\eta)/2|^2=\sin^2(\theta/2)\). This random variable has the arcsine law on \((0,1)\). Therefore, for every integer \(n\ge0\),
\[
\|a^n\|_{H^2(\mathcal P)}^2
=\frac1\pi\int_0^1\frac{s^n}{\sqrt{s(1-s)}}\,ds
=\frac{\Gamma(n+1/2)}{\sqrt\pi\,\Gamma(n+1)}
=\frac{\binom{2n}{n}}{4^n}.
\]
These identities prove the asserted minimum-extension coefficient norm, first for polynomials and then for their completion. Conversely every square-summable coefficient sequence in that norm produces an ambient holomorphic function depending only on \(a\), so the restriction is onto. The same moment identity identifies the quotient space with the analytic \(L^2\)-space for the rotationally invariant disk measure with uniform angular component and arcsine squared radius.

**2. Exact reproducing kernel.** The normalized monomials \(a^n/\|a^n\|\) form an orthonormal basis of this quotient. Their kernel is the stated power series \(S(t)\). Its coefficients satisfy
\[
\frac{4^{n+1}/\binom{2n+2}{n+1}}{4^n/\binom{2n}{n}}=\frac{2(n+1)}{2n+1}.
\]
Consequently \(S(0)=1\) and
\[
2t(1-t)S'(t)=(1+2t)S(t)-1.
\]
Direct substitution shows that the displayed arcsine expression satisfies this analytic initial-value equation, proving the closed formula on \(|t|<1\). The reciprocal central-binomial generating identity is classical; its geometric realization here is the point of the calculation.

**3. Quantitative zero-freeness.** Set \(H(t)=(1-t)^{3/2}S(t)\). From the closed formula,
\[
H(t)=\sqrt{1-t}+\sqrt t\,\arcsin\sqrt t,
\qquad H'(t)=\frac{\arcsin\sqrt t}{2\sqrt t}.
\]
Hence \(H(t)=1+\sum_{n\ge1}d_nt^n\), where
\[
d_n=\frac1{2n(2n-1)}\frac{\binom{2n-2}{n-1}}{4^{n-1}}>0.
\]
The coefficients are summable with \(\sum_{n\ge1}d_n=H(1)-1=\pi/2-1<1\). For every \(|t|<1\),
\[
\operatorname{Re}H(t)\ge1-\sum_{n\ge1}d_n|t|^n
\ge2-\pi/2>0.
\]
Since \(1-t\ne0\) on the disk, this proves the lower bound and zero-freeness.

**4. Complete-Pick obstruction.** At the origin the axis kernel is normalized, \(S(0)=1\) and \(S(a\overline0)=1\), and it is irreducible and nonvanishing. The standard normalized complete-Pick necessity states that \(1-1/S(a\overline b)\) must be positive definite if \(S\) is a complete Pick kernel. But the first three coefficients give
\[
S(t)=1+2t+\frac83t^2+O(t^3),\qquad
1-\frac1{S(t)}=2t-\frac43t^2+O(t^3).
\]
A radial positive-definite analytic kernel on the disk has nonnegative Taylor coefficients, as follows by isolating each angular Fourier coefficient in its finite Gram forms. The negative quadratic coefficient contradicts positivity. The complete Pick property passes to restrictions, so the full pentablock Hardy kernel cannot be complete Pick.

**5. Sharp boundary metric.** The formula for \(H\) extends continuously to the real endpoint with \(H(1)=\pi/2\), giving \(S(t)\sim(\pi/2)(1-t)^{-3/2}\) as \(t\uparrow1\). Differentiating \(H\) shows \(H'(t)\to\pi/4\), and \(H''(t)=O((1-t)^{-1/2})\). Therefore, for real \(t\uparrow1\),
\[
\frac{d}{dt}\log S(t)+t\frac{d^2}{dt^2}\log S(t)
=\frac{3/2}{(1-t)^2}+o((1-t)^{-2}).
\]
This is exactly the stated pulled-back kernel metric, because \(t=|a|^2\).

## Verification

The standalone `CHECK.py` uses exact rational Laurent-polynomial torus inner products to check the monomial orthogonality and central-binomial moments at finite orders, independently evaluates the series and closed kernel, checks the negative complete-Pick coefficient and evaluates the boundary metric numerically. The saved script passed 734 assertions. These finite computations do not prove the general theorem; the proof above supplies the all-order arguments. Run with `python CHECK.py` and an installed `mpmath` package.

## Relationship to prior work

Su and Tomar (arXiv:2610.17729, first submitted 13 October 2026) define this canonical pentablock Hardy space, establish its two orthogonal decompositions in Proposition 2.2, and express the embedded kernel as an abstract projection in Proposition 3.5; Proposition 3.6 gives a boundary growth lower bound. Those general structural statements are the essential starting point, but the inspected text does not evaluate the axis kernel, identify its arcsine radial norm, establish its zero-free estimate, quantify its axial metric, or decide its complete-Pick status. Pal and Tomar (arXiv:2606.00850) analyze a Toeplitz corona problem via admissible kernels, rather than this canonical kernel. The reciprocal central-binomial generating function was known long before this work (Sprugnoli and earlier treatments) and is not presented as new. Alpay and Jorgensen (arXiv:1212.1564) study a different binomial-coefficient kernel on the nonnegative integers. The complete-Pick positivity criterion is classical.

## Limitations

The zero-free statement applies to **pairs of points on the first-coordinate axis**, not to the full three-dimensional kernel. No claim is made that the one-variable generating identity or the complete Pick criterion is new. The asymptotic concerns approach to \(|a|=1\) along the axis, not general boundary directions of the pentablock. Publication-priority verification is not independent and cannot rule out a differently titled earlier calculation of this natural slice.

## References

1. G. Su and N. Tomar, *Hardy Spaces and Toeplitz operators on the Pentablock*, arXiv:2610.17729 (first version, 13 October 2026). https://arxiv.org/abs/2610.17729
2. S. Pal and N. Tomar, *A Toeplitz corona theorem for the pentablock and applications*, arXiv:2606.00850 (30 May 2026). https://arxiv.org/html/2606.00850v1
3. D. Alpay and P. Jorgensen, *Reproducing kernel Hilbert spaces generated by the binomial coefficients*, arXiv:1212.1564 (2012). https://arxiv.org/abs/1212.1564
4. R. Sprugnoli, *Sum of reciprocals of the central binomial coefficients*, Integers 6 (2006), A27; classical generating-series identity discussed at https://planetmath.org/generatingfunctionforthereciprocalcentralbinomialcoefficients
5. G. Marx, *The Complete Pick Property and Reproducing Kernel Hilbert Spaces*, 2014; discussion of normalized kernel characterizations. https://vtechworks.lib.vt.edu/items/c02381a1-4169-42ad-811b-a90146fdd8ef
