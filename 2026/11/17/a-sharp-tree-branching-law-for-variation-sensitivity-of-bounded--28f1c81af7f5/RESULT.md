# The sharp fixed-order variation-amplification envelope for bounded-slope least squares on trees

## Finding

Let \(T=(V,E)\) be any finite simple unweighted tree of order \(n\ge2\), and fix a common positive edge-slope bound \(R>0\). For real vertex data \(x\), let \(P_{T,R}x\) be the unique Euclidean least-squares fit satisfying \(|z_u-z_v|\le R\) on every edge. Set
\[
\operatorname{TV}_T(x)=\sum_{uv\in E}|x_u-x_v|,
\qquad
L(T)=\sup_{\operatorname{TV}_T(x-y)>0}
\frac{\operatorname{TV}_T(P_{T,R}x-P_{T,R}y)}{\operatorname{TV}_T(x-y)}.
\]
The **sharp envelope at fixed tree order** is
\[
\boxed{\mathcal M_n:=\max_{|V(T)|=n}L(T)
 =\max\left\{1,\max_{2\le s\le n-1}\frac{(s-1)(n-s)}s\right\}.}
\tag{1}
\]
The second maximum is omitted when its range is empty. Every nonbaseline candidate in (1) is realized by a tree consisting of an \(s\)-vertex path with all \(n-s\) extra leaves attached to one endpoint. The amplification is attained **exactly** by a pair of distinct finite input signals, not only as a directional derivative or a limit.

In particular, \(\mathcal M_2=\mathcal M_3=\mathcal M_4=1\), while \(\mathcal M_5=3/2\). For every \(n\ge5\), an optimal spine length is the smallest integer \(s\ge2\) satisfying \(s(s+1)\ge n\) (restricted to \(s\le n-1\)); adjacent lengths may tie when \(n=s(s+1)\). Hence
\[
\boxed{\mathcal M_n=n+1-2\sqrt n+O(n^{-1/2})\quad(n\to\infty).}
\tag{2}
\]
The leading amplification thus grows almost linearly with \(n\), and an optimal construction balances a path of order about \(\sqrt n\) with a pendant-leaf branch of order about \(n-\sqrt n\).

**Prior-work boundary.** The connected-subtree boundary-cut formula for the graph-variation norm of connected-block averages, and its path/star consequences, are already established for Euclidean *isotonic* projection on arbitrary orientations of a tree in the published finding *Exact tree-variation sensitivity of isotonic projection and unbounded cubic-branch amplification* (2026-11-17). This document does **not** claim that formula, the path/claw stability classification, or the star constant as new. Those facts are used as background after identifying the same averaging-derivative family for the different symmetric bounded-slope projection. The additional finding here is the **global extremization over all trees of a prescribed order**: its exact \(n\)-dependent coefficient, attained broom witnesses, integer optimizer, and sharp asymptotic law. No generalization to weighted graphs or graphs with cycles is asserted.

## Assumptions and normalization

All trees are finite, simple, connected, and unweighted. The least-squares objective is \(\sum_v(z_v-x_v)^2\), with equal vertex masses. Each unoriented edge imposes both inequalities \(-R\le z_u-z_v\le R\) with the same \(R>0\), and each edge contributes unit weight to \(\operatorname{TV}_T\). The coefficient is a **two-input difference** modulus on signals modulo constants, not the one-input inequality \(\operatorname{TV}_T(Px)\le\operatorname{TV}_T(x)\). Constants are respected because \(P(x+t\mathbf1)=P(x)+t\mathbf1\). The value of \(L(T)\) is independent of positive \(R\) by scaling the input and fitted signal by \(R\).

## Proof

**1. Why connected-block averaging governs these fits.** An active edge is one where the fitted edge difference is exactly \(+R\) or \(-R\). On an ordinary full-dimensional active-set cell, let \(F\subseteq E\) be the active forest. Differentiating the constrained least-squares optimum under the fixed active affine equalities gives the orthogonal projector \(Q_F\) onto the subspace of vectors constant on every connected component of \((V,F)\). This is componentwise arithmetic averaging; its derivative does not depend on the signs of the saturated differences.

Every forest \(F\) is genuinely realized on a nonempty open cell. Fix a root orientation and choose a feasible fitted signal \(z\) with oriented edge differences \(\pm R\) on \(F\) and \(0\) on edges outside \(F\); such a choice is consistent because the graph is a tree. Let \(d_e\) be the outward active inequality normal and set \(x=z+\sum_{e\in F}\lambda_e d_e\) with all \(\lambda_e>0\). Strict KKT multipliers, strict slackness on inactive edges, and independence of the active incidence rows yield a full-dimensional neighborhood where the same face remains active. The projection is continuous and piecewise affine with finitely many such cells; integrating derivatives along input segments and using finite-pair perturbations within a maximizing open cell therefore establishes
\[
L(T)=\max_{F\subseteq E}\|Q_F\|_{\operatorname{TV}_T\to\operatorname{TV}_T}.
\tag{3}
\]
This step identifies the derivative family for the bounded-slope estimator, rather than claiming the resulting connected-average variation norm as previously unknown.

**2. Known cut-boundary expression and its interpretation.** Edge-cut indicators \(h_e\) for the components of \(T\setminus\{e\}\) form, modulo constants, the \(\ell^1\) edge-gradient basis: \(\operatorname{TV}_T(h_e)=1\), and every signal is a signed sum of these indicators plus a constant. Thus the variation operator norm of \(Q_F\) is the maximum \(\operatorname{TV}_T(Q_Fh_e)\). If the cut edge \(e\notin F\), the gain is \(1\). Otherwise, \(e\) belongs to the active connected component \(S\), and its deletion splits \(S=A\sqcup B\) with \(a=|A|,b=|B|\). Write \(b_A\) and \(b_B\) for the numbers of edges leaving these respective parts for \(V\setminus S\). Since averaging makes \(h_e\) constant on \(S\), the output jumps occur only across the boundary of \(S\), with magnitudes \(b/(a+b)\) and \(a/(a+b)\), respectively. Consequently
\[
\operatorname{TV}_T(Q_Fh_e)=\frac{b\,b_A+a\,b_B}{a+b},
\qquad
L(T)=\max\left\{1,\max_{S,e}\frac{b\,b_A+a\,b_B}{a+b}\right\}.
\tag{4}
\]
This is the same connected-subtree expression already proved for isotonic projection in the published 2026 tree-variation result cited below. Equation (3) shows why the expression also applies to the present symmetric bounded-slope fit, despite the different feasible set.

**3. Sharp bound over all \(n\)-vertex trees.** Fix any connected \(S\) of size \(s=a+b\ge2\), with an internal cut edge. Each component of \(T\setminus S\) attaches by exactly one edge to \(S\), because \(T\) is a tree. Hence \(b_A+b_B\le n-s\), while \(a,b\le s-1\). Applying these two elementary but sharp constraints to (4) gives
\[
\frac{b\,b_A+a\,b_B}{s}
\le\frac{s-1}{s}(b_A+b_B)
\le\frac{(s-1)(n-s)}s.
\tag{5}
\]
If \(s=n\) the right side is zero, so only \(2\le s\le n-1\) can contribute above the baseline \(1\). This proves the upper bound in (1) simultaneously for every tree of order \(n\).

For the matching lower bound, take a path \(S=(v_0,v_1,\ldots,v_{s-1})\) and attach \(n-s\) new leaves at \(v_0\). Choose the active forest \(F=E(S)\) and the cut edge \(e=v_0v_1\). One side of \(S\setminus\{e\}\) has one vertex and all \(n-s\) boundary edges; the other side has \(s-1\) vertices and no boundary edges. Formula (4) gives exactly \((s-1)(n-s)/s\). By step 1, this norming direction is achieved between two sufficiently close distinct data vectors inside the corresponding strict active-set cell. When \(1\) is the maximum, an inactive cell makes the fit the identity on nearby inputs, attaining the baseline. Thus **every term in (1), including the overall optimum, is attained by finite inputs on an explicit tree**.

**4. Integer optimizer and asymptotic.** For fixed \(n\), put \(f_n(s)=(s-1)(n-s)/s=n+1-s-n/s\). Its discrete difference is
\[
f_n(s+1)-f_n(s)=\frac{n}{s(s+1)}-1.
\]
Therefore it increases up to the first integer \(s\) with \(s(s+1)\ge n\), then decreases, with a tie exactly when equality holds. For \(n\ge5\) the maximizing value exceeds \(1\), except the tie at the smallest cases where the formula still applies. Finally the continuous function \(n+1-s-n/s\) has its maximum at \(s=\sqrt n\), equal to \(n+1-2\sqrt n\). Choosing a nearest admissible integer \(s\) changes this maximum by \(O(n^{-1/2})\), by Taylor's theorem or the exact identity
\[
\bigl(n+1-2\sqrt n\bigr)-f_n(s)=\frac{(s-\sqrt n)^2}{s}.
\]
This proves (2) with its correct additive constant and completes the sharp fixed-order classification.

## Reproducibility and scope of verification

An independent exact-arithmetic check of the envelope formula and integer optimizer for the first several tree orders corroborates the sharp finite values \(\mathcal M_4=1,\mathcal M_5=3/2,\mathcal M_6=2,\mathcal M_9=4,\mathcal M_{16}=9\). The package's unchanged `verify.py` additionally reconstructs block averaging and cut-boundary gains for every labeled tree through six vertices using exact rational arithmetic, and gives explicit strict-KKT finite-pair witnesses for broom trees. These are finite diagnostics, not the argument for every \(n\). The universal result is proved in steps 1–4, including the separate upper bound and matching construction. The new statement concerns only order-wise extremization for symmetric uniform edge caps; it does not assert a new universal connected-subtree formula or the complete class of all maximizing tree shapes.

## Relation to prior work and limitations

The published 2026 result *Exact tree-variation sensitivity of isotonic projection and unbounded cubic-branch amplification* establishes the connected-subtree graph-variation norm of connected-block averaging derivatives on trees, independent of isotonic edge orientations. In particular it already includes the star law, the path case, and arbitrarily large variation gain on maximum-degree-three caterpillars. Those are **credited** here, not new results. Although its tree-by-tree formula supplies the starting point for the bound (5), that source does not state the extremum over all \(n\)-vertex tree shapes, its attaining broom shape for every \(n\), or the sharp \(n+1-2\sqrt n\) growth law. The derivation here supplies the needed additional extremal argument and explicit witnesses.

Yeganova and Wilbur (2009) study monotone Lipschitz-isotonic regression, and Agarwal, Phillips and Sadri (2009) provide Lipschitz-isotonic and unimodal regression algorithms on paths and trees. Kyng, Rao, Sachdeva and Spielman (2015) treat fixed-label Lipschitz extension rather than nearest-point fitting of full vertex data. These results give context but not an explicit fixed-order graph-TV envelope for this symmetric bounded-slope fit.

The endpoint \(R=0\), weighted observations or edges, nonuniform edge caps, arbitrary graphs with cycles, and complete characterization of **every** maximizing tree are outside scope. The order-wise extremal calculation is short once the known connected-block formula is in place; its claim to originality is specifically that natural sharp envelope and matching construction, not an independent invention of the formula. Unindexed earlier derivations of the same envelope remain a historical-priority risk; no external certification is claimed.

## References

1. *Exact tree-variation sensitivity of isotonic projection and unbounded cubic-branch amplification*, publicly recorded 2026-11-17, full mathematical statement and proof: https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-exact-tree-variation-sensitivity-of-isotonic-projection-and-unbo--8a180bae4c2f/RESULT.md.
2. P. K. Agarwal, J. M. Phillips and B. Sadri, *Lipschitz Unimodal and Isotonic Regression on Paths and Trees*, arXiv:0912.5182 (2009), https://arxiv.org/abs/0912.5182.
3. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, J. Optim. Theory Appl. 141 (2009), 429–443, https://doi.org/10.1007/s10957-008-9477-0.
4. R. Kyng, A. Rao, S. Sachdeva and D. A. Spielman, *Algorithms for Lipschitz Learning on Graphs*, arXiv:1505.00290 (2015), https://arxiv.org/abs/1505.00290.
