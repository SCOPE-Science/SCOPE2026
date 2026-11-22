# Three habitat types are sharp for isolated coexistence multiplicity under separable colonization

## Finding

In the two-species competitive patch-occupancy model below, with both colonization matrices **strictly positive and rank one**, at most one **isolated** strictly positive coexistence equilibrium can occur if the landscape has one or two habitat types. The qualification “isolated” is essential: degenerate choices may support a continuum of positive equilibria. With three habitat types, two isolated strictly interior coexistence equilibria can coexist. An exact positive rational model exhibits one hyperbolic sink and one hyperbolic saddle; both equilibria persist under small perturbations that preserve the rank-one, strictly positive structure. Thus three is the sharp minimum number of habitat types for multiple isolated coexistence states in this colonization class.

## Assumptions and scope

Let \(n\geq1\). Positive type masses \(p_i\) satisfy \(\sum_{i=1}^n p_i=1\), local extinction rates \(\tau_i,\sigma_i\) are positive, and the two colonization matrices have independent strictly positive rank-one factorizations \(C_{ij}=a_i b_j\) and \(\Gamma_{ij}=c_i d_j\), with every factor positive. For \(i=1,\ldots,n\), write \(u_i,v_i\) for the fractions of all patches occupied by species one and two in habitat type \(i\). The physical state space is \(u_i,v_i\geq0\), \(u_i+v_i\leq p_i\). The dynamics are

\[
\begin{aligned}
\dot u_i&=-\tau_i u_i+(p_i-u_i-v_i)\sum_{j=1}^n C_{ij}u_j,\\
\dot v_i&=-\sigma_i v_i+(p_i-u_i-v_i)\sum_{j=1}^n\Gamma_{ij}v_j.
\end{aligned}
\]

“Strictly positive coexistence equilibrium” means \(u_i>0\), \(v_i>0\), and \(p_i-u_i-v_i>0\) for every habitat type. “Isolated” refers to the equilibrium set in the interior of this finite-dimensional state space, rather than to local dynamical stability.

## Proof

**Rank-one scalar reduction.** Define \(U=\sum_j b_ju_j\), \(V=\sum_jd_jv_j\), \(h_i=a_i/\tau_i\), \(k_i=c_i/\sigma_i\), \(\alpha_i=p_i b_ih_i\), and \(\beta_i=p_id_ik_i\). At any positive coexistence equilibrium \(U,V>0\), with \(z_i=1+h_iU+k_iV\),

\[
u_i=\frac{p_ih_iU}{z_i},\qquad v_i=\frac{p_ik_iV}{z_i},\qquad
\sum_{i=1}^n\frac{\alpha_i}{z_i}=1=\sum_{i=1}^n\frac{\beta_i}{z_i}.
\]

Conversely, every positive solution \((U,V)\) of the two consistency equations defines a strictly interior coexistence equilibrium by these formulas. The two parameterizations are one-to-one because \(U\) and \(V\) are recovered as the corresponding weighted totals.

**One or two habitat types.** With two habitat types, set \(w_i=1/z_i\). If the two vectors \(\alpha\) and \(\beta\) are linearly independent, the consistency equations constitute an invertible linear system for \((w_1,w_2)\), fixing both denominators. If the two vectors \((h_1,k_1)\) and \((h_2,k_2)\) are independent, they in turn fix \((U,V)\) uniquely. If those vectors are dependent, any positive solution extends locally along their common null direction to a positive one-parameter family of equilibria and therefore is not isolated. If instead \(\alpha\) and \(\beta\) are linearly dependent, a positive solution requires \(\alpha=\beta\), since both scalar sums equal one. Then there is just one equation

\[
\sum_{i=1}^2\frac{\alpha_i}{1+h_iU+k_iV}=1.
\]

Its partial derivatives with respect to both \(U\) and \(V\) are strictly negative, so the implicit-function theorem makes every positive solution part of a local nontrivial curve. Thus two distinct isolated positive equilibria are impossible. With one habitat type the same last argument applies: if coexistence is possible, its scalar consistency equation has a positive-dimensional solution family.

**Three-habitat construction.** Let all masses be \(p_i=1/3\), all extinction rates \(\tau_i=\sigma_i=1\), and let

\[
C=\begin{pmatrix}
297/40&12&297/80\\
297/80&6&297/160\\
297/20&24&297/40
\end{pmatrix},\qquad
\Gamma=\begin{pmatrix}
99/20&32&99/10\\
99/80&8&99/40\\
99/40&16&99/20
\end{pmatrix}.
\]

Both matrices have strictly positive entries and rank one. This is explicit from \(h=(2,1,4)\), \(k=(4,1,2)\), \(\alpha=(99/40,2,99/40)\), \(\beta=(33/20,8/3,33/20)\), and the formulas \(C_{ij}=3h_i\alpha_j/h_j\), \(\Gamma_{ij}=3k_i\beta_j/k_j\). The scalar consistency equations become

\[
\begin{aligned}
\frac{99}{40}\left(\frac{1}{1+2U+4V}+\frac{1}{1+4U+2V}\right)+\frac{2}{1+U+V}&=1,\\
\frac{33}{20}\left(\frac{1}{1+2U+4V}+\frac{1}{1+4U+2V}\right)+\frac{8/3}{1+U+V}&=1.
\end{aligned}
\]

These two linear equations in the displayed sum and reciprocal yield \(1/(1+U+V)=1/4\), hence \(U+V=3\), and

\[
\frac{1}{1+2U+4V}+\frac{1}{1+4U+2V}=\frac{20}{99}.
\]

Upon eliminating \(V=3-U\), the last equation is exactly \((U-1)(U-2)=0\). Thus there are **exactly two**, not just at least two, strictly positive coexistence equilibria, corresponding to \((U,V)=(1,2)\) and \((2,1)\):

\[
\begin{array}{c|cc}
& (u_1,u_2,u_3)&(v_1,v_2,v_3)\\\hline
E_1&(2/33,1/12,4/27)&(8/33,1/6,4/27)\\
E_2&(4/27,1/6,8/33)&(4/27,1/12,2/33)
\end{array}
\]

Every listed component is strictly positive, and the combined occupancy in each type is strictly below \(1/3\). These equilibria are isolated by the explicit scalar equation.

**Exact hyperbolicity and robustness.** The characteristic polynomials of the full six-dimensional Jacobians at these two states are

\[
\chi_{E_1}(\lambda)=\frac{(\lambda+1)^2}{60}\left(60\lambda^4+1380\lambda^3+9679\lambda^2+19218\lambda+80\right),
\]

\[
\chi_{E_2}(\lambda)=\frac{(\lambda+1)^2}{15}\left(15\lambda^4+345\lambda^3+2424\lambda^2+4838\lambda-20\right).
\]

For a quartic \(a\lambda^4+b\lambda^3+c\lambda^2+d\lambda+e\), the strict Hurwitz conditions are positivity of the coefficients, \(bc-ad>0\) and \(bcd-ad^2-b^2e>0\). At \(E_1\), these two determinants are \(12,203,940\) and \(234,382,966,920\), and all coefficients are positive, so \(E_1\) is a hyperbolic sink. At \(E_2\), the corresponding determinants are \(763,710\) and \(3,697,209,480\), with the first four coefficients positive and \(e=-20\). The Routh first-column signs are \(+,+,+,+,-\), so exactly one quartic eigenvalue has positive real part and the other three have negative real parts. Therefore \(E_2\) is a hyperbolic saddle with one unstable direction. The full Jacobian determinants are respectively \(4/3\) and \(-4/3\), so both equilibria continue by the implicit-function theorem for every sufficiently small positive perturbation of the prescribed rank-one factors, capacities and extinction rates.

## Verification

The standalone Python/SymPy checker `verify.py` reconstructs both rank-one matrices, both equilibria, every exact stationary residual, the scalar polynomial identity, the full symbolic Jacobians, characteristic polynomials, Routh determinant values, and the strict physical inequalities. Execute `python verify.py` with SymPy installed. Its checks are exact-rational symbolic computations; no finite sampling is substituted for the general one/two-type proof or the exact three-type equilibrium census. The mathematical proof of the general bound and all-state exclusion is above.

## Relationship to prior work

Costa, Kubasch and Loeuille (2026) formulate the competing metacommunity occupancy equations, analyze extinction and persistence, and study the two-habitat finite reduction. The new statement concerns a different structural restriction: independent, strictly positive separable colonization kernels and the **minimum habitat-type number allowing multiple isolated positive coexistence equilibria**. The source's persistence criteria do not imply this equilibrium-multiplicity threshold or the rational three-type sink/saddle construction. Existing uniqueness theorems for competitive strains sharing an *aligned common* rank-one contact kernel impose a stronger common-contact assumption not satisfied by the two independent matrices here. Related two-strain network SIS analyses restrict contact structure or model dynamics differently; they do not provide the exact two-versus-three-habitat classification. The source article, relevant related literature, and searchable research records were compared by mathematical statements and hypotheses; unindexed historical analogues cannot be excluded.

## Limitations

The theorem proves a **local equilibrium** multiplicity threshold and a robust example, not a global bound on the number of coexistence equilibria for arbitrary three-or-more habitat systems. The constructed three-type dynamics have one sink and one saddle, not two attracting positive coexistence equilibria. Other equilibria on boundary faces are not classified. A continuum of positive equilibria is permitted for one or two types in special degenerate cases; the result concerns isolated equilibria. The claim is for deterministic occupancy fractions with positive independent rank-one colonization factors, not arbitrary full-rank matrices, stochastic finite patches, or continuous-space ecological dynamics. Independent scientific review has not been performed.

## References

1. Manon Costa, Madeleine Kubasch and Nicolas Loeuille (2026), *Metacommunity persistence on spatially heterogeneous landscapes*, arXiv:2607.11291v1, publicly posted 13 July 2026, https://arxiv.org/abs/2607.11291.
2. *Strictly concave coexistence potential for aligned rank-one competitive bivirus networks* (2026), publicly accessible research finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-strictly-concave-coexistence-potential-for-aligned-rank-one-comp--567a29ac68ce.
