# Balanced concentric-square phase retrieval: the exact angular and radial criterion

## Finding
For positive radii \(r,s\) and angles \(\vartheta,\delta\in\mathbb R\), put
\[
\mathcal S(r,s,\vartheta,\delta)=
\{r e^{i(\vartheta+j\pi/2)}:j=0,1,2,3\}
\cup\{s e^{i(\vartheta+\delta+j\pi/2)}:j=0,1,2,3\}.
\]
The eight point intensities \((|p(z)|^2)_{z\in\mathcal S}\) identify **every** complex polynomial \(p(z)=a+bz+cz^2\), including polynomials of lower degree and the zero polynomial, up to one unimodular scalar **if and only if**
\[
\boxed{r\ne s\quad\text{and}\quad\sin(2\delta)\ne0.}
\]
In the positive regime, the measurement map on Hermitian \(3\times3\) matrices has rank exactly eight and kernel exactly
\[
\mathbb R\operatorname{diag}\big(r^2s^2,-(r^2+s^2),1\big).
\]
Its nonzero elements are invertible, proving universal phase retrieval despite one missing Hermitian degree of freedom. Both failure conditions are sharp, with explicit pairs of distinct-phase polynomials having the same intensities. No set of seven complex polynomial point evaluations can universally retrieve all quadratic polynomials. Thus the balanced four-plus-four design realizes the global cardinal minimum exactly on the stated parameter region.

## Assumptions and scope
Here polynomial degree is at most two, coefficients are arbitrary complex numbers, point evaluations are complex-linear, and global phase equivalence means \(q=\eta p\) with \(|\eta|=1\). Radii are strictly positive; the point sets are four equally spaced points on each circle. An overall rotation \(\vartheta\) is immaterial. The condition \(r\ne s\) ensures eight distinct points. No restriction that the sample circles lie in the unit disk is necessary since the signals are polynomials; multiplying all sample points by a sufficiently small positive constant places them in that disk without affecting the criterion.

## Proof
**Hermitian lifting and Fourier blocks.** Let \(v(z)=(1,z,z^2)^\top\), and for Hermitian \(H=(h_{jk})_{0\le j,k\le2}\) set \(Q_H(z)=v(z)^*Hv(z)\). Its restriction to a circle of radius \(R\) is
\[
Q_H(Re^{it})=D(R)+2\operatorname{Re}\bigl[B(R)e^{it}+C(R)e^{2it}\bigr],
\]
where
\[
D(R)=h_{00}+R^2h_{11}+R^4h_{22},\qquad
B(R)=Rh_{01}+R^3h_{12},\qquad C(R)=R^2h_{02}.
\]
Four equally spaced real samples starting at angle \(\alpha\) yield the discrete mean \(D(R)\), the full complex first Fourier coefficient \(B(R)\), and the one real second-frequency projection \(2R^2\operatorname{Re}(h_{02}e^{2i\alpha})\). Indeed the four-point discrete Fourier transform isolates frequencies \(0\) and \(\pm1\), and aliases \(+2\) with \(-2\) only.

Suppose \(H\) has zero lifted measurements at all eight points. The first-frequency conditions read
\[
\begin{pmatrix}r&r^3\\s&s^3\end{pmatrix}
\begin{pmatrix}h_{01}\\h_{12}\end{pmatrix}=0.
\]
When \(r\ne s\), its determinant \(rs(s^2-r^2)\) is nonzero, giving \(h_{01}=h_{12}=0\). The second-frequency conditions at \(\vartheta\) and \(\vartheta+\delta\) are two real equations for the real and imaginary parts of \(h_{02}\); their determinant is a nonzero scalar multiple of \(\sin(2\delta)\). Thus if \(\sin(2\delta)\ne0\), also \(h_{02}=0\). The two remaining mean equations are \(D(r)=D(s)=0\), whose unique real solution space is
\[
(h_{00},h_{11},h_{22})=t\big(r^2s^2,-(r^2+s^2),1\big),\quad t\in\mathbb R.
\]
The generator has determinant \(-r^2s^2(r^2+s^2)\ne0\). The real Hermitian space has dimension nine, and the nullspace has dimension one, so the measurement map has rank eight.

If \(|p(z)|^2=|q(z)|^2\) at all eight nodes, the Hermitian matrix \(aa^*-bb^*\), where \(a,b\in\mathbb C^3\) are the conjugates of their coefficient vectors, lies in the kernel. Such a difference has rank at most two, whereas every nonzero matrix in the kernel has rank three. Hence \(aa^*=bb^*\), which forces \(b=\eta a\) for some \(|\eta|=1\) (also valid for the zero vector).

**Necessity and explicit ambiguity.** If \(r=s\), take \(p(z)=r^2\) and \(q(z)=z^2\). Their intensities agree on the entire common circle, but the polynomials are not scalar multiples. If \(\sin(2\delta)=0\), take
\[
p(z)=1+i e^{-2i\vartheta}z^2,\qquad q(z)=1-i e^{-2i\vartheta}z^2.
\]
On both square grids, \(e^{-2i\vartheta}z^2\) is real because \(\delta\in\frac\pi2\mathbb Z\); therefore \(|p|^2=|q|^2\) at every node. The two polynomials are not phase multiples.

**Minimality of eight measurements.** For any \(m\le7\) complex evaluation points, consider the real linear map from nine-dimensional Hermitian matrices to their \(m\) quadratic evaluations. If evaluation vectors fail to span \(\mathbb C^3\), a nonzero polynomial vanishes at every point and phase retrieval fails. Otherwise, the Hermitian kernel has real dimension at least two. Pick linearly independent kernel matrices \(A,B\). As the determinant of a \(3\times3\) Hermitian matrix is an odd homogeneous cubic, \(\det(A\cos t+B\sin t)\) changes sign under \(t\mapsto t+\pi\), so some nonzero kernel matrix \(H\) is singular. No nonzero positive or negative semidefinite Hermitian matrix lies in the kernel, because zero quadratic forms on a spanning family force a semidefinite matrix to vanish. Hence \(H\) is indefinite of rank two, and spectral decomposition writes \(H=aa^*-bb^*\) for non-collinear vectors \(a,b\). They supply two non-phase-equivalent quadratic polynomials with identical measurements. Therefore seven or fewer evaluations never suffice.

## Verification
Run `python verify_two_square.py` with SymPy available. It verifies the eight-node Gaussian-integer example \(\{1,i,-1,-i,1+i,-1+i,-1-i,1-i\}\): lifted matrix rank eight, one-dimensional kernel, diagonal generator \(\operatorname{diag}(2,-3,1)\) of determinant \(-6\). It also verifies both symbolic radial identities and an untwisted rank-two invisible direction. These finite checks corroborate, but do not replace, the all-parameter Fourier-block proof above. The proof covers all real angles, all positive radii, and all coefficient triples without genericity assumptions.

## Relationship to prior work
Pohl, Li and Boche (2017) treat polynomial amplitude recovery using concentric circles: their explicit degree-two sampling guarantee uses five points on one circle and three on the other, via outer/inner factorization. That result establishes the two-circle problem and the eight-measurement benchmark but does **not** imply retrieval from the balanced four-plus-four grids or their sharp angular twist condition. Chalendar and Partington (2024) prove uniqueness from complete circles or suitable infinite subsets; continuity and infinite-set uniqueness do not establish a four-samples-per-circle theorem. Bodmann and Hammen (2013) give sharp-cardinality complex frames using polynomial values and derivative-type measurements; their construction does not cover the present pure point-evaluation grids. The novelty asserted here is the all-parameter equivalence for **balanced regular-square sampling**, its exact Hermitian kernel and explicit failures, not the previously known abstract eight-measurement threshold. Independent of these sources, the eight-point single logarithmic-spiral construction is a different minimal design and gives no condition for concentric-square configurations.

## Limitations
This is a complete classification only for the balanced two-square geometry in degree at most two. The Fourier-block argument does not classify arbitrary four-plus-four point configurations, higher polynomial degrees or uniform noise stability near the degeneracy curves. Similar earlier phase-retrieval constructions may contain another equivalent presentation; the present comparison establishes best-knowledge distinctness, not absolute historical priority.

## References
- V. Pohl, N. Li and H. Boche, *Phase Retrieval in Spaces of Analytic Functions on the Unit Disk*, SampTA 2017, conference presentation dated July 4, 2017, slides 13–19, https://www.ce.cit.tum.de/fileadmin/w00cgn/lti/pdf/vortraege/Pohl-Phase_Retrieval_in_Spaces_of_Analytic_Functions_on_the_Unit_Disk.pdf ; published proceedings DOI: 10.1109/SAMPTA.2017.8024411.
- I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255, sections 1 and 2, https://arxiv.org/pdf/2403.16255.
- B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487, section 2, https://arxiv.org/pdf/1302.5487.
- P. Jaming and M. Rathmair, *Uniqueness of phase retrieval from three measurements*, arXiv:2205.08753, sections 1 and 3, https://arxiv.org/pdf/2205.08753.
