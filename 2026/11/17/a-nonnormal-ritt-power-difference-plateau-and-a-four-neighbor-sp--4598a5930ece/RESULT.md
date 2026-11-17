# A nonnormal Ritt power-difference plateau and a four-neighbor spectral-spacing law

## Finding
Fix \(c>0\) and \(0<q<1\). On the complex Hilbert space \(\mathcal H=\bigoplus_{j\ge1}\mathbb C^2\) let
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
T=\bigoplus_{j\ge1}\bigl[(1-q^j)I_2+cq^jN\bigr].
\]
The operator \(T\) is a strongly stable, power-bounded Ritt operator; \(I-T\) belongs to every Schatten ideal. It is a contraction exactly when \(c\le2-q\). Define its normalized Ritt power-difference sequence
\[
D_n=n\|T^n-T^{n+1}\|,\qquad n\ge1.
\]
With
\[
F_c(t)=te^{-t}\left(\sqrt{1+\frac{c^2(t-1)^2}{4}}+\frac{c|t-1|}{2}\right),\quad t>0,
\qquad H_{c,q}(u)=\max_{k\in\mathbb Z}F_c(uq^k),\quad 1\le u\le q^{-1},
\]
its **entire set of finite subsequential limits** is the nondegenerate interval
\[
\boxed{\operatorname{Cluster}(D_n)=[m_{c,q},M_c],\quad
m_{c,q}=\min_{1\le u\le q^{-1}}H_{c,q}(u),\quad M_c=\max_{t>0}F_c(t).}
\]
There are exactly two strict local maxima of \(F_c\): at \(t_-(c)\in(0,1)\) and \(t_+(c)>1\), separated by the strict cusp minimum at \(t=1\). The **unique global maximum** is at \(t_+\), and \(1<t_+<(3+\sqrt5)/2\). These points are the unique roots in their indicated intervals of
\[
\frac1{t_-}-1-\frac{c}{\sqrt{4+c^2(t_--1)^2}}=0,\qquad
\frac1{t_+}-1+\frac{c}{\sqrt{4+c^2(t_+-1)^2}}=0.
\]
There are unique \(a_c\in(0,t_-)\) and \(b_c\in(t_+,\infty)\) satisfying
\(F_c(a_c)=F_c(b_c)=e^{-1}\). The lower endpoint obeys the **exact three-regime classification**
\[
\boxed{
\begin{array}{ll}
m_{c,q}<e^{-1},&0<q<a_c/b_c,\\
m_{c,q}=e^{-1},&a_c/b_c\le q\le\min\{a_c,b_c^{-1}\},\\
m_{c,q}>e^{-1},&\min\{a_c,b_c^{-1}\}<q<1.
\end{array}}
\]
In particular the equality interval has positive length for **every** \(c>0\): the asymptotic lower power-difference norm is exactly flat at \(e^{-1}\) over a whole interval of geometric spectral gap ratios. For \(c=1\), the plateau endpoints are approximately \(0.143654226\) and \(0.340749433\), wholly within the contraction regime.

The minimum defining \(m_{c,q}\) is an exact **four-neighbor** one-variable problem: for \(u\in[1,q^{-1}]\) set \(k_\pm=\lfloor \log(t_\pm/u)/\log q\rfloor\). Then
\[
H_{c,q}(u)=\max_{\sigma\in\{-,+\}}
\big\{F_c(uq^{k_\sigma}),F_c(uq^{k_\sigma+1})\big\}.
\]
No infinite spectral scan is necessary to evaluate the lower endpoint.

## Assumptions and scope
The norm is the Hilbert-space operator norm on the standard orthogonal sum of complex two-dimensional Euclidean blocks. The shear parameter \(c\) is any fixed **strictly positive real number**; the ratio \(q\) lies strictly between zero and one. The normalized difference uses \(T^n-T^{n+1}\), not a shifted time convention. All limits are taken over positive integer \(n\to\infty\); \(c\) and \(q\) remain fixed. The Schatten assertion allows every real \(p>0\), including quasi-norm exponents. The formula does not claim that \(m_{c,q}\) is elementary outside the stated plateau.

## Proof
**1. Ritt, compactness, and contraction.** Write \(\varepsilon_j=q^j\) and \(r_j=1-\varepsilon_j\). Each block is \(A_j=r_jI_2+c\varepsilon_jN\). Its powers are
\[
A_j^n=r_j^nI_2+n c\varepsilon_jr_j^{n-1}N.
\]
Since \(n\varepsilon(1-\varepsilon)^{n-1}\le1\) for \(0<\varepsilon<1\), \(\sup_n\|T^n\|\le1+c\). Every fixed block tends to zero; density of finite-support vectors proves strong stability. The resolvent is
\[
(z-A_j)^{-1}=(z-r_j)^{-1}I_2+c\varepsilon_j(z-r_j)^{-2}N.
\]
For \(|z|>1\), \(|z-r_j|>\varepsilon_j\) and \(|z-1|\le|z-r_j|+\varepsilon_j\), giving
\[
|z-1|\|(z-T)^{-1}\|\le2+2c.
\]
The spectrum lies in \([0,1]\), so this is the Ritt resolvent criterion. The singular values of \(I_2-A_j=\varepsilon_j(I_2-cN)\) are \(\varepsilon_j G_c\) and \(\varepsilon_j/G_c\), where \(G_c=\sqrt{1+c^2/4}+c/2\). Consequently
\[
\|I-T\|_{\mathcal S_p}^p=(G_c^p+G_c^{-p})\frac{q^p}{1-q^p}<\infty\quad(p>0).
\]
Finally the positivity of \(I_2-A_j^*A_j\) is equivalent to \(c\varepsilon_j\le1-r_j^2\), or \(c\le 2-\varepsilon_j\). Simultaneously for every \(j\), this is exactly \(c\le2-q\).

**2. Exact singular norm and uniform scalar envelope.** Direct multiplication yields
\[
nA_j^n(I_2-A_j)=
\begin{pmatrix}
 n\varepsilon_jr_j^n&n c\varepsilon_jr_j^{n-1}((n+1)\varepsilon_j-1)\\
 0&n\varepsilon_jr_j^n
\end{pmatrix}.
\]
The norm of a real upper triangular matrix with equal positive diagonal \(d\) and upper entry \(b\) is \(\sqrt{d^2+b^2/4}+|b|/2\). Thus, **exactly**, with \(t_{j,n}=n\varepsilon_j\),
\[
D_n=\sup_{j\ge1}n\varepsilon_jr_j^n
\left[\sqrt{1+\frac{c^2((n+1)\varepsilon_j-1)^2}{4r_j^2}}+
\frac{c|(n+1)\varepsilon_j-1|}{2r_j}\right].
\]
For \(t_{j,n}\) in a fixed compact subinterval of \((0,\infty)\), the summand tends **uniformly** to \(F_c(t_{j,n})\), since \(r_j=1-t_{j,n}/n\) and \(r_j^n\to e^{-t_{j,n}}\). To control all blocks, as \(t\downarrow0\) the diagonal is at most \(t\) and the upper entry at most \(ct(2+t)\). As \(t\uparrow\infty\), for \(n\ge2\), \(r_j^{n-1}\le e^{-t/2}\), so both entries are bounded by \((t+ct(2+t))e^{-t/2}\). These tails vanish uniformly. It follows that
\[
\boxed{D_n-\sup_{j\ge1}F_c(nq^j)\longrightarrow0.}
\]
The finite checker independently compares the displayed exact matrix entries and the scalar norm formula. Its tests are supplementary; uniformity follows analytically from these bounds.

**3. Critical points and global peak.** Write
\[
\log F_c(t)=\log t-t+\operatorname{arsinh}\bigl(c|t-1|/2\bigr).
\]
On each of \((0,1)\) and \((1,\infty)\), its derivative is strictly decreasing, with respective formulas shown in the finding and one root on each interval. At \(t=1\) the one-sided derivatives are \(-c/2\) and \(+c/2\), so the point is a strict cusp minimum, not a maximum. For \(0<t<1\) set \(\delta=1-t\). Since the shear factor is unchanged by \(t\mapsto2-t\),
\[
\log\frac{F_c(2-t)}{F_c(t)}=
\log\frac{1+\delta}{1-\delta}-2\delta>0,
\]
by \(\operatorname{arctanh}(\delta)>\delta\). Hence the right local maximum is strictly larger than the left one and is the unique global maximum. The right derivative becomes negative at \((3+\sqrt5)/2\), proving the stated bound on \(t_+\).

**4. Full cluster interval and four-neighbor reduction.** Write \(\log_{1/q}n=J_n+\theta_n\) with \(J_n\in\mathbb Z\), \(0\le\theta_n<1\). Then \(nq^j=q^{j-J_n-\theta_n}\). The uniform scalar envelope and its vanishing tails show
\[
D_n-H_{c,q}(q^{-\theta_n})\longrightarrow0.
\]
The increments of \(\log_{1/q}n\) tend to zero while this sequence diverges, so its fractional parts \(\theta_n\) are dense in the unit interval. The geometric-grid maximum is a continuous, periodic function of \(\theta\), since the tails of \(F_c(q^{k-\theta})\) vanish uniformly in \(\theta\). Therefore the cluster set is precisely its connected image \([m_{c,q},M_c]\). The upper endpoint is \(M_c\) because some grid phase contains \(t_+\). Since \(t_+\) is the unique global maximum, phases not containing \(t_+\) yield strictly smaller envelope values; hence \(m_{c,q}<M_c\).

Within each of the intervals \((0,1)\) and \((1,\infty)\), \(F_c\) is strictly increasing up to its respective maximum and strictly decreasing thereafter. Thus its largest value over a geometric grid occurs among the two grid points bracketing each of \(t_-\) and \(t_+\). This gives exactly the four-neighbor formula in the finding.

**5. Sharp plateau.** Because \(F_c\) decreases to zero at both ends, is strictly larger than \(F_c(1)=e^{-1}\) at its two maxima, and has no other local extrema, its superlevel set is
\[
\{t>0:F_c(t)\ge e^{-1}\}=[a_c,b_c],
\]
with equality only at \(a_c,1,b_c\). If \(q<a_c/b_c\), the logarithmic mesh gap exceeds the logarithmic length of \([a_c,b_c]\); a phase of the grid avoids the interval completely, so \(m_{c,q}<e^{-1}\). If \(q\ge a_c/b_c\), every grid phase meets that interval, so \(m_{c,q}\ge e^{-1}\). When additionally \(q\le\min\{a_c,b_c^{-1}\}\), take the phase containing \(1\); its two adjacent lattice points are \(q\le a_c\) and \(q^{-1}\ge b_c\), hence the grid maximum equals exactly \(e^{-1}\). Finally, if \(q>\min\{a_c,b_c^{-1}\}\), then \(q>a_c/b_c\), so every phase has a point strictly inside \((a_c,b_c)\). Were its maximum at most \(e^{-1}\), every such interior point would have to equal \(1\). But then either the adjacent point \(q\) lies in \((a_c,1)\) or the adjacent point \(q^{-1}\) lies in \((1,b_c)\), a contradiction. Thus \(m_{c,q}>e^{-1}\), completing the trichotomy.

## Verification
The included standard-library file `checker.py` reproduces the exact triangular matrix norm, evaluates the two critical points, checks that the four-neighbor expression equals a much larger geometric-grid scan, compares finite-time block defects with the claimed phase envelope, and samples all three plateau regimes. Its output is `JORDAN_RITT_DIAGNOSTICS_OK 3465` and `JORDAN_RITT_PLATEAU_DIAGNOSTICS_OK 3489`. The proof is analytical; finite tests do not certify all parameters or infinite subsequences. Root decimals in the finding are illustrative rather than part of the exact definition.

## Relationship to prior work
Borichev, Gomilko, and Tomilov, *Beurling–Kato theory, Hardy–Sobolev calculus and Ritt operators* (arXiv:2607.10507, first submitted 11 July 2026), develop discrete Ritt criteria and Hardy–Sobolev functional calculus. Badea, *Iterates of Ritt operators close to the identity* (arXiv:2609.27458), studies sampled powers, displacement gaps, and Ritt characterizations. These works provide the Ritt framework, not the present full cluster interval and sharp plateau in nonnormal two-dimensional blocks.

The public work *Inverse spectral-spacing law for normalized Ritt power differences* (2026) already establishes an interval and an inverse gap law for **normal diagonal** Ritt contractions with a single-peaked exponential profile. That diagonal theorem does not imply the present two-peaked nonnormal profile or its positive-length \(e^{-1}\) plateau; the normal inverse-gap ratio is strictly monotone, in contrast to the present flat lower endpoint. The public work *The sharp affine Jordan norm pencil and its scaled \(q\)-spectral-set transition* supplies finite Jordan-pencil norm information, but does not analyze geometric direct sums, integer-time cluster sets, or the sharp plateau. The exact \(2\times2\) norm itself is not claimed as new.

## Limitations
Only exact geometric block scales and a fixed real shear \(c>0\) are considered; arbitrary nonnormal Ritt operators, uneven spectral gaps and higher Jordan blocks are not classified. The lower endpoint outside the plateau is given by an exact finite-candidate one-variable minimization, not an elementary closed formula. Numerical tests are not infinite proofs. No independent peer review or publication-priority guarantee is asserted.

## References
1. A. Borichev, A. Gomilko, Yu. Tomilov, *Beurling–Kato theory, Hardy–Sobolev calculus and Ritt operators*, arXiv:2607.10507 (v1: 11 July 2026), https://arxiv.org/abs/2607.10507.
2. C. Badea, *Iterates of Ritt operators close to the identity*, arXiv:2609.27458 (v1: 23 September 2026), https://arxiv.org/abs/2609.27458.
3. *Inverse spectral-spacing law for normalized Ritt power differences* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-inverse-spectral-spacing-law-for-normalized-ritt-power-differenc--e574be857180.
4. *The sharp affine Jordan norm pencil and its scaled q-spectral-set transition* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-sharp-affine-jordan-norm-pencil-and-its-scaled-q-spectral-se--00a25760cd57.
