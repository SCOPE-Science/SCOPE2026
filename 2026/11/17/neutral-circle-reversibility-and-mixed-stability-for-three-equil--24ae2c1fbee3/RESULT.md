# Neutral-circle reversibility and mixed stability for three equilateral quartic cycles

## Finding
For three disjoint, equal-radius invariant circles at the vertices of a unit equilateral triangle, every prescribed periodic circle of a planar quartic flow is **either hyperbolic or surrounded by a local annulus of periodic orbits**. Nonhyperbolic isolated prescribed cycles cannot occur. Moreover, whenever at least one of the prescribed circles is hyperbolic, some prescribed circle attracts transversely and another repels transversely; all six mixed transverse-stability patterns actually occur at every admissible radius. The polynomial-flow normal form and general Floquet-exponent calculation are due to Cao and Llibre (2026); the new specialization classifies the neutral boundary and proves the mixed-sign obstruction and its sharp realization.

## Assumptions and scope
Choose \(0<r<1/2\), \(v=\sqrt3/2\), and centers \(C_1=(0,0)\), \(C_2=(1,0)\), \(C_3=(1/2,v)\). Write \(z=(x,y)\), \(J(a,b)=(-b,a)\), and \(f_i(z)=|z-C_i|^2-r^2\). For arbitrary real \(\lambda,\mu,\kappa\), define
\[
\begin{aligned}
 A_1&=-\lambda-\mu+\kappa(-vx-y/2-v),\\
 A_2&=\lambda+\kappa(vx-y/2),\\
 A_3&=\mu+\kappa y,\\
 X(z)&=\sum_{i=1}^{3} A_i(z)\!\prod_{j\ne i} f_j(z)\,J(z-C_i).
\end{aligned}
\]
Cao--Llibre's non-collinear normal-form theorem shows that these are precisely the real degree-at-most-four polynomial fields preserving the three chosen circles. Let \(\Gamma_i=\{f_i=0\}\). Set
\[
\omega_1=-\lambda-\mu-\kappa v,\quad
\omega_2=\lambda+\kappa v,\quad
\omega_3=\mu+\kappa v.
\]
We assume that **all three** prescribed circles are regular periodic trajectories. By the published periodicity criterion this is equivalent to \(|\omega_i|>|\kappa|r\) for each \(i\). Their positive-time Floquet log-multipliers, denoted \(\chi_i\), are negative for attracting and positive for repelling hyperbolic circles. No claim is made about periodic orbits not among the three specified circles.

## Proof
**1. Exact equilateral Floquet specialization.** Let \(h=\sqrt{1-4r^2}>0\), and define for \(i=1,2,3\)
\[
\delta_i=\operatorname{sgn}(\omega_i)\sqrt{\omega_i^2-\kappa^2r^2},\qquad
H_i=\omega_i+\delta_i h-2\kappa vr^2.
\]
Since \(|\omega_i|>|\kappa|r\), and \(2vr<1\), both \(\delta_i\) and \(H_i\) have the sign of \(\omega_i\); in particular their denominators do not vanish. For the equilateral geometry, the six quantities \(H_{ij}\) in Cao--Llibre's general formula reduce to the corresponding \(H_i\). Their three numerator pairs reduce to
\[
 B_{12}=\omega_1-\omega_2,\quad
 B_{13}=\omega_3-\omega_1,\quad
 B_{23}=\omega_2-\omega_3.
\]
Let \(S_1=\omega_3-\omega_2\), \(S_2=\omega_1-\omega_3\), and \(S_3=\omega_2-\omega_1\). By Proposition 6.2 of Cao--Llibre, including their correction from counterclockwise integration to **positive-time** orientation, the Floquet log-multipliers are exactly
\[
\boxed{\quad \chi_i=\frac{2\pi\kappa r^2}{|\delta_i|H_i}\,S_i,\quad i=1,2,3.\quad}
\]
For \(\kappa\ne0\) the neutral loci \(\chi_i=0\) are exactly \(S_i=0\), yielding respectively the three explicit linear relations
\[
\lambda=\mu,\qquad
\lambda+2\mu+\sqrt3\kappa=0,\qquad
2\lambda+\mu+\sqrt3\kappa=0.
\]

**2. A neutral circle always belongs to a period annulus.** For each vertex \(C_i\), let \(R_i\) be reflection in the line through \(C_i\) and the centroid of the triangle. Its linear part \(M_i\) is
\[
 M_1=\begin{pmatrix}\frac12&v\\v&-\frac12\end{pmatrix},\quad
 M_2=\begin{pmatrix}\frac12&-v\\-v&-\frac12\end{pmatrix},\quad
 M_3=\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]
Every such reflection fixes circle \(i\) and swaps the other two circles. Substituting the displayed affine functions \(A_i\) proves the exact polynomial identity \(X(R_i z)=-M_iX(z)\) precisely when the corresponding linear relation in step 1 holds. One can see the mechanism directly: under that relation, \(A_j(R_i z)=A_{\sigma_i(j)}(z)\), where \(\sigma_i\) swaps the other two labels; also \(JM_i=-M_iJ\). Therefore the flow is time-reversal symmetric with respect to the reflection line. The regular periodic circle \(\Gamma_i\) meets the line transversely in two points. The reversible-periodic-orbit lemma (Cao--Llibre, Lemma 2.4, explicitly a **previously established** criterion) implies the existence of a local period annulus. When \(\kappa=0\), Cao--Llibre's Proposition 6.3 already supplies a first integral and shows that all three periodic circles lie in period annuli. Conversely if \(\chi_i\ne0\), the circle is hyperbolic and isolated by the Poincaré return-map criterion. This proves the exact isolation dichotomy.

**3. A positive-weight zero sum forbids common stability.** Put
\[
 w_i=\frac{|\delta_i|H_i\omega_i}{2\pi r^2}>0.
\]
Then the preceding Floquet formula gives
\[
\sum_{i=1}^{3}w_i\chi_i
=\kappa\sum_{i=1}^{3}\omega_i S_i
=\kappa[\omega_1(\omega_3-\omega_2)+\omega_2(\omega_1-\omega_3)+\omega_3(\omega_2-\omega_1)]=0.
\]
If any exponent is nonzero, the positive weights force both a positive and negative exponent. The conclusion concerns transverse stability of these three prescribed circles, not other attractors or invariant sets.

**4. All six mixed sign patterns occur.** Fix \(\kappa=1\) and take any permutation \((a_1,a_2,a_3)\) of \((3,1,-4)\). Specify
\[
\omega_i=v/3+2a_i,\qquad\lambda=\omega_2-v,\qquad\mu=\omega_3-v.
\]
Since \(\omega_1+\omega_2+\omega_3=v\), these choices satisfy the defining equations for the \(\omega_i\). Every \(|\omega_i|\) exceeds \(1/2\), so periodicity holds for every radius \(0<r<1/2\). None of the three \(S_i\) vanishes. The sign of \(\chi_i\) equals that of \(\omega_iS_i\) because \(\kappa>0\), \(\delta_i\) and \(H_i\) have the sign of \(\omega_i\). The six permutations yield the six possible mixed triples of signs: \((+,+,-)\), \((+,-,+)\), \((-,+,+)\), \((+,-,-)\), \((-,+,-)\), and \((-,-,+)\). No other nonzero-sign pattern is possible by step 3. This completes the classification.

## Verification
The standalone `verify.py` confirms, by symbolic polynomial substitution, all three reflection identities on the three neutral hyperplanes; verifies the equilateral specialization of the published numerator parameters and the telescoping weighted cancellation; and enumerates all six mixed sign patterns at exact symbolic parameters. Run using `python verify.py` with Python 3 and SymPy installed. The script confirms algebraic identities and finite examples; the statements for all real parameters and all admissible radii follow from the analytical inequalities and the reversible-orbit lemma, not sample enumeration.

## Relationship to prior work
Cao and Llibre (arXiv:2611.05696v1, 2026) provide the full degree-four normal form, periodicity inequalities, characteristic exponent integrals and explicit hyperbolicity criterion (Theorem D, Proposition 6.2); all these are expressly **prior results**. Their Proposition 6.3 covers the \(\kappa=0\) period-annulus case; their Lemma 2.4 supplies the general reversible-orbit criterion. What is addressed here is the equilateral subclass at **nonzero** \(\kappa\): the exact neutral-to-annulus implication, the positive-weight three-circle sign obstruction, and sharp realizability of each remaining stability pattern. Their stated main theorems do not present this equal-radius stability-sign and isolation classification. Earlier general constructions (Christopher 2001; Llibre, Ramírez, Ramírez and Sadovskaia 2016) construct circular limit cycles and give degree/count bounds, without an identified competing theorem for these exact equilateral normal-form conditions. This is a best-knowledge comparison, not proof of historic uniqueness.

## Limitations
The equal-radius, equilateral, pairwise exterior geometry is essential for the stated rigidity; non-equilateral examples in the motivating paper can have three exponents of the same sign. There may be additional periodic orbits away from the three prescribed circles, and neither a global basin decomposition nor all possible phase portraits are classified. A local period annulus need not extend globally. The sign classification assumes all three prescribed circles are periodic. Historical priority remains provisional, and independent mathematical validation has not been performed.

## References
1. C. Cao and J. Llibre, *Quartic polynomial differential systems with three disjoint invariant circles*, arXiv:2611.05696v1 (first public release 2026-11-03), Theorem D, Lemma 2.4, Propositions 6.1–6.3. https://arxiv.org/html/2611.05696v1
2. C. Christopher, *Polynomial vector fields with prescribed algebraic limit cycles*, Geom. Dedicata 88 (2001), 255–258, DOI:10.1023/A:1013171019668.
3. J. Llibre, R. Ramírez, V. Ramírez, N. Sadovskaia, *The 16th Hilbert problem restricted to circular algebraic limit cycles*, J. Differential Equations 260 (2016), 5726–5760, DOI:10.1016/j.jde.2015.12.019.
