# Sharp weighted two-point Neumann–Sobolev traces and a sensor saturation threshold

## Finding

Let \(\alpha\ge\beta>0\), \(r=\alpha/\beta\), and \(r_*=5-2\sqrt3\). For the real, arclength-mean-zero Sobolev space \(H=\{f\in H^1(0,1):\int_0^1 f(t)\,dt=0\}\), determine the minimum over two *distinct* sample points of the squared operator norm \(C_{\alpha,\beta}(x,y)^2\) in
\[
\alpha |f(x)|^2+\beta |f(y)|^2\le C_{\alpha,\beta}(x,y)^2\int_0^1|f'(t)|^2\,dt \qquad(f\in H).
\]
Put \(a_0=(1-\sqrt{2/3})/2\) and \(b_0=(1-1/\sqrt3)/2\).

**Low-imbalance phase.** For \(1\le r<r_*\), let \(a\in(0,a_0]\) be the unique solution of
\[
 r=\frac{b(a)^2+1/12}{a^2+1/12},\qquad
 b(a)=\frac{1-\sqrt{1/3+4a-4a^2}}2.
\]
Then the exact minimum and all minimizing *ordered* pairs (with the weight \(\alpha\) at the first coordinate) are
\[
 \boxed{\ \min_{x\ne y} C_{\alpha,\beta}(x,y)^2=\alpha(a^2+1/12)\ },\qquad
 (x,y)=(1/2-a,1/2+b(a))\ \text{or}\ (1/2+a,1/2-b(a)).
\]
At these sites the two weighted evaluation representers are orthogonal and have equal squared norm; equivalently their \(2\times2\) Gram matrix is scalar.

**Saturation phase.** For \(r\ge r_*\),
\[
 \boxed{\ \min_{x\ne y} C_{\alpha,\beta}(x,y)^2=\frac{\alpha}{12}\ },
\]
and the complete ordered minimizing family is \((x,y)=(1/2,1/2\pm b_0)\). The smaller-weight sensor remains at a fixed off-center location and cannot improve the cost beyond the individually optimal heavier sensor at the midpoint. For equal weights \(\alpha=\beta=\gamma>0\), the unique unordered design is \(\{1/\sqrt6,1-1/\sqrt6\}\), with squared constant \(\gamma(1-\sqrt{2/3})/2\). Swapping the original labels swaps the ordered coordinates accordingly.

## Assumptions and scope

The interval has unit length; \(f\) is real-valued, absolutely continuous, and mean zero with square-integrable weak derivative. Evaluation includes the endpoints. Both weights are strictly positive. Two sample locations must be distinct, and the displayed constant is the *squared* induced norm of the joint weighted evaluation operator, not a reconstruction-error criterion. The convention \(\alpha\ge\beta\) only fixes which sample receives the heavier weight; all unequal labeling is handled by swapping labels.

## Proof

**1. Reproducing kernel and exact norm reduction.** The derivative-energy inner product on \(H\) is a Hilbert inner product. The real symmetric reproducing kernel is
\[
 K(s,t)=\frac13-\max(s,t)+\frac{s^2+t^2}{2}.
\]
Indeed, \(\partial_tK(s,t)=t-\mathbf1_{t>s}\), hence integration by parts gives \(\int_0^1 f'(t)\partial_t K(s,t)\,dt=f(s)-\int_0^1f=f(s)\), and direct integration shows that \(K(s,\cdot)\) has mean zero. The squared norm \(C_{\alpha,\beta}(x,y)^2\) equals the largest eigenvalue of
\[
 G=\begin{pmatrix}
 \alpha K(x,x)&\sqrt{\alpha\beta}\,K(x,y)\\
 \sqrt{\alpha\beta}\,K(x,y)&\beta K(y,y)
\end{pmatrix}.
\]
For each \(t\in[0,1]\), the diagonal is \(K(t,t)=(t-1/2)^2+1/12\).

**2. Construction of the low-imbalance tight design.** By symmetry divide the matrix by \(\beta\) and place the heavier site at \(x=1/2-a\) and lighter at \(y=1/2+b\), with \(0\le a\le a_0\) and \(a\le b\le b_0\). The condition \(K(x,y)=0\) is exactly
\[
 a^2+b^2-a-b+1/6=0,
\]
whose relevant root is \(b=b(a)\) above. The diagonal-equality requirement is \(r(a^2+1/12)=b(a)^2+1/12\), giving \(r=R(a)\). The derivative of \(b(a)\) is strictly negative on the stated interval, whereas \(a^2+1/12\) is strictly increasing, so \(R\) decreases strictly from \(R(0)=5-2\sqrt3\) to \(R(a_0)=1\). Hence the stated \(a\) exists uniquely. The resulting matrix is exactly \(\alpha(a^2+1/12)I_2\).

**3. Global lower bound and rigidity in the low-imbalance phase.** For \(1\le r<r_*\), use the unique \(a>0\) and associated \(b\) above. Set \(x_0=1/2-a\), \(y_0=1/2+b\), and
\[
 L=\frac{\sqrt r\,a}{x_0},\qquad
 U=\frac{b}{\sqrt r(1-y_0)},\qquad
 u=\frac{U}{L+U},\qquad v=\frac{LU}{L+U},\qquad
 W=\begin{pmatrix}u&v\\v&1-u\end{pmatrix}.
\]
Here \(L,U>0\). Moreover \(v^2/[u(1-u)]=LU=ab/[x_0(1-y_0)]<1\); the last inequality follows from \(a+b<1/2\). Thus \(W\) is positive definite with trace \(1\). By reflection, it suffices to examine the triangle \(0\le x\le y\le1\). The following scalar quadratic is an exact lower bound for the largest eigenvalue of the rescaled Gram matrix:
\[
 \Phi(x,y)=\operatorname{tr}\!\left(W G_{r,1}(x,y)\right)
 =ur\bigl(x^2-x+1/3\bigr)+(1-u)\bigl(y^2-y+1/3\bigr)
 +2v\sqrt r\bigl(1/3-y+(x^2+y^2)/2\bigr).
\]
Because \(W\succeq0\) and \(\operatorname{tr}W=1\), \(\lambda_{\max}(G_{r,1})\ge\Phi\). The Hessian of \(\Phi\) is diagonal with entries \(2(ur+v\sqrt r)>0\) and \(2(1-u+v\sqrt r)>0\). Its two first derivatives vanish at \((x_0,y_0)\): they are
\[
 ur(2x_0-1)+2v\sqrt r\,x_0=0,\quad
 (1-u)(2y_0-1)+2v\sqrt r\,(y_0-1)=0,
\]
precisely because \(v/u=L\) and \(v/(1-u)=U\). Consequently \(\Phi\) has a unique global minimum at \((x_0,y_0)\) throughout the ordered triangle; its value there is \(r(a^2+1/12)\), since \(G_{r,1}(x_0,y_0)\) is scalar. The spectral bound is sharp there and is strict at any other point in the ordered triangle. Reflection gives exactly the two asserted designs (which represent the same unordered pair when \(r=1\)).

**4. Saturation and its equality cases.** The largest eigenvalue of any positive semidefinite Gram matrix is at least its upper-left diagonal, whence
\[
 C_{\alpha,\beta}(x,y)^2\ge\alpha K(x,x)\ge\alpha/12.
\]
Equality forces \(x=1/2\). For the largest eigenvalue to equal that diagonal exactly, the off-diagonal must vanish, so \(K(1/2,y)=0\), giving only \(y=1/2\pm b_0\). At either such point, the lighter diagonal equals \(\beta(b_0^2+1/12)=\beta(5-2\sqrt3)/12\), which is at most \(\alpha/12\) exactly when \(r\ge r_*\). This proves attainability, the sharp transition, and every equality configuration. For \(r<r_*\), the strict convex certificate from step 3 excludes all other configurations.

For every fixed minimizing design, all functions maximizing its trace norm lie in the top eigenspace of its evaluation Gram operator, pulled back to \(H\): below and at the transition both weighted kernel representers span norming directions; above the transition only the heavier midpoint kernel does.

## Verification

The standalone standard-library script `check.py` reconstructs \(K\), the exact two-phase design rule, the scalar-Gram and semidefinite certificate identities, and random comparisons against 150,000 alternative pairs, with explicit finite tolerance. Execute `python3 check.py` in the extracted package. The analytical positivity and strict-convexity arguments above certify all real positions and every weight ratio; finite tests are not an exhaustive proof.

## Relationship to prior work

Wang–Zhang (2012) study placement for finite-sample **reconstruction error** in general reproducing-kernel Hilbert spaces and supply a general sampling framework. Their reconstruction objective is not the worst-case joint evaluation norm optimized here; no implication transfers their subspace error criterion to this minimax trace value. Privat–Trélat–Zuazua (2014) optimize positive-measure observation domains in parabolic equations, averaged over random initial data, rather than two point evaluations in a derivative-energy RKHS. Jorgensen–Tian (2015) examine RKHS kernels and Dirac masses on countably discrete sets rather than this continuous interval trace design. The present classification follows directly from the displayed kernel and strict semidefinite lower certificate. Equivalent formulation to search for includes a two-vector Neumann Green-function tight-frame design, or minimum maximal eigenvalue of two weighted Brownian-motion-centering evaluation functionals.

## Limitations

The result is for precisely two point evaluations of real mean-zero \(H^1(0,1)\) with continuous arclength centering and derivative seminorm. It does not optimize recovery error, high-order Sobolev norms, periodic boundary conditions, more sample sites, or noisy observations. Novelty can never be certified by database absence: an earlier equivalent in RKHS frame-design or optimal experimental design literature remains possible. This is a mathematically explicit proof with self-review, not an independent mathematical audit.

## References

- R. Wang and H. Zhang, *Optimal Sampling Points in Reproducing Kernel Hilbert Spaces* (first public 2012-07-25), https://arxiv.org/abs/1207.5871, Sections 1–4 and Appendix.
- Y. Privat, E. Trélat and E. Zuazua, *Optimal shape and location of sensors for parabolic equations with random initial data* (first public 2014-03-25), https://arxiv.org/abs/1403.6445, Sections 1–3 and observability comparisons.
- P. Jorgensen and F. Tian, *Discrete reproducing kernel Hilbert spaces: Sampling and distribution of Dirac-masses* (first public 2015-01-10), https://arxiv.org/abs/1501.02310, Introduction and discrete sampling framework.
