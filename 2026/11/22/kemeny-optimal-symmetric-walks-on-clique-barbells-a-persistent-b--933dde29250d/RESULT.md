# Kemeny-optimal symmetric walks on clique barbells: a persistent bridge allocation

## Finding
Let \(s\ge3\) be an integer, and join two disjoint copies of \(K_s\) by one edge connecting distinguished vertices (the gateways). Among **all** irreducible symmetric nonnegative stochastic matrices \(P\) whose off-diagonal entries vanish outside this graph, the following matrix uniquely minimizes
\[
\mathcal K(P)=\sum_{j=2}^{2s}\frac{1}{1-\lambda_j(P)},
\]
where \(1=\lambda_1(P)>\lambda_2(P)\ge\cdots\ge\lambda_{2s}(P)\) are the real eigenvalues. This is the zero-at-start convention for Kemeny's constant; adding the alternative return-time constant \(1\) does not change the optimizer.

For each gateway-to-nongateway edge within its own clique, the optimal transition probability is \(u_s\). The single bridge receives \(t_s=1-(s-1)u_s\), and each edge between two nongateway vertices within the same clique receives
\[
v_s=\frac{1-u_s}{s-2}.
\]
All diagonal holding probabilities are exactly zero. The number \(u_s\) is the unique root in \(0<u<1/(s-1)\) of
\[
\frac{2(s-2)^2}{(s-1-u)^2}-\frac{s+1}{s u^2}
+\frac{s(s-1)}{2(1-(s-1)u)^2}=0.
\]
The exact minimum is
\[
\mathcal K_s^* = \frac{2(s-2)^2}{s-1-u_s}
+\frac{s+1}{s u_s}+\frac{s}{2(1-(s-1)u_s)}.
\]
In particular, the bridge probability stays bounded away from zero as the cliques grow:
\[
su_s\longrightarrow 2-\sqrt2,\qquad
 t_s\longrightarrow\sqrt2-1,\qquad
\frac{\mathcal K_s^*}{s}\longrightarrow\frac72+\sqrt2.
\]
By contrast, assigning probability \(1/s\) to every graph edge (and placing the remaining probability on the diagonal) gives
\[
\mathcal K_{\mathrm{degree},s}=\frac{s^2}{2}+3s-3,
\qquad
\frac{\mathcal K_{\mathrm{degree},s}}{\mathcal K_s^*}
\sim\frac{s}{7+2\sqrt2}.
\]
Thus the standard maximum-degree symmetric walk can be arbitrarily worse in Kemeny's constant, even though it uses the same graph edges and has the same uniform invariant distribution.

## Assumptions and scope
The graph has exactly \(2s\) vertices and a single bridge. Every allowed undirected graph edge has one freely chosen shared transition probability; the total incident probability at each vertex is at most one, with the remaining probability assigned to a self-loop. The stationary distribution is uniform because \(P\) is symmetric. No vertex weights, heterogeneous traversal costs, or restriction to graph-automorphism-invariant competitors is imposed. An irreducible matrix has a connected positive-probability support graph. Results are for the zero-at-start Kemeny normalization specified above.

## Proof
**Global uniqueness and symmetry reduction.** Put \(L=I-P\), \(N=2s\), \(J=\mathbf1\mathbf1^\top\), and \(A=L+J/N\). For an irreducible symmetric chain, \(A\) is positive definite and \(\mathcal K=\operatorname{tr}(A^{-1})-1\). For every nonzero symmetric perturbation \(H\),
\[
\frac{d^2}{d\varepsilon^2}\operatorname{tr}(A+\varepsilon H)^{-1}\Big|_{\varepsilon=0}
=2\operatorname{tr}(A^{-1}H A^{-1}H A^{-1})>0.
\]
Indeed, writing \(B=A^{-1/2}HA^{-1/2}\), the matrix inside the trace is \(A^{-1/2}B^2A^{-1/2}\), positive semidefinite and nonzero. Changing any graph-edge probability changes an off-diagonal entry of \(L\), so the map from edge probabilities to \(A\) is injective. Hence the objective is strictly convex in all edge probabilities. The feasible region of stochastic symmetric matrices is compact, and \(\mathcal K\) tends to infinity toward a disconnected limit. An irreducible feasible matrix exists, so the optimum exists and is unique. Graph automorphisms preserve the objective, forcing this unique optimum to be invariant under permutations of nongateway vertices and interchange of the two cliques.

**Spectrum.** Write \(u\) for each gateway-to-nongateway probability, \(v\) for each nongateway-to-nongateway probability, and \(t\) for the bridge. Then \((s-1)u+t\le1\) and \(u+(s-2)v\le1\). Nongateway vectors of sum zero on each clique have Laplacian eigenvalue \(u+(s-1)v\), multiplicity \(2(s-2)\). The clique-symmetric two-level subspace has eigenvalues \(0\) and \(su\). On the clique-antisymmetric two-level subspace, the Laplacian is represented by
\[
\begin{pmatrix}(s-1)u+2t&-(s-1)u\\-u&u\end{pmatrix},
\]
whose eigenvalues have sum \(su+2t\) and product \(2tu\). Consequently
\[
\mathcal K(u,t,v)=\frac{2(s-2)}{u+(s-1)v}
+\frac{s+1}{su}+\frac{s}{2t}.
\]
This formula is valid for positive \(u,t\) and any nonnegative feasible \(v\), including zero.

**Exact optimizer.** At fixed positive \(u\), the last display decreases strictly as either \(t\) or \(v\) increases. Thus both vertex probability budgets are saturated:
\(t=1-(s-1)u\) and \(v=(1-u)/(s-2)\). Substitution gives
\[
f_s(u)=\frac{2(s-2)^2}{s-1-u}+\frac{s+1}{su}
+\frac{s}{2(1-(s-1)u)},\quad 0<u<\frac1{s-1}.
\]
Its derivative is the stated scalar equation and
\[
f_s''(u)=\frac{4(s-2)^2}{(s-1-u)^3}
+\frac{2(s+1)}{su^3}
+\frac{s(s-1)^2}{(1-(s-1)u)^3}>0.
\]
The derivative tends to negative infinity at the left endpoint and positive infinity at the right endpoint, so its unique root is the unique global minimizer. Strict convexity before symmetrization excludes every noninvariant competitor. At the optimum, all three edge classes are positive and each row sum of off-diagonal entries is exactly one.

**Asymptotics and comparison.** Set \(x=su\). On compact subintervals of \(0<x<1\),
\[
\frac{f_s(x/s)}s\longrightarrow 2+\frac1x+\frac1{2(1-x)}.
\]
The terms \(1/x\) and \(1/[2(1-x)]\) force minimizers away from the interval endpoints. The strictly convex limit has unique stationary point \(x=2-\sqrt2\), yielding the three limits stated in the finding. Finally, setting \(u=v=t=1/s\) in the spectral formula gives the exact maximum-degree benchmark. Taking the ratio proves the claimed unbounded penalty.

## Verification
Run `python verify.py` with Python 3.10+ and SymPy 1.10+. The script builds complete \(2s\)-vertex Laplacians, evaluates the inverse of \(L+J/(2s)\) over exact rationals and independently checks the orbit-spectrum formula for several rational weight allocations and graph sizes. It also checks the maximum-degree closed form, numerically locates the unique scalar minimum, and tests the large-size constants. Its 63 assertions pass. The finite tests support the calculation but are not an infinite-family proof; the proof is the spectral and convex analysis above.

## Relationship to prior work
Boyd, Diaconis and Xiao (2004) developed optimization of symmetric stochastic edge probabilities for the **different** second-largest-eigenvalue-modulus objective. Patel, Agharkar and Bullo (2015, preceded by a 2014 conference paper) established the general convex-programming framework for minimizing Kemeny's constant with fixed stationary distribution; the convex formulation and spectral trace identity are prior work. Breen et al. (2019) computed Kemeny's constant for **degree-proportional simple random walks** on barbell-type graphs, without freely optimizing the transition entries. Durastante, Gnazzo and Meini (2026) studied structure-preserving Kemeny improvements and numerical solvers, not the exact unrestricted optimum of this two-clique family. The claim here is the explicit unique family optimizer, its strictly positive limiting bridge allocation, and the asymptotically unbounded benchmark gap, not general convexity or the unweighted barbell calculation.

## Limitations
Only two **equal-size** cliques connected by exactly one bridge are classified. The theorem does not cover nonsymmetric or nonuniform-stationary policies, fixed nonzero self-loop requirements, different edge prices, or longer bridge paths. The comparison is to one precisely specified maximum-degree symmetric walk, not to every natural heuristic. Earlier general convex-programming results may yield the exact optimum after specialized algebra not spelled out there; equivalent closed-form or asymptotic results in unindexed literature remain possible. No independent audit is claimed.

## References
1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. DOI: 10.1137/S0036144503423264. https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf
2. R. Patel, P. Agharkar and F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control 60 (2015), 3156–3167. DOI: 10.1109/TAC.2015.2426317. https://motion.me.ucsb.edu/pdf/2014b-pab.pdf
3. J. Breen et al., *Computing Kemeny's Constant for Barbell-Type Graphs*, Electronic Journal of Linear Algebra 35 (2019), 583–598. DOI: 10.13001/ela.2019.5175. https://journals.uwyo.edu/index.php/ela/article/download/5175/4941/5239
4. F. Durastante, M. Gnazzo and B. Meini, *Kemeny's Constant Minimization for Reversible Markov Chains via Structure-Preserving Perturbations*, BIT Numerical Mathematics 66 (2026), article 59. DOI: 10.1007/s10543-026-01152-6. https://link.springer.com/article/10.1007/s10543-026-01152-6
