# Sharp Lipschitz spread and a quadratic clique–tail transition on lollipop graphs

## Finding

Let \(L_{m,\ell}\) be the unit-edge graph obtained from a clique of order \(m\ge3\) by attaching a path of \(\ell\ge3\) new edges at one distinguished clique vertex. Equip its \(N=m+\ell\) vertices with the uniform probability measure. The sharp real Lipschitz variance (spread)
\[
\operatorname{spr}(L_{m,\ell})=\max_{\lvert f(u)-f(v)\rvert\le1\,\,(uv\in E)}\left[\frac1N\sum_v f(v)^2-\left(\frac1N\sum_v f(v)\right)^2\right]
\]
has the following exact value. Define
\[
A=\frac{\ell(\ell+1)}2,\qquad B=\frac{\ell(\ell+1)(2\ell+1)}6,\qquad T=\ell(\ell+2).
\]
Then
\[
\boxed{\operatorname{spr}(L_{m,\ell})=
\begin{cases}
\displaystyle\frac{N(B+m-1)-(A-m+1)^2}{N^2},&m\le T+2,\\[6pt]
\displaystyle\frac14+\frac{\ell(\ell+1)(\ell+2)}{3N}-\frac{\mathbf1_{\{N\text{ odd}\}}}{4N^2},&m\ge T+3.
\end{cases}}
\]
There is no gap at the boundary. The transition has a sharp optimizer interpretation: the configuration with **all** nondistinguished clique vertices one unit below the attachment vertex is uniquely optimal up to graph symmetries, translation, and sign when \(m\le T+2\); it first coexists with a distinct clique occupancy when \(m=T+3\), and becomes strictly suboptimal for \(m\ge T+4\). Thus the first nontrivial optimizer coexistence occurs exactly at the quadratic threshold \(m=\ell(\ell+2)+3\).

Every maximizer, up to an additive constant and an overall sign, has the following form. Number the path vertices from the attachment vertex by \(j=0,1,\ldots,\ell\); assign them \(f(j)=j\). Assign \(-1\) to exactly \(k\) of the other \(m-1\) clique vertices and \(0\) to the rest. The permitted \(k\) are precisely the integers in \(\{0,\ldots,m-1\}\) closest to
\[
c=\frac{m+\ell(\ell+2)}2.
\]
Hence all possible equality cases, including all ties, are specified. When \(m\ge T+4\), the clique occupancy is asymptotically half as \(m\to\infty\) with fixed \(\ell\): \(k=m/2+\ell(\ell+2)/2+O(1)\).

## Assumptions and scope

All graphs are simple, finite, undirected and connected; edge lengths are one and the vertex probability measure is uniform. The function is real-valued and one-Lipschitz for the graph shortest-path metric, equivalently on every edge. The statement is for integer \(m\ge3\), integer \(\ell\ge3\). The path has \(\ell\) new vertices and \(\ell\) edges; its attachment vertex is **already** one of the \(m\) clique vertices. The variance is probability-normalized, not the unnormalized sum of squares. Translations preserve the variance and Lipschitz constraints.

## Proof

**Step 1 (strict convexity of core variables).** Normalize the attachment value to zero. Write the remaining clique values as \(x_1,\ldots,x_{m-1}\), and the successive path increments as \(\varepsilon_1,\ldots,\varepsilon_\ell\in[-1,1]\). The constraints are independent between the clique-value polytope
\[
\mathcal C=\{x:\lvert x_i\rvert\le1,\;\lvert x_i-x_j\rvert\le1\}
\]
and the increment cube. With the path increments fixed, centered variance is a strictly convex quadratic function of \(x\): its quadratic form is the variance of the vector that equals \(x_i\) at each nondistinguished clique vertex and zero at the attachment and at all new path vertices. This form is positive definite because the attachment coordinate is fixed at zero and every vertex has positive mass. Thus every maximizing \(x\) is a vertex of \(\mathcal C\).

The vertices of \(\mathcal C\) have all coordinates in \(\{0,1\}\), or all coordinates in \(\{-1,0\}\), with at least one nonzero coordinate. To verify this, consider the graph on the \(m\) clique vertices made of tight inequalities \(\lvert x_u-x_v\rvert=1\), including the distinguished zero vertex. If it were disconnected, a tight component not containing the distinguished vertex could be shifted by a sufficiently small amount in both directions, contradicting extremality. Therefore the tight graph is connected. All coordinates differ from zero by integers along tight paths, hence are in \(\{-1,0,1\}\); the clique diameter constraint excludes the simultaneous occurrence of \(-1\) and \(1\). Conversely, each such binary assignment with a nonzero coordinate is a vertex: the nonzero vertices have tight constraints to the attachment and all zero-valued vertices are tightly linked to a nonzero vertex. The all-zero assignment is not a vertex when \(m\ge2\), although it may be harmlessly included among candidates before Step 3 excludes it.

**Step 2 (straightening the tail).** By negating the function if necessary, all clique values lie in \(\{-1,0\}\). For a feasible path \(g(j)\) rooted at \(g(0)=0\), the Lipschitz property gives \(\lvert g(i)-g(j)\rvert\le\lvert i-j\rvert\) and \(\lvert g(j)-x\rvert\le j-x\) for each clique value \(x\in\{-1,0\}\). The straight path \(g_*(j)=j\) achieves **all** these upper bounds simultaneously for tail–tail pairs and all clique–tail pairs. Since
\[
\operatorname{Var}(f)=\frac1{N^2}\sum_{\{u,v\}\subset V}(f(u)-f(v))^2,
\]
replacing the tail by \(g_*\) cannot decrease variance. If some clique vertex has value \(-1\), equality forces \(g(j)=j\) for every \(j\), because all pairs involving that clique vertex have positive coefficient and attain the strict distance maximum only at \(j\). If no clique vertex has value \(-1\), this case is never optimal (Step 3). Hence every optimizer has the stated straight tail, not merely some optimizer.

**Step 3 (integer occupancy and transition).** Let \(k\in\{0,\ldots,m-1\}\) denote the number of clique values \(-1\). The value sum and squared-value sum are respectively \(A-k\) and \(B+k\), giving
\[
N^2\operatorname{Var}(f)=N(B+k)-(A-k)^2
=N(A+B)+\frac{N^2}4-(k-c)^2,
\qquad c=\frac{N+2A}2=\frac{m+\ell(\ell+2)}2.
\]
This is strictly concave in real \(k\); its integer maximizers are exactly the nearest integers to \(c\) after clipping to \(0\le k\le m-1\). In particular, \(k=0\) is never maximizing since the first difference of the numerator at zero is \(N+2A-1>0\).

The boundary occupancy \(k=m-1\) wins uniquely iff \(c>m-\tfrac32\), i.e. \(m<T+3\). At \(m=T+3\), \(c=m-\tfrac32\), so \(k=m-2\) and \(k=m-1\) tie. For larger \(m\), the maximizers are interior. This establishes the complete equality classification and the exact quadratic threshold.

In the interior/tie regime \(m\ge T+3\), the nearest-integer distance from \(c\) is zero when \(N\) is even and one half when \(N\) is odd, because \(2A=\ell(\ell+1)\) is even. Substituting \(A+B=\ell(\ell+1)(\ell+2)/3\) gives the second formula; inserting \(k=m-1\) gives the first. All statements follow. \(\square\)

## Verification

The standalone pure-Python script `verify_lollipop_spread.py` independently enumerates every clique-polytope vertex and every extreme path-increment vector for 47 small parameter pairs. It verifies the exact formula against full rational variance calculations, then checks the integer-quadratic optimizer and transition conditions for 35,920 additional parameter pairs and 17 coexistence thresholds. Execute `python verify_lollipop_spread.py` with Python 3. The exhaustive small cases are finite corroboration, not a proof for all parameters; Steps 1–3 establish the universal claim.

## Relationship to prior work

Alon, Boppana and Spencer introduced the weighted finite-metric spread constant and established general integral-optimizer structure for graph metrics. Addario-Berry, Janson and McDiarmid developed graph-spread theory for random graphs. Neither general framework is an explicit sharp lollipop formula or the quadratic optimizer transition stated here. A known bridge-barbell computation covers the short-tail specialization \(\ell=2\), which is **not claimed as new** and is excluded from the stated domain. The present assertion concerns the first and all longer genuinely path-shaped tails \(\ell\ge3\), and their new quadratic threshold. The lollipop terminology also occurs with other invariants (such as metric bases), which do not determine maximum Lipschitz variance.

## Limitations

The formula does not address nonuniform vertex measures, weighted edge lengths, several pendant paths, nonlinear moments, or arbitrary clique–tree attachments. The proof establishes maximum variance, not a sub-Gaussian constant or a general concentration rate. Although relevant primary sources have been compared, an equivalent exact lollipop variance calculation in differently indexed literature cannot be ruled out. The boundary \(\ell=2\) is an acknowledged previously covered specialization.

## References

1. N. Alon, R. Boppana and J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis **8** (1998), 411–436, DOI: 10.1007/s000390050062; author-hosted paper: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf. See the definition of spread and Section 2.1, particularly Theorem 2.1.
2. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, first posted 2009-02-06, https://arxiv.org/abs/0902.1156. See Section 1 for graph spread and its literature context, and the later random-graph results.
