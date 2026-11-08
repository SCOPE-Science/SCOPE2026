# Sharp ventilation-budget threshold and universal critical decay in a multi-hyperedge aerosol–SIS system

## Finding
A multi-aerosol-class extension of the droplet/aerosol susceptible–infected–susceptible (SIS) mean-field equations has a sharp **global** threshold and a sharp **intervention-budget** threshold. At the least budget that eradicates an otherwise persistent infection, removal is not exponential: the prevalence and every aerosol-class prevalence have explicit, positive, universal \(t^{-1}\) asymptotic coefficients. Their values depend on curvature of the class-contamination laws, not merely on the linear reproduction index.

The key feature is the conjunction of (i) finite heterogeneous aerosol groups with nonlinear contamination saturation, (ii) constrained expenditure on class-dependent environmental removal, and (iii) the full critical-time asymptotic—not a claim that square-root resource allocation or generic center-manifold theory is new.

## Assumptions and scope
For \(m\ge1\), consider \((x,y_1,\dots,y_m)\in[0,1]^{m+1}\):
\[
\begin{aligned}
\dot x&=\left(d x+\sum_{i=1}^m b_i y_i\right)(1-x)-\gamma x,\\
\dot y_i&=h_i(x)(1-y_i)-\delta_i y_i.
\end{aligned}
\tag{1}
\]
Assume \(d\ge0\), \(b_i>0\), \(\gamma>0\), \(\delta_i>0\). The class-contamination laws \(h_i:[0,1]\to[0,\infty)\) are \(C^3\), nondecreasing, concave, satisfy \(h_i(0)=0\), and have \(q_i=h_i'(0)>0\). This includes \(h_i(x)=\sigma_i\arctan(s_i x)\), with distinct hyperedge sizes \(s_i\ge3\). The cube is forward invariant: at zero each coordinate has nonnegative derivative and at one each has negative derivative.

Set
\[
 a_i=\frac{b_iq_i}{\gamma},\qquad
 \mathcal R(\boldsymbol\delta)=\frac d\gamma+\sum_{i=1}^m\frac{a_i}{\delta_i}.
\tag{2}
\]
Here \(\mathcal R\) is the linear invasion **threshold index**, not a separate probabilistic interpretation for secondary-case counts.

A ventilation intervention chooses \(\delta_i\ge d_i>0\) under a weighted increment budget \(\sum_{i=1}^m c_i(\delta_i-d_i)\le B\), \(c_i>0\), \(B\ge0\). Distinguish the *uncontrolled* baseline rates \(d_i\) from the direct-droplet coefficient \(d\).

## Proof
**1. Exact equilibrium and global threshold.** The Jacobian at the disease-free state is the irreducible Metzler arrowhead matrix
\[
 A=\begin{pmatrix}
 d-\gamma & b_1&\cdots&b_m\\
 q_1&-\delta_1& &0\\
 \vdots&&\ddots&\\
 q_m&0&&-\delta_m
 \end{pmatrix}.
\tag{3}
\]
Its spectral bound has the sign of \(\mathcal R-1\): for real \(\lambda\ge0\), the Schur equation \(\lambda+\gamma-d-\sum_i b_iq_i/(\lambda+\delta_i)=0\) is strictly increasing and has a nonnegative root exactly when \(\mathcal R\ge1\). The irreducible Metzler Perron eigenvalue is real and algebraically simple. If \(\mathcal R<1\), the nonlinear system is bounded above componentwise by \(\dot z=Az\), as \(h_i(x)\le q_i x\). Because \(A\) is Hurwitz, every state decays exponentially.

When \(\mathcal R=1\), let \(\ell=(1,b_1/\delta_1,\ldots,b_m/\delta_m)\) and \(V=\ell\cdot z\). Then \(\ell^TA=0\) and
\[
 \dot V=-x\left(d x+\sum_i b_i y_i\right)
 +\sum_i\frac{b_i}{\delta_i}\left(h_i(x)-q_i x-h_i(x)y_i\right)\le0.
\tag{4}
\]
The largest invariant subset of \(\{\dot V=0\}\) is the origin: if \(x=0\) but some \(y_i>0\), then \(\dot x=\sum_i b_i y_i>0\); if \(x>0\), every aerosol compartment becomes positive immediately, forcing a strict negative term in (4). LaSalle on the invariant compact cube gives global disease-free convergence.

For \(\mathcal R>1\), any equilibrium with \(x>0\) has \(y_i=H_i(x)=h_i(x)/(\delta_i+h_i(x))\), and solves
\[
 (1-x)\left[d+\sum_i b_i\frac{H_i(x)}{x}\right]=\gamma.
\tag{5}
\]
Each \(H_i(x)/x\) strictly decreases on \((0,1]\): concavity makes \(h_i(x)/x\) nonincreasing, while the factor \(\delta_i/(\delta_i+h_i(x))\) makes the decrease strict. The left side of (5) decreases from \(\gamma\mathcal R>\gamma\) to zero, hence has exactly one root \(x_*\in(0,1)\), giving a unique positive equilibrium \(z_*\).

The vector field is cooperative. For every \(0<\epsilon<1\), concavity and equilibrium identities show that \(\epsilon z_*\) is a strict componentwise subsolution, whereas \(\mathbf1\) is a strict supersolution. Their trajectories increase and decrease, respectively, and converge by monotonicity to equilibria; uniqueness makes both limits \(z_*\). Any nonzero initial condition becomes strictly positive after positive time and lies between a sufficiently small \(\epsilon z_*\) and \(\mathbf1\). Order comparison proves attraction to \(z_*\) from every nonzero state.

**2. Unique optimal environmental allocation.** For \(B>0\), minimize \(\mathcal R\) over the feasible recovery rates. Every term \(a_i/\delta_i\) is strictly convex and strictly decreasing. The full budget must be spent. The Karush–Kuhn–Tucker equations give
\[
 \delta_i^*(B)=\max\left\{d_i,\sqrt{\frac{a_i}{\lambda_B c_i}}\right\},\quad
 \sum_i c_i\bigl(\delta_i^*(B)-d_i\bigr)=B.
\tag{6}
\]
The right budget expression is continuous and strictly decreasing in \(\lambda_B\) on the positive-expenditure branch, from infinity to zero; therefore \(\lambda_B\) is unique. Strict convexity proves the unique minimizer. The minimum \(\mathcal R_{\min}(B)\) is continuous and strictly decreasing, from its baseline value to \(d/\gamma\) as \(B\to\infty\). Thus if \(\mathcal R_{\min}(0)>1\) and \(d<\gamma\), there is a unique finite \(B_*>0\) with \(\mathcal R_{\min}(B_*)=1\). Below it every feasible intervention leaves a globally attracting endemic state; at and above it the optimally controlled system eradicates globally, exponentially only above it. If \(d\ge\gamma\), no finite aerosol-only budget reaches \(\mathcal R\le1\). For \(B=0\), the unique feasible allocation is the baseline. Once all floor constraints are inactive,
\[
 \mathcal R_{\min}(B)=\frac d\gamma+
 \frac{(\sum_i\sqrt{a_ic_i})^2}{B+\sum_i c_i d_i}.
\tag{7}
\]
This ordinary inverse-rate convex optimization is not claimed as an original general-purpose technique.

**3. Universal algebraic critical profile.** At any rates satisfying \(\mathcal R=1\), define
\[
 p_i=\frac{q_i}{\delta_i},\quad
 C=1+\sum_i\frac{b_iq_i}{\delta_i^2},\quad
 \Lambda=\gamma+\sum_i\frac{b_i}{\delta_i}
 \left(\frac{q_i^2}{\delta_i}-\frac{h_i''(0)}{2}\right)>0.
\tag{8}
\]
Then \(v=(1,p_1,\ldots,p_m)^T\) satisfies \(Av=0\), \(\ell\cdot v=C\), and every other eigenvalue of \(A\) has negative real part. The nonlinear remainder \(Q(z)=F(z)-Az\) is quadratic, and direct Taylor expansion gives
\[
 \ell\cdot Q(xv)=-\Lambda x^2+O(x^3).
\tag{9}
\]
By part 1 every nonzero trajectory approaches the origin. Decompose its state as \(z=(V/C)v+w\) with \(\ell\cdot w=0\). Exponential stability of \(A\) on this invariant complementary subspace and \(Q(z)=O(\lVert z\rVert^2)\) give \(w=o(V)\) as \(t\to\infty\). To exclude an orbit lying entirely in a fast stable leaf, observe that positivity of \(\ell\), the compact cube, and quadratic nonlinearity give \(\dot V\ge-KV^2\) for some constant \(K>0\), whence \(V(t)\ge [V(0)^{-1}+Kt]^{-1}\). Thus \(V\) cannot decay exponentially and the stable spectral component is asymptotically smaller. Inserting \(z=(V/C)v+o(V)\) into (9) yields
\[
 \dot V=-\frac{\Lambda}{C^2}V^2+o(V^2),\qquad
 \lim_{t\to\infty}tV(t)=\frac{C^2}{\Lambda}.
\tag{10}
\]
Consequently for every nonzero state of the cube,
\[
 \boxed{\lim_{t\to\infty}t x(t)=\frac C\Lambda,\qquad
 \lim_{t\to\infty}t y_i(t)=\frac{q_i}{\delta_i}\frac C\Lambda.}
\tag{11}
\]
The first-order spectral splitting statement also follows directly from the variation-of-constants formula for the stable projection; no finite simulation is being used as a proof of the infinite-time limit.

**4. Exact two-class threshold illustration.** Choose two hyperedge sizes \(s_1=3,s_2=6\),
\[
 d=\frac15,\quad\gamma=1,\quad b_1=b_2=\frac15,\quad
 h_i(x)=\frac23\arctan(s_i x),\quad d_1=d_2=c_1=c_2=1.
\]
Then \((q_1,q_2)=(2,4)\), \((a_1,a_2)=(2/5,4/5)\), the uncontrolled index equals \(7/5\), and the budget critical point is
\[
 \boxed{B_*=\sqrt2-\tfrac12,\quad
 \delta_1^*=\tfrac{1+\sqrt2}{2},\quad
 \delta_2^*=1+\tfrac1{\sqrt2}.}
\tag{12}
\]
Both class floors are inactive at criticality. Put \(\lambda=\tfrac85(3-2\sqrt2)\); here \(C=1+2\lambda\), \(\Lambda=1+6\lambda\), so
\[
 \boxed{\lim_{t\to\infty}t x(t)=
 \frac{1753+320\sqrt2}{3769}=0.585181305375\ldots.}
\tag{13}
\]
The limits for each \(y_i\) follow by multiplying (13) by \(q_i/\delta_i^*\). For \(0<B\le\sqrt2-1\), only the larger hyperedge class receives a ventilation increment; above that budget both are improved.

## Verification
The attached `CHECK.py` checks the exact radical equalities for (12)–(13), verifies the critical arrowhead Jacobian's eigenvalue and the signs of its remaining eigenvalues, compares the KKT allocation with numerical constrained optimization on 80 independently parameterized multi-class examples, and integrates the exact two-class ODE for increasing times up to \(t=50000\). The computed \(t x(t)\) approaches the coefficient in (13). These finite checks are consistency tests; the quantified global statements and the \(t\to\infty\) limit rest on the analytic proof above.

## Relationship to prior work
Nguyen and Porter (2026) introduced the hypergraph droplet/aerosol SIS dynamics and analyzed a single uniform hyperedge-size homogeneous mean-field system; their exploration of nonuniform hyperedge sizes and hyperedge recovery rates is numerical, and Section 5 identifies heterogeneous-size mean-field analysis and different ventilation rates as future work. Equation (1) is an explicitly defined multi-class extension, **not a claim to derive exactly the original stochastic hypergraph process**. Paré et al. (2021) develop broader network–infrastructure epidemic threshold theory, but their analyzed infrastructure models do not supply this bounded nonlinear multi-class closure's combined optimum and critical-profile coefficients. Chen et al. (2017) already use optimal budget allocation and square-root relationships for disease-control rates; equations (6)–(7) instantiate familiar convex optimization rather than claim to invent it. The joint sharp threshold/critical asymptotic for this explicit nonlinear class model is the comparison target. The possibility of an equivalent result embedded in general cooperative-system theory remains open.

## Limitations
The claim applies to finite groups, homogeneous host prevalence, deterministic fractional aerosol states, concave increasing contamination, linear expenditure in recovery rates, and globally unlimited incremental recovery. It does not imply global results for heterogeneous vertex-level networks, nonconcave dose responses, bounded control ceilings, stochastic extinction times, or time-varying intervention. A value \(B=B_*\) reaches disease-free attraction but never a uniform positive exponential decay rate from generic positive states. Independent scientific audit has not been performed.

## References
1. T. D. Nguyen and M. A. Porter, *A disease-spread model on hypergraphs with distinct droplet and aerosol transmission modes*, arXiv:2601.03563v1, 7 January 2026. https://arxiv.org/abs/2601.03563
2. P. E. Paré et al., *Multi-Layer SIS Model with an Infrastructure Network*, arXiv:2109.09493, 2021. https://arxiv.org/abs/2109.09493
3. X. Chen et al., *Optimal Allocation of Resources for Suppressing Epidemic Spreading on Networks*, arXiv:1702.08444, 2017. https://arxiv.org/abs/1702.08444
