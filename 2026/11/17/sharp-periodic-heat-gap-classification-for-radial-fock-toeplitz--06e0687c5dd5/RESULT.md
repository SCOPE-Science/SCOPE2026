# Sharp periodic heat-gap classification for radial Fock Toeplitz operators

## Finding

Let \(d\ge1\), let \(P>0\), and let \(g:\mathbb R\to\mathbb R\) be continuous and \(P\)-periodic. On the standard Fock space \(\mathcal F^2(\mathbb C^d)\) with Gaussian measure \(\pi^{-d}e^{-|z|^2}\,dz\), consider the bounded self-adjoint Toeplitz operator \(T_f\) with \(f(z)=c+g(|z|)\), where \(c\in\mathbb R\). For \(t>0\), define the one-dimensional heat average
\[
(H_tg)(x)=\frac1{\sqrt{4\pi t}}\int_{\mathbb R}e^{-(x-y)^2/(4t)}g(y)\,dy,
\qquad m_t=\min_{0\le x\le P}(H_tg)(x),\quad M_t=\max_{0\le x\le P}(H_tg)(x).
\]
Then the exact Fredholm essential spectrum and the full cluster interval of the Berezin transform at infinity are
\[
\boxed{\sigma_{\mathrm{ess}}(T_f)=[c+m_{1/8},c+M_{1/8}],}
\qquad
\boxed{\mathrm{Clust}_{|z|\to\infty}\widetilde f(z)=[c+m_{1/4},c+M_{1/4}].}
\]
In particular, \(\liminf_{|z|\to\infty}\widetilde f(z)=c+m_{1/4}\). If \(g\) is nonconstant, the four endpoints satisfy
\[
m_{1/8}<m_{1/4}<M_{1/4}<M_{1/8}.
\]
Thus there is a strictly positive Berezin lower limit with a negative essential spectral point **exactly** for offsets
\[
\boxed{-m_{1/4}<c<-m_{1/8}.}
\]
For constant \(g\), this interval is empty. The entire statement, including its offset interval, is dimension-independent.

There is also a sharp quantitative statement. If \(g\) is \(L\)-Lipschitz, then the width of the false-positive offset interval obeys
\[
\boxed{0\le m_{1/4}-m_{1/8}\le\frac{\sqrt2-1}{\sqrt{2\pi}}L.}
\]
The coefficient is best possible uniformly over the periods and continuous periodic profiles: the periodic triangular profiles \(g_P(x)=L\operatorname{dist}(x,P\mathbb Z)\) approach equality as \(P\to\infty\). For any nonconstant periodic profile, the left inequality is strict.

An explicit two-frequency example is \(g(x)=\cos x+\cos(2x)\). At both needed heat times,
\[
m_t=-e^{-4t}-\tfrac18e^{2t},\quad t\in\{1/8,1/4\}.
\]
Taking \(c=2/3\) gives \(c+m_{1/8}\approx-0.1003672\) but \(c+m_{1/4}\approx0.0926971\).

## Assumptions and scope

The dimension \(d\) is any fixed positive integer; the period \(P\) need not be minimal. A continuous periodic profile is automatically bounded and uniformly continuous. The Fock inner product is normalized so that the normalized coherent vector at \(z\) has squared mass density \(\pi^{-d}e^{-|w-z|^2}\), and \(\widetilde f(z)=\langle T_fk_z,k_z\rangle\). The essential spectrum means the set of \(\lambda\) for which \(T_f-\lambda I\) is not Fredholm. The additional Lipschitz assertion assumes only global Lipschitz continuity with constant at most \(L\ge0\); it does not impose a bound on the amplitude or the period.

## Proof

**Step 1: Exact radial diagonalization.** Write \(m\ge0\) for total monomial degree. Rotational invariance makes distinct normalized monomials orthogonal under multiplication by \(f\). All monomials of total degree \(m\) have one eigenvalue
\[
\lambda_m=c+\frac1{\Gamma(m+d)}\int_0^\infty g(\sqrt s)\,s^{m+d-1}e^{-s}\,ds.
\]
Its multiplicity is the finite integer \(\binom{m+d-1}{d-1}\). If \(S_k\) has the gamma law with integer shape \(k=m+d\) and unit scale, \(\lambda_m=c+\mathbb E[g(\sqrt{S_k})]\).

**Step 2: Uniform heat limit for the eigenvalues.** Since \(S_k\) is a sum of \(k\) independent mean-one exponential variables, the central limit theorem and the identity
\[
\sqrt{S_k}-\sqrt k=\frac{S_k-k}{\sqrt{S_k}+\sqrt k}
\]
show that \(\sqrt{S_k}-\sqrt k\Rightarrow N(0,1/4)\). For each fixed trigonometric polynomial approximating the continuous periodic function \(g\) uniformly, convergence of characteristic functions yields uniform convergence over all center phases \(x\) of the expectations of its translates. Uniform approximation transfers this to \(g\). In particular,
\[
\lambda_m=c+(H_{1/8}g)(\sqrt{m+d})+o(1)\qquad (m\to\infty).
\]

**Step 3: Entire essential spectrum.** The sequence \(\sqrt{m+d}\) increases to infinity and has successive gaps tending to zero. For every \(x\in[0,P]\), choosing \(m_j\) closest to \((jP+x)^2-d\) gives \(\sqrt{m_j+d}\equiv x+o(1)\pmod P\). Hence the limit-point set of \((\lambda_m)\) is exactly \(c+(H_{1/8}g)([0,P])\), the indicated compact interval. For a diagonal operator with finite multiplicity at each degree, its Fredholm essential spectrum is exactly this tail-limit set: outside it all but finitely many diagonal differences are uniformly bounded away from zero; inside it a weakly null sequence of distinct monomial eigenvectors provides a Weyl sequence. This proves the first box.

**Step 4: Berezin cluster interval.** Let \(Z\) have density \(\pi^{-d}e^{-|Z|^2}\) on \(\mathbb C^d\). By unitary invariance, for any \(R>0\),
\[
\widetilde f(Re_1)=c+\mathbb E\,g(|Re_1+Z|).
\]
As \(R\to\infty\), one has \(|Re_1+Z|-R\to\operatorname{Re}Z_1\) almost surely. Moreover, its absolute value is bounded by \(|Z|\); the uniform continuity of \(g\) and bounded convergence give
\[
\widetilde f(Re_1)=c+\mathbb E\,g(R+\operatorname{Re}Z_1)+o(1)
=c+(H_{1/4}g)(R)+o(1).
\]
Here \(\operatorname{Re}Z_1\sim N(0,1/2)\). The error is independent of the phase of \(R\), since the same modulus-of-continuity bound works for every translate. Positive radii attain all phases modulo \(P\), so the complete Berezin cluster interval is as claimed.

**Step 5: Strict separation and offset classification.** Gaussian kernels form a convolution semigroup: \(H_{1/4}=H_{1/8}\circ H_{1/8}\). Each positive-time periodic heat kernel is everywhere strictly positive on one period. If \(g\) is nonconstant, \(h=H_{1/8}g\) is nonconstant: its nonzero Fourier modes are multiplied by strictly positive factors \(e^{-(1/8)(2\pi k/P)^2}\) and cannot all vanish. Consequently, every value of \(H_{1/8}h\) is strictly between \(\min h\) and \(\max h\). The new heat output is itself nonconstant by the same Fourier argument. This gives all three strict inequalities. Positivity of the Berezin liminf is equivalent to \(c>-m_{1/4}\), whereas failure of essential positivity is equivalent to \(c<-m_{1/8}\); their intersection is precisely the open interval displayed. Constant profiles have equal heat endpoints and no such offsets.

**Step 6: Sharp Lipschitz gap.** Let \(N\sim N(0,1)\) and couple the two heat distributions using the same \(N\). For any \(x\),
\[
|(H_{1/4}g)(x)-(H_{1/8}g)(x)|
\le L\left(\frac1{\sqrt2}-\frac12\right)\mathbb E|N|
=\frac{\sqrt2-1}{\sqrt{2\pi}}L.
\]
Taking minima gives the upper bound; the lower bound follows by positive-kernel averaging. To prove sharpness, fix \(L>0\) and let \(g_P(x)=L\operatorname{dist}(x,P\mathbb Z)\). This periodic triangular wave is symmetric and rises from \(0\) to \(LP/2\) on the half-period. For each \(t>0\), \(H_tg_P\) retains this symmetry and is increasing on \([0,P/2]\): its derivative solves the one-dimensional heat equation on the half-period with zero boundary values and nonnegative initial derivative \(L\), so positivity of the Dirichlet heat semigroup applies (or approximate the corners smoothly and pass to a limit). Therefore \(m_t=(H_tg_P)(0)=L\mathbb E\operatorname{dist}(\sqrt{2t}N,P\mathbb Z)\). As \(P\to\infty\), dominated convergence gives \(m_t\to L\sqrt{2t}\mathbb E|N|\), and the difference at times \(1/4\) and \(1/8\) tends to the stated upper constant.

**Step 7: Explicit two-frequency example.** Heat flow gives \(H_tg(x)=e^{-t}\cos x+e^{-4t}\cos(2x)\). With \(u=\cos x\), this is \(2e^{-4t}u^2+e^{-t}u-e^{-4t}\). Its unconstrained minimum occurs at \(u=-e^{3t}/4\), which lies strictly inside \([-1,1]\) at both specified times. Substitution yields the stated exact minimum and the signs at \(c=2/3\).

## Verification

A standalone standard-library script `checker.py` verifies finite trigonometric lower bounds, samples of the gamma-eigenvalue heat asymptotic, samples of the two-dimensional coherent-state Gaussian integral, and the sign of the explicit offset. It reports 4013 successful finite assertions. These are diagnostics only; Steps 1–7 provide the infinite-dimensional proof and sharpness argument. Run with `python3 checker.py` in the directory containing this document.

## Relationship to prior work

Esmeral and Maximenko, arXiv:1505.07906, Proposition 6.5, already prove general heat-kernel approximation for the one-dimensional radial Fock eigenvalue sequence; that ingredient is not new. Looi, arXiv:2603.10879, Theorem 2.2, Remark 2.5 and Proposition 3.8, prove the Berezin-liminf counterexample for a single cosine profile (with an adjustable frequency and offset) and in all dimensions. Fulsche, arXiv:2405.15496, proves general limit-operator criteria for Fock essential positivity and the Berezin criterion in vanishing-oscillation classes. The present result assembles an exact **all-continuous-periodic** phase diagram with two complete endpoint cluster intervals and adds a **globally optimal Lipschitz envelope** on the false-positive interval. No stronger publication-priority assertion is made; the general eigenvalue heat limit and the cosine mechanism are credited in full.

## Limitations

The periodicity and continuity assumptions are essential to the stated full-interval and strict-separation proof. The theorem does not classify arbitrary bounded radial profiles, the Bergman analogue, general Gaussian Fock scalings, or fixed-period optimal Lipschitz constants. For arbitrary profiles the limiting heat ranges may be more complicated. The coefficient bound is a best possible supremum across varying periods, not a claim of attainment at a fixed finite period. The published ingredients are strong, and an earlier unlocated corollary combining them may overlap this classification; independent publication-priority and mathematical audits are not claimed.

## References

- Sam Looi, *The Berezin liminf criterion fails for radial Toeplitz operators*, arXiv:2603.10879v1 (first public March 11, 2026), https://arxiv.org/abs/2603.10879 .
- Kevin Esmeral and Egor A. Maximenko, *Radial Toeplitz operators on the Fock space and square-root-slowly oscillating sequences*, arXiv:1505.07906v1 (May 29, 2015), https://arxiv.org/abs/1505.07906 .
- Robert Fulsche, *Essential positivity for Toeplitz operators on the Fock space*, arXiv:2405.15496v2 (first public May 24, 2024), https://arxiv.org/abs/2405.15496 .
