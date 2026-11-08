# Exact product-rank census for two-generator exterior-algebra modules over finite fields

## Finding
Let \(q\) be any prime power, \(k=\mathbb F_q\), and \(n\ge 4\). Consider ordered \(n\)-square matrix pairs satisfying
\[A^2=B^2=0,\qquad AB+BA=0.\]
For \(t=\operatorname{rank}(AB)>0\), define \(a=\operatorname{rank}A\), \(b=\operatorname{rank}B\), \(w=\dim(\operatorname{im}A+\operatorname{im}B)\), and \(u=\dim(\ker A\cap\ker B)\). Every admissible five-index fiber has the exact labeled count stated below, uniformly in \(n,q\), including characteristic two. In particular, \(1\le t\le\lfloor n/4\rfloor\) and every such \(t\) occurs. This counts actual matrix pairs, not module isomorphism classes or conjugacy orbits.

For \(m=n-4t\), set \(r=a-2t\), \(s=b-2t\), \(v=w-3t\), \(z=u-t\). Put \(P_q(d,j)=\prod_{i=0}^{j-1}(q^d-q^i)\), the empty product being one, and \(G_d(q)=\prod_{i=0}^{d-1}(q^d-q^i)\), with \(G_0(q)=1\). Let \({d\brack j}_q\) denote the Gaussian coefficient, taken to be zero outside \(0\le j\le d\). Define
\[
F_q(\ell;r,s)=\sum_{j=0}^{\ell}(-1)^j q^{j(j-1)/2}{\ell\brack j}_q P_q(\ell-j,r)P_q(\ell-j,s).
\]
For admissible parameters,
\[
\boxed{\begin{aligned}
N_{n,q}(a,b,t,w,u)={}&\frac{G_n(q)}{G_m(q)G_t(q)q^{3t^2+2tm}}
{m\brack v}_q{v\brack r}_q{r\brack r+s-v}_q\\[-1mm]
&\times q^{(v-r)(v-s)}{m-v\brack z-v}_q F_q(m-z;r,s).
\end{aligned}}
\]
The parameters are admissible exactly when \(t\ge1\), \(4t\le n\), and
\[
0\le r,s\le m,\qquad \max(r,s)\le v\le r+s,\qquad v\le z\le m,\qquad \max(r,s)\le m-z\le r+s.
\]
Outside this range the fiber is empty. Each admissible tuple occurs over every finite field.

For example the positive-product stratum has \(2520\) pairs at \((n,q,t)=(4,2,1)\), \(449280\) at \((4,3,1)\), and \(312480\) at \((5,2,1)\). At \((6,2,1)\) there are \(262483200\) pairs: the \((a,b)=(2,2)\) fiber has \(26248320\), while each of \((2,3),(3,2),(3,3)\) has \(78744960\). In particular, there can be no nonzero product on a module of dimension below four.

## Assumptions and scope
All representations are left modules over the four-dimensional exterior algebra
\[E=k\langle x,y\rangle/(x^2,y^2,xy+yx),\]
with \(x\) acting as \(A\) and \(y\) acting as \(B\). In characteristic two, this is the commutative algebra \(k[x,y]/(x^2,y^2)\). The result concerns exactly the positive-product locus \(\operatorname{rank}(AB)>0\). It does not claim as new the rank-refined census of annihilating pairs \(AB=BA=0\), which supplies an input to the formula.

## Proof
**Step 1: split off all positive-product directions.** The algebra \(E\) is local Frobenius: the coefficient of \(xy\) in a product gives a perfect associative bilinear pairing, so its regular module is injective as well as projective. If \(ABv\ne0\), the four vectors \(v,Av,Bv,ABv\) are independent: a relation, after successive application of \(AB,A,B\), forces every coefficient to vanish. Therefore \(Ev\cong E\), and this copy splits from the representation by injectivity. Repeating in the complement shows that every module \(M\) has a decomposition \(E^{\oplus t}\oplus N\), with \((xy)N=0\) and \(t=\operatorname{rank}(AB)\). The equality holds because multiplication by \(xy\) has rank exactly one on each free \(E\) summand and zero on \(N\). A module annihilated by \(xy\) cannot contain a nonzero free summand. Consequently \(t\) and the isomorphism class of \(N\) are intrinsic. The decomposition holds in every characteristic.

**Step 2: transport the five invariants.** On a free \(E\) summand, the individual ranks of \(x,y\) equal two, their joint image has dimension three, and their common kernel has dimension one. Therefore \((a,b,t,w,u)=(2t+r,2t+s,t,3t+v,t+z)\), where \((r,s,v,z)\) are the corresponding invariants of \(N\). On \(N\), the two endomorphisms satisfy all four zero-product relations \(A_0^2=B_0^2=A_0B_0=B_0A_0=0\).

**Step 3: count the annihilating residual.** For \(N\) of dimension \(m\), choose the joint image \(W\) of dimension \(v\), and images \(I,J\subseteq W\) of dimensions \(r,s\) spanning \(W\). Their choices number \({m\brack v}_q{v\brack r}_q{r\brack r+s-v}_q q^{(v-r)(v-s)}\), obtained by choosing \(I\), then \(I\cap J\), then a graph complement. Choose the common kernel \(U\supseteq W\), of dimension \(z\), in \({m-v\brack z-v}_q\) ways. The induced maps on \(N/U\), with target spaces \(I,J\), must each be surjective and have trivial intersected kernels. Applying subspace-lattice Möbius inversion to the common kernel gives exactly \(F_q(m-z;r,s)\). These steps are reversible, so there is no overcounting. The displayed admissibility conditions are necessary and sufficient; for each permitted tuple the finite-field surjections with zero common kernel exist by linear algebra.

**Step 4: count labeled extensions by free summands.** Fix one isomorphism class of an annihilating \(m\)-module \(N\). Since \(E\) is Frobenius,
\[\dim_k\operatorname{Hom}_E(E^{\oplus t},N)=\dim_k\operatorname{Hom}_E(N,E^{\oplus t})=tm.\]
Also \(|\operatorname{GL}_t(E)|=q^{3t^2}G_t(q)\). Because \(N\) has no regular-module summand, off-diagonal maps between \(E^{\oplus t}\) and \(N\) lie in the categorical radical, so a block endomorphism of their direct sum is invertible precisely when the two diagonal blocks are invertible. Hence
\[|\operatorname{Aut}_E(E^{\oplus t}\oplus N)|=q^{3t^2+2tm}G_t(q)|\operatorname{Aut}_E(N)|.\]
The \(\operatorname{GL}_n(k)\) orbit-stabilizer formula, divided by the corresponding orbit-stabilizer formula for \(N\), multiplies every labeled residual pair by
\[K_{n,t,q}=\frac{G_n(q)}{G_m(q)G_t(q)q^{3t^2+2tm}}.\]
This factor depends only on \(m,t,q\), not on the residual module isomorphism class. Summing over all residual isomorphism classes proves the boxed joint-fiber formula. The free summands exist for every \(1\le t\le\lfloor n/4\rfloor\), by adjoining a zero residual module, establishing all stated ranges.

## Verification
The accompanying standalone `verify_exterior_product.py` uses Python's standard library and directly reconstructs the original matrix multiplication and rank equations over \(\mathbb F_2\) and \(\mathbb F_3\). It exhaustively checks all ordered pairs satisfying the defining equations at \((n,q)=(4,2)\) and \((3,3)\), direct residual annihilating-pair distributions in dimensions \(1\)–\(3\), and every compatible second matrix at a canonical rank-two square-zero first matrix for \((4,2),(4,3),(5,2)\). Every tested profile agrees with the closed formula; the precise output is in `verification_output.txt`. The computations cover only finite test cases and are not offered as proof of the uniform theorem.

## Relationship to prior work
Schröer studies the annihilating-pair variety \(AB=BA=A^2=B^2=0\), and the rank-refined count of this zero-product locus is an available input, not a new assertion here. Levy studies the commuting square-zero variety in characteristic two; Chen and Wang study the larger anti-commuting matrix variety; and Huang gives counts for broad quantum-plane representation varieties. None of the material inspected provides the present all-dimensional five-index labeled finite-field formula for the strictly positive-product locus. The Frobenius splitting and stabilizer principles are established background tools; the novel assessed statement is their explicit uniform rank-refined enumeration in this setting. Priority beyond the inspected sources is not certified.

## Limitations
The theorem classifies finite-field labeled counts by five linear-algebraic invariants; it does not classify indecomposable nonprojective exterior-algebra modules, conjugacy orbits, irreducible components, or scheme structure. It does not apply without change to higher-generator exterior algebras. Historical novelty remains provisional and independent mathematical audit has not been performed.

## References
- Jan Schröer, *Varieties of pairs of nilpotent matrices annihilating each other*, arXiv:math/0211293, first submitted November 19, 2002; Commentarii Mathematici Helvetici **79** (2004), 396–426, DOI:10.1007/s00014-003-0788-3.
- Paul Levy, *Varieties of Modules for Z/2Z × Z/2Z*, arXiv:math/0609180, first submitted September 6, 2006.
- Xinhong Chen and Weiqiang Wang, *Anti-commuting varieties*, arXiv:1805.00378 (2018).
- Yifeng Huang, *Counting on variety of modules over quantum plane*, arXiv:2110.15570 (2021).
