# A sharp spectral-band numerical-radius law for square-zero factors

## Finding
Let \(H\) be a complex Hilbert space of dimension at least two, let \(A\ne0\) be a bounded positive selfadjoint operator, and put \(M=\|A\|\), \(m=\inf\sigma(A)\), \(r=m/M\in[0,1]\). For a bounded operator \(T\), write \(w(T)=\sup_{\|x\|=1}|\langle Tx,x\rangle|\). Define
\[
F_r(t)=\sqrt{r^2+(1-r^2)t}+(1-r)\sqrt{t(1-t)},\quad 0\le t\le1,
\qquad C(r)=\max_{0\le t\le1}F_r(t).
\]
Then the following **exact fixed-operator optimization** holds:
\[
\boxed{\sup_{B\ne0,\ B^2=0}\frac{w(AB)}{\|A\|w(B)}=C(r).}
\]
The same supremum results when \(B\) is restricted to rank-one square-zero operators. In particular every square-zero \(B\) satisfies \(w(AB)\le \|A\|C(r)w(B)\), with the best constant depending only on the extreme spectral values of \(A\), even when its spectrum is continuous.

For \(0\le r<1\), \(F_r\) is strictly concave and has a unique maximizing \(t_r\in(1/2,1)\) characterized by
\[
(1+r)\sqrt{t_r(1-t_r)}=(2t_r-1)\sqrt{r^2+(1-r^2)t_r}.
\]
At the endpoints, \(C(0)=3\sqrt3/4\) and \(C(1)=1\); for \(0<r<1\), \(1<C(r)<3\sqrt3/4\). The endpoint expansions are
\[
C(r)=\frac{3\sqrt3}{4}-\frac{\sqrt3}{4}r+O(r^2)\quad(r\downarrow0),\qquad
C(r)=1+\frac{\sqrt2-1}{2}(1-r)+O((1-r)^2)\quad(r\uparrow1).
\]
For \(r<1\), an optimizing rank-one square-zero operator exists if and only if the spectral endpoints \(m\) and \(M\) are both eigenvalues of \(A\). Otherwise the sharp constant is approached by approximate endpoint eigenvectors.

## Assumptions and scope
All operators act on the same complex Hilbert space \(H\), of possibly infinite dimension, with \(\dim H\ge2\). Positivity means \(A=A^*\ge0\); \(A\) need not be invertible or compact. The first factor \(A\) is fixed, and \(B\) ranges over every nonzero bounded square-zero operator. The spectrum's infimum and supremum are well-defined, but need not be attained. The formula does not claim an analogous bound for unrestricted \(B\) or for higher-order nilpotents.

## Proof
**1. Rank-one radius.** Write \(a\otimes b:x\mapsto\langle x,b\rangle a\). Direct optimization in \(\operatorname{span}\{a,b\}\) gives
\[
w(a\otimes b)=\frac{\|a\|\|b\|+|\langle a,b\rangle|}{2}.
\]
For orthonormal vectors \(u,v\), the operator \(B=u\otimes v\) obeys \(B^2=0\), \(w(B)=1/2\), and
\[
\frac{w(AB)}{w(B)}=\|Au\|+|\langle Au,v\rangle|.
\]
For a fixed unit \(u\), the largest latter term over unit \(v\perp u\) equals
\(\sqrt{\|Au\|^2-\langle Au,u\rangle^2}\), realized by the normalized perpendicular component of \(Au\) if it is nonzero. Therefore the rank-one supremum is
\[
\sup_{\|u\|=1}\left(\|Au\|+\sqrt{\|Au\|^2-\langle Au,u\rangle^2}\right).
\]

**2. Every square-zero factor reduces to rank one.** Let \(B^2=0\ne B\) and \(K=\ker B\). Relative to \(H=K\oplus K^\perp\), \(B\) has block matrix \(\begin{psmallmatrix}0&D\\0&0\end{psmallmatrix}\), where \(\|D\|=\|B\|\). Hence \(w(B)=\|B\|/2\). Fix a unit \(x\) with \(Bx\ne0\), put \(x_N=P_{K^\perp}x\), \(u=Bx/\|Bx\|\in K\), and \(v=x_N/\|x_N\|\in K^\perp\). Define \(R=\|B\|u\otimes v\). Then \(R^2=0\), \(w(R)=w(B)\), and
\[
Bx=\frac{\|Bx\|}{\|B\|\|x_N\|}Rx,\qquad 0<\frac{\|Bx\|}{\|B\|\|x_N\|}\le1.
\]
Consequently \(|\langle ABx,x\rangle|\le |\langle ARx,x\rangle|\le w(AR)\). The case \(Bx=0\) is trivial. Taking the supremum over unit \(x\) shows that the optimum among arbitrary square-zero \(B\) cannot exceed the rank-one optimum, while the reverse inequality is immediate.

**3. Spectral variance envelope.** Normalize \(\|A\|=1\). For each unit \(u\), let \(s=\langle Au,u\rangle\in[r,1]\). Functional calculus applied to \((A-rI)(I-A)\ge0\) gives
\[
\|Au\|^2\le(1+r)s-r,\qquad
\|Au\|^2-s^2\le(1-s)(s-r).
\]
Both terms in the rank-one expression increase with the second moment \(\|Au\|^2\) at fixed \(s\). Writing \(s=r+(1-r)t\), the upper bound becomes precisely \(F_r(t)\). For \(r<1\), spectral projections onto arbitrarily small neighborhoods of the distinct endpoints \(r\) and \(1\) contain unit vectors \(e_{r,\varepsilon}\) and \(e_{1,\varepsilon}\) that are mutually orthogonal. Taking \(u_\varepsilon=\sqrt{1-t}\,e_{r,\varepsilon}+\sqrt t\,e_{1,\varepsilon}\) makes both second-moment bounds asymptotically equalities. The perpendicular normalization of \(Au_\varepsilon-su_\varepsilon\) supplies the maximizing rank-one factor in the limit. Thus the upper bound is the exact supremum. If \(r=1\), \(A=I\) after normalization, and the ratio is exactly one for all nonzero square-zero \(B\).

**4. Unique optimizer, attainment and asymptotics.** For \(r<1\), each summand of \(F_r(t)\) is concave, and at least the second is strictly concave on \((0,1)\). Its derivative tends to positive infinity at \(t=0\) (with the appropriate one-sided interpretation at \(r=0\)) and to negative infinity at \(t=1\). The unique critical point obeys the stated equation and lies above \(1/2\). At \(r=0\), it is \(t_0=3/4\). As \(r\uparrow1\), maximizers tend to \((1+1/\sqrt2)/2\); expansion at these unique maximizers gives the stated coefficients. The strict improvement for \(r>0\) follows also from writing normalized \(A=rI+(1-r)P\), \(0\le P\le I\), and applying the universal \(C(0)\) estimate to \(PB\): \(C(r)\le r+(1-r)C(0)<C(0)\). The inequality \(C(r)>1\) follows from taking \(t<1\) sufficiently close to one. Finally, exact equality in the positive operator inequality \((A-rI)(I-A)\ge0\) for an optimizing rank-one factor forces the spectral measure of its generating unit vector to be supported on \(\{r,1\}\), with both endpoint masses positive. Conversely two endpoint eigenvectors give equality by the construction in Step 3.

## Verification
A standalone standard-library script `check.py` reproduces the scalar root calculation, the two-dimensional rank-one extremizer, and 9,000 deterministic sample inequalities for positive two-point spectra. The script is supplementary: Step 3 uses functional calculus and approximate spectral endpoint vectors and therefore proves the claim for arbitrary Hilbert-space dimension; numerical sampling alone would not suffice. Representative values are \(C(0.1)\approx1.2575850983\), \(C(0.5)\approx1.1221848548\), and \(C(0.9)\approx1.0213565534\).

## Relationship to prior work
Benabdi, Baghdad, Chraibi Kaadoud and Barraa proved the universal sharp inequality \(w(AB)\le(3\sqrt3/4)\|A\|w(B)\) for every positive \(A\) and unrestricted \(B\), including a rank-one square-zero extremizing example. That sharp universal theorem does not specify the optimal constant when the positive operator has a fixed nonzero spectral minimum. The result here determines the full spectral-band interpolation *for every square-zero second factor*, including infinite-dimensional endpoint nonattainment. Gau, Huang and Wu studied square-zero and idempotent factors under commutation assumptions; the present product is generally noncommuting and has the positive operator first. General numerical-radius product and commutator bounds of Bhunia and coauthors do not supply this fixed-spectral-band optimization. The rank-one radius identity and spectral variance inequality are standard ingredients; neither is presented as new.

## Limitations
No claim is made for unrestricted second factors, or for higher-order nilpotents. The theorem establishes sharpness as a supremum, not always an attained maximum. Independent review and historical priority beyond the identified comparisons remain open. Specialized unindexed inequalities for products with a quadratic factor could conceivably yield an equivalent formulation.

## References
1. P. Bhunia and K. Paul, *Furtherance of Numerical Radius Inequalities of Hilbert Space Operators*, arXiv:2102.01953v1, first posted 3 February 2021, https://arxiv.org/html/2102.01953v1.
2. E. H. Benabdi, A. Baghdad, M. Chraibi Kaadoud and M. Barraa, *On the Inequality \(w(AB)\le c\|A\|w(B)\) where \(A\) is a Positive Operator*, Filomat 36 (2022), 1337–1340, https://doi.org/10.2298/FIL2204337B.
3. H.-L. Gau, C.-Y. Huang and P. Y. Wu, *Numerical Radius Inequalities for Square-zero and Idempotent Operators*, Operators and Matrices 2 (2008), 137–141, https://doi.org/10.7153/oam-02-08.
4. P. Bhunia, S. Jana and K. Paul, *Refined inequalities for the numerical radius of Hilbert space operators*, arXiv:2106.13949v1, 26 June 2021, https://arxiv.org/abs/2106.13949.
