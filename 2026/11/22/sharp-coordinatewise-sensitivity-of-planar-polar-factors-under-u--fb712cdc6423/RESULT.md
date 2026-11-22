# Sharp coordinatewise sensitivity of planar polar factors under uniform accretivity

## Finding
Let \(\mu>0\). On the domain of real \(2\times2\) matrices with symmetric part at least \(\mu I\), the proper orthogonal polar factor \(Q(A)=A(A^{\mathsf T}A)^{-1/2}\) has sharp two-input Lipschitz coefficient in the maximum absolute-entry norm:
\[
\boxed{\sup_{A\ne B\in\mathcal D_\mu}\frac{\|Q(A)-Q(B)\|_{\max}}{\|A-B\|_{\max}}
=\frac{C_*}{\mu},\qquad C_*=\sqrt{\frac{71+17\sqrt{17}}{108}}=1.142985028074638\ldots.}
\]
The sharp infinitesimal geometry has skew-to-trace ratio \(t_*=(\sqrt{17}-3)/4\), uniquely maximizing the normalized derivative. Hence entrywise polar-rotation extraction can amplify unit entrywise input error by more than \(1/\mu\), even for matrices with a uniformly positive symmetric part.

## Assumptions and scope
For \(\mu>0\) write
\[\mathcal D_\mu=\{A\in\mathbb R^{2\times2}:\tfrac12(A+A^{\mathsf T})\succeq\mu I\},\qquad \|A\|_{\max}=\max_{1\le i,j\le2}|A_{ij}|.\]
The positive semidefinite order is the Euclidean operator order on real symmetric matrices. Every matrix in \(\mathcal D_\mu\) is invertible and orientation preserving: writing \(A=S+kJ\) with symmetric \(S\succeq\mu I\), one has \(\det A=\det S+k^2>0\). Thus \(Q(A)\) is the unique special-orthogonal polar factor, and the domain is convex. This is a global *two-input* statement with no upper bound on the entries or singular values.

## Proof
**1. Planar polar formula.** Write \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), \(u=a+d\), and \(v=c-b\). Since \(u\ge2\mu>0\) and \(\det A>0\), its proper polar factor is
\[
Q(A)=\frac1{\sqrt{u^2+v^2}}\begin{pmatrix}u&-v\\v&u\end{pmatrix}.
\]
Indeed, among planar rotations, the Frobenius inner product with \(A\) is \(u\cos\theta+v\sin\theta\); its unique maximizing angle gives the stated rotation. The positive determinant excludes the reflection branch.

**2. Exact derivative norm.** For any perturbation \(H\), set \(\dot u=H_{11}+H_{22}\) and \(\dot v=H_{21}-H_{12}\). If \(\|H\|_{\max}\le1\), then \(|\dot u|\le2\) and \(|\dot v|\le2\); conversely all four sign-extremes of these two independent variables are realized by matrices of maximum-entry norm one. With \(r=\sqrt{u^2+v^2}\), differentiation of the preceding formula gives
\[
\dot{\cos\theta}=\frac{v^2\dot u-uv\dot v}{r^3},\qquad
\dot{\sin\theta}=\frac{-uv\dot u+u^2\dot v}{r^3}.
\]
Consequently the exact induced entrywise derivative norm is
\[
\|DQ(A)\|_{\max\to\max}=
\frac{2(u+|v|)\max\{u,|v|\}}{(u^2+v^2)^{3/2}}.
\]
Put \(t=|v|/u\ge0\). Using \(u\ge2\mu\) yields
\[
\|DQ(A)\|_{\max\to\max}\le\frac1\mu f(t),\qquad
f(t)=\frac{(1+t)\max\{1,t\}}{(1+t^2)^{3/2}}.
\]

**3. Exact scalar optimization.** On \(0\le t\le1\), the sign of \(f'(t)\) is the sign of \(1-3t-2t^2\), which changes from positive to negative at the unique root
\[t_*=(\sqrt{17}-3)/4\in(0,1).\]
On \(t\ge1\), the sign is the sign of \(-(t-1)(t^2+3t+1)\), hence \(f\) is nonincreasing there. Since \(f(t_*)>f(0)=1\), the unique global maximizer is \(t_*\). Direct substitution of \(2t_*^2+3t_*-1=0\) gives
\[f(t_*)^2=\frac{71+17\sqrt{17}}{108}.\]
This proves the pointwise upper bound \(\|DQ(A)\|_{\max\to\max}\le C_*/\mu\).

**4. Globalization and sharpness.** For any \(A,B\in\mathcal D_\mu\), convexity keeps the entire connecting segment inside the domain. Integrating \(DQ\) along that segment proves
\[\|Q(B)-Q(A)\|_{\max}\le\frac{C_*}{\mu}\|B-A\|_{\max}.\]
For the reverse inequality set
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
A_*=\mu(I+t_*J),\qquad
H=\begin{pmatrix}1&1\\-1&1\end{pmatrix}=I-J.
\]
Both \(A_*\) and \(A_*+hH\) lie in \(\mathcal D_\mu\) for every \(h>0\), because the symmetric parts equal \(\mu I\) and \((\mu+h)I\). Also \(\|H\|_{\max}=1\), \(\dot u=2\), and \(\dot v=-2\). The sine entry of \(DQ(A_*)[H]\) has absolute value \(C_*/\mu\) by Step 2. Hence
\[
\lim_{h\downarrow0}\frac{\|Q(A_*+hH)-Q(A_*)\|_{\max}}{h}=\frac{C_*}{\mu},
\]
showing the global coefficient is sharp. This is a derivative-limit extremizer, not a claim of a distinct finite pair attaining the constant.

## Verification
The accompanying standalone `check_polar.py` requires only Python's standard library. Running `python3 check_polar.py` reproduces 115,037 supplementary assertions: the exact critical polynomial identity and closed-form coefficient, 15,005 scalar-grid upper checks, 100,000 randomly sampled two-input matrix inequalities across five margins, and 30 positive-direction sharpness and scaling checks. The analytic four-step argument above, not those finite checks, proves the universal inequality. All defining domain and boundary hypotheses are used explicitly.

## Relationship to prior work
Mbekhta (first online 2020-11-25) studies representations and approximations of Hilbert-space polar factors, but does not state a sharp two-input maximum-entry modulus for uniformly accretive real matrices. Duong–Philipp (2016), Liu–Luo–Xu (2018), and Chen–Sun (1989) obtain polar-factor perturbation bounds in the operator, unitarily invariant, or Frobenius norms under different assumptions. Kenney–Laub (1991) studies operator-norm condition estimation. None of the material inspected establishes the present entrywise optimum, its algebraic constant, or its unique skew-to-trace geometry. Related sharp planar semidefinite *projection* estimates concern a different nonlinear map. The novelty comparison is a documented literature comparison, not a proof of historical uniqueness.

## Limitations
The sharp formula is restricted to real \(2\times2\) matrices, the maximum absolute-entry norm, and a strictly positive symmetric-part lower bound. It is not claimed for higher dimensions, other matrix norms, merely invertible matrices, or the full rank-deficient polar factor. The sharp value is approached infinitesimally. Earlier equivalent formulae possibly embedded in specialized matrix-conditioning literature remain a priority risk. No independent mathematical audit has been performed.

## References
1. M. Mbekhta, *Representation and approximation of the polar factor of an operator on a Hilbert space*, Discrete Contin. Dyn. Syst. Ser. S, early access 2020-11-25, doi:10.3934/dcdss.2020463, https://www.aimsciences.org/article/doi/10.3934/dcdss.2020463.
2. R. Duong and F. Philipp, *The effect of perturbations of linear operators on their polar decomposition*, arXiv:1602.05304, first posted 2016-02-17, https://arxiv.org/abs/1602.05304.
3. N. Liu, W. Luo and Q. Xu, *New multiplicative perturbation bounds for the generalized polar decomposition*, arXiv:1807.03298, first posted 2018-07-09, https://arxiv.org/abs/1807.03298.
4. C. Kenney and A. J. Laub, *Polar decomposition and matrix sign function condition estimates*, SIAM J. Sci. Stat. Comput. 12 (1991), doi:10.1137/0912027.
5. Y. Chen and J.-G. Sun, *Perturbation bounds for the polar factors*, J. Comput. Math. 7 (1989), 397–401, https://www.global-sci.com/JCM/article/view/10967.
