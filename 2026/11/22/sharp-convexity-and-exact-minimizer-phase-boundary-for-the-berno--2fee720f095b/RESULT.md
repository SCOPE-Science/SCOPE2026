# Sharp convexity and exact-minimizer phase boundary for the Bernoulli logistic forward–backward envelope

## Finding

For a single real-valued logit with a soft Bernoulli target, the smooth forward–backward envelope has an **exact label-dependent global convexity frontier** despite the original loss being convex. In the standard forward–backward stepsize range the envelope remains an exact, uniquely minimized surrogate even after it loses convexity.

Precisely, for \(q\in(0,1)\), let
\[
f_q(x)=\log(1+e^x)-qx,\qquad
E_{\gamma,q}(x)=f_q(x)-\frac{\gamma}{2}[f_q'(x)]^2.
\]
Then, for every \(\gamma>0\),
\[
\boxed{\ E_{\gamma,q}\text{ is globally convex }\iff\gamma\le\gamma_c(q):=\frac{3}{1-q+q^2}.\ }
\]
It is actually strictly convex at the boundary. For every \(\gamma>\gamma_c(q)\), its curvature is negative on precisely one open interval. For every \(0<\gamma<4\), the envelope has the unique global minimizer \(x_* =\log(q/(1-q))\), identical to the original loss. Thus every unbalanced label \(q\ne1/2\) has a nonempty **nonconvex-but-exact** stepsize window
\[
\frac{3}{1-q+q^2}<\gamma<4.
\]
The balanced target \(q=1/2\) is unique in retaining global convexity throughout \(0<\gamma<4\).

## Assumptions and scope

The variable is scalar \(x\in\mathbb R\), the soft label satisfies \(0<q<1\), the smooth term is \(f_q\) above, and the nonsmooth term is **identically zero**. Consequently its Moreau envelope vanishes and the usual forward–backward envelope reduces to the displayed function. All arithmetic and derivatives concern the exact real-valued functions, with no discretization or regularizer. The logistic curvature bound is \(\sup_x f_q''(x)=1/4\), giving the standard admissible interval \(0<\gamma<4\) for the familiar exactness statement. The convexity classification itself is proved for all \(\gamma>0\).

Write \(p=p(x)=1/(1+e^{-x})\). This is a bijection from \(\mathbb R\) to \((0,1)\). For \(\gamma>\gamma_c(q)\), set
\[
p_{\pm}=\frac{1+q\pm\sqrt{1-q+q^2-3/\gamma}}{3}.
\]
Both points belong to \((0,1)\), and the **entire** negative-curvature region is precisely
\[
\log\frac{p_-}{1-p_-}<x<\log\frac{p_+}{1-p_+}.
\]
For a fixed \(3<\gamma<4\), convexity as a function of the target holds exactly when
\[
\left|q-\frac12\right|\le\sqrt{\frac3\gamma-\frac34}.
\]

## Proof

Differentiate in logistic probability coordinates:
\[
f_q'(x)=p-q,\quad f_q''(x)=p(1-p),\quad
f_q'''(x)=p(1-p)(1-2p).
\]
By the product rule,
\[
\begin{aligned}
E_{\gamma,q}'(x)&=(p-q)[1-\gamma p(1-p)],\\
E_{\gamma,q}''(x)&=p(1-p)\left[1-\gamma\{p(1-p)+(p-q)(1-2p)\}\right]\\
&=p(1-p)\left[1-\gamma Q_q(p)\right],
\end{aligned}
\]
where
\[
Q_q(p)=-3p^2+2(1+q)p-q
=-3\left(p-\frac{1+q}{3}\right)^2+\frac{1-q+q^2}{3}.
\]
The maximizing probability \(p_0=(1+q)/3\) belongs to \((0,1)\); hence the maximum of \(Q_q\) over the entire probability range is exactly \((1-q+q^2)/3\). Since \(p(1-p)>0\), nonnegative curvature everywhere is equivalent to \(\gamma\le 3/(1-q+q^2)\). At equality the curvature vanishes at exactly one point, remaining positive elsewhere, and the derivative is strictly increasing, so strict convexity remains. Above the threshold, the inequality \(Q_q(p)>1/\gamma\) defines exactly the open interval between \(p_-\) and \(p_+\), whose endpoints lie inside \((0,1)\) because \(Q_q(0)=-q<0\) and \(Q_q(1)=q-1<0\). This proves the full sign classification and location formula.

For \(0<\gamma<4\), the uniform inequality \(p(1-p)\le1/4\) makes \(1-\gamma p(1-p)>0\) for all finite \(x\). Thus \(E'_{\gamma,q}\) has exactly the sign of \(p-q\), and vanishes only at \(p=q\), i.e. \(x_*\). Furthermore \(f_q(x)\to+\infty\) at both ends of the real line when \(q\in(0,1)\), while \(|f_q'(x)|\le1\). Therefore \(E_{\gamma,q}\) is coercive and \(x_*\) is its unique global minimizer. The inequality \(q^2-q+1\ge3/4\), with equality exactly at \(q=1/2\), proves the balanced-label claim. Rearranging \(\gamma\le3/(q^2-q+1)\) yields the fixed-stepsize target condition.

## Verification

The accompanying \(\texttt{verify.py}\) independently recomputes the polynomial curvature identity, its maximum and zero-curvature roots in exact SymPy arithmetic, checks the sharp threshold at rational labels, and runs additional floating-point sign-regression cases. In particular, the exact witness \(q=1/10\), \(\gamma=7/2\), and \(p=11/30\) satisfies
\[
\gamma_c(1/10)=\frac{300}{91}<\frac72<4,\qquad
E''_{7/2,1/10}\!\left(\log\frac{11}{19}\right)
=-\frac{7733}{540000}<0.
\]
The same envelope still minimizes uniquely at \(x_*=-\log9\). These finite checks supplement the analytic proof; they are not substituted for its universal quantifiers. Reproduction requires Python 3 and SymPy: \(\texttt{python verify.py}\).

## Relationship to prior work

The forward–backward envelope formula and exactness interval belong to established splitting literature, including Giselsson and Fält's envelope analysis (2018) and the exposition by Zhang (2026). Zhang, Gao and Udell (2026), the motivating paper, analyze smoothness and sufficient convexity conditions for envelope-based online scaling and discuss logistic regression. The statement here is not a general convexity theorem for splitting: it is a sharp **necessary-and-sufficient** curvature and minimizer classification for the scalar soft-label logistic model, including a nonconvex-yet-exact interval and explicit negative-curvature locus. Publicly accessible material for the motivating paper does not establish this precise classification; unavailable portions could contain relevant analysis and therefore publication priority remains unconfirmed.

## Limitations

This result has \(g\equiv0\), one scalar logit, and one soft label. It does not imply the same frontier for multi-feature logistic regression, regularized logistic objectives, matrix preconditioners, generalized DRS/ADMM, or algorithmic acceleration. Convexity and unique minimization concern the envelope, not a statement that all numerical iterations converge at arbitrary stepsizes. The original loss is convex throughout; only its envelope can be nonconvex. Independent external validation and exhaustive historical-priority verification have not been performed.

## References

- Wanyu Zhang, Wenzhi Gao, Madeleine Udell, *Operator Splitting Methods with Online Scaling*, arXiv:2609.10732, first posted 2026-09-09. https://arxiv.org/abs/2609.10732
- Pontus Giselsson and Mattias Fält, *Envelope Functions: Unifications and Further Properties*, *Journal of Optimization Theory and Applications* (2018), DOI 10.1007/s10957-018-1328-z. https://link.springer.com/article/10.1007/s10957-018-1328-z
- Wanyu Zhang, *Envelope function for extended DRS*, 2026-06-10. https://zwyhahaha.github.io/2026/06/10/envelope-function-for-extended-drs/
