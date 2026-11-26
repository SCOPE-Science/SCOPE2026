# An infinite staircase of attracting high-amplitude two-cycles in a symmetric sine-delay map

## Finding
Consider the real map
\[
F_{p,a,g}(x,y,z)=(y,\sin z,px+ay-g\sin z),\qquad A=p+a-g,\quad B=a+g-p.
\]
Suppose \(a,g>0\), \(|A|<1\), and \(B>0\). Every primitive real period-two orbit is antipodal and, up to time shift, is uniquely represented by
\[
P_d=(\sin d,-\sin d,d),\quad -P_d,\qquad d>0,\quad d=B\sin d.
\]
This is a complete period-two census, including for \(p\ne0\).

For the everywhere-singular Jacobian subfamily \(p=0\), fix \(A=a-g\in(-1,1)\) and vary \(B=a+g>|A|\). For each integer \(k\ge1\), the positive sine lobe \(I_k=(2k\pi,(2k+1)\pi)\) contains exactly one **hyperbolically attracting** primitive two-cycle precisely when \(B_k<B<R_k(A)\). Hyperbolic attraction means that all eigenvalues of the two-step derivative lie strictly inside the unit disk. Outside the open window no cycle in that lobe is hyperbolically attracting. At the endpoints the boundary cycles are counted and their linear multipliers are specified below, without asserting their nonlinear stability or instability. With \(m_k=(2k+\tfrac12)\pi\),
\[
 B_k=m_k-\frac{1}{2m_k}+O(m_k^{-3}),\qquad
 R_k(A)=m_k+\frac4{m_k}+O_A(m_k^{-2}),\qquad
 R_k(A)-B_k=\frac9{2m_k}+O_A(m_k^{-2}).
\]
The principal lobe \(I_0=(0,\pi)\) contains exactly one hyperbolically attracting primitive two-cycle for \(1<B<R_0(A)\) and none at other values of \(B\).

## Threshold definitions
For \(k\ge1\), let \(q_k\in(2k\pi,m_k)\) be the unique root of \(q_k\cot q_k=1\), and set \(B_k=q_k/\sin q_k\). Set \(B_0=1\). For \(k\ge0\), let \(r_k(A)\in(m_k,(2k+1)\pi)\) be the unique root of
\[
r_k\cot r_k+A\cos r_k=-2,
\qquad R_k(A)=r_k(A)/\sin r_k(A).
\]

## Proof

**Antipodal rigidity.** Let \(P=(x,y,z)\), \(Q=(X,Y,Z)\), and suppose \(F(P)=Q\), \(F(Q)=P\). The first two coordinates give \(x=\sin z\), \(y=\sin Z\), \(X=y\), and \(Y=x\). The last coordinates then yield
\[
z=a\sin z+(p-g)\sin Z,\qquad Z=(p-g)\sin z+a\sin Z.
\]
For \(s=(z+Z)/2\) and \(d=(z-Z)/2\) these become \(s=A\sin s\cos d\) and \(d=B\cos s\sin d\). The first identity forces \(s=0\) by \(|A|<1\). Thus \(d=B\sin d\), with \(d>0\) after swapping orbit points if necessary. The case \(d=0\) is the origin, the only fixed point under these hypotheses. Substitution verifies the converse and primitivity for \(d>0\).

**Root census.** Put \(H(d)=d/\sin d\) for \(d\in I_k\); these lobes contain every admissible positive root since \(B>0\). The sign of \(H'(d)\) is the sign of \(1-d\cot d\), and
\[
(d\cot d)'=\frac{\sin d\cos d-d}{\sin^2 d}<0.
\]
On \(I_0\), \(H\) increases strictly from \(1\) to infinity. On every higher lobe \(d\cot d\) decreases from \(+\infty\) to \(-\infty\) and is zero at \(m_k\). Thus \(H\) decreases from infinity to its unique nondegenerate minimum at \(q_k\), and then increases to infinity. On that lobe there are zero, one tangential, or two roots according as \(B<B_k\), \(B=B_k\), or \(B>B_k\). Since \(B_k>2k\pi\), only finitely many lobes contribute for fixed \(B\).

**Hyperbolic attraction on \(p=0\).** At the two phases the same one-step Jacobian has rows \((0,1,0),(0,0,c),(0,a,-gc)\), where \(c=\cos d\). The two-step derivative is its square. Its one-step characteristic polynomial is \(\lambda(\lambda^2+gc\lambda-ac)\), so the strict quadratic Schur inequalities are
\[
|ac|<1,\qquad 1-Ac>0,\qquad 1-Bc>0.
\]
The middle inequality always holds. For \(c>0\) the other two reduce to \(Bc<1\), since then \(2ac=Bc+Ac<1+|A|<2\). By \(Bc=d\cot d\), this is the increasing branch of \(H\) up to \(m_k\) (or the whole left half of \(I_0\)). The strictly decreasing branch has a multiplier of modulus greater than one, from the quadratic's negative value at \(-1\). At \(c=0\) all multipliers are zero. For \(c<0\) the criterion is \(2ac=d\cot d+A\cos d>-2\). On the right half-lobe the derivative of this last expression is
\[
\frac{\sin d\cos d-d}{\sin^2d}-A\sin d\le -d+|A|<0.
\]
It decreases from zero to \(-\infty\), giving precisely the threshold \(r_k(A)\) and thus the asserted open windows. Above the threshold the modulus of the product of the two nonzero one-step multipliers exceeds one. At \(q_k\) a one-step multiplier is \(-1\), hence the return has a multiplier \(+1\). At \(r_k\), \(ac=-1\) and \(|gc|=g/a<2\): indeed \(a=1/|c|>1\) and \(g/a=1-A/a\). The two nonzero one-step multipliers are a complex unit pair. These unit-modulus statements do not decide nonlinear stability at equality.

**High-lobe asymptotics.** With \(m=m_k\), the fold has \(q_k=m-v\), where \((m-v)\tan v=1\); this yields \(v=m^{-1}+O(m^{-3})\) and \(B_k=(m-v)\sec v=m-1/(2m)+O(m^{-3})\). At the right boundary \(r_k=m+w\), where \((m+w)\tan w+A\sin w=2\). Since \((m+w)\tan w+A\sin w\ge(m-|A|)w\), first \(w=O(m^{-1})\), and Taylor expansion then gives \(w=2/m+O_A(m^{-2})\). Hence \(R_k=(m+w)\sec w=m+4/m+O_A(m^{-2})\). Subtraction proves the width law. The high-lobe windows are separated: \(R_k=\sqrt{r_k^2+(2-A\sin w)^2}<r_k+9/(2r_k)<m_k+\pi/2+9/(2m_k)<2(k+1)\pi<B_{k+1}\) for \(k\ge1\).

## Verification and limitations
The accompanying `checker.py` contains symbolic checks of the Jacobian determinant, characteristic polynomial, and antipodal orbit identities, and finite numerical tests of threshold locations, strict Floquet stability, off-window branches, and the large-lobe widths. It requires Python 3, NumPy, SciPy, and SymPy. The infinite census and open hyperbolic-attraction windows follow from the proof, not from finite tests. This result does not classify nonlinear stability at unit-modulus boundaries, global basins, or longer periods, and does not extend the stability assertions to \(p\ne0\).

## Relationship to prior work
Almatroud et al. define this map and analyze its equilibrium, numerical bifurcations, and synchronization. Mammeri and Rajagopal et al. study related sine-delay systems. The companion analytic treatment [4] of the same family proves antipodal period-two uniqueness when \(1<B<\pi\) and nonexistence when \(0<B\le1\) in its strip \(|A|\le1\). It gives the same antipodal form on that range and a nilpotent resonance at \(B=\pi/2\), even for \(p\ne0\). The antipodal reduction, low-gain census and standard Schur criterion are not priority claims here. The distinct contribution is the exhaustive higher-lobe census and the infinite sequence of sharp hyperbolic-attraction windows with the universal \(9/(2m_k)\) leading width.

1. O. A. Almatroud et al., *Multistability, Chaos, and Synchronization in Novel Symmetric Difference Equation*, Symmetry 16 (2024), 1093, https://doi.org/10.3390/sym16081093.
2. M. Mammeri, *Symmetry and Periodic-Chaos in 3-D Sinusoid Discrete Maps*, Bulletin of Mathematical Analysis and Applications 9 (2017), 1–8, https://emis.muni.cz/journals/BMAA/repository/docs/BMAA9-1-1.pdf.
3. K. Rajagopal et al., *Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems*, Symmetry 15 (2023), 780, https://doi.org/10.3390/sym15040780.
4. *A unique antipodal two-cycle with a nilpotent superattraction sheet*, Resultary record 1546559d174a, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-unique-antipodal-two-cycle-with-a-nilpotent-superattraction-sh--1546559d174a.
