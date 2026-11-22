# Exact numerical index of every three-point real Lipschitz-free space

## Finding
Let \(M\) be a three-point metric space, and write its three pairwise distances in cyclic order as \(a,b,c>0\). Suppose first that all three triangle inequalities are strict. For \(i\in\{1,2,3\}\), let \((w_1,w_2,w_3)=(a,b,c)\), and let \(\{i,j,k\}=\{1,2,3\}\). Define
\[
A_i=\frac{w_j+w_k}{w_i},\qquad
B_i=1+\frac{(w_i+w_j-w_k)(w_i+w_k-w_j)}{w_i(w_j+w_k-w_i)},\qquad R_i=\min\{A_i,B_i\}.
\]
The exact *real* numerical index of its Lipschitz-free Banach space is
\[
\boxed{n(\mathcal F_{\mathbb R}(M))=\frac1{\max\{R_1,R_2,R_3\}}.}
\]
The infimum defining the numerical index is attained by a **rank-one real operator** on \(\mathcal F_{\mathbb R}(M)\) (equivalently on the finite-dimensional dual) for every choice of strict triangle side lengths. If one triangle inequality is an equality, then the free space is real \(\ell_1^2\) and its numerical index is \(1\).

For the asymmetric metric with sides \((a,b,c)=(2,3,4)\), the three sharp missing-coordinate ratios are \((13/10,14/9,5/4)\) in edge order and the numerical index is \(9/14\). The one-parameter isosceles subfamily \((1,1,t)\), \(0<t<2\), simplifies to \(n=1/(1+\min\{t,2-t\})\).

## Assumptions and scope
The scalar field is \(\mathbb R\). For a real Banach space \(X\), its numerical index is \(n(X)=\inf_{\|T\|=1}v(T)\) with \(v(T)=\sup\{|x^*(Tx)|:\|x\|=\|x^*\|=x^*(x)=1\}\). Here \(M\) has **exactly three distinct points**, and its side lengths form a metric triangle. No result is asserted for complex scalars or larger finite metrics. The real finite-dimensional identity \(n(X)=n(X^*)\) is used.

The dual \(\mathcal F_{\mathbb R}(M)^*=\mathrm{Lip}_0(M;\mathbb R)\) can be written using oriented edge slopes as
\[
X_w=\left\{z\in\mathbb R^3:w_1z_1+w_2z_2+w_3z_3=0\right\},\qquad\|z\|=\max_i|z_i|.
\]
The weighted-zero-sum constraint follows by summing the three oriented increments around the triangle, and every vector in this plane gives a unique pointed potential.

## Proof
**1. Vertices and numerical radius.** Under strict triangle inequalities, \(B_{X_w}=X_w\cap[-1,1]^3\) is a centrally symmetric hexagon. Denote by \(v_i\), for \(i=1,2,3\), the vertex (unique up to sign) whose *missing* coordinate \(i\) has absolute value strictly less than \(1\), while the other two coordinates have absolute value \(1\). Its opposite vertex is \(-v_i\). On the vertex \(v_i\), the extreme norming functionals are the signed restrictions of coordinate functionals \(\phi_j(z)=z_j\) and \(\phi_k(z)=z_k\), where \(\{i,j,k\}=\{1,2,3\}\). Since norm and numerical radius of a finite-dimensional polyhedral space may be computed at its extreme points, every \(T:X_w\to X_w\) satisfies
\[
\|T\|=\max_{i,k}|\phi_k(Tv_i)|,\qquad
v(T)=\max_i\max_{k\ne i}|\phi_k(Tv_i)|.
\]
Thus only the three missing-coordinate entries \(\phi_i(Tv_i)\) can exceed \(v(T)\).

**2. Two independent upper bounds.** Put \(V=v(T)\), fix \(i\), and let \(\{i,j,k\}=\{1,2,3\}\). Since \(Tv_i\in X_w\), the triangle inequality for real numbers gives
\[
|\phi_i(Tv_i)|\le\frac{w_j+w_k}{w_i}V=A_iV.
\]
The other two vertices \(v_j,v_k\) form a basis of the plane. Write \(v_i=\alpha_i v_j+\beta_i v_k\). Direct solution of the two weighted edge-slope equations gives
\[
|\alpha_i|+|\beta_i|
=1+\frac{(w_i+w_j-w_k)(w_i+w_k-w_j)}{w_i(w_j+w_k-w_i)}=B_i.
\]
Because \(i\ne j,k\), both \(\phi_i(Tv_j)\) and \(\phi_i(Tv_k)\) are numerical-radius entries and hence have absolute value at most \(V\). Therefore \(|\phi_i(Tv_i)|\le B_iV\). Combining the two bounds proves \(\|T\|\le\max_iR_i\,v(T)\).

**3. Every bound is attained by a rank-one operator.** Fix any index \(i\), and retain the expansion \(v_i=\alpha_i v_j+\beta_i v_k\). Since \(v_j,v_k\) are linearly independent, there is a real linear functional \(\psi\) with \(\psi(v_j)=\operatorname{sgn}(\alpha_i)\) and \(\psi(v_k)=\operatorname{sgn}(\beta_i)\). Then \(\psi(v_i)=B_i\). Put \(\eta=(R_i/B_i)\psi\), so that \(|\eta(v_j)|,|\eta(v_k)|\le1\) and \(\eta(v_i)=R_i\). Define \(u\in X_w\) by
\[
u_i=1,\qquad u_j=u_k=-\frac{w_i}{w_j+w_k}.
\]
By the strict triangle inequality, \(\|u\|=1\). Let \(T(z)=\eta(z)u\). At \(v_j,v_k\), all norming coordinates of \(Tv_j,Tv_k\) have magnitude at most \(1\). At \(v_i\), the two norming coordinates have magnitude \(R_iw_i/(w_j+w_k)\le1\), because \(R_i\le A_i\). Consequently \(v(T)\le1\), while its missing-coordinate entry \(|\phi_i(Tv_i)|=R_i\), so \(\|T\|\ge R_i\). Taking an index maximizing \(R_i\), and rescaling \(T\) to norm one, gives \(n(X_w)\le1/\max_iR_i\). Together with step 2 and finite-dimensional duality, this proves the theorem. The construction is explicitly rank one.

**4. Collinear boundary.** If, for instance, \(c=a+b\), the third metric point lies between the other two in the path metric. Oriented increments on the two segments are freely and independently \(\ell_\infty\)-bounded, so \(\mathrm{Lip}_0(M)\cong\ell_\infty^2\) and \(\mathcal F_{\mathbb R}(M)\cong\ell_1^2\), both with numerical index \(1\).

## Verification
All steps above are exact and quantify over **every** real linear operator in dimension two. An optional self-contained Python script \(\texttt{CHECK.py}\) uses rational arithmetic to confirm all three rank-one constructions and their exact norm and radius bounds on \(7^3=343\) strictly nondegenerate integer-parameter triangles and three additional rational examples. This finite diagnostic is supplementary, not an infinite proof. The displayed asymmetric and isosceles values follow by direct substitution into the theorem.

## Relationship to prior work
Pal, Roy and Sain (2026) characterize Banach spaces with numerical index one and identify the relevant finite-dimensional numerical-radius dual extreme points, but do not give the present numerical-index function on non-equilateral three-point metric spaces. Martín and Merí (2007) compute the numerical index of a **one-parameter reflection-symmetric** hexagonal norm family \(X_\gamma\); our formula includes its isosceles metric realization but also varies **all three side lengths** modulo common scaling. Sain, Paul, Bhunia and Bag (2018/2019) give a general polyhedral lower-bound method and an irregular-hexagon example, but not this exact two-parameter metric-triangle formula with universal rank-one equality. The relation to the isosceles hexagon result is specialization, not a claim that case is new. General extremal-geometry theorems underlie the finite-dimensional norming reduction; their broad applicability alone does not state this formula.

## Limitations
The result concerns only real three-point metrics and finite-dimensional operators, not a universal extension to arbitrary metric spaces, complex scalars or all planar centrally symmetric hexagons with arbitrary affine geometry. Independent peer assessment has not occurred. An equivalent result in literature not located by the targeted searches remains possible.

## References
1. S. Pal, S. Roy, D. Sain, *A characterization of Banach spaces with numerical index one*, arXiv:2604.03690 (first posted 4 April 2026), https://arxiv.org/abs/2604.03690.
2. M. Martín and J. Merí, *Numerical index of some polyhedral norms on the plane*, Journal of Mathematical Analysis and Applications 330 (2007), 525–537, https://www.ugr.es/~mmartins/Curriculum/Papers/2007-Polygons.pdf.
3. D. Sain, K. Paul, P. Bhunia, S. Bag, *On the numerical index of polyhedral Banach spaces*, Linear Algebra and Its Applications 577 (2019), 121–133; preprint arXiv:1809.04778, https://arxiv.org/abs/1809.04778.
4. R. J. Aliaga, E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, Revista Matemática Iberoamericana 36 (2020), 2073–2089, https://arxiv.org/abs/1810.11278.
