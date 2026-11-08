# Two interaction degrees are necessary and sufficient for universal ecological stabilization

## Finding

Fix a positive integer \(n\) and a finite support \(K\subseteq\{2,3,\dots\}\). Let arbitrary intrinsic rates \(r\in\mathbb R^n\) and pairwise interactions \(S\in\mathbb R^{n\times n}\) be prescribed. Allow free real homogeneous higher-order forms \(H_i^{(k)}\) for each \(k\in K\), in
\[
\dot x_i=x_i G_i(x),\qquad G_i(x)=r_i+\sum_{j=1}^n S_{ij}x_j+\sum_{k\in K}H_i^{(k)}(x).
\]
Here \(x\in\mathbb R_{\ge0}^n\), and all forms may contain monomials with repeated partner indices. The following universal completion property is equivalent to \(|K|\ge2\): **for every prescribed pair \((r,S)\), some allowed higher-order forms create a positive, locally asymptotically stable equilibrium**.

In fact, choose any two degrees \(2\le p<q\) in \(K\) and any desired relaxation rate \(\lambda>0\). Using these two degrees alone, an explicit choice stabilizes \(\mathbf1=(1,\ldots,1)\) with full Jacobian \(-\lambda I_n\). Conversely, with \(r_i=-1\) and \(S_{ij}=-1\), any one-degree completion that produces an interior equilibrium forces that equilibrium to be radially repelling, with nearby rays escaping in finite time on the upper side. Hence no single higher-order arity, however large, is universally adequate.

## Assumptions and scope

1. \(n\ge1\), \(K\) is finite, and each permitted degree satisfies \(k\ge2\). Degree \(k\) is polynomial degree in the *per-capita* growth rate, corresponding to an interaction of order \(k+1\) in the standard higher-order Lotka--Volterra convention.
2. The coefficients of \(H_i^{(k)}\) are unrestricted real numbers, independently selectable for each species and degree; repeated-index monomials are allowed. Tensor coefficients may be symmetrized in their partner indices.
3. The growth vector and the pairwise interaction matrix are fixed inputs, not tunable completion variables. A positive equilibrium is \(x_*\in(0,\infty)^n\) with \(G(x_*)=0\). The stability claim is local asymptotic stability in the full population space.
4. No fixed total-population constraint, conservation law, sign pattern, diagonal restriction, or global boundedness condition is imposed on the higher-order coefficients.

## Proof

**Sufficiency for any two distinct degrees.** Fix \(2\le p<q\) and put \(t(x)=n^{-1}\sum_{j=1}^n x_j\). Define homogeneous-degree-supported interpolation polynomials
\[
\phi_0(x)=\frac{q t(x)^p-p t(x)^q}{q-p},
\qquad
\phi_j(x)=x_jt(x)^{p-1}-t(x)^p+\frac{t(x)^q-t(x)^p}{q-p}.
\]
Each polynomial is a sum of a degree-\(p\) form and a degree-\(q\) form. Direct evaluation at \(\mathbf1\), where \(t=1\), yields
\[
\phi_0(\mathbf1)=1,\quad \partial_k\phi_0(\mathbf1)=0,\quad
\phi_j(\mathbf1)=0,\quad \partial_k\phi_j(\mathbf1)=\delta_{jk}.
\]
For clarity, the last identity follows because the derivative of \((x_j-t)t^{p-1}\) is \(\delta_{jk}-1/n\) and the derivative of \((t^q-t^p)/(q-p)\) is \(1/n\), both at \(\mathbf1\).

Let \(b_i=r_i+\sum_j S_{ij}\), and define
\[
H_i(x)=-b_i\phi_0(x)+\sum_{j=1}^n(-\lambda\delta_{ij}-S_{ij})\phi_j(x).
\]
Split \(H_i\) into its homogeneous pieces of degrees \(p\) and \(q\) and set every other permitted piece to zero. Then
\[
G_i(\mathbf1)=b_i+H_i(\mathbf1)=0,
\quad \partial_jG_i(\mathbf1)=S_{ij}+\partial_jH_i(\mathbf1)=-\lambda\delta_{ij}.
\]
Since \(\dot x_i=x_iG_i(x)\), its Jacobian at the positive equilibrium is exactly \(-\lambda I_n\). Linearization proves local exponential stability, for arbitrary \(n,r,S\) and \(\lambda>0\).

**Necessity: empty or singleton support.** Fix the strictly negative ecological baseline
\[
r_i=-1,\qquad S_{ij}=-1\quad(1\le i,j\le n).
\]
If \(K\) is empty, the per-capita rate equals \(-1-\sum_jx_j<0\) throughout the positive cone, so there is no interior equilibrium.

If \(K=\{m\}\) with \(m\ge2\), write the added forms as \(H_i(x)\), each homogeneous of degree \(m\). Suppose \(x_*\in(0,\infty)^n\) is any equilibrium; let \(T=\sum_jx_{*,j}>0\). Equilibrium balance forces \(H_i(x_*)=1+T\) for every \(i\), regardless of the coefficients. Homogeneity gives \(H_i(c x_*)=c^m(1+T)\). Consequently the entire ray \(\{c x_*:c>0\}\) is invariant under the vector field, and its multiplier solves
\[
\dot c=c f(c),\qquad
f(c)=-1-Tc+(1+T)c^m.
\]
Here \(f(0)=-1\), \(f(1)=0\), \(f''(c)=m(m-1)(1+T)c^{m-2}>0\) for \(c>0\), and
\[
f'(1)=m+(m-1)T>0.
\]
Strict convexity places \(f(c)\) below the chord from \((0,-1)\) to \((1,0)\) when \(0<c<1\), hence \(f(c)<0\). For \(c>1\), the strictly increasing derivative and \(f'(1)>0\) imply \(f(c)>0\). Thus trajectories starting at arbitrarily small radial perturbations \(c(0)>1\) move away from the equilibrium, proving Lyapunov instability, regardless of transverse eigenvalues. Moreover \(c f(c)\sim(1+T)c^{m+1}\) as \(c\to\infty\); the scalar escape time \(\int_{c(0)}^\infty dc/[c f(c)]\) is finite. This excludes universal stable completion for every singleton support \(K\). Together with sufficiency, it proves the asserted equivalence.

## Verification

The self-contained file `check_orders.py` verifies the interpolation values, all gradient identities and every entry of the completed Jacobian with exact symbolic arithmetic for \(n=1,2,3,4\), degree pairs \((2,3),(2,5),(3,4),(4,7)\), and nontrivial rational input coefficients. It also checks the radial equilibrium multiplier and positive derivative for several single orders with and without pairwise competition. These are reproducibility checks for the displayed identities; the arbitrary-dimensional conclusion follows from the algebraic proof above rather than from finite sampling.

To reproduce: `python check_orders.py`, with Python and SymPy installed. The checker prints `PASS: 56 exact symbolic tests`.

## Relationship to prior work

Çelik, Isoldi, Portakal and Zucal (2026), Theorem 4.2, prove universal stable completion with the specifically chosen degree pair \((2,3)\), using closely related two-degree interpolation polynomials. That sufficiency instance is prior work. The result here instead determines the *entire class of permissible degree supports*: any two distinct higher-order degrees work, and every one-degree support fails universally, even with strictly competitive prescribed pairwise interactions. Its main mathematical distinction is the necessary-versus-sufficient interaction-order diversity boundary and the invariant-ray obstruction.

A related fixed-target result on the same model classifies the possible Jacobians of one *quadratic per-capita* higher-order component at a **fixed prescribed equilibrium**. Its one-order obstruction is therefore acknowledged as prior work; the present theorem does not claim that special case independently. The support classification includes arbitrary singleton degrees, flexible positive equilibrium locations, and every sparse pair of distinct degrees, which that fixed-degree theorem does not provide.

Cui et al. (2024) establish existence and stability results for structured higher-order tensors under positivity and monotonicity conditions; Gibbs et al. (2024) study feasible, stability-producing three-body terms with biologically motivated restrictions (including restrictions on repeated indices). Neither gives the unrestricted universal if-and-only-if support classification here. Standard Euler homogeneity and local Hurwitz criteria are used as established tools, not claimed as discoveries.

## Limitations

The theorem requires arbitrary **signed** higher-order coefficients and permits repeated partner indices. It may fail under prescribed interaction signs, sparsity patterns, bounded coefficient magnitudes, or when only distinct partner species may jointly interact. It ensures an attracting local interior equilibrium for appropriately constructed coefficients, not global attraction or boundedness of every positive orbit. Indeed the single-degree counterexample has finite-time escaping rays. Higher-order terms of different polynomial degrees are distinct arities; no interpretation of the same monomial as both degrees is permitted. The comparison with earlier work is based on accessible primary texts and indexed records and is not proof against an unindexed equivalent statement.

## References

- T. Ö. Çelik, V. A. Isoldi, I. Portakal and G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1 (posted 2026-09-08), especially Section 4 and Theorem 4.2. https://arxiv.org/html/2609.09286v1
- S. Cui, Q. Zhao, G. Zhang, H. Jardón-Kojakhmetov and M. Cao, *On the analysis of a higher-order Lotka-Volterra model*, arXiv:2405.18333 (2024). https://arxiv.org/abs/2405.18333
- T. L. Gibbs et al., *When can higher-order interactions produce stable coexistence?*, Ecology Letters **27** (2024), e14458. https://doi.org/10.1111/ele.14458
- C. Chen, X.-W. Wang and Y.-Y. Liu, *Stability of Ecological Systems: A Theoretical Review*, Physics Reports **1088** (2024), 1–41. https://doi.org/10.1016/j.physrep.2024.08.001
