# Exact cyclic Turán mass for the separated five-site support \(\{0,\pm1,\pm3\}\)

## Finding
For every integer \(N\ge7\), let \(G_N=\mathbb Z/N\mathbb Z\) and \(\Omega_N=\{0,\pm1,\pm3\}\). With counting measure, define
\[
T_N=\max\Big\{\sum_{x\in G_N}f(x): f(0)=1,\ \operatorname{supp}f\subseteq\Omega_N,\ f\colon G_N\to\mathbb C\text{ positive definite}\Big\}.
\]
The exact sharp values and all **real-even** optimizers are as follows.

If \(N\) is even, then \(\boxed{T_N=2}\), attained by \(f(0)=1\), \(f(\pm1)=1/2\), and \(f(\pm3)=0\).

If \(N\) is odd, put
\[
\delta=\frac{\pi}{N},\quad C=\cos\delta,\quad r=\left\lfloor\frac{N+1}{6}\right\rfloor,\quad u=\cos\frac{2\pi r}{N},\quad w=C-u.
\]
Then \(u,w>0\), and the sharp value is
\[
\boxed{T_N=\frac{(1+C)(1-u)(1-w)}{Cuw}>2.}
\]
The **unique real-even optimizer** has Fourier polynomial
\[
\boxed{P_N(\theta)=\frac{(\cos\theta+C)(\cos\theta-u)(\cos\theta-w)}{Cuw}}
=1+2a_N\cos\theta+2b_N\cos3\theta,
\]
where
\[
\boxed{b_N=\frac1{8Cuw},\qquad a_N=\frac{3-4(C^2-Cu+u^2)}{8Cuw}.}
\]
Its only nonzero values outside zero are \(f(\pm1)=a_N\), \(f(\pm3)=b_N\). One has \(b_N>0\) and \(a_N\ge0\), with \(a_N=0\) **exactly when \(3\mid N\)**. At those odd multiples of three,
\[
T_N=1+\sec\frac{3\pi}{N}.
\]
Across odd moduli, \(T_N=2+9\pi^2/(2N^2)+O(N^{-3})\). The claimed uniqueness is in the real-even class; no classification of complex-valued optimizer faces is asserted.

## Assumptions and scope
A function \(f\) is positive definite if \(\sum_{x,y\in G_N}c_x\overline{c_y}f(x-y)\ge0\) for every complex family \((c_x)\). Equivalently, all Fourier eigenvalues \(\sum_xf(x)e^{2\pi ijx/N}\) are nonnegative real numbers. Every such \(f\) satisfies \(f(-x)=\overline{f(x)}\); its real part is positive definite (the Fourier eigenvalues are replaced by symmetric averages) and preserves both \(f(0)\) and its total sum. Consequently the maximum over complex-valued functions equals that over real-even ones. Since \(N\ge7\), the five stated residues are pairwise distinct. Every real-even candidate is uniquely parameterized by \(a=f(1)=f(-1)\) and \(b=f(3)=f(-3)\), and is feasible precisely when
\[
1+2a\cos(2\pi j/N)+2b\cos(6\pi j/N)\ge0\quad\text{for every }0\le j<N.
\]
The objective is \(1+2(a+b)\). The admissible set is compact since positive definiteness and \(f(0)=1\) imply \(|f(x)|\le1\).

## Proof
**Even moduli.** At the Fourier site \(j=N/2\), both odd cosines equal \(-1\). Hence \(1-2(a+b)\ge0\), so the mass is at most \(2\). The polynomial \(1+\cos\theta\) is nonnegative at every site and has mass \(2\). Complex candidates reduce to real-even candidates as above.

**Factorization and feasibility at odd moduli.** Fix an odd \(N\ge7\) and the quantities \(\delta,C,r,u,w\) above. Write \(x=\cos\theta\). The cubic \((x+C)(x-u)(x-w)\) has no quadratic term because \(u+w=C\), and constant term \(Cuw\). Since \(T_3(x)=4x^3-3x=\cos3\theta\), the displayed Chebyshev expansion follows exactly, provided \(u,w>0\).

To verify positivity and establish that no sampled cosine lies strictly between \(u\) and \(w\), distinguish the three classes of odd \(N\). If \(N=6m+1\), then \(2\pi r/N=\pi/3-\delta/3\). Writing \(x_j=\cos(2\pi j/N)\), one has \(x_{r+1}<w<u=x_r\). Indeed
\[
\cos(\pi/3+5\delta/3)<\cos(\pi/3+\delta)<C-\cos(\pi/3-\delta/3)<\cos(\pi/3-\delta/3),
\]
where \(C=\cos(\pi/3-\delta)+\cos(\pi/3+\delta)\); the final inequality follows from \(\cos(\pi/3-\delta/3)>1/2\) and \(C<1\). If \(N=6m+3\), then \(r=m\), \(u=\cos(\pi/3-\delta)\), and \(w=\cos(\pi/3+\delta)=x_{r+1}\). If \(N=6m+5\), then \(r=m+1\), \(u=\cos(\pi/3+\delta/3)\), and \(u<w<x_{r-1}\). For the last inequality, \(w<C-\cos(\pi/3+\delta)=\cos(\pi/3-\delta)<\cos(\pi/3-5\delta/3)=x_{r-1}\); also
\[
w-u=C-2u=\sin(\delta/3)\big(\sqrt3-2\sin(2\delta/3)\big)>0.
\]
All expressions are valid for \(m\ge1\). Thus \(u,w\) are positive and either coincide with consecutive positive-frequency cosine values or lie strictly between such consecutive values. The sampled cosines range over \([-C,1]\), because the minimum cosine on an odd cyclic grid is \(-C\). Hence \((x+C)(x-u)(x-w)\ge0\) at every sampled \(x\), proving positive definiteness of the constructed function.

**Matching positive two-contact dual certificate.** The constructed polynomial vanishes at the Fourier sites with cosines \(u\) and \(-C\). Set \(v=T_3(u)=4u^3-3u<0\) and \(D=\cos(3\delta)\). Here \(0<D<C\), since \(0<3\delta<\pi/2\), and \(0<u<\sqrt3/2\). Define
\[
\lambda=\frac{-(C-D)}{Cv-Du},\qquad \mu=\frac{-(u-v)}{Cv-Du}.
\]
The denominator is strictly negative, so both weights are strictly positive, and direct substitution gives
\[
\lambda u-\mu C=-1,\qquad \lambda v-\mu D=-1.
\]
For any feasible real-even pair \((a,b)\), the weighted sum of its two sampled Fourier inequalities gives
\[
0\le\lambda(1+2au+2bv)+\mu(1-2aC-2bD)
=\lambda+\mu-2(a+b).
\]
Our polynomial vanishes at both sites, so equality is attained, proving global optimality. Any other real-even maximizer must vanish at both since \(\lambda,\mu>0\). The coefficient matrix of those two equations has determinant \(Cv-Du<0\), so \((a,b)\) is uniquely fixed. Substituting \(x=1\) in the factored polynomial gives the displayed formula for \(T_N\).

**Parity and the third-harmonic transition.** On an odd grid the polynomial \(1+\cos\theta\) is *strictly* positive at all sites. Slightly increasing its first Fourier coefficient preserves feasibility and raises its mass, proving \(T_N>2\). For the optimum, elementary algebra gives
\[
\frac{a_N}{b_N}=3\sin^2\delta-4(u-C/2)^2.
\]
The angle defining \(u\) belongs to the closed interval \([\pi/3-\delta,\pi/3+\delta]\). The two endpoints give \(|u-C/2|=(\sqrt3/2)\sin\delta\), and an interior angle gives a strict inequality. The defining angle is an endpoint precisely when \(N=6m+3\); thus \(a_N=0\) exactly for odd multiples of three, and is positive otherwise. At that resonance \(P_N(\theta)=1+\cos3\theta/D\), giving \(T_N=1+1/D\). Finally, set \(u=1/2+O(\delta)\), \(C=1-\delta^2/2+O(\delta^4)\), \(uw=1/4+O(\delta^2)\) uniformly across the three odd residue classes. Writing
\[
T_N=\frac{1+C}{C}\left(1+\frac{1-C}{uw}\right)
\]
and expanding yields \(T_N=2+\tfrac92\delta^2+O(\delta^3)\).

## Verification
Run the included standalone standard-library program with `python3 check.py`. It checks the exact factorized expression, all Fourier inequalities, positive dual weights and dual equalities, the three modular root-bracketing cases, the resonance formula, and strict first-coefficient signs for every integer \(7\le N\le2001\). For every \(7\le N\le101\), it additionally enumerates every two-constraint intersection of the real-even linear program and independently finds the same maximum. The recorded run passed 18,055 assertions. Finite tests are corroboration, not a proof for all \(N\); the preceding analytic argument supplies the infinite proof.

## Relationship to prior work
Fu, Li, Wang and Wang (first public 2026-08-16) study the continuous Turán problem for three intervals and a discrete approximation through finite supports in \(\mathbb Z\); their integer-parameter special case identifies a continuous value of \(2\), not this fixed five-site optimization on every finite cyclic group. Kolountzakis and Révész (2003) develop group Turán methods and determine \(T_{\mathbb Z}(\{0,\pm1,\pm(2k+1)\})=2\); the finite-quotient correction for \(\{0,\pm1,\pm3\}\), its exact optimizers and odd-grid residue transition are not given by that infinite-group bound. Published related finite-grid work for \(\{0,\pm1,\pm4\}\) has a different support and modulus-five phenomenon. A published Carathéodory–Fejér result on exactly the same harmonic support \(\{0,\pm1,\pm3\}\) maximizes the *first Fourier coefficient alone*, not their sum; its two active contacts occur in a different region of the cosine grid. These are distinct objectives, not equivalent by simply relabeling coefficients. General finite cyclic Turán and circular-graph theta literature remains a possible source of an older equivalent formulation; global priority is not asserted.

## Limitations
The theorem requires \(N\ge7\), and uniqueness is only in the real-even class; no assertion about uniqueness among all complex-valued positive-definite functions is made. It is specific to \(\{0,\pm1,\pm3\}\) and does not cover larger supports or arbitrary fixed gaps. The literature comparison is bounded and cannot rule out an equivalent older circulant semidefinite, graph-theta, or discretized Turán formulation. Independent mathematical audit has not been performed.

## References
- X.-Y. Fu, Y.-K. Li, W.-J. Wang and X. Wang, *Turán problem on the union of three intervals of equal length*, arXiv:2608.15643v1, first public 2026-08-16, https://arxiv.org/abs/2608.15643.
- M. N. Kolountzakis and Sz. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218v1, first public 2003-12-10, https://arxiv.org/pdf/math/0312218, especially §3.3, Example 3.
- M. N. Kolountzakis and Sz. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1, first public 2003-02-17, https://arxiv.org/pdf/math/0302193.
- *Pentagonal locking and residue-sensitive finite Turán defects for a five-point cyclic support*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-pentagonal-locking-and-residue-sensitive-finite-tur-n-defects-fo--b2ce368d6213/RESULT.md.
- *Exact discrete Carathéodory–Fejér constant for the isolated third harmonic*, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-discrete-carath-odory-fej-r-constant-for-the-isolated-thir--e309f8e59103/RESULT.md.
