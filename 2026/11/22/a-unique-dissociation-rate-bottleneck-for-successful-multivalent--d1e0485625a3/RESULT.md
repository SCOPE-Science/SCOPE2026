# A unique dissociation-rate bottleneck for successful multivalent attachment

## Finding

Let a homogeneous bond-number chain begin with one bond and be absorbed either upon losing all bonds or upon reaching a specified stabilization threshold. Holding the association rate fixed while changing the dissociation rate produces a **unique interior conditional-time maximum if and only if the stabilization threshold is at least four**. In the large-threshold limit the maximizer approaches equal rates with a sharp quadratic correction, and the maximum exceeds its equal-rate value by a finite universal amount.

Precisely, for an integer \(m\ge2\), association rate \(\lambda>0\), and dissociation rate \(\mu\ge0\), let \(T\) be the time to absorption starting from state \(1\), and \(S\) the event of reaching state \(m\) before state \(0\). Set \(\rho=\mu/\lambda\) and \(n=m-1\). Then

\[
\mathbb E[T\mid S]=\frac{1}{\lambda}\,
\frac{\sum_{k=0}^{n-1}(k+1)(n-k)\rho^k}
{\sum_{k=0}^{n}\rho^k}.
\]

For \(m=2\) this mean is strictly decreasing in \(\rho\ge0\); for \(m=3\) it is strictly decreasing for \(\rho>0\) and has zero right derivative at \(\rho=0\). For every \(m\ge4\) it increases strictly on \((0,\rho_m)\) and decreases strictly on \((\rho_m,\infty)\), where \(\rho_m\in(0,1)\) is its **only** positive critical point and global maximizer. In addition,

\[
\lim_{m\to\infty}m^2(1-\rho_m)=15,
\qquad
\lim_{m\to\infty}\lambda\left(
\mathbb E[T\mid S]_{\rho=\rho_m}
-\mathbb E[T\mid S]_{\rho=1}\right)=\frac58.
\]

For the first nonmonotone threshold, \(m=4\), the maximizing rate ratio is the only positive root of
\[
1-10\rho^2-8\rho^3-3\rho^4=0,
\qquad \rho_4=0.2828147640150715\ldots .
\]

## Assumptions and scope

The finite continuous-time chain has states \(0,1,\dots,m\), with \(0\) and \(m\) absorbing. Every interior state \(i=1,\dots,m-1\) jumps to \(i+1\) with rate \(\lambda\) and to \(i-1\) with rate \(\mu\). All holding times are exponential; there are no transitions that skip a bond number, spatial degrees of freedom, rebinding after failure, or bond-count-dependent rates. The association rate is held fixed while the dissociation rate varies, a distinction essential to the optimization result. The success probability is positive for all finite \(\rho\ge0\), so the conditional mean is well-defined, including \(\mu=0\). The physical threshold is a model-defined bond-count criterion, not an observed microscopic ligand number.

## Proof

**1. Laplace transform and conditional mean.** Write \(Q\) for the \(n\times n\) transient subgenerator on states \(1,\dots,n\), and \(D_n(s)=\det(sI-Q)\). Absorption at \(m\) occurs from state \(n\), so the defective Laplace transform \(\Phi_1(s)=\mathbb E_1[e^{-sT}\mathbf1_S]\) is \(\lambda[(sI-Q)^{-1}]_{1,n}\). The corresponding tridiagonal cofactor equals \(\lambda^{n-1}\), whence
\[
\Phi_1(s)=\frac{\lambda^n}{D_n(s)},\qquad
\mathbb E[T\mid S]=\frac{D'_n(0)}{D_n(0)}.
\]
The equality for the mean follows by differentiating \(\Phi_1(s)/\Phi_1(0)\) at \(s=0\). In particular \(\Pr(S)=\Phi_1(0)\). Set \(x=\rho\) and \(u=s/\lambda\). Writing \(D_n(s)=\lambda^nP_n(u,x)\), the tridiagonal determinant recurrence is
\[
P_0=1,\quad P_1=1+x+u,\quad
P_j=(1+x+u)P_{j-1}-xP_{j-2}.
\]
Induction, including differentiation of this recurrence at \(u=0\), gives
\[
P_n(0,x)=B_n(x):=\sum_{k=0}^{n}x^k,
\qquad
\partial_uP_n(0,x)=A_n(x):=
\sum_{k=0}^{n-1}(k+1)(n-k)x^k.
\]
Thus the displayed conditional mean is \(A_n(x)/(\lambda B_n(x))\), and the success probability is \(1/B_n(x)\). The latter strictly decreases with \(x\) for \(n\ge1\).

**2. Exact derivative signs and a unique optimizer.** Let
\[
R_n(x)=A'_n(x)B_n(x)-A_n(x)B'_n(x).
\]
By multiplying the two finite sums and collecting the coefficient of \(x^j\), one obtains, for every integer \(n\ge1\),
\[
[x^j]R_n(x)=
\begin{cases}
\dfrac{(j+1)(j+2)(j+3)(n-j-2)}6,
&0\le j\le n-2,\\[5pt]
\dfrac{(j-2n)(j-2n-1)(j-2n+1)(j-n+2)}6,
&n-1\le j\le2n-2.
\end{cases}
\]
For clarity, in the first range this is the finite sum \(\sum_{i=0}^{j+1}(2i-j-1)(i+1)(n-i)\); in the second range it is the analogous sum over \(j+1-n\le i\le n-1\). Each evaluates to the corresponding factored polynomial by the ordinary formulas for sums of powers up to degree three. For \(n=1\), \(R_1=-1\). For \(n=2\), \(R_2=-4x-2x^2\). For every \(n\ge3\), coefficients in degrees \(0,\dots,n-3\) are strictly positive, the degree \(n-2\) coefficient is zero, and all coefficients in degrees \(n-1,\dots,2n-2\) are strictly negative. Descartes' rule of signs therefore gives at most one positive real root. Since \(R_n(0)=n-2>0\) and its leading coefficient is negative, there is exactly one, with a strict sign change. Since \(\frac{d}{dx}(\lambda\mathbb E[T\mid S])=R_n/B_n^2\), this proves all global sign classifications. Finally, the reciprocity \(A_n(1/x)=x^{-(n-1)}A_n(x)\) and \(B_n(1/x)=x^{-n}B_n(x)\) imply \(\lambda\mathbb E[T\mid S](1/x)=x\lambda\mathbb E[T\mid S](x)\). Differentiating at \(x=1\) gives a strictly negative derivative there, so the unique maximizer for \(n\ge3\) lies in \((0,1)\).

**3. Large-threshold location and peak gain.** Denote \(f_m(x)=\lambda\mathbb E[T\mid S]\) with \(n=m-1\). Direct differentiation of the two displayed finite polynomials and elementary power-sum identities yield the **exact** derivatives
\[
f_m(1)=\frac{m^2-1}{6},\qquad
f'_m(1)=-\frac{m^2-1}{12},\qquad
f''_m(1)=\frac{-m^4+20m^2-19}{180}.
\]
The eigenvalues of the transient tridiagonal matrix, divided by \(\lambda\), are
\[
\theta_j(x)=1+x-2\sqrt{x}\cos\frac{j\pi}{m},
\qquad 1\le j\le m-1,
\]
so \(f_m(x)=\sum_{j=1}^{m-1}\theta_j(x)^{-1}\) for \(x>0\). For any fixed \(C>0\), uniformly on \(1-C/m^2\le x\le1\) for sufficiently large \(m\), the inequalities \(\theta_j(x)\ge c_Cj^2/m^2\), \(|\theta'_j(x)|\le C_Cj^2/m^2\), and \(|\theta''_j(x)|+|\theta'''_j(x)|\le C_C\) hold with positive constants depending only on \(C\). The third derivative of \(\theta_j^{-1}\) is a sum of terms proportional to \((\theta'_j)^3/\theta_j^4\), \(\theta'_j\theta''_j/\theta_j^3\), and \(\theta'''_j/\theta_j^2\). Summing their bounds gives \(\sup|f'''_m(x)|=O_C(m^4)\) on this window. Taylor's theorem consequently gives, for each fixed \(c>0\),
\[
\frac{f'_m(1-c/m^2)}{m^2}
=-\frac1{12}+\frac{c}{180}+o(1).
\]
For any fixed \(\epsilon\in(0,15)\), the derivative at \(1-(15-\epsilon)/m^2\) is negative and that at \(1-(15+\epsilon)/m^2\) is positive for all large \(m\). The already proved unique root therefore satisfies \(m^2(1-\rho_m)\to15\). A second Taylor expansion, using the same uniform derivative bound, yields
\[
f_m(\rho_m)-f_m(1)
=\frac{15}{12}-\frac{15^2}{360}+o(1)
=\frac58+o(1),
\]
which proves the remaining asymptotic statement. No finite-size numerical inference is used in the argument.

## Verification

The accompanying `check.py` uses only the Python standard library. Run `python3 check.py` in the directory containing this document. It verifies integer-polynomial identities through transient dimension \(22\), independently solves the conditional backward problem over exact rational fields in transient dimensions \(1\) through \(9\), and locates selected critical points with 70-digit decimal arithmetic. The expected final line begins with `PASS: 545`. These computations verify examples and proof algebra, not the infinite family or asymptotic limit on their own.

For \(m=4\), the rate ratio \(\rho_4\approx0.2828147640\) gives dimensionless conditional mean \(\lambda\mathbb E[T\mid S]\approx3.1551534451\), compared with \(3\) at zero dissociation. The success probability at the optimum is approximately \(0.7218029493\). The numerical series for \(m^2(1-\rho_m)\) approaches \(15\) and the dimensionless excess above the equal-rate mean approaches \(5/8\).

## Relationship to prior work

Wu (2026, arXiv:2611.01293v1), particularly the conditional Doob-transform theorem, Proposition V.2 and Figure 3, already establishes the bond-number model and **illustrates** a nonmonotone conditional stabilization time versus dissociation-to-association ratio for selected thresholds. That phenomenon and the general time-backward equation are prior work. The present result instead proves the exact threshold \(m=4\) for the onset of such a maximum, uniqueness for every allowable threshold, strict monotonicity on both sides, and the large-threshold constants \(15\) and \(5/8\); those assertions are not supplied by the numerical illustration or the general backward equation alone.

Ashcroft, Traulsen and Galla (2015, arXiv:1504.04249) and older Karlin–McGregor-type theory supply general spectral and first-passage constructions for birth–death processes. The determinant/spectral starting point is therefore not claimed as new. The novel mathematical content assessed here is the all-threshold derivative sign classification and its sharp finite-size optimizer asymptotics. Related work on fixation-time nonmonotonicity in population processes demonstrates the wider existence of such effects, but does not establish these constants for the fixed-association-rate homogeneous adhesion chain.

## Limitations

The result is exact only for homogeneous forward/backward rates and conditioning on successful attainment of \(m\) from state \(1\). It makes no claim for state-dependent receptor accessibility, cooperativity, spatially coupled binding, nonexponential bond lifetimes, or experimentally inferred bond counts. The success probability decreases as dissociation increases; a smaller conditional time at strong dissociation does **not** imply a greater yield of successful attachments. The asymptotic gain \(5/(8\lambda)\) is absolute; the relative gain tends to zero because typical conditional times scale like \(m^2/\lambda\) near balanced rates. The prior-art assessment is literature-based, not an independent priority certification.

## References

1. H. Wu, *From First Bond to Stable Adhesion: Multivalent Bond Stabilization in Receptor-Mediated Endocytosis*, arXiv:2611.01293v1 (first publicly submitted 31 October 2026), https://arxiv.org/html/2611.01293v1 .
2. P. Ashcroft, A. Traulsen, T. Galla, *When the mean is not enough: Calculating fixation time distributions in birth-death processes*, Phys. Rev. E **92**, 042154 (2015), arXiv:1504.04249, https://arxiv.org/pdf/1504.04249 .
3. *On conditional passage time structure of birth-death processes*, J. Appl. Probab. **21**, 10–21 (1984), https://doi.org/10.2307/3213660 .
4. *Time to fixation in changing environments* (2021), https://pmc.ncbi.nlm.nih.gov/articles/PMC8570778/ .
