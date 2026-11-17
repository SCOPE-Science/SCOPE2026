# Sharp rare-obtuse asymptotics and the marked boundary layer of random ball triangles

## Finding
Let \(A_d,B_d,C_d\) be three independent points sampled uniformly by Euclidean volume from the unit ball of \(\mathbb R^d\), with \(d\ge3\). Then, as \(d\to\infty\),
\[
\Pr\{\triangle A_dB_dC_d\text{ is obtuse}\}
\sim\frac{\sqrt6}{4}\left(\frac{16}{27}\right)^{d/2}.
\]
The marked limit is more informative than this marginal asymptotic. Conditionally on a unique obtuse angle at \(A_d\), put \(G_{ij}=X_i\cdot X_j\) for \((X_1,X_2,X_3)=(A_d,B_d,C_d)\), and define
\[
\begin{aligned}
T_d&=\sqrt d\,(1-G_{11}),&P_d&=\sqrt d\,(G_{12}-1/3),\\
Q_d&=\sqrt d\,(G_{13}-1/3),&Z_d&=d(-G_{11}+G_{12}+G_{13}-G_{23}),\\
U_d&=d(1-G_{22}),&V_d&=d(1-G_{33}).
\end{aligned}
\]
The vector \((T_d,P_d,Q_d,Z_d,U_d,V_d)\) converges **in total variation** to the following six-dimensional law: \(T\) is half-normal with parent variance \(8/9\); given \(T=t\), \((P,Q)\) is bivariate normal with mean \((-t/2,-t/2)\), both variances \(16/27\), and covariance \(-8/27\); and \(Z,U,V\) are three independent exponential variables of rate \(3/4\), jointly independent of \((T,P,Q)\). In particular,
\[
\Pr\{\sqrt d(1-\|A_d\|^2)>t\mid A_d\text{ is obtuse}\}
\longrightarrow\operatorname{erfc}(3t/4),\qquad t\ge0.
\]
The same statement holds, by relabeling, at either other vertex. The three disjoint obtuse-vertex events have equal probabilities.

## Assumptions and scope
All three vertices are independent, with the continuous **volume-uniform** law on the closed Euclidean unit ball. An obtuse angle means a Euclidean internal angle strictly greater than \(\pi/2\), not an intrinsic spherical angle. Zero-probability collinear and right-angle configurations are immaterial. The result concerns the fixed three-point model and dimension tending to infinity. Convergence in total variation is for the displayed six real Gram-coordinate marks, not for ambient-dimensional vertex vectors.

## Proof
**1. Exact Gram density.** For \(d\ge3\), the six independent entries of the symmetric Gram matrix \(G=(X_i\cdot X_j)_{1\le i,j\le3}\) have density proportional to \((\det G)^{(d-4)/2}\) on the positive-definite matrices satisfying \(0<G_{ii}<1\). Writing the diagonal as \(r_i^2\) and the off-diagonal entries as \(r_i r_j\rho_{ij}\), the exact normalization integral is
\[
I_d=\int_{G\succ0,\,G_{ii}<1}(\det G)^{(d-4)/2}\,dG
=\frac{8\pi^{3/2}}{d^3}
\frac{\Gamma((d-1)/2)\Gamma((d-2)/2)}{\Gamma(d/2)^2}.
\]
Indeed, the three independent radial-square integrations each contribute \(2/d\). The correlation-matrix determinant integral separates, after the substitution \(\rho_{23}=\rho_{12}\rho_{13}+\sqrt{(1-\rho_{12}^2)(1-\rho_{13}^2)}\,s\), into two beta integrals \(B(1/2,(d-1)/2)\) and one \(B(1/2,(d-2)/2)\). Stirling's formula gives \(I_d\sim16\sqrt2\pi^{3/2}d^{-9/2}\).

**2. The uniquely dominant constrained Gram matrix.** The angle at \(A_d\) is obtuse exactly when
\[
F(G):=G_{11}-G_{12}-G_{13}+G_{23}<0.
\]
On this region \(\det G\) has the unique maximizer
\[
G_*=
\begin{pmatrix}
1&1/3&1/3\\
1/3&1&-1/3\\
1/3&-1/3&1
\end{pmatrix},\qquad\det G_*=16/27.
\]
The inverse matrix is
\[
G_*^{-1}=\begin{pmatrix}
3/2&-3/4&-3/4\\
-3/4&3/2&3/4\\
-3/4&3/4&3/2
\end{pmatrix}.
\]
For independent symmetric-matrix coordinates, its supporting gradient gives
\[
\log\det G\le\log(16/27)+\tfrac32F(G)+\tfrac32(G_{22}-1)+\tfrac32(G_{33}-1).
\]
All three terms on the right are nonpositive on the feasible region. Strict concavity of \(\log\det\) proves uniqueness. Singular matrices have zero determinant and cannot maximize.

**3. Mixed boundary scales and exact Hessian.** Set \(G_{11}=1-t/\sqrt d\), \(G_{12}=1/3+p/\sqrt d\), \(G_{13}=1/3+q/\sqrt d\), \(G_{22}=1-u/d\), \(G_{33}=1-v/d\), and \(G_{23}=-G_{11}+G_{12}+G_{13}-z/d\), with \(t,u,v,z\ge0\). The Jacobian is exactly \(d^{-9/2}\). Uniformly on bounded transformed coordinates,
\[
\frac{d-4}{2}\log\frac{\det G}{16/27}
=-\frac34(z+u+v)-\frac14 Q(t,p,q)+o(1),
\]
where
\[
Q(t,p,q)=\frac{45}{8}t^2+\frac{27}{4}t(p+q)
+\frac92(p^2+pq+q^2).
\]
This is a positive-definite quadratic form. Its coefficient matrix, with coordinate order \((t,p,q)\), is
\[
M=\begin{pmatrix}
45/8&27/8&27/8\\
27/8&9/2&9/4\\
27/8&9/4&9/2
\end{pmatrix},\qquad \det M=2187/64.
\]
Since the exponent is \(-\tfrac14(t,p,q)M(t,p,q)^\mathsf T\), the associated unrestricted Gaussian covariance is \(2M^{-1}\). Restricting to \(t\ge0\), its \(t\)-marginal is half-normal with variance \(8/9\); Gaussian conditioning gives the asserted mean, variances and covariance for \((p,q)\).

**4. Integration and total variation.** The limiting local integral is
\[
J=\left(\frac43\right)^3\int_{t\ge0}\int_{\mathbb R^2}
\exp[-Q(t,p,q)/4] \,dp\,dq\,dt
=\left(\frac43\right)^3\frac{32\sqrt3\pi^{3/2}}{81}.
\]
The three factors \(4/3\) come from the active one-sided constraints \(z,u,v\). Uniqueness of the determinant maximizer and strict negative definiteness of the tangent Hessian permit the standard boundary Laplace argument: outside a fixed neighborhood the determinant has a strictly smaller maximum, and inside it the local quadratic and one-sided linear bounds dominate the rescaled integrals. Thus
\[
\Pr\{F(G)<0\}
\sim\frac{Jd^{-9/2}(16/27)^{(d-4)/2}}{I_d}
=\frac{\sqrt6}{12}\left(\frac{16}{27}\right)^{d/2}.
\]
An ordinary triangle has at most one obtuse angle. Summing the three disjoint vertex events gives the probability constant \(\sqrt6/4\). After the same change of variables, the normalized conditional densities converge pointwise almost everywhere to the stated product of the truncated Gaussian and three exponential densities. Their integrals converge to one by the Laplace calculation. Scheffé's lemma therefore upgrades the marked convergence to total variation.

## Verification
A standalone checker `verify_ball_obtuse.py` validates the determinant and inverse identities, the positive-definite Hessian and normalization coefficient, and performs independent numerical importance integration using the **exact finite-dimensional Gram density**. It also samples random triangles in low dimensions and compares their acute probabilities with the published exact two- and three-dimensional values. Numerical integration supports but does not prove the limiting assertion. The exact probability and marked asymptotics rest on the analytic argument above.

## Relationship to prior work
G. R. Hall's *Acute triangles in the n-ball* (1982) gives an all-dimension integral formula for the **marginal acute-triangle probability**, including exact dimensions two and three. The present marginal asymptotic may also be extracted from such a formula and is not claimed to supersede it. The assessed result is the explicit **six-dimensional conditional Gram-coordinate law**, particularly the anomalous half-normal radial depth of the obtuse vertex and the independent exponential marks of the other vertices and the angle slack. Published research on surface-uniform spherical triangles has a different sampling measure and a \(d^{-1/2}\) prefactor at the same exponential rate; sphere points have no radial boundary layer. General Gram-density methods and Laplace's method are used as proof tools, not asserted as novel.

## Limitations
No finite-dimensional error bound or independent external mathematical audit is claimed. The result is specific to independent uniform samples in Euclidean balls, not to Gaussian samples or arbitrary radial distributions. Historical priority for the marked law is provisional: Hall's 1982 full text was not obtainable in this investigation, so the accessible abstract, cited results and indexed comparisons do not rule out unexamined specialized predecessor statements.

## References
1. G. R. Hall, *Acute triangles in the n-ball*, Journal of Applied Probability **19** (1982), 712–715, https://doi.org/10.2307/3213533. Abstract and bibliography accessible; full text not inspected.
2. E. Langford, *The probability that a random triangle is obtuse*, Biometrika **56** (1969), 689–690, https://doi.org/10.1093/biomet/56.3.689. Rectangle-sampling model, not the ball model.
3. A. J. Stam, *Limit theorems for uniform distributions on spheres in high-dimensional euclidean spaces*, Journal of Applied Probability **19** (1982), https://doi.org/10.2307/3213932. General high-dimensional background.
