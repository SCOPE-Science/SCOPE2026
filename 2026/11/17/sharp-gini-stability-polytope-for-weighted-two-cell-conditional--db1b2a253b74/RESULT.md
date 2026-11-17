# Sharp Gini stability polytope for weighted two-cell conditional expectations

## Finding
Let \(n=a+b\ge2\), with \(a,b\ge1\). Partition the coordinates into two nonempty labelled classes \(A,B\), of sizes \(a,b\). Let \(p_i>0\) for \(i\in A\) and \(q_j>0\) for \(j\in B\), normalized by \(\sum_{i\in A}p_i=\sum_{j\in B}q_j=1\). Define the positive idempotent conditional averaging operator
\[
(P_{p,q}x)_i=\begin{cases}
\sum_{r\in A}p_rx_r,&i\in A,\\
\sum_{r\in B}q_rx_r,&i\in B.
\end{cases}
\]
For real signals, write the unweighted complete-pair Gini seminorm
\[
G(x)=\sum_{1\le i<j\le n}|x_i-x_j|.
\]
Let \(P_k^{\downarrow}\) be the sum of the \(k\) largest probabilities in class \(A\), and let \(Q_k^{\downarrow}\) be the corresponding sum in class \(B\). Then the **exact, attained two-input operator seminorm** is
\[
\boxed{\displaystyle
L_{p,q}=\sup_{G(x-y)>0}\frac{G(P_{p,q}x-P_{p,q}y)}{G(x-y)}
=ab\max\left\{\max_{1\le k\le a}\frac{P_k^{\downarrow}}{k(n-k)},\ \max_{1\le k\le b}\frac{Q_k^{\downarrow}}{k(n-k)}\right\}.}
\]
Every maximizing term is realized by an indicator of exactly those \(k\) largest-weight coordinates in its own class. In particular, **all-input Gini nonexpansivity** is equivalent to the complete system
\[
P_k^{\downarrow}\le\frac{k(n-k)}{ab}\quad(1\le k\le a),\qquad
Q_k^{\downarrow}\le\frac{k(n-k)}{ab}\quad(1\le k\le b).
\]
These inequalities define a nonempty closed convex polytope (relative to the closed product of the two probability simplices). The strictly positive part is the exact stability region.

There are three additional sharp conclusions.

**Exact mass-imbalance tolerance.** Assume \(a,b\ge2\). With \(u_A,u_B\) the uniform class distributions and \(d_{\rm TV}(p,u_A)=\frac12\sum_{i\in A}|p_i-1/a|\), every pair satisfying
\[
d_{\rm TV}(p,u_A)\le\frac{a-1}{ab},\qquad
 d_{\rm TV}(q,u_B)\le\frac{b-1}{ab}
\]
is nonexpansive. The displayed separate radii are each largest possible: exceeding either by an arbitrarily small amount can yield expansion while the other class stays exactly uniform.

**Sharp mass-concentration envelope.** For fixed positive class sizes,
\[
\boxed{\displaystyle \sup_{p_i,q_j>0} L_{p,q}=\frac{ab}{n-1}.}
\]
For \(a,b\ge2\), this value is not attained by any strictly positive pair of probability vectors, but is approached by concentrating one class on a single vertex. If \(\min(a,b)=1\), every permissible weighting has norm exactly one. Accordingly, amplification first becomes possible for \(n=4\), and for balanced classes \(a=b=n/2\) the envelope is \(n^2/[4(n-1)]\), asymptotic to \(n/4\).

**Non-bistochastic contraction.** For \(a=b=2\), the complete criterion reduces to \(\max_i p_i\le3/4\) and \(\max_jq_j\le3/4\). In particular \(p=(2/3,1/3)\) and \(q=(1/2,1/2)\) give a positive, non-doubly-stochastic conditional expectation with \(L_{p,q}=1\), whereas changing the first class to \(p=(4/5,1/5)\) gives \(L_{p,q}=16/15\).

## Assumptions and scope
The data are real-valued, with no ordering assumption on the coordinates. Every within-class probability is strictly positive; the formula itself extends continuously to zero weights, but nonattainment in the mass-concentration statement uses strict positivity. The complete-pair Gini variation is unweighted even when the conditional expectation weights are unequal. The map preserves constants, so \(G\) is a norm after quotienting by constant vectors, and the displayed two-input quotient is well-defined. All statements hold for any relabelling of coordinates and both class sizes, including singleton classes. There is no claim for more than two output classes or for weighted pair-variation edges.

## Proof
**1. Reduce the operator quotient to an absolute linear functional.** Let \(\mu_A(x)=\sum_{i\in A}p_ix_i\) and \(\mu_B(x)=\sum_{j\in B}q_jx_j\). Since the output is constant on each class, its nonzero pair differences occur on the \(ab\) cross-class pairs, and hence
\[
G(P_{p,q}x)=ab|\mu_A(x)-\mu_B(x)|.
\]
Also \(P_{p,q}\mathbf1=\mathbf1\); therefore the requested two-input norm equals the one-input induced seminorm.

**2. A finite cut principle, without an unproved linear-programming reduction.** For any \(x\in\mathbb R^n\), order its distinct values increasingly. By subtracting its minimum and decomposing it into positive gaps times indicators of successive upper level sets \(S_r\), one has \(x=c\mathbf1+\sum_r\delta_r\mathbf1_{S_r}\), where \(\delta_r>0\). Each pair contributes precisely its total level-crossing gaps, so
\[
G(x)=\sum_r\delta_r\,|S_r|(n-|S_r|).
\]
By the triangle inequality and preservation of constants,
\[
G(P_{p,q}x)\le\sum_r\delta_r\,G(P_{p,q}\mathbf1_{S_r}).
\]
Thus the sharp induced norm is the maximum ratio over nonempty proper binary cuts, and an optimizing binary cut attains it. No finite test is being used in place of this all-dimensional argument.

**3. Optimize every cardinality exactly.** Let \(c\in\mathbb R^n\) have coefficients \(p_i\) on \(A\) and \(-q_j\) on \(B\), so \(\sum_i c_i=0\). For a cut \(S\),
\[
\frac{G(P_{p,q}\mathbf1_S)}{G(\mathbf1_S)}=
\frac{ab|\sum_{i\in S}c_i|}{|S|(n-|S|)}.
\]
At fixed size \(k\), the largest signed sum uses the \(k\) largest entries of \(c\). If \(k\le a\), these are the \(k\) largest entries of \(p\), giving \(P_k^{\downarrow}\). If \(k>a\), they comprise all of \(p\) together with the \(k-a\) smallest negative entries \(-q_j\), giving the sum \(Q_{n-k}^{\downarrow}\) of the \(n-k\) largest entries of \(q\). Replacing a cut by its complement changes the sign but not the ratio, so taking the two families over \(1\le k\le a\) and \(1\le k\le b\) includes both signs. This proves the norm formula and every attainment claim. The full stability polytope follows because the indicator of all of \(A\) has ratio one, so \(L_{p,q}\ge1\).

**4. Quantify the stable neighbourhood.** For a probability vector \(p\) on \(a\) atoms, the elementary total-variation identity gives \(P_k^{\downarrow}\le k/a+d_{\rm TV}(p,u_A)\). For \(1\le k<a\),
\[
\frac{k(n-k)}{ab}-\frac ka=\frac{k(a-k)}{ab}\ge\frac{a-1}{ab}.
\]
Hence the asserted distance bound on \(p\) implies every required partial-sum inequality. The argument for \(q\) is identical, and the full-class inequalities at \(k=a,b\) are equalities. To prove sharpness of the first radius, set \(\delta=(a-1)/(ab)+\varepsilon\) and
\[
p_1=\frac1a+\delta,\qquad p_2=\cdots=p_a=\frac1a-\frac\delta{a-1}.
\]
For sufficiently small positive \(\varepsilon\), all coordinates are strictly positive, their total-variation distance from uniform is exactly \(\delta\), and \(abp_1>n-1\); the singleton cut strictly amplifies. Keep \(q\) uniform. The analogous construction for the second class establishes its independent sharpness.

**5. Maximize over all weights.** For \(1\le k<n\), the elementary integer inequality \(k(n-k)\ge n-1\), together with \(P_k^{\downarrow},Q_k^{\downarrow}\le1\), gives \(L_{p,q}\le ab/(n-1)\). If one class is a singleton, \(ab=n-1\), while the full-class binary cut already has ratio one. If \(a,b\ge2\), one probability vector may concentrate arbitrarily closely at one atom while remaining positive, producing ratios approaching \(ab/(n-1)\). Equality is impossible at positive weights: a maximizing partial-sum ratio would require both \(k(n-k)=n-1\) and a partial sum one; since each class has at most \(n-2\) atoms, the only possible index is \(k=1\), but no single weight is one. For both class sizes at least two, \(ab>n-1\) since \(ab-(a+b-1)=(a-1)(b-1)>0\); the first amplifying dimension is four. The balanced asymptotic and explicit four-site examples follow by substitution.

## Verification
Run `python3 check.py` with Python 3 and the standard library only. Its exact rational arithmetic independently compares the formula with every nontrivial binary cut for 75 rational positive mass vectors across all class-size pairs up to five. It checks randomly chosen rational real signals against the proposed norm, checks uniform weights across 1600 class-size pairs through size forty, checks both sharp mass-imbalance radii and nearby strictly positive violations in 256 class-size pairs, and verifies the two contrasting four-site examples. The recorded successful output is reproduced in `VERIFICATION.md`. These finite checks corroborate critical formulas; the proof above is valid in all finite dimensions and for arbitrary real positive mass weights.

## Relationship to prior work
Estaremi's preprint on weighted conditional expectation operators (arXiv:1302.0597, first posted February 4, 2013) develops \(L^2\) boundedness, polar decomposition and spectral decomposition for multiplication–conditional-expectation operators. It supplies a natural operator-theoretic starting point but not a norm formula in complete-pair Gini variation or an unweighted variation contractivity classification.

Khan, Latif and Pečarić's 2012 paper on majorization (open-access journal publication May 8, 2012) provides background convex/majorization inequalities. For equal within-class masses, the averaging matrix is doubly stochastic, and the classical symmetric-convex argument gives Gini contraction. Such a general implication does not classify the non-bistochastic positive idempotents treated here: some of them contract Gini while others amplify it, and the exact boundary depends on every sorted partial sum.

The published finding *Sharp cyclic-variation stability of two-cell conditional expectations* (published-finding corpus record 2026/11/1/.../19779f163091) treats the **same class of two-cell averaging operators** but uses cyclic adjacent-edge total variation, for which its sharp norm is the number of color runs times a cumulative mass-discrepancy range. Its full `RESULT.md` was compared, including the proof and equality conditions. That variation norm depends on cyclic arrangement, unlike the present permutation-invariant complete-pair variation. For a four-site alternating arrangement with class masses \(p=(2/3,1/3)\), \(q=(1/2,1/2)\), its cyclic-edge norm is \(4/3\) while the present exact Gini norm is one. Neither norm bound implies the other's exact stability region.

The separate *Sorted-rate criterion and sharp first obstruction for clique-heat variation* (published-finding corpus record 2026/11/2/.../b99f02c470ef) gives infinitesimal conditions for a continuous heat semigroup on a complete graph. Its operator is not this idempotent two-cell conditional expectation, and its result is neither an all-weight classification of two-cell averaging nor a finite-time norm identity for it. Gini-mean-difference inequalities surveyed by Cerone (2008) are additional related background; the accessible institutional repository offered only an abstract, so a hidden specialized analogue there remains a literature-access risk.

## Limitations
The classification is restricted to **exactly two** output classes and unweighted complete-pair Gini variation on finite real signal spaces. Its strongest mass-concentration constant is a **supremum across different weight vectors**, not attained for strictly positive weights when both classes have at least two elements. The total-variation radii are largest *guaranteed neighbourhood radii*, not necessary conditions for each stable nonuniform mass vector; the exact necessary-and-sufficient test is the partial-sum polytope. The direct literature inspection and database searches do not prove priority against every unindexed source. There is no assertion about arbitrary multi-cell projections, weighted pairwise dispersion or infinite-measure extensions.

## References
1. Y. Estaremi, *Decompositions of Weighted Conditional Expectation Type Operators*, arXiv:1302.0597, first public preprint February 4, 2013. https://arxiv.org/abs/1302.0597
2. A. R. Khan, N. Latif and J. Pečarić, *Exponential convexity for majorization*, Journal of Inequalities and Applications 2012, article 105, published May 8, 2012, DOI:10.1186/1029-242X-2012-105. https://link.springer.com/article/10.1186/1029-242X-2012-105
3. *Sharp cyclic-variation stability of two-cell conditional expectations*, published published-finding corpus record 2026/11/1/SCOPE-sharp-cyclic-variation-stability-of-two-cell-conditional-expecta--19779f163091, `RESULT.md`. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-cyclic-variation-stability-of-two-cell-conditional-expecta--19779f163091
4. *Sorted-rate criterion and sharp first obstruction for clique-heat variation*, published published-finding corpus record 2026/11/2/SCOPE-sorted-rate-criterion-and-sharp-first-obstruction-for-clique-hea--b99f02c470ef, `RESULT.md`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sorted-rate-criterion-and-sharp-first-obstruction-for-clique-hea--b99f02c470ef
5. P. Cerone, *Bounding the Gini Mean Difference*, International Series of Numerical Mathematics 157 (2008), 77–89, DOI:10.1007/978-3-7643-8773-0_8. Full text not accessible from the inspected repository. https://vuir.vu.edu.au/5289/
