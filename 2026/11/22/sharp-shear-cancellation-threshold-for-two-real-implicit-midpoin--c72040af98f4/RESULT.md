# Sharp shear-cancellation threshold for two real implicit-midpoint steps

## Finding
Let \(a>0\), \(s\geq0\), \(H>4/a\), and consider the stable but generally nonnormal Jordan generator
\[
 A=\begin{pmatrix}-a&s\\0&-a\end{pmatrix}.
\]
For two real, strictly positive implicit-midpoint (trapezoidal/Cayley) steps \(h_1,h_2\) with \(h_1+h_2=H\), minimize the induced Euclidean operator norm of their product over all such allocations. The following are equivalent:

1. The ratio \(s/a\) is at least \(2\).
2. The unique minimizing **unordered** pair is
\[
 \{h_1,h_2\}=\left\{\frac{H-\sqrt{H^2-16/a^2}}2,\frac{H+\sqrt{H^2-16/a^2}}2\right\}.
\]
3. The unique minimizing unordered pair has \(h_1h_2=4/a^2\), making its two-step amplification an exact scalar matrix.

In this case the exact minimum norm is
\[
 \boxed{\frac{aH-4}{aH+4}},\qquad
 C(h_2)C(h_1)=-\frac{aH-4}{aH+4}I_2,
 \quad C(h)=(I-hA/2)^{-1}(I+hA/2).
\]
For every \(0\leq s/a<2\), the shear-canceling pair is strictly suboptimal: a nearby pair of unequal positive steps achieves a smaller operator norm. At the excluded boundary \(H=4/a\), the equal steps \(h_1=h_2=2/a\) yield the zero matrix for **all** \(s\geq0\); the strict-horizon assumption is essential to the equivalence.

## Assumptions and scope
The ODE is autonomous and real, with the displayed fixed coordinate basis and its standard Euclidean norm. The two steps are classical implicit-midpoint endpoint maps, not a variable-coefficient multistep discretization. Both step lengths are allowed to vary but are strictly positive and must sum to the fixed physical duration \(H\). The objective is worst-initial-direction *terminal numerical damping*, not accuracy against \(e^{AH}\), per-solve cost, or intermediate-stage growth. Since the two endpoint maps are rational functions of one matrix they commute, so allocations are unordered.

The shear threshold has an independent geometric interpretation: the symmetric part \((A+A^{\mathsf T})/2\) is negative semidefinite exactly when \(s\leq2a\). Thus the regime \(s>2a\), where the exact flow can initially exhibit Euclidean transient amplification, is precisely the regime where cancellation is strictly optimal (with equality at the dissipativity boundary).

## Proof
Write \(x=aH/2>2\), \(\beta=s/a\), and \(y=a^2h_1h_2/4\). Feasible allocations correspond bijectively, up to permutation, to \(0<y\leq x^2/4\); the shear-canceling point \(y=1\) is feasible and has two strictly positive preimages.

With \(N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), direct rational multiplication using \(N^2=0\) gives
\[
 C(h_2)C(h_1)=dI_2+vN,\qquad
 d=\frac{1-x+y}{1+x+y},\qquad
 v=\frac{2\beta x(1-y)}{(1+x+y)^2}.
\]
For real \(d,v\), its induced norm is exactly
\[
 \|dI_2+vN\|_2=\frac{\sqrt{4d^2+v^2}+|v|}{2}.
\]
Set \(q=(x-2)/(x+2)>0\). At \(y=1\), \(d=-q\), \(v=0\), so the candidate norm is \(q\). For \(0<y<1\), one has \(d<-q\), proving a strictly larger norm. For \(1<y\leq x^2/4\), monotonicity of \(d\) and \(x^2/4<(x^2-2)/2\) show \(-q<d<q\). At such a point, elementary squaring of the exact norm formula yields
\[
 \|dI_2+vN\|_2\geq q
 \quad\Longleftrightarrow\quad
 |v|\geq\frac{q^2-d^2}{q}.
\]
The exact algebraic identity
\[
 q^2-d^2=\frac{4x(y-1)(x^2-2y-2)}{(x+2)^2(1+x+y)^2}
\]
turns the latter inequality into
\[
 \beta\geq B_x(y):=\frac{2(x^2-2y-2)}{x^2-4}.
\]
On the relevant interval, \(B_x(1)=2\), \(B_x'(y)=-4/(x^2-4)<0\), and \(B_x(y)>0\). Hence if \(\beta\geq2\), every \(y>1\) produces a *strictly* larger norm than \(q\). This proves global optimality and uniqueness of \(y=1\) for \(\beta\geq2\).

Conversely, for \(0\leq\beta<2\), continuity and \(B_x(1)=2\) give a feasible \(y>1\), arbitrarily close to \(1\), satisfying \(\beta<B_x(y)\). The norm inequality is then reversed strictly; the shear-canceling candidate is not a minimizer. Finally, solving \(h_1+h_2=H\) and \(h_1h_2=4/a^2\) gives the stated pair, and substitution gives the stated scalar product. These arguments cover the entire continuous allocation interval, not a finite sampled grid.

## Verification
The standalone Python 3 standard-library script `verify.py` checks the rational factor identity with exact fractions for 606 feasible grid points, the threshold necessity with 20 additional exact-rational cases, and 5,000 randomized samples against the analytic global bound. It also assembles both Cayley factors independently for \(a=1\), \(s=3\), \(H=6\) and checks the numerical example. Its expected output begins `CHECKS_OK 5626`.

In that example the unique pair is \(3\pm\sqrt5\), the optimal product is \(-I_2/5\), and the norm is \(0.2\). Two equal steps have norm approximately \(0.5787645095\); one full step and a zero step have norm approximately \(1.3150996612\) (the latter is a *comparison*, not an admissible strictly-positive allocation).

## Relationship to prior work
Reuter (first posted 2019) analyzes transient growth caused by nonnormal invariant and Jordan subspaces of exact matrix exponentials and matrix powers, not a fixed-duration minimax allocation of two Cayley endpoint maps. George, Jung and Mangan (2021) study complex time-step compositions, including the midpoint method and order conditions; their two-step complex conjugate construction optimizes consistency order rather than the real-positive substep spectral-norm problem here. Liao, Tang and Zhou (2020) develop variable-step Crank–Nicolson-type energy stability for time-fractional Allen–Cahn equations, not an optimal Jordan-shear allocation. Known normal-oscillator two-Cayley optimization and Jordan-shear two-backward-Euler optimization have different map families/parameter geometries and do not imply this equality-iff-shear-threshold claim. The proof here exploits the exact feasible Cayley rational curve and the nonnormal operator norm, not just eigenvalues.

## Limitations
This is a two-dimensional, repeated-eigenvalue Jordan model with exactly two real positive steps and a sufficiently long horizon. It does not assert an optimizer for \(s<2a\), for higher Jordan blocks, or for unequal damping eigenvalues. Optimization of terminal norm can seriously differ from accurate physical-time integration, and a step longer than \(2/a\) reverses the scalar Cayley sign. Source comparisons are limited to the explicitly inspected works and indexed findings; broader classical equivalence and historical priority remain open to independent review. No independent mathematical audit was performed.

## References
- M. G. Reuter, *Associating the Invariant Subspaces of a Non-Normal Matrix with Transient Effects in its Matrix Exponential or Matrix Powers*, arXiv:1909.05931, version 1 posted 2019-09-12; https://arxiv.org/html/1909.05931v2.
- J. D. George, S. Y. Jung, N. M. Mangan, *Walking into the Complex Plane to “Order” Better Time Integrators*, arXiv:2110.04402, version 1 posted 2021-10-08; https://arxiv.org/abs/2110.04402, section 8.
- H.-L. Liao, T. Tang, T. Zhou, *An Energy Stable and Maximum Bound Preserving Scheme with Variable Time Steps for Time Fractional Allen–Cahn Equation*, arXiv:2012.10740, version 1 posted 2020-12-19; https://arxiv.org/abs/2012.10740.
