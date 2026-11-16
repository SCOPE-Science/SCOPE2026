# Sharp dyadic Fourier divisibility and the first singular rank of binary projective matroid bases

## Finding
Let \(r\ge1\), let \(V=\mathbb F_2^r\), and put \(E=V\setminus\{0\}\). Let \(\mathcal B_r\) be the unordered \(r\)-element vector-space bases of \(V\), considered as subsets of \(E\). For each frequency \(S\subseteq E\), define the unnormalized Walsh multiplier
\[
W_r(S)=\sum_{B\in\mathcal B_r}(-1)^{|B\cap S|}.
\]
The exact common divisor of all these integer multipliers is
\[
\gcd_{S\subseteq E}W_r(S)=
\begin{cases}
1,&r=1,2,\\
4,&r=3,\\
8,&r=4,\\
2^r,&r\ge5.
\end{cases}
\]
For every \(r\ge5\), write \(c_r(S)\) for the number of bases contained in \(S\). A stronger frequency-by-frequency congruence holds:
\[
W_r(S)\equiv(-2)^r c_r(S)\pmod{2^{r+1}}.
\]
It is sharp: if \(S\) is any basis, the multiplier has exact two-adic valuation \(r\). When \(r\le4\), every multiplier is nonzero. At \(r=5\), an explicit frequency gives zero, so rank five is the first singular rank for counting convolution by the basis-incidence indicator on \(\mathbb F_2^E\).

## Assumptions and scope
The ground set contains all \(2^r-1\) nonzero binary column vectors with no identification except equality. Independence and basis are over \(\mathbb F_2\). The sign of a basis is the product of the independently selected point signs. The underlying convolution is unnormalized counting convolution on the finite additive group \(\mathbb F_2^E\); its eigenvalues, with Walsh characters indexed by \(S\subseteq E\), are precisely \(W_r(S)\). The gcd is the positive gcd of all signed eigenvalues; it need not be their smallest positive absolute value. No singularity assertion is made for every rank above five.

## Proof
**1. The signed extension identity.** For any \(S\subseteq E\), expand
\[
(-1)^{|B\cap S|}=\prod_{v\in B\cap S}(1-2)
=\sum_{I\subseteq B\cap S}(-2)^{|I|}.
\]
Let \(c_k(S)\) denote the number of linearly independent \(k\)-subsets of \(S\), with \(c_0(S)=1\). Every independent \(k\)-set extends to exactly
\[
N_k(r)=\frac{\prod_{j=k}^{r-1}(2^r-2^j)}{(r-k)!}
\]
unordered bases: enumerate ordered supplementary vectors and divide by their permutation count. A dependent set extends to none. Consequently, for every \(S\),
\[
W_r(S)=\sum_{k=0}^{r}(-2)^k c_k(S)N_k(r).\tag{1}
\]
In particular, \(N_0(r)\) is the total number of bases.

**2. Exact dyadic divisibility in every rank at least five.** All factors \(2^{r-j}-1\) are odd, so
\[
\nu_2\bigl(2^kN_k(r)\bigr)
=k+\frac{(r-k)(r+k-1)}2-\nu_2((r-k)!).
\]
Writing \(s=r-k\) gives
\[
\nu_2\bigl(2^{r-s}N_{r-s}(r)\bigr)
=r+\frac{s(2r-s-3)}2-\nu_2(s!).\tag{2}
\]
If \(r\ge5\) and \(1\le s\le r\), then \(2r-s-3\ge r-3\ge2\). Also \(\nu_2(s!)\le s-1\). Thus the expression in (2) is at least \(r+1\) whenever \(k<r\). At \(k=r\), \(N_r(r)=1\). Reducing (1) modulo \(2^{r+1}\) proves the stated congruence. Choosing \(S\) itself to be a basis yields \(c_r(S)=1\), so \(W_r(S)\) has valuation exactly \(r\). This establishes the gcd for all \(r\ge5\).

**3. Small-rank boundary.** In ranks one and two the total number of bases is respectively \(1\) and \(3\), hence every signed sum is odd and the gcd is one. For rank three, the extension counts \((N_0,N_1,N_2,N_3)=(28,12,4,1)\) give \(W_3(S)\equiv4\pmod8\). For rank four, the counts \((840,224,48,8,1)\) give \(W_4(S)\equiv8\pmod{16}\). The constant terms attain the indicated exact valuations. Thus all multipliers are nonzero for ranks at most four, and their gcd values are those claimed.

**4. An exact rank-five zero.** Fix standard unit vectors \(e_1,\ldots,e_5\) and put
\[
S=\bigl(\operatorname{span}(e_1,e_2,e_3)\setminus\{0\}\bigr)\cup\{e_4,e_5\}.
\]
This nine-point set has independent-subset counts
\[
(c_0,c_1,c_2,c_3,c_4,c_5)=(1,9,36,77,77,28).
\]
Indeed, the seven nonzero vectors of the three-dimensional subspace have respective independent counts \((1,7,21,28)\); each of the two extra unit vectors may be selected independently. The rank-five extension counts are
\[
(N_0,N_1,N_2,N_3,N_4,N_5)=(83328,13440,1792,192,16,1).
\]
Substitution into (1) gives the exact cancellation
\[
W_5(S)=83328-241920+258048-118272+19712-896=0.
\]
Therefore rank five is singular; the previous paragraph shows it is the first such rank. \(\square\)

## Verification
The accompanying standalone Python checker directly enumerates all rank-four bases, constructs their complete Boolean indicator in dimension fifteen, applies an exact Walsh--Hadamard transform at all \(32768\) frequencies, and checks nonvanishing and the congruence modulo sixteen. Its exact rank-four multiplier histogram is \(\{-56:3000,-40:2016,-8:6720,8:15120,24:5600,72:70,136:210,392:30,840:2\}\).

A second path directly enumerates all \(83328\) rank-five bases and evaluates the explicit signed witness, independently of the extension-count calculation. It checks a basis-sized negative set whose multiplier has valuation five. A separate arithmetic loop tests the valuation formula through rank 64; the all-rank result is proved symbolically above, not extrapolated from this loop. Run `python3 pg_basis_fourier_check.py` with Python 3 and no third-party packages. Successful output ends with `PG_BINARY_BASE_FOURIER_PASS`.

## Relationship to prior work
Binary projective geometries and their basis-generating polynomials are classical. Brändén and González D'León (arXiv:0906.1071, 2009) prove that projective geometries fail the weak half-plane property; this is an analytic stability question and does not determine evaluations at all real sign vectors. Kordecki (arXiv:1305.3119, 2013) studies perfect matroid designs, including projective geometries, and counts hyperplanes and circuits relative to a basis. The present statement instead evaluates the dyadic content of all independently signed basis enumerators and identifies the first rank with an exact sign cancellation. Previously derived Fourier congruences for Fano-plane complementary triples account for the rank-three boundary, not the higher-rank statement.

## Limitations
The exact congruence controls dyadic valuations, not the complete multiplier distribution at arbitrary ranks. Invertibility is proved for ranks at most four, and singularity is exhibited at rank five; behavior of every higher rank is not determined. No sharp endpoint projection constant or complete nullity is claimed. The literature comparison is bounded and cannot establish exhaustive historical priority. There has been no independent external mathematical audit.

## References
1. Petter Brändén and Rafael S. González D'León, *On the half-plane property and the Tutte group of a matroid*, arXiv:0906.1071, first posted 2009-06-05. https://arxiv.org/abs/0906.1071
2. Wojciech Kordecki, *Hyperplanes and hamiltonian circuits in Perfect Matroid Designs with fixed basis*, arXiv:1305.3119, first posted 2013-05-14. https://arxiv.org/abs/1305.3119
