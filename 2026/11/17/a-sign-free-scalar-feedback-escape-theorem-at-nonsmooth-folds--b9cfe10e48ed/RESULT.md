# A sign-free scalar-feedback escape theorem at nonsmooth folds

## Finding
For the continuous two-zone planar map
\[
F_\mu(x,y)=
\begin{cases}
((1+\delta_L-\alpha)x+y+\mu,\,-\delta_Lx-g(y)),&x\le0,\\
((1+\delta_R+\alpha)x+y+\mu,\,-\delta_Rx-g(y)),&x\ge0,
\end{cases}
\]
assume \(\alpha>0\), \(\delta_L,\delta_R\in\mathbb R\), and \(g:\mathbb R\to\mathbb R\) is continuous with \(g(y)=o(|y|)\) at zero. There is a radius \(\eta>0\) depending on \(\alpha,\delta_L,\delta_R,g\), but **not** on \(\mu\), such that for all \(\mu>0\) and every \((x_0,y_0)\in B_\eta\), the first step \(\tau\) at which the orbit leaves \(B_\eta\) satisfies
\[
\tau\le\left\lfloor\frac{5\eta}{\mu}\right\rfloor+1.
\]
Consequently no nonempty forward-invariant set lies in this ball. This conclusion holds for arbitrary signs and sizes of the two branch determinants and for scalar feedback that may change sign or need not be differentiable.

## Assumptions and scope
The switching convention at \(x=0\) is immaterial because the branches agree there. The Euclidean closed ball is \(B_\eta=\{(x,y):x^2+y^2\le\eta^2\}\). The feedback assumption means \(\lim_{y\to0}|g(y)|/|y|=0\); hence \(g(0)=0\). No assumption about the behavior of \(g\) away from zero is needed to establish first departure; continuity on \(\mathbb R\) ensures the iterates are defined. The result asserts **local exit**, not global divergence after exit, a global absence of invariant sets, or a solution of the general higher-order-perturbation conjecture.

## Proof
Set \(D=\max\{|\delta_L|,|\delta_R|\}\) and
\[
\varepsilon=\min\left\{\frac18,\frac{\alpha}{8(1+D)}\right\}>0.
\]
By the smallness assumption there is \(r>0\) such that \(|g(s)|\le\varepsilon |s|\) for every \(|s|\le r\). Fix
\[
\eta=\min\left\{1,\frac{r}{2(1+D)}\right\}>0.
\]
For \((x,y)\in B_\eta\), write \(F_\mu(x,y)=(x',y')\), and let \(\delta=\delta_L\) or \(\delta_R\) according to the branch. Then \(y'=-\delta x-g(y)\), so
\[
|y'|\le D|x|+|g(y)|\le(D+\varepsilon)\eta\le r.
\]
In particular \(|g(y')|\le\varepsilon|y'|\le\varepsilon(D|x|+|g(y)|)\).

Define the continuous (not necessarily differentiable) function
\[
\Phi(x,y)=x+y-g(y)-|g(y)|.
\]
Both branches satisfy the exact identity \(x'+y'-(x+y)=\mu+\alpha|x|-g(y)\). Hence
\[
\begin{aligned}
\Phi(x',y')-\Phi(x,y)
&=\mu+\alpha|x|+|g(y)|-g(y')-|g(y')|\\
&\ge\mu+(\alpha-2\varepsilon D)|x|+(1-2\varepsilon)|g(y)|\\
&\ge\mu+\frac{3\alpha}{4}|x|+\frac34|g(y)|\ge\mu.
\end{aligned}
\]
Here \(2\varepsilon D\le\alpha/4\) and \(2\varepsilon\le1/4\). Meanwhile, for every \((x,y)\in B_\eta\),
\[
|\Phi(x,y)|\le|x|+|y|+2|g(y)|\le(2+2\varepsilon)\eta\le\frac94\eta.
\]
Thus the range of \(\Phi\) within \(B_\eta\) has diameter at most \(9\eta/2<5\eta\). If the first \(n\) iterates remain in the ball, monotonicity forces \(n\mu\le5\eta\). At \(n=\lfloor5\eta/\mu\rfloor+1\) this is impossible. Therefore exit occurs no later than that step. A nonempty forward-invariant subset of the ball would yield a never-exiting orbit, also impossible. \(\square\)

For the linear truncation \(g=0\), the two virtual fixed points of the branch extensions have first coordinates \(\mu/\alpha\) (left branch) and \(-\mu/\alpha\) (right branch), irrespective of \(\delta_L\) and \(\delta_R\). Moreover \(\det(I-A_L)=\alpha\) and \(\det(I-A_R)=-\alpha\), so this is precisely the nonsmooth-fold configuration of the motivating work.

## Verification
The proof is an all-parameter analytic inequality. The auxiliary standalone `CHECKER.py` uses exact rational arithmetic to independently test the one-step identity, the stated Lyapunov bound and the first-exit inequality for several distinct signs of branch determinants and for signed polynomial feedback examples. Running `python CHECKER.py` prints a success token. Finite tests illustrate but do not replace the quantified proof.

## Relationship to prior work
Simpson's *Nonsmooth folds are tipping points* (first public 2024-06-07), Section 3, proves escape for the piecewise-affine truncation without general feedback. Section 4 poses the higher-order local-escape conjecture. Appendix A, Proposition 6, verifies it for \(g(y)=y^2\) only with \(\delta_L>0\) and \(\delta_R<0\), using a quadratic Lyapunov function. The present theorem establishes an entire sublinear scalar-feedback class with **no determinant-sign restrictions**, and supplies a new absolute-value Lyapunov gauge. The older result cannot imply the newly permitted parameter signs or nonlinear feedback; the general conjecture, on the other hand, would imply this theorem if established, and is not claimed here. Simpson and Glendinning (arXiv:2111.12222, Section 3) instead prove persistence of *existing chaotic attractors* under nondegenerate perturbations in a different regime; their conclusion does not give extinction of all invariant sets in the present virtual-fixed-point regime.

## Limitations
The perturbation must enter through the single scalar feedback \(-g(y)\) in the second coordinate. General higher-order terms in both coordinates, or feedback with a nonzero linear part at the origin, are not addressed. The ball may be very small and depends on the feedback modulus; the explicit bound is an upper bound, not an optimal first-exit asymptotic. No independent external mathematical audit or general literature-priority certification has been performed.

## References
1. D. J. W. Simpson, *Nonsmooth folds are tipping points*, arXiv:2406.04587 (first public 2024-06-07), Sections 3–4 and Appendix A; later published in *Chaos* 35 (2025), 023125. https://arxiv.org/abs/2406.04587
2. D. J. W. Simpson and P. A. Glendinning, *Inclusion of higher-order terms in the border-collision normal form: persistence of chaos and applications to power converters*, arXiv:2111.12222 (2021), Sections 2–3. https://arxiv.org/abs/2111.12222
