# Sharp penalty-Wolfe certificate inflation on affine constraints

## Finding
For every real \(r\geq 1\), the least universal factor \(K(r)\) such that an \((\iota,\nu,\gamma)\)-Penalty normalized Wolfe certificate necessarily remains an \((\iota,K(r)\nu,r\gamma)\)-certificate at the same point is
\[
K(r)=2r-1.
\]
The upper bound appears in Proposition 4.3 of Lin--Zhang [1]. The matching **lower bound**, even under strict Slater feasibility and the paper's positive quadratic-growth hypothesis, is supplied here. For the attaining affine problem, all affine cutting planes coincide with their underlying functions; adding evaluations at the fixed candidate cannot improve the lower bound.

## Assumptions and scope
Let \(X\subset\mathbb R^d\) be closed and convex, \(f:X\to\mathbb R\) and \(G:X\to\mathbb R\) convex, and \(\gamma>0\), \(\iota>0\), \(\nu>0\). For a finite set \(P\subseteq B(\bar y,\iota)\cap X\) containing \(\bar y\), let
\[
\psi_{P,\gamma}(x)=\max_{z\in P}\ell_f(x;z)+\gamma\left[\max_{z\in P}\ell_G(x;z)\right]_+,
\qquad
V_{P,\gamma}(\iota;\bar y)=\frac1\iota\max_{x\in B(\bar y,\iota)\cap X}
\bigl(\psi_{P,\gamma}(\bar y)-\psi_{P,\gamma}(x)\bigr).
\]
Here \(\ell_f\) and \(\ell_G\) are affine first-order minorants at evaluation points (choose subgradients if needed), and \([a]_+=\max\{a,0\}\). The certificate requires both \(V_{P,\gamma}(\iota;\bar y)\leq\nu\) and \([G(\bar y)]_+\leq 2\iota\nu/\gamma\). This is Definition 3 in [1]. The inflation statement concerns the same point and the same penalty-certificate definition; it does not preclude improving guarantees by changing the point or using other information.

## Proof
Fix any \(r\geq1\). Because the separated cutting-plane penalty term is nonnegative, \(\psi_{P,r\gamma}(x)\geq\psi_{P,\gamma}(x)\) for every \(x\). Since \(\bar y\in P\), the cut model interpolates at \(\bar y\), and therefore
\[
\psi_{P,r\gamma}(\bar y)-\psi_{P,\gamma}(\bar y)
=(r-1)\gamma[G(\bar y)]_+.
\]
Consequently, for every \(x\) in the ball/domain intersection,
\[
\psi_{P,r\gamma}(\bar y)-\psi_{P,r\gamma}(x)
\leq\psi_{P,\gamma}(\bar y)-\psi_{P,\gamma}(x)
+(r-1)\gamma[G(\bar y)]_+.
\]
Divide by \(\iota\) and maximize. The two source certificate inequalities yield
\[
V_{P,r\gamma}(\iota;\bar y)\leq\nu+2(r-1)\nu=(2r-1)\nu.
\]
The target feasibility inequality also holds because \(r\leq2r-1\):
\[
[G(\bar y)]_+\leq\frac{2\iota\nu}{\gamma}
\leq\frac{2\iota(2r-1)\nu}{r\gamma}.
\]
Thus \(K(r)\leq2r-1\), recovering the source upper bound.

For sharpness use the **same scalar instance for every** \(r\geq1\):
\[
X=[-2,2],\qquad f(x)=-x,\qquad G(x)=2(1+x),
\qquad\bar y=0,\quad\iota=\nu=\gamma=1,\quad P=\{0\}.
\]
Every affine first-order model is exact, so for **any** finite evaluation set, \(\psi_{P,t}(x)=-x+t[2(1+x)]_+\) whenever \(t>0\). On the certificate ball \([-1,1]\), the positive part is active, giving
\[
\psi_{P,1}(x)=2+x,\qquad
\psi_{P,r}(x)=2r+(2r-1)x.
\]
Both expressions have positive slope. Their local model residuals at zero are therefore
\[
V_{P,1}(1;0)=\psi_{P,1}(0)-\psi_{P,1}(-1)=1,
\qquad
V_{P,r}(1;0)=\psi_{P,r}(0)-\psi_{P,r}(-1)=2r-1.
\]
Also \([G(0)]_+=2=2\iota\nu/\gamma\). Thus \(P\) is an original certificate, while no smaller-than-\((2r-1)\) target constant can satisfy the target model-residual inequality. This proves \(K(r)\geq2r-1\), including if the fixed candidate's bundle is enlarged.

The sharpness witness obeys the source's regularity assumptions. The point \(x=-2\) is strictly feasible, since \(G(-2)=-2\). The constrained problem has the unique optimum \(x_*=-1\), and its optimal multiplier is \(\lambda_*=1/2\). At the corresponding exact-penalty coefficient \(2\lambda_*=1\), the penalty objective is
\[
\phi_1(x)=f(x)+[G(x)]_+=1+|x+1|\qquad(x\in[-2,2]).
\]
Since \(|x+1|\leq3\) on \(X\), its exact global quadratic-growth modulus is \(\mu_*=2/3\):
\[
\phi_1(x)-\phi_1(x_*)=|x+1|\geq\frac13|x+1|^2
=\frac{\mu_*}{2}\operatorname{dist}(x,\{-1\})^2.
\]
The value \(2/3\) cannot be increased because equality holds at \(x=2\). Both functions are affine and hence one-piece smooth.

## Verification
An accompanying standalone Python script, `CHECK.py`, performs exact-fraction checks at representative penalty ratios, the saturated source-certificate inequalities, the strict Slater point, and exact quadratic-growth checks at rational domain points. It reports `VERIFY_OK`. The proof above, not these finite tests, establishes all real parameter values and all points in the domain.

## Relationship to prior work
Lin and Zhang [1], Definition 3 and Proposition 4.3 (pp. 13--17 of version 1), introduce the same separated penalty-Wolfe model and prove the transfer **upper bound** \(2r-1\). They do not give a matching worst-case construction or establish sharpness under Slater and quadratic-growth regularity. The new assertion here is the universal optimality of that factor, witnessed by a one-dimensional affine constrained problem. The ordinary unconstrained Wolfe-certificate predecessors discussed in [1, Sec. 4] do not themselves have a penalty-parameter transfer result.

## Limitations
Sharpness is for the specified local residual, unchanged candidate, and the certificate information in Definition 3. It does not rule out sharper guarantees with additional information, alternate certificate definitions, or changes to the candidate point. The exact witness has an active affine constraint and a nonsmooth composite penalty, but its objective and constraint are individually smooth. Independent validation has not been performed. Literature search and full-text comparison do not establish uniqueness against all unpublished or unindexed work.

## References
[1] Z. Lin and Z. Zhang, *Accelerated Prox-Level Methods for Unknown Piecewise-Smooth Optimization II: Function-constrained Optimization*, arXiv:2609.03251v1 (first public 2026-09-03), especially Definition 3, Proposition 4.3, and its detailed proof, pp. 13--17. https://arxiv.org/abs/2609.03251
