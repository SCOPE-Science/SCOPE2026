# Fourier orthogonality on a positively weighted square: a complete mass stratification

## Finding
Let the four vertices of a nondegenerate parallelogram in the plane carry strictly positive probability masses. The maximum number of mutually orthogonal exponential characters with unrestricted real frequencies is **exactly one, two, three, or four**, with the following complete mass classification.

After an invertible affine change of coordinates put
\[
\mu=a\delta_{(0,0)}+b\delta_{(1,0)}+c\delta_{(0,1)}+d\delta_{(1,1)},\qquad a,b,c,d>0,\quad a+b+c+d=1.
\]
Write
\[
H=a^2+b^2-c^2-d^2,\qquad J=ab-cd,
\]
and let \(Q\) denote the inequality \(|H|\le 2|J|\), including equality and \(H=J=0\). Let \(T\) denote the union of these three explicitly described loci:
\[
\begin{aligned}
T_1&:\ a=d,\quad b=c,\quad \max(a,b)\le2\min(a,b),\\
T_2&:\ a=d=b+c,\\
T_3&:\ b=c=a+d.
\end{aligned}
\]
Then, reading the conditions **in priority order**, the sharp maximum is
\[
\boxed{\mathcal O(\mu)=\begin{cases}
4,&a=b=c=d=\tfrac14,\\
3,&\text{the masses satisfy }T,\\
2,&\text{the masses satisfy }Q,\\
1,&\text{otherwise}.
\end{cases}}
\]
Thus the complete three-character locus comprises a one-parameter opposite-equal-mass interval and two distinct one-parameter linear resonance families. In particular, some nonuniform positive square measures admit exactly three mutually orthogonal exponentials.

## Assumptions and scope
An exponential is \(e_\xi(x)=e^{2\pi i\langle \xi,x\rangle}\) for \(\xi\in\mathbb R^2\). A family is orthogonal when \(\langle e_\xi,e_\eta\rangle_{L^2(\mu)}=0\) for each pair of distinct frequencies. Because integer frequency shifts act identically on the four sites, frequencies are taken modulo \(\mathbb Z^2\) for combinatorial analysis; all constructions produce real frequencies. The four masses are positive, normalized to sum to one, and assigned to the vertices in the displayed order. The result classifies **maximum cardinality**, not every inclusion-maximal (potentially smaller) family.

The parallelogram extension uses \(x_{ij}=x_{00}+i u+j v\) with independent \(u,v\): the map \(\xi\mapsto(\langle\xi,u\rangle,\langle\xi,v\rangle)\) is onto \(\mathbb R^2\), and the translation phase is irrelevant to orthogonality.

## Proof
**Fourier-zero criterion.** Put \(z=e^{2\pi i\xi_1}\), \(w=e^{2\pi i\xi_2}\). The Fourier coefficient governing orthogonality at difference \(\xi\) is
\[
P(z,w)=a+bz+cw+dzw.
\]
Consequently two distinct orthogonal characters exist iff there is \((z,w)\in\mathbb T^2\) with \(P(z,w)=0\). For fixed \(z\), this means \(a+bz=-(c+dz)w\). A suitable unit \(w\) exists precisely when
\[
|a+bz|^2-|c+dz|^2=H+2J\operatorname{Re}(z)=0.
\]
As \(\operatorname{Re}(z)\) ranges over \([-1,1]\), this has a solution exactly on \(Q\), even when both complex quantities vanish. This proves the pair criterion.

**Four characters.** Four orthogonal exponentials form an orthonormal basis of the four-dimensional weighted evaluation space. Each matrix row is a vector of four unimodular entries times the square root of its vertex mass. Since a unitary square matrix has unit row norm, each mass must be \(1/4\). Conversely the four frequencies \((0,0),(1/2,0),(0,1/2),(1/2,1/2)\) give the Fourier basis when all masses equal. This also bounds every orthogonal family by four.

**Degenerate Fourier-zero locus.** Suppose \(H=J=0\). The equalities \(ab=cd\) and \(a^2+b^2=c^2+d^2\), together with positivity, imply equality of the unordered pairs \(\{a,b\}=\{c,d\}\). There are two pairings. If \(a=c,b=d\) and \(a\ne b\), then
\[
P(z,w)=(a+bz)(1+w),
\]
and its unit-torus zeros are **only** the line \(w=-1\), because \(a+bz\ne0\) on \(\mathbb T\). Three pairwise orthogonal frequencies would require three distinct points on the circle with all pairwise differences having second-coordinate phase \(-1\), which is impossible: the product of two such phases is \(+1\). If both pairings hold, all masses are equal, already treated.

The remaining pairing is \(a=d,b=c\). An orthogonal family of three normalized vectors in \(\mathbb C^4\) gives an orthogonal projection of rank three. Each of the four diagonal entries is three times its vertex mass, hence cannot exceed one. Thus \(3\max(a,b)\le1\), equivalent (as \(a+b=1/2\)) to \(\max(a,b)\le2\min(a,b)\). We now show sufficiency explicitly.

If \(a\ge b\), let \(r=b/a\in[1/2,1]\), \(C=\sqrt{(1-r)/2}\), and choose \(u,v\in\mathbb R\) with \(\cos(2\pi u)=C\), \(\cos(2\pi v)=-C/r\). Both choices exist because \(C/r\le1\) for \(r\ge1/2\). Let \(\xi=(u+v,u-v)\), \(\eta=(-u+v,-u-v)\). The factorization
\[
P(e^{2\pi ix},e^{2\pi iy})=2e^{\pi i(x+y)}\bigl[a\cos\pi(x+y)+b\cos\pi(x-y)\bigr]
\]
shows \(P\) vanishes at the frequency differences \(\xi,\eta,\xi-\eta\). Indeed the first two give \(aC+b(-C/r)=0\), and the third gives \(a\cos(4\pi u)+b=a(2C^2-1)+b=0\). If \(b\ge a\), interchange \(a,b\) and the roles of \(u,v\): set \(r=a/b\), \(\cos(2\pi v)=\sqrt{(1-r)/2}\), \(\cos(2\pi u)=-\sqrt{(1-r)/2}/r\), and take \(\xi=(u+v,u-v)\), \(\eta=(u-v,u+v)\). The same identity verifies all three differences. Hence \(\{0,\xi,\eta\}\) is orthogonal throughout \(T_1\), with the endpoints included.

**Nondegenerate Fourier-zero locus.** Suppose \((H,J)\ne(0,0)\). If \(J=0\), the pair criterion fails, so suppose \(J\ne0\). Every zero must have \(\operatorname{Re}(z)=-H/(2J)\). Unless \(z=-1\) and \(a=b,c=d\), a zero uniquely determines \(w=-(a+bz)/(c+dz)\). Thus the unit-torus zero set has at most two points \(t,-t\) as a subset of \(\mathbb T^2\) (using additive phase notation), related by complex conjugation. In the exceptional denominator-zero case \(a=b,c=d\), \(a\ne c\), one has \(P(z,w)=(1+z)(a+cw)\): the only zeros form the line \(z=-1\), and the same parity argument above forbids a triple.

For a zero set of at most the two points \(\{t,-t\}\), an orthogonal triple translated to include zero must have other points \(t,-t\) (if both are present). Their difference \(2t\) must also be a zero, forcing \(2t=-t\), i.e. \(3t=0\) in \(\mathbb T^2\). Since \(P(1,1)=1\), \(t\ne0\), so each coordinate phase is a cube root of unity. If \(z=1\), then \(P(1,w)=(a+b)+(c+d)w=0\) forces \(w\) to be the negative real number \(-(a+b)/(c+d)\). Because \(|w|=1\), it would have to be \(-1\), not a cube root of unity. The case \(w=1\) is symmetric. Thus both coordinates belong to \(\{\omega,\omega^2\}\), where \(\omega=e^{2\pi i/3}\).

If \(z=w=\omega\), the equation is \(a+(b+c)\omega+d\omega^2=0\). The only real linear relation between \(1,\omega,\omega^2\) is their sum, so \(a=d=b+c\), which is \(T_2\). If \(z=\omega,w=\omega^2\), then \(P(z,w)=(a+d)+b\omega+c\omega^2=0\), giving \(b=c=a+d\), which is \(T_3\). Their conjugates yield the same mass conditions. Conversely under \(T_2\) the frequencies \(\{(0,0),(1/3,1/3),(2/3,2/3)\}\) are orthogonal, and under \(T_3\) the frequencies \(\{(0,0),(1/3,2/3),(2/3,1/3)\}\) are orthogonal. Thus no further three-character cases exist. Combining this fact with the pair and four-character criteria proves the ordered classification. \(\square\)

## Verification
The self-contained standard-library script `CHECK.py` checks the stated mass predicates on every positive-integer weight quadruple with coefficients from one through twelve, verifies numerical unit-torus zeros whenever the generic formula applies, and tests explicit three-frequency constructions for hundreds of nonuniform ratios and both torsion-resonance families. Its completed run reports `PASS: 20736 positive integer weight quadruples; 336 nonuniform constructed zero relations; 722 order-three resonance verifications`. The entire real-parameter theorem is established by the preceding analytic argument; these finite checks are supplementary and do **not** prove exhaustive equivalence over real masses.

## Relationship to prior work
Fu and Song's 2026 finite-Hadamard-pair rationality theorem concerns complete unweighted finite spectral pairs, not maximum cardinality of incomplete orthogonal families for a positive four-mass measure. Li and Wang's 2026 work on orthogonal exponential cardinalities concerns infinite self-affine measures in dimension three, rather than four positive atoms in a planar parallelogram. A published classification of Fourier-zero **counts** for equal-modulus coefficients on cyclic product grids includes the same four-point rectangle as an algebraic support but does not treat arbitrary positive weight quadruples or three mutually orthogonal real-frequency characters. In particular, none of these inspected results yields the three-locus classification by an implication.

## Limitations
Strict positivity, the affine-parallelogram support, and unrestricted real frequencies are substantive hypotheses. Integer-only frequency sampling gives a different problem. The result determines the largest family size and demonstrates existence of each maximum, but does not enumerate all maximum-cardinality frequency sets. No claim is made for more than four sites, arbitrary quadrilateral support or every inclusion-maximal orthogonal family. An older weighted trigonometric/quadrature formulation of the same theorem could exist without appearing under these search terms; independent bibliographic evaluation has not been performed.

## References
1. Fu and Song, *Rational Spectra for Finite Hadamard Pairs and Bounded Spectral Sets on the real line*, arXiv:2607.19858, first submitted 22 July 2026, https://arxiv.org/abs/2607.19858.
2. Li and Wang, *The Number of Orthogonal Exponential Functions of a Class of Self-Affine Measures in \(\mathbb R^3\)*, *Axioms* 15(8), 563, first published 29 July 2026, https://doi.org/10.3390/axioms15080563.
3. *Phase-only Fourier-zero spectrum of a four-point rectangle on cyclic product groups*, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-phase-only-fourier-zero-spectrum-of-a-four-point-rectangle-on-cy--b51ecb1779fe.
