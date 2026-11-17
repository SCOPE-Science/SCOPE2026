# Sharp fixed-vertex-count law for Minkowski decomposition of Boolean polytopes

## Finding
For integers \(d\ge 1\) and \(2\le k\le 2^d\), call a \(k\)-element set \(S\subseteq\{0,1\}^d\) *coordinate-active* when both binary values occur in each of its \(d\) coordinates. Let \(A_{d,k}\) count such sets, \(I_{d,k}\) count those whose convex hull is Minkowski indecomposable, and \(D_{d,k}=A_{d,k}-I_{d,k}\). In particular, these counts concern **labeled coordinates** and actual embedded vertex sets, not equivalence classes under cube symmetries. Write \(F(j)=2^j-2\) for integers \(j\ge2\).

The total count and the complete indecomposable census are exact:
\[
 A_{d,k}=\sum_{j=0}^{d}(-1)^j\binom dj2^j\binom{2^{d-j}}k,
\qquad
 I_{d,k}=A_{d,k}-\sum_{\substack{\pi\in\Pi([d])\\|\pi|\ge2}}
\sum_{\substack{k_B\ge2\ (B\in\pi)\\\prod_{B\in\pi}k_B=k}}
\prod_{B\in\pi}I_{|B|,k_B}.
\]
The second formula is a recursion in the coordinate dimension, with \(I_{e,k}=0\) whenever \(k>2^e\). For every prime \(k\), one has \(D_{d,k}=0\) **exactly**, for every \(d\).

For each **fixed composite** integer \(k\ge4\), let \(p\) be its smallest prime divisor, let \(q=k/p\), let \(\eta=2\) if \(p=q\) and \(\eta=1\) otherwise, and set \(B_k=F(p)+F(q)=2^p+2^q-4\). As \(d\to\infty\),
\[
 \boxed{D_{d,k}=\frac{B_k^d}{\eta\,p!q!}\bigl(1+O_k(\theta_k^d)\bigr)},
 \qquad \text{for some }0<\theta_k<1,
\]
and, among coordinate-active sets with \(k\) vertices,
\[
 \boxed{\frac{D_{d,k}}{A_{d,k}}
 =\frac{k!}{\eta\,p!q!}
 \left(\frac{2^p+2^q-4}{2^k-2}\right)^d
 \bigl(1+O_k(\theta_k^d)\bigr)}.
\]
The same \(\theta_k\) may be enlarged, while remaining below one, to cover both formulas. These are fixed-\(k\), growing-\(d\) statements; no claim of uniformity in \(k\) is made.

Exact illustrative cases, valid for every \(d\ge2\) (with the natural zero values when there are fewer than \(k\) cube points), are
\[
 D_{d,4}=\frac{4^d-2^{d+1}}8,
 \qquad D_{d,6}=\frac{8^d-6^d-3\cdot4^d+5\cdot2^d}{12},
\]
\[
 D_{d,9}=\frac{12^d-6\cdot8^d+4\cdot6^d+9\cdot4^d-12\cdot2^d}{72}.
\]

## Assumptions and scope
All arithmetic is exact. A coordinate-active set has no constant coordinate; this removes trivial embedded degeneracies but **does not require affine full dimension**. In the fixed-\(k\) regime its affine dimension is at most \(k-1\), regardless of \(d\). A Minkowski decomposition is nontrivial when neither proper summand is homothetic to the whole polytope. The theorem classifies by the number of vertices, not Euclidean dimension, ambient volume, or orbit under cube symmetries.

Every Boolean point of \(S\) is an exposed vertex of \(\operatorname{conv}(S)\). Indeed, the linear functional whose coefficients are \(+1\) on the ones of that point and \(-1\) on the zeros uniquely maximizes at that point among all cube vertices. Therefore \(|S|=k\) equals the number of polytope vertices and is multiplicative under Cartesian products.

The proof uses the published theorem of Higashitani–Padrol–Sanyal that Minkowski decomposition of a Boolean polytope is equivalent to a unique Cartesian product decomposition along disjoint coordinate blocks. That geometric factorization result is **prior work**. The new assertion is the cardinality-refined exact enumeration and sharp fixed-vertex-count rare-event asymptotic.

## Proof
**1. All coordinate-active vertex sets.** For labeled distinct points \(s_1,\ldots,s_k\), each coordinate is a nonconstant word in \(\{0,1\}^k\), yielding \(F(k)^d\) labeled arrays before enforcing distinctness. A collision between two specified rows allows \(F(k-1)^d\) arrays, so the union bound and division by \(k!\) yield
\[
 \frac{F(k)^d-\binom{k}{2}F(k-1)^d}{k!}\le A_{d,k}\le \frac{F(k)^d}{k!},
 \quad A_{d,k}=\frac{F(k)^d}{k!}\bigl(1+O_k((F(k-1)/F(k))^d)\bigr).
\]
Here \(F(1)=0\). Alternatively, to obtain the first displayed *exact* formula, start from all \(k\)-subsets of the \(d\)-cube; choose \(j\) coordinates forced constant, choose each value in two ways, and apply inclusion–exclusion over coordinates.

**2. Exact product recurrence.** The cited Boolean Minkowski factorization theorem gives each decomposable \(S\) a unique *unordered partition* \(\pi\) of the labeled coordinates into nonempty supports of indecomposable factors. Its vertex set is the Cartesian product of the coordinate-projected factor vertex sets; each factor is coordinate-active on its block. If the numbers of vertices of the factors are \(k_B\ge2\), then \(\prod_B k_B=k\). Conversely any such product yields a coordinate-active decomposable Boolean polytope with exactly those indecomposable factors. Counting independently over the blocks gives the stated recurrence without duplicate counting. Prime \(k\) cannot be written as a product of at least two integers exceeding one, so \(I_{d,k}=A_{d,k}\).

**3. Exponential separation of composite vertex counts.** If \(a,b\ge2\), then \(ab\ge a+b\), and
\[
 F(ab)=2^{ab}-2>2^a+2^b-4=F(a)+F(b).
\]
By repeatedly merging factors, for any multiplicative partition \(k=k_1\cdots k_r\) with \(r\ge2\) one has \(\sum_{j=1}^rF(k_j)<F(k)\). Summing the upper bound from Step 1 over assignments of coordinates to factors (there are only finitely many multiplicative partitions of fixed \(k\)) gives
\[
 D_{d,k}=O_k(C_k^d),\qquad C_k<F(k).
\]
Consequently \(I_{d,k}=F(k)^d/k!\,(1+O_k(\xi_k^d))\), for some \(\xi_k<1\), for each fixed \(k\ge2\). The inequality is uniform in the coordinate dimension and works without a full-dimensionality assumption.

**4. Sharp prefactor for each multiplicative partition.** Fix a multiset of factor cardinalities \(\boldsymbol{k}=\{k_1,\ldots,k_r\}\) with \(r\ge2\) and product \(k\). Let \(m_a\) be the multiplicity of cardinality \(a\) in that multiset. Assigning disjoint nonempty labeled-coordinate blocks to those factors and using Step 3 shows that the number of Boolean polytopes with exactly that factor-cardinality multiset is
\[
 N_{d,\boldsymbol{k}}
 =\frac{(F(k_1)+\cdots+F(k_r))^d}
 {\left(\prod_{j=1}^r k_j!\right)\left(\prod_a m_a!\right)}
 \bigl(1+O_{\boldsymbol{k}}(\zeta_{\boldsymbol{k}}^d)\bigr)
\]
for a constant \(\zeta_{\boldsymbol{k}}<1\). To justify the error, use the multinomial expansion by block sizes. Under its normalized weights \(F(k_j)/\sum_iF(k_i)>0\), each block has a positive linear size with exponentially high probability (e.g. by the elementary Chernoff bound). On this central region, the relative error in substituting \(I_{t,k_j}\) by \(F(k_j)^t/k_j!\) is exponentially small by Step 3. The neglected tails, empty blocks and corrections due to row collisions are also exponentially small. Uniqueness of the factorization prevents overlap between distinct multisets; division by \(\prod_a m_a!\) removes permutations of equal-cardinality factors.

**5. The unique dominant arithmetic factorization.** Merging any two factors strictly increases \(\sum_jF(k_j)\); therefore a maximizing proper factorization must have exactly two factors \(a\le b\), with \(ab=k\). On the real interval \(2\le a\le\sqrt k\), the derivative of \(2^a+2^{k/a}\) is
\[
 (\log 2)\left(2^a-\frac{k}{a^2}2^{k/a}\right)<0
\]
except possibly at the right endpoint. Thus the **unique** maximal base comes from \(a=p\), the smallest prime divisor of \(k\), and \(b=q\). Every other multiplicative partition has a strictly smaller exponential base. Summing the finite partition contributions in Step 4 proves the asymptotics, with symmetry factor \(\eta=2\) exactly when the two factor cardinalities coincide.

**6. Exact small-cardinality formulas.** The counts for two and three vertices are \(I_{d,2}=2^{d-1}\) and \(I_{d,3}=(6^d-3\cdot2^d)/6\) for \(d\ge1\). The sole proper factorization of four, six, or nine vertices is respectively \(2\cdot2\), \(2\cdot3\), or \(3\cdot3\). Insert these exact factor counts into the two-block multinomial convolution, accounting for interchange of equal factors. Applying the binomial theorem yields the three stated expressions.

## Verification
The self-contained `verify.py` evaluates the exact active-subset inclusion–exclusion formula and implements the entire prime-factor recurrence using set partitions. Separately, it enumerates **all** Boolean vertex subsets with up to ten points in dimensions one through four and tests all coordinate bipartitions directly for the Cartesian-product criterion. The two implementations agree in all tested configurations; the script also tests the explicit four-, six-, and nine-vertex expressions against the recurrence through dimension five.

Run `python verify.py` with Python 3 and only the standard library. Enumeration is finite and does not prove the statements for arbitrarily large dimensions; the proof is Steps 1–6 above.

## Relationship to prior work
Higashitani–Padrol–Sanyal, *Indecomposability of 0/1-polytopes* (arXiv:2605.22594, first posted May 21, 2026), prove the unique geometric Cartesian decomposition used in Step 2. Their theorem does **not** give the fixed-vertex-count enumerators or the sharp arithmetic asymptotic above.

The published finding *Sharp rare-event law for Minkowski decomposability of Bernoulli Boolean polytopes* (published-finding corpus, October 18, 2026, identifier ending `a5dcb777adc8`) establishes a different law, conditioning on **full affine dimension** for independent Bernoulli retention with a *fixed positive vertex-density parameter*. That regime has exponentially many retained points, unlike the present fixed-\(k\) regime. Its leading event is a full coordinate prism. It does not imply the fixed-cardinality exact counts or the smallest-prime-factor dependence above. Existing treatments of Cartesian factorization of finite relations provide analogous structural decompositions, but no inspected source gave these specific labeled-coordinate, fixed-cardinality formulas.

## Limitations
The asymptotic theorem holds only with fixed \(k\) as \(d\to\infty\). It does not address growing-\(k\) regimes, full-dimensional sampling, or equivalence classes under cube symmetries. The exact recurrence is finite but grows rapidly in \(d\). Historical priority is provisional: the same enumeration might occur in older Boolean-function or relational-product literature under different terminology. No independent specialist review has been performed.

## References
- A. Higashitani, A. Padrol, and R. Sanyal, *Indecomposability of 0/1-polytopes*, arXiv:2605.22594 (first posted 2026-05-21), https://arxiv.org/html/2605.22594v1.
- *Sharp rare-event law for Minkowski decomposability of Bernoulli Boolean polytopes*, published-finding corpus (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-rare-event-law-for-minkowski-decomposability-of-bernoulli--a5dcb777adc8.
- W. Y. C. Chen and P. L. Guo, *Equivalence Classes of Full-Dimensional 0/1-Polytopes with Many Vertices*, arXiv:1101.0410 (2011), https://arxiv.org/abs/1101.0410 (distinct counting regime, included for context).
