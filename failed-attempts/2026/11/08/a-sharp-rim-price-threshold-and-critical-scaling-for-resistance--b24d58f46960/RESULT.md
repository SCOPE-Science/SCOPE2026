# A sharp rim-price threshold and critical scaling for resistance-optimal wheel networks

## Finding

For an integer \(m\ge3\), let \(W_{m+1}=K_1\vee C_m\) have one hub, \(m\) spokes, and \(m\) rim edges. Every spoke costs one unit per unit conductance, every rim edge costs \(c>0\), and the total conductance budget is \(B>0\). Conductances may be chosen independently on all \(2m\) edges and may be zero provided the weighted network remains connected. Let \(K\) denote the Kirchhoff index, the sum of effective resistances over unordered vertex pairs.

**Exact global allocation.** The optimal allocation is unique. Its spokes all have a common conductance \(x>0\), and its rim edges all have a common conductance \(y\ge0\), with \(m(x+cy)=B\). Writing \(t=y/x\), \(\alpha_k=4\sin^2(\pi k/m)\), and
\[
F_m(t)=1+(m+1)\sum_{k=1}^{m-1}\frac{1}{1+\alpha_k t},
\qquad
\Phi_{m,c}(t)=(1+ct)F_m(t),
\]
the sharp price cutoff is
\[
\boxed{c_m^*=2+\frac2m.}
\]
If \(c\ge c_m^*\), the unique optimum has \(t=0\), \(x=B/m\), \(y=0\), and \(K_{\min}=m^3/B\). If \(0<c<c_m^*\), its ratio \(t>0\) is the unique positive solution of
\[
\boxed{c+(m+1)\sum_{k=1}^{m-1}\frac{c-\alpha_k}{(1+\alpha_k t)^2}=0,}
\]
with \(x=B/[m(1+ct)]\), \(y=tx\), and \(K_{\min}=m\Phi_{m,c}(t)/B\). At the cutoff the optimal rim conductance is still exactly zero; there is no coexisting positive-rim optimizer.

**Large wheels and the boundary layer.** For every fixed \(0<c<2\),
\[
\lim_{m\to\infty}t=\frac{2-c}{2c},\qquad
\lim_{m\to\infty}\frac{BK_{\min}}{m^3}=\frac{\sqrt{c(4-c)}}2,
\]
and the optimal fraction of the total budget spent on the rim tends to \((2-c)/(4-c)\). For fixed \(c\ge2\), the normalized index instead tends to \(1\). At the critical scale \(c=2+\kappa/m\), with fixed real \(\kappa\) and \(m\) sufficiently large to make \(c>0\),
\[
\boxed{t=\frac{(2-\kappa)_+}{4m}+O(m^{-2}),\qquad
m^2\left(1-\frac{BK_{\min}}{m^3}\right)\longrightarrow
\frac{(2-\kappa)_+^2}{8},}
\]
where \((s)_+=\max\{s,0\}\). For \(\kappa\ge2\), the stronger assertion \(t=0\) holds exactly for all admissible \(m\).

## Assumptions and scope

The graph is simple, undirected, and unweighted as a *topology*, with independently selectable nonnegative electrical conductances. The rim forms a simple cycle, requiring \(m\ge3\). The budget is an equality because increasing any connected network conductance strictly improves the total effective resistance. The two price classes are invariant under the dihedral symmetries of the wheel. No assumption of equal actual conductances is made in the optimization domain; equality within price classes is a proved consequence. Effective resistance is finite on connected allocations and regarded as infinite on disconnected allocations. The same theorem applies to an upper-bound budget because the optimum spends it all.

## Proof

**1. Strict convexity and symmetry.** Put \(N=m+1\), \(J=\mathbf1\mathbf1^\top\), and \(X=L+J/N\), where \(L\) is the weighted Laplacian of a connected allocation. Then \(X\) is positive definite and
\[
K=N\bigl(\operatorname{tr}X^{-1}-1\bigr).
\]
For a nonzero symmetric Laplacian direction \(H\), the second derivative of this expression is
\[
2N\operatorname{tr}(X^{-1}H X^{-1}H X^{-1})>0.
\]
Indeed the trace is the squared Frobenius norm of \(X^{-1/2}H X^{-1}\), and edge-weight directions yield distinct nonzero \(H\) because every edge appears in a distinct off-diagonal entry. Thus the Kirchhoff index is strictly convex on the connected feasible set. The connected feasible set is convex, since mixtures of two connected nonnegative weighted graphs have connected support, and the index diverges upon loss of connectivity. Therefore an optimum exists and is unique. Averaging an optimum over the wheel's dihedral automorphisms preserves both the cost and the index; uniqueness forces constant conductance within the spoke and rim orbits. Since the hub would be isolated if all spokes vanished, \(x>0\). The budget is saturated by positive homogeneity and strict decrease under uniform conductance scaling.

**2. Exact reduction.** In the symmetry-reduced allocation the nonzero eigenvalues of \(L\) are \((m+1)x\) and \(x+\alpha_k y\) for \(1\le k<m\). Consequently
\[
K=\frac1x+(m+1)\sum_{k=1}^{m-1}\frac1{x+\alpha_k y}
=\frac{m}{B}(1+ct)F_m(t).
\]
The formula is a known spectral reduction for the uniformly priced wheel; the new analysis concerns unequal *prices* and the resulting support transition and scaling. For \(t\ge0\), differentiation gives
\[
\Phi_{m,c}'(t)=c+(m+1)\sum_{k=1}^{m-1}\frac{c-\alpha_k}{(1+\alpha_k t)^2}.
\]
The cycle trace identity \(\sum_{k=1}^{m-1}\alpha_k=2m\) yields
\[
\Phi_{m,c}'(0)=m^2\left(c-2-\frac2m\right).
\]
The map \(t\mapsto y=Bt/[m(1+ct)]\) is a strictly increasing bijection from \([0,\infty)\) onto \([0,B/(mc))\). On this latter interval the cost-constrained Kirchhoff index is strictly convex in \(y\). Also, \(\Phi_{m,c}'(t)\to c>0\) as \(t\to\infty\), and the objective diverges as \(x\to0\). The sign of the derivative at zero and strict convexity therefore give the asserted zero-rim cutoff, unique positive-rim stationary solution below it, and global optimality, including uniqueness at equality.

**3. Closed resolvent identity.** For \(t>0\), put \(s=\sqrt{1+4t}\) and \(q=(s-1)/(s+1)\). The Poisson-kernel identity
\[
\frac1{1+2t-2t\cos\theta}=\frac1s\left(1+2\sum_{j=1}^{\infty}q^j\cos(j\theta)\right)
\]
is absolutely convergent because \(0<q<1\). Summation over the \(m\)-th roots of unity retains exactly the Fourier indices divisible by \(m\) and gives
\[
\sum_{k=0}^{m-1}\frac1{1+4t\sin^2(\pi k/m)}
=\frac{m}{s}\frac{1+q^m}{1-q^m},\qquad
F_m(t)=\frac{m(m+1)}s\frac{1+q^m}{1-q^m}-m.
\]
The \(t=0\) value follows by continuity. This identity is useful for independent evaluation and asymptotics; it is not required to deduce the exact support cutoff.

**4. Large-ring limit at fixed price.** For fixed \(t>0\), the preceding identity gives \(F_m(t)/m^2\to(1+4t)^{-1/2}\), together with locally uniform derivative convergence on \(t>0\). At zero the same convergence holds by the elementary power-series expansion. Hence
\[
\frac{\Phi_{m,c}(t)}{m^2}\longrightarrow
G_c(t)=\frac{1+ct}{\sqrt{1+4t}},\quad
G_c'(t)=\frac{c-2+2ct}{(1+4t)^{3/2}}.
\]
For \(0<c<2\), this derivative has exactly one positive zero \(t_\infty=(2-c)/(2c)\). Uniform derivative convergence in neighborhoods on either side and uniqueness of every finite-dimensional optimum trap its ratio near that zero. Substitution gives \(G_c(t_\infty)=\sqrt{c(4-c)}/2\) and the budget fraction \(ct_\infty/(1+ct_\infty)=(2-c)/(4-c)\). For fixed \(c>2\), the exact cutoff eventually forces \(t=0\); for \(c=2\), the next step yields \(t\to0\) and normalized value \(1\).

**5. Critical finite-size scaling.** Let \(c=2+\kappa/m\). For bounded \(u\ge0\), the closed resolvent identity and a Taylor expansion at \(t=u/m\) give, uniformly for \(u\) in compact intervals,
\[
\frac{\Phi_{m,c}(u/m)}{m^2}
=1+\frac{2u^2+(\kappa-2)u}{m^2}+O(m^{-3}),
\]
with the same uniformity after differentiating once with respect to \(u\). The discarded factor \(q^m\) is super-polynomially small on such intervals. If \(\kappa<2\), the exact derivative at zero is negative. Using the differentiated expansion, the unique positive root is trapped between \(u=(2-\kappa)/4\pm\epsilon\) for each fixed \(\epsilon>0\), and Taylor's formula sharpens this to \(u=(2-\kappa)/4+O(m^{-1})\). Substitution into the quadratic coefficient yields the stated limiting improvement \((2-\kappa)^2/8\). If \(\kappa\ge2\), then \(c\ge c_m^*\) exactly and the rim is unfunded. This also proves the borderline \(c=2\) expansion \(t=1/(2m)+O(m^{-2})\).

## Verification

Run `python3 VERIFY.py` in the same directory as this document. The program uses only Python's standard library and checks the wheel Kirchhoff index against a direct exact-rational inverse of \(L+J/N\), the cycle-resolvent reduction, the first two cycle Laplacian moments, the Fourier sum identity at selected positive arguments, and the exact marginal-price identity. The replay output is `VERIFY_OK 260`. These are finite consistency checks; all parameter-uniform conclusions rest on the displayed proof.

## Relationship to prior work

Ghosh, Boyd, and Saberi already prove the strict-convexity framework, automorphism reduction, and the uniformly priced wheel optimization (their section 5.2 and equation (38)). Bendito, Carmona, Encinas, and Gesto independently present the known weighted wagon-wheel Kirchhoff-index formula on pages 1205–1206. Neither of these inspected derivations gives the separate rim-to-spoke *price* cutoff \(2+2/m\), the above finite-size priced critical law, or the global allocation regimes under two prices. The present result uses their established spectral starting point rather than claiming it as a new formula. The price change can be incorporated into the general convex program, but extracting its exact support boundary and its singular large-ring scaling requires the explicit analysis above.

## Limitations

Only wheels with a common price on all spokes and a separate common price on all rim edges are covered. Prices may not vary edge by edge within each orbit. A positive optimal rim-to-spoke ratio below threshold is generally specified implicitly, not by radicals. The model optimizes continuous nonnegative conductances, not discrete construction decisions or failure-robust designs. The material inspected does not exclude every older, unindexed equivalent result, and independent mathematical review has not occurred. The 2006 conference version of the general optimization framework predates the day-verified 2008 focal source, but its exact public release day was not established; no publication date is inferred from its conference month.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, DOI 10.1137/050645452. Authorized author-hosted full text: https://stanford.edu/~boyd/papers/pdf/eff_res.pdf. Section 5.2, especially equation (38), is the closest prior wheel optimization.
2. E. Bendito, A. Carmona, A. M. Encinas, and J. M. Gesto, *A Formula for the Kirchhoff Index*, International Journal of Quantum Chemistry 108 (2008), 1200–1206, DOI 10.1002/qua.21588; first published online January 22, 2008. Full text: https://mapthe.upc.edu/en/publications/docs/publications_2008_a-formula-for-the-kirchhoff-index.pdf. Pages 1205–1206 contain the wagon-wheel formula.
3. A. Ghosh, S. Boyd, and A. Saberi, shorter 2006 conference version, linked by the authors at https://stanford.edu/~boyd/papers/eff_res.html. It establishes the earlier public provenance of the general framework.
