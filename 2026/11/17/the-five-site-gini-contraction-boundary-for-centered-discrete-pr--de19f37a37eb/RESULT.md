# The five-site Gini-contraction boundary for centered discrete primitives

## Finding
Let \(n\ge2\). For real vectors \(x\in\mathbb R^n\) define the centered discrete primitive \(T_n\) by
\[
(T_nx)_i=\sum_{r=1}^{i}\left(x_r-\frac1n\sum_{s=1}^n x_s\right),\qquad 1\le i\le n,
\]
and define unweighted complete-pair Gini variation by
\[
G_n(x)=\sum_{1\le i<j\le n}|x_i-x_j|.
\]
The induced quotient seminorm \(L_n=\sup_{G_n(x)>0}G_n(T_nx)/G_n(x)\) satisfies
\[
\boxed{L_n\le1\ \Longleftrightarrow\ 2\le n\le5.}
\]
More precisely, \(L_2=1/2\), \(L_3=2/3\), \(L_4=5/6\), and \(L_5=1\), while for every \(n\ge2\)
\[
\boxed{\frac{n+1}{6}\le L_n\le\frac{\lfloor n^2/4\rfloor}{n}.}
\]
The lower bound is attained as a ratio by every one-coordinate indicator. Thus, for every \(n\ge6\), the same explicit input witnesses strict amplification, and the optimal amplification grows linearly with dimension.

## Assumptions and scope
The input is an arbitrary real finite vector indexed \(1,\ldots,n\), with the standard cyclic centering convention: the cumulative increments have zero total and hence the last output coordinate is zero. The quotient seminorm ignores additive constants, and \(T_n\) annihilates constants, so its induced operator norm is well-defined. No positivity, ordering, smoothness, or probability assumptions are imposed on inputs.

## Proof
**Step 1 (interval crossing identity and uniform upper bound).** For \(1\le i<j\le n\), write \(I_{ij}=\{i+1,\ldots,j\}\), of cardinality \(d=j-i\). The difference of two output coordinates is
\[
(T_nx)_j-(T_nx)_i=\sum_{r\in I_{ij}}(x_r-\bar x)
=\frac1n\sum_{r\in I_{ij}}\sum_{s\notin I_{ij}}(x_r-x_s).
\]
Applying the triangle inequality, summing over \(i<j\), and then interchanging sums yields
\[
G_n(T_nx)\le\frac1n\sum_{1\le p<q\le n}N_{p,q}|x_p-x_q|,
\]
where \(N_{p,q}\) is the number of intervals \(I_{ij}\) containing exactly one of the two indices \(p,q\). Every such interval is a contiguous subinterval of \(\{2,\ldots,n\}\). Counting endpoints directly gives \(N_{p,q}=(q-p)(n-q+p)\) (for \(p=1\), only intervals containing \(q\) contribute, giving the same count). Consequently
\[
G_n(T_nx)\le \frac{\lfloor n^2/4\rfloor}{n}G_n(x).
\]

**Step 2 (singleton lower bound).** For \(x=e_1\), one has \((T_n e_1)_i=1-i/n\). Therefore
\[
G_n(T_ne_1)=\frac1n\sum_{i<j}(j-i)=\frac{n^2-1}{6},\qquad G_n(e_1)=n-1,
\]
which proves \(L_n\ge(n+1)/6\). This quantity exceeds one for all \(n\ge6\), proving failure of nonexpansivity there.

**Step 3 (exact small dimensions).** A finite coarea reduction is valid for any constant-annihilating linear map \(T\): write \(x=\min_r x_r\,\mathbf1+\int\mathbf1_{\{r:x_r>t\}}\,dt\), apply \(T\), use convexity and homogeneity of \(G_n\), and observe \(G_n(x)=\int k_t(n-k_t)\,dt\), where \(k_t\) is the size of the level-set cut. It follows that the sharp quotient norm equals the largest binary-cut quotient \(G_n(T\mathbf1_S)/(|S|(n-|S|))\), with \(\varnothing\ne S\subsetneq\{1,\ldots,n\}\). For \(n=2,3,4,5\), direct exact enumeration of every such cut gives, grouped by cut size \(k=1,\ldots,n-1\):

| \(n\) | Sharp quotients for successive cut sizes \(k\) |
| --- | --- |
| 2 | \(1/2\) |
| 3 | \(2/3,\ 2/3\) |
| 4 | \(5/6,\ 3/4,\ 5/6\) |
| 5 | \(1,\ 14/15,\ 14/15,\ 1\) |

The included exact-rational checker computes each entry from the defining formulas, considering all \(2^n-2\) cuts, not a sample. By the coarea reduction these finite computations certify the exact operator norm in these four dimensions. Hence every dimension up to five is nonexpansive; combined with Step 2 the threshold is sharp. \(\square\)

## Verification
Run `python3 check.py` using only the Python standard library. It verifies all 52 nontrivial binary cuts over dimensions two through five and independently checks the singleton ratio and analytic-bound inequalities for dimensions two through fifty-nine. The proof of the all-dimensional interval bound and the singleton obstruction is analytical; no extrapolation from finite tests is used.

## Relationship to prior work
Finite prefix and Cesàro summation operators have extensive functional-analytic literature. Curbera and Ricker's 2013 treatment concerns normalized Cesàro mappings and Hardy-space optimal domains; the present finite operator is an **unnormalized, mean-centered primitive**, measured in complete-pair Gini variation. These normalizations are not isometries of the target seminorm, and that published analysis does not assert the dimension-five stability boundary here. Standard variation-norm and maximal-function contraction results use different operators or different seminorms. This result makes the finite-dimensional Gini threshold and its interval-crossing mechanism explicit; exhaustive historical priority is not claimed.

## Limitations
The upper and lower bounds do not coincide for general \(n>5\), so the exact norm beyond dimension five is **not proved here**. Only unweighted pairwise Gini variation and uniform discrete centering are treated; weighted observations, alternative normalization, and continuous limit operators require separate arguments. Literature coverage may omit equivalent results under different terminology. The computational certificate is exhaustive only in the stated small dimensions.

## References
1. G. P. Curbera and W. J. Ricker, *Solid Extensions of the Cesàro Operator on the Hardy Space H²*, Oberwolfach Preprints OWP 2013-11, first publicly posted April 23, 2013. https://www.mfo.de/document/1314/OWP2013_11.pdf
2. The standard finite layer-cake/coarea identity for absolute pairwise differences is used with a self-contained derivation above.
