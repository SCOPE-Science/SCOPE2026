# A three-stage screening migration for one Nyström landmark on a defective five-cycle

## Finding

Let the five-cycle have consecutive unit-conductance edges \((0,1),(1,2),(2,3),(3,4)\) and one exceptional edge \((4,0)\) of conductance \(0<w<1\). For every positive screening strength \(\mu\), let
\[
G_\mu=(\mu I+L_w)^{-1},\qquad
T_i=\operatorname{tr}\left(G_\mu-\frac{G_\mu e_i e_i^{\mathsf T}G_\mu}{(G_\mu)_{ii}}\right).
\]
The exact minimizers of the single-landmark Nyström trace error \(T_i\) pass through three genuinely distinct vertex orbits as \(\mu\) increases. Denote the weak-edge endpoints by \(A=\{0,4\}\), their neighbors by \(B=\{1,3\}\), and the opposite vertex by \(C=\{2\}\). Put
\[
F_w(x)=3x^4+(12+4w)x^3+(11+10w)x^2-(1+4w)
\]
and
\[
J_w(x)=x^6+8x^5+(22-2w)x^4+(22-14w)x^3
 +(2-34w)x^2-(8+32w)x-(3+12w).
\]
Each polynomial has exactly one positive real root. Call these \(\alpha_w\) and \(\beta_w\), respectively. Then \(0<\alpha_w<\beta_w\), and all optimal one-vertex sets are exactly

- \(C\) if \(0<\mu<\alpha_w\);
- \(B\cup C\) if \(\mu=\alpha_w\);
- \(B\) if \(\alpha_w<\mu<\beta_w\);
- \(A\cup B\) if \(\mu=\beta_w\);
- \(A\) if \(\mu>\beta_w\).

Here an orbit listed as optimal means each of its vertices individually achieves the same smallest residual trace. In contrast, **maximizing the one-landmark determinant** \(\det G_{\{i\},\{i\}}=(G_\mu)_{ii}\) always selects exactly the two vertices of \(A\), for every \(\mu>0\). Thus the determinant- and trace-optimal sensors disagree throughout \(0<\mu<\beta_w\), notwithstanding their common choice at large screening. For \(w=1/2\), exact rational sign brackets give \(0.372419<\alpha_w<0.372420\) and \(1.023614<\beta_w<1.023615\).

Within the family of five-or-fewer-vertex simple cycles having one exceptional edge, five vertices are the first order with three distinct vertex orbits under the residual reflection symmetry; hence three successive strict optimal-location orbits are impossible at smaller orders in this family.

## Assumptions and scope

The vertex set is \(\{0,1,2,3,4\}\). The weighted combinatorial Laplacian is
\[
L_w=\sum_{\{i,j\}\text{ an edge}}c_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T},
\quad c_{04}=w,\quad c_{01}=c_{12}=c_{23}=c_{34}=1.
\]
Only \(0<w<1\), \(\mu>0\), noiseless observation of exactly one vertex, and the unscaled positive-definite covariance \(G_\mu\) are considered. The trace residual is the total posterior conditional variance, not the posterior entropy. A single selected marginal covariance determinant equals its variance and controls the entropy of the selected Gaussian observation; the two are different design objectives. The optimality claim compares all five possible singleton sets, with no imposed symmetry on the choice.

## Proof

**1. Exact inverse diagonals.** Set \(x=\mu\), and define strictly positive quantities
\[
Q=x^2+5x+5,\qquad
D=x^2+3x+1+(2x+4)w,\qquad
h=\frac{x^2+3x+1}{xQ}.
\]
Direct inversion of the cyclic tridiagonal precision matrix, or a rank-one Sherman--Morrison update of the uniform-cycle inverse, gives
\[
(G_\mu)_{22}=h,\quad
(G_\mu)_{11}=(G_\mu)_{33}=h+\frac{1-w}{QD},\quad
(G_\mu)_{00}=(G_\mu)_{44}=h+\frac{(1-w)(x+2)^2}{QD}.
\tag{1}
\]
For completeness, the uniform-cycle update replaces an edge of weight one by weight \(w\), a precision decrement \((1-w)(e_0-e_4)(e_0-e_4)^{\mathsf T}\). Its inverse correction is positive and rank one; the update vector vanishes at vertex 2 and has absolute amplitude ratio \((x+2):1\) on \(A:B\). Solving the three distinct orbit equations and the uniform-cycle diagonal gives (1), independently verified by exact matrix multiplication in the included checker. As \((x+2)^2>1\), (1) proves the strict determinant ordering \(G_{AA}>G_{BB}>G_{CC}\) (meaning their representative diagonal entries).

**2. Trace-gain derivative identity.** For a singleton landmark, cyclicity of trace gives
\[
T_i=\operatorname{tr}(G_\mu)-R_i,\qquad
R_i=\frac{(G_\mu^2)_{ii}}{(G_\mu)_{ii}}.
\]
Differentiating \((\mu I+L_w)G_\mu=I\) proves \(G_\mu'=-G_\mu^2\), and therefore the exact identity
\[
R_i=-\frac{d}{dx}\log (G_\mu)_{ii}.\tag{2}
\]
Write \(R_A,R_B,R_C\) for the three orbit scores. Define the positive polynomials
\[
U_A=xQD(G_\mu)_{00},\qquad U_B=xQD(G_\mu)_{11}.
\]
Substitution of (1) into (2) and cancellation yield the two exact rational identities
\[
R_C-R_B=\frac{(w-1)F_w(x)}{(x^2+3x+1)D U_B},\qquad
R_B-R_A=\frac{(w-1)J_w(x)}{U_AU_B}.\tag{3}
\]
Every denominator in (3) is strictly positive. The symbolic checker verifies these identities as exact polynomial equalities, not numerical fits.

**3. Unique positive roots.** \(F_w(0)=-(1+4w)<0\), \(F_w(x)\to+\infty\), and \(F'_w(x)>0\) for every \(x>0\), proving that \(\alpha_w\) exists uniquely. The descending coefficient sequence of \(J_w\) has exactly one sign change for every \(0<w<1\): its \(x^6,x^5,x^4,x^3\) coefficients are positive, its \(x,x^0\) coefficients are negative, and the \(x^2\) coefficient may have either sign. Descartes' rule of signs yields at most one positive root. Its negative constant and positive leading term yield at least one, hence precisely \(\beta_w\).

**4. Strict root ordering without resultants.** From (1), put \(z=(G_{00}/h)-1>0\) and \(v=(x+2)^{-2}\). Then \(G_{11}=h(1+vz)\). At \(x=\alpha_w\), identity (3) gives \(R_B=R_C\), so (2) implies \((vz)'=0\). Since \(v'<0\), this forces \(z'>0\). Consequently
\[
R_A-R_C=-\frac{z'}{1+z}<0
\quad\text{at }x=\alpha_w.
\]
Thus \(R_B>R_A\) at \(\alpha_w\); by the unique sign crossing for \(R_B-R_A\) in (3), necessarily \(\alpha_w<\beta_w\).

**5. Exhaustive optimum and ties.** For \(x<\alpha_w\), (3) gives \(R_C>R_B>R_A\). On \((\alpha_w,\beta_w)\), \(R_B\) exceeds both alternatives. For \(x>\beta_w\), \(R_A>R_B>R_C\). At \(\alpha_w\) only \(R_B=R_C>R_A\); at \(\beta_w\) only \(R_A=R_B>R_C\). Since the reflection has exactly the three orbits \(A,B,C\), these comparisons cover all five candidates. Finally, a three- or four-cycle with a single exceptional edge has at most two reflection orbits, proving the stated minimality *within this family*.

## Verification

Run `python verify.py` with SymPy installed. It reconstructs the full five-by-five inverse symbolically; proves (1) and both identities (3) by exact cancellation; checks exact rational sign brackets for \(w=1/2\); and performs direct exact-rational comparisons for 210 screening/weight parameter pairs. The current checker passes 871 assertions/check groups. Numerical root sampling is supplementary and is not substituted for the derivative, Descartes, and ordering arguments proving the universal statements.

## Relationship to prior work

Belabbas and Wolfe (2009, preprint first public June 24, 2009) give the general Nyström trace-residual formula, rank-restricted landmark framework, and determinant-based selection theory. Krause, Singh and Guestrin (2008) compare entropy-, variance- and other Gaussian sensor design criteria for broad covariance models. Neither of the inspected primary treatments classifies screening-dependent optimizers for one weakened edge on a five-cycle. The exact first/second crossing polynomials, their ordering for *all* \(0<w<1\), and the complete tie classifications constitute the narrower claim here; generic Schur complement and inverse derivative identities are prior mathematical tools, not claimed as new. A cyclic graph with all edges equal is vertex-transitive and has no such distinct landmark migration.

## Limitations

The theorem is confined to one defective edge on a five-cycle and one noiseless selected vertex. It does not imply the same ordering for larger cycles, multiple landmarks, noisy measurements, strengthening the exceptional edge, or nonuniform vertex killing. It does not assert that determinant optimization and trace optimization are equivalent measures. Any publication-priority conclusion remains limited by available indexing and primary literature inspection; the stated proof has not undergone independent mathematical audit.

## References

1. M.-A. Belabbas and P. J. Wolfe, *On landmark selection and sampling in high-dimensional data analysis*, arXiv:0906.4582 (first submitted 2009-06-24), https://arxiv.org/abs/0906.4582 . In particular Sections 3.2 and 4.1--4.2.
2. A. Krause, A. Singh, and C. Guestrin, *Near-Optimal Sensor Placements in Gaussian Processes: Theory, Efficient Algorithms and Empirical Studies*, Journal of Machine Learning Research 9 (2008), 235--284, https://www.cs.cmu.edu/~guestrin/Publications/JMLR08SensorPlace/jmlr08-sensor-place.pdf . In particular Sections 1 and 9.5.
