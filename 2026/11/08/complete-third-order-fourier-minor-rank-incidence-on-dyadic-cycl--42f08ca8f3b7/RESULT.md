# Complete third-order Fourier-minor rank incidence on dyadic cycles

## Finding
For each integer \(k\ge3\), put \(N=2^k\) and form the unnormalized Fourier character matrix \(F_N=(\exp(2\pi i rc/N))_{r,c\in\mathbb Z/N\mathbb Z}\). Choose independently an unordered three-element row set \(R\) and an unordered three-element column set \(C\). The complete rank distribution of \(F_N[R,C]\), among the \(\binom N3^2\) ordered pairs \((R,C)\), is as follows:
\[
\begin{aligned}
T_1(k)&=\frac{N^2}{9}+\frac{kN^3}{8}+\left(\frac{k}{48}-\frac19\right)N^4,\\
T_2(k)&=\frac{N^5}{12}+\left(\frac14-\frac{5k}{32}-\frac{k^2}{32}\right)N^4-\left(\frac13+\frac{k}{8}\right)N^3,\\
T_3(k)&=\binom N3^2-T_1(k)-T_2(k).
\end{aligned}
\]
Here \(T_j(k)\) counts matrices of complex rank exactly \(j\). All three expressions are nonnegative integers. In particular, rank-one minors first occur at \(N=16\), with exactly \(256\) such pairs, while none occurs at \(N=8\).

There is also a complete geometric classification of the singular pairs. For an unordered three-set \(R\subset\mathbb Z/N\mathbb Z\), the three differences have exactly two equal \(2\)-adic valuations \(a\) and one strictly larger valuation \(b\), so record its **signature** \((a,b)\), with \(0\le a<b\le k-1\). Let \((c,d)\) be the signature of \(C\). Then
\[
\operatorname{rank}F_N[R,C]=
\begin{cases}
1,&a+c\ge k,\\
2,&a+c<k\text{ and }(b+c\ge k\text{ or }a+d\ge k),\\
3,&b+c<k\text{ and }a+d<k.
\end{cases}
\]
A uniformly random pair of three-row and three-column sets therefore has singularity probability
\[
\frac{T_1(k)+T_2(k)}{\binom N3^2}=\frac3N+O\!\left(\frac{k^2}{N^2}\right),
\]
and rank-one probability \(O(k/N^2)\), as \(k\to\infty\).

## Assumptions and scope
The rows and columns are indexed by **distinct** elements of the cyclic group \(\mathbb Z/N\mathbb Z\); the pair \((R,C)\) is ordered, while each individual three-set is unordered. All ranks are over \(\mathbb C\). The Fourier matrix is unnormalized; nonzero scalar normalization does not change rank. The valuation of a nonzero class modulo \(N\) is the largest integer \(v<k\) for which that class is divisible by \(2^v\). The asymptotic probability selects row and column three-sets uniformly and independently. No statement about matrices of size greater than three is intended.

## Proof
**Step 1: third-order character-table rigidity.** The following lemma applies to any finite abelian group with unit-modulus characters. A three-row/three-column character submatrix is singular if and only if two of its restricted rows are proportional or two of its restricted columns are proportional. Indeed, translate the first row and first column labels to zero and multiply by invertible diagonal phases. The submatrix then has the form
\[
\begin{pmatrix}1&1&1\\1&A&B\\1&C&D\end{pmatrix},\qquad |A|=|B|=|C|=|D|=1.
\]
Its determinant vanishes precisely when \((A-1)(D-1)=(B-1)(C-1)\). If this common product is nonzero, use \((z-1)/(\overline z-1)=-z\) for \(|z|=1\) to deduce \(AD=BC\). Substitution gives \((A-B)(A-C)=0\). In the first case, \(A=B\) and \(AD=BC\) imply \(C=D\), hence two columns coincide; in the second, \(A=C\) implies \(B=D\), hence two rows coincide. If the common product is zero, one of \(A,D\) and one of \(B,C\) must equal one. Checking the four possibilities again gives a constant restricted row or column. The converse is immediate. Distinct original rows and columns are allowed; proportionality refers only to their restrictions.

**Step 2: dyadic valuations and rank.** For any distinct three points of \(\mathbb Z/2^k\mathbb Z\), the differences have valuations \(a,a,b\) with \(a<b\). After removing the common factor \(2^a\), exactly one pair has equal parity; this is the unique close pair. For row signature \((a,b)\) and column signature \((c,d)\), two rows are proportional on the three columns if and only if some row difference annihilates every column difference. Since the largest row-difference valuation is \(b\), this holds exactly when \(b+c\ge k\). By symmetry two columns are proportional exactly when \(a+d\ge k\). The entire matrix has rank one if and only if all pairwise row differences annihilate all pairwise column differences, namely \(a+c\ge k\). Combined with Step 1, these facts establish the rank classification.

**Step 3: count three-set signatures.** The number of unordered three-sets with signature \((a,b)\) is
\[
M_{a,b}=\frac{N\,2^{k-b-1}}2\,2^{k-a-1}=2^{3k-a-b-3}.
\]
The first factor chooses the unique close unordered pair of valuation \(b\); the second chooses the third point with valuation \(a\) from either member. Every triple is counted once. Thus all rank counts are exact sums of \(M_{a,b}M_{c,d}\) over the conditions from Step 2.

For completeness, the elementary geometric-series evaluation is displayed. Put
\[
L_a=\sum_{b=a+1}^{k-1}M_{a,b}=2^{3k-2a-3}-2^{2k-a-2}
\]
for \(0\le a\le k-2\), and \(L_{k-1}=0\). The rank-one count is
\[
T_1=\sum_{a+c\ge k}L_aL_c
=\frac{N^2}{9}+\frac{kN^3}{8}+\left(\frac{k}{48}-\frac19\right)N^4.
\]
Here and in the next sums, indices range over \(0\le a<b\le k-1\), \(0\le c<d\le k-1\), unless narrowed explicitly.

Let \(X\) be the number of pairs satisfying \(b+c\ge k\), and let \(I\) count the intersection \(b+c\ge k\) and \(a+d\ge k\). By row-column symmetry the number \(S\) of singular minors is \(S=2X-I\). Summing \(M_{a,b}M_{c,d}\) with the stated inequalities gives
\[
\begin{aligned}
X&=\frac{N^5}{24}+\left(\frac{19}{72}-\frac{k}{6}\right)N^4-\frac{5N^3}{12}+\frac{N^2}{9},\\
I&=\left(\frac{k^2}{32}-\frac{19k}{96}+\frac7{18}\right)N^4-\frac{N^3}{2}+\frac{N^2}{9}.
\end{aligned}
\]
One direct way to check the second evaluation is to set \(u=k-b\), \(v=k-a\), so \(1\le u<v\le k-1\). After summing over \((c,d)\), the contribution from each \((u,v)\) equals
\[
\frac{N^4}{16}-\frac{N^4}{24}2^{u-v}-\frac{N^3}{16}2^v+\frac{N^2}{24}2^{u+v}.
\]
The requisite four sums are \(\binom{k-1}{2}\), \(k-3+4/N\), \((k-3)N+4\), and \((N^2-6N+8)/3\), respectively. The first evaluation follows by setting \(b\) as the close-pair valuation and using \(\sum_{a=0}^{b-1}M_{a,b}=2^{3k-b-2}(1-2^{-b})\); after summation the summand is proportional to \(2^b-4+5\cdot 2^{-b}-2\cdot 4^{-b}\). Finally \(T_2=S-T_1\), \(T_3=\binom N3^2-S\), as claimed.

**Step 4: asymptotics.** The exact formulas imply \(S=N^5/12+O(k^2N^4)\), \(T_1=O(kN^4)\), and \(\binom N3^2=N^6/36+O(N^5)\). Dividing proves both probability statements. The count for rank one vanishes when \(k=3\) and is positive when \(k\ge4\) by the signature criterion: choose \(a=c=k-2\), \(b=d=k-1\).

## Verification
The accompanying `verify.py` checks the formula and signature counts with exact integer arithmetic for \(2\le k\le13\). For \(k=3,4\), it additionally enumerates **every** three-by-three Fourier minor (\(3,136\) and \(313,600\) cases respectively), computes its determinant exactly in \(\mathbb Z[z]/(z^{N/2}+1)\) (the relevant cyclotomic ring), and compares zero/nonzero status with the valuation-rank criterion. Rank-one cases are separately checked by direct modular pairings. The output is `DYADIC_THIRD_ORDER_FOURIER_MINOR_CHECKS_OK`.

The finite checks corroborate rather than prove the universal theorem. Its proof is Steps 1–4 and does not depend on a numerical extrapolation or computational oracle.

## Relationship to prior work
Tao proves sharp Fourier uncertainty for cyclic prime order, whereas the present objects are composite dyadic character tables. Alexeev--Cahill--Mixon characterize whether an entire prime-power Fourier row frame is full spark; their Theorem 9 is a yes/no statement for each row set, not an exact census of the ranks of every row/column three-set pair. Delvaux--Van Barel analyze maximal rank-deficient submatrices and Fourier block tilings; their structural methods are relevant, but the accessible 2006 follow-up does not supply these third-order multiplicity formulas. The 2008 single-prime-power paper is a particularly relevant uninspected full text and remains a priority risk; its accessible abstract does not resolve whether the census is implicit.

Existing published exact classifications of third-order Fourier minors treat odd prime-square cycles, elementary prime affine planes, or even semiprime cycles; none of those groups is isomorphic to a cyclic group of order \(2^k\) for \(k\ge3\). The present result provides an all-exponent dyadic valuation signature, three rank multiplicities, and a quantitative asymptotic law. A general character-table rigidity lemma is included only as a tool for this exact all-dyadic rank census, not claimed as a separate discovery.

## Limitations
The result covers only third-order minors on cyclic powers of two, not arbitrary composite moduli, larger minors, exact singular values, or conditioning of nonsingular minors. Character-table rigidity is elementary and may have appeared in earlier forms. Although the compared statements do not directly give the rank census, older hierarchical Fourier-matrix literature might imply it via further counting; independent priority review is not available. The 2008 Delvaux--Van Barel paper was accessible in abstract only after open-access searches, and institutional full-text retrieval was unavailable. Thus originality is a bounded assessment, not a claim of universal priority.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286, v1 2003-08-29.
2. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, v1 2011-10-17, Theorem 9.
3. S. Delvaux, M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, Linear Algebra Appl. 429 (2008), 1587–1605, DOI 10.1016/j.laa.2008.04.043; preceding report TW470 (2006).
4. S. Delvaux, M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, report TW477 (2006-11-15), published in Linear Algebra Appl. 426 (2007), 349–367; DOI 10.1016/j.laa.2007.05.009.
5. *All singular three-by-three minors of prime-square Fourier matrices*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-singular-three-by-three-minors-of-prime-square-fourier-matri--feb52ea6712b.
6. *Singular three-by-three Fourier minors on even semiprime cycles*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-singular-three-by-three-fourier-minors-on-even-semiprime-cycles--8f025c6183d3.
7. *Exact three-point Fourier uncertainty on every cyclic group*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-point-fourier-uncertainty-on-every-cyclic-group--cf7d7124f263.
