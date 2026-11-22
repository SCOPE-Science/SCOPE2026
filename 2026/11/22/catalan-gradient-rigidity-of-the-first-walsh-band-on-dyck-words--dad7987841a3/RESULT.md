# Catalan-gradient rigidity of the first Walsh band on Dyck words

## Finding
Let \(D_n\) be the binary length-\(2n\) Dyck language, where 1 is an up-step and 0 a down-step. The **entire first Walsh band** of its unnormalized indicator has an explicit Catalan-convolution gradient. Define, for \(j\ge0\),
\[
C_j=\frac{1}{j+1}\binom{2j}{j},\qquad A_0=0,\qquad A_j=\sum_{k=1}^{j}C_{k-1}C_{n-k}\quad(1\le j\le n).
\]
Then, at each \(1\le j\le n\),
\[
W_n(\{2j-1\})=2A_{j-1}-C_n,\qquad W_n(\{2j\})=2A_j-C_n.
\]
Consequently the coefficient profile moves strictly upward from odd to the following even position, remains constant from an even position to the next odd position, and reverses sign uniquely across the center. If \(n\) is even, the **only vanishing singleton frequencies** are \(\{n\}\) and \(\{n+1\}\); if \(n\) is odd, none vanish. The smallest strictly positive absolute singleton multiplier is
\[
\min_{1\le i\le 2n:\,W_n(\{i\})\ne0}|W_n(\{i\})|=
\begin{cases}
C_m^2,&n=2m+1,\ m\ge0,\\
2C_{m-1}C_m,&n=2m,\ m\ge1.
\end{cases}
\]
This is a first-band statement; it is not a classification of higher-order Fourier zeros or of the full convolution nullity.

## Assumptions and scope
Fix any integer \(n\ge1\). The ambient group is \(G_n=(\mathbb Z/2\mathbb Z)^{2n}\), with coordinates ordered from left to right. A word \(x=(x_1,\ldots,x_{2n})\) is Dyck if \(\sum_i x_i=n\) and \(\sum_{i=1}^{t}(2x_i-1)\ge0\) for every \(1\le t\le2n\). The indicator is \(f_n=\mathbf1_{D_n}\). The transform is unnormalized: \(W_n(S)=\sum_{x\in G_n}f_n(x)(-1)^{\sum_{i\in S}x_i}\). In particular, \(W_n(\varnothing)=C_n\). A singleton is a set containing one coordinate, not an arbitrary Fourier subset.

## Proof
Write \(U_i\) for the number of words in \(D_n\) with step \(i\) up. Then \(W_n(\{i\})=C_n-2U_i\).

For \(1\le j<n\), interchange the adjacent steps at positions \(2j\) and \(2j+1\). The height just before position \(2j\) is odd and nonnegative, therefore at least 1; both \(10\mapsto01\) and \(01\mapsto10\) preserve the Dyck condition. This involution exchanges the occurrence of an up-step at those two positions; therefore \(U_{2j}=U_{2j+1}\).

For \(1\le j\le n\), the analogous swap of steps \(2j-1\) and \(2j\) fails in exactly one direction: a local \(10\mapsto01\) at height zero before position \(2j-1\) would go below zero. All other opposite adjacent pairs cancel by the involution. The unpaired \(10\) at height zero separates uniquely into a Dyck prefix of semilength \(j-1\), that local \(10\), and a Dyck suffix of semilength \(n-j\). Hence
\[
U_{2j-1}-U_{2j}=C_{j-1}C_{n-j}>0.
\]
Since \(U_1=C_n\), telescoping with the even/next-odd equalities gives \(U_{2j-1}=C_n-A_{j-1}\) and \(U_{2j}=C_n-A_j\). This proves the multiplier formulas and all strict/equal transitions.

The Catalan recurrence gives \(A_n=C_n\). Moreover the summands \(C_{k-1}C_{n-k}\) are symmetric under \(k\mapsto n+1-k\), and all are positive. If \(n=2m\), then \(A_m=C_n/2\); the only coordinates whose cumulative value equals that half are \(2m\) and \(2m+1\). Their adjacent nonzero coefficients are \(\pm2C_{m-1}C_m\). If \(n=2m+1\), the unique central summand is \(C_m^2\), so \(A_m=(C_n-C_m^2)/2\) and \(A_{m+1}=(C_n+C_m^2)/2\). The central coefficients are \(\mp C_m^2\), and strict monotonicity makes these the least nonzero magnitudes. These identities also cover \(n=1\).

## Verification
A standalone Python 3 checker enumerates Dyck words independently by a prefix-height recursion, counts up-steps at every coordinate, evaluates the direct singleton character sums, and checks all formulas, zero locations and sharp gap for semilengths 1 through 10 (110 singleton multipliers). Run `python3 verify_dyck_firstband.py` with only the standard library. Its output is a finite corroboration, not the all-integer proof.

## Relationship to prior work
The Catalan recurrence and the Chung–Feller tradition supply the enumeration background. The 2016 minimum-change Chung–Feller bijections of Mütze, Standke and Wiechert concern a different statistic: changing the number of flaws among balanced paths, rather than the position-indexed Fourier coefficients of zero-flaw Dyck words. Existing research on first-ascent/last-descent kernels and Catalan-language subsequence statistics likewise treats different data. The direct all-coordinate Walsh gradient and parity-dependent singleton zero set are the new scope asserted here; historical priority remains subject to unknown equivalent positional-step identities.

## Limitations
No assertion is made about Fourier coefficients of support size two or greater, full convolution rank, or exact higher-band conditioning. The proof is elementary and may admit equivalents in the older literature on Dyck-path positional marginals; an unindexed equivalent would defeat originality. The source literature does not independently audit this result.

## References
- T. Mütze, C. Standke and V. Wiechert, *A minimum-change version of the Chung–Feller theorem for Dyck paths*, arXiv:1603.02525 (first posted 2016-03-08), https://arxiv.org/abs/1603.02525.
- Classical Catalan first-return decomposition: \(C_n=\sum_{j=1}^{n}C_{j-1}C_{n-j}\); reproduced here as an elementary counted identity.
