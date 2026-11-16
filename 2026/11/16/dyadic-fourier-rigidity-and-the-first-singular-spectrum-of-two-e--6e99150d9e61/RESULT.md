# Dyadic Fourier rigidity and the first singular spectrum of two-edge complete-graph matchings

## Finding

Let \(n\ge4\), write \(E_n=E(K_n)\), and let \(G_n=\mathbb F_2^{E_n}\). Let \(f_n:G_n\to\{0,1\}\) be the indicator of the edge-incidence vectors of matchings of **exactly two disjoint edges** in the labelled complete graph \(K_n\). Use the unnormalized Walsh transform
\[
 W_n(F)=\sum_{x\in G_n}f_n(x)(-1)^{\langle F,x\rangle},\qquad F\subseteq E_n.
\]
Write \(t=|F|\), let \(q(F)\) count unordered disjoint pairs of edges lying in \(F\), and put \(N=\binom n2\). For the signing \(s_e=(-1)^{\mathbf1_{e\in F}}\), write \(S=\sum_es_e\) and \(d_v=\sum_{e\ni v}s_e\). Then **every multiplier** has the equivalent exact forms
\[
\boxed{W_n(F)=3\binom n4-2\binom{n-2}{2}t+4q(F)
=\frac{S^2-\sum_{v=1}^n d_v^2+N}{2}.}
\]
The gcd of all nonzero absolute multipliers (equivalently the gcd of all integer multipliers) is exactly
\[
\boxed{
\gcd_{F\subseteq E_n}W_n(F)=
\begin{cases}
1,&n\bmod16\in\{4,5,6,7,12,13,14,15\},\\
2,&n\bmod16\in\{0,1,8,9,10,11\},\\
4,&n\bmod16\in\{2,3\}.
\end{cases}}
\]
In the eight odd-cardinality residue classes \(4,5,6,7,12,13,14,15\), all multipliers are odd. In the additional residue classes \(10,11\pmod{16}\), every multiplier is \(2\pmod4\), despite the matching family having even cardinality. Thus convolution by \(f_n\) is invertible in each of these ten residue classes (this is **not** a converse classification in other classes).

At the first singular order \(n=8\), there are exactly \(210\) such matchings and \(2^{28}=268{,}435{,}456\) frequencies. An exhaustive integer classification gives exactly \(20{,}467{,}680\) zero Walsh multipliers, hence
\[
\boxed{\operatorname{rank}T_8=247{,}967{,}776,\quad
\min_{W_8(F)\ne0}|W_8(F)|=2,\quad
\|T_8^\dagger\|_{2\to2}=\tfrac12.}
\]
The maximum absolute multiplier equals \(210\), so the positive-spectrum condition number is exactly \(105\). The entire **signed** multiplier histogram, with \(84\) distinct integers including zero, is given in `walsh_histogram_n8.csv`. No earlier order \(4\le n\le7\) is singular.

## Assumptions and scope

All vertices and edges are labelled. The underlying group \(G_n\) has counting measure, and convolution is \((T_n h)(x)=\sum_{y\in G_n}f_n(y)h(x-y)\). The operator norm and pseudoinverse are on complex counting-measure \(\ell^2(G_n)\). All multiplicities in the CSV count **all** ambient Fourier frequencies; no quotient normalization is used. ``Singular'' means at least one vanishing Walsh multiplier. The exact rank census is only asserted for \(n=8\); the arithmetic identities and sufficient invertibility classes hold for every integer \(n\ge4\).

## Proof

**1. Signed two-matching identity.** There are \(3\binom n4\) unordered disjoint edge pairs. For any such pair \(\{e,e'\}\), its character is \((1-2\mathbf1_{e\in F})(1-2\mathbf1_{e'\in F})\). Summing, each negative edge belongs to \(\binom{n-2}{2}\) pairings and each pair of disjoint negative edges contributes once, giving
\[
W_n(F)=3\binom n4-2\binom{n-2}{2}|F|+4q(F).
\]
Independently, summing products \(s_e s_{e'}\) over all unordered distinct edge pairs gives \((S^2-N)/2\). Summing instead over adjacent pairs gives \(\sum_v(d_v^2-(n-1))/2\), since two distinct adjacent edges in a simple graph share precisely one vertex. Subtracting yields the degree-moment identity.

**2. Arithmetic classification.** Write \(A=3\binom n4\) and \(b=\binom{n-2}{2}\). The exact formula implies that \(g=\gcd(A,2b,4)\) divides every multiplier. Conversely the signings with zero, one, and two **disjoint** negative edges have multipliers \(A\), \(A-2b\), and \(A-4b+4\). Their integer span contains \(A\), \(2b\), and \(4\), hence the gcd of *all* multipliers equals \(g\). Modulo four the formula is \(W_n(F)\equiv A-2b|F|\pmod4\). The residues of \(A\pmod4\) and \(b\pmod2\) depend only on \(n\pmod{16}\): Vandermonde's identity and \(4\mid\binom{16}{j}\) for \(1\le j\le4\) prove the first periodicity, and the parity of \(\binom{n-2}{2}\) has period four. Substitution at the sixteen residues yields the stated gcd and the ten guaranteed nonvanishing classes. For the classes \(0,1,8,9\pmod{16}\), exactly half the frequencies have \(W_n(F)\equiv2\pmod4\), because the parity of \(|F|\) is balanced; in particular their rank is at least \(2^{N-1}\). No assertion of complete singularity classification is made for the other classes.

**3. The first singular instance and its sharp gap.** For \(n=4,5,6,7\), \(3\binom n4\) is odd, hence every coefficient is odd and the operator is invertible. For \(n=8\), take the negative-edge graph to be a seven-edge star. Then \(t=7,q=0\), so \(W_8(F)=210-30\cdot7=0\). Every coefficient is even. To attain the smallest positive magnitude, take six negative star edges from vertex \(0\) to vertices \(1,2,3,4,5,6\), together with negative edges \(\{1,2\}\) and \(\{1,3\}\), leaving vertex \(7\) isolated in the negative-edge graph. Here \(t=8,q=8\), and \(W_8(F)=210-30\cdot8+4\cdot8=2\). Thus \(2\) is the least nonzero absolute coefficient, without computational extrapolation.

**4. Exact finite nullity.** `check_two_matchings.cpp` is a deterministic, self-contained C++17 certificate that enumerates all \(2^{27}\) edge signings with one fixed positive edge and doubles their multiplicities. This reduction is exact: negating every edge sign leaves the product on each two-edge matching invariant and pairs each ambient signing uniquely with one having the distinguished edge positive. The program independently computes the full signed histogram by (A) Gray-code updates of signed vertex degrees and (B) Gray-code updates of the negative-edge count and disjoint negative pairs; it checks equality of the two complete histograms. It also checks 2,048 direct matching sums, cardinality, Parseval, and exact expected integers. The output contains \(20{,}467{,}680\) zeros and \(247{,}967{,}776\) nonzeros. Walsh diagonalization supplies the rank, pseudoinverse norm and condition number.

## Verification

Run `g++ -O3 -std=c++17 check_two_matchings.cpp -o check_two_matchings && ./check_two_matchings`. The first output line must be

`TWO_EDGE_MATCHINGS_K8_PASS total=268435456 zeros=20467680 rank=247967776 min_nonzero=2 max=210 levels=84`

The subsequent CSV lines must agree byte-for-byte with `walsh_histogram_n8.csv` when its header is followed by the program's 84 entries. The histogram satisfies \(\sum_m N_m=2^{28}\) and \(\sum_m m^2N_m=2^{28}\cdot210=56{,}371{,}445{,}760\), the latter being Parseval for a 210-point indicator. The exact zero proportion is \(639615/8388608\). This exhausts only the finite \(n=8\) space; infinite-order conclusions have the separate symbolic proof above.

## Relationship to prior work

Kamat and Misra study fixed-size matching families and an Erdős–Ko–Rado intersection theorem (arXiv:1303.4061v1), which supplies a dated motivating framework but does not evaluate their signed Fourier multiplier multiplicities. Li, Shi and Trinks study the conventional matching polynomial and its reconstruction from graph deletions (arXiv:1404.3469v1); their unsigned matching coefficients do not imply this frequency-by-frequency rank census. Signed graph weights and matching polynomials are classical, so the elementary degree formula is not separately claimed as historically new. The particular complete Fourier nullity at the first singular order, together with the exact mod-four spectral structure and its zero-free even-cardinality classes, is the contribution assessed here. Related complete-graph **perfect-matching** Fourier spectra concern a four-edge matching orbit on eight vertices and do not imply the present two-edge matching distribution.

## Limitations

There is no classification here of zero multipliers in all larger orders, nor of the sharp endpoint \(\ell^1\) Fourier-range projection norm. The finite census relies on an exhaustive exact-integer checker and is not independently audited; the general algebraic identities are proved on paper. Historical priority is assessed by bounded full-text and indexed searches, not by an exhaustive search of all older literature. External independent validation remains unperformed.

## References

1. V. Kamat and N. Misra, *An Erdős--Ko--Rado theorem for matchings in the complete graph*, arXiv:1303.4061v1, publicly posted 2013-03-17. https://arxiv.org/abs/1303.4061
2. X. Li, Y. Shi and M. Trinks, *Polynomial reconstruction of the matching polynomial*, arXiv:1404.3469v1, publicly posted 2014-04-14. https://arxiv.org/abs/1404.3469
3. O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics 25 (1972), 190–232, DOI:10.1007/BF01877590 (classical background, not a source of the Fourier rank census).
