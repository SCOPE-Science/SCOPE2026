# Exact lexicographic minimizer density and two-step plateaus on the golden-mean source

## Finding

Let \(X\subset\{0,1\}^{\mathbb Z}\) be the shift forbidding adjacent `11`, equipped with its unique maximal-entropy stationary measure \(\mu\). For every integer \(k\ge1\), use the ordinary lexicographic ordering \(0<1\) of binary \(k\)-mers, break equal-minimum ties to the left, and select one minimizer position from every window of **three** consecutive \(k\)-mers. The asymptotic fraction \(\rho_k\) of selected \(k\)-mer locations exists \(\mu\)-almost surely and in mean, and equals

\[
\boxed{\rho_k=\frac{2+\varphi^{-(2\lfloor k/2\rfloor+1)}}{\varphi+2}},\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]

In particular \(\rho_{2m}=\rho_{2m+1}\) for every \(m\ge1\), \(\rho_{2m+1}>\rho_{2m+2}\), and
\[
\lim_{k\to\infty}\rho_k=\frac2{\varphi+2}=1-\frac1{\sqrt5}.
\]

More precisely, let \(C_k^{ab}\) count charged admissible binary contexts of length \(k+3\), beginning with \(a\) and ending with \(b\), for \(a,b\in\{0,1\}\). A context is **charged** if the minimizer locations in its two consecutive three-\(k\)-mer windows differ. With Fibonacci numbers \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\), the complete endpoint-refined count is
\[
\boxed{\begin{aligned}
C_k^{00}&=F_{k+2}+1,\\
C_k^{01}&=F_{k+1}+\mathbf1_{k\text{ odd}},\\
C_k^{10}&=F_k-\mathbf1_{k\text{ odd}},\\
C_k^{11}&=F_{k-1}-\mathbf1_{k\text{ even}}.
\end{aligned}}
\]

## Assumptions and scope

The source is the **stationary Parry measure**, not the uniform distribution on finite admissible words. The alphabet is binary, the excluded factor is `11`, the minimizer window consists of exactly three overlapping \(k\)-mers, the order is lexicographic with \(0<1\), and ties go to the left. Positions are distinguished even if the corresponding \(k\)-mers coincide. The claim is for every integer \(k\ge1\) and the two-sided stationary source. The same mean density is the limit of selected-position counts divided by all available \(k\)-mer positions in any sufficiently long sample, with fixed \(k\).

## Proof

**1. Charge representation.** For any legal word \(s=s_0\cdots s_{k+2}\), put \(K_i=s_i\cdots s_{i+k-1}\), \(0\le i\le3\). Compare the smallest of \(K_0,K_1,K_2\) with the smallest of \(K_1,K_2,K_3\), always breaking equal values toward the smaller index. The two selected positions differ exactly when the context is charged. This indicator is the increment in the number of selected minimizer positions when a new window is added. Its stationary expectation is therefore the mean density; by the ergodic theorem, the same density holds almost surely.

**2. Local ordering.** Because `11` is forbidden, \(s_i=0\) implies \(K_i\le_{\rm lex}K_{i+1}\): the first possible difference in two adjacent suffixes is a `01` transition. Conversely \(s_i=1\) implies \(K_i>_{\rm lex}K_{i+1}\), since the next bit is zero. The five possible prefixes \(s_0s_1s_2\) lead to the following exhaustive cases:

- `000` or `001`: charged, because the first window chooses \(K_0\), which exits the next window.
- `100`: uncharged, because both windows choose \(K_1\).
- `010`: charged exactly when \(K_0\le K_2\), because the two candidate minima of the first window are \(K_0,K_2\), while the next chooses \(K_2\). For an admissible word beginning `010`, the inequality holds exactly if \(s_0\cdots s_{k+1}\) alternates. Indeed, any first disagreement between the length-\(k\) sequences starting at positions zero and two results from a `10` versus `00` transition, so it makes \(K_0>K_2\); equality occurs precisely during complete alternation.
- `101`: necessarily begins `1010`; the first window chooses \(K_1\), and the next chooses \(K_3\) instead precisely when \(K_3<K_1\). This holds exactly when \(s_1\cdots s_{k+2}\) fails to alternate: complete alternation makes those two \(k\)-mers equal; the first break makes the later one smaller.

**3. Exact endpoint counts.** Admissible contexts beginning `00` contribute \(F_{k+2}\) with final zero and \(F_{k+1}\) with final one. Among the alternating-prefix `010` contexts, exactly one ends in zero for every \(k\), and one additional context ends in one iff \(k\) is odd. Admissible contexts beginning `1010` contribute \(F_k\) ending in zero and \(F_{k-1}\) ending in one, but exactly one fully alternating suffix must be excluded, ending in zero iff \(k\) is odd (in one iff \(k\) is even). Summing the disjoint cases proves all four displayed Fibonacci identities. Their sum also gives the finite-context charged count \(2F_{k+2}+F_{k-1}+1-\mathbf1_{k\text{ even}}\).

**4. Stationary weighting and simplification.** The admissibility matrix is
\[
A=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\]
whose Perron eigenvalue is \(\varphi\) and whose left and right eigenvectors can both be taken as \(r=(\varphi,1)\). Accordingly, any legal word \(s\) of length \(k+3\) has the exact Parry cylinder probability
\[
\mu[s]=\frac{r_{s_0}r_{s_{k+2}}}{(\varphi+2)\varphi^{k+2}}.
\]
Thus the charged probability is
\[
\rho_k=\frac{\varphi^2 C_k^{00}+\varphi(C_k^{01}+C_k^{10})+C_k^{11}}
{(\varphi+2)\varphi^{k+2}}.
\]
The numerator, by step 3 and \(\varphi^2+\varphi=\varphi^3\), equals
\[
\varphi^3F_{k+2}+F_{k-1}+\varphi^2-\mathbf1_{k\text{ even}}.
\]
The Fibonacci identity \(\varphi^3F_{k+2}+F_{k-1}=2\varphi^{k+2}\) holds at \(k=1,2\) and thereafter by the shared Fibonacci recursion. Therefore
\[
\rho_k=\frac{2+(\varphi^2-\mathbf1_{k\text{ even}})\varphi^{-(k+2)}}{\varphi+2}.
\]
If \(k\) is even, \(\varphi^2-1=\varphi\); if odd, the correction is \(\varphi^2\). Both cases simplify to \(\varphi^{-(2\lfloor k/2\rfloor+1)}\). This proves the all-\(k\) formula, two-step plateaus, strict intervening decreases, and limit.

## Verification

Run `python3 verify.py` with the Python 3 standard library. Its separate brute-force minimizer implementation and prefix-based structural implementation agree for all admissible contexts and every \(1\le k\le20\), totaling 196,405 contexts. The script verifies each endpoint count against the Fibonacci formulas, computes Parry-weighted densities using 50-digit decimal arithmetic, and tests plateau/decrease patterns up to \(k=99\). These finite checks only test the all-parameter proof; they are not substitutes for steps 1–4.

For illustration the exact densities begin \(\rho_1\simeq0.723606797750\), \(\rho_2=\rho_3=\varphi^{-1}\simeq0.618033988750\), and \(\rho_4=\rho_5\simeq0.577708764000\).

## Relationship to prior work

Zheng, Marçais, and Kingsford (2023) formalize minimizer schemes, leftmost tie-breaking, charged contexts, and the equivalence between expected density and charged-context probability. Those generic identities are used here, but they do not specify the endpoint-refined Fibonacci counts, this non-iid source, or the two-step plateau formula. Hoang, Marçais, and Kingsford (first online 2023) optimize generalized masked minimizer density and conservation, without deriving this particular source-dependent exact lexicographic law. Other reported small-\(k\) optimization studies concern iid biased or uniform sources and different objective/parameter ranges. This statement does not follow numerically from those published density values.

## Limitations

This is a theorem about a specific stationary constrained source, a fixed three-\(k\)-mer window, and ordinary lexicographic ordering. It does not assert optimality of that ordering, extend to other alphabet sizes or window widths, or predict density on real genomic data. A **uniform random finite admissible context** has charged fraction
\[
\frac{2F_{k+2}+F_{k-1}+1-\mathbf1_{k\text{ even}}}{F_{k+5}},
\]
which is generally different from the stationary Parry density. Historical priority of a formula hidden in unindexed sources remains uncertain; no independent expert audit has occurred.

## References

1. H. Zheng, G. Marçais, and C. Kingsford, “Creating and Using Minimizer Sketches in Computational Genomics,” *Journal of Computational Biology* 30 (2023), https://doi.org/10.1089/cmb.2023.0094, first online 2023-08-30. See definitions of minimizer, density, and charged context and Lemmas 5–6.
2. M. Hoang, G. Marçais, and C. Kingsford, “Density and Conservation Optimization of the Generalized Masked-Minimizer Sketching Scheme,” *Journal of Computational Biology* 31 (2024), https://doi.org/10.1089/cmb.2023.0212, first online 2023-11-17. See sections 1–2 and the optimization formulation.
