# Sharp two-sample quasi-Banach Lebesgue constants and a symmetry-breaking transition for the Laplace kernel

## Finding

Let \(K(s,t)=e^{-|s-t|}\) on \(\mathbb R\). For two distinct samples \(a<b\), write \(h=b-a\), let \(0<p<1\), and set
\[
\Lambda_p(h)=\sup_{t\in\mathbb R}\left\|\begin{pmatrix}1&e^{-h}\\e^{-h}&1\end{pmatrix}^{-1}\begin{pmatrix}K(a,t)\\K(b,t)\end{pmatrix}\right\|_p^p.
\]
This is the sharp \(p\)-th-power coefficient amplification (and the smallest relaxed sample-span representer penalty factor) for the two samples in the coefficient \(\ell^p\) kernel space.

Define the critical separation
\[
h_c(p)=2\operatorname{arctanh}\sqrt{1-p}=2\operatorname{arsinh}\sqrt{\frac{1-p}{p}}.
\]
If \(0<h\le h_c(p)\), the unique maximizer is the midpoint \(t=(a+b)/2\), and
\[
\boxed{\Lambda_p(h)=2^{1-p}\bigl(\cosh(h/2)\bigr)^{-p}.}
\]
If \(h>h_c(p)\), there are exactly two maximizers \(t=a+x_*(p,h)\) and \(t=b-x_*(p,h)\), where \(0<x_*(p,h)<h/2\) is the unique solution in this interval of
\[
\frac{\cosh x}{(\sinh x)^{1-p}}=
\frac{\cosh(h-x)}{(\sinh(h-x))^{1-p}}.
\]
The exact sharp factor in this regime is
\[
\boxed{\Lambda_p(h)=\frac{(\sinh x_*)^p+(\sinh(h-x_*))^p}{(\sinh h)^p}.}
\]
The midpoint is then a strict local minimum of the coefficient-amplification profile on \((a,b)\). At the threshold it remains the unique global maximizer.

The function \(h\mapsto\Lambda_p(h)\) is strictly decreasing, from \(2^{1-p}\) as \(h\downarrow0\) to \(1\) as \(h\to\infty\), and is strictly greater than \(1\) for every finite \(h\). At the onset of symmetry breaking,
\[
\frac h2-x_*(p,h)\sim
\sqrt{\frac{3\sqrt{1-p}}{2-p}}\,\sqrt{h-h_c(p)}
\quad\text{as }h\downarrow h_c(p)\text{ from above}.
\]
For large separation,
\[
x_*(p,h)\sim 2^{p/(1-p)}e^{-ph/(1-p)},\qquad
\Lambda_p(h)-1\sim(1-p)2^{p/(1-p)}e^{-ph/(1-p)}.
\]

There is a closed form for the especially natural sparsity exponent \(p=1/2\): letting \(h_0=\operatorname{arcosh}3\),
\[
\boxed{\Lambda_{1/2}(h)=
\begin{cases}
\sqrt{2/\cosh(h/2)},&0<h\le h_0,\\
\sqrt{\coth(h/2)},&h\ge h_0.
\end{cases}}
\]
For \(h>h_0\), the two maximizing offsets are
\[
x_* =\frac{h-\operatorname{arcosh}(\cosh h-2)}2,
\quad h-x_*,
\]
characterized equivalently by \(\sinh x_*\sinh(h-x_*)=1\).

## Assumptions and scope

The parameter \(p\) is real with \(0<p<1\), the sample sites are arbitrary distinct reals \(a<b\), and the full center domain is \(\mathbb R\). The coefficient space consists of real atomic kernel expansions with an \(\ell^p\) coefficient quasi-norm; the same sharp coefficient bound holds with complex coefficients. The theorem concerns the two-sample coefficient interpolant and the coefficient-penalty factor, not arbitrary sample sets or minimax error for noisy data. The kernel length scale can be restored by replacing \(h\) by the distance divided by that scale.

The injectivity and bounded-evaluation premises hold directly: \(|K|\le1\), \(\ell^p\subseteq\ell^1\), and the distribution identity \((1-\partial_x^2)e^{-|x-t|}=2\delta_t\) shows that a summable atomic expansion vanishing identically has zero coefficients. The two-sample Gram determinant is \(1-e^{-2h}>0\). These observations identify the coefficient-space norm without an unverified representation assumption.

## Proof

**1. Exact cardinal coefficients and localization.** Inverting the two-by-two sample Gram matrix gives
\[
(c_a(t),c_b(t))=
\begin{cases}
(e^{t-a},0),&t\le a,\\
\left(\dfrac{\sinh(b-t)}{\sinh h},\dfrac{\sinh(t-a)}{\sinh h}\right),&a\le t\le b,\\
(0,e^{b-t}),&t\ge b.
\end{cases}
\]
The exterior coefficient cost is at most one. Inside, with \(x=t-a\), it equals \(F_{p,h}(x)=[(\sinh x)^p+(\sinh(h-x))^p]/(\sinh h)^p\). Since \(p-1<0\), its one-sided derivative at \(x=0\) is positive infinite, so its maximum is strictly greater than one and lies inside \((0,h)\).

**2. Global classification of stationary points.** Set \(g(x)=\cosh x\,(\sinh x)^{p-1}\) and \(L(x)=\log g(x)\). The sign of \(F_{p,h}'(x)\) is the sign of \(g(x)-g(h-x)\). Direct differentiation gives
\[
L'(x)=\tanh x-(1-p)\coth x,
\quad L''(x)=\operatorname{sech}^{2}x+(1-p)\operatorname{csch}^{2}x>0.
\]
Moreover \(L''\) is strictly decreasing on \((0,\infty)\). On \(0<x<h/2\) put \(H(x)=L(x)-L(h-x)\). Then
\[
H''(x)=L''(x)-L''(h-x)>0,
\quad H(h/2)=0,
\quad H(x)\to+\infty\ (x\downarrow0).
\]
The sign of \(H'(h/2)=2L'(h/2)\) changes precisely when \(\tanh^2(h/2)=1-p\), i.e. at \(h=h_c(p)\). If \(h\le h_c\), strict convexity gives \(H'<0\) on the entire left half, whence \(H>0\); thus the profile rises strictly to the midpoint, then falls by symmetry. If \(h>h_c\), \(H\) is negative just left of the midpoint yet tends to \(+\infty\) at zero; strict convexity gives exactly one zero \(x_*\) in \((0,h/2)\), with the sign positive before and negative after. Accordingly the only global maxima are \(x_*\) and \(h-x_*\), and the midpoint is a strict local minimum. Substituting \(x=h/2\) in the first regime gives its explicit formula.

**3. Strict separation monotonicity.** At fixed \(0<\theta<1\), each of \(\sinh(\theta h)/\sinh h\) and \(\sinh((1-\theta)h)/\sinh h\) decreases strictly as \(h\) increases: \(z\mapsto z\coth z\) is strictly increasing for positive \(z\). Evaluating at the interior maximizer for the larger separation proves strict decrease of \(\Lambda_p\). The small-separation limit follows from \(\sinh(\theta h)/\sinh h\to\theta\) and strict concavity of \(\theta^p+(1-\theta)^p\). The large-separation limit follows from Step 4.

**4. Endpoint and bifurcation asymptotics.** Write \(u_0=h_c/2\), \(u=h/2\), and \(\delta=u-x_*\). Taylor expansion of the stationary equation \(L(u-\delta)=L(u+\delta)\), with \(L'(u_0)=0\), gives
\[
\delta^2\sim-\frac{6L''(u_0)(u-u_0)}{L'''(u_0)}.
\]
Here \(L''(u_0)=2p\) and \(L'''(u_0)=-2p(2-p)/\sqrt{1-p}\), yielding the stated square-root coefficient. For \(h\to\infty\), the unique off-center maximizer tends to the left endpoint: at any fixed \(x>0\), \(g(h-x)/g(x)\to\infty\), so the unique left root lies below \(x\). In the stationarity equation \(g(x_*)=g(h-x_*)\), the two sides are asymptotic to \(x_*^{p-1}\) and \(2^{-p}e^{ph}\), respectively, hence \(x_*\sim2^{p/(1-p)}e^{-ph/(1-p)}\). Expanding the two cardinal coefficients at that root and using the stationary identity yields \(F_{p,h}(x_*)-1\sim(1-p)x_*\), as claimed.

**5. Exact half-power branch.** For \(p=1/2\), squaring the stationary equation is legitimate because all quantities are positive. With \(z=\sinh x\) and \(w=\sinh(h-x)\), it becomes \(z+z^{-1}=w+w^{-1}\), equivalent to either \(z=w\) (midpoint) or \(zw=1\). The second case occurs off-center exactly when \(\sinh(h/2)>1\), i.e. \(h>\operatorname{arcosh}3\). The identity \(2\sinh x\sinh(h-x)=\cosh h-\cosh(h-2x)\) yields the explicit offsets. When \(zw=1\), one also has \(z+w=\cosh h-1\), so \((\sqrt z+\sqrt w)^2=\cosh h+1\). Dividing by \(\sinh h\) and taking the square root gives \(\Lambda_{1/2}(h)=\sqrt{\coth(h/2)}\). The midpoint formula supplies the other branch; they agree at the threshold.

**6. Sharp coefficient and penalty interpretation.** For any absolutely summable expansion \(f=\sum_t\alpha_tK(t,\cdot)\) with \(\ell^p\) coefficients, its unique two-sample interpolant has coefficient vector \(c=\sum_t\alpha_t(c_a(t),c_b(t))\). Scalar \(p\)-subadditivity gives \(\|c\|_p^p\le\Lambda_p(h)\sum_t|\alpha_t|^p\), extended to countable sums by Fatou. Taking the sole atom at any maximizing \(t\) proves sharpness of the coefficient penalty. The equivalence to the smallest relaxed representer factor for arbitrary continuous sample-value losses follows also from the coefficient criterion in Wang–Song–Zhang, Theorem 27.

## Verification

The standalone file `check.py` independently evaluates the two-by-two inverse, the exact cardinal functions, the stationary equation, the two phase branches, the square-root onset, the half-power closed form, and large-separation behavior for multiple exponents and separations. It uses only Python's standard library. These finite tests supplement, but do not replace, the all-parameter analytical argument above. Run with `python3 check.py` from the package directory.

## Relationship to prior work

Wang, Song and Zhang (arXiv:2611.08032, first posted 2026-11-05), Sections 3–4, introduce the \(0<p<1\) generalized Lebesgue constant and show it equals the sharp relaxed representer penalty factor. Their two-point Laplace-kernel example establishes qualitative failure of the exact sample-span representer theorem; their exponential-decay theorem supplies dimension-uniform upper bounds. The present theorem determines the exact two-point factor for all separations and exponents, including all optimizing center locations, a nontrivial symmetry-breaking threshold, its bifurcation and large-gap constants, and a closed half-power formula. The general factor criterion itself is prior art and is not claimed as new.

Bejancu (arXiv:2009.00711) studies ordinary \(L^\infty\) Lebesgue constants for infinite-grid Matérn cardinal interpolation; its object, parameter range, and statement are different. Other two-point interpolation and exponential-kernel condition-number results do not determine the \(p\)-power coefficient maximum in this quasi-Banach problem. No claim of priority beyond the literature actually compared is made.

## Limitations

Only two real sampling sites and the one-dimensional Laplace kernel are covered. The threshold does not classify multi-site sample configurations, other Matérn smoothness values, arbitrary alternative center domains, or optimal generalization error. The published-literature comparison is not an exhaustive priority proof. The asymptotic statements are for fixed \(p\in(0,1)\), not uniform as \(p\) approaches either endpoint.

## References

1. T. Wang, G. Song and H. Zhang, *Reproducing Kernel (Quasi-)Banach Spaces with the \(\ell^p\) Coefficient Norms*, arXiv:2611.08032, initial version posted 2026-11-05. https://arxiv.org/abs/2611.08032
2. A. Bejancu, *Uniformly bounded Lebesgue constants for scaled cardinal interpolation with Matérn kernels*, arXiv:2009.00711, initial version 2020-08-28. https://arxiv.org/abs/2009.00711
