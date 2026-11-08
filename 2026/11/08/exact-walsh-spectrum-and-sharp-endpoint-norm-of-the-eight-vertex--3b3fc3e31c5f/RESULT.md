# Exact Walsh spectrum and sharp endpoint norm of the eight-vertex perfect-matching orbit

## Finding

Let \(K_8\) be the complete graph on eight labeled vertices and let \(E\) denote its 28-edge set. View the indicator vectors of the 105 perfect matchings as a frequency set \(\mathcal M\subset G=\mathbb F_2^E\). The Fourier projection \(P_{\mathcal M}\) retaining these characters has the **sharp endpoint norms**
\[
\|P_{\mathcal M}\|_{\ell^1(G)\to\ell^1(G)}
=\|P_{\mathcal M}\|_{\ell^\infty(G)\to\ell^\infty(G)}
=\frac{4213545}{524288}.
\]
In particular, the complete absolute Walsh spectrum of \(\mathbf1_{\mathcal M}\), equivalently the absolute signed-hafnian spectrum of all symmetric sign matrices of order eight with zero diagonal, has precisely the following 23 levels. The counts shown are for the 21 free non-star edge signs after normalizing the seven edges incident to one fixed vertex. To obtain multiplicities over the entire 28-dimensional group, multiply each count by \(128\).

| Absolute signed hafnian | Reduced multiplicity |
| ---: | ---: |
| 1 | 403200 |
| 3 | 259280 |
| 5 | 256032 |
| 7 | 289680 |
| 9 | 221340 |
| 11 | 175560 |
| 13 | 146160 |
| 15 | 122976 |
| 17 | 90720 |
| 19 | 33600 |
| 21 | 23800 |
| 23 | 25200 |
| 25 | 15750 |
| 27 | 16800 |
| 29 | 5040 |
| 33 | 6720 |
| 39 | 3430 |
| 41 | 210 |
| 43 | 840 |
| 45 | 336 |
| 57 | 420 |
| 75 | 56 |
| 105 | 2 |

The reduced counts sum to \(2^{21}\), their weighted absolute sum is \(16854180\), their weighted second moment is \(105\cdot2^{21}\), and their weighted fourth moment is \(40425\cdot2^{21}\). In particular the Walsh transform has no zeros, and the full signed spectrum has equal positive and negative multiplicities at each absolute level. The extremal magnitude \(105\) occurs at exactly 256 points of \(G\).

## Assumptions and scope

All graph vertices and edges are labeled. The edge group \(G=\mathbb F_2^E\) is equipped with counting measure for \(\ell^1\) and \(\ell^\infty\). Its characters are \(\chi_x(\omega)=(-1)^{\sum_{e\in E}x_e\omega_e}\). Define the unnormalized transform of the matching indicator by
\[
H(x)=\sum_{M\in\mathcal M}(-1)^{\sum_{e\in M}x_e}.
\]
For the symmetric sign matrix with off-diagonal entries \(B_{ij}=(-1)^{x_{ij}}\), this is the signed hafnian \(H(x)=\operatorname{haf}(B)\); the diagonal never enters the hafnian. The claim covers exactly eight vertices and all \(2^{28}\) sign assignments, with no implied infinite-order statement.

## Proof

**1. Hafnian and convolution identity.** A perfect matching partitions the eight vertices into four unordered pairs. By the hafnian definition, each matching contributes precisely its product of four off-diagonal signs, yielding the displayed formula for \(H\). The projection multiplier \(\mathbf1_{\mathcal M}\) has convolution kernel \(K(x)=2^{-28}H(x)\). The \(\ell^1\) and \(\ell^\infty\) operator norm of convolution by \(K\) equals \(\sum_x|K(x)|\): the triangle inequality gives the upper bound, a point mass realizes the \(\ell^1\) bound, and the sign of \(K(-x)\) realizes the \(\ell^\infty\) bound.

**2. Exact reduction by vertex switching.** For each vector \(t\in\mathbb F_2^8\), change the edge-sign exponent by \(x_{ij}\mapsto x_{ij}+t_i+t_j\). Every perfect matching uses each vertex exactly once, so every matching term is multiplied by the same sign \((-1)^{\sum_i t_i}\). Hence \(|H(x)|\) is unchanged. Choose the unique normalized star representative with \(x_{0j}=0\) for all seven other vertices; each assignment to the remaining 21 edges has exactly \(2^7=128\) full edge assignments mapping to it. A switching vector and its complement act identically on edges, and changing \(\sum_i t_i\) among the 128 representatives changes the signed hafnian by a minus sign. This proves the multiplicity conversion and the sign symmetry. (More explicitly, use switches with \(t_0=0\); their parities range evenly over both signs.)

**3. Exhaustive integer certificate for the reduced spectrum.** Order the 21 non-star edges lexicographically. Recursively pair the least unmatched vertex with each available later vertex. This generates exactly \(7\cdot5\cdot3\cdot1=105\) perfect matchings, each once. Erase the edge incident to vertex zero and represent the remaining three edges of each matching by a 21-bit mask \(m\). These masks are distinct. Form the integer array \(a\) of length \(2^{21}\), with \(a_m=1\) at these 105 masks and zero elsewhere. Apply all 21 butterfly stages \((u,v)\mapsto(u+v,u-v)\). The output at position \(x\) is, by induction on the number of stages,
\[
a_x'=\sum_{m\in\mathcal M_0}(-1)^{\langle x,m\rangle}=H(x),
\]
where \(\mathcal M_0\) is the normalized matching-mask set. The standalone `verify.py` executes this exact integer transform, asserts all 23 histogram counts in the table, and checks both moments. Its independent fourth-moment verification counts XOR differences among all ordered pairs of the 105 masks: if \(c_d=\#\{(m,m'):m\oplus m'=d\}\), orthogonality gives \(\sum_xH(x)^4=2^{21}\sum_dc_d^2=40425\cdot2^{21}\). All loops have fixed finite ranges and no floating-point operations.

**4. Independent direct evaluation.** The standalone C11 program `hafnian_direct.c` recursively generates the same perfect-matchings set but does **not** use any Fourier transform. Instead it evaluates, for each of the \(2^{21}\) normalized sign vectors, the parity of all 105 matching intersections and sums the corresponding 105 signs. It checks the entire tabulated histogram and both moment totals by 64-bit integer arithmetic. This is a distinct implementation of the defining hafnian sum. Its output agrees entry-for-entry with the butterfly certificate. Both complete algorithms are included here and constitute an exhaustive proof of the finite table.

**5. Norm and extremal multiplicity.** Summing the table gives \(\sum_x|H(x)|=128\cdot16854180\). Thus
\[
\sum_{x\in G}|K(x)|=\frac{128\cdot16854180}{2^{28}}=\frac{4213545}{524288}.
\]
Every matching sum contains 105 terms from \(\{+1,-1\}\), so its value is odd and never zero. The two normalized assignments at magnitude 105 yield \(2\cdot128=256\) full assignments.

## Verification

Run `python3 verify.py` with standard Python 3. The program outputs the full histogram, exact moments, rational norm, and `K8_MATCHING_WALSH_CERTIFICATE_PASS`. To reproduce the independent direct counting, compile using `cc -O3 -std=c11 hafnian_direct.c -o hafnian_direct` and execute `./hafnian_direct`; it checks the full table and prints `DIRECT_HAFNIAN_CENSUS_PASS`. No input datasets, randomness, packages, or noninteger numerical tolerances are used.

## Relationship to prior work

The classical hafnian/perfect-matching correspondence is used as a known starting point. Rudelson, Samorodnitsky, and Zeitouni study Gaussian estimators for hafnians of nonnegative graph matrices, and do not give this full independent-sign order-eight distribution or its Fourier endpoint norm. Existing signed-permanent statistics for bipartite matching matrices do not imply the symmetric nonbipartite eight-vertex distribution, whose terms range over a different perfect-matching orbit. Standard character orthogonality gives moment identities, but does not determine the 23-level histogram or the absolute first moment. This report makes no priority claim beyond a bounded literature comparison.

## Limitations

The theorem is an exact finite order-eight classification, not a formula valid for all even orders. The proof uses exhaustive finite integer computation supported by two independent implementations; these are exhaustive because the entire reduced \(2^{21}\)-case space is covered, unlike a random test. The signed-hafnian/perfect-matching identity is classical. Historical literature and tables may contain an earlier equivalent distribution that was not located, and independent mathematical review has not been carried out.

## References

Rudelson, M.; Samorodnitsky, A.; Zeitouni, O. *Hafnians, perfect matchings and Gaussian matrices*. arXiv:1409.3905v1 (first posted September 13, 2014). Journal version: *Annals of Probability* 44 (2016), 2858–2888. https://arxiv.org/abs/1409.3905

`verify.py` and `hafnian_direct.c`, accompanying exact finite certificates in this package.
