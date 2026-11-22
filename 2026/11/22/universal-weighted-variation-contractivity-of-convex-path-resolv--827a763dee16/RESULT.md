# Universal weighted-variation contractivity of convex path resolvents and flows

## Finding

**Theorem (universal two-input weighted-variation criterion).** Fix an integer \(n\ge2\), positive vertex masses \(m_1,\ldots,m_n\), positive edge weights \(w_1,\ldots,w_{n-1}\), and define \(w_0=w_n=0\). On real vectors let
\[
V_w(h)=\sum_{j=1}^{n-1}w_j|h_{j+1}-h_j|.
\]
For each collection of finite convex functions \(\phi_j:\mathbb R\to\mathbb R\), define the unique proximal minimizer
\[
P_\phi(f)=\underset{u\in\mathbb R^n}{\arg\min}\left\{\frac12\sum_{i=1}^n m_i(u_i-f_i)^2+\sum_{j=1}^{n-1}\phi_j(u_{j+1}-u_j)\right\}.
\]
Let \(S^\phi_t\) be the gradient-flow semigroup of \(\sum_j\phi_j(u_{j+1}-u_j)\) in the Hilbert metric induced by the masses. The following assertions are equivalent:

1. For **every** such collection of finite convex edge energies and **every** pair \(f,g\in\mathbb R^n\),
\[
V_w(P_\phi(f)-P_\phi(g))\le V_w(f-g).
\]
2. For every such collection and all \(t\ge0\),
\[
V_w(S^\phi_t f-S^\phi_t g)\le V_w(f-g).
\]
3. Every edge satisfies the local superharmonicity inequality
\[
\boxed{\frac{w_j-w_{j-1}}{m_j}+\frac{w_j-w_{j+1}}{m_{j+1}}\ge0\qquad(1\le j\le n-1).}
\]

When the masses are equal, (3) is precisely concavity of the weight sequence extended by zero boundary values. Both nonexpansivity bounds are sharp as universal constants: setting all edge energies to zero gives equality. If any single inequality in (3) fails, a quadratic energy supported on that edge gives strict two-input amplification in (1) and (2), with an explicit step-data witness.

## Assumptions and scope

The path is the open chain of \(n\) real coordinates, with differences \((Du)_j=u_{j+1}-u_j\). Masses and variation weights are strictly positive and independent of the coefficients inside the convex edge energies. Each \(\phi_j\) is finite and convex on all of \(\mathbb R\), not necessarily even, differentiable or nonnegative. Additive constants in an edge energy have no effect. The quadratic fidelity makes every proximal minimizer unique. The gradient flow is understood as the unique Hilbert-space subgradient flow, equivalently the limit of implicit-Euler proximal steps. These statements do not assert that each individual fixed penalty requires (3); they characterize contractivity uniformly across **all** choices of penalties.

## Proof

**1. Edge Green matrix.** Let \(D\) be the forward difference matrix, \(M=\operatorname{diag}(m_1,\ldots,m_n)\), and \(B=DM^{-1}D^{\mathsf T}\), an \((n-1)\)-square symmetric positive-definite tridiagonal matrix. Its diagonal and adjacent entries are
\[
B_{jj}=m_j^{-1}+m_{j+1}^{-1},\quad
B_{j,j-1}=-m_j^{-1},\quad
B_{j,j+1}=-m_{j+1}^{-1}.
\]
All other entries vanish. Accordingly
\[
(w^{\mathsf T}B)_j=\frac{w_j-w_{j-1}}{m_j}+\frac{w_j-w_{j+1}}{m_{j+1}}.
\]
Thus (3) is exactly \(w^{\mathsf T}B\ge0\) coordinatewise.

**2. Nonnegative edge resolvents.** For any diagonal \(A=\operatorname{diag}(a_j)\) with \(a_j\ge0\), put \(G=I+BA\). Then \(G\) has nonpositive off-diagonal entries. If all \(a_j>0\), each principal submatrix of \(G\) is similar to a positive-definite matrix \(I+A_I^{1/2}B_{I,I}A_I^{1/2}\). In particular all leading principal minors are positive. Tridiagonal Gaussian elimination gives positive pivots, and its lower and upper bidiagonal factors have nonpositive off-diagonal entries. Their inverses are entrywise nonnegative, so \(G^{-1}\ge0\). Letting positive \(a_j\) tend to zero proves the same for arbitrary nonnegative \(A\). If (3) holds, then
\[
w^{\mathsf T}G=w^{\mathsf T}+(w^{\mathsf T}B)A\ge w^{\mathsf T}.
\]
Multiplying on the right by the nonnegative matrix \(G^{-1}\) yields \(w^{\mathsf T}G^{-1}\le w^{\mathsf T}\). Consequently, for every real edge vector \(d\),
\[
\sum_jw_j|(G^{-1}d)_j|\le w^{\mathsf T}G^{-1}|d|\le\sum_jw_j|d_j|.
\]

**3. All convex proximal maps.** First suppose the \(\phi_j\) are differentiable. For data \(f,g\) write \(u=P_\phi(f)\), \(v=P_\phi(g)\), \(h=f-g\), \(k=u-v\), and \(z=Dk\). Subtracting their optimality equations gives
\[
M(k-h)+D^{\mathsf T}A Dk=0,
\]
where \(A\) is diagonal with nonnegative divided-difference entries
\[
a_j=\frac{\phi_j'((Du)_j)-\phi_j'((Dv)_j)}{(Du)_j-(Dv)_j}
\]
when the denominator is nonzero, and \(a_j=0\) otherwise. Since derivatives of convex functions are monotone, \(A\ge0\); the zero-denominator choice is legitimate because then the numerator also vanishes. Applying \(DM^{-1}\) gives
\[
(I+BA)z=Dh.
\]
Step 2 now proves \(V_w(k)\le V_w(h)\). For any finite convex, possibly nonsmooth \(\phi_j\), approximate it by smooth convex convolutions, uniformly on compact intervals. The strongly convex objectives have bounded minimizers and their minimizers converge under this local uniform approximation, so the inequality passes to the limit.

**4. Nonlinear flows.** In the differentiable smooth case, subtract the two gradient-flow equations. The difference of their edge-gradient vectors again factors through a nonnegative time-dependent diagonal secant matrix \(A(t)\); hence the difference of edge vectors obeys
\[
\dot z(t)=-B A(t)z(t).
\]
This is a cooperative linear equation on edges, with nonnegative off-diagonal evolution and weighted column dissipation \(w^{\mathsf T}[-BA(t)]\le0\). For any such time-dependent coefficient, the weighted \(\ell^1\) norm of \(z(t)\) is nonincreasing, by the upper right Dini derivative of its absolute-value sum (equivalently by positive Euler products). This establishes (2). For nonsmooth finite convex energies, each proximal implicit-Euler step satisfies (1), so its arbitrarily fine time-step limit, the subgradient semigroup, satisfies (2) by continuity. Thus (3) implies both (1) and (2).

**5. Necessary criterion and attainment.** Suppose \((w^{\mathsf T}B)_j<0\) for an edge \(j\). Set \(\phi_j(s)=\tfrac a2s^2\) with \(a>0\) and \(\phi_i\equiv0\) for all other edges. Let \(h\) have precisely one unit upward step across edge \(j\), so \(Dh=e_j\). Its projected difference has edge vector
\[
z=(I+aBe_je_j^{\mathsf T})^{-1}e_j
=e_j-\frac a{1+aB_{jj}}Be_j\ge0,
\]
where nonnegativity follows entry by entry from the tridiagonal signs. Therefore
\[
V_w(P_\phi(h)-P_\phi(0))=w_j-\frac a{1+aB_{jj}}(w^{\mathsf T}B)_j>w_j=V_w(h).
\]
For the corresponding smooth flow, the edge vector equals \(e_j-\frac{1-e^{-aB_{jj}t}}{B_{jj}}Be_j\), so the same strict gain holds for every \(t>0\). Thus either universal contractivity assertion forces (3).

As a concrete rational witness, take four sites with unit masses, weights \((1,\tfrac12,1)\), and unit quadratic energy on the middle edge. A step on that edge has variation \(\tfrac12\), while its output has edge differences \((\tfrac13,\tfrac13,\tfrac13)\) and variation \(\tfrac56\), an amplification factor of \(\tfrac53\). Conversely, weights \((1,\tfrac32,1)\) satisfy (3) with unit masses, so **every** finite convex edge penalty is two-input variation-nonexpansive for that nonconstant weighting.

## Verification

The standalone standard-library program `check.py` checks 126 exact-rational edge resolvents for arbitrary positive masses and the nonconstant positive weights \(w=B^{-1}\mathbf1\), including positivity and all weighted column inequalities. It constructs 504 random exact-rational two-input quartic-proximal instances by specifying the unique minimizers first and recovering their data from optimality, then checks the weighted variation bounds without a numerical optimizer. It also checks the explicit four-site strict counterexample exactly. Run `python check.py` in the extracted package. The universal assertion depends on the preceding proof, not on finite samples.

## Relationship to prior work

Barbero and Sra (2014, arXiv:1411.0589) study computational proximal algorithms for 1D total variation, including weighted variants; their closest results establish a proximal framework rather than the universal two-input weighted-variation inequality. Kolmogorov, Pock and Rolínek (2015, arXiv:1502.07770) develop algorithms for tree-TV minimization with convex unaries, likewise without a stated sharp pairwise stability criterion of this form. The published result *A conductance-independent contraction criterion for weighted tree heat flow in total variation* (2026; reference below) proves the same edge-weight superharmonicity condition on paths for **linear** graph heat, and more general graph topology. That precedent covers the linear heat specialization of the present condition. The current theorem separately establishes, with its divided-difference argument, a universal equivalence for **arbitrary nonlinear convex edge resolvents, nonsmooth TV penalties and their gradient flows**; this nonlinear-uniform claim is not an immediate statement of the cited linear theorem. Prior literature may contain equivalent versions under different vocabulary, so historical priority is not certified.

## Limitations

The result is finite-dimensional, real and specific to open paths; it assumes a diagonal positive fidelity metric and finite separable convex edge potentials. It does not claim the same criterion for graph cycles, branched trees, nonseparable edge interactions, infinite paths, variable vertex masses along time, or perturbation metrics other than weighted first variation. No claim of independent verification is made.

## References

1. Á. Barbero and S. Sra, *Modular proximal optimization for multidimensional total-variation regularization*, arXiv:1411.0589, first submitted 2014-11-03; §2 and algorithmic discussion. https://arxiv.org/abs/1411.0589
2. V. Kolmogorov, T. Pock and M. Rolínek, *Total variation on a tree*, arXiv:1502.07770, first submitted 2015-02-26; §§1, 4. https://arxiv.org/abs/1502.07770
3. *A conductance-independent contraction criterion for weighted tree heat flow in total variation*, 2026-10-26, published mathematical result, especially its path specialization and linear-heat limitation. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-conductance-independent-contraction-criterion-for-weighted-tre--9fedb9294a7c
