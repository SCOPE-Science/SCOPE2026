# Exact signed square-root and logarithmic relaxation at the degenerate Chialvo fixed point

## Finding

Consider the reduced Chialvo iteration \(x_{n+1}=f(x_n)\) for \(x_0\ge0\), where
\[
f(x)=x^2e^{r_*-x}+k_*,\qquad c=2-\sqrt2,\quad k_*=3-2\sqrt2,\quad r_*=c-\log[c(2-c)].
\]
Every orbit converges to the unique equilibrium \(c\). Let \(\mathcal E=\bigcup_{j\ge0}f^{-j}(\{c\})\), the at most countable set of initial conditions that hit the equilibrium in finite time. For \(x_0\in[0,\infty)\setminus\mathcal E\), there is an eventual side \(s\in\{-1,+1\}\), constant for all sufficiently large \(n\), and a finite constant \(C(x_0)\) such that
\[
\boxed{\frac1{(x_n-c)^2}=A n+sD\sqrt n+H\log n+C(x_0)+o(1)},\qquad n\longrightarrow\infty,
\]
with explicit, orbit-independent coefficients
\[
A=\frac{2+\sqrt2}{3},\qquad
D=-\frac{5+3\sqrt2}{6\sqrt{(2+\sqrt2)/3}},\qquad
H=\frac{59}{160}+\frac{\sqrt2}{5}.
\]
Here \(s=+1\) when the orbit approaches from above, and \(s=-1\) when it approaches from below. In particular, the signed leading relaxation and the first asymmetric correction are
\[
x_n-c=\frac{s}{\sqrt{A n}}-\frac{D}{2A^{3/2}n}+O\!\left(\frac{\log n}{n^{3/2}}\right).
\]
The leading \(n^{-1/2}\) rate reflects a cubic parabolic fixed point. The exact \(\sqrt n\), \(\log n\), and position corrections distinguish the model's original discrete-time relaxation from a leading-order normal form and quantify the approach from both sides. The source identifies the degenerate equilibrium itself; its location is not claimed as new.

## Assumptions and scope

The iteration is deterministic, has exactly the displayed parameters, and begins at any nonnegative real position. Time \(n\) counts original updates, with no rescaling or continuous approximation. The exceptional set \(\mathcal E\) contains the equilibrium and all its finite preimages, and the displayed reciprocal-square formula is explicitly restricted to initial positions outside this set. For initial data in \(\mathcal E\), the orbit instead eventually equals \(c\) exactly. There is no claim about the full two-dimensional Chialvo model, arbitrary forcing or the persistence of this formula under parameter perturbations.

## Proof

**1. Critical fixed point and global convergence.** Differentiation gives
\[
f'(x)=e^{r_*-x}x(2-x),\qquad
f''(x)=e^{r_*-x}(x^2-4x+2).
\]
By construction, \(f(c)=c\), \(f'(c)=1\), and \(f''(c)=0\). For \(0\le x\le2\), the positive derivative \(f'(x)\) attains its unique maximum \(1\) at \(x=c\); this follows from the sign of \(f''\) and the second zero \(2+\sqrt2>2\). For \(x\ge2\), \(-f'(x)\) has its maximum at \(x=2+\sqrt2\), and its value there is
\[
\max_{x\ge2}|f'(x)|=(3+2\sqrt2)e^{-2\sqrt2}<1.
\]
The final inequality follows, for instance, from the positive exponential series: \(e^{2\sqrt2}>1+2\sqrt2+(2\sqrt2)^2/2=5+2\sqrt2>3+2\sqrt2\). Thus \(|f'(x)|\le1\) for every \(x\ge0\), with equality only at \(x=c\). Integrating the derivative strictly over each nondegenerate segment joining \(x\ne c\) to \(c\) yields \(|f(x)-c|<|x-c|\). Since \(f([0,\infty))\subset[k_*, k_*+4e^{r_*-2}]\), each orbit is bounded and its distance to \(c\) strictly decreases until hitting it. Its limiting distance must be zero: otherwise a convergent subsequence in the compact image interval would have a limit \(z\ne c\) with \(|f(z)-c|=|z-c|\), a contradiction. Hence \(x_n\to c\) for every \(x_0\ge0\).

The map increases on \([0,c]\), and \(f([0,c])=[k_*,c]\). Therefore any orbit entering \([0,c)\) stays below \(c\), whereas any orbit staying above \(c\) approaches from above. Unless an exact hit occurs, the eventual sign \(s=\operatorname{sgn}(x_n-c)\) is well defined. For a fixed target, the analytic unimodal map has at most two inverse images on \([0,\infty)\); thus \(\mathcal E\) is countable.

**2. Exact local coefficients.** Put \(u=x-c\). Taylor expansion of the analytic map at the critical fixed point, using \(e^{r_*-c}=1/[c(2-c)]\), gives
\[
f(c+u)-c=u-au^3+bu^4+du^5+O(u^6),
\]
where
\[
a=\frac{2+\sqrt2}{6},\qquad
b=\frac{5+3\sqrt2}{24},\qquad
d=-\frac{3+2\sqrt2}{40}.
\]
The derivatives used here can be calculated exactly from \(\frac{d^j}{dx^j}(x^2e^{-x})=(-1)^je^{-x}[x^2-2jx+j(j-1)]\) for \(j\ge2\). In particular \(f^{(3)}(c)=-6a=-2/c<0\). This sign accounts for attraction on both sides, but the global conclusion above does not rely on a normal-form theorem.

**3. Reciprocal-square increment.** For an orbit outside \(\mathcal E\), put \(u_n=x_n-c\) and \(w_n=u_n^{-2}\). Since eventually \(u_n=s/\sqrt{w_n}\) and \(w_n\to\infty\), the Taylor expansion gives
\[
\begin{aligned}
w_{n+1}-w_n
&=A+sB w_n^{-1/2}+Q w_n^{-1}+O(w_n^{-3/2}),\\
A&=2a,\qquad B=-2b,\qquad Q=3a^2-2d.
\end{aligned}
\]
To see the coefficient \(Q\), write \(u_{n+1}=u_n(1-au_n^2+bu_n^3+du_n^4+O(u_n^5))\), expand the inverse square, and subtract \(w_n\). This is the discrete update, so the term \(3a^2\) cannot be omitted.

**4. Sharp summation.** As the increments tend to \(A>0\), the Stolz–Cesàro theorem gives \(w_n/n\to A\). Therefore \(w_n=An+O(\sqrt n)\) by summing the \(O(n^{-1/2})\) increment error. Substituting back shows
\[
w_n=An+sD\sqrt n+O(\log n),\qquad D=\frac{2B}{\sqrt A}.
\]
Indeed \(\sum_{j=1}^{n}j^{-1/2}=2\sqrt n+O(1)\), and the replacement of \(w_j^{-1/2}\) by \((Aj)^{-1/2}\) has an \(O(j^{-1})\) per-step error. Expand the square root one order further:
\[
\begin{aligned}
w_n^{-1/2}&=(An)^{-1/2}-\frac{sD}{2A^{3/2}n}+O\!\left(\frac{\log n}{n^{3/2}}\right),\\
w_n^{-1}&=(An)^{-1}+O(n^{-3/2}).
\end{aligned}
\]
The increment therefore has the refined form
\[
w_{n+1}-w_n
=A+\frac{sB}{\sqrt{An}}
+\frac1n\left(\frac QA-\frac{BD}{2A^{3/2}}\right)
+O\!\left(\frac{\log n}{n^{3/2}}\right).
\]
Now \(\sqrt{n+1}-\sqrt n=1/(2\sqrt n)+O(n^{-3/2})\) and \(\log(n+1)-\log n=1/n+O(n^{-2})\). Because \(D=2B/\sqrt A\), the expression in parentheses is
\[
H=\frac QA-\frac{B^2}{A^2}
=\frac{59}{160}+\frac{\sqrt2}{5}.
\]
Consequently \(w_n-An-sD\sqrt n-H\log n\) has increments bounded by a summable sequence \(O((\log n)n^{-3/2})\). It converges to a finite constant \(C(x_0)\). This proves the complete three-term expansion, including the existence of its orbit-dependent limit and the \(o(1)\) remainder. Expanding the reciprocal square root yields the signed-coordinate corollary. \(\square\)

## Verification

The included standalone `checker.py` uses SymPy for exact identities defining the equilibrium, the cubic/quartic/quintic Taylor coefficients, and the constants \(A,D,H\). Its high-precision iteration checks two initial conditions \(c\pm1/4\), two large horizons, and an optional fold-opening consistency check; all assertions pass. Run `python checker.py` with SymPy and mpmath available. The numerical convergence of a logarithmic coefficient is necessarily slow, and these finite computations are corroborative, not a proof of the limiting expansion. The analytic increment argument above proves the infinite-time statement.

## Relationship to prior work

Llovera Trujillo, Signerska-Rynkowska and Bartłomiejczyk (2021, arXiv:2111.14499) introduced and rigorously analyzed the same reduced Chialvo map. Their Theorem 2.3 and subsequent discussion *already identify* the degenerate fold endpoint \(k=3-2\sqrt2\), \(c=2-\sqrt2\), and the associated parameter \(r_*=c-\log[c(2-c)]\). The new statement concerns original-step, global-basin, two-sided **quantitative relaxation**, including exact square-root and logarithmic corrections and a convergent remainder. Ordinary cubic-parabolic local theory predicts the leading \(n^{-1/2}\) exponent; neither this exponent by itself nor the existence of a degenerate fixed point is claimed as a new general theorem. The inspected primary text does not state the model-specific three-term law or establish the convergence of the renormalized reciprocal-square residual.

## Limitations

The parameters are fixed exactly at their degenerate values. This is not a persistence, robustness, or nearby-parameter theorem. The constant \(C(x_0)\) exists but does not have a closed form in general; its dependence on the initial point need not be smooth across preimages. Countably many initial points land on the equilibrium in finitely many steps and have no reciprocal-square asymptotic. This self-review is not independent validation. Broader parabolic-iteration theory and earlier literature may contain equivalent general formulas that specialize to the present exact coefficients; published-priority independence is not certified.

## References

1. F. Llovera Trujillo, J. Signerska-Rynkowska, P. Bartłomiejczyk, *Periodic and chaotic dynamics in a map-based neuron model*, arXiv:2111.14499 (first posted 2021-11-29), https://arxiv.org/abs/2111.14499; sections 2.2–2.3.
2. Y. A. Kuznetsov, *Elements of Applied Bifurcation Theory*, third edition, Springer (2004). Classical generic normal-form context, not a source for the claimed model-specific constants.
