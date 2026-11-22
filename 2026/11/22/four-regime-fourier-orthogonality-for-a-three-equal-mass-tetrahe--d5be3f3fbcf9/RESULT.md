# Four-regime Fourier orthogonality for a three-equal-mass tetrahedral measure

## Finding
Let \(x_1,x_2,x_3,x_4\in\mathbb R^3\) be affinely independent and \(0<t<1\). Put \(s=(1-t)/3\) and \(\mu_t=s\sum_{j=1}^3\delta_{x_j}+t\delta_{x_4}\). Let \(\mathcal O(\mu_t)\) denote the maximum cardinality of a pairwise orthogonal set of Fourier characters \(e_\xi(x)=e^{2\pi i\langle\xi,x\rangle}\), \(\xi\in\mathbb R^3\), in \(L^2(\mu_t)\). Then
\[
\mathcal O(\mu_t)=\begin{cases}
3,&0<t<1/4,\\
4,&t=1/4,\\
2,&1/4<t\le 1/2,\\
1,&1/2<t<1.
\end{cases}
\]
The result is invariant under invertible affine changes of the tetrahedron. It classifies maximal **cardinalities**, not all attaining frequency triples.

## Assumptions and scope
Every weight is strictly positive, and the four sites are affinely independent in \(\mathbb R^3\). Frequencies are arbitrary real vectors (not restricted to an integer lattice). A character is normalized automatically because \(\mu_t\) is a probability measure. The endpoint masses \(t=0,1\) are excluded. The primary mathematical setting is orthogonal exponential families and finite Fourier frames.

## Proof
**Phase realization.** For each column of any \(4\times m\) matrix whose row \(j\) has entries of constant modulus \(\sqrt{w_j}\) and whose columns are orthonormal, choose row phases to make the first column \((\sqrt{w_j})_{j=1}^4\). For each other column, subtract its fourth-site phase. Since the three vectors \(x_j-x_4\) are a real basis, there exists \(\xi\in\mathbb R^3\) realizing any prescribed three relative phases. Hence such a matrix is equivalent to \(m\) orthogonal Euclidean characters.

**One versus two.** Two unit-modulus vectors with weighted zero inner product exist precisely when the four masses can form a closed planar quadrilateral, i.e. when the largest mass does not exceed half their total. Because \(s<1/3\), this is precisely \(t\le1/2\). The necessity follows from the triangle inequality, while sufficiency follows by varying the resultant length of three planar segments: its possible lengths include \(t\) exactly under the polygon inequality. If \(t>1/2\), only one character is possible.

**Four.** A \(4\times4\) matrix of orthonormal columns is unitary. Its row squared norms are one, but every entry in row \(j\) has squared modulus \(w_j\); hence \(4w_j=1\) for each row. Thus four characters require \(t=s=1/4\). Conversely a normalized Fourier matrix of order four, transferred by phase realization, gives four characters when all weights are equal.

**Construction of three for \(0<t\le1/4\).** Write \(\tau=t/s=3t/(1-t)\le1\), \(z=e^{i\theta}\), and \(\theta=\arccos(-(1+\tau)/2)\). Consider
\[
H=\begin{pmatrix}1&1&z\\ z&1&1\\1&z&1\end{pmatrix},\qquad
U=\begin{pmatrix}\sqrt{s}&\sqrt{s}&\sqrt{s}z\\ \sqrt{s}z&\sqrt{s}&\sqrt{s}\\ \sqrt{s}&\sqrt{s}z&\sqrt{s}\\ \sqrt t&\sqrt t&\sqrt t\end{pmatrix}.
\]
Each diagonal of \(H^*H\) equals three, and each off-diagonal equals \(1+2\cos\theta=-\tau\). Consequently \(U^*U=(3s+t)I_3=I_3\). Each row of \(U\) has its prescribed constant entry modulus, so phase realization supplies an orthogonal triple.

**No triple when \(1/4<t\le1/2\).** If \(t>1/3\), a four-row, three-column column-isometry would have last-row squared norm \(3t>1\), impossible. Suppose \(1/4<t\le1/3\) and such an isometry \(U\) exists. Complete \(U\) to a \(4\times4\) unitary \(W\). Gauge its row and column phases so that the top three entries of column four and the first three entries of row four all equal \(\sqrt t\). Write the upper-left block as \(\sqrt s H\). Unitarity implies
\[
HH^*=H^*H=\frac1s I_3-\tau J_3,\qquad \tau=\frac ts>1,
\]
where \(J_3\) is the all-ones matrix. In particular \(H\) is normal, commutes with \(J_3\), and all its row and column sums equal some \(\eta\) satisfying
\[
|\eta|^2=\frac{1-3t}{s}<1.
\]
Let the first row of \(H\) be \((a,b,c)\), where all three values have modulus one. They are pairwise distinct: two equal unit numbers plus a third unit number have sum modulus at least one. No two are antipodal either, since their sum would vanish and the total row sum would have modulus one.

Every column sums to \(\eta=a+b+c\). Fixing its first-row entry, the remaining two entries are unit numbers whose sum is the corresponding nonzero sum of the other two first-row entries. Such an unordered pair is unique: it is the pair of intersections of the unit circle with the circle centered at that nonzero sum. Each column is therefore a permutation of \((a,b,c)\). Every row also has three distinct entries, by \(|\eta|<1\), so each row is a permutation. A three-by-three Latin square is equivalent by row and column permutations to the cyclic square. Thus some distinct rows of \(H\) have scalar product \(\rho=a\bar b+b\bar c+c\bar a\) or \(\bar\rho\), while the off-diagonal Gram entry is \(-\tau\). Hence \(\rho=-\tau\).

Set \(u=a\bar b\), \(v=b\bar c\), \(w=c\bar a\). Then \(|u|=|v|=|w|=1\), \(uvw=1\), \(u+v+w=-\tau\), and \(uv+uw+vw=\overline{u+v+w}uvw=-\tau\). They must be roots (with multiplicity) of
\[
X^3+\tau X^2-\tau X-1=(X-1)(X^2+(1+\tau)X+1).
\]
The last quadratic has both roots on the unit circle only if \(1+\tau\le2\), contradicting \(\tau>1\). Hence no triple exists in this regime. The pair construction completes the classification.

## Verification
The supplied `verify.py` checks the exact algebraic identity of the three-column construction at multiple rational weights, the phase Gram relation, the polynomial factorization, the strict forbidden threshold, and an explicit four-column Fourier unitary at equal weights. These calculations support, but do not replace, the analytic necessity argument; the proof applies to all real \(t\in(0,1)\).

## Relationship to prior work
Fu and Song (arXiv:2607.19858, first public July 22, 2026) treat **complete unweighted** spectral pairs on the line and rational frequency rigidity. Their fully accessible paper's introduction, definitions, and main proofs address square unitary generalized-Vandermonde matrices; they do not derive the number of columns possible for unequal-weight four-atomic measures on an affinely independent tetrahedron. Li and Wang (2026) study infinite self-affine measures in three dimensions with distinct scaling hypotheses; their four-exponential bounds do not imply the present finite weighted classification. Known paired-mass tetrahedral results with weights \((a,a,b,b)\) do not imply the \((s,s,s,t)\) statement except at the uniform intersection. The present theorem uses a three-column partial complex Hadamard/isometry obstruction rather than a complete spectral pair theorem.

## Limitations
Only the four cardinality regimes are classified; no all-frequency parametrization is claimed. It excludes dependent sites, fewer than four positive masses, general unrelated weights, and lattice-restricted characters. Classical literature on weighted partial complex Hadamard matrices and partial unistochastic matrices may contain equivalent formulations; no independence or external certification is claimed.

## References
1. X.-Y. Fu and Z.-J. Song, *Rational Spectra for Finite Hadamard Pairs and Bounded Spectral Sets on the real line*, arXiv:2607.19858, first public July 22, 2026. https://arxiv.org/abs/2607.19858
2. Y.-Q. Li and Z.-M. Wang, *The Number of Orthogonal Exponential Functions of a Class of Self-Affine Measures in R3*, Axioms 15 (2026), 563. https://doi.org/10.3390/axioms15080563
