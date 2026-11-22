# An infinite staircase of attracting high-amplitude two-cycles in a symmetric sine-delay map

## Finding
For the real map
\[
F_{p,a,g}(x,y,z)=(y,\sin z,px+ay-g\sin z),
\qquad A=p+a-g,\quad B=a+g-p,
\]
assume \(a,g>0\), \(|A|<1\) and \(B>0\). Every primitive real period-two orbit is antipodal and is represented, uniquely up to time shift, by
\[
P_d=(\sin d,-\sin d,d),\quad -P_d,\qquad d>0,\quad d=B\sin d.
\]
In particular, this is a complete period-two census even when \(p\ne0\). For the natural singular-Jacobian subfamily \(p=0\), fix any \(A=a-g\in(-1,1)\) and vary \(B=a+g>|A|\). For every integer \(k\ge1\) there is an exactly determined open interval \((B_k,R_k(A))\) on which the \(k\)-th positive sine lobe supports exactly one asymptotically attracting primitive period-two orbit. The second orbit in that lobe, when present, is never attracting. Outside this interval neither orbit of that lobe attracts. There are infinitely many such windows, increasingly narrow:
\[
B_k=m_k-\frac{1}{2m_k}+O(m_k^{-3}),\qquad
R_k(A)=m_k+\frac4{m_k}+O_A(m_k^{-2}),\qquad
R_k(A)-B_k=\frac9{2m_k}+O_A(m_k^{-2}),
\quad m_k=(2k+\tfrac12)\pi.
\]
The unique attracting orbit on the principal lobe exists for \(1<B<R_0(A)\). These results do not assert global attraction or a classification of periods beyond two.

## Assumptions and scope
All states and parameters are real. A primitive period-two orbit consists of two distinct points exchanged by \(F\), counted only once under swapping the points. The census hypotheses are \(a>0\), \(g>0\), \(B=a+g-p>0\), and \(|A=p+a-g|<1\). For the sharp sink windows further take \(p=0\), equivalently the everywhere-singular Jacobian subfamily of this map, and hold \(A=a-g\) fixed. Then \(a=(B+A)/2>0\), \(g=(B-A)/2>0\) whenever \(B>|A|\). Hyperbolic attraction means all eigenvalues of the two-step derivative have modulus strictly below one; equality at a boundary is not classified as a sink.

Write \(I_k=(2k\pi,(2k+1)\pi)\), \(k\ge0\). For each \(k\ge1\), define the unique \(q_k\in(2k\pi,(2k+\tfrac12)\pi)\) by
\[
q_k\cot q_k=1,\qquad B_k=q_k/\sin q_k.
\]
Let \(m_k=(2k+\tfrac12)\pi\). For each \(k\ge0\), let \(r_k(A)\in(m_k,(2k+1)\pi)\) be the unique root of
\[
r_k\cot r_k+A\cos r_k=-2,
\qquad R_k(A)=r_k(A)/\sin r_k.
\]
Define \(B_0=1\); no \(q_0>0\) is needed.

## Proof
**1. Exact elimination and antipodal rigidity.** Let \(P=(x,y,z)\), \(Q=(X,Y,Z)\) and \(F(P)=Q\), \(F(Q)=P\). The first two coordinates force \(x=\sin z\), \(y=\sin Z\). The remaining coordinates are
\[
z=a\sin z+(p-g)\sin Z,\qquad Z=(p-g)\sin z+a\sin Z.
\]
With \(s=(z+Z)/2\) and \(d=(z-Z)/2\), these become
\[
s=A\sin s\cos d,\qquad d=B\cos s\sin d.
\]
Because \(|A|<1\), the first identity implies \(s=0\): otherwise \(|s|\le|A||\sin s|<|s|\). Thus \(z=d\), \(Z=-d\), and \(d=B\sin d\). Swapping orbit points changes the sign of \(d\), so take \(d>0\). Conversely every positive solution yields the displayed orbit, which is primitive because \(d\ne0\). The same elimination with \(d=0\) shows that the origin is the only fixed point in this parameter strip.

**2. Exact positive-root census.** Since \(B>0\), every positive solution belongs to some \(I_k\), where \(\sin d>0\). Put \(H(d)=d/\sin d\). Its derivative has the sign of \(1-d\cot d\), and
\[
\frac{d}{dd}(d\cot d)=\frac{\sin d\cos d-d}{\sin^2d}<0\quad(d>0,\ \sin d\ne0).
\]
On \(I_0\), \(d\cot d\) decreases from \(1\) to \(-\infty\), so \(H\) increases strictly from \(1\) to infinity. This lobe has one positive root exactly for \(B>1\). On every \(I_k\), \(k\ge1\), \(d\cot d\) decreases from \(+\infty\) to \(-\infty\), crossing \(1\) once at \(q_k\). Therefore \(H\) decreases from infinity to \(B_k\) and then increases to infinity: there are zero, one double/tangential, or two distinct roots according as \(B<B_k\), \(B=B_k\), or \(B>B_k\). Since \(B_k>2k\pi\), only finitely many lobes contribute for fixed \(B\). This exhausts every real primitive two-cycle.

**3. Floquet criteria on the rank-two sheet.** At \(p=0\), the one-step Jacobian at both \(P_d\) and \(-P_d\) is the same matrix, since \(\cos(-d)=\cos d=:c\):
\[
J_c=\begin{pmatrix}0&1&0\\0&0&c\\0&a&-gc\end{pmatrix}.
\]
The two-step Floquet matrix is \(J_c^2\), and its one-step characteristic polynomial is
\[
\lambda(\lambda^2+gc\lambda-ac).
\]
The elementary quadratic Schur inequalities give strict attraction precisely when
\[
|ac|<1,\qquad 1-(a-g)c=1-Ac>0,\qquad 1-(a+g)c=1-Bc>0.
\]
The middle inequality always holds because \(|A|<1\). If \(c>0\), the remaining inequalities reduce to \(Bc<1\): indeed \(0<2ac=Bc+Ac<1+|A|<2\). If \(c<0\), the last inequality is automatic, and attraction is equivalent to \(ac>-1\). The same criterion also covers \(c=0\), when the return derivative is nilpotent and the orbit is superattracting.

For \(d\in I_k\) with \(d<m_k\), the sign of \(1-Bc=1-d\cot d\) changes exactly at \(q_k\) (at \(0\) for the principal lobe). Hence each left-of-fold branch is unstable, and every branch with \(q_k<d\le m_k\) is attracting. For \(d>m_k\), \(c<0\), and the attracting condition becomes
\[
2ac=d\cot d+A\cos d>-2.
\]
The function on the left is strictly decreasing for \(d>m_k\), because
\[
\frac{d}{dd}(d\cot d+A\cos d)
=\frac{\sin d\cos d-d}{\sin^2d}-A\sin d
\le -d+|A|<-1/2.
\]
It starts at zero and tends to \(-\infty\) at the right endpoint, so it crosses \(-2\) once, at \(r_k(A)\). Because \(H\) increases strictly for \(d>q_k\), this proves the exact sink interval \(B_k<B<R_k(A)\), and the analogous principal interval. At the fold the one-step characteristic polynomial has \(\lambda=-1\) and a two-step multiplier \(+1\); at the exit \(ac=-1\), and the nonzero one-step multipliers are a complex unit pair: indeed \(a=1/|c|>1\) and \(g/a=1-A/a\in(0,2)\). Both endpoints are therefore nonhyperbolic and excluded from the strict sink interval. No other period-two orbit exists to evade this conclusion.

**4. High-lobe asymptotics.** Write \(m=m_k\). Since \(\cot(m+v)=-\tan v\), the fold equation for \(q_k=m-v\) is \((m-v)\tan v=1\), giving \(v=m^{-1}+O(m^{-3})\) and
\[
B_k=(m-v)\sec v=m-\frac1{2m}+O(m^{-3}).
\]
Likewise \(r_k=m+w\) solves \((m+w)\tan w+A\sin w=2\). Hence \(w=2/m+O_A(m^{-2})\), so
\[
R_k(A)=(m+w)\sec w=m+\frac4m+O_A(m^{-2}).
\]
Subtracting gives \(R_k(A)-B_k=9/(2m)+O_A(m^{-2})\). Since adjacent midpoints are separated by \(2\pi\) whereas these windows have width tending to zero, the sufficiently high windows are pairwise disjoint. The leading coefficient \(9/2\) does not depend on \(A\).

## Verification
The accompanying `checker.py` independently evaluates the symbolic determinant, characteristic polynomial and exact antipodal orbit identity. It then samples \(A=-3/4,0,3/4\) and lobes \(1\) through \(30\), checks the predicted Floquet stability within each window, checks an unstable left branch and the region above the upper window, and compares the last five sampled widths with \(9/(2m_k)\). These computations corroborate the algebra but do not substitute for the monotonicity and asymptotic proofs above.

To reproduce from the extracted package: `python checker.py` with Python 3, NumPy, SciPy and SymPy installed. The expected final line is `all finite diagnostics PASS`.

## Relationship to prior work
The 2024 Almatroud–Abu Hammad–Dababneh–Diabi–Ouannas–Khennaoui–Alshammari paper defines this three-dimensional sine map and analyzes the origin, numerical bifurcations and synchronization. The 2017 Mammeri map and the 2023 Rajagopal–Kanagaraj–Volos–Karthikeyan extension include closely related sine maps and investigate fixed points, numerical attractors, and networks. These prior works are not claimed as new. An earlier quantitative treatment of this exact family already classifies the small-gain antipodal period-two region \(B<\pi\) and its special nilpotent resonance; the present contribution concerns the infinitely many higher sine lobes (first high-lobe fold \(B_1>2\pi\)), the complete corresponding root census, and sharp non-overlapping high-amplitude attracting windows with the universal \(9/(2m_k)\) width law. We make no priority claim for standard Schur inequalities or elementary sine-root analysis in isolation.

## Limitations
The complete positive-root census requires \(|A|<1\) and \(B>0\). The sharp attracting-window classification is proved on the natural noninvertible subfamily \(p=0\), not for arbitrary \(p\). This is a period-two theorem; it neither classifies longer cycles nor implies that trajectories outside the exhibited local basins must diverge or converge to the origin. Nonhyperbolic boundary orbits are counted, but no nonlinear center-manifold classification at their boundary multipliers is asserted. The numerical checks are finite and cannot prove global uniqueness; that follows from analytic elimination and monotonicity. Equivalent unindexed work remains possible; no independent audit has been performed.

## References
1. O. A. Almatroud, M. Abu Hammad, A. Dababneh, L. Diabi, A. Ouannas, A. A. Khennaoui and S. Alshammari, *Multistability, Chaos, and Synchronization in Novel Symmetric Difference Equation*, Symmetry 16 (2024), 1093, first published 2024-08-22, https://doi.org/10.3390/sym16081093.
2. M. Mammeri, *Symmetry and Periodic-Chaos in 3-D Sinusoid Discrete Maps*, Bulletin of Mathematical Analysis and Applications 9 (2017), 1–8, https://emis.muni.cz/journals/BMAA/repository/docs/BMAA9-1-1.pdf.
3. K. Rajagopal, S. Kanagaraj, C. Volos and A. Karthikeyan, *Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems*, Symmetry 15 (2023), 780, https://doi.org/10.3390/sym15040780.
