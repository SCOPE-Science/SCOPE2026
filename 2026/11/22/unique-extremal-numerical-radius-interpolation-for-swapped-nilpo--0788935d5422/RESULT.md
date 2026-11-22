# Unique extremal numerical-radius interpolation for swapped nilpotent targets

## Finding

For every \(0<t<2\), let \(E_{12},E_{21}\in M_2(\mathbb C)\) be matrix units and let \(\lambda_1\ne\lambda_2\) lie in the unit disk. Define their pseudohyperbolic separation by
\[
\rho(\lambda_1,\lambda_2)=\left|\frac{\lambda_1-\lambda_2}{1-\overline{\lambda_1}\lambda_2}\right|.
\]
There is a holomorphic \(F:\mathbb D\to M_2(\mathbb C)\) with \(\sup_{z\in\mathbb D}w(F(z))\le1\) and
\[
F(\lambda_1)=tE_{12},\qquad F(\lambda_2)=tE_{21}
\]
if and only if
\[
\rho(\lambda_1,\lambda_2)\ge\rho_t:=\frac{4t}{4+t^2}.
\]
At equality, **the entire matrix-valued interpolant is unique**, not merely one scalar matrix entry. At strict inequality a strict numerical-radius interpolant exists and there are infinitely many different admissible interpolants. Thus the exact solvability threshold is also a transition from a unique boundary extremizer to a nontrivial family.

Normalize the critical nodes via a disk automorphism to \((-q,q)\), where \(q=t/2\in(0,1)\). The unique critical interpolant in these coordinates is
\[
U_q(z)=\begin{pmatrix}
0& a_q(1+z^2)-z\\
a_q(1+z^2)+z&0
\end{pmatrix},\qquad a_q=\frac{q}{1+q^2}.
\]
Any other critical ordered pair is handled by precomposition with the appropriate disk automorphism.

## Assumptions and scope

All matrices are complex \(2\times2\); \(w(M)=\sup_{\|v\|_2=1}|\langle Mv,v\rangle|\) denotes numerical radius. Solutions are **arbitrary** bounded holomorphic matrix functions; they need not be off diagonal, rational, or polynomial. The amplitude is real and strictly between zero and two, and the nodes are distinct interior disk points. Unitary phase variants follow by unitary conjugation and common scalar phases, but no asymmetric-amplitude classification is claimed.

## Proof

**1. A scalar necessary bound.** For any \(2\times2\) matrix \(M\), the scalar functional \((M_{21}-M_{12})/2\) has absolute value at most \(w(M)\): apply numerical-radius bounds to the unit vectors \((1,i)/\sqrt2\) and \((1,-i)/\sqrt2\) and take half their difference. Consequently
\[
h(z)=\frac{F_{21}(z)-F_{12}(z)}2
\]
is a scalar Schur function whose values at the prescribed nodes are \(-q\) and \(q\). Schwarz--Pick gives \(\rho(\lambda_1,\lambda_2)\ge 2q/(1+q^2)=\rho_t\).

**2. Attainment.** Every pair at pseudohyperbolic distance \(2q/(1+q^2)\) can be sent by a disk automorphism to \((-q,q)\), preserving the order. Direct substitution gives \(U_q(-q)=2qE_{12}\) and \(U_q(q)=2qE_{21}\). The elementary identity
\[
w\begin{pmatrix}0&b\\c&0\end{pmatrix}=\frac{|b|+|c|}{2}
\]
implies that, for \(|z|=1\),
\[
w(U_q(z))=\frac{|2a_q\cos\theta-1|+|2a_q\cos\theta+1|}{2}=1,
\quad z=e^{i\theta},
\]
because \(2a_q<1\). The maximum principle applied to the scalar functions \(\langle U_q(z)v,v\rangle\), uniformly over unit vectors \(v\), therefore gives \(\sup_{\mathbb D} w(U_q)\le1\).

**3. Rigidity at equality.** Pull back an arbitrary admissible critical solution to the normalized points \((-q,q)\) and continue to call it \(F\). The Schwarz--Pick equality case, with \(h(-q)=-q\) and \(h(q)=q\), forces \(h(z)=z\) identically. The entries of \(F\) have bounded radial boundary values almost everywhere. Write \(c(z)=(F_{11}(z)+F_{22}(z))/2\). For \(u_\pm=(1,\pm i)/\sqrt2\), their scalar expectations have boundary values \(c(z)\pm iz\) (up to exchanging the signs). At \(|z|=1\), both have modulus at most one. Summing the two squares shows \(2|c(z)|^2+2\le2\), so \(c=0\) almost everywhere and hence identically.

Put \(D=F_{11}=-F_{22}\) and \(J=(F_{12}+F_{21})/2\). Then
\[
F(z)=\begin{pmatrix}D(z)&J(z)-z\\J(z)+z&-D(z)\end{pmatrix}.
\]
For almost every boundary \(z\), divide this matrix by \(z\); this does not change its numerical radius. The two vectors \(u_\pm\) give equality in the extremal constraints on the imaginary part of this divided matrix. As \(I\pm\operatorname{Im}(F(z)/z)\succeq0\), equality of a quadratic form for a positive matrix forces its vector into the kernel. Reading the first coordinate of the resulting vector equation gives
\[
\operatorname{Im}(D(z)/z)=0,\qquad \operatorname{Im}(J(z)/z)=0
\]
for almost every unit-circle \(z\). (Equivalently, insert the displayed matrix and \(u_+=(1,i)/\sqrt2\) into \((I+\operatorname{Im}(F(z)/z))u_+=0\).)

**4. Boundary Fourier rigidity.** If a bounded holomorphic \(g(z)=\sum_{k\ge0}g_kz^k\) has \(g(z)/z\) real almost everywhere on the unit circle, comparison of the positive and negative Fourier coefficients shows
\[
g(z)=\alpha+\beta z+\overline\alpha z^2,\quad \beta\in\mathbb R.
\]
Apply this separately to \(D,J\). The interpolation data give \(D(\pm q)=0\) and \(J(\pm q)=q\). Subtracting the two values forces each linear coefficient to vanish. As \(0<q<1\), the remaining equations yield \(D\equiv0\) and \(J(z)=q(1+z^2)/(1+q^2)\). Therefore \(F=U_q\), proving uniqueness without an a priori off-diagonal restriction.

**5. Beyond threshold.** For a pair of pseudohyperbolic separation greater than \(\rho_t\), normalize it to \((-s,s)\) with \(s>q\). The analytic function \(V(z)=U_q((q/s)z)\) gives the prescribed values. Since \(q/s<1\) and \(w(U_q(0))=a_q<1\), the strong maximum principle gives \(\sup_{\mathbb D}w(V)<1\). Small independent analytic perturbations that vanish at the two nodes, for example \(\epsilon(z^2-s^2)E_{12}\), preserve the strict bound when \(\epsilon\) is sufficiently small, giving infinitely many interpolants.

## Verification

The explicit polynomial, its boundary numerical-radius identity, both interpolation values, and the strict-contraction construction were independently checked by finite numerical diagnostics in `diagnostic.py` (4,998 assertions). These are sanity checks only. The global necessity, boundary rigidity, and uniqueness follow from the analytic proof above rather than from finite sampling.

## Relationship to prior work

Ahmed, Bhowmik, Das and Sau (arXiv:2611.19189v1, Examples 2.5 and 4.6) already demonstrate non-solvability at nodes \((0,1/2)\) and solvability at \((0,4/5)\) for the unit-amplitude swapped nilpotent targets; they give one rational extremal interpolant and force the scalar off-diagonal difference by Schwarz--Pick equality. **Those examples, the scalar bound, and existence at unit amplitude are not new here.** The present result is a sharp all-amplitude solvability/uniqueness trichotomy, including rigidity of both diagonal entries and the symmetric off-diagonal sum for the *entire* matrix-valued analytic solution, rather than one constructed interpolant. Piekarz (arXiv:2509.09579v1) concerns uniqueness for scalar-valued three-point interpolation on a Euclidean ball, a different source/target geometry and interpolation problem.

## Limitations

No asymmetric pair of nilpotent amplitudes, higher matrix sizes, or multivariate source domains are addressed. The proof relies on complex Hilbert-space numerical radius and one-dimensional disk boundary Fourier rigidity. The general structural factorization results in the motivating paper could subsume the explicit solvability portion, but its examined examples do not explicitly classify all full-matrix extremizers. Undetected prior implicit coverage by general complex-geodesic or interpolation rigidity theory remains possible; absence of a search hit is not a proof of novelty. Independent validation has not been performed.

## References

1. H. Ahmed, M. Bhowmik, B. K. Das and H. Sau, *Interpolation, Factorization, and Approximation in the Numerical Radius Unit Ball*, arXiv:2611.19189v1 (first posted 2026-11-14), https://arxiv.org/html/2611.19189v1. Particularly §§2 and 4.3.
2. D. Piekarz, *The uniqueness problem for the 3-Point Nevanlinna-Pick extremal interpolation problem in the unit Euclidean ball*, arXiv:2509.09579v1 (2025-09-11), https://arxiv.org/html/2509.09579v1.
3. Classical scalar Schwarz--Pick theorem and its equality case; classical Fatou radial-limit and Fourier-uniqueness theorems.
