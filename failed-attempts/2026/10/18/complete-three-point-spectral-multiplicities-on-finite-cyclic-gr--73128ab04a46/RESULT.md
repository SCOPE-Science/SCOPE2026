# Complete three-point spectral multiplicities on finite cyclic groups

## Finding

Write \(G_N=\mathbb Z/N\mathbb Z\), where \(N\ge 3\), and \(F_N=(\exp(2\pi iuv/N))_{u,v\in G_N}\). For every three-element set \(A\subset G_N\), let \(\sigma_N(A)\) be the number of **distinct unordered** three-element sets \(B\subset G_N\) for which the restricted matrix \(F_N[A,B]\) is complex Hadamard, equivalently \(3^{-1/2}F_N[A,B]\) is unitary. The pair \((A,B)\) is a spectral pair. Distinct translations of spectra are counted separately.

**Theorem (complete spectrum-multiplicity histogram).** When \(3\nmid N\), every multiplicity is zero. Otherwise write
\[
N=3^a m,\qquad a\ge1,\qquad \gcd(m,3)=1,\qquad m=\prod_{p\ne3}p^{b_p}.
\]
For a prime power \(p^b\), set \(v_{p,b}(d)=\max\{j\in\{0,\ldots,b\}:p^j\mid d\}\), with \(v_{p,b}(0)=b\). For \(A=\{a_0,a_1,a_2\}\), put
\[
\mathcal D(A)=\{a_0-a_1,a_0-a_2,a_1-a_2\},\qquad
k_p(A)=\min_{d\in\mathcal D(A)}v_{p,b_p}(d).
\]
The set \(A\) has a spectrum if and only if the three values \(v_{3,a}(d)\), for \(d\in\mathcal D(A)\), are all the same integer \(r\in\{0,\ldots,a-1\}\). In that case its **exact number of spectra** is
\[
\boxed{\sigma_N(A)=3^{a+2r-1}\prod_{p^{b_p}\parallel m}p^{b_p+2k_p(A)}.}
\]

For each \(r\in\{0,\ldots,a-1\}\) and independently each \(k_p\in\{0,\ldots,b_p\}\), exactly
\[
\boxed{3^{3a-2r-3}\prod_{p^{b_p}\parallel m}D_{p,b_p}(k_p)}
\]
three-element sets \(A\) have those valuation parameters, where
\[
D_{p,b}(k)=\begin{cases}
p^{3b-2k}-p^{3b-2k-2},&0\le k<b,\\
p^b,&k=b.
\end{cases}
\]
Consequently the complete multiplicity histogram is obtained by summing the displayed stratum counts whenever distinct parameter tuples produce the same value of \(\sigma_N(A)\), and adding \(\binom N3\) minus the total stratum counts at multiplicity zero.

**Corollary (all spectral pairs).** The total number \(T_N\) of ordered pairs \((A,B)\) of three-element subsets forming a spectral pair is
\[
\boxed{T_N=\begin{cases}
0,&3\nmid N,\\[2pt]
\displaystyle\frac{aN^4}{81}\prod_{p^b\parallel m}\left(1+b(1-p^{-2})\right),&N=3^am,\ \gcd(3,m)=1.
\end{cases}}
\]
Here **ordered** means that \((A,B)\) and \((B,A)\) are individually counted (even when they coincide); the elements inside each set are unordered. Equivalently, for \(3\mid N\) the integer formula is \(T_N=a3^{4a-4}\prod_{p^b\parallel m}p^{4b-2}\bigl[p^2+b(p^2-1)\bigr]\). Empty products equal one. Examples are \(T_6=28\), \(T_9=162\), \(T_{12}=640\), \(T_{18}=4536\) and \(T_{24}=13312\).

## Assumptions and scope

The group is cyclic of arbitrary integer order \(N\ge3\), not necessarily a prime power or squarefree. The Fourier matrix is unnormalized; complex Hadamard means orthogonal rows with squared norm three. The valuation parameters depend only on residues modulo the indicated prime powers. Every choice of three distinct row indices is counted once, regardless of translation or permutation; the same convention applies to spectra. This is an exact finite-group, three-frequency result, not a claim about larger spectral sets or continuous spectral measures.

## Proof

**Step 1: three-root rigidity.** Three complex numbers of modulus one have sum zero precisely when, up to common phase and permutation, they are \(1,\omega,\omega^2\), with \(\omega=\exp(2\pi i/3)\). Indeed, after dividing by one of the three numbers, \(1+u+v=0\) and \(|u|=|v|=1\) yield \(\operatorname{Re}(u)=-1/2\); hence \(\{u,v\}=\{\omega,\omega^2\}\). Dephasing any three-by-three Hadamard matrix therefore leaves exactly two possibilities, the Fourier matrix of order three and its conjugate, with its first row and column all ones. This standard classification is also used by Herr and Wiegand [1, Theorem 3.6].

**Step 2: local congruences.** Order the row and column triples provisionally as \((a_0,a_1,a_2)\) and \((b_0,b_1,b_2)\). Write \(d_i=a_i-a_0\) and \(e_j=b_j-b_0\), for \(i,j\in\{1,2\}\). Dephasing the submatrix leaves entries \(\exp(2\pi i d_i e_j/N)\). By Step 1, the four products, in row-major order, must be congruent modulo \(N\) to either
\[
(N/3,\,2N/3,\,2N/3,\,N/3)
\quad\text{or}\quad
(2N/3,\,N/3,\,N/3,\,2N/3).
\]
Thus \(3\mid N\) is necessary. For \(N=3^am\), the Chinese remainder theorem says that all four products vanish modulo each \(p^b\parallel m\), and modulo \(3^a\) all four have valuation exactly \(a-1\), with their unit residues modulo three occurring in opposite pairs.

At the ternary component, the first row difference \(d_1\) and the second difference \(d_2\) must have the same valuation \(r<a\), with \(d_2/3^r\equiv-d_1/3^r\pmod3\); otherwise the two nonzero entries in any column could not have opposite primitive-cube-root phases. Equivalently all three pairwise row differences have valuation \(r\). The column differences must both have valuation \(s=a-1-r\) and satisfy \(e_2/3^s\equiv-e_1/3^s\pmod3\). Conversely these ternary constraints, together with vanishing at every other prime-power component, give exactly one of the two dephased Hadamard patterns: the first cross-product is a primitive cube-root exponent, the adjacent ones are its negatives, and the bottom-right one agrees with it. Hence the conditions are both necessary and sufficient.

**Step 3: exact spectra for a fixed row triple.** Take an eligible \(A\) with ternary valuation \(r\). At \(3^a\), choose \(b_0\) in \(3^a\) ways, then choose \(e_1\) of exact valuation \(s=a-1-r\) in \(2\cdot3^r\) ways, and choose \(e_2\) with the required opposite residue modulo \(3^{s+1}\) in \(3^r\) ways. This gives \(2\cdot3^{a+2r}\) ordered ternary column triples. At each \(p^b\parallel m\), the four cross products vanish exactly when both \(e_1,e_2\) are divisible by \(p^{b-k_p(A)}\): there are \(p^b\) choices of \(b_0\) and \(p^{k_p(A)}\) choices for each difference, or \(p^{b+2k_p(A)}\) ordered local triples. The CRT combines these independent choices. Because the ternary component already makes the three global columns distinct, every unordered spectrum corresponds to exactly six ordered triples, yielding the stated \(\sigma_N(A)\).

**Step 4: count the row-valuation strata.** For the ternary component with parameter \(r\), choose \(a_0\) in \(3^a\) ways, \(a_1-a_0\) of exact valuation \(r\) in \(2\cdot3^{a-r-1}\) ways, and \(a_2-a_0\) with opposite residue modulo \(3^{r+1}\) in \(3^{a-r-1}\) ways. Dividing the resulting number of ordered triples by six gives \(3^{3a-2r-3}\). At a different prime power \(p^b\), the number of ordered triples all congruent modulo \(p^k\) is \(p^{3b-2k}\), because the common residue has \(p^k\) choices and the three lifts have \(p^{b-k}\) choices each. Subtraction for \(k<b\), or the all-equal case for \(k=b\), gives \(D_{p,b}(k)\). The CRT and the single division by six produce the histogram. Distinctness is guaranteed by the ternary component even if all other components coincide.

**Step 5: sum the incidence counts.** Each ternary stratum contributes
\[
3^{3a-2r-3}\cdot3^{a+2r-1}=3^{4a-4}
\]
independently of \(r\). At each other prime power,
\[
\sum_{k=0}^b D_{p,b}(k)p^{b+2k}
=p^{4b}\left(1+b(1-p^{-2})\right).
\]
Summing over the \(a\) possible ternary depths and multiplying independent local factors gives \(T_N=a3^{4a-4}\prod_{p^b\parallel m}p^{4b}(1+b(1-p^{-2}))\), equivalent to both displayed formulas. All divisions and empty-product boundary cases are accounted for.

## Verification

The included `verify.py` independently enumerates **every** unordered three-row set and three-column set at each order \(N\in\{3,4,6,8,9,10,12,15,18,21,24\}\). It tests the four dephased products against the two exact cube-root congruence patterns rather than applying the valuation formula. It then compares each individual multiplicity, its full histogram, and the total with the theorem. The included `verification_output.txt` records successful exact-integer checks, including the non-prime-power composite orders \(6,12,15,18,21,24\). Run with Python 3 using `python verify.py` in a directory containing that file. These finite experiments are supplementary; the general theorem follows from Steps 1–5, not extrapolation.

## Relationship to prior work

Herr and Wiegand [1, Theorem 3.6] already give a **necessary-and-sufficient compatibility criterion** for individual three-by-three Fourier Hadamard submatrices for every cyclic order, building on the standard uniqueness of order-three complex Hadamard matrices. Thus neither existence of compatible pairs nor the individual-pair test is claimed new. Their paper studies primitive-set compatibility graphs and examples, but does not state the formula for the number of spectra of **each** fixed three-element row set, the complete histogram of these multiplicities, or the multiplicative all-modulus incidence total derived here. The theorem is an enumeration refinement, not a different characterization theorem. Malikiosis [2] develops the finite-cyclic spectral-set framework and its relation to tiling, while An and Lai [3] study product-form Hadamard triples and spectral measures; neither examined primary text supplies this multiplicity census.

## Limitations

The counting formulas classify three-element spectral sets and their spectra **within the specified finite cyclic group**, not equivalence classes modulo automorphisms or translations, higher-cardinality spectral sets, or all Fourier submatrix ranks. The criterion for a given pair has strong published precedent [1], so the new contribution is specifically the enumerative refinement. Search coverage cannot exclude an unindexed earlier census, and no independent audit has been performed. The finite verification covers only the listed orders; no exhaustive computation across all orders is claimed.

## References

[1] John E. Herr and Troy M. Wiegand, *Identifying Complex Hadamard Submatrices of the Fourier Matrices via Primitive Sets*, arXiv:1909.13145 (first public 2019-09-28), especially Theorem 3.6 and Section 4. https://arxiv.org/pdf/1909.13145

[2] Romanos Diogenes Malikiosis, *On the Structure of Spectral and Tiling Subsets of Cyclic Groups*, arXiv:2005.05800 (first public 2020-05-12), especially Definition 3.1 and Theorem 3.3. https://arxiv.org/pdf/2005.05800

[3] Lixiang An and Chun-Kit Lai, *Product-form Hadamard triples and its spectral self-similar measures*, arXiv:2209.05616 (2022), especially the definition of a Hadamard triple. https://arxiv.org/pdf/2209.05616
