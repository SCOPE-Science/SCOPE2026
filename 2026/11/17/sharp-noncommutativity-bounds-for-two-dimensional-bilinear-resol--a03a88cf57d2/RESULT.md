# Sharp noncommutativity bounds for two-dimensional bilinear-resolvent moment completions

## Finding
Let \(A,B\) be noncommuting, strictly positive definite Hermitian \(2\times2\) matrices. Call \(A,B\) **moment-completable** if a positive semidefinite Hermitian \(C\) and a normalized positive operator-valued measure \(E\) on \([0,1]^2\) exist such that, for all integers \(m,n\ge0\),
\[
 (I+mA+nB+mnC)^{-1}=\int_{[0,1]^2} s^m t^n\,dE(s,t).
\]
Set \(\lambda=\lambda_{\min}(A)/\|A\|\in(0,1)\), \(\mu=\lambda_{\min}(B)/\|B\|\in(0,1)\), and \(r=\lambda\mu/((1-\lambda)(1-\mu))\). For prescribed \(\lambda,\mu\), the exact attainable maximum of \(\|[A,B]\|/(\|A\|\|B\|)\) over moment-completable noncommuting pairs is
\[
 M(\lambda,\mu)=\begin{cases}
 \sqrt{\lambda\mu(1-\lambda-\mu)},&r<1/2,\\[2pt]
 (1-\lambda)(1-\mu)/2,&r\ge1/2.
 \end{cases}
\]
The formulas coincide at the transition. The optimizing squared overlap of the two minimum-eigenvalue eigenvectors is \(r\) in the first regime and \(1/2\) in the second. In particular,
\[
\boxed{\frac{\|[A,B]\|}{\|A\|\|B\|}\le\frac1{3\sqrt3}.}
\]
Equality is possible and occurs precisely when \(\lambda=\mu=1/3\) and the modulus of the minimum-eigenvector overlap is \(1/2\). These conditions determine the normalized pair up to simultaneous unitary conjugacy (and independent positive rescalings before normalization).

## Assumptions and scope
Matrix norms are the spectral/operator norm on \(\mathbb C^2\), and \([A,B]=AB-BA\). Strict positivity and noncommutation ensure that each normalized matrix has a simple smaller eigenvalue. The word *completion* requires a positive operator-valued representing measure for **every** nonnegative integer pair, not merely positivity of individual resolvents. Tian's Theorem 4.1 (arXiv:2611.03081v1, Section 4) establishes that a noncommuting positive definite pair is completable exactly when
\[
X+Y\succeq I,\quad X=A/\|A\|,\quad Y=B/\|B\|,
\]
and then \(C=\|B\|A+\|A\|B-\|A\|\|B\|I\) is the unique positive completion. The present theorem **takes that qualitative equivalence as an established premise**; it does not reprove existence of the measure.

## Proof
**1. Complete angle parametrization.** Let \(P,Q\) be the rank-one spectral projections onto the smaller-eigenvalue lines of \(X,Y\), and put \(u=1-\lambda\) and \(v=1-\mu\). Thus \(0<u,v<1\) and
\[
 X=I-uP,\qquad Y=I-vQ.
\]
Choose unit vectors \(p,q\) spanning their ranges, and set \(z=|\langle p,q\rangle|\). Noncommutation is equivalent to \(0<z<1\). The two eigenvalues of \(uP+vQ\) are
\[
\frac{u+v\pm\sqrt{(u-v)^2+4uvz^2}}2.
\]
By the cited completion criterion, \(A,B\) are completable if and only if the larger eigenvalue is at most \(1\). Squaring the equivalent inequality \(\sqrt{(u-v)^2+4uvz^2}\le2-u-v\) (whose right side is strictly positive) gives
\[
uvz^2\le(1-u)(1-v)=\lambda\mu,
\]
so the allowed overlaps are precisely \(0<z<1\) with \(z^2\le r\). Every such overlap is realized by rank-one projections on \(\mathbb C^2\), hence this is also sufficient.

**2. Exact commutator at fixed spectra.** In an orthonormal basis with \(P=\operatorname{diag}(1,0)\) and \(q=(z,e^{i\phi}\sqrt{1-z^2})\), a direct calculation gives
\[
\|[P,Q]\|=z\sqrt{1-z^2},\qquad
\frac{\|[A,B]\|}{\|A\|\|B\|}=uvz\sqrt{1-z^2}.
\]
The function \(w\mapsto w(1-w)\) increases on \((0,1/2)\) and decreases on \((1/2,1)\). The maximizing overlap squared is therefore \(\min(r,1/2)\). If \(r<1/2\), the maximum equals
\[
uv\sqrt{r(1-r)}=\sqrt{\lambda\mu(uv-\lambda\mu)}=\sqrt{\lambda\mu(1-\lambda-\mu)}.
\]
If \(r\ge1/2\), it equals \(uv/2=(1-\lambda)(1-\mu)/2\). Both are attained with \(0<z<1\), and the completion exists by Step 1.

**3. Sharp universal bound and rigidity.** For the sum of rank-one projections, the triangle-free estimate
\[
\sqrt{(u-v)^2+4uvz^2}\ge(u+v)z
\]
follows by subtracting squares, obtaining \((u-v)^2(1-z^2)\ge0\). Hence the positive-completion constraint implies
\[
(u+v)(1+z)\le2,\qquad uv\le(u+v)^2/4\le(1+z)^{-2}.
\]
It follows that
\[
\frac{\|[A,B]\|}{\|A\|\|B\|}\le
\frac{z\sqrt{1-z^2}}{(1+z)^2}
=\frac{z\sqrt{1-z}}{(1+z)^{3/2}}=:f(z).
\]
For \(0<z<1\),
\[
\frac{f'(z)}{f(z)}=\frac{1-2z}{z(1-z^2)}.
\]
Thus the unique maximizer is \(z=1/2\), with \(f(1/2)=1/(3\sqrt3)\). Equality in the AM–GM step forces \(u=v\); equality in \((u+v)(1+z)\le2\) then forces \(u=v=2/3\). Therefore \(\lambda=\mu=1/3\), and these conditions are necessary and sufficient for global equality.

**4. Attaining pair.** With
\[
 P=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 Q=\begin{pmatrix}1/4&\sqrt3/4\\\sqrt3/4&3/4\end{pmatrix},\quad
 A=I-\tfrac23P=\begin{pmatrix}1/3&0\\0&1\end{pmatrix},\quad
 B=I-\tfrac23Q=\begin{pmatrix}5/6&-\sqrt3/6\\-\sqrt3/6&1/2\end{pmatrix},
\]
both matrices are strictly positive with norm one and do not commute. The unique completion from Tian's theorem is
\[
 C=A+B-I=\begin{pmatrix}1/6&-\sqrt3/6\\-\sqrt3/6&1/2\end{pmatrix}\succeq0,
\]
with eigenvalues \(0,2/3\). Direct multiplication gives \(\|[A,B]\|=\sqrt3/9=1/(3\sqrt3)\). This also proves attainment at the boundary where \(C\) is singular.

## Verification
The proof needs no asymptotic approximation or external computational certificate. The accompanying `checker.py` verifies the exact witness (including eigenvalue and norm identities), the fixed-ratio formulas in both regimes, and an extensive deterministic grid of admissible projections. Those checks are supplementary to, not replacements for, the analytic proof and Tian's qualitative criterion.

## Relationship to prior work
Tian, *Joint Moments of Bilinear Resolvents*, arXiv:2611.03081v1 (2026), Theorem 4.1, proves the complete existence/uniqueness criterion \(X+Y\succeq I\). Its full accessible Section 4 provides the premise but does not state either the fixed-ratio sharp commutator envelope or its universal attained maximum. Classical studies of commutators of positive operators and two-projection norm identities (Kittaneh; Conde) concern relevant ingredients but do not, in the accessible material, supply the joint-moment constraint. Earlier results on weighted rank-one commutator constants and crossed-Heinz inequalities likewise address different optimizations. Known projection identities are not claimed as novel; the quantitative joint-moment completion law and all equality cases are the asserted contribution.

## Limitations
The theorem is only about noncommuting strictly positive Hermitian two-by-two matrices under the precise moment-completion requirement. It does not classify higher dimensions, singular input matrices, or arbitrary compatible measurements. The general POVM existence assertion is cited from Tian rather than independently proved here. Some older commutator papers were accessible only through abstracts/metadata, so an unlocated equivalent formulation under different terminology remains possible. Independent mathematical validation and publication-priority certification have not been performed.

## References
1. James Tian, *Joint Moments of Bilinear Resolvents*, arXiv:2611.03081v1, submitted 2 November 2026, Theorem 4.1. https://arxiv.org/html/2611.03081v1
2. Cristian Conde, *A note about the norm of the sum and the anticommutator of two orthogonal projections*, Journal of Mathematical Analysis and Applications 505 (2022), 125650. https://doi.org/10.1016/j.jmaa.2021.125650
3. Fuad Kittaneh, *Inequalities for commutators of positive operators*, Journal of Functional Analysis 250 (2007), 132–143. https://doi.org/10.1016/j.jfa.2007.05.008
4. Fuad Kittaneh, *Norm inequalities for commutators of positive operators and applications*, Mathematische Zeitschrift 258 (2008), 845–849. https://doi.org/10.1007/s00209-007-0201-9
