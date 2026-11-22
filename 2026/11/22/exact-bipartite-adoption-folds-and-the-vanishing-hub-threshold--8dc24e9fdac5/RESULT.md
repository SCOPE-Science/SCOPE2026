# Exact bipartite adoption folds and the vanishing hub threshold

## Finding

Consider the deterministic nonlinear social-adoption network equation of Ariwayo, Morsky and Asllani, with fixed reinforcement exponent \(d>1\):
\[
\frac{dx_i}{d\tau}=-x_i+\lambda(1-x_i)\sum_j A_{ij}x_j^d,\qquad 0\le x_i\le1.
\]
Time has been rescaled by the positive abandonment rate, and \(\lambda=\beta/\gamma>0\). On the simple, unweighted, complete bipartite social network \(K_{m,n}\), for every pair of integers \(m,n\ge1\), the following is an **exact full-network equilibrium and local-stability classification**.

Define \(F_d(s)=s^{d+1}/(1-s)\) for \(0<s<1\). There is a unique pair \((x_c,y_c)\in(0,1)^2\) solving
\[
\frac{F_d(x_c)}{F_d(y_c)}=\frac{n}{m},\qquad
(1-x_c)(1-y_c)=d^{-2}.
\]
Set
\[
\lambda_c(m,n,d)=\frac{y_c}{m x_c^d(1-y_c)}
=\frac{x_c}{n y_c^d(1-x_c)}.
\]
If \(0<\lambda<\lambda_c\), the all-zero state is the sole equilibrium. At \(\lambda=\lambda_c\), there are exactly two equilibria: zero and one strictly positive, nonhyperbolic equilibrium with one simple zero eigenvalue and all remaining eigenvalues negative. At \(\lambda>\lambda_c\), there are precisely three equilibria: zero, a lower positive branch that is a saddle with exactly one positive eigenvalue, and an upper positive branch that is locally exponentially attracting. The zero state is locally exponentially attracting for every \(\lambda>0\). No equilibria with a partially adopted set of vertices exist.

For the star \(K_{1,n}\) with \(n\to\infty\), the exact critical threshold satisfies
\[
\boxed{\lambda_c(1,n,d)\sim\kappa_d n^{-1/(d+1)},\qquad
\kappa_d=d^{2/(d+1)}(1-d^{-2})^{1-d}.}
\]
In particular, at quadratic reinforcement \(d=2\),
\[
\lambda_c(1,n,2)\sim\frac{2^{8/3}}{3}n^{-1/3}.
\]
The source's scalar degree-averaged equation predicts a threshold approaching \(2\) for this star family when \(d=2\), whereas the exact node-level threshold tends to zero. This does **not** contradict the source approximation: its narrow-degree assumptions are violated by stars.

## Assumptions and scope

The graph is exactly the undirected, loopless, unweighted \(K_{m,n}\), all vertices share \(\beta,\gamma>0\) and the fixed real exponent \(d>1\), and the dynamics are deterministic fractions on the compact cube \([0,1]^{m+n}\). The per-vertex social-influence input is the unnormalized sum of neighbors' \(d\)-th powers, **not** a power of the count of distinct adopted neighbors. For \(d>1\), the vector field is continuously differentiable on the cube. Boundaries point inward or are tangent: at \(x_i=0\), \(\dot x_i\ge0\); at \(x_i=1\), \(\dot x_i=-1\). Claims concern all equilibria and local spectral stability, not stochastic epidemic thresholds or global attraction from all nonzero initial conditions.

## Proof

**1. Support propagation and equalization.** At any equilibrium, \(x_i=1\) is impossible, and
\[
\frac{x_i}{1-x_i}=\lambda\sum_jA_{ij}x_j^d.
\]
A positive coordinate forces every neighboring coordinate to be positive: the neighbor's right-hand side contains a strictly positive term. Connectedness of \(K_{m,n}\) implies that an equilibrium is either identically zero or strictly positive at every vertex. All vertices in either bipartition have exactly the same input and therefore equal equilibrium values; write \(x\) for each of the \(m\) vertices, \(y\) for each of the \(n\). Their equations are
\[
\frac{x}{1-x}=\lambda n y^d,\qquad
\frac{y}{1-y}=\lambda m x^d.\tag{1}
\]

**2. A strictly unimodal equilibrium parameter.** Dividing (1) yields
\[
\frac{F_d(x)}{F_d(y)}=\frac{n}{m}.
\]
The map \(F_d:(0,1)\to(0,\infty)\) is smooth, strictly increasing and onto, so for each \(x\in(0,1)\) there is exactly one \(y=y(x)=F_d^{-1}((m/n)F_d(x))\). This function is strictly increasing from 0 to 1. The only parameter supporting this equilibrium is
\[
L(x)=\frac{y(x)}{m x^d(1-y(x))}.
\]
At both endpoints \(L(x)\to\infty\). At zero this follows from \(y(x)\sim(m/n)^{1/(d+1)}x\), giving \(L(x)\asymp x^{1-d}\to\infty\); at one, the denominator contains \(1-y(x)\to0\). Direct logarithmic differentiation, using \(F'_d(s)/F_d(s)=(d+1-ds)/(s(1-s))\), gives the exact identity
\[
\frac{d}{dx}\log L(x)=
\frac{1-d^2(1-x)(1-y(x))}{x(1-x)[d+1-dy(x)]}.\tag{2}
\]
The denominator is positive; \((1-x)(1-y(x))\) decreases strictly from 1 to 0. As \(d>1\), the numerator has exactly one zero, from negative to positive, at \((x_c,y_c)\). Consequently \(L\) decreases strictly, reaches one **nondegenerate** minimum \(\lambda_c\), then increases strictly. This proves uniqueness, the exact zero/one/two positive-equilibrium counts and the nondegenerate turning of the positive branch. At the minimum \(L''(x_c)>0\) by differentiating the numerator in (2), since \(y'(x_c)>0\).

**3. Full \((m+n)\)-dimensional stability, not merely symmetry-restricted stability.** At a positive equilibrium, the Jacobian has the block form
\[
J=\begin{pmatrix}
-\dfrac1{1-x}I_m & \dfrac{d x}{n y}\mathbf 1_m\mathbf 1_n^{\mathsf T}\\
\dfrac{d y}{m x}\mathbf 1_n\mathbf 1_m^{\mathsf T} & -\dfrac1{1-y}I_n
\end{pmatrix}.
\]
The within-part differences supply \(m-1\) eigenvalues \(-1/(1-x)\) and \(n-1\) eigenvalues \(-1/(1-y)\). The remaining two are the eigenvalues of
\[
J_{\mathrm{part}}=\begin{pmatrix}-1/(1-x)&d x/y\\d y/x&-1/(1-y)\end{pmatrix},
\quad \operatorname{tr}J_{\mathrm{part}}<0,
\quad \det J_{\mathrm{part}}=\frac1{(1-x)(1-y)}-d^2.\tag{3}
\]
Before the minimum of \(L\), the product exceeds \(d^{-2}\), so the determinant is negative and there is exactly one positive eigenvalue. After the minimum it is positive with negative trace, and all eigenvalues have negative real parts. At the minimum the determinant is zero, the other part eigenvalue is strictly negative, and the zero is simple. The smooth, nondegenerate turning of \(L\) gives a standard saddle-node as \(\lambda\) increases. At the zero state, all derivatives of the nonlinear influence terms vanish because \(d>1\), so \(J(0)=-I_{m+n}\): zero remains locally exponentially attracting.

**4. Star asymptotics.** For \(m=1\), \(n\to\infty\), at the fold \(F_d(y_c)=F_d(x_c)/n\). The fold equation implies \(x_c\le1-d^{-2}\) and \(y_c\ge0\). If a subsequence had \(y_c\ge\varepsilon>0\), then \(F_d(x_c)\ge nF_d(\varepsilon)\to\infty\), forcing \(x_c\to1\), which contradicts \((1-x_c)(1-y_c)=d^{-2}>0\). Thus \(y_c\to0\) and \(x_c\to x_*=1-d^{-2}\). From the \(F_d\)-ratio,
\[
y_c\sim n^{-1/(d+1)}\left(\frac{x_*^{d+1}}{1-x_*}\right)^{1/(d+1)}.
\]
Substitution in \(\lambda_c=y_c/[x_c^d(1-y_c)]\) gives \(\kappa_d\) as claimed. At \(d=2\), \(\kappa_2=2^{8/3}/3\).

Finally, the scalar degree-averaged equation is \(\dot z=-z+\lambda\bar k z^d(1-z)\), whose saddle-node threshold is
\[
\lambda_{\mathrm{avg}}=\frac{d^d}{(d-1)^{d-1}\bar k}.
\]
For \(K_{1,n}\), \(\bar k=2n/(n+1)\to2\), so for \(d=2\), \(\lambda_{\mathrm{avg}}\to2\). This is a comparison of different models, not an error claim about a model applied outside its stated approximation regime.

## Verification

The standalone standard-library program `verify_bipartite.py` checks the equilibrium equations, unique-fold identities, the sign of the two-dimensional determinant on both branches, exact rational balanced-biclique witnesses, and large-star asymptotics for four exponents. Run `python3 verify_bipartite.py` next to this file. It reports 313 passed exact-rational / floating-point checks. The checks support algebra and numerical examples; the uniform all-size result follows from steps 1–4, **not** finite enumeration. The proof uses no imported numerical certificate.

## Relationship to prior work

Ariwayo, Morsky and Asllani introduced the node-level power-law adoption model, obtained a scalar degree-averaged approximation under concentrated degrees, and analyzed its homogeneous positive branches; they did not establish the complete-bipartite node-level fold, spectral classification or star threshold exponent in their accessible main text and appendices. The present result is an analysis of their model's highly heterogeneous network regime, rather than a claim that a degree-averaged approximation should apply to stars. Chiba-Okabe and Plotkin analyze a different payoff-biased social-learning process with power-law exposure thresholds. Prior SIS work on star graphs and nonlinear hypergraph contagion uses other stochastic generators or multiple-neighbor mechanisms and does not directly give (1)–(3). General saddle-node and monotone-systems techniques are standard; the contribution is the exact model-specific two-part threshold and its asymptotic topology dependence.

## Limitations

These deterministic fractions are not an exact finite binary-state stochastic adoption process. The star result has one hub and \(n\) leaves and says nothing about random scale-free ensembles without additional work. No quantitative basin volumes, global outcome probabilities, robustness to edge-weight asymmetry or behavior under time-varying awareness \(d(t)\) are proved. The exact threshold depends on the **unnormalized** interaction sum and would change if each node averaged neighbors rather than summing their powers. The balanced-graph scalar fold and the fact that heterogeneity challenges degree averaging are familiar phenomena; only the explicit bipartite and star classification for the stated node-level equation is claimed. Literature comparisons are bounded; independent historical-priority and scientific review have not been performed.

## References

1. A. Ariwayo, B. Morsky and M. Asllani, *Collective action through adaptive awareness*, arXiv:2607.05608v1, first posted 2026-07-06, https://arxiv.org/abs/2607.05608. Equations (1)–(2), Figure 1 and Appendices A–C.
2. H. Chiba-Okabe and J. B. Plotkin, *Social learning with complex contagion*, PNAS 121 (2024), e2414291121; arXiv:2406.14922, https://arxiv.org/abs/2406.14922. Different power-exposure, payoff-biased imitation model.
3. E. Cator and P. Van Mieghem, *Susceptible-infected-susceptible epidemics on the complete graph and the star graph: Exact analysis*, Phys. Rev. E 87 (2013), 012811, https://doi.org/10.1103/PhysRevE.87.012811. Finite-state stochastic SIS, not the present deterministic nonlinear network ODE.
4. J. P. de Arruda and collaborators, *Influential groups for seeding and sustaining nonlinear contagion in heterogeneous hypergraphs*, Communications Physics 5 (2022), https://www.nature.com/articles/s42005-021-00788-w. Group-based hypergraph contagion rather than neighborwise power response.
