# Sharp seasonal-length threshold for weak persistence in a smooth nonautonomous metapopulation

## Finding

Consider the occupied-patch fraction \(p(t)\) in the time-varying Levins model
\[
\dot p=c(t)p(1-p)-e(t)p,
\qquad 0<p(0)\le1.
\]
Fix \(c(t)\equiv2\) and construct smooth positive extinction rates \(e(t)=2-r(t)\) from successive hostile and favorable plateaux. In cycle \(n\), first impose \(r=-1\) for duration \(H_n\), smoothly switch to \(r=+1\), maintain it for duration \(F_n\), and smoothly switch back. Assume \(H_n\to\infty\), \(F_n\to\infty\), both durations are strictly positive, the transition widths \(\eta_n\to0\), and \(F_n-H_n\to\delta\in\mathbb R\). Each switch is symmetric in the sense defined below.

The upper and lower Bohl exponents of \(c-e\) are **identically \(+1\) and \(-1\)** for every such calendar. Nevertheless, for **every** initial \(p(0)\in(0,1]\), the occupied-patch trajectory has the exact classification
\[
\liminf_{t\to\infty}p(t)=0,\qquad
\limsup_{t\to\infty}p(t)=
\begin{cases}
\displaystyle \frac{1-e^{-\delta}}{2(1+e^{-\delta})},&\delta>0,\\[3pt]
0,&\delta\le0.
\end{cases}
\]
Thus an asymptotically positive *finite difference* of favorable minus hostile season lengths yields weak persistence; zero or negative limiting difference gives extinction. The positive upper limit does not depend on initial occupancy or the choice of vanishing, symmetric smooth transition widths.

In the natural balanced linear-length calendar \(H_n=F_n=n\), \(\eta_n=2^{-n}\), if \(T_n\) is the beginning of hostile season \(n\), then
\[
\lim_{n\to\infty}n\,p(T_n)=\frac14.
\]
This critical algebraic decay at season boundaries coexists with arbitrarily deep hostile-season troughs.

## Assumptions and scope

Choose any \(C^\infty\) function \(\theta:[0,1]\to[0,1]\) satisfying \(\theta(0)=0\), \(\theta(1)=1\), all derivatives vanish at the endpoints, and \(\theta(u)+\theta(1-u)=1\). One explicit choice on \(0<u<1\) is
\[
\theta(u)=\frac{e^{-1/u}}{e^{-1/u}+e^{-1/(1-u)}},
\]
with its continuous endpoint extensions.

Set \(T_1=0\). On \([T_n,T_{n+1}]\), in chronological order, define \(r(t)\) to be (i) \(-1\) for \(H_n\) units, (ii) \(-1+2\theta(s/\eta_n)\) for \(0\le s\le\eta_n\), (iii) \(+1\) for \(F_n\) units, and (iv) \(+1-2\theta(s/\eta_n)\) for \(0\le s\le\eta_n\), where \(T_{n+1}=T_n+H_n+F_n+2\eta_n\). Require \(H_n,F_n,\eta_n>0\), \(H_n,F_n\to\infty\), \(\eta_n\to0\), and \(F_n-H_n\to\delta\in\mathbb R\). This defines \(r\in C^\infty([0,\infty))\) and \(1\le e(t)\le3\). There are no finite-time accumulation points of switches. The two ramps have zero signed growth integral by reflection symmetry.

The Bohl exponents use all intervals \([s,t]\) with \(t-s\to\infty\), not only intervals starting at zero. Occupancy represents a deterministic fraction of occupied habitat patches; neither demographic stochastic extinction nor higher-dimensional patch networks is included.

## Proof

**1. Reciprocal reduction and positivity.** Since \(p'=rp-2p^2\), the interval \((0,1]\) is forward invariant. The reciprocal variable \(y=1/p\) satisfies the exact linear equation \(y'=-r(t)y+2\). Across any interval \([a,b]\),
\[
y(b)=e^{-\int_a^b r}\,y(a)
+2\int_a^b e^{-\int_s^b r}\,ds.
\]
The second term is positive.

**2. Exact cycle recurrence.** Write \(y_n=y(T_n)\) and \(q_n=e^{H_n-F_n}\). A hostile plateau maps \(y\mapsto e^{H_n}y+2(e^{H_n}-1)\), whereas a favorable plateau maps \(y\mapsto e^{-F_n}y+2(1-e^{-F_n})\). On each ramp, \(\int r=0\), so the homogeneous multiplier is exactly one and the additive term \(B_n\) or \(E_n\) obeys
\[
2\eta_n e^{-\eta_n}\le B_n,E_n\le2\eta_n e^{\eta_n}.
\]
Composing the four maps gives the **exact** recurrence
\[
\begin{aligned}
y_{n+1}&=q_ny_n+b_n,\\
b_n&=2q_n(1-e^{-H_n})+2(1-e^{-F_n})+e^{-F_n}B_n+E_n.
\end{aligned}
\]
Since \(q_n\to q=e^{-\delta}\in(0,\infty)\), both long plateaux diverge, and \(\eta_n\to0\), it follows that \(b_n\to2(1+q)>0\).

**3. Complete phase classification.** If \(\delta>0\), then \(q<1\) and the affine recurrence has the attracting limit
\[
Y=\frac{2(1+q)}{1-q}.
\]
Indeed the error \(y_{n+1}-Y=q_n(y_n-Y)+(q_n-q)Y+(b_n-2(1+q))\) tends to zero under eventual uniform contraction. Hence \(p(T_n)\to1/Y\). If \(\delta<0\), then eventually \(q_n>1+\varepsilon\) for some \(\varepsilon>0\), so \(y_n\to\infty\). If \(\delta=0\), then \(q_n\to1\), \(b_n\to4\); for every \(\varepsilon\in(0,1)\), eventually \(y_{n+1}\ge(1-\varepsilon)y_n+3\), implying \(\liminf y_n\ge3/\varepsilon\), and therefore \(y_n\to\infty\). Thus \(p(T_n)\to0\) for every \(\delta\le0\).

**4. Extrema within cycles.** The hostile plateau decreases \(p\), and its endpoint obeys \(p\le e^{-H_n}\). The subsequent ramp has \(\eta_n\to0\), so its occupancy differs multiplicatively from the plateau endpoint by at most \(e^{3\eta_n}\). The long favorable plateau starts below \(1/2\); there \(p'=p(1-2p)>0\). Its endpoint differs by \(o(1)\) from \(p(T_{n+1})\), because the final ramp has width \(\eta_n\to0\) and \(|p'|\le3\) on \([0,1]\). Therefore the maximal occupancy in a sufficiently late cycle is, up to \(o(1)\), the larger of its two cycle-boundary values. This establishes the stated \(\limsup\). Every hostile plateau has \(p\le e^{-H_n}\) at its end, yielding \(\liminf p=0\).

**5. Identical Bohl exponents.** For \(D=c-e=r\), one always has \(-1\le D(t)\le1\). Hostile plateaux of lengths \(H_n\to\infty\) attain mean \(-1\); favorable plateaux of lengths \(F_n\to\infty\) attain mean \(+1\). Consequently \(\beta^-(D)=-1\) and \(\beta^+(D)=+1\), independently of \(\delta\).

**6. Critical rate for linearly lengthening balanced seasons.** With \(H_n=F_n=n\) and \(\eta_n=2^{-n}\), \(q_n=1\) exactly and the recurrence yields \(b_n=4+O(e^{-n}+2^{-n})\). Therefore \(y_n=4n+O(1)\) by summation, which proves \(n p(T_n)\to1/4\). This rate is asserted only for this specified calendar, not for every sequence with \(\delta=0\).

## Verification

The accompanying pure-Python `CHECK.py` numerically integrates the additive ramp terms in the exact reciprocal cycle map and compares finite long-season trajectories with the analytical limits. It checks four positive offsets, three negative offsets and the zero-offset critical rate, together with ramp symmetry and quantitative coefficient bounds. The checker has no nonstandard dependencies and can be run by `python3 CHECK.py`. These finite tests support, but do not replace, the infinite proofs above.

## Relationship to prior work

Robledo and Bustamante (arXiv:2504.20396v1, §§2–4 and Appendices A–B) introduce the time-varying Levins model, the reciprocal formula and Bohl-exponent criteria, prove zero lower occupancy in the mixed-sign case, and construct an example of weak persistence using tuned alternating piecewise-constant rates. Those results are **not** claimed as new. The present theorem addresses the residual upper-limit question for a structured family with smooth positive rates and long favorable/hostile blocks: it gives a sharp necessary-and-sufficient duration-offset condition, an exact nonzero peak and a critical power law. It is an application of the known reciprocal reduction with a new complete asymptotic calendar classification.

Amster, Robledo and Sepúlveda (arXiv:2412.02952v1) treat almost-periodic ecological forcing; such forcing does not contain the increasingly long plateaux with distinct Bohl extremes considered here. Standard scalar nonautonomous logistic theory provides the general variation-of-constants formula, but that identity alone does not state this phase classification for diverging seasons. Some broader results on asymptotically affine positive recurrences may imply portions of the recurrence argument; independent historical-priority review remains appropriate.

## Limitations

The theorem covers a deliberately specified deterministic seasonal calendar, not arbitrary mixed-sign Bohl forcing. Long plateaux increasing without bound are a mathematical stress test, rather than an empirical seasonal forecast. The extinction conclusion is convergence of deterministic occupancy to zero, not finite-population extinction time. The \(1/n\) critical law is for the explicitly balanced linear schedule and is not universal over all vanishing season differences. Historical novelty is literature-bounded; no independent scientific validation has been conducted.

## References

1. G. Robledo and R. Bustamante, *Generalizing the Levins metapopulation model to time varying colonization and extinction rates*, arXiv:2504.20396v1, first publicly available 2025-04-29. https://arxiv.org/abs/2504.20396
2. P. Amster, G. Robledo and D. Sepúlveda, *Persistence/extinction scenarios in an almost periodic metapopulation with competition and habitat destruction*, arXiv:2412.02952v1, 2024-12-04. https://arxiv.org/abs/2412.02952
3. R. Levins, *Some demographic and genetic consequences of environmental heterogeneity for biological control*, Bulletin of the Entomological Society of America **15** (1969), 237–240.
