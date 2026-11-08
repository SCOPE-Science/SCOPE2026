# Every positive compact continuum occurs as a root-cluster set of finite sums of weighted shifts

## Finding

Fix a positive integer \(d\). On \(H=\bigoplus_{i=1}^{d}\ell^2(\mathbb N)\), let \(T=\bigoplus_{i=1}^{d}S_i\), where each unilateral weighted forward shift has weights \(w_{i,k}\) satisfying \(0<m\le w_{i,k}\le M<\infty\) for all \(i,k\). Write \(A_n=|T^n|^{1/n}\) and let \(\mathfrak C(T)\) be its set of weak-operator subsequential limits. Then there is a unique nonempty compact connected set \(C\subset(0,\infty)^d\) such that

\[
\mathfrak C(T)=\left\{\bigoplus_{i=1}^{d}s_i I_{\ell^2}: (s_1,\ldots,s_d)\in C\right\}.
\]

Conversely, **every** nonempty compact connected \(C\subset(0,\infty)^d\) is obtained from bounded-below, bounded, positive-weight shifts \(S_i\) in this way. The associated asymptotic numerical range, using the definition of Ji and Yang, is exactly

\[
W_a(T)=\left[\min_{s\in C}\min_{1\le i\le d}s_i,\ \max_{s\in C}\max_{1\le i\le d}s_i\right].
\]

In one summand the only possible cluster sets are positive closed intervals or singletons. Two summands already realize nonconvex Jordan curves, as well as every other nonempty compact connected subset of the positive quadrant.

## Assumptions and scope

All Hilbert spaces and weighted shifts are complex; weights are positive real numbers and have common finite upper and strictly positive lower bounds. The integer \(d\) is fixed and finite. The root \(|T^n|^{1/n}\) means the positive functional-calculus root of \((T^{*n}T^n)^{1/2}\), not an operator root of \(T\). Cluster limits are taken along sequences of integers tending to infinity, in the weak operator topology (WOT); in the asserted realization they are also strong-operator limits (SOT). A continuum means a nonempty compact connected set, without any local connectedness assumption.

## Proof

**Step 1: reduction to vector Cesàro means.** Write \(b_{i,k}=\log w_{i,k}\), and let \(B=\sup_{i,k}|b_{i,k}|<\infty\). Set \(c_{i,n}=n^{-1}\sum_{j=1}^{n}b_{i,j}\) and \(c_n=(c_{1,n},\ldots,c_{d,n})\). For the standard basis vector \(e_k\) in the \(i\)-th summand, the positive diagonal operator \(A_n\) has eigenvalue

\[
\exp\!\left(\frac1n\sum_{j=k}^{k+n-1}b_{i,j}\right).
\]

For fixed \(k\), the exponent differs from \(c_{i,n}\) by at most \(2B(k-1)/n\): the difference of the two sums consists of the last \(k-1\) entries minus the first \(k-1\) entries, divided by \(n\). All eigenvalues of \(A_n\) lie in \([e^{-B},e^B]\). Therefore whenever \(c_{n_j}\to v\), dominated convergence on the coordinate basis gives

\[
A_{n_j}\xrightarrow{\mathrm{SOT}}\bigoplus_{i=1}^{d}e^{v_i}I.
\]

Conversely, if \(A_{n_j}\) converges in WOT, its first diagonal coefficient in each summand is \(e^{c_{i,n_j}}\). These converge, and their logarithms converge because they lie in a compact positive interval. Hence \(c_{n_j}\to v\) and the WOT limit is the displayed block-scalar operator. Thus \(\mathfrak C(T)\) is exactly the coordinate-exponential image of the accumulation set of \((c_n)\).

**Step 2: necessity of a continuum.** The sequence \((c_n)\) is bounded, and

\[
\|c_{n+1}-c_n\|_\infty\le\frac{2B}{n+1}.
\]

The cluster set of a bounded sequence in a finite-dimensional Euclidean space whose consecutive distances tend to zero is nonempty, compact and connected. For completeness: if the cluster set split into two disjoint nonempty compact pieces at positive distance \(\delta\), all sufficiently late terms would lie within \(\delta/4\) of the union and all late successive jumps would be less than \(\delta/4\). The sequence could then not visit neighborhoods of both pieces infinitely often, a contradiction. Coordinatewise exponentiation preserves compactness and connectedness and maps bounded subsets into the positive orthant. This proves necessity and uniqueness of \(C\).

**Step 3: a Lipschitz curve with any prescribed continuum as omega-limit.** Let \(K\subset\mathbb R^d\) be nonempty, compact and connected, and fix \(v_0\in K\). For every integer \(m\ge1\), take a finite \(1/m\)-net \(F_m\subset K\). Connectedness implies that any two points of \(K\) can be joined by a finite chain in \(K\) whose successive distances are at most \(1/m\): the set reachable by such chains is both relatively open and relatively closed. Construct a polygonal route from \(v_0\) through all members of \(F_m\) and back to \(v_0\), using such chains. Every segment lies within distance \(1/m\) of \(K\). Parametrize this route with speed at most one, followed by a stationary interval of length one at \(v_0\). Concatenating these stages gives a bounded globally \(1\)-Lipschitz curve \(\gamma:[0,\infty)\to\mathbb R^d\); stage times tend to infinity. The distance from the tail of \(\gamma\) to \(K\) tends to zero, while every point of \(K\) is approached at arbitrarily late visits to its shrinking finite nets. Therefore its omega-limit set is exactly \(K\).

**Step 4: exact inverse Cesàro construction.** Given a desired \(C\subset(0,\infty)^d\), put \(K=\{(\log s_1,\ldots,\log s_d):s\in C\}\), and choose \(\gamma\) as in Step 3. Define \(c_n=\gamma(\log n)\) for integers \(n\ge1\), then define the vector sequence

\[
b_1=c_1,\qquad b_n=nc_n-(n-1)c_{n-1}\quad(n\ge2).
\]

Telescoping gives \(n^{-1}\sum_{j=1}^{n}b_j=c_n\) exactly. If \(R=\sup_{t\ge0}\|\gamma(t)\|_\infty\), the Lipschitz condition yields, for \(n\ge2\),

\[
\|b_n\|_\infty\le R+(n-1)\log\frac{n}{n-1}\le R+1.
\]

Consequently \(w_{i,n}=e^{b_{i,n}}\) are uniformly bounded above and away from zero. Since \(\log(n+1)-\log n\to0\) and \(\gamma\) is Lipschitz, the accumulation points of the sampled sequence \(\gamma(\log n)\) are precisely the omega-limit points of \(\gamma\), namely \(K\). Step 1 now gives exactly the desired \(\mathfrak C(T)\). No approximation of \(C\) is involved in the theorem: the realized cluster set equals \(C\).

**Step 5: the asymptotic numerical range.** A unit vector \(x=(x_1,\ldots,x_d)\in H\) determines weights \(p_i=\|x_i\|^2\ge0\) with \(\sum_i p_i=1\). Along a subsequence with block-scalar limit associated to \(s\in C\), the scalar expectation tends to \(\sum_i p_i s_i\). Conversely every point of this form is obtained by choosing \(x\) with prescribed squared component norms. Thus

\[
W_a(T)=\left\{\sum_{i=1}^d p_i s_i : s\in C,\ p_i\ge0,\ \sum_i p_i=1\right\}.
\]

This is a compact interval, because it is the continuous image of the compact connected set \(C\times\Delta_{d-1}\). Its two endpoints are the minimum and maximum coordinate values over \(C\), proving the formula. For \(d=1\), nonempty compact connected subsets of \((0,\infty)\) are exactly positive closed intervals and singletons. For \(d=2\), choosing \(\gamma(t)=(\cos t,\sin t)\) yields the explicit nonconvex WOT cluster curve \(\{(e^{\cos t},e^{\sin t}):0\le t\le2\pi\}\), which is a simple closed curve. All assertions follow.

## Verification

A standalone Python diagnostic, `check_continua.py`, tests the exact telescoping identity with rational input data, the predicted boundedness for a periodic Lipschitz curve, the shifted-average estimate, and finite-section diagonal-root formulas. Its finite numerical checks illustrate but do not establish the infinite-dimensional or arbitrary-continuum statement. The complete proof above supplies those arguments; no unproved spectral or topological classification theorem is assumed.

## Relationship to prior work

Ji and Yang's 2026 paper introduces \(\mathfrak C(T)\), shows its WOT connectedness when \(T\) is bounded below (Corollary 2.13 and Proposition 2.14), and identifies a scalar interval of limits for a **single** bounded-below unilateral weighted shift (Proposition 4.1). It also constructs a disconnected example without a lower weight bound (Example 4.3). The necessity and one-summand portions here agree with those results. The added statement is a converse realization classification: with only finitely many bounded-below shift summands, **every** positive compact continuum of simultaneous limiting scales is possible. The source's scalar statement gives the possible coordinates separately but does not establish the correlations or converse realization. Nayak and Shekhawat (2024), Proposition 5.2, instead characterize **norm convergence** of positive roots of powers of one unilateral weighted shift through uniform convergence of window geometric means. This does not characterize nonconvergent WOT cluster sets for several summands, and its criterion neither implies nor rules out the present realization. Classical summability literature on connectedness of transformed sequence limit sets is related to Step 2 and may contain broader vector sequence realization principles; the operator-level conclusion and its numerical-range formula are explicit here.

## Limitations

The theorem concerns finite orthogonal sums of bounded-below unilateral weighted shifts. It does not classify WOT cluster sets for arbitrary operators or infinite orthogonal sums. The construction can have very large but finite weight bounds depending on \(C\). It does not assert that every compact connected family of arbitrary positive operators is realizable. The formula for \(W_a(T)\) loses the nonconvex geometry of \(C\). Publication priority remains subject to comparison with classical vector summability realization results, including older articles not available in full text during the literature review.

## References

1. Y. Ji and B. Yang, *Asymptotic Numerical Ranges and Invariant Subspaces of Operators*, arXiv:2608.21553, first submitted 2026-08-21, especially Corollary 2.13, Proposition 2.14, Proposition 4.1, and Examples 4.2–4.3. https://arxiv.org/html/2608.21553
2. H. G. Barone, *Limit points of sequences and their transforms by methods of summability*, Duke Mathematical Journal **5** (1939), 740–752. https://doi.org/10.1215/S0012-7094-39-00560-0
3. D. Leviatan and L. Lorch, *On the connectedness of the sets of limit points of certain transforms of bounded sequences*, Canadian Mathematical Bulletin **14** (1971), 175–181. https://doi.org/10.4153/CMB-1971-032-0
4. S. Nayak and S. Shekhawat, *On the convergence of the normalized power sequence of spectral operators on Hilbert space*, arXiv:2410.16318, first submitted 2024-10-14, especially Section 5, Proposition 5.2. https://arxiv.org/html/2410.16318
5. A. L. Shields, *Weighted shift operators and analytic function theory*, in *Topics in Operator Theory*, AMS, 1974, pp. 49–128.
