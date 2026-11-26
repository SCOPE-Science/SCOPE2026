# Exact second-bound-state threshold and onset law for the sphere-point hybrid rank-one model
## Finding
Consider the three-dimensional rank-one hybrid interaction consisting of a sphere of radius \(R\) and a point at distance \(a>R\) from its center. Let \(\mu>0\) be the point-interaction scale and \(\lambda_2>0\) the spherical coupling in the normalization of Erman, Seymen, and Turgut. For energy \(E=-\nu^2<0\), the source gives the principal matrix
\[
\Phi(\nu)=\begin{pmatrix}
\dfrac{\nu-\mu}{4\pi} & -\dfrac{e^{-\nu a}\sinh(\nu R)}{4\pi\nu aR}\\[5pt]
-\dfrac{e^{-\nu a}\sinh(\nu R)}{4\pi\nu aR} & \dfrac1{\lambda_2}-\dfrac{e^{-\nu R}\sinh(\nu R)}{4\pi\nu R^2}
\end{pmatrix}.
\]
Define
\[
D=\frac{\mu}{R}-\frac{4\pi\mu}{\lambda_2}-\frac1{a^2}.
\]
Then there are exactly two negative eigenvalues if and only if \(D>0\), and exactly one if and only if \(D\le0\). Equivalently, a second bound state is possible exactly when \(\mu a^2>R\), and then its sharp coupling threshold is
\[
\lambda_c=\frac{4\pi\mu Ra^2}{\mu a^2-R},\qquad
\text{with two bound states exactly for }\lambda_2>\lambda_c.
\]

For fixed \(\mu,R,a\) with \(\mu a^2>R\), let \(E_2(\lambda_2)<0\) be the second bound-state energy. When \(\lambda_2\downarrow\lambda_c\), equivalently \(D\downarrow0\),
\[
E_2(\lambda_2)\sim-
\left(\frac{a^2\mu}{(a\mu-1)^2}\right)^2D^2
\quad\text{if }a\mu\ne1.
\]
On the exceptional locus \(a\mu=1\), the leading order changes to
\[
E_2(\lambda_2)\sim-
\frac{3a^2}{R^2-2aR+3a^2}\,D.
\]
Thus the second level has quadratic generic onset and linear onset on a natural codimension-one resonance locus.

## Assumptions and scope
The statement uses the exact principal-matrix normalization of arXiv:2202.10599v1. The geometry is three-dimensional, the sphere and point are disjoint with \(a>R\), and \(R,a,\mu,\lambda_2\) are positive. The result concerns only negative discrete spectrum. The asymptotic laws vary \(\lambda_2\) at fixed \(\mu,R,a\); no claim is made about mixed multi-parameter approaches to the threshold.

## Proof
At \(\nu=0\), continuity of the matrix entries gives
\[
\Phi(0)=\frac1{4\pi}
\begin{pmatrix}
-\mu & -a^{-1}\\
-a^{-1} & 4\pi\lambda_2^{-1}-R^{-1}
\end{pmatrix},
\qquad
\det\Phi(0)=\frac{D}{16\pi^2}.
\]
The first diagonal entry is strictly negative. Hence \(D>0\) is equivalent to \(\Phi(0)\) being negative definite, while \(D<0\) gives one negative and one positive eigenvalue; at \(D=0\) the inertia is one negative and one zero.

The principal matrix is the Birman--Schwinger matrix for two linearly independent rank-one form factors. Differentiating the resolvent representation at energy \(-\nu^2\) gives, for \(\nu>0\),
\[
\Phi'(\nu)=2\nu\big(\langle f_i,(p^2+\nu^2)^{-2}f_j\rangle\big)_{i,j=1}^2.
\]
Because the point and spherical form factors are linearly independent when \(a>R\), this Gram matrix is positive definite. Thus both eigenvalues of \(\Phi(\nu)\) are strictly increasing functions of \(\nu\). Moreover,
\[
\Phi_{11}(\nu)\to+\infty,
\qquad
\Phi_{22}(\nu)\to\lambda_2^{-1}>0,
\qquad
\Phi_{12}(\nu)\to0
\]
as \(\nu\to\infty\). Therefore each negative eigenvalue of \(\Phi(0)\) crosses zero exactly once for positive \(\nu\). At \(D=0\), the zero eigenvalue of \(\Phi(0)\) increases immediately and produces no negative-energy state. This proves the exact count criterion.

Solving \(D>0\) for \(\lambda_2\) gives the stated threshold. If \(\mu a^2\le R\), even the limit \(\lambda_2\to\infty\) leaves \(D\le0\), so a second state is impossible.

For the threshold law, expand the determinant at \(\nu=0\), with fixed \(\mu,R,a\) and \(\lambda_2\) close to \(\lambda_c\):
\[
\det\Phi(\nu)=
\frac{D}{16\pi^2}
-
\frac{(a\mu-1)^2}{16\pi^2a^2\mu}\,\nu
+O(\nu^2)+O(D\nu).
\]
If \(a\mu\ne1\), the small positive zero is therefore
\[
\nu_2\sim\frac{a^2\mu}{(a\mu-1)^2}D,
\]
and \(E_2=-\nu_2^2\) gives the quadratic law.

If \(a\mu=1\), the linear coefficient vanishes. At \(D=0\), the quadratic coefficient is
\[
-\frac{R^2-2aR+3a^2}{48\pi^2a^2},
\]
which is strictly negative because \(R^2-2aR+3a^2=(a-R)^2+2a^2\). Hence
\[
\nu_2^2\sim
\frac{3a^2}{R^2-2aR+3a^2}D,
\]
and the linear energy onset follows.

## Verification
Symbolic expansion of the exact determinant reproduces \(\det\Phi(0)=D/(16\pi^2)\), the generic linear-in-\(\nu\) coefficient, and the exceptional quadratic coefficient above. A standalone checker included with this result evaluates the source's Figure 6 parameter choices \(R=\mu=1\), \(a=2\): \(\lambda_2=10\) has one positive determinant zero, while \(\lambda_2=20\) has two. It also numerically checks the generic coefficient \(-16\) for \(R=\mu=1,a=2\) and the exceptional coefficient \(-4/3\) for \(R=1,a=2,\mu=1/2\). These computations corroborate, but do not replace, the analytic proof.

## Relationship to prior work
The primary article gives the principal matrix, proves that the model has at least one and at most two bound states, and displays numerical examples in which changing \(\lambda_2\) changes the count from one to two. It does not state the exact inequality \(D>0\), the closed-form critical coupling above, or the two threshold-onset exponents in the inspected bound-state section.

Earlier solvable sphere-interaction work by Antoine, Gesztesy, and Shabani studies local sphere interactions and a point interaction at the sphere center, which is a different interaction and geometry. A later paper on rank-one interactions supported by deformed hyperspheres studies a single hypersurface-supported interaction rather than the sphere-plus-exterior-point hybrid considered here.

## Limitations
The proof uses strict positive eigenvalue flow of the two-by-two principal matrix and the source normalization. It does not address positive-energy resonances, embedded spectrum, higher-rank surface form factors, or deformed spheres. The threshold asymptotics are one-parameter asymptotics at fixed \(R,a,\mu\). No claim of exhaustive historical priority is made beyond the literature and database comparisons documented in the accompanying review.

## References
1. F. Erman, S. Seymen, and O. T. Turgut, “Rank One Perturbations Supported by Hybrid Geometries and Their Deformations,” arXiv:2202.10599v1; J. Math. Phys. 63, 123505 (2022), DOI 10.1063/5.0090401.
2. J.-P. Antoine, F. Gesztesy, and J. Shabani, “Exactly solvable models of sphere interactions in quantum mechanics,” J. Phys. A 20 (1987), 3687–3712, DOI 10.1088/0305-4470/20/12/022.
3. D. Demirdöğen, F. Erman, and M. Sayar, “Bound State Analysis of Rank-One Delta Interactions Supported by Deformed Hyperspheres,” arXiv:2608.24508.
