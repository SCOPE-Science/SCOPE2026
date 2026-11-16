# Eight-column-type Walsh compression and the complete spectrum of balanced \(4\times6\) tables

## Finding
Let \(\mathcal B_n\) be the binary \(4\times 2n\) matrices whose four row sums equal \(n\) and whose \(2n\) column sums equal \(2\), with \(n\ge1\). Write \(W_n(B)=\sum_{X\in\mathcal B_n}(-1)^{\langle B,X\rangle}\) for their **unnormalized** Walsh transform on \(\mathbb F_2^{8n}\), where the pairing is the entrywise binary dot product. There is an exact eight-column-type coefficient formula for every \(W_n(B)\), and the complete signed Walsh spectrum (values and multiplicities) can be computed with \(O(n^{11})\) exact integer arithmetic operations, with integer bit lengths \(O(n)\).

For \(n=3\), the \(4\times6\) case, \(|\mathcal B_3|=1860\). The multiplier \(0\) has multiplicity \(8,388,608\), and all 28 nonzero signed levels occur in \(\pm\)-pairs with the following multiplicity **for each sign**:

| Multiplier magnitude | Multiplicity of \(+a\) | Multiplicity of \(-a\) |
| ---: | ---: | ---: |
| 4 | 2,073,600 | 2,073,600 |
| 12 | 829,440 | 829,440 |
| 20 | 69,120 | 69,120 |
| 44 | 92,160 | 92,160 |
| 60 | 307,200 | 307,200 |
| 68 | 391,680 | 391,680 |
| 116 | 138,240 | 138,240 |
| 124 | 230,400 | 230,400 |
| 148 | 23,040 | 23,040 |
| 236 | 7,680 | 7,680 |
| 324 | 11,520 | 11,520 |
| 372 | 15,360 | 15,360 |
| 620 | 4,608 | 4,608 |
| 1860 | 256 | 256 |

Thus the unnormalized convolution \(T_3 f=\mathbf1_{\mathcal B_3}*f\) has exact rank \(2^{23}=8,388,608\), smallest nonzero singular value \(4\), largest singular value \(1860\), recoverable-spectrum condition number \(465\), and \(\|T_3^\dagger\|_{\ell^2\to\ell^2}=1/4\). Its image consists exactly of functions invariant under translation by the all-one matrix, and its kernel consists exactly of the anti-invariant functions. The norm-one projection onto the image is the average of identity and this translation.

## Assumptions and scope
All row and column indices are labelled; a binary matrix and its complement are counted as different objects. The Fourier group is the full \(24\)-dimensional Boolean matrix group in the concrete case, not a quotient. The convolution, Fourier transform, and singular values use counting measure and **unnormalized** convolution. This is not a formula for Eulerian circuit counts: the matrices encode Eulerian **orientations** of \(K_{4,2n}\). The result states a general exact computation method, plus one complete first non-square spectrum; it does **not** assert analogous half-rank or spectral-gap formulas for every \(n\).

## Proof
**Eight-type reduction.** Every column of \(X\in\mathcal B_n\) contains exactly two ones. If a frequency \(B\) has column \(j\) equal to \((b_{1j},b_{2j},b_{3j},b_{4j})\), adding \(1\) to all four of those frequency entries changes its character by \((-1)^2=1\). Hence only the three relative bits \(v_j=(b_{1j}+b_{4j},b_{2j}+b_{4j},b_{3j}+b_{4j})\in\mathbb F_2^3\) matter. Column permutations preserve the matrix family and its Fourier coefficients. Put \(c_v=|\{j:v_j=v\}|\), so \(\sum_vc_v=2n\).

For \(v\in\mathbb F_2^3\), extend it by \(v_4=0\) and define the signed quadratic polynomial
\[
P_v(z_1,z_2,z_3,z_4)=\sum_{1\le a<b\le4}(-1)^{v_a+v_b}z_az_b.
\]
Selecting a term \(z_az_b\) from a column chooses the two entries that are one in that column, with exactly the character sign \((-1)^{v_a+v_b}\). Imposing row sums gives the identity
\[
W_n(B)=[z_1^n z_2^n z_3^n z_4^n]\prod_{v\in\mathbb F_2^3}P_v(z)^{c_v}.
\]
Conversely, each histogram \(c=(c_v)\) corresponds to exactly
\[
M_n(c)=2^{2n}\frac{(2n)!}{\prod_vc_v!}
\]
distinct frequency matrices: \((2n)!/\prod_vc_v!\) relative-bit sequences and two gauges for each column. These classes partition all \(2^{8n}\) frequencies. Their number is \(\binom{2n+7}{7}\).

**Effective exact coefficient recurrence.** Process the \(2n\) column types in any fixed order, maintaining a signed integer count \(D_t(r_1,r_2,r_3)\) for the first \(t\) columns. At step \(t\), the fourth partial row count is necessarily \(r_4=2t-r_1-r_2-r_3\). For each of six choices \(\{a,b\}\subseteq\{1,2,3,4\}\), increment the two corresponding counts and multiply by \((-1)^{v_a+v_b}\), discarding states with any row count greater than \(n\). Begin with \(D_0(0,0,0)=1\); the target \(D_{2n}(n,n,n)\) is the coefficient above, because its fourth row count is automatically \(n\). This is an induction on the number of processed columns, not a heuristic. There are at most \((n+1)^3\) states, six transitions per state, and \(2n\) stages, requiring \(O(n^4)\) arithmetic operations per histogram. Enumerating all \(\binom{2n+7}{7}=O(n^7)\) histograms gives \(O(n^{11})\) integer arithmetic operations for the complete signed spectrum. Every intermediate coefficient is bounded in magnitude by \(6^{2n}\), so integers have \(O(n)\) bits.

**Complete \(4\times6\) calculation.** For \(n=3\), weakly composing six labelled column positions into eight types yields precisely \(\binom{13}{7}=1716\) classes. The included `data/eulerian_k46_orbits.csv` records, in their exact deterministic composition order, each tuple \(c\), the integer coefficient from the above recurrence, and its multiplicity \(64\cdot6!/\prod_vc_v!\). Summing the class multiplicities by coefficient gives the signed histogram stated in the finding. This is an **exhaustive finite certificate**: every frequency occurs in one and only one recorded class, and every integer coefficient is reconstructed by an explicit recurrence. The independent row-mask enumeration in `verify_eulerian_k46.py` finds exactly \(1860\) matrices; the script additionally checks 256 frequency values by direct character sums, and verifies the integer Parseval identity \(\sum_BW_3(B)^2=2^{24}\cdot1860\).

The certificate shows that the zeros are precisely half the frequencies. Separately, complementing every entry of a balanced matrix preserves its margins and changes the character sign by \((-1)^{|B|}\), so all odd-weight frequencies vanish. Since these already number \(2^{23}\), no other frequencies vanish. The signed spectrum is symmetric: toggling an entire row of the *frequency* multiplies every character by \((-1)^3=-1\). This also independently explains equal positive and negative multiplicities.

The Walsh diagonalization of convolution identifies multiplier values as its real eigenvalues and their absolute values as singular values. The minimum nonzero absolute value is \(4\) and the maximum is \(1860\), giving the stated inverse norm and condition number. The nonzero frequency set is exactly the even-weight hyperplane. Its Fourier projector is convolution by \((\delta_0+\delta_{\mathbf1})/2\), proving the image/kernel description and norm-one projection formula.

## Verification
Run `python3 verify_eulerian_k46.py` from this package. This requires only the Python standard library and the adjacent `data/eulerian_k46_orbits.csv`; both are included. Expected final line:

`EULERIAN_K46_WALSH_ORBIT_PASS orbits=1716 frequencies=16777216 direct=256`

The 1716 checks reconstruct **every** frequency coefficient through the rigorous orbit partition, not through sampling. The independent 256-frequency direct check is supplementary. All operations used for the complete census are exact integers. No floating point or asymptotic approximation is used.

## Relationship to prior work
Nester (1994) counts Eulerian orientations of complete bipartite graphs and already records \(1860\) orientations for \(K_{4,6}\), and supplies the unsigned three-partition count for general \(K_{4,2n}\); this cardinality and the classical labelled-orientation model are **not** claimed as new. Barvinok (2008) develops cardinality and maximum-entropy estimates for binary matrices with prescribed margins, not the complete signed Walsh histogram. Beluhov (2025) proves the two-adic valuation of unsigned balanced-grid counts in families including four rows, not the 29-level signed spectrum. Standard Walsh diagonalization, complement symmetry, column permutations, and orbit counting are also prior techniques. The specific eight-type all-frequency compression for this operator and the complete 4-by-6 signed spectral census are the assessed contributions.

## Limitations
The exact 29-level list is specific to four rows and six columns. The general algorithm does not provide a closed formula for each spectral multiplicity at arbitrary width, nor prove that every even-weight multiplier remains nonzero at larger widths. All finite coefficients are exactly verified by an exhaustive, reproducible integer certificate, but no independent mathematical audit has been performed. Historical-priority checking is bounded and might miss an equivalent signed contingency-table formula in another literature.

## References
1. M. R. Nester, “Eulerian orientations and circuits of complete bipartite graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 16 (1994), 3–17. https://combinatorialpress.com/article/jcmcc/Volume%2016/vol-16-paper%201.pdf (publisher record dated 1994-10-31).
2. A. Barvinok, “On the number of matrices and a random matrix with prescribed row and column sums and 0-1 entries,” arXiv:0806.1480, first public 2008-06-09; *Advances in Mathematics* 224 (2010), 316–339. https://arxiv.org/abs/0806.1480.
3. N. Beluhov, “Powers of 2 in Balanced Grid Colourings,” *Enumerative Combinatorics and Applications* 6:1 (2026), article S2R3, publicly published 2025-10-03. https://doi.org/10.54550/ECA2026V6S1R3. Only the **unsigned** valuation results are invoked as context, not as part of the new claim.
