# A sharp uniform Gini-decay envelope for normalized heat on complete bipartite graphs

## Finding
Let \(p,q\ge1\) be integers, \(K_{p,q}\) the complete bipartite graph, and \(H_t=\exp[t(D^{-1}A-I)]\), acting on real vertex functions. Write \(G(f)=\sum_{i<j}|f_i-f_j|\), where the sum is over **all** unordered vertex pairs, not merely graph edges. For \(r\in\{0,\ldots,p\}\), \(s\in\{0,\ldots,q\}\), and \(0<r+s<p+q\), put
\[
 d_{r,s}=\frac rp-\frac sq,\qquad
 C_{p,q}(r,s)=\frac{-pq d_{r,s}^{2}+[rs+(p-r)(q-s)]|d_{r,s}|}{(r+s)(p+q-r-s)},
\]
and \(C_{p,q}=\max C_{p,q}(r,s)\) over these finitely many integer pairs. Then for every real \(t\ge0\), the **exact attained** Gini operator seminorm is
\[
 \boxed{\ \|H_t\|_{G\to G}=e^{-t}\bigl[1+(1-e^{-t})C_{p,q}\bigr].\ }
\]
The formula is computable by at most \((p+1)(q+1)-2\) rational cut comparisons, independently of time. Every maximizing cut gives a binary norming function for **all finite times** \(t>0\), including in cases where many cuts tie.

For every finite \(p,q\), one has \(C_{p,q}<1\), and hence **strict Gini contraction at every positive time**. Across all finite complete bipartite graphs, however, the exact pointwise sharp envelope is
\[
 \boxed{\ \sup_{p,q\ge1}\|H_t\|_{G\to G}=e^{-t}(2-e^{-t})\qquad(t\ge0).\ }
\]
For \(t>0\) this supremum is not attained at any finite \(p,q\). It is approached, for example, by \(p=k\), \(q=k^2\) as \(k\to\infty\), using a singleton cut in the smaller vertex class. In particular, the envelope retains the leading long-time coefficient \(2\), despite strict contraction in every finite graph.

## Assumptions and scope
The graph is finite, unweighted, nonempty on both sides, with no vertex loops. The averaging generator acts by
\[
 (Qf)(i)=\frac1q\sum_{j\in B}f(j)-f(i)\quad(i\in A),\qquad
 (Qf)(j)=\frac1p\sum_{i\in A}f(i)-f(j)\quad(j\in B).
\]
The seminorm \(G\) vanishes precisely on constant functions; the operator norm is the supremum of \(G(H_tf)/G(f)\) over nonconstant real signals. The time variable is any finite nonnegative real number. The formula includes the two-vertex graph \(K_{1,1}\), where \(C_{1,1}=-1\) and the norm is \(e^{-2t}\). All cut counts \(r,s\) are integers in the stated range. The all-graph envelope is a supremum over two **integer** class sizes; no infinite graph is asserted to attain it.

## Proof
**1. Spectral evolution.** Let \(a=e^{-t}\), let \(u\) and \(v\) denote the means of the input over the two vertex classes, and write \(z=(u+v)/2\). The within-class mean-zero subspaces decay by \(a\), while the interclass mean difference decays by \(a^2\). Therefore, for each input \(f\),
\[
 (H_tf)(i)=z+\frac{a^2}{2}(u-v)+a(f_i-u)\quad(i\in A),
\]
\[
 (H_tf)(j)=z-\frac{a^2}{2}(u-v)+a(f_j-v)\quad(j\in B).
\]
These expressions solve the displayed generator equations with the correct initial values. In particular, \(H_t\mathbf1=\mathbf1\).

**2. Exact binary-cut computation.** Let \(f\) be the indicator of a vertex set containing \(r\) vertices of \(A\) and \(s\) of \(B\). Set \(d=r/p-s/q\) and \(c=1-a\). Each within-class crossing contributes \(a\). Across the classes, the pairs labelled \((1,0)\), \((0,1)\), and equally labelled contribute respectively \(a(1-cd)\), \(a(1+cd)\), and \(ac|d|\). The first two expressions are nonnegative because \(|d|\le1\) and \(0\le c\le1\). The corresponding multiplicities are \(r(q-s)\), \((p-r)s\), and \(rs+(p-r)(q-s)\). Collecting these terms, and using \((p-r)s-r(q-s)=-pq d\), gives
\[
 G(H_tf)=a\left[G(f)+c\bigl(-pq d^2+[rs+(p-r)(q-s)]|d|\bigr)\right].
\]
Since \(G(f)=(r+s)(p+q-r-s)\), every cut has the ratio \(a[1+c C_{p,q}(r,s)]\).

**3. Reduction from arbitrary real functions.** Subtract the minimum coordinate of an arbitrary nonconstant real input and list its increasing distinct levels. The signal is a positive linear combination of nested superlevel-set indicators, plus a constant. For every unordered pair, the scalar layer-cake identity gives exactly \(G(f)=\sum_\ell\lambda_\ell G(\mathbf1_{S_\ell})\) with \(\lambda_\ell>0\). Linearity, constant preservation, and the triangle inequality imply
\[
 G(H_tf)\le\sum_\ell\lambda_\ell G(H_t\mathbf1_{S_\ell})
 \le a(1+c C_{p,q})G(f).
\]
A maximizing nonconstant cut attains equality. This proves the operator norm formula for every real input and every finite time, without extrapolating from cut enumeration.

**4. Strict finite-size contraction.** Suppose \(d>0\). Then \(r>0\), \(s<q\), and the correction numerator from step 2 equals
\[
 E=(qr-ps)\left[1-2\frac rp\left(1-\frac sq\right)\right].
\]
If \(E\le0\), then \(E<G(f)\). Otherwise its bracket lies strictly below one and \(qr-ps\le r(q-s)\le G(f)\). Thus again \(E<G(f)\). If \(d<0\), interchange the two classes; if \(d=0\), then \(E=0<G(f)\). There are finitely many nonconstant cuts, so \(C_{p,q}<1\). For finite \(t>0\), \(0<a<1\), and hence
\[
 \|H_t\|_{G\to G}<a(2-a)<1.
\]

**5. Sharpness of the size-uniform envelope.** For a singleton cut in \(A\), \(r=1\), \(s=0\), direct substitution yields
\[
 C_{p,q}(1,0)=\frac{q(p-2)}{p(p+q-1)}.
\]
Take \(p=k\), \(q=k^2\). This equals \(k(k-2)/(k^2+k-1)\), which tends to one from below. Thus for every fixed \(t\ge0\), this cut's ratio converges to \(a(2-a)\); the upper bound from step 4 proves it is the exact all-size supremum. At \(t>0\) strict finite-size inequality prevents attainment. At \(t=0\), the norm is one on every graph. The stated leading long-time envelope coefficient follows immediately.

## Verification
The included standalone `verify.py` uses exact rational arithmetic for \(a\in\{1/4,1/2,3/4,1\}\); it compares the finite cut formula against independently constructed semigroup values on every cut-count orbit for \(1\le p,q\le10\), checks signed real inputs, and tests the finite-size bound and the explicit size-unbalanced lower witnesses. The code passes as packaged. These are finite diagnostics of the identities; the unlimited integer-size and continuous-time assertions follow from the proof.

## Relationship to prior work
Gaubert and Qu (2013 arXiv first submission) characterize the Doeblin–Dobrushin contraction coefficient for the **oscillation seminorm** of Markov operators, equivalently the dual total variation norm on probability measures. Their full-text introduction and main semigroup framework do not identify the unweighted **sum of all pairwise absolute vertex-value differences**, which is not the same norm or its dual. The previously published exact Wasserstein-one amplification theorem for bipartite Markov semigroups uses the graph-distance transport seminorm on probability measures and can exhibit transient amplification at asymmetric rates; its statement does not imply this strictly contracting complete-pair Gini formula. A published weighted edge-variation criterion on \(K_{2,q}\) studies independently weighted graph-edge differences and only an all-time contraction decision, not the present complete-pair norm or sharp time profile. Earlier explicit complete-bipartite heat results for unnormalized edge variation differ in both generator and seminorm. Thus the coarea reduction is classical, but the exact \(C_{p,q}\) cut formula and sharp universal envelope are separate claims. This comparison is best-knowledge only, not proof of historical priority.

## Limitations
The exact fixed-size coefficient is a finite two-integer maximization; no closed singleton-extremizer classification is asserted. The result concerns the degree-normalized Markov generator with equal unit total exit rate in both classes, unweighted complete-pair Gini variation, real signals, and finite complete bipartite graphs. It does not imply analogous contractions for arbitrary graph weights, nonuniform vertex masses, independently chosen exit rates, or other variation metrics. Historical priority may be affected by unindexed exact seminorm calculations.

## References
1. S. Gaubert and Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649, first public submission 2013-07-17, Sections 1–2 and 5; https://arxiv.org/abs/1307.4649; full-text rendering https://ar5iv.labs.arxiv.org/html/1307.4649.
2. *Exact transport amplification for asymmetric bipartite Markov semigroups*, publicly indexed research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-transport-amplification-for-asymmetric-bipartite-markov-se--4fd69f17c057.
3. *A sorted-cut criterion for weighted-variation contraction of normalized heat on* \(K_{2,q}\), publicly indexed research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sorted-cut-criterion-for-weighted-variation-contraction-of-nor--cfbda9d03a0c.
