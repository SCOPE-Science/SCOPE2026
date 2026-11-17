# The six-site onset and linear growth of Gini instability in Basic Chebyshev isotonic regression

## Finding

For an integer \(n\ge 2\), define the unweighted **Basic** Chebyshev isotonic regression selector \(B_n:\mathbb R^n\to\mathbb R^n\) by
\[
(B_na)_i=\frac12\left(\max_{1\le j\le i}a_j+\min_{i\le j\le n}a_j\right),\qquad 1\le i\le n.
\]
Let the (unnormalized) complete-pair Gini variation be
\[
G_n(a)=\sum_{1\le i<j\le n}|a_i-a_j|,
\]
and define its sharp **two-input** Lipschitz modulus
\[
\Lambda_n=\sup_{G_n(a-b)>0}\frac{G_n(B_na-B_nb)}{G_n(a-b)}.
\]
Then
\[
\boxed{\Lambda_2=\Lambda_3=\Lambda_4=\Lambda_5=1,\qquad\Lambda_6=\frac98.}
\]
In addition, for all integers \(n\ge6\),
\[
\boxed{\frac{\lfloor n^2/4\rfloor}{2(n-2)}\le\Lambda_n
\le\frac{\lfloor n^2/4\rfloor}{n-1}.}
\]
Thus the first strict Gini expansion of this canonical Chebyshev selector occurs at exactly six observations; its sharp two-input Gini instability is already \(12.5\%\) at that threshold, and its modulus grows linearly with dimension. The second displayed inequality is not claimed to be optimal when \(n\ge7\).

## Assumptions and scope

All inputs and outputs are real sequences with a fixed total order on observation indices, all observation weights equal one, and all pairwise differences included in \(G_n\). The selector is the classical Basic/Avg unweighted \(L^\infty\) isotonic regression, **not** the strict \(L^\infty\) regression obtained by limiting \(L^p\) fits. The modulus compares the outputs of two arbitrary nearby or distant inputs, rather than the variation of a single fitted sequence.

The selector really is a Chebyshev best approximation onto the cone of nondecreasing vectors. Let \(r=\frac12\max_{i<j}(a_i-a_j)_+\), with maximum of the empty set zero. Every nondecreasing fit has uniform error at least \(r\). The minimal and maximal feasible fits at error \(r\) are respectively \(\max_{j\le i}a_j-r\) and \(\min_{j\ge i}a_j+r\); their midpoint is precisely \(B_na\). Each of the two envelope sequences is nondecreasing, and this midpoint has uniform error at most \(r\). The same formula shows that \(B_n\) is \(1\)-Lipschitz in the coordinate maximum norm, even though its Gini modulus can exceed one.

## Proof

**1. Exact reduction to permutation chambers.** On every open chamber where the values of \(a\) are pairwise distinct, let \(p(i)\) index the largest value among the first \(i\) coordinates and let \(q(i)\) index the smallest value among the coordinates from \(i\) through \(n\). On this chamber, \(B_n\) is affine-linear with matrix
\[
(Ja)_i=\frac{a_{p(i)}+a_{q(i)}}2.
\]
Every permutation of the ranks occurs in a nonempty chamber. Each matrix preserves constants and is positive row-stochastic. Any segment between two inputs crosses finitely many chamber boundaries; taking the sum of its affine pieces and using the triangle inequality proves that the global Lipschitz modulus is the largest \(G_n\)-operator seminorm of these matrices. Conversely, an arbitrarily short segment inside any chamber attains each local linear ratio. Hence no unexamined tie or nondifferentiability case is needed.

**2. Exact reduction to binary cuts.** For a fixed constant-preserving linear map \(J\), put the coordinates of a nonconstant \(h\) in nondecreasing order. The telescoping decomposition into its distinct consecutive values gives
\[
h=c\mathbf1+\sum_{k=1}^{n-1}d_k\mathbf1_{S_k},\qquad d_k\ge0,
\]
where \(S_k\) consists of the \(n-k\) largest-ranked coordinates, and
\[
G_n(h)=\sum_{k=1}^{n-1}d_k k(n-k).
\]
Consequently
\[
\|J\|_{G_n\to G_n}=
\max_{\varnothing\ne S\subsetneq\{1,\ldots,n\}}
\frac{G_n(J\mathbf1_S)}{|S|(n-|S|)}.
\]
Complementation of \(S\) preserves this ratio, so it suffices to enumerate nonempty indicator subsets that omit the last coordinate.

**3. Complete exact finite bound through six sites.** For each rank permutation and indicator set \(S\), write
\[
u_i=\mathbf1_S(p(i))+\mathbf1_S(q(i))\in\{0,1,2\}.
\]
The candidate ratio has the exact integer expression
\[
R(\text{rank},S)=\frac{\sum_{i<j}|u_i-u_j|}{2|S|(n-|S|)}.
\]
The accompanying standalone certificate `verify_basic_gini.py` enumerates every \(n!\) rank permutation and all \(2^{n-1}-1\) complement-distinct indicator cuts, using only integer arithmetic and exact rational comparison. It exhausts respectively \(2,18,168,1800,22320\) chamber-cut pairs for \(n=2,3,4,5,6\). Its exact maxima are \(1,1,1,1,9/8\). The finite computation is exhaustive **because** Steps 1 and 2 prove that these are all possible local operator norm maximizers. The code also checks the sharpness example directly using exact rational arithmetic.

**4. Six-site sharp witness.** Consider
\[
a=(0,1,2,5,4,3),\qquad h=(1,1,1,0,1,0),\qquad b=a+\varepsilon h
\]
for any \(0<\varepsilon<1\). Both points belong to the same strict rank chamber. Direct evaluation yields
\[
B_6b-B_6a=\varepsilon(1,1,1,0,0,0),\quad G_6(h)=8,\quad G_6((1,1,1,0,0,0))=9.
\]
Thus the ratio is exactly \(9/8\), matching the exhaustive upper bound. An increasing input is fixed by \(B_n\), giving the lower bound \(\Lambda_n\ge1\) in every dimension.

**5. Linear-dimensional lower and upper bounds.** For \(n\ge6\) set \(k=\lfloor n/2\rfloor\) and \(m=n-k\). Choose
\[
a=(0,1,\ldots,k-1,n-1,n-2,\ldots,k)
\]
and let \(h\) equal one in the first \(k\) coordinates and in the \(m-2\) interior coordinates of the descending tail, but zero at the two endpoints of that tail. For \(0<\varepsilon<1\), the rank chamber is unchanged, and
\[
B_n(a+\varepsilon h)-B_n(a)=\varepsilon(\underbrace{1,\ldots,1}_{k},\underbrace{0,\ldots,0}_{m}).
\]
There are precisely two zero coordinates of \(h\), so \(G_n(h)=2(n-2)\); the output indicator has Gini variation \(km=\lfloor n^2/4\rfloor\). This proves the lower bound for every \(n\ge6\).

For the upper bound, Steps 1 and 2 show it is enough to consider \(J\mathbf1_S\). As each \(J\) is row-stochastic and nonnegative, all output coordinates lie in \([0,1]\). For any such vector, the convex function \(G_n\) is maximized over the cube at a binary vertex, with value at most \(\lfloor n^2/4\rfloor\). Since \(G_n(\mathbf1_S)=|S|(n-|S|)\ge n-1\), the claimed upper bound follows. The two bounds are both of exact linear order as \(n\to\infty\).

## Verification

Run `python3 verify_basic_gini.py` using Python's standard library. The script checks all \(24{,}308\) reduced chamber-cut cases for \(2\le n\le6\), the precise six-site equality under four rational perturbations, and the explicit lower-bound family through dimension thirty. It has no external package dependencies. All arithmetic in the deciding comparisons and finite witness calculations is exact; the proof does not extrapolate finite enumeration to arbitrary dimensions. The all-dimensional inequality is established analytically in Step 5.

## Relationship to prior work

The Basic unweighted selector is a classical construction: Stout's study of strict \(L^\infty\) isotonic regression explicitly writes its prefix-max/suffix-min midpoint formula and credits Barlow and Ubhaya for the underlying Basic approximation. The strict/limiting-\(L^p\) selector is different on some data. Later work by Stout addresses efficient calculation of \(L^\infty\) isotonic fits, while Yang and Barber study norm contraction of the **least-squares** isotonic projection, not the Basic Chebyshev selector. These results do not, in the inspected relevant portions, establish the present six-site Gini threshold or linear growth bounds. Classical Gini mean difference supplies the dispersion seminorm but not the nonlinear stability coefficient. See also the limitations and priority caveat below.

## Limitations

The exact coefficient is proved only through dimension six. For larger dimensions the displayed two-sided bounds give the correct order, not an exact constant. The result is restricted to real unweighted chains and the named Basic selector; it says nothing about the strict Chebyshev selector, weighted data, general partial orders, or least-squares isotonic regression. The 1971 Barlow–Ubhaya original was identifiable bibliographically but was not available for complete text comparison, so historical originality remains qualified. No independent mathematical audit is asserted.

## References

1. Q. F. Stout, *Strict \(L^\infty\) Isotonic Regression*, Journal of Optimization Theory and Applications 152 (2012), 121–135, author-hosted full text: https://web.eecs.umich.edu/~qstout/pap/StrictIso.pdf , DOI: https://doi.org/10.1007/s10957-011-9865-8 (particularly Section 2.1 and its citations).
2. Q. F. Stout, *\(L^\infty\) Isotonic Regression for Linear, Multidimensional, and Tree Orders*, arXiv:1507.02226, first submitted 2015-07-08: https://arxiv.org/abs/1507.02226 .
3. Q. F. Stout, *Weighted \(L^\infty\) isotonic regression*, Journal of Computer and System Sciences 91 (2018), 69–81: https://doi.org/10.1016/j.jcss.2017.09.001 .
4. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852, 2017: https://arxiv.org/html/1706.01852v3 .
5. R. E. Barlow and V. A. Ubhaya, *Isotonic approximation*, in *Optimizing Methods in Statistics* (1971), 77–86, cited in Reference 1; original full text was not inspected.
