# Sharp finite-length bounded-variation stability of Aitken \(\Delta^2\) extrapolation on geometric-ratio cones

## Finding
Fix an integer \(n\ge 3\) and a contraction bound \(0<q<1\). Define the open, translation-invariant cone
\[
\mathcal C_{n,q}=\{x\in\mathbb R^n:\ u_j=x_{j+1}-x_j>0\ (0\le j<n-1),\quad 0<u_{j+1}<q u_j\ (0\le j<n-2)\}.
\]
For \(x\in\mathcal C_{n,q}\), apply the classical Aitken transform to every consecutive triple:
\[
(\mathcal A x)_j=x_j-\frac{(x_{j+1}-x_j)^2}{x_{j+2}-2x_{j+1}+x_j}
=x_j+\frac{u_j^2}{u_j-u_{j+1}},\quad 0\le j<n-2.
\]
For a real finite sequence \(z\), let \(V(z)=\sum_{j=0}^{\operatorname{len}(z)-2}|z_{j+1}-z_j|\) (and \(V(z)=0\) for singleton sequences). The sharp two-input seminorm Lipschitz constant is
\[
K_n(q)=\sup_{x,y\in\mathcal C_{n,q},\,V(x-y)>0}\frac{V(\mathcal A x-\mathcal A y)}{V(x-y)}
=\begin{cases}
0,&n=3,\\
\dfrac{\max\{1,2q\}}{(1-q)^2},&n=4,\\
\dfrac{1+2q}{(1-q)^2},&n=5,\\
\left(\dfrac{1+q}{1-q}\right)^2,&n\ge6.
\end{cases}
\]
These are exact supremum values for all real inputs satisfying the stated cone inequalities, not just linearized estimates. In particular the four-input constant changes its maximizing step position at \(q=1/2\), and at six inputs the fully developed amplification law stabilizes in sequence length. For each fixed \(n\ge4\), the constant diverges quadratically as \(q\uparrow1\), despite Aitken's exact elimination of geometric errors. The singleton-output case \(n=3\) has zero variation for every \(q\).

## Assumptions and scope
The domain is the *strict* cone of increasing finite real sequences whose positive forward increments decrease by a factor strictly below \(q\) at each step. The upper bound also holds if the ratio inequalities \(u_{j+1}<q u_j\) are replaced with \(u_{j+1}\le q u_j\), while keeping all increments positive. All statements use the unweighted adjacent Jordan variation of discrete input and output sequences. Translation of the inputs does not change either variation seminorm. No claim is made about arbitrary sequences, alternating-sign increments, rounding errors, or stochastic perturbations crossing the cone boundary.

## Proof
**1. Differential of one extrapolated value.** Write \(t_j=u_{j+1}/u_j\in(0,q)\). Direct differentiation of the Aitken quotient, in coordinates \((x_j,x_{j+1},x_{j+2})\), gives the row
\[
D(\mathcal A x)_j
=\frac{1}{(1-t_j)^2}\big(t_j^2,-2t_j,1\big).
\]
The row sum is one. Put
\[
U(t)=\frac{1}{(1-t)^2},\qquad H(t)=\frac{1-2t}{(1-t)^2}=U(t)-\frac{2t}{(1-t)^2}.
\]
On \((0,1)\), \(U\) is increasing, \(H\) is decreasing, and \(U(t)\ge1\ge H(t)\). These identities remain valid when \(H(t)\) is negative.

**2. Step reduction.** For a perturbation \(h\in\mathbb R^n\), let \(s^{(k)}_i=\mathbf1_{\{i\ge k\}}\) for \(1\le k<n\). The identity
\[
h=h_0\mathbf1+\sum_{k=1}^{n-1}(h_k-h_{k-1})s^{(k)}
\]
combined with translation covariance of the derivative and the triangle inequality yields
\[
V(D\mathcal A_x h)\le V(h)\max_{1\le k<n}V(D\mathcal A_x s^{(k)}).
\]
For a fixed \(k\), the derivative image of \(s^{(k)}\) has the following consecutive entries, omitting those outside the output index range \(0,\ldots,n-3\): zero before index \(k-2\), then \(U(t_{k-2})\) at index \(k-2\), then \(H(t_{k-1})\) at index \(k-1\), and finally one from index \(k\) onward. Thus only at most three nonconstant adjacent transitions matter. In the inequalities below write \(U=U(q)\), \(H=H(q)\); the inequalities \(U(t)\le U\) and \(H(t)\ge H\) hold for all permitted ratios.

**3. Exhaustive symbolic boundary cases.** For \(n=3\) the output has one coordinate, so its variation is zero. For \(n=4\), the step positions \(k=1,2,3\) have variation bounded respectively by \(1-H\), \(U-H\), \(U\). Because
\[
1-H=\frac{q^2}{(1-q)^2},\quad U-H=\frac{2q}{(1-q)^2},\quad U=\frac1{(1-q)^2},
\]
the largest is \(\max\{1,2q\}/(1-q)^2\).

For \(n=5\), the four step positions have variation bounded respectively by
\[
1-H,\quad U+1-2H,\quad 2U-H,\quad U.
\]
The largest is \(2U-H=(1+2q)/(1-q)^2\). Indeed \(2U-H\ge U\), \(2U-H\ge 1-H\), and
\[
(2U-H)-(U+1-2H)=U+H-1=\frac{1+q}{1-q}>0.
\]
For every \(n\ge6\), all step images are truncated pieces of the same four-level pattern \(0,U(t),H(t),1\), with possible repeated constant entries. Their variation is at most
\[
U+(U-H)+(1-H)=2U+1-2H=\frac{(1+q)^2}{(1-q)^2}.
\]
These are uniform derivative bounds.

**4. From the derivative to two finite inputs.** The cone is convex: each defining constraint is a strict linear inequality in the input coordinates. The Aitken map is smooth on this cone since \(u_j-u_{j+1}>(1-q)u_j>0\). Consequently, for any \(x,y\) in it,
\[
\mathcal Ax-\mathcal Ay=\int_0^1D\mathcal A_{y+s(x-y)}(x-y)\,ds.
\]
Variation is a seminorm, so the derivative estimates above, followed by the triangle inequality for the integral, yield \(V(\mathcal A x-\mathcal A y)\le K_n(q)V(x-y)\). Continuity gives the asserted weak-ratio-bound extension.

**5. Sharpness by interior geometric inputs.** Fix \(0<t<q\), and choose the finite geometric-increment input \(x_0=0\), \(x_i=\sum_{r=0}^{i-1}t^r\) for \(1\le i<n\). All derivative rows use the same ratio \(t\). For \(n=4\), take the direction \(s^{(3)}\) when \(q\le1/2\), or \(s^{(2)}\) when \(q\ge1/2\). For \(n=5\) and \(n\ge6\), take \(s^{(3)}\). The step calculations give, respectively, the lower values \(U(t)\), \(U(t)-H(t)\), \(2U(t)-H(t)\), and \(2U(t)+1-2H(t)\) (according to the indicated cases). For every sufficiently small positive \(\varepsilon\), the perturbed input \(x+\varepsilon s^{(k)}\) remains inside the strict cone. Letting \(\varepsilon\downarrow0\) gives the directional derivative ratio; then letting \(t\uparrow q\) gives exactly the claimed upper constants. These limits prove sharpness without claiming that the supremum is attained by a fixed positive-size perturbation.

## Verification
The accompanying standalone `verify_aitken.py` uses exact rational arithmetic, checking 624 homogeneous-ratio step identities, 27,000 heterogeneous-ratio derivative step inequalities, 2,700 admissible two-input inequalities, and 24 near-sharp finite perturbations. All its checks passed. The symbolic proof above, not finite sampling, establishes the assertions for every \(n\ge3\), every real \(0<q<1\), and every pair of admissible signals.

To reproduce, run `python verify_aitken.py` with a standard Python installation (no third-party packages). The checker intentionally includes the \(n=4\) phase transition and both positive and negative middle derivative weights.

## Relationship to prior work
Aitken's classical \(\Delta^2\) process eliminates a geometric error mode. Brezinski and Redivo Zaglia (2007) study its kernel, equivalent formulas, numerical cancellation, and broader acceleration transforms. Tiruneh's 2013 preprint uses geometric difference ratios and higher-order extrapolation in iterative linear equations. Pomeranz (2017) studies convergence acceleration with different sign patterns. These are relevant but address approximation to a limit, numerical cancellation, or convergence rates rather than the sharp *two-input adjacent-variation* modulus on a uniformly contracting increment cone.

An independent published investigation of Aitken's noisy scalar extrapolation concerns stochastic tail and moment transitions; those statements do not imply the deterministic finite-input constants here. Brezinski (1989), *Contraction properties of sequence transformations*, is a particularly relevant earlier title, but no accessible complete text could be obtained for an exact implication comparison. The present norm is a sensitivity result for an entire sliding transformed sequence, not a floating-point error bound or a claim of faster convergence. Equivalent results outside the inspected literature, including this unresolved 1989 source, cannot be ruled out without additional bibliographic review.

## Limitations
The domain excludes vanishing, negative, or sign-alternating increments, and assumes a common strict ratio cap \(q<1\) for every triple. The seminorm is unweighted adjacent total variation and ignores overall additive translation. Sharpness is established as a supremum through arbitrarily close finite pairs, not as finite-pair attainment. The bounds do not quantify absolute bias or convergence acceleration toward an unknown limit, and do not cover higher-order, vector, or iterated Aitken transforms. The bibliography review is not an independent priority certification.

## References
- C. Brezinski and M. Redivo Zaglia, *Generalizations of Aitken's process for accelerating the convergence of sequences*, Computational & Applied Mathematics 26 (2007), 171–189. https://doi.org/10.1590/S0101-82052007000200001
- A. T. Tiruneh, *Higher Order Aitken Extrapolation with Application to Converging and Diverging Gauss-Seidel Iterations*, arXiv:1310.4288, first posted 2013-10-16. https://arxiv.org/abs/1310.4288
- S. B. Pomeranz, *Aitken's \(\Delta^2\) method extended*, Cogent Mathematics 4 (2017), article 1308622. https://doi.org/10.1080/23311835.2017.1308622
- C. Brezinski, *Contraction properties of sequence transformations*, Numerische Mathematik 54 (1989), 565–574. https://doi.org/10.1007/BF01396362 (full text not accessed)
