# A Fréchet law for the largest shared key interval in independent random binary search trees

## Finding
For each integer \(n\ge2\), independently build two binary search trees from independent uniformly random insertion orders of the **same** ordered keys \(1,\ldots,n\). A *fringe key interval* is the full set of keys descended from some node; in a binary search tree it is an interval of consecutive keys. Call an interval *shared* if it is a fringe key interval in both trees. Exclude the full root interval \([1,n]\), and let \(M_n\) be the maximum cardinality of any remaining shared interval (zero if none exists).

For every fixed \(x>0\),
\[
\lim_{n\to\infty}\Pr\{M_n < x n^{1/3}\}
= \exp\!\left(-\frac{4}{3x^3}\right).
\]
More precisely, for fixed \(0<x<y<\infty\), the number \(N_n(x,y)\) of shared proper intervals of sizes between \(\lceil x n^{1/3}\rceil\) and \(\lfloor y n^{1/3}\rfloor\) converges in total variation to a Poisson law of mean \(\tfrac43(x^{-3}-y^{-3})\). The point-process intensity in the size coordinate is \(4u^{-4}\,du\). Thus independent tree construction changes the critical *shared* fringe scale from the single-tree fixed-size \(\sqrt n\) regime to an extreme-size \(n^{1/3}\) regime.

For exact finite-size calibration, the expected number of shared intervals of each size \(1\le k<n\) is
\[
\mathbb E C_{n,k}=
\frac{4(n-k-1)}{(k+1)^2(k+2)^2}+\frac{2}{(k+1)^2}.
\]

## Assumptions and scope
The two insertion permutations are independent and uniform on \(n\) distinct totally ordered keys. Equivalently, each tree has an independent vector of iid continuous priorities, and its root is the smallest-priority key with recursive Cartesian subtrees on either side. A fringe key interval is defined by node descendants, **not** by shape isomorphism or shared insertion times. Only non-root intervals count toward \(M_n\). All limit statements concern \(n\to\infty\) with fixed positive window endpoints.

## Proof
**One-interval probability.** Write \(I=[a,b]\), with \(k=b-a+1<n\). Its fringe condition is that every existing neighboring boundary priority, at \(a-1\) and/or \(b+1\), is below the minimum priority among the \(k\) interior keys. (Here and below nonexistent boundaries are omitted.) Hence for an interior interval
\[
p_k=\frac{2}{(k+1)(k+2)},
\]
while for either terminal interval \(p_k^{\partial}=1/(k+1)\). For two independent trees the respective probabilities square. There are \(n-k-1\) interior and two terminal intervals, giving the displayed exact mean.

**Joint dependence classification.** Let \(F_I\) denote the one-tree fringe event for an interval \(I\). If \(J\subsetneq I\), then conditional on \(F_I\), the relative priorities inside \(I\) are a fresh uniform permutation. Consequently
\[
\Pr(F_I\cap F_J)=\Pr(F_I)\,p_{J\mid I},
\]
where \(p_{J\mid I}\) is the same one-interval formula inside the parent key interval. If two intervals overlap without containment, both cannot be fringe because rooted subtrees are laminar. If they are adjacent and disjoint, their two boundary conditions contradict each other, so simultaneous occurrence is again impossible. If their extended key intervals (obtained by adjoining existing immediate neighbors) are disjoint, the events are independent.

The only other interaction is a pair of disjoint intervals of lengths \(k,\ell\) separated by exactly one key of priority \(t\). With exterior boundaries present, their one-tree joint probability is
\[
H_{k,\ell}=\int_0^1 A_k(t)A_\ell(t)\,dt,
\quad A_j(t)=t(1-t)^j+\frac{(1-t)^{j+1}}{j+1}.
\]
If an exterior boundary is absent, replace its \(A_j(t)\) by \((1-t)^j\). For \(K\le k,\ell\le LK\) and fixed \(L>1\), the displayed integral is \(O_L(K^{-3})\) with both outer boundaries, since \(A_j(t)\le (t+1/(j+1))e^{-jt}\). If exactly one boundary is missing, it is \(O_L(K^{-2})\). All these one-tree joint probabilities square in the independent two-tree model.

**A Poisson window.** Fix \(x,y\) with \(0<x<y\). Write \(K=\lceil x n^{1/3}\rceil\), \(L>y/x+1\), and consider all key intervals with lengths in \([K,\lfloor y n^{1/3}\rfloor]\). The common-fringe indicator for each interval depends only on the independent priority pairs at that interval and its immediate neighbors. Thus the family has a dependency graph whose neighborhoods have at most \(O_L(K^2)\) other intervals. There are \(O_L(nK)\) interior candidates, each of probability \(O_L(K^{-4})\), plus \(O_L(K)\) terminal candidates, each of probability \(O_L(K^{-2})\).

The standard dependency-graph Poisson bound uses \(b_1=\sum_I\sum_{J\sim I}\Pr(F_I^{(1)}F_I^{(2)})\Pr(F_J^{(1)}F_J^{(2)})\) and \(b_2=\sum_I\sum_{J\sim I,\,J\ne I}\Pr(F_I^{(1)}F_I^{(2)}F_J^{(1)}F_J^{(2)})\). Direct counting gives
\[
b_1=O_L(n/K^5+K^{-2}),\qquad
b_2=O_L(n/K^4+K^{-2}).
\]
Indeed, crossing-overlap and adjacent-disjoint pairs contribute zero. Nested pairs with the smaller interval touching a parent boundary contribute at most \(O_L(nK^2)\) terms of probability \(O_L(K^{-6})\); nested pairs strictly interior contribute at most \(O_L(nK^3)\) terms of probability \(O_L(K^{-8})\). One-key-separated interior pairs contribute at most \(O_L(nK^2)\) terms of probability \(O_L(K^{-6})\) by the integral bound. Exceptional pairs touching an extreme global boundary contribute \(O_L(K^{-2})\) in total. These exhaust dependence. At \(K\asymp n^{1/3}\), both bounds vanish, so total variation from Poisson of the exact mean tends to zero.

Using the finite mean identity, the mean of the window count is
\[
\sum_{k=K}^{\lfloor y n^{1/3}\rfloor}\left(
\frac{4(n-k-1)}{(k+1)^2(k+2)^2}+\frac{2}{(k+1)^2}
\right)\longrightarrow \frac43(x^{-3}-y^{-3}).
\]
This proves the window law. For fixed \(x>0\), the expected number of proper shared intervals longer than \(y n^{1/3}\) has limiting superior at most \(4/(3y^3)\) by the same exact mean and summation, with boundary terms vanishing. Letting \(y\to\infty\) yields the Fréchet maximum law by the zero-count event in a finite window. Standard disjoint-window Poisson approximation, or the same dependency-graph bound with independent marks, gives the stated size point-process intensity.

## Verification
Run `python verify.py` using Python 3 standard library only. The program independently recursively builds Cartesian trees from every priority permutation of orders two through seven; enumerates all fringe key intervals and every pair of interval events; and checks their exact rational probabilities against separate interval-boundary and one-separator beta-integral formulas. It also checks the two-tree squared pair probabilities and the exact finite-size expected-size formula. The delivered run passed 1,622 exact assertions. These finite checks do not replace the proof of asymptotic Poisson approximation.

## Relationship to prior work
The single-tree fringe-size profile, including the \(\sqrt n\) transition for the count at one *specified* size, is established by Feng–Mahmoud–Panholzer (2008), Fuchs (2008), Dennert–Grübel (2010), and Holmgren–Janson (2015). Holmgren and Janson's detailed survey (2016 preprint) gives the one-tree asymptotic fringe-size probability \(2/((k+1)(k+2))\). The present theorem instead requires the **same consecutive key interval** to be a fringe subtree in two independent trees, sums over a growing range of sizes, and identifies an extreme-value law. Neither the single-tree count at a fixed size nor shape-isomorphic repeated-fringe results imply the labelled-key overlap law without an additional spatial dependence analysis. No claim is made that the single-tree laws are new.

## Limitations
This is a two-tree, uniformly randomized search-tree model with a common *key order*, not a result about unlabeled tree isomorphism or correlated insertion orders. No independent audit has been performed. Search-based historical priority is necessarily qualified: equivalent results under random Cartesian-tree, treap, range-minimum or common-clade terminology could have escaped the inspected indexes, and the full text of certain older individual-profile articles was not accessible. The window total-variation proof is asymptotic; the program checks small finite instances, not all orders.

## References
1. Q. Feng, H. M. Mahmoud and A. Panholzer, *Phase Changes in Subtree Varieties in Random Recursive and Binary Search Trees*, SIAM J. Discrete Math. 22 (2008), 160–184, DOI:10.1137/060653950, https://epubs.siam.org/doi/10.1137/060653950.
2. M. Fuchs, *Subtree Sizes in Recursive Trees and Binary Search Trees: Berry–Esseen Bounds and Poisson Approximations*, Combin. Probab. Comput. 17 (2008), DOI:10.1017/S0963548308009243.
3. F. Dennert and R. Grübel, *On the Subtree Size Profile of Binary Search Trees*, Combin. Probab. Comput. 19 (2010), DOI:10.1017/S0963548309990630.
4. C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Random Recursive Trees*, arXiv:1406.6883, first public 2014-06-26, https://arxiv.org/abs/1406.6883.
5. C. Holmgren and S. Janson, *Fringe Trees, Crump–Mode–Jagers Branching Processes and m-ary Search Trees*, preprint dated 2016-01-14, https://www2.math.uu.se/~svantejs/papers/sj306.pdf, especially Section 7.2 and Theorem 7.10.
