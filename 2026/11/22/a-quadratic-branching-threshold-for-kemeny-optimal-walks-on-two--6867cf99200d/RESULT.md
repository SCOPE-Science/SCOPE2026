# A quadratic branching threshold for Kemeny-optimal walks on two-level trees

## Finding

Let \(T_{k,m}\) be the tree with one root, \(k\ge2\) children of the root, and \(m\ge1\) terminal leaves attached to each child. Put \(N=1+k(m+1)\). Among **all** irreducible, symmetric, entrywise-nonnegative row-stochastic matrices \(P\) whose off-diagonal support is contained in \(T_{k,m}\), the minimizer of
\[
\mathcal K(P)=\sum_{i=2}^{N}\frac{1}{1-\lambda_i(P)}
\]
is unique. Its edge probabilities are constant on root-to-child edges (value \(x\)) and child-to-leaf edges (value \(y\)), where
\[
 a=(m+1)\bigl((k-1)(m+1)+1\bigr),\quad b=k(m+1),
\qquad
 x_0=\frac{\sqrt a}{\sqrt a+m\sqrt b},
\]
\[
\boxed{\quad x=\min\{k^{-1},x_0\},\qquad y=(1-x)/m.\quad}
\]
The root is assigned a **strictly positive holding probability** if and only if
\[
\boxed{\quad m\ge k^2-3k+4.\quad}
\]
At every child the holding probability is zero; at every terminal leaf it is \(1-y>0\). The root holds with probability \(1-kx\).

The exact minimum, with \(A=ka\) and \(B=km^2b\), is
\[
\boxed{\mathcal K_*=\frac1N\begin{cases}
 kA+\dfrac{kB}{k-1}, &m<k^2-3k+4,\\[3pt]
 (\sqrt A+\sqrt B)^2, &m\ge k^2-3k+4.
\end{cases}}
\]
The integer threshold is strict: no integral parameter lies exactly at the stationary/boundary transition.

The quadratic scale is sharp. If \(k\to\infty\) with \(m/k^2\to\rho\in(0,\infty)\), then the optimal root holding probability obeys
\[
\boxed{\quad P_{rr}^*\longrightarrow (1-\rho^{-1/2})_+.\quad}
\]
For each fixed \(k\), as \(m\to\infty\),
\[
 x\sim\sqrt{\frac{k-1}{k}}\,m^{-1/2},\qquad y\sim m^{-1},\qquad
\mathcal K_*\sim k m^2.
\]
The feasible equal-edge walk with every edge probability \(1/(m+1)\), for sufficiently large \(m\), has a limiting excess factor
\[
\boxed{\quad\frac{\mathcal K_{\mathrm{equal}}}{\mathcal K_*}\longrightarrow 2-\frac1k.\quad}
\]

## Assumptions and scope

All matrices are real, symmetric, stochastic, irreducible and supported on the **fixed** tree, with diagonal holding allowed. No symmetry is imposed on individual edge probabilities. The stationary distribution is necessarily uniform. The objective uses the zero-target Kemeny convention, omitting an optional additive constant of one used in some references. In particular, periodic feasible chains are permitted. The tree has exactly \(k\) identical depth-one branches, each containing exactly \(m\) leaves, and the parameters are integers in the stated ranges. No conclusion is made for nonuniform stationary distributions, directed walks, unequal branch sizes, or other trees.

## Proof

**1. Tree resistance formula and unrestricted uniqueness.** Set \(L=I-P\), with positive off-diagonal transition probabilities represented as conductances \(w_e\) on the fixed tree. The stationary constraint is equivalently
\[
\sum_{e\ni v}w_e\le1\quad\text{for every vertex }v,
\]
with the unused row mass forming \(P_{vv}\). If an edge had zero weight, the unique path across it would be disconnected, contrary to irreducibility. For a connected weighted tree, each pair's effective resistance is the sum of reciprocal edge conductances along its unique path. With \(s_e\) vertices on one side of the cut made by removing edge \(e\), the standard Kirchhoff-index identity therefore gives
\[
\mathcal K(P)=\operatorname{tr}L^+=\frac1N\sum_e\frac{s_e(N-s_e)}{w_e}.
\]
All coefficients are positive, making this objective strictly convex in the independent positive \(w_e\). Since an objective sublevel set stays away from zero weights and lies inside the compact row-capacity polytope, a unique minimizer exists. Every automorphism preserves that objective and feasible set, so uniqueness forces common weights within each of the two edge orbits. This proves global uniqueness among *unrestricted*, not merely orbit-invariant, designs.

**2. Reduction to a one-dimensional constrained minimum.** A root-to-child edge separates \(m+1\) vertices from \(N-(m+1)\), and a leaf edge separates one vertex from \(N-1\). Their cut products are \(a\) and \(b\) as displayed above. There are \(k\) root edges and \(km\) leaf edges. Thus
\[
N\mathcal K=\frac{ka}{x}+\frac{kmb}{y}.
\]
Root feasibility is \(kx\le1\), and branch feasibility is \(x+my\le1\). For fixed \(x>0\), the objective strictly decreases with \(y\), so every branch must satisfy \(x+my=1\). Hence \(y=(1-x)/m\), while \(0<x\le1/k\). Writing \(A=ka\), \(B=km^2b\), the remaining objective is
\[
N\mathcal K=\frac A x+\frac B{1-x}.
\]
Its second derivative is \(2A/x^3+2B/(1-x)^3>0\), and its unconstrained critical point is \(x_0=\sqrt A/(\sqrt A+\sqrt B)\), yielding \(x=\min\{1/k,x_0\}\). Evaluating at these two alternatives yields the minimum formula. The terminal leaves hold since \(0<y<1\); the branch vertices never hold.

**3. Exact integer cutoff.** Root holding is strictly positive exactly when \(x_0<1/k\), or equivalently
\[
(k-1)^2a<m^2b.
\]
After cancelling the positive factor \(m+1\), this says
\[
F_k(m):=km^2-(k-1)^2((k-1)m+k)>0.
\]
For each \(k\ge2\), this upward quadratic has exactly one positive root, because its constant term is negative. At the integer \(t=k^2-3k+4\), direct polynomial expansion gives the **exact identities**
\[
F_k(t)=4,\qquad F_k(t-1)=3-kt<0.
\]
Consequently that sole positive root is strictly between \(t-1\) and \(t\). Since \(m\) is an integer, \(F_k(m)>0\) holds precisely when \(m\ge t\). This proves both the sharp cutoff and strictness at the first active integer.

**4. Two limits.** The scalar optimizer can be rewritten as
\[
x_0=\left(1+\frac{m\sqrt k}{\sqrt{(k-1)(m+1)+1}}\right)^{-1}.
\]
If \(m/k^2\to\rho>0\), then \(k x_0\to\rho^{-1/2}\); hence \(kx\to\min\{1,\rho^{-1/2}\}\) and \(P_{rr}^*=1-kx\to(1-\rho^{-1/2})_+\). For fixed \(k\), the same expression gives \(x\sim\sqrt{(k-1)/k}\,m^{-1/2}\) and \(y=(1-x)/m\sim m^{-1}\). From \(A\sim k(k-1)m^2\), \(B\sim k^2m^3\), and \(N\sim km\), the optimal objective is \(\mathcal K_*\sim km^2\). Finally the equal-edge feasible chain has exact objective
\[
\mathcal K_{\mathrm{equal}}=\frac{m+1}{N}(ka+kmb),
\]
which is asymptotic to \((2k-1)m^2\), proving the claimed cost ratio.

## Verification

The included `verify.py` uses only the Python standard library. It checks the cutoff identities and feasibility on a large integer parameter grid, constructs exact tree support, computes \(\operatorname{tr}L^+\) independently by Gauss–Jordan inversion of \(L+\mathbf1\mathbf1^\mathsf T/N\), and compares the result with the cut formula on small graphs. Random independently weighted feasible walks are additional diagnostics, not a substitute for the strict-convexity proof. Run `python3 verify.py` from this directory. The packaged run reported 1,484 passed checks.

## Relationship to prior work

Hunter (2012) discusses the Kemeny constant and its spectral/electrical interpretations. Patel, Agharkar and Bullo (2015; publicly available full text) formulate and convexify fixed-stationary-distribution Kemeny design, but do not give this two-level tree's optimizer or integer root-holding threshold. Zeng (2021) treats natural random walks on weighted trees with stationary distribution proportional to weighted degree, and extremizes over tree shapes with a fixed weight multiset; neither model is this uniform-stationary design with free holding and vertex-capacity constraints. Durastante, Gnazzo and Meini (2026) study fixed-pattern reversible optimization and numerical algorithms, rather than a two-level branching classification. All these observations refer to the cited materials inspected, not to an assertion of exhaustive worldwide priority.

## Limitations

The theorem is an exact family-specific solution, not a closed-form optimizer for arbitrary trees or stationary distributions. The root-holding frontier is a structural boundary for the stated objective, not a universal mixing-time frontier. Finite verifier diagnostics do not prove the infinite family; that proof is given above. Although relevant literature and database records were compared, an equivalent formulation in unindexed material cannot be ruled out without independent specialist review.

## References

1. J. J. Hunter, *The Role of Kemeny's Constant in Properties of Markov Chains*, arXiv:1208.4716 (first publicly posted 2012-08-23). https://arxiv.org/abs/1208.4716
2. R. Patel, P. Agharkar and F. Bullo, *Robotic Surveillance and Markov Chains With Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control 60 (2015), 3156–3167. DOI:10.1109/TAC.2015.2426317. Lawful author full text: https://motion.me.ucsb.edu/pdf/2014b-pab.pdf
3. J. Zeng, *On average hitting time and Kemeny's constant for weighted trees*, arXiv:2109.09249 (first posted 2021-09-19). https://arxiv.org/abs/2109.09249
4. F. Durastante, M. Gnazzo and B. Meini, *Kemeny’s constant minimization for reversible Markov chains via structure-preserving perturbations*, BIT Numerical Mathematics 66 (2026), article 59. https://doi.org/10.1007/s10543-026-01152-6
