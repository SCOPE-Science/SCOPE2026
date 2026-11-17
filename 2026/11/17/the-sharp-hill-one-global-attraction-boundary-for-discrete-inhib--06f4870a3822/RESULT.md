# The sharp Hill-one global-attraction boundary for discrete inhibitory gene networks

## Finding

For the finite, nonnegative, reciprocally inhibited gene-expression map
\[
F_i(x)=\beta_i x_i+\frac{\alpha_i}{1+\sum_{j=1}^{N}c_{ij}x_j^h},
\]
**the entire nonnegative state space converges to one positive equilibrium whenever \(0<h\le1\)**, independently of network size, topology, and interaction strength. An explicit logarithmic contraction coefficient controls the convergence from every initial state.

This global-attraction boundary is sharp as a statement about all admissible networks and parameters: every real exponent \(h>1\) permits a positive prime-two orbit. In the original two-gene specialization with exponent \(h=2\), a simple diagonal prime-two orbit is explicitly attracting for a whole continuum of couplings.

## Assumptions and scope

Let \(N\ge1\) be an integer and let \(0<h\le1\). For all \(i,j\in\{1,\ldots,N\}\), assume \(\alpha_i>0\), \(0\le\beta_i<1\), and \(c_{ij}\ge0\). The initial vector belongs to \([0,\infty)^N\), with arbitrary finite coordinates. Define \(x(k+1)=F(x(k))\). A fixed point means \(F(x^*)=x^*\); global attraction means attraction from every such initial vector, not an assertion of a uniform rate independent of its magnitude.

Fix any upper bounds
\[
U_i\ge\max\left\{x_i(0),\frac{\alpha_i}{1-\beta_i}\right\},\qquad
D_i=1+\sum_jc_{ij}U_j^h,\qquad L_i=\frac{\alpha_i}{D_i},
\]
and put
\[
\delta=\min_i\frac{\alpha_i}{D_i^2(\beta_i U_i+\alpha_i)},
\qquad q=1-\delta.
\]
Then \(0<\delta\le1\), so \(0\le q<1\), and the explicit estimate is
\[
\|\log x(k)-\log x^*\|_\infty\le
q^{k-1}\|\log x(1)-\log x^*\|_\infty\quad(k\ge1).
\]
Logarithms act coordinatewise; all arguments of them are strictly positive.

## Proof

**1. Strict entry and an invariant box.** Positivity of every \(\alpha_i\) gives \(F_i(x)>0\) for all \(x\ge0\). For any \(x\in[0,U]\), the denominator lies between \(1\) and \(D_i\). Thus
\[
L_i\le F_i(x)\le\beta_iU_i+\alpha_i\le U_i.
\]
Since \(0<L_i\le U_i\), the box \(K=\prod_i[L_i,U_i]\) is nonempty, positively invariant, and contains \(x(1)\). Notice that no invertibility, symmetry, irreducibility, or connectivity is assumed.

**2. Logarithmic contraction.** Let \(z_i=\log x_i\) and \(G_i(z)=\log F_i(e^z)\) on the convex log-box \(\log K\). Write \(S_i=\sum_jc_{ij}x_j^h\). Direct differentiation gives
\[
\frac{\partial G_i}{\partial z_j}
=\frac{\beta_i x_i\mathbf1_{i=j}-\alpha_i h c_{ij}x_j^h/(1+S_i)^2}
{\beta_i x_i+\alpha_i/(1+S_i)}.
\]
By the triangle inequality, its absolute row sum is bounded by
\[
\sum_j\left|\frac{\partial G_i}{\partial z_j}\right|
\le\frac{\beta_i x_i+\alpha_i hS_i/(1+S_i)^2}
{\beta_i x_i+\alpha_i/(1+S_i)}
=1-\frac{\alpha_i[1+(1-h)S_i]}
{(1+S_i)^2F_i(x)}.
\]
The crucial point is \(1-h\ge0\). Since \(0\le S_i\le D_i-1\) and \(F_i(x)\le\beta_i U_i+\alpha_i\), the final deficit is at least \(\alpha_i/[D_i^2(\beta_i U_i+\alpha_i)]\ge\delta\). Consequently the supremum matrix norm of \(DG(z)\) is at most \(q<1\) everywhere on the log-box. The segment mean-value inequality gives
\[
\|G(z)-G(w)\|_\infty\le q\|z-w\|_\infty
\qquad(z,w\in\log K).
\]

**3. Fixed point, global attraction, and uniqueness.** The logarithmic box is complete and \(G\) maps it into itself. The contraction mapping theorem supplies a unique positive fixed point \(x^*\in K\), and iteration from \(x(1)\) gives the stated estimate. Any other nonnegative fixed point \(y\) must be strictly positive, and obeys
\[
 (1-\beta_i)y_i=\frac{\alpha_i}{1+\sum_jc_{ij}y_j^h},
\qquad 0<y_i\le\frac{\alpha_i}{1-\beta_i}\le U_i.
\]
Therefore \(y\in K\), by the lower bound in Step 1, and uniqueness in \(K\) forces \(y=x^*\). Coordinatewise convergence is exponential because \(\exp\) is Lipschitz on the fixed compact log-box. Thus there are no nontrivial positive cycles or other forward recurrence for \(0<h\le1\).

**4. Sharpness for every exponent above one.** Fix any real \(h>1\) and consider the scalar map
\[
f(x)=\frac{\alpha}{1+x^h},\qquad x\ge0,
\qquad \alpha>\frac{h}{(h-1)^{1+1/h}}.
\]
Its positive fixed point \(t\) is the unique solution of \(\alpha=t(1+t^h)\). The displayed strict condition gives \(t^h>1/(h-1)\), and hence
\[
f'(t)=-\frac{h t^h}{1+t^h}<-1.
\]
Set \(H(x)=f(f(x))-x\). Then \(H(0)=f(\alpha)>0\), \(H(t)=0\), and \(H'(t)=f'(t)^2-1>0\). Thus \(H(x)<0\) for some \(x<t\) sufficiently close to \(t\); continuity produces \(p\in(0,t)\) with \(H(p)=0\). Strict decrease of \(f\) gives \(q_2=f(p)>t\), and \(f(q_2)=p\): a positive prime-two orbit. This disproves parameter-uniform global attraction for every \(h>1\) (without claiming that every network above that threshold oscillates).

**5. An attracting two-gene dimer cycle.** In the symmetric two-gene Andrecut–Kauffman map, let \(h=2\), \(\alpha_1=\alpha_2=a>2\), \(\beta_1=\beta_2=0\), and
\[
 C_\varepsilon=\begin{pmatrix}1-\varepsilon&\varepsilon\\\varepsilon&1-\varepsilon\end{pmatrix},\quad 0\le\varepsilon\le1.
\]
The diagonal \(x=y\) is invariant and there the map is \(f_a(s)=a/(1+s^2)\). Put \(r_\pm=(a\pm\sqrt{a^2-4})/2\). The identities \(r_-r_+=1\) and \(r_-+r_+=a\) give \(f_a(r_-)=r_+\), \(f_a(r_+)=r_-\). At a diagonal point \((s,s)\), the Jacobian equals \(f_a'(s)C_\varepsilon\). Therefore the two-step derivative has eigenvalues
\[
\frac4{a^2},\qquad\frac{4(1-2\varepsilon)^2}{a^2},
\]
both strictly inside the unit disk for every \(a>2\) and \(\varepsilon\in[0,1]\). The orbit is hyperbolically attracting in the full two-dimensional model. At each fixed \(a>2\) and coupling \(\varepsilon\), it persists (still attracting) under a sufficiently small positive common \(\beta\) by the implicit-function theorem applied to the second iterate.

## Verification

The accompanying standalone `verify.py` uses SymPy to check the exact logarithmic Jacobian gap, the two-cycle formulas, the scalar critical multiplier, and the two-step multiplier identity. It also iterates three heterogeneous networks with twelve initial states as finite consistency checks. Its output on the provided package is

`VERIFY_OK log_jacobian_gap=1 exact_two_cycle=4 scalar_threshold=1 network_cases=3 initial_states=12 two_gene_attractor=1`

The infinite-dimensional quantifiers over all finite network sizes, real exponents, and parameters are established by the preceding proof, not by numerical sampling. No externally independent certification is claimed.

## Relationship to prior work

The motivating discrete two-gene map, including the exponent \(h\), appears in Andrecut and Kauffman's work and in the 2026 topological–numerical analysis of Falęcki, Rosman, Palczewski, Pilarczyk, and Bartłomiejczyk. Their 2026 analysis uses \(h=3\) and selected parameter boxes. Rosman and collaborators' earlier full-text study gives an absorbing-box proposition for all positive integer exponents and investigates \(h=3,4\) numerically. Neunhäuserer's 2025 full article proves topological chaos for higher cooperativity and describes the lower-exponent regime as apparently nonchaotic, rather than proving the global contraction theorem. Subramani and collaborators' 2023 analysis also focuses on bifurcation and numerical behavior, with a separate fractional extension.

The new mathematical claim is the **uniform-over-parameters sharp Hill-exponent division for global attraction**, with a quantitative contraction bound for arbitrarily many asymmetric inhibitory genes and a full two-dimensional attracting dimer counterexample. Ordinary contraction mapping and scalar flip mechanisms are classical, and are not themselves claimed as new. The 2007 foundational paper was not inspectable in full text, so definitive priority is unresolved.

## Limitations

The conclusion applies to the specified discrete positive reciprocal-Hill map, with additive nonnegative inhibition, positive synthesis, survival factors smaller than one, and finite \(N\). It does not cover activator terms, negative interaction coefficients, variable or delayed coefficients, noisy dynamics, or continuous-time differential equations. The per-trajectory rate depends on a priori bounds that can depend on the initial state; no global uniform constant independent of initial magnitude is claimed. For \(h>1\), the theorem produces **existence** of a counterexample, not universal oscillation. The linear-feedback-free dimer illustration is the closure \(\beta=0\) of the physically common \(\beta>0\) regime, with persistence proved for small positive \(\beta\).

## References

1. D. Falęcki, M. Rosman, M. Palczewski, P. Pilarczyk, and A. Bartłomiejczyk, “Topological–numerical analysis of global dynamics in the discrete-time two-gene Andrecut–Kauffman model,” arXiv:2603.03850v1, posted 2026-03-04. https://arxiv.org/html/2603.03850
2. M. Rosman, M. Palczewski, P. Pilarczyk, and A. Bartłomiejczyk, “Bistability and chaos in the discrete two-gene Andrecut-Kauffman model,” arXiv:2411.16699v2 (first posted 2024-11-10), *DCDS-B* 30 (2025), 4442–4461. https://arxiv.org/html/2411.16699v2
3. J. Neunhäuserer, “Topological chaos in the two-gene Andrecut-Kauffman model,” arXiv:2509.11881, posted 2025-09-15. https://arxiv.org/abs/2509.11881
4. R. Subramani and collaborators, “The dynamic analysis of discrete fractional-order two-gene map,” *European Physical Journal Special Topics* 232 (2023), 2445–2457. https://doi.org/10.1140/epjs/s11734-023-00912-7
5. M. Andrecut and S. A. Kauffman, “Chaos in a discrete model of a two-gene system,” *Physics Letters A* 367 (2007), 281–287. https://doi.org/10.1016/j.physleta.2007.03.074 (full text not inspected).
