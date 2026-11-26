# A sharp angle-uniform inverse-sensitivity frontier for planar vector play

## Finding
For the planar sliding-cell tangent map \(J=I+AP\), with
\[
 A=\alpha I+(\tau-\alpha)hh^{\mathsf T},\qquad
 P=\gamma I+(1-\gamma)rr^{\mathsf T},
\]
where \(h,r\in\mathbb R^2\) are unit vectors, \(\alpha\ge\tau>0\), and \(0<\gamma<1\), the inverse \(J^{-1}\) is nonexpansive in the Euclidean norm at **every** relative angle of the unit vectors if and only if
\[
 \boxed{(1-\gamma)^2(\alpha-\tau)^2
 \le 4\alpha\tau\gamma\,[4+(\alpha+\tau)(1+\gamma)].}
\]
If \(\alpha>\tau\), there is a unique equality threshold \(\gamma_*\in(0,1)\). For \(\gamma<\gamma_*\), at least one angle has \(\lVert J^{-1}\rVert_2>1\); for \(\gamma>\gamma_*\), every angle has \(\lVert J^{-1}\rVert_2<1\). At equality, a worst angle \(\theta_*\) between \(h\) and \(r\) satisfies
\[
 \cos(2\theta_*)=\frac{2\alpha\tau\gamma_*}{(\alpha-\tau)(1-\gamma_*)}\in(0,1),
 \qquad \lVert J(\theta_*)^{-1}\rVert_2=1.
\]
If \(\alpha=\tau\), every admissible angle and every \(\gamma>0\) give strict inverse contraction.

This is a *local inverse-conditioning* boundary, not an assertion of global invertibility of a nonlinear constitutive operator or convergence of a complete Newton algorithm.

## Assumptions and scope
Work in \(\mathbb R^2\) with its ordinary Euclidean norm. \(A\) is a symmetric positive-definite differential-susceptibility matrix with tangent and secant eigenvalues \(\tau\) and \(\alpha\). \(P\) is a symmetric positive-definite sliding-response matrix with radial and transverse eigenvalues \(1\) and \(\gamma\). The ordered product \(AP\), rather than the symmetrized product, is the linearized response. Since \(AP\) is similar to the positive-definite matrix \(P^{1/2}AP^{1/2}\), \(J=I+AP\) is invertible and has real eigenvalues greater than one. Those eigenvalues alone do not determine Euclidean inverse sensitivity because \(AP\) need not be normal. Angles are unrestricted, apart from \(h,r\) being unit vectors.

## Proof
Use an orthogonal coordinate change taking \(r\) to the first basis vector and write \(h=(\cos\theta,\sin\theta)^{\mathsf T}\). Set \(d=\alpha\tau\), \(D=\alpha-\tau\), \(S=\alpha+\tau\), and write
\[
 A=\begin{pmatrix}u&b\\ b&v\end{pmatrix},\quad
 u=\frac{S-D\cos(2\theta)}2,\quad
 v=\frac{S+D\cos(2\theta)}2,\quad
 b=(\tau-\alpha)\cos\theta\sin\theta.
\]
In particular \(uv-b^2=d\). The normalized sliding response is \(P=\operatorname{diag}(1,\gamma)\), hence
\[
 J=\begin{pmatrix}1+u&\gamma b\\b&1+\gamma v\end{pmatrix},
 \qquad \det J=1+u+\gamma(v+d)>0.
\]
The condition \(\lVert J^{-1}\rVert_2\le1\) is equivalent to \(J^{\mathsf T}J-I\succeq0\). Its trace is strictly positive, since \(\lVert J\rVert_F^2>2\) (in fact \(u,v>0\)). For a symmetric two-by-two matrix with positive trace, nonnegative determinant is equivalent to positive semidefiniteness. Using \(\det(J^{\mathsf T}J-I)=(\det J)^2-\lVert J\rVert_F^2+1\) and \(uv-b^2=d\), direct expansion gives
\[
 q(\theta):=\det(J^{\mathsf T}J-I)
 =d\gamma[4+2u+\gamma(2v+d)]-(1-\gamma)^2b^2.
\]
Put \(z=\cos(2\theta)\in[-1,1]\). Then \(b^2=D^2(1-z^2)/4\), so
\[
 q(z)=Kz^2-Lz+C-K,\quad
 K=\frac{(1-\gamma)^2D^2}{4},\quad
 L=d\gamma D(1-\gamma),\quad
 C=d\gamma[4+S(1+\gamma)+\gamma d].
\]
For \(D=0\) the expression is strictly positive. Suppose \(D>0\). The parabola's unconstrained minimizer is
\[
 z_0=\frac{L}{2K}=\frac{2d\gamma}{D(1-\gamma)}>0,
\]
and its minimum is
\[
 F:=q(z_0)=d\gamma[4+S(1+\gamma)]-\frac{(1-\gamma)^2D^2}{4}.
\]
When \(F\ge0\), every \(z\in[-1,1]\) has \(q(z)\ge0\), proving uniform inverse nonexpansivity. Conversely, if \(F\le0\), necessarily \(z_0<1\): if \(z_0\ge1\), then \(D(1-\gamma)\le2d\gamma\), whence \(K\le d\gamma D(1-\gamma)/2\), and thus
\[
 F\ge d\gamma\left[4+S(1+\gamma)-\frac{D(1-\gamma)}2\right]>0,
\]
a contradiction. Therefore whenever \(F<0\), the attainable angle \(z=z_0\) makes \(q<0\) and \(\lVert J^{-1}\rVert_2>1\); when \(F=0\), the same attainable angle makes \(\lVert J^{-1}\rVert_2=1\). Thus \(F\ge0\) is necessary and sufficient. Multiplying by four yields the displayed inequality. Finally
\[
 F'(\gamma)=d[4+S(1+2\gamma)]+\frac{D^2(1-\gamma)}2>0
\]
for \(0<\gamma<1\). Since \(F(0^+)=-D^2/4<0\) and \(F(1)=d(4+2S)>0\), the threshold exists uniquely. Strict positivity away from it implies strict contraction at every angle.

An explicit strictly monotone forward derivative can still have an expansive inverse. Choose \(\alpha=4\), \(\tau=1\), \(\gamma=1/50\), \(h=(1,1)^{\mathsf T}/\sqrt2\), and \(r=(1,0)^{\mathsf T}\). Then
\[
 J=\begin{pmatrix}\tfrac72&-\tfrac3{100}\\-\tfrac32&\tfrac{21}{20}\end{pmatrix},\qquad
 \det(J^{\mathsf T}J-I)=-\tfrac{2853}{2000}<0.
\]
But \(\operatorname{sym}J=(J+J^{\mathsf T})/2\) is positive definite: its first diagonal entry is \(7/2>0\) and its determinant is \(123591/40000>0\). Therefore local strict monotonicity does not guarantee Euclidean inverse nonexpansivity. A nonnegative increasing concave constitutive response realizing the two susceptibilities is \(M(s)=16s/(1+3s)\) at \(s=1\), where \(M(1)=4\) and \(M'(1)=1\). The critical sliding factor for this example is approximately \(\gamma_*=0.0542649822871\), whereas its \(\gamma=0.02\) has \(\lVert J^{-1}\rVert_2\approx1.0564825341\).

## Verification
Run `python3 verify_inverse_frontier.py` using Python's standard library. Its output is `VERIFY_OK 1734`: 1,729 reproducible exact-rational cases checking the determinant identity and threshold implications, plus five fixed exact example conditions. These finite checks supplement, but do not replace, the unrestricted analytical proof. The numerical threshold and sample norm are illustrations, not proof dependencies.

## Relationship to prior work
Cibicki, Roppert and Kaltenbacher (2026) introduce the planar vector-play tangent model and analyze loss of monotonicity and its consequences for Newton-type solvers; the current theorem instead concerns the exact *Euclidean norm of the inverse derivative* uniformly over all relative angles. Moll and collaborators (2025) treat forward/inverse constitutive evaluation in a different energy-based magnetic hysteresis setting and do not supply this angle-uniform vector-play criterion. Published spectral and nonnormal-iteration examples illuminate why eigenvalue positivity is insufficient but do not imply the quantitative scalar frontier above.

## Limitations
The claim is restricted to a *single planar sliding cell* and to the stated positive-definite secant/tangent regime. Superpositions of cells, discrete nonlinear Newton basins, finite-precision errors, and globally Lipschitz inverse mappings require separate analysis. The literature comparison cannot rule out an unindexed earlier equivalent formula. No independent mathematical audit has been performed.

## References
1. Cibicki, Roppert, Kaltenbacher, *Loss of Monotonicity in the Vector Play Model and Consequences for Newton-Type Solvers*, arXiv:2611.00168v1, first submitted 2026-10-30, https://arxiv.org/abs/2611.00168.
2. Moll et al., *A Dynamic Energy-Based Hysteresis Model for Pulsed-Operated Fast-Ramping Magnets*, arXiv:2509.04115, https://arxiv.org/abs/2509.04115.
3. Egger et al., *On forward and inverse energy-based magnetic vector hysteresis operators*, IEEE Transactions on Magnetics (2025), DOI:10.1109/TMAG.2025.3544507.
