# The fixed-contrarian beta law and exact finite-population fluctuations

## Finding

Let \(m,r\ge 1\) be integers. In the well-mixed, binary-opinion *model 1* of Masuda [1], there are \(m\) congregators, who copy either type of agent, and \(r\) contrarians, who copy other contrarians but adopt the opposite opinion from congregators. Let \((A,B)\) be the numbers holding opinion \(1\) in the two groups under the unique stationary law. Define \(D=2mr+m+r\). For **every finite** \(m,r\ge1\),

\[
\begin{aligned}
\mathbb E A&=m/2,\qquad \mathbb E B=r/2,\\
\operatorname{Var}(A/m)&=\frac{m+3r}{4D},\\
\operatorname{Cov}(A/m,B/r)&=\frac{r-m}{4D},\\
\operatorname{Var}(B/r)&=\frac{3m+r}{4D}.
\end{aligned}
\]

Moreover, if \(r\ge1\) is **fixed** while \(m\to\infty\), the joint stationary law converges weakly:

\[
(A/m,B)\ \Longrightarrow\ (U,V),\qquad
U\sim\operatorname{Beta}(r,r),\qquad
(V\mid U=u)\sim\operatorname{Binomial}(r,1-u).
\]

Thus \(U\) has density \(u^{r-1}(1-u)^{r-1}/\mathrm B(r,r)\) for \(0<u<1\). In particular, \(\operatorname{Var}(A/m)\to1/[4(2r+1)]\). For one contrarian the limiting congregator share is uniform; for two it has the nonuniform density \(6u(1-u)\). These statements concern a **fixed number of contrarians**, not a fixed positive contrarian fraction.

## Assumptions and scope

The time-homogeneous finite-state continuous-time chain has states \((a,b)\in\{0,\ldots,m\}\times\{0,\ldots,r\}\) and the following *unscaled* nonzero neighbor transition rates (zero rates simply suppress a transition):

| Change | Rate |
|---|---|
| \((a,b)\mapsto(a+1,b)\) | \((m-a)(a+b)\) |
| \((a,b)\mapsto(a-1,b)\) | \(a(m-a+r-b)\) |
| \((a,b)\mapsto(a,b+1)\) | \((r-b)(m-a+b)\) |
| \((a,b)\mapsto(a,b-1)\) | \(b(a+r-b)\) |

The rates follow the four pair-counts for copy/oppose interactions. Multiplication of all rates by the same positive constant leaves the stationary law unchanged. No external noise, stubborn agents, nonlinear response or interaction network other than complete mixing is assumed. Counts \(m,r\) are at least one; the limit holds for each fixed positive integer \(r\), not uniformly in \(r\).

## Proof

**1. Unique stationary law and centering.** Every state reaches \((0,0)\) through positive-rate steps: reduce \(a\) when \(b<r\); when \(b=r\) and reduction is blocked, first decrease \(b\) after creating a positive \(a\) if needed. Then decrease \(b\) with \(a=0\) while \(b<r\). Conversely, from \((0,0)\) increase \(b\) to the desired positive value, increase \(a\) while \(b>0\), and (when the target has \(b=0\)) decrease \(b\) at positive \(a\). This also handles all boundary states. Hence the finite chain is irreducible and has a unique stationary distribution. The rates are invariant under \((a,b)\mapsto(m-a,r-b)\); uniqueness gives \(\mathbb E A=m/2\) and \(\mathbb E B=r/2\).

**2. Exact finite-size moments.** Set \(X=A-m/2\), \(Y=B-r/2\), and denote their stationary second moments by \(S=\mathbb E X^2\), \(H=\mathbb E XY\), \(T=\mathbb E Y^2\). The generator \(L\) obeys

\[
LX=mY-rX,\qquad LY=-rX-mY,
\]

and direct substitution of the four jump rates into \(L(X^2)\), \(L(XY)\), \(L(Y^2)\), followed by stationarity, yields

\[
\begin{aligned}
0&=(m^2+mr)/2-2(r+1)S+2(m-1)H,\\
0&=-rS-(m+r)H+mT,\\
0&=(mr+r^2)/2-2(r-1)H-2(m+1)T.
\end{aligned}
\]

This linear system has the unique solution

\[
(S,H,T)=\frac{1}{4D}
\bigl(m^2(m+3r),\ mr(r-m),\ r^2(3m+r)\bigr).
\]

Dividing by the respective group-size factors proves all finite-size formulas. The equations are exact generator identities, with no Gaussian or infinite-size approximation.

**3. Fast conditional contrarian equilibrium.** Write \(x=a/m\) and view the stationary count law as a measure \(\mu_m\) on the compact space \([0,1]\times\{0,\ldots,r\}\). Fix \(r\). Let \(K_x\) act on functions of the count \(b\) by

\[
(K_x g)(b)=(r-b)(1-x)[g(b+1)-g(b)]
+bx[g(b-1)-g(b)].
\]

For every smooth \(f\) and every function \(g\) on \(\{0,\ldots,r\}\), Taylor expansion of the congregator jumps and the exact contrarian rates give, uniformly on the entire state space including its boundary,

\[
\frac1m L[f(x)g(b)]=f(x)(K_x g)(b)+O_{f,g,r}(m^{-1}).
\]

Every sequence \(\mu_m\) has weakly convergent subsequences. For a limit \(\mu\), stationarity and the last display imply \(\int f(x)K_xg(b)\,d\mu=0\). Since continuous \(f\) are arbitrary, the conditional law of \(b\) given \(x\) must be stationary for \(K_x\) for almost every \(x\). This finite birth-death chain has the **unique** stationary distribution \(\operatorname{Binomial}(r,1-x)\): detailed balance applies on \(0<x<1\), and at \(x=0,1\) it has respectively the unique absorbing states \(b=r\) and \(b=0\). Thus every limit satisfies

\[
\mathbb E_\mu[B\mid U=u]=r(1-u),\qquad
(B\mid U=u)\sim\operatorname{Binomial}(r,1-u).
\]

**4. The slow marginal is beta.** For each \(f\in C^3([0,1])\), the exact congregator drift \((q_A^+-q_A^-)/m=b-rx\) and its jump-rate sum give the uniform expansion

\[
L f(x,b)=(b-rx)f'(x)+x(1-x)f''(x)+O_{f,r}(m^{-1}).
\]

Passing to the same stationary limit and substituting the conditional mean from step 3 yields

\[
\mathbb E_\mu\left[r(1-2U)f'(U)+U(1-U)f''(U)\right]=0.
\]

For \(f(u)=u^k\), \(k\ge1\), writing \(M_k=\mathbb E U^k\) and \(M_0=1\) gives

\[
M_k=\frac{r+k-1}{2r+k-1}M_{k-1}
=\frac{(r)_k}{(2r)_k}.
\]

These are precisely the moments of \(\operatorname{Beta}(r,r)\). Probability measures on \([0,1]\) are uniquely determined by their moments, so every subsequential marginal limit is the same beta law. The conditional law from step 3 uniquely determines the joint measure as well. All subsequences therefore have the same limit, proving the full claimed weak convergence.

## Verification

Run `python3 checker.py` with Python's standard library. For all \(1\le m\le6\), \(1\le r\le4\), the checker constructs the exact rational Markov generator, solves its stationary equations using rational elimination, verifies positivity and stationarity, compares all three centered second moments to the formulas, and independently checks the three generator moment equations. It reports 24 finite chains and 378 aggregate states. The uniform generator expansions and Hausdorff-moment argument above, **not** these finite checks, prove the infinite-limit assertion. Exact arithmetic gives, for example, limiting congregator variances \(1/12\), \(1/20\), and \(1/28\) for fixed \(r=1,2,3\), respectively.

## Relationship to prior work

Masuda [1] introduced exactly the copy/oppose type rule used here. His Section III.2.1 derives a Gaussian small-fluctuation approximation when the relevant populations are large, and Section III.3 derives the uniform congregator-share limit for the **one-contrarian** case. The result here supplies the nonperturbative finite-\(m,r\) covariance matrix and a joint \(\operatorname{Beta}(r,r)\)–binomial law for every fixed \(r\), including \(r\ge2\), without claiming the already known \(r=1\) case as new.

Banisch [2] analyzes a different rule: the contrarian action is chosen randomly by any agent at each update, rather than being assigned permanently to a subpopulation. Mori–Hisakado–Nakayama [3] derive a multivariate beta law for voter dynamics with intrinsic preference parameters on networks, not the conditional fixed-contrarian joint limit here. Khalil–Toral [4] derive exact moments for a *noisy* model where contrarians oppose both agent types; this differs from model 1, where contrarians **imitate their own type**. Generic Wright–Fisher beta stationary laws explain the form of the marginal limit, but do not by themselves establish the specific finite-state reduction, joint conditional law, or finite-size covariance formulas.

## Limitations

The theorem is limited to stationary distributions under complete mixing, unit relative interaction propensities and the precise model-1 contrarian rule. It does not assert convergence rates in \(m\), an exact closed-form **entire finite-state** stationary probability mass function, transient mixing-time estimates, the same beta law when \(r\) grows with \(m\), or any result for Masuda's models 2 and 3. Historical priority beyond the inspected literature is not independently certified.

## References

1. N. Masuda, *Voter models with contrarian agents*, arXiv:1306.4401 (first posted 19 June 2013), *Physical Review E* **88**, 052803 (2013), https://arxiv.org/abs/1306.4401.
2. S. Banisch, *From Microscopic Heterogeneity to Macroscopic Complexity in the Contrarian Voter Model*, arXiv:1510.04467 (2015), https://arxiv.org/abs/1510.04467.
3. S. Mori, M. Hisakado, and K. Nakayama, *A voter model on networks and multivariate beta distribution*, arXiv:1810.05643 (2018), https://arxiv.org/abs/1810.05643.
4. N. Khalil and R. Toral, *The noisy voter model under the influence of contrarians*, arXiv:1807.03176 (2018), https://arxiv.org/abs/1807.03176.
