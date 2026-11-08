# Complete third-order Fourier-minor rank incidence for distinct-prime cyclic products

## Finding
Let \(p\ne q\) be primes, including the case where one equals \(2\). Put \(G=\mathbb Z_p\times\mathbb Z_q\), \(N=pq\), and take the unnormalized Fourier character table
\[
F_{(a,b),(c,d)}=\exp(2\pi i(ac/p+bd/q)).
\]
For every pair of distinct three-element sets \(R,C\subseteq G\), let \(F[R,C]\) be the corresponding complex \(3\times3\) submatrix. There are exactly \(T^2\) such row-set/column-set pairs, where \(T=\binom{pq}{3}\).

**Complete rank incidence.** Define
\[
\begin{aligned}
X&=p\binom q3,&Y&=q\binom p3,\\
A&=T-q^3\binom p3,&B&=T-p^3\binom q3.
\end{aligned}
\]
The exact counts of rank one, rank two, and rank three are respectively
\[
\boxed{R_1=2XY,\qquad R_2=2(XB+YA-2XY),\qquad R_3=T^2-R_1-R_2.}
\]
Equivalently,
\[
\boxed{R_1=\frac{p^2q^2(p-1)(p-2)(q-1)(q-2)}{18}}
\]
and
\[
\boxed{R_2=\frac{p^2q^2(p-1)(q-1)}6
 (p^2q+pq^2-6pq+2p+2q).}
\]
Thus rank-one minors occur precisely when **both** primes are odd (the prime \(2\) gives none). The formulas are symmetric under exchanging \(p\) and \(q\). In particular \(\operatorname{rank}F[R,C]\) is completely determined by two simple residue-incidence rules below, without evaluating a determinant.

For a triple \(S\subseteq G\), call it \(p\)-pure if its three first coordinates agree, \(q\)-pure if its three second coordinates agree; call it \(p\)-colliding if two first coordinates agree, and \(q\)-colliding if two second coordinates agree. Then
\[
\begin{aligned}
\operatorname{rank}F[R,C]=1\quad\Longleftrightarrow\quad
 &(R\text{ is }p\text{-pure and }C\text{ is }q\text{-pure})\\
 &\text{or }(R\text{ is }q\text{-pure and }C\text{ is }p\text{-pure});
\end{aligned}
\]
and the minor is singular if and only if at least one of the following four conditions holds:
\[
\begin{gathered}
R\ p\text{-pure},\ C\ q\text{-colliding};\quad
R\ q\text{-colliding},\ C\ p\text{-pure};\\
R\ q\text{-pure},\ C\ p\text{-colliding};\quad
R\ p\text{-colliding},\ C\ q\text{-pure}.
\end{gathered}
\]
Any singular minor not satisfying the rank-one criterion has rank two.

The special case \(p=2\) reduces to the previously established rank-two-only semiprime formula; for odd distinct primes the additional rank-one sector has strictly positive multiplicity. For instance, at \((p,q)=(3,5)\) the triple-rank distribution is \((300,13800,192925)\) among \(455^2=207025\) pairs.

## Assumptions and scope
The matrix entries have unit complex modulus. A selected row set and a selected column set are each *unordered* three-point subsets, while a pair \((R,C)\) distinguishes rows from columns. All ranks use ordinary exact complex linear algebra; the unnormalized character-table convention fixes the entries but has no effect on rank. The group is isomorphic to the cyclic group \(\mathbb Z_{pq}\), with index permutations under the Chinese remainder theorem. Distinctness of the primes is essential for the simple two-coordinate collision classification. The rule includes \(p=2\) and \(q=2\) using \(\binom 23=0\).

## Proof
**1. Unit-modulus rigidity.** Every \(3\times3\) matrix with unit-modulus entries and zero determinant has two proportional rows or two proportional columns. To see this, normalize the first row and column to ones, producing
\[
M=\begin{pmatrix}1&1&1\\1&u&v\\1&w&t\end{pmatrix},\quad
|u|=|v|=|w|=|t|=1.
\]
The determinant equation is \((u-1)(t-1)=(v-1)(w-1)\). If either side is zero, a direct check of the zero factors yields a repeated row or column. Otherwise conjugating the equation and using \(\overline{z-1}=-(z-1)/z\) for unit \(z\), then dividing by the nonzero original equation, gives \(ut=vw\). Substitution gives \(u+t=v+w\). Equal sums and products force the multisets \(\{u,t\}\) and \(\{v,w\}\) to agree. This yields equal second/third columns or equal second/third rows. Conversely such proportionalities imply singularity. This elementary lemma is previously established in the Fourier-minor literature and is used here, not asserted as a new general theorem.

**2. Character annihilation and the complete rank rule.** Two different character-table rows \(r,r'\in G\) restrict proportionally to \(C\) exactly when the character \(\chi_{r-r'}\) is constant on \(C\). Equivalently, for every \(c,c'\in C\), both congruences
\[
(r_p-r'_p)(c_p-c'_p)=0\pmod p,\qquad
(r_q-r'_q)(c_q-c'_q)=0\pmod q
\]
hold. The two prime-order root factors must separately equal one, because their orders are coprime. If \(r-r'\) is nonzero in both coordinates, the congruences force all three elements of \(C\) to coincide, impossible. Otherwise precisely one coordinate of \(r-r'\) vanishes, and \(C\) must be pure in the other coordinate. The transpose gives the analogous proportional-column condition. Therefore the four displayed collision/purity alternatives are necessary and sufficient for singularity by Step 1.

A minor has rank one exactly when **all** selected rows become proportional, equivalently all the selected columns do. If two independent types of row difference occurred, all column differences would vanish in both coordinates, contradicting the three-point condition. Thus a rank-one minor must have a pure triple in one coordinate and the opposing pure triple in the other; these configurations are easily seen to have rank one. This proves the full three-rank classification.

**3. Count the incidence sets.** There are \(T=\binom{pq}{3}\) triples. Exactly \(X=p\binom q3\) are \(p\)-pure, and \(Y=q\binom p3\) are \(q\)-pure. Exactly \(A=T-q^3\binom p3\) are \(p\)-colliding, since the complement selects three distinct first coordinates and one of \(q\) second coordinates for each. Similarly \(B=T-p^3\binom q3\) are \(q\)-colliding. Pure triples in the first and second coordinates cannot overlap because their three points are distinct. Also a \(p\)-pure triple cannot be \(q\)-colliding and conversely.

The four singularity alternatives in Step 2 contribute in total \(2XB+2YA\) pairs before intersections. The only nonempty pairwise intersections are the two opposite-purity configurations, each of cardinality \(XY\); there are no triple intersections. Hence the total number of singular minors is \(2(XB+YA-XY)\). The two disjoint rank-one configurations contribute \(2XY\), leaving \(R_2=2(XB+YA-2XY)\). Subtracting from \(T^2\) gives \(R_3\). Expanding and factoring gives the two stated polynomial formulas. All steps hold even if one prime is two.

## Verification
An independently executable C++17 program `checker.cpp` uses exact cyclotomic arithmetic, without tolerances or reliance on the preceding rigidity argument. For a fixed prime product \(N\), it constructs the monic cyclotomic polynomial
\[
\Phi_{pq}(z)=\frac{(z^{pq}-1)(z-1)}{(z^p-1)(z^q-1)}
\]
by exact integer polynomial division, and reduces all powers \(\zeta_N^j\) to its degree-\((p-1)(q-1)\) integer basis. For every pair of three-point sets it computes an exact determinant via the six-term formula and tests its vanishing coefficient by coefficient; rank one is separately checked through the four normalized phase exponents. Separately it evaluates the combinatorial classification and compares it against the exact rank of each submatrix.

Compile and run with `c++ -O3 -std=c++17 checker.cpp -o checker && ./checker`. Successful complete enumerations were obtained for \((p,q)=(2,5),(3,5),(3,7)\), with respective rank distributions \((0,1600,12800)\), \((300,13800,192925)\), and \((1470,91728,1675702)\). The program prints `ODD_SEMIPRIME_3X3_EXACT_TESTS_PASS`. These finite checks are independent corroboration; the universal quantifiers follow from Steps 1–3.

## Relationship to prior work
The earliest publicly dated motivating source used here is Bonami and Ghobber's arXiv:1003.5060v1 (2010-03-26). Their work concerns the sharp *support-size minima and equality cases* for Fourier uncertainty on \(\mathbb Z_p\times\mathbb Z_q\), not the complete third-minor rank incidence. The earlier KU Leuven report TW477 by Delvaux and Van Barel (dated November 2006, later published in 2007) develops rank-deficient Fourier-Kronecker blocks, subgroup tilings, and extremal Hamming numbers; its inspected results do not enumerate all third-order row/column restrictions. Loukaki's later arXiv:2412.08600 gives sufficient nonvanishing conditions, especially for principal minors and certain residue-balanced selections, rather than the exact full rank count here.

The published *Singular three-by-three Fourier minors on even semiprime cycles* already establishes the \(p=2\) boundary case, and the present formulas reproduce its count exactly. The published *Complete three-by-three Fourier-minor rank geometry on prime affine planes* uses the same elementary unit-modulus rigidity but treats \(\mathbb F_p^2\), not the distinct-prime group. Neither establishes the new odd-odd semiprime rank-one sector and full two-prime census as stated here. An implicit stronger classification in the broader literature remains possible; no historical uniqueness is claimed.

## Limitations
Only minors of size exactly three, and only cyclic groups of order the product of two **distinct primes**, are classified. This does not establish a corresponding formula for repeated factors, general squarefree integers with at least three prime factors, or larger minors. An arbitrary pair of primes is handled by the proof, while the checker exhausts only the three listed finite examples. The determinant-rigidity ingredient is preexisting and is not independently novel. The originality assessment is bounded by the inspected literature and does not constitute independent historical or mathematical certification.

## References
1. A. Bonami and S. Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060v1, first posted 2010-03-26; full-text inspection of v2: https://arxiv.org/html/1003.5060v2.
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven Report TW477, 2006; published in Linear Algebra and its Applications 426 (2007), 349–367. Accessible full report text: https://citeseerx.ist.psu.edu/document?doi=8e34019b75494fa56d9b8791527fcaed304a7ff9&repid=rep1&type=pdf.
3. M. Loukaki, *Chebotarev's theorem for groups of order pq and an uncertainty principle*, arXiv:2412.08600v5, https://arxiv.org/html/2412.08600v5.
4. *Singular three-by-three Fourier minors on even semiprime cycles*, public mathematical finding, 2026-10-11, reference ID `8f025c6183d3`.
5. *Complete three-by-three Fourier-minor rank geometry on prime affine planes*, public mathematical finding, 2026-10-11, reference ID `ba0b52ec4cec`.
