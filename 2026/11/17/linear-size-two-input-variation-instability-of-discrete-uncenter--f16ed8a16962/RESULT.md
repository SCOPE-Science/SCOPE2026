# Linear-size two-input variation instability of discrete uncentered maximal averaging

## Finding

For every integer \(n\ge24\), let \(\mathcal M_n\) be the uncentered maximal operator over *all nonempty contiguous intervals* in \(\{1,\ldots,n\}\) with uniform counting measure and nonnegative inputs. Write
\[
V_n(h)=\sum_{i=1}^{n-1}|h_{i+1}-h_i|,\qquad
L_n=\sup_{\substack{f,g\in[0,\infty)^n\\V_n(f-g)>0}}
\frac{V_n(\mathcal M_n f-\mathcal M_n g)}{V_n(f-g)}.
\]
Then the unrestricted finite-dimensional two-input seminorm constant satisfies the quantitative bounds
\[
\boxed{2\left\lfloor\frac n{24}\right\rfloor-\frac32\le L_n\le n-1.}
\]
In particular, \(L_n\) grows linearly in \(n\), despite the familiar single-input bounded-variation contraction for the same maximal averaging operation on \(\mathbb Z\).

The construction simultaneously proves that the uncentered discrete Hardy–Littlewood maximal map on \(\mathbb Z\) is **not locally Lipschitz at zero** in the bounded-variation norm, even on its positive cone of finitely supported nonnegative functions. This is consistent with the established continuity (as opposed to local Lipschitz continuity) of the map on \(BV(\mathbb Z)\).

## Assumptions and scope

For a real vector \(f\) of length \(n\) define
\[
(\mathcal M_nf)(i)=\max_{1\le a\le i\le b\le n}\frac1{b-a+1}\sum_{j=a}^b f_j
\]
**only for nonnegative inputs**; for signed inputs the conventional Hardy–Littlewood definition uses averages of absolute values. The input perturbation \(g-f\) may have either sign, although the explicit witnesses below are nonnegative. On the integer line \(\mathbb Z\) use the analogous supremum over finite integer intervals containing the evaluation site, applied to absolute values; for nonnegative data this equals raw averaging.

For \(BV(\mathbb Z)\), use
\[
\|h\|_{BV}=|\lim_{i\to-\infty}h_i|+\sum_{i\in\mathbb Z}|h_{i+1}-h_i|.
\]
On finitely supported functions this norm equals total variation. An operator is locally Lipschitz at zero on the positive cone if some radius and some finite constant bound the output norm of differences by the input norm of differences for every two inputs in that positive cone with norm less than the radius.

The finite intervals in the definition are **not** restricted to balls around integer centers; that distinction matters for even-sized intervals. All vertex weights are one, and no end-point mass concentration is used.

## Proof

**1. Universal upper bound.** For \(h=g-f\) every interval average of \(g\) differs from its average of \(f\) by a number in \([\min h,\max h]\). Taking maxima preserves this two-sided bound: for every vertex,
\[
\min h\le(\mathcal M_ng)_i-(\mathcal M_nf)_i\le\max h.
\]
Every neighboring output difference therefore has absolute value at most
\(\max h-\min h\le V_n(h)\). Summing \(n-1\) neighboring differences gives \(L_n\le n-1\).

**2. Alternating-tail witnesses.** Fix \(q\ge1\) and put \(m=12q\), \(N=2m=24q\). On the first \(N\) vertices define
\[
f_i=\begin{cases}1,&1\le i\le m,\\3/4,&i=m+d\text{ with odd }1\le d\le m,\\0,&i=m+d\text{ with even }1\le d\le m,\end{cases}
\]
\[
h_i=\boldsymbol 1_{\{1,\ldots,m\}}(i),\qquad
\varepsilon=\frac1{100m},\qquad g=f+\varepsilon h.
\]
For any \(n\ge24q\), extend both \(f\) and \(h\) by zero after \(N\). Both \(f\) and \(g\) are nonnegative and \(V_n(g-f)=\varepsilon\).

**3. Odd tail positions are insensitive.** Consider odd \(d\ge8q+3\) with \(d\le m\), and the site \(i=m+d\). Every interval containing \(i\) either lies entirely to the right of the unit block, or touches that block. An interval in the alternating tail (possibly continuing into zero padding) has average at most \(3/4\); the singleton at \(i\) attains \(3/4\). For an interval touching the unit block, extending the left endpoint to vertex one can only increase the average, since all newly added entries equal \(1\) for \(f\), or \(1+\varepsilon\) for \(g\), and all input entries do not exceed these respective values. Thus a best such interval has the form \([1,m+t]\), for \(t\ge d\). Intervals extending into the appended zero padding have no larger average than the interval ending at \(N\).

For \(d\le t\le m\), the prefix mean for \(g\) is
\[
A_t(g)=\frac{m(1+\varepsilon)+(3/4)\lceil t/2\rceil}{m+t}.
\]
It is strictly smaller than \(3/4\) exactly when
\(m(1/4+\varepsilon)<(3/4)\lfloor t/2\rfloor\).
The left side equals \(3q+1/100\) and the right side is at least \(3q+3/4\), since \(t\ge8q+3\). The same strict inequality holds for \(f\). Hence at all these odd tail sites
\[
(\mathcal M_nf)_{m+d}=(\mathcal M_ng)_{m+d}=3/4,
\qquad D_{m+d}=0,
\]
where \(D=\mathcal M_ng-\mathcal M_nf\).

**4. Even tail positions respond by at least half the perturbation.** Let even \(d\) satisfy \(8q+3\le d\le m\). Every interval containing \(m+d\) and disjoint from the unit block contains at least one zero in an alternating zero/\(3/4\) tail; there are at most two high entries per zero entry, so its mean is at most \(1/2\). By contrast the interval \([1,m+d]\) has, for both \(f\) and \(g\), mean at least
\[
\frac{m+(3/4)\lceil d/2\rceil}{m+d}>\frac12,
\]
where the strict inequality holds because \(d\le m\). Therefore all maximizing intervals touch the unit block. Extending to vertex one again raises their averages. Thus every maximizing interval is a prefix \([1,m+t]\) with \(d\le t\le m\), and the added \(\varepsilon h\) contributes \(\varepsilon m/(m+t)\ge\varepsilon/2\) to its mean. Comparing all available prefixes gives
\[
D_{m+d}\ge\varepsilon/2.
\]
The argument applies to the padded construction because a prefix continuing beyond \(N\) only dilutes nonnegative averages.

**5. Total-variation amplification.** The \(4q-2\) consecutive tail vertices with indices \(d=8q+3,\ldots,12q\) alternate between odd and even indices. There are exactly \(4q-3\) edges between them. Along every one of these edges, the neighboring values of \(D\) are zero and at least \(\varepsilon/2\). Hence
\[
V_n(\mathcal M_ng-\mathcal M_nf)\ge (4q-3)\varepsilon/2.
\]
Since \(V_n(g-f)=\varepsilon\), we obtain \(L_n\ge 2q-3/2\). For each \(n\ge24\) choose \(q=\lfloor n/24\rfloor\); combining this with Step 1 proves the finite theorem. The lower constant is not asserted to be the exact \(L_n\) at each dimension.

**6. Failure of local Lipschitz continuity on \(BV(\mathbb Z)\).** Extend the same \(f,g\) by zero *on both sides* of \(\{1,\ldots,24q\}\). Any interval containing one of the tested tail vertices and leaving this range only adds zeros, so Steps 3–5 hold verbatim for the discrete uncentered maximal operator \(\mathcal M\) on \(\mathbb Z\). However, the infinite-line input difference \(g-f=\varepsilon h\) now has **two** jumps, hence \(\|g-f\|_{BV}=2\varepsilon\). Therefore
\[
\frac{\|\mathcal Mg-\mathcal Mf\|_{BV}}{\|g-f\|_{BV}}
\ge\frac{4q-3}{4}\longrightarrow\infty.
\]
Both maximal functions tend to zero at negative infinity, and their total variations are finite by the known one-input variation theorem; therefore the ratio uses genuine \(BV\) norms. Finally, for any \(t>0\), positive homogeneity gives \(\mathcal M(tf)=t\mathcal Mf\) and \(\mathcal M(tg)=t\mathcal Mg\). Scaling the constructed input pairs into arbitrarily small \(BV\)-balls about zero preserves these unbounded ratios, contradicting every proposed local Lipschitz constant.

## Verification

The self-contained exact-rational checker `verification/check_bv_instability.py` evaluates every interval in the finite witnesses for \(q=1,\ldots,5\), verifies each asserted high/low response, and checks the total-variation lower bound. It also checks the algebraic inequalities underlying the construction for many larger values of \(q\). Run `python verification/check_bv_instability.py` after extracting the package. The argument for all dimensions and the infinite integer line is the complete analytic proof above; the finite checker is supplementary and is not an infinite proof.

## Relationship to prior work

Bober, Carneiro, Hughes and Pierce proved in 2010 that the uncentered discrete maximal operator decreases **each input's own total variation**, a statement involving \(V(\mathcal Mf)\le V(f)\), not the variation of \(\mathcal Mf-\mathcal Mg\). Carneiro, Madrid and Pierce subsequently established continuity of the discrete maximal operator on \(BV(\mathbb Z)\); continuity does not imply local Lipschitz continuity, so there is no contradiction. Aldaz, Colzani and Pérez Lázaro proved sharp **one-input pointwise Lipschitz** bounds for uncentered maximal functions, using another seminorm. A published finite-path result on *endpoint-mass concentration and sharp Lipschitz amplification* concerns vertex-mass imbalance and the **maximum adjacent slope of one input**, which is logically distinct from the present uniform-weight **two-input sum of all adjacent slopes**. Results for running extrema and finite-graph medians likewise concern different nonlinear maps.

## Limitations

The quantitative finite-path constants are proved between explicit nonmatching bounds, rather than determined exactly. The proof uses all contiguous intervals, counting measure and the nonnegative input cone; it does not supply an exact two-input constant for each finite dimension, arbitrary vertex measures, centered interval families or other graphs. Infinite-line non-Lipschitzness is proved at zero and hence under positive rescaling, not at every positive input. Historical priority for the exact explicit counterexample is qualified because unindexed treatments of nonlinear \(BV\) stability may exist.

## References

1. J. Bober, E. Carneiro, K. Hughes and L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030v1, publicly submitted 2010-05-17, https://arxiv.org/abs/1005.3030 .
2. J. M. Aldaz, L. Colzani and J. Pérez Lázaro, *Optimal bounds on the modulus of continuity of the uncentered Hardy-Littlewood maximal function*, arXiv:1009.1359v1, publicly submitted 2010-09-07, https://arxiv.org/abs/1009.1359 .
3. E. Carneiro, J. Madrid and L. B. Pierce, *Endpoint Sobolev and BV continuity for maximal operators*, arXiv:1708.06051v1, publicly submitted 2017-08-21, https://arxiv.org/abs/1708.06051 .
4. *Endpoint-mass concentration and sharp Lipschitz amplification of discrete interval maximal averages*, published mathematical record, 2026-11-02, public full-text record at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-endpoint-mass-concentration-and-sharp-lipschitz-amplification-of--e07aeee621fe .
