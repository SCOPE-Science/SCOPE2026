# Signed-Jordan orbit counts for involutions anticommuting with nilpotent matrices

## Finding

For every odd prime power \(q\), positive integer \(n\), and nilpotent \(N\in M_n(\mathbb F_q)\) of arbitrary Jordan type \(\lambda=(1^{m_1},2^{m_2},\ldots)\), this result determines the exact number of involutions \(S\) satisfying \(S^2=I\) and \(SN=-NS\), refined by the dimension of their \(+1\) eigenspace. It determines the complete orbit decomposition under conjugation by invertible matrices commuting with \(N\).

Write \(a_i\) for the number of length-\(i\) Jordan chains whose initial vector has sign \(+\), let \(b_i=m_i-a_i\), and range over every \(0\le a_i\le m_i\). Put \(m_{i,0}=a_i\), \(m_{i,1}=b_i\), \(g_d(q)=\prod_{j=0}^{d-1}(q^d-q^j)\) and \(g_0(q)=1\). Define

\[
D=\sum_{i,j\ge1}m_i m_j\min(i,j),\qquad \rho=\sum_i m_i^2,
\]
\[
h(i,j;\sigma,\tau)=\#\{r\in\mathbb Z:\max(0,j-i)\le r<j,\ r\equiv\sigma-\tau\pmod 2\},
\]
\[
E(\mathbf a)=\sum_{i,j\ge1}\sum_{\sigma,\tau\in\{0,1\}}m_{i,\sigma}m_{j,\tau}h(i,j;\sigma,\tau),\qquad
\rho_{\mathbf a}=\sum_i(a_i^2+b_i^2).
\]
All sums are finite because only finitely many \(m_i\) are nonzero. Set
\[
G=q^{D-\rho}\prod_i g_{m_i}(q),\qquad
H(\mathbf a)=q^{E(\mathbf a)-\rho_{\mathbf a}}\prod_i g_{a_i}(q)g_{b_i}(q).
\]
Then the complete \(+1\)-eigenspace-dimension generating polynomial is
\[
\boxed{\mathcal P_{\lambda,q}(z)=
\sum_{\mathbf a}\frac{G}{H(\mathbf a)}
 z^{\sum_i(a_i\lceil i/2\rceil+b_i\lfloor i/2\rfloor)}.}
\]
Each quotient \(G/H(\mathbf a)\) is a positive integer: precisely one conjugacy orbit under the centralizer unit group consists of the signed-Jordan type \(\mathbf a\), and its cardinality is \(G/H(\mathbf a)\). In particular the number of orbits is \(\prod_i(m_i+1)\).

Writing \(L=\sum_i m_i\lfloor i/2\rfloor\) and \(U=\sum_i m_i\lceil i/2\rceil\), the attainable \(+1\)-eigenspace dimensions are **exactly every integer in** \([L,U]\), with no gaps; the polynomial is palindromic of total degree \(n\): \(z^n\mathcal P_{\lambda,q}(1/z)=\mathcal P_{\lambda,q}(z)\).

For equal-size blocks \(\lambda=(s^m)\), write the Gaussian binomial as \({m\brack a}_q\). The general formula specializes to
\[
\mathcal P_{(2h)^m,q}(z)=z^{hm}\sum_{a=0}^{m}q^{hm^2-a(m-a)}{m\brack a}_q
\quad(h\ge1),
\]
\[
\mathcal P_{(2h+1)^m,q}(z)=\sum_{a=0}^{m}q^{hm^2+a(m-a)}{m\brack a}_q z^{hm+a}
\quad(h\ge0).
\]
For instance, \(\mathcal P_{(3,1),3}(z)=3z+54z^2+3z^3\) and \(\mathcal P_{(2,2),3}(z)=270z^2\).

## Assumptions and scope

The field has odd characteristic, so an involution \(S\) is diagonalizable with eigenspaces \(V_+\oplus V_-\). Fix a specific nilpotent operator \(N\), not merely a similarity class; the polynomial counts distinct linear transformations \(S\), not orbits, pairs of unspecified matrices, or signed diagrams. The convention is that \(N\) acts by multiplication by \(t\) on Jordan chains, taking each homogeneous vector to the opposite sign. Chain generators carrying \(+\) sign are counted by \(a_i\). There is no assertion for fields of characteristic two.

## Proof

**1. Homogeneous Jordan decomposition.** The relation \(SN=-NS\) is equivalent to the two-eigenspace grading \(V=V_0\oplus V_1\) for which \(N V_\sigma\subseteq V_{1-\sigma}\). Thus \(V\) is a finite graded module over \(\mathbb F_q[t]\), where \(t\) has degree one, and is annihilated by a power of \(t\). The graded Jordan-chain theorem gives a direct sum of homogeneous cyclic modules \(\mathbb F_q[t]/(t^i)\) with generator sign \(0\) or \(1\). A constructive proof is to choose homogeneous complementary vectors to \(\ker N\cap\operatorname{im}N\) inside \(\ker N\), lift them along homogeneous surjections of successive power images, and iterate at decreasing chain lengths; each constructed chain is homogeneous and the remaining graded space splits by induction. The multiplicities \(m_{i,\sigma}\) are intrinsic: for each \(i\), they are the graded dimensions of the quotient of the length-\(i\) layer \(\operatorname{im}N^{i-1}\cap\ker N\) by its length-\((i+1)\) successor, with the generator grading recovered by shifting parity \(i-1\). In particular, the two sign choices for a given length exhaust the possibilities and distinguish isomorphism classes.

For each choice \(\mathbf a\), the action of \(S\) on its homogeneous basis is uniquely determined by alternating signs down chains. Two such involutions are conjugate through an invertible map commuting with \(N\) exactly when their signed-chain multiplicities agree. This proves that the centralizer has precisely \(\prod_i(m_i+1)\) orbits.

**2. Full centralizer unit count.** Identify \(V\) as the ungraded \(\mathbb F_q[t]\)-module \(\bigoplus_i(\mathbb F_q[t]/(t^i))^{m_i}\). Between a cyclic module of length \(i\) and one of length \(j\), an equivariant homomorphism is given by choosing the image of the generator, a linear combination of \(t^r\) with \(\max(0,j-i)\le r<j\). Thus the full endomorphism algebra has dimension \(D=\sum_{i,j}m_i m_j\min(i,j)\). Its semisimple quotient is \(\prod_i M_{m_i}(\mathbb F_q)\): blocks between different lengths and positive-degree maps on equal-length blocks lie in its Jacobson radical, whose dimension is \(D-\rho\). An element is invertible precisely when its image in each matrix factor is invertible. Hence the unit group has order \(G\).

**3. Graded stabilizer count.** Fix a signed-chain decomposition. A degree-zero homomorphism from a cyclic generator of sign \(\sigma\) and length \(i\) to one of sign \(\tau\) and length \(j\) admits exactly \(h(i,j;\sigma,\tau)\) free scalar coefficients: the exponent of each allowed monomial must satisfy \(\tau+r\equiv\sigma\pmod2\). Therefore the graded endomorphism algebra has dimension \(E(\mathbf a)\). Its semisimple quotient is \(\prod_i(M_{a_i}(\mathbb F_q)\times M_{b_i}(\mathbb F_q))\); the radical has dimension \(E(\mathbf a)-\rho_{\mathbf a}\). Thus the degree-zero unit group, which is exactly the stabilizer of the involution inside the centralizer of \(N\), has order \(H(\mathbf a)\). Orbit-stabilizer now gives the claimed coefficient \(G/H(\mathbf a)\). These are sizes of actual finite groups, so integrality follows without numerical assumptions.

**4. Rank and boundary.** In a length-\(i\) chain generated in \(V_+\), exactly \(\lceil i/2\rceil\) vectors have plus sign, versus \(\lfloor i/2\rfloor\) for a minus-generated chain. Summing gives the displayed exponent. Each odd-length block contributes an independently selectable increment of zero or one above \(L\); all integers through \(U\) therefore occur. Interchanging plus and minus sends \(S\) to \(-S\), proving coefficient symmetry around \(n/2\). For rectangular partitions, evaluation of \(E\) gives the two Gaussian-binomial specializations: when \(s=2h\), \(E=h m^2\); when \(s=2h+1\), \(E=hm^2+a^2+(m-a)^2\). Substituting into the orbit quotient and using \(g_m/(g_a g_{m-a})=q^{a(m-a)}{m\brack a}_q\) yields the displayed formulas.

## Verification

The included `verify.py` independently constructs Jordan matrices, solves the linear matrix equation \(SN+NS=0\) over \(\mathbb F_3\) and \(\mathbb F_5\), enumerates all solutions of that linear equation in the tested dimensions, checks the nonlinear equation \(S^2=I\), measures the rank of \(S+I\), and compares every rank coefficient with the formula. The checker does not assume a signed-chain normal form in its direct enumeration. It also enumerates all \(2\times2\) matrices over \(\mathbb F_9\), with explicit arithmetic in \(\mathbb F_3[u]/(u^2-2)\). The accompanying executable passed eleven prime-field cases and two extension-field cases, reporting `ALL_EXACT_CHECKS_PASSED 13`. Further formula-only consistency checks covered all partition shapes through dimension ten at field order three. These finite tests are checks, not substitutes for the general proof.

## Relationship to prior work

Nilpotent Jordan chains, signed-chain or graded-module classifications, and orbit-stabilizer are standard structural ingredients and are not claimed as discoveries. Bogdanić, Đurić, Koljančić, Oblak and Šivic (arXiv:2212.08425v1, December 16, 2022) determine nilpotent Jordan forms possible in the centralizer of a prescribed two-equal-block nilpotent operator. Their main theorem asks a different commuting-nilpotent-orbit question and does not give finite-field counts of involutions \(S\) satisfying \(SN=-NS\), nor the plus-eigenspace polynomial for arbitrary \(\lambda\). Khatami's survey (arXiv:2304.08550) reviews commuting nilpotent Jordan forms, not these anti-involution fibers. Eick and Moede (arXiv:2205.03155) compute \(\mathbb Z_2\)-gradings of simple Lie algebras in characteristic two, an inequivalent setting. Fulman and Guralnick (2018, DOI:10.1007/s00026-018-0390-4) enumerate commuting pairs in finite Lie algebras, not an involution fixed against one nilpotent operator.

The contribution assessed here is the all-partitions exact finite-field fiber/orbit coefficient and complete plus-dimension spectrum, not the pre-existing existence of graded Jordan chains. A literature search cannot establish priority absolutely.

## Limitations

Characteristic two is excluded; then \(\pm1\) are equal and the eigenspace/graded-chain argument no longer applies. The theorem fixes the nilpotent \(N\); it does not sum over all nilpotent conjugacy classes or address nonnilpotent operators. A comprehensive historical classification of signed nilpotent orbits may already imply, or explicitly contain, a related stabilizer formula: this remains a residual originality risk.

## References

1. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425v1 (first public December 16, 2022), https://arxiv.org/abs/2212.08425.
2. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155v1 (May 6, 2022), https://arxiv.org/abs/2205.03155.
3. L. Khatami, *Commuting Jordan Types: a Survey*, arXiv:2304.08550v1 (April 17, 2023), https://arxiv.org/abs/2304.08550.
4. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, Annals of Combinatorics 22 (2018), 295–316, DOI:10.1007/s00026-018-0390-4.
