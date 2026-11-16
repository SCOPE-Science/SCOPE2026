# A four-class Paley sampling law for four consecutive Fourier characters

## Finding

Let \(p\equiv1\pmod4\) be prime, let \(Q_p\subset\mathbb Z/p\mathbb Z\) consist of the nonzero quadratic residues, and define the quadratic-residue Fourier observation map
\[
(T_pa)(x)=p^{-1/2}\sum_{j=0}^{3}a_j e^{2\pi i jx/p},\qquad x\in Q_p,\quad a\in\mathbb C^4.
\]
Set \(G_p=T_p^*T_p\) and \(h=\sqrt p\). The **complete squared-singular-value spectrum** of this four-channel sampling map has exactly the following four arithmetic forms (multiplicities in brackets):

| Prime residue | Complete spectrum of \(G_p\) |
|---|---|
| \(p\equiv1\pmod{24}\) | \((p-h)/(2p)\) [3]; \((p+3h-4)/(2p)\) [1] |
| \(p\equiv5\pmod{24}\) | \((p-2\pm\sqrt{p+4})/(2p)\); \((p\pm\sqrt{5p})/(2p)\) [all one except coincidences at \(p=5\)] |
| \(p\equiv13\pmod{24}\) | \((p-3h)/(2p)\) [1]; \((p+h-4)/(2p)\) [1]; \((p+h)/(2p)\) [2] |
| \(p\equiv17\pmod{24}\) | \((p-2\pm\sqrt{5p-8h+4})/(2p)\); \((p\pm h)/(2p)\) [all one] |

In particular, \(T_p\) has full column rank for every allowed \(p\ge13\), while \(p=5\) has a two-dimensional kernel. The sharp lower-frame eigenvalue \(A_p\) is, in the order of the four table rows,
\[
\frac{p-h}{2p},\qquad
\frac{p-\sqrt{5p}}{2p},\qquad
\frac{p-3h}{2p},\qquad
\frac{p-2-\sqrt{5p-8h+4}}{2p}.
\]
For \(p\ge13\), the sharp squared condition number \(B_p/A_p\) is respectively
\[
\frac{p+3h-4}{p-h},\qquad
\frac{p+\sqrt{5p}}{p-\sqrt{5p}},\qquad
\frac{p+h}{p-3h},\qquad
\frac{p-2+\sqrt{5p-8h+4}}{p-2-\sqrt{5p-8h+4}}.
\]
The three possible leading deficits are sharp:
\[
2\sqrt p\,(1/2-A_p)\longrightarrow
\begin{cases}
1,&p\equiv1\pmod{24},\\
\sqrt5,&p\equiv5\text{ or }17\pmod{24},\\
3,&p\equiv13\pmod{24},
\end{cases}
\]
with limits along the indicated prime progressions.

For \(p\ge13\), a nonzero coefficient vector attaining \(A_p\) is characterized up to scalar as follows: the entire three-dimensional hyperplane \(\sum_{j=0}^3a_j=0\) for class \(1\); the line through \((1,-\varphi,\varphi,-1)\) for class \(5\), where \(\varphi=(1+\sqrt5)/2\); the line through \((1,-1,1,-1)\) for class \(13\); and the line through \((1,-r_p,-r_p,1)\) for class \(17\), where
\[
r_p=\frac{\sqrt{5p-8\sqrt p+4}-\sqrt p}{2(\sqrt p-1)}.
\]
For \(p=5\), the lower eigenspace is the two-dimensional kernel of the two-row sampling matrix.

## Assumptions and scope

The cyclic-group character is normalized as \(e^{2\pi i jx/p}\). Row measure is the counting measure and each character column is scaled by \(p^{-1/2}\), so \(\|T_pa\|_2^2=a^*G_pa\) and the full-cyclic Fourier family would have squared norm \(\|a\|_2^2\). The four frequency indices are exactly \(\{0,1,2,3\}\), and the sampling locations are the \((p-1)/2\) nonzero squares, without the zero-frequency sensing row used in the augmented Paley matrix. Only odd primes congruent to one modulo four are asserted.

The choice of four characters is intrinsic: it is the shortest consecutive band simultaneously seeing the independent quadratic characters of the gaps \(2\) and \(3\); these yield all four prime residue classes modulo \(24\). The lowest concentration eigenvalue is the worst-observed coefficient direction for this precise four-channel design.

## Proof

**Character-sum reduction.** Write \(\chi_p\) for the quadratic character, including \(\chi_p(0)=0\). For \(d\ne0\pmod p\), the classical quadratic Gauss sum with the indicated positive-exponent convention gives
\[
\sum_{x\in Q_p}e^{2\pi i dx/p}
=\frac{-1+\sqrt p\,\chi_p(d)}2,
\qquad p\equiv1\pmod4.
\]
This follows, for instance, by writing twice the sum as \(\sum_{x\ne0}(1+\chi_p(x))e^{2\pi i dx/p}\) and applying the positive real Gauss-sum evaluation \(\sum_x\chi_p(x)e^{2\pi ix/p}=\sqrt p\). The latter evaluation, including its sign, is also given as the equivalent quadratic-sum identity in Satake's Lemma 11 and is classical. Since \(\chi_p(-d)=\chi_p(d)\), the Gram matrix is real symmetric. Put \(t=\chi_p(2)\), \(u=\chi_p(3)\), \(J=\mathbf1\mathbf1^{\mathsf T}\), and
\[
S_{t,u}=\begin{pmatrix}
0&1&t&u\\1&0&1&t\\t&1&0&1\\u&t&1&0
\end{pmatrix}.
\]
The diagonal and off-diagonal identities combine into the exact formula
\[
G_p=\tfrac12I_4+\frac{\sqrt p}{2p}S_{t,u}-\frac1{2p}J.
\]
Quadratic reciprocity supplies \((t,u)=(+,+),(-,-),(-,+),(+,-)\) for prime classes \(1,5,13,17\pmod{24}\), respectively.

**Two explicit spectral blocks.** Reflect the coordinates \(0\leftrightarrow3\), \(1\leftrightarrow2\). In the orthonormal even basis \((1,0,0,1)/\sqrt2\), \((0,1,1,0)/\sqrt2\), and odd basis \((1,0,0,-1)/\sqrt2\), \((0,1,-1,0)/\sqrt2\), the matrix splits as
\[
E_{t,u}=\frac12 I_2+\frac{h}{2p}
\begin{pmatrix}u&1+t\\1+t&1\end{pmatrix}
-\frac1p\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
O_{t,u}=\frac12 I_2+\frac{h}{2p}
\begin{pmatrix}-u&1-t\\1-t&-1\end{pmatrix}.
\]
These blocks preserve the original squared norm, and each is diagonalized by its quadratic characteristic polynomial. Substituting the four sign pairs gives all entries in the displayed spectrum table. In class \(1\), the simpler identity \(S=J-I\) yields the one-dimensional constant mode and its three-dimensional orthogonal complement. In class \(13\), \(S=I-ww^{\mathsf T}\) for \(w=(1,-1,1,-1)\), with \(w\perp\mathbf1\).

**Ordering and equality.** For class \(5\), the least eigenvalue comes from the odd block when \(p>5\), since
\[
\sqrt{5p}>2+\sqrt{p+4}\qquad(p>5),
\]
with equality at \(p=5\). Its eigenvector ratio is the negative golden ratio, giving the fixed extremizing vector stated above. In class \(17\), the even negative root is below the odd negative root since
\[
\sqrt{5p-8\sqrt p+4}>\sqrt p-2\qquad(p>1);
\]
and its positive root exceeds the odd positive root for \(p\ge17\) since \(\sqrt{5p-8\sqrt p+4}>\sqrt p+2\) whenever \(\sqrt p>3\). The even-block eigenvector equation gives \(r_p\). For class \(13\), the four eigenvalues are ordered because \(h>1\). In class \(1\), the sum-zero hyperplane has the least eigenvalue. Thus the lower bounds, upper bounds, multiplicities, and equality descriptions are sharp.

**Rank and limits.** Four distinct cyclic characters restricted to at least four distinct row phases form a Vandermonde matrix of column rank four. Hence all primes \(p\ge13\) in the domain are full rank. At \(p=5\) there are exactly two sampling rows, and distinct nodes make its rank two. Dividing the explicit lower bounds and condition numbers by the powers of \(p\) claimed above proves the residue-wise asymptotics. Dirichlet's theorem ensures that each of the four reduced classes modulo \(24\) contains infinitely many primes, so all limits are nonvacuous.

## Verification

Run `python check_paley.py` with Python 3 and NumPy. The script assembles the four columns directly from nonzero square residues, forms the numerical Gram matrix without using the predicted eigenvalue formulas, compares all four eigenvalues against the closed forms for every prime \(p\equiv1\pmod4\) below \(400\), and separately checks the Gauss-character Gram identity and the exceptional two-dimensional kernel at \(p=5\). The reproduced maximal absolute discrepancy is below \(7\times10^{-16}\) over \(37\) tested primes, including all four classes. These finite checks corroborate, but do not substitute for, the Gauss-sum and block-diagonalization proof.

## Relationship to prior work

Waldron (2018) develops the Fourier/Gramian language for group frames. Magsino–Mixon–Parshall (2019) study limiting random-subensemble spectra of Paley conference frames. Satake (2020) defines the augmented quadratic-residue Paley matrix and gives the quadratic Gauss-sum identity and conditional sparse restricted-isometry estimates. The present unaugmented four-column operator is obtained by removing the constant sensing row and restricting to the first four consecutive character columns. The exact removal term \(-J/(2p)\) changes the four spectral branches; random spectral laws and conditional RIP estimates do not imply these exact deterministic low-band eigenvalues or their equality subspaces.

## Limitations

The result is a fixed four-dimensional spectral calculation, not a general restricted-isometry theorem. No sharp claim is made for nonconsecutive frequency sets, arbitrary four-column submatrices, primes congruent to three modulo four, or large frequency-band widths. Exact bibliographic priority outside the inspected specialized sources remains subject to verification.

## References

- S. Waldron, *The Fourier transform of a projective group frame*, arXiv:1806.06067 (first public version 14 June 2018), especially the Gramian framework and primary MSC 42C15. https://arxiv.org/abs/1806.06067
- M. Magsino, D. G. Mixon and H. Parshall, *Kesten–McKay law for random subensembles of Paley equiangular tight frames*, arXiv:1905.04360 (first public version 10 May 2019), especially the conference-matrix construction and Theorem 1. https://arxiv.org/abs/1905.04360
- S. Satake, *On the restricted isometry property of the Paley matrix*, arXiv:2011.02907 (2020), especially Definition 3, Lemmas 11–12 and Theorem 10. https://arxiv.org/abs/2011.02907
