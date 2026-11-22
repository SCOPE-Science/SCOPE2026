# Exact rooted-resultant D-volumes for arbitrary weighted diffusion paths

## Finding
For every path with \(n\ge2\) vertices and **arbitrary positive edge conductances**, the full-state one-actuator diffusion controllability-Gramian determinant factors into a vertex-independent positive spectral factor and the square of an **explicit edge-weight monomial times the resultant of the two principal blocks cut by the actuator**. This gives an exact algebraic D-optimal placement rule at every size, for all finite positive horizons and all nonnegative homogeneous damping rates, without integrating the Gramian. In the first nontrivial reflection-symmetric five-vertex family with unequal outer and inner edge weights, the rule gives a sharp, complete endpoint-to-interior actuator transition at equality of the two conductances.

More precisely, let \(L=L(w)\) be the weighted combinatorial Laplacian of the path on vertices \(1,\ldots,n\): \(L_{i,i+1}=L_{i+1,i}=-w_i\) and \(L_{ii}=w_{i-1}+w_i\), where \(w_0=w_n=0\). Let \(\mu\ge0\), \(T>0\), and
\[
G_j(T)=\int_0^T e^{-(L+\mu I)t}e_je_j^{\mathsf T}e^{-(L+\mu I)t}\,dt,
\qquad
C_j=[e_j,Le_j,\ldots,L^{n-1}e_j].
\]
Cutting vertex \(j\) leaves principal submatrices \(L^-_j=L[1{:}j-1,1{:}j-1]\) and \(L^+_j=L[j+1{:}n,j+1{:}n]\); **the original diagonal degrees are retained**. For an empty block, set its characteristic polynomial to \(1\). Define
\[
p_j^-(z)=\det(zI-L_j^-),\quad
p_j^+(z)=\det(zI-L_j^+),\quad
R_j=\operatorname{Res}_z(p_j^-,p_j^+),
\]
\[
E_j=\left(\prod_{i=1}^{j-1}w_i^{i}\right)
\left(\prod_{i=j}^{n-1}w_i^{n-i}\right),
\qquad s_j=E_jR_j.
\]
A resultant involving the constant polynomial \(1\) equals \(1\). Then, for every such path and vertex,
\[
\boxed{\big|\det C_j\big|=|s_j|.}
\]
Let \(0=\lambda_0<\lambda_1<\cdots<\lambda_{n-1}\) be the distinct eigenvalues of \(L\), put \(\alpha_k=\mu+\lambda_k\), and define the positive-definite matrix
\[
H_T=(h_{kl})_{0\le k,l<n},\qquad
h_{kl}=\int_0^T e^{-(\alpha_k+\alpha_l)t}\,dt,
\quad
\Delta=\prod_{0\le k<l<n}(\lambda_l-\lambda_k).
\]
The exact finite-horizon factorization is
\[
\boxed{\det G_j(T)=\frac{\det H_T}{\Delta^2}\,s_j^2.}
\tag{1}
\]
If \(\mu>0\), the infinite-horizon factorization is
\[
\boxed{\det G_j(\infty)
=\frac{s_j^2}{\displaystyle\prod_{k,l=0}^{n-1}(\alpha_k+\alpha_l)}.}
\tag{2}
\]
Thus the entire D-optimal set is exactly \(\arg\max_j |s_j|\), independent of \(T>0\) and \(\mu\ge0\) (and the same for infinite time when \(\mu>0\)). The Gramian is nonsingular precisely when \(R_j\ne0\), equivalently when the two cut-block spectra have no common eigenvalue.

**A complete five-site weighted design consequence.** Let \(n=5\) and put \((w_1,w_2,w_3,w_4)=(a,b,b,a)\) for any \(a,b>0\). The five factors satisfy
\[
|s_1|=|s_5|=a^5b^5,\qquad
|s_2|=|s_4|=a^4b^5|a-2b|,\qquad s_3=0.
\]
Consequently the **complete set** of D-optimal actuator sites, for every \(T>0\) and \(\mu\ge0\), is
\[
\boxed{
\begin{cases}
\{1,5\},&b<a,\\
\{1,2,4,5\},&b=a,\\
\{2,4\},&b>a.
\end{cases}}
\tag{3}
\]
The midpoint is uncontrollable for every \(a,b\). The change at \(a=b\) is a sharp boundary-to-interior switch, not a claim about any unequal-noise or multiple-input design.

## Assumptions and scope
The path is finite, undirected and symmetric, with strictly positive real conductances; damping is homogeneous and nonnegative. There is precisely one unit-strength coordinate actuator, the objective is the determinant of its **full-state** finite-horizon controllability Gramian, and all actuator locations have the same physical scale. The integral uses continuous time, with \(T>0\) and no probabilistic interpretation required. Infinite-horizon determinants require \(\mu>0\). Formula (1) includes uncontrollable sites with zero determinant. The five-site classification (3) assumes the mirror-symmetric two-parameter weight pattern; the root-resultant formulas (1)–(2) allow **all** positive conductance vectors. Polynomial formulas in the resultants do not presuppose rational conductances.

## Proof
**1. Spectral reduction.** Every real symmetric tridiagonal matrix with all off-diagonal entries nonzero has simple real spectrum. Let \(U\) be orthogonal with \(L=U\operatorname{diag}(\lambda_k)U^{\mathsf T}\), and let \(u_{kj}\) denote its \(k\)-th modal coefficient at vertex \(j\). Spectral conjugation gives
\[
U^{\mathsf T}G_j(T)U
=\operatorname{diag}(u_{kj})H_T\operatorname{diag}(u_{kj}).
\]
For every nonzero \(a\in\mathbb R^n\),
\[
a^{\mathsf T}H_Ta
=\int_0^T\Big(\sum_{k=0}^{n-1}a_ke^{-\alpha_k t}\Big)^2dt>0
\]
because exponentials with distinct real rates are linearly independent on any nonempty interval. Meanwhile, the Vandermonde factorization of \(C_j\) gives
\[
\big|\det C_j\big|^2=\Delta^2\prod_k u_{kj}^2,
\qquad
\det G_j(T)=\det H_T\prod_k u_{kj}^2.
\tag{4}
\]

**2. From a rooted cofactor to a resultant.** Set \(p(z)=\det(zI-L)\), and \(q_j(z)=\det(zI-L_{\widehat j})=p_j^-(z)p_j^+(z)\). The spectral resolvent identity is
\[
\frac{q_j(z)}{p(z)}
=e_j^{\mathsf T}(zI-L)^{-1}e_j
=\sum_k\frac{u_{kj}^2}{z-\lambda_k}.
\]
Comparing residues yields \(u_{kj}^2=q_j(\lambda_k)/p'(\lambda_k)\). Since \(\prod_k|p'(\lambda_k)|=\Delta^2\), equation (4) gives the *exact* identity
\[
\big|\det C_j\big|^2=\left|\operatorname{Res}_z(p,q_j)\right|.
\tag{5}
\]
This identity remains valid when one or more modes are unexcited: the resultant then vanishes.

**3. Factor the weighted-path resultant.** Denote the two block sizes by \(a=j-1\) and \(b=n-j\), and denote by \(p_{L,\mathrm{near}}\) and \(p_{R,\mathrm{near}}\) the characteristic polynomials obtained from the corresponding block by deleting the boundary vertex **nearest the cut** (with polynomial \(1\) for an empty smaller block). Three-term determinant expansion gives
\[
p(z)=(z-L_{jj})p_j^-(z)p_j^+(z)
-w_{j-1}^2p_{L,\mathrm{near}}(z)p_j^+(z)
-w_j^2p_j^-(z)p_{R,\mathrm{near}}(z),
\tag{6}
\]
where terms involving a missing edge are omitted. Evaluating (6) at the roots of the left and right block polynomials, respectively, and multiplying values establishes
\[
\left|\operatorname{Res}(p,p_j^-)\right|
=w_{j-1}^{2a}\left|\operatorname{Res}(p_{L,\mathrm{near}},p_j^-)\right|\,|R_j|,
\]
\[
\left|\operatorname{Res}(p,p_j^+)\right|
=w_{j}^{2b}\left|\operatorname{Res}(p_{R,\mathrm{near}},p_j^+)\right|\,|R_j|.
\tag{7}
\]
The same tridiagonal recurrence, applied successively to the boundary-principal minors of the left and right blocks, gives
\[
\left|\operatorname{Res}(p_{L,\mathrm{near}},p_j^-)\right|
=\prod_{i=1}^{j-2}w_i^{2i},
\qquad
\left|\operatorname{Res}(p_{R,\mathrm{near}},p_j^+)\right|
=\prod_{i=j+1}^{n-1}w_i^{2(n-i)}.
\tag{8}
\]
For example, (8) follows by taking the product of \(p_m(\xi)=-w_{m-1}^2p_{m-2}(\xi)\) over the roots \(\xi\) of the preceding monic polynomial \(p_{m-1}\), then iterating to the constant polynomial \(1\); it does not require numerical roots. Resultant multiplicativity, (7) and (8) therefore imply
\[
\left|\operatorname{Res}(p,q_j)\right|
=\left(\prod_{i=1}^{j-1}w_i^{2i}\right)
\left(\prod_{i=j}^{n-1}w_i^{2(n-i)}\right)|R_j|^2
=s_j^2.
\]
Combining with (5) proves the rooted-Krylov determinant formula; inserting it into (4) proves (1). If \(\mu>0\), \(H_\infty\) is the Cauchy matrix \([1/(\alpha_k+\alpha_l)]\); the classical Cauchy determinant identity says \(\det H_\infty=\Delta^2/\prod_{k,l}(\alpha_k+\alpha_l)\), proving (2). Finally, by positivity of \(H_T\) and \(E_j\), full controllability is equivalent to \(R_j\ne0\), or coprimality of the two block polynomials.

**4. Five-site symmetric conductances.** When \(n=5\) and the conductances are \((a,b,b,a)\), substituting the corresponding two cut-block characteristic polynomials into \(s_j=E_jR_j\) and simplifying gives
\[
(|s_1|,|s_2|,|s_3|,|s_4|,|s_5|)
=\big(a^5b^5,\ a^4b^5|a-2b|,\ 0,\ a^4b^5|a-2b|,\ a^5b^5\big).
\]
These absolute factors, not the irrelevant resultant sign convention, enter (1). The center has two isospectral nonempty principal blocks and therefore resultant zero. By (1), comparison of the two positive squared factors reduces to \(|a-2b|\) versus \(a\). For \(a,b>0\), \(|a-2b|<a\) exactly when \(b<a\), equality holds exactly when \(b=a\), and the inequality reverses when \(b>a\). This proves every optimal set and all boundaries in (3).

## Verification
The companion standalone `verify.py` compares \((\det C_j)^2\) with \(s_j^2\) by exact rational arithmetic for three conductance patterns at every vertex for \(2\le n\le8\). It also rechecks the previously understood **uniform** path coprimality/unimodularity case at every vertex for \(2\le n\le12\) as a regression test, not as a new claimed result. A separately computed 80-point Gauss–Legendre quadrature tests the spectral-Gramian determinant on a heterogeneous path, and exact inverse checks exercise related stable-diffusion identities. All 200 checks pass. The general proof, not finite tests, establishes the arbitrary-size and arbitrary-weight result.

Run `python verify.py` with Python 3, SymPy, NumPy and SciPy installed. The implementation constructs every matrix directly from the displayed definitions. No external file or network connection is required.

## Relationship to prior work
Parlangeli and Notarstefano (2011) analyze reachability of unweighted paths and cycles. The exact unweighted-path coprimality/unimodularity and common positive-volume classification is **background, not claimed as a new finding**. Dilip (2019), especially Theorems 2–3, gives the general symmetric spectral-Gramian determinant reduction and illustrates a six-node unweighted path tie; this determinant method and its horizon independence are explicitly prior results. Liu and Shan (2026) connect path cyclicity to root cofactors and resultants and evaluate central-root resultants for a uniformly parameterized path in a different rooted-product problem. A published four-site weighted-path D-optimal phase diagram gives all positive-weight cases at that **fixed size**, with exact polynomial factors and boundary ties. The present contribution is the **all-length, all-positive-weight path-specific resultant formula with precise edge-exponent factors**, together with the distinct symmetric five-site design phase (3). The rooted-cofactor identity and three-term Jacobi recurrences used in the derivation are classical; their combination and all-vertex weighted placement expression are the claimed specialization, not newly invented general techniques.

## Limitations
The result concerns a single coordinate actuator on a symmetric path and does not classify D-optimality for multiple actuators, directed dynamics, general graphs or arbitrary vertex-dependent actuation strengths. No positive value is claimed for a singular Gramian. The general weighted formula determines optimal vertices by exact polynomials but does not give a complete inequality phase diagram for every arbitrary conductance vector. The five-site application assumes reflection symmetry and two common edge classes. The unweighted all-length volume tie is not asserted to be new. Publication-priority searches cannot exclude unindexed or inaccessible older equivalent formulas, particularly in the Jacobi-matrix and orthogonal-polynomial literature; the weighted resultant identity may have been derived elsewhere in another notation. The claims are analytically proved but have not undergone independent mathematical validation.

## References
1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556, initial submission 2011-09-16. https://arxiv.org/abs/1109.3556
2. A. S. A. Dilip, *The Controllability Gramian, the Hadamard Product, and the Optimal Actuator/Leader and Sensor Selection Problem*, IEEE Control Systems Letters **3** (2019), 883–888, DOI:10.1109/LCSYS.2019.2919278. https://doi.org/10.1109/LCSYS.2019.2919278
3. T. H. Summers, F. L. Cortesi and J. Lygeros, *On Submodularity and Controllability in Complex Dynamical Networks*, arXiv:1404.7665 (2014). https://arxiv.org/abs/1404.7665
4. X. Liu and H. Shan, *\(A_\alpha\)-Wronskian Vertices of Paths and Controllability of Path-Rooted Products*, arXiv:2611.21385, first submitted 2026-11-16. https://arxiv.org/abs/2611.21385
5. *A complete D-optimal sensor phase diagram for four-vertex weighted diffusion paths*, public research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-complete-d-optimal-sensor-phase-diagram-for-four-vertex-weight--8e5b80a6bdef
