# Certified higher even-distance local stability of the regular hexagon

## Finding

For each \(k\in\{8,10,12,14,16,18,20,22,24\}\), let \(P\) be a positively oriented, labeled, strictly convex Euclidean hexagon, and define the scale-invariant pairwise-distance energy
\[
\Phi_k(P)=\frac{1}{\operatorname{area}(P)^{(k+4)/2}}\int_P\int_P\|x-y\|^k\,dx\,dy.
\]
The unit-circumradius regular hexagon \(H\) is a **strict local minimizer modulo direct Euclidean similarities** of \(\Phi_k\) for every listed exponent. Thus there is a neighborhood of its six ordered vertices such that \(\Phi_k(P)\ge\Phi_k(H)\), with equality exactly when \(P\) is directly similar to \(H\). This holds under *arbitrary* sufficiently small vertex displacements, not just symmetric, centrally symmetric, or affine perturbations.

A complete exact rational Hessian certificate is given for all nine exponents: after fixing two opposite vertices, each of the nine eight-dimensional reduced Hessians has eight strictly positive \(LDL^{\mathsf T}\) pivots. The certified range is the higher-even portion of the numerical range examined in the 2023 study by Bogosel, Bucur and Fragalà.

## Assumptions and scope

Hexagons are represented by six distinct vertices in counterclockwise cyclic order, with all interior angles strictly between \(0\) and \(\pi\). The statement is local in vertex-coordinate topology and does not claim a global optimizer. Exponents are exactly the nine even integers displayed above; no conclusion is claimed for intermediate real or higher powers. Direct similarities are translations, orientation-preserving rotations and positive homotheties.

Let \(T(u,v)=(u/2,\sqrt3\,v/2)\). The reference regular hexagon has ordered \((u,v)\)-vertices
\[
(2,0),\ (1,1),\ (-1,1),\ (-2,0),\ (-1,-1),\ (1,-1).
\]
Fix vertices \(0\) and \(3\) at \((2,0)\) and \((-2,0)\), respectively. The two coordinates of each of vertices \(1,2,4,5\) give an eight-dimensional local chart. Every nearby labeled hexagon can be uniquely mapped into this chart by a direct similarity, because two distinct ordered vertices determine a unique direct similarity sending them to two specified distinct points.

## Proof

Write \(k=2m\), \(b=m+2\), and let \(A\) denote area in the \((u,v)\)-plane. For any polygon \(Q\) in this coordinate plane, put
\[
J_m(Q)=\int_Q\int_Q\big((u-u')^2+3(v-v')^2\big)^m\,du\,dv\,du'\,dv'.
\]
The affine change of variables gives exactly
\[
\Phi_{2m}(TQ)=3^{-m/2}\frac{J_m(Q)}{A(Q)^b}.
\]
The constant factor is strictly positive. At the reference polygon \(A=6\), so it suffices to study \(F=J_m/A^b\).

For every sufficiently nearby hexagon the origin lies inside it, so its six triangles with vertices \(0,U_i,V_i\), where \(U_i,V_i\) are consecutive boundary vertices, triangulate it. The monomial moment \(M_{ab}=\int_Q u^av^b\,du\,dv\), for nonnegative integers \(a,b\), is given by the finite identity
\[
M_{ab}=\sum_{i=0}^{5}\det(U_i,V_i)\sum_{p=0}^{a}\sum_{q=0}^{b}
\binom ap\binom bq (U_{i,u})^p(V_{i,u})^{a-p}(U_{i,v})^q(V_{i,v})^{b-q}
\frac{(p+q)!(a+b-p-q)!}{(a+b+2)!}.
\]
Indeed, substituting \((u,v)=sU_i+tV_i\) reduces each term to the beta integral of \(s^{p+q}t^{a+b-p-q}\) over \(s,t\ge0\), \(s+t\le1\). The formula is a polynomial identity in the vertex coordinates, not a numerical quadrature approximation.

Expanding the even power in \(J_m\) gives a second exact identity:
\[
J_m=\sum_{h=0}^{m}\binom mh3^{m-h}
\sum_{i=0}^{2h}\sum_{j=0}^{2m-2h}
(-1)^{2m-i-j}\binom{2h}{i}\binom{2m-2h}{j}
M_{ij}M_{2h-i,\,2m-2h-j}.
\]
All relevant derivatives can therefore be obtained by truncating rational polynomials in the eight free vertex coordinates at total perturbation degree two. Denote the gradient and Hessian by \(g\) and \(H\). Exact evaluation for every listed \(m\) verifies stationarity, \(gJ_m=(bJ_m/A)gA\). Stationarity also follows from dihedral symmetry and scale invariance.

At a stationary point, the following **exact** Hessian identity holds:
\[
A^{b+2}H(F)=K_m:=A^2H(J_m)-bJ_m A H(A)+b(1-b)J_m\,g(A)g(A)^{\mathsf T}.
\]
The artifact `certificate.json` contains, for each listed exponent, all \(64\) entries of the symmetric rational matrix \(K_m\), its rational energy \(J_m\), and the eight positive rational pivots of its exact \(LDL^{\mathsf T}\) decomposition. `verify.py` independently recomputes these quantities using the displayed monomial integration formula and tests all matrix entries, stationarity identities and strict positivity with arbitrary-precision integer fractions.

Because \(A=6>0\), each reduced \(H(F)\) is positive definite. The ordinary multivariate Taylor theorem yields a strict local minimum in the eight-coordinate slice. Invariance under direct similarities transports that inequality to all nearby convex labeled hexagons, proving the claim.

## Verification

Run `python3 verify.py certificate.json` without Python optimization flags. The verifier uses only the Python standard library and exact rational arithmetic. The recorded replay checked nine exponents, \(72\) strictly positive rational pivots, and \(576\) exact Hessian-matrix entry comparisons. It also confirms first-derivative stationarity at the reference hexagon and reconstruction of each \(LDL^{\mathsf T}\) factorization.

An independent floating-point diagnostic, `numeric_crosscheck.py`, computes each of three selected energies by Gauss–Legendre integration over pairs of fan triangles and approximates a directional Hessian entry by symmetric finite differences. For \(k=8,16,24\) its baseline relative energy discrepancies were below \(7\cdot10^{-14}\), and the selected Hessian discrepancies were below \(2\cdot10^{-6}\) relative. These diagnostics are not used as the proof of matrix positivity.

## Relationship to prior work

Bogosel, Bucur and Fragalà (2023) numerically found positive nontrivial Hessian eigenvalues for regular polygons with \(5\) through \(10\) sides and even powers through \(24\), while explicitly distinguishing this from a certified analytic result. Their theorems prove the all-polygon inequality for the second and fourth powers, but not for higher even powers. Their linear-image lemma also does not control arbitrary nonaffine hexagon perturbations. The present claim converts their **nine higher-even hexagon tests** into exact, reproducible proofs in the first even side count admitting global symmetry breaking at sufficiently high power.

The sixth-power hexagon local minimum has separately been proved exactly; it is **not** a new exponent claimed here. The separate exact pentagon results at these exponents do not imply the hexagonal case. Bonacini, Cristoferi and Topaloglu (2021) study three- and four-sided Riesz-type extremizers and cannot directly imply the present six-sided assertion.

## Limitations

Only local minimality modulo similarities is proved. Global optimality over all convex hexagons, a uniform neighborhood radius, higher or noninteger exponents, and the location of any high-exponent symmetry-breaking transition remain open here. The rational certificate is finite computation supported by explicit moment identities and a reproducible checker; it is not an independent external mathematical audit. An unindexed equivalent exact proof remains a historical priority risk.

## References

- B. Bogosel, D. Bucur, I. Fragalà, *The nonlocal isoperimetric problem for polygons: Hardy–Littlewood and Riesz inequalities*, arXiv:2302.11677v1 (first public version 22 February 2023), https://arxiv.org/html/2302.11677v1, especially Sections 2, 3.1, 3.3 and 9.3.
- M. Bonacini, R. Cristoferi, I. Topaloglu, *Riesz-type inequalities and overdetermined problems for triangles and quadrilaterals*, arXiv:2103.06657, https://arxiv.org/abs/2103.06657.
