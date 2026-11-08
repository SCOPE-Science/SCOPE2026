# Regular-polygon finite-step rigidity and an explicit spectral rate for Fourier Kaczmarz recovery

## Finding
Let \(m\ge2\). For distinct \(\zeta_1,\ldots,\zeta_m\in\mathbb T\) and strictly positive masses \(p_1,\ldots,p_m\) summing to one, set \(\mu=\sum_{j=1}^m p_j\delta_{\zeta_j}\). Apply the *unrelaxed, sequential* Kaczmarz algorithm to the measurement vectors \(e_n(\zeta)=\zeta^n\) in \(H=L^2(\mu)\), starting at the first measurement \(n=0\). Denote the approximation after processing \(e_0,\ldots,e_N\) by \(x_N\).

Put \(w_j=\overline{\zeta_j}\) and define the explicit monic polynomial
\[
R_\mu(t)=\sum_{j=1}^m p_j\prod_{k\ne j}(t-w_k).
\]
All its \(m-1\) complex zeros lie strictly inside \(\mathbb D\). With \(r_\mu\) the largest modulus of a zero, the **exact worst-case exponential error rate** is
\[
\lim_{N\to\infty}\left(\sup_{\|x\|=1}\|x-x_N\|\right)^{1/N}=r_\mu<1.
\]
The limit is \(0\) precisely when \(\mu\) is the uniform measure on a rotated regular \(m\)-gon. Moreover, **uniform exact finite-step recovery occurs if and only if that exceptional condition holds**: in that case \(x_{m-1}=x\) for every \(x\in H\), and no earlier common cutoff works. For every other positive atomic measure, \(x_N\ne x\) for some \(x\in H\) at every finite \(N\).

For two atoms \(\zeta_j=e^{i\theta_j}\) with masses \(p,1-p\), the complete finite-time error is explicitly
\[
\sup_{\|x\|=1}\|x-x_N\|=\left(1-4p(1-p)\sin^2\frac{\theta_1-\theta_2}{2}\right)^{N/2}\quad(N\ge1).
\]

## Assumptions and scope
The complex Hilbert-space inner product is linear in its first entry; the rank-one orthogonal projection onto the unit vector \(u\) is \(P_u x=\langle x,u\rangle u\). All atoms are distinct, all masses strictly positive, and \(m\) is finite and at least two. The sequence begins at \(e_0\) and visits exponents in the fixed order \(0,1,2,\ldots\). We consider exact data, no relaxation, and worst-case error over unit-norm target vectors. These hypotheses are essential to the uniform-rate and rigidity statements; no infinite-support or noisy-data extension is asserted.

## Proof
Write \(U f(\zeta)=\zeta f(\zeta)\) and \(u=e_0\equiv1\), so \(U\) is unitary, \(\|u\|=1\), and \(e_n=U^n u\). Let \(Q=I-P_u\). The Kaczmarz error \(x-x_N\) is the product of orthogonal complements of the successive measurement lines:
\[
E_Nx:=x-x_N=\bigl(U^NQU^{-N}\bigr)\cdots\bigl(UQU^{-1}\bigr)Qx.
\]
Define \(M=u^\perp\) and \(B=(QU^{-1})|_M:M\to M\); the codomain is \(M\) by the leading \(Q\). The elementary telescoping product identity gives
\[
E_N=U^N(QU^{-1})^NQ=U^N B^NQ.
\]
Since \(Q\) maps the unit sphere onto the closed unit ball of \(M\), and \(U^N\) is unitary, we have the **exact finite-time identity**
\[
\|E_N\|=\|B^N\|\quad(N\ge1).
\]

To compute the characteristic polynomial, use the orthonormal coordinate representation of \(L^2(\mu)\), where \(U^{-1}=D=\operatorname{diag}(w_1,\ldots,w_m)\) and \(u=(\sqrt{p_1},\ldots,\sqrt{p_m})\). In an orthonormal basis whose first vector is \(u\), the lower-right \((m-1)\)-dimensional block of \(D\) is \(B\). Expansion of the complementary principal minor, or the adjugate identity, gives
\[
\det(tI_M-B)=\langle\operatorname{adj}(tI-D)u,u\rangle
=\sum_{j=1}^m p_j\prod_{k\ne j}(t-w_k)=R_\mu(t).
\]
The polynomial is monic because \(\sum p_j=1\).

Because \(B\) is a compression of the unitary \(D\), \(\|B\|\le1\). Suppose \(Bx=\lambda x\) with \(|\lambda|=1\) and \(0\ne x\in M\). Then equality in \(\|QDx\|\le\|Dx\|\) forces \(Dx\in M\), hence \(Dx=Bx=\lambda x\). The distinct eigenspaces of diagonal \(D\) are coordinate lines, none orthogonal to \(u\) because \(p_j>0\). This contradiction proves every zero of \(R_\mu\) lies strictly inside \(\mathbb D\). The finite-dimensional spectral-radius formula (Gelfand's formula) and \(\|E_N\|=\|B^N\|\) establish the stated exponential-rate limit.

It remains to classify \(r_\mu=0\). This is equivalent to \(B\) being nilpotent and therefore to the polynomial identity \(R_\mu(t)=t^{m-1}\). Let \(P(t)=\prod_{k=1}^m(t-w_k)\) and \(W=\prod_{k=1}^mw_k\). At \(t=w_j\), polynomial equality gives
\[
p_jP'(w_j)=w_j^{m-1}.
\]
For unimodular, distinct roots, direct conjugation of the product \(P'(w_j)=\prod_{k\ne j}(w_j-w_k)\) yields
\[
\overline{P'(w_j)}=\frac{(-1)^{m-1}}{w_j^{m-2}W}P'(w_j).
\]
Conjugate the preceding equality for \(p_jP'(w_j)\), use that \(p_j\) is real and \(|w_j|=1\), and cancel the nonzero derivative: this gives \(w_j^m=(-1)^{m-1}W\) for every \(j\). Thus the \(m\) distinct nodes are **all** solutions of one equation \(t^m=c\), a rotated regular \(m\)-gon. For them \(P(t)=t^m-c\) and \(P'(w_j)=m w_j^{m-1}\), so the same evaluation equation forces \(p_j=1/m\). Conversely the uniform regular polygon satisfies \(R_\mu(t)=t^{m-1}\) by the logarithmic derivative of \(t^m-c\). The resulting nilpotent \((m-1)\)-dimensional operator obeys \(B^{m-1}=0\), hence \(E_{m-1}=0\). No \(N<m-1\) can work for every target, since a nonzero vector perpendicular to the \(N+1<m\) measurement vectors remains completely unchanged by all those updates. Outside the exceptional case, \(B\) has a nonzero eigenvalue and no positive power vanishes, so there is no uniform finite cutoff.

For \(m=2\), \(M\) is one-dimensional and \(B\) is the scalar \(p w_2+(1-p)w_1\). Its modulus squared equals \(1-4p(1-p)\sin^2((\theta_1-\theta_2)/2)\), giving the displayed positive-\(N\) error formula; at \(N=0\), \(\|E_0\|=1\).

## Verification
A standalone `verify.py` checks the polynomial-minor identity and the full finite-time operator identity for deterministic random distinct supports, tests root inclusion and nilpotence for regular supports, checks a rational two-atom example exactly, and tests the two-atom rate formula numerically. For the initial stage \(N=0\), the exact worst-case error is \(1\) (including in the zero-rate exceptional case). Execute `python3 verify.py` with NumPy and SymPy installed. The code is a finite consistency check; the full theorem is proved above. The separately recorded execution result and limitations appear in `VERIFICATION.md`.

## Relationship to prior work
Alpay–Berner–Weber (arXiv:2508.13861v1, §§1,3–4) prove qualitative effectiveness of Kaczmarz iteration in Hilbert modules and for stationary sequences, including finite-dimensional settings. The classical Haller–Szwarc 2005 paper and the Herr–Weber 2017 work give general Kaczmarz effectivity and Fourier reconstruction results. Those conclusions do not in themselves determine the weighted-root polynomial, the exact asymptotic spectral rate, or the exceptional finite-step cutoff for a finite atomic unitary orbit. The recently released Berner–Herr–Jorgensen (arXiv:2611.03358v2, particularly Lemma 5.7) already proves that a related finite-atomic compressed-unitary operator has spectral radius strictly less than one and invokes Gelfand’s formula for decay; this qualitative/spectral-radius part is **not claimed as original**. Its Theorem 4.1 proves absolute convergence for finite atomic measures. The present contribution is the explicit polynomial determining that spectral radius and the if-and-only-if characterization of zero rate and exact finite-step recovery, which those results do not state. General results on finite products of projections, compressed unitaries, and orthogonal polynomials on the unit circle could subsume portions of the derivation; this is a residual priority risk, not a claim that the method is new.

## Limitations
The formula identifies the exact **asymptotic exponential factor** in arbitrary finite dimension; it does not imply a dimension-independent prefactor \(\|E_N\|\le C r_\mu^N\) when \(B\) has defective eigenvalues. The two-atom formula is an exact finite-time statement. The argument does not address infinite or continuous spectral measures, perturbed data, randomized orders, or complex unit-circle measures with zero or negative weights. Independent mathematical and priority review is not yet performed.

## References
1. D. Alpay, C. Berner, E. S. Weber, *The Kaczmarz Algorithm in Hilbert \(C^*\)-modules*, arXiv:2508.13861v1 (first public August 19, 2025), https://arxiv.org/abs/2508.13861.
2. R. Haller and R. Szwarc, *Kaczmarz algorithm in Hilbert space*, Studia Mathematica 169 (2005), 123–132, DOI: 10.4064/sm169-2-2.
3. J. E. Herr and E. S. Weber, *Fourier Series for Singular Measures*, Axioms 6 (2017), article 7, DOI: 10.3390/axioms6020007.
4. C. Berner, J. E. Herr, P. E. T. Jorgensen, *Frame Properties of Effective Stationary Sequences*, arXiv:2611.03358v1 (November 2, 2026), https://arxiv.org/abs/2611.03358 (supporting context only; not the motivating dated source).
