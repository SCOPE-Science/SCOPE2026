# A sharp weighted-perimeter transition and strict convexity for regular approximations of a disk

## Finding
Let \(B\subset\mathbb R^2\) be the closed Euclidean unit disk. For \(n\ge3\), let \(Q_n(R)\) be any centered regular \(n\)-gon with circumradius \(R>0\). For conjugate weights \(p,q\in[1,\infty]\), so that \(1/p+1/q=1\), define the weighted perimeter deviation
\[
\mathcal D_{p,q}(B,Q)=p\bigl[\mathcal H^1(\partial B\setminus\operatorname{int}Q)-\mathcal H^1(\partial Q\cap B)\bigr]+q\bigl[\mathcal H^1(\partial Q\setminus\operatorname{int} B)-\mathcal H^1(\partial B\cap Q)\bigr].
\]
At the endpoints, a term multiplied by \(\infty\) is zero if its bracket is zero and is \(+\infty\) otherwise. Put \(\alpha=\pi/n\) and \(T_n=1+\sec\alpha\). The **unique optimal circumradius** among all centered regular \(n\)-gons is
\[
\boxed{R_{n,p}=\begin{cases}1,&1\le p\le T_n,\\
\cos(2\arctan(\tan\alpha/p))/\cos\alpha,&T_n<p<\infty,\\
\sec\alpha,&p=\infty.
\end{cases}}
\]
The exact optimized deviation \(D_{n,p}=\min_{R>0}\mathcal D_{p,q}(B,Q_n(R))\) is
\[
\boxed{D_{n,p}=\begin{cases}
2np(\alpha-\sin\alpha),&1\le p\le T_n,\\
2n\,\dfrac p{p-1}\left[2p\arctan\left(\dfrac{\tan\alpha}{p}\right)-\tan\alpha-\alpha\right],&T_n<p<\infty,\\
2n(\tan\alpha-\alpha),&p=\infty.
\end{cases}}
\]
For every fixed \(p\in[1,\infty]\), the sequence \(D_{n,p}\), \(n=3,4,\ldots\), is **strictly decreasing and strictly convex**:
\[
D_{n-1,p}+D_{n+1,p}>2D_{n,p}\quad(n\ge4).
\]
More generally, the expression defines a strictly convex function of the real variable \(n\ge3\).

For every finite \(p>T_n\), an unrestricted Euclidean convex polygon with at most \(n\) vertices that is wholly contained in \(B\), or wholly contains \(B\), cannot minimize \(\mathcal D_{p,q}(B,Q)\). Indeed, the exhibited crossing regular polygon has deviation **strictly smaller** than the infimum in either of the two nested classes. This conclusion is a sharp sufficient transition for nonnested competitors, not a classification of unrestricted optimizers.

Finally, for fixed \(p\),
\[
\boxed{\lim_{n\to\infty}n^2D_{n,p}=
\begin{cases}
\dfrac{p\pi^3}{3},&1\le p\le2,\\
\dfrac{2\pi^3(p^2-2)}{3p(p-1)},&2<p<\infty,\\
\dfrac{2\pi^3}{3},&p=\infty.
\end{cases}}
\]

## Assumptions and scope
Euclidean perimeter means one-dimensional Hausdorff measure on the boundary. \(Q_n(R)\) may be rotated arbitrarily about the origin; its orientation does not affect the result. Its circumradius \(R\) is unrestricted and positive, and only the **centered regular** family is optimized in the exact formula. The weights are conjugate: \(q=p/(p-1)\) when \(1<p<\infty\), with limiting choices \((p,q)=(1,\infty)\) and \((\infty,1)\). All algebraic and trigonometric inequalities are for \(n\ge3\), hence \(0<\alpha\le\pi/3\). The strict global nonnesting obstruction applies only for finite \(p>T_n\).

## Proof
**1. Exact crossing geometry.** Write \(d=R\cos\alpha\) for the polygon's inradius, and \(h=R\sin\alpha\) for half of one edge length. For \(R\le1\), the polygon is inside \(B\), and the deviation is \(p(2\pi-2nR\sin\alpha)\), strictly decreasing in \(R\). For \(R\ge\sec\alpha\), the polygon contains \(B\), and the deviation is \(q(2nR\sin\alpha-2\pi)\), strictly increasing in \(R\). Thus every optimum lies in \([1,\sec\alpha]\).

In the crossing interval \(1<R<\sec\alpha\), put \(\beta=\arccos d\in(0,\alpha)\). Each edge crosses the unit circle at tangent-coordinate values \(\pm\sin\beta\); its outward portion has total length \(2(h-\sin\beta)\). On the circle, each edge-normal sector loses the central arc \((-\beta,\beta)\); the total length of circle outside the polygon is \(2n\beta\). Therefore the two nonnegative bracketed terms in the definition are exactly
\[
A=2n(\beta-\sin\beta),\qquad
C=2n\bigl[\tan\alpha\cos\beta-\sin\beta-\alpha+\beta\bigr],
\]
and the deviation divided by \(2n\) is
\[
F_p(\alpha,\beta)=(p+q)(\beta-\sin\beta)+q\tan\alpha\cos\beta-q\alpha,\qquad0\le\beta\le\alpha.
\tag{1}
\]
Formula (1) also holds at the two endpoints, and the radial monotonicity outside the crossing interval proves that minimizing it captures **all** \(R>0\).

**2. Unique optimizer and exact profile.** For finite \(1<p<\infty\),
\[
\frac{\partial F_p}{\partial\beta}=(p+q)(1-\cos\beta)-q\tan\alpha\sin\beta
=2\sin(\beta/2)\bigl[(p+q)\sin(\beta/2)-q\tan\alpha\cos(\beta/2)\bigr].
\]
Since \(q/(p+q)=1/p\), this derivative is negative before \(\beta_*=2\arctan(\tan\alpha/p)\) and positive afterward. Thus the unique minimum occurs at \(\beta=\min\{\alpha,\beta_*\}\). The condition \(\beta_*\ge\alpha\) is equivalent to
\[
p\le\frac{\tan\alpha}{\tan(\alpha/2)}=1+\sec\alpha=T_n.
\]
For \(p\le T_n\), choose \(\beta=\alpha\), yielding the first branches of the two displayed formulas. For \(p>T_n\), substitute \(t=\tan\alpha/p=\tan(\beta_*/2)\) into (1). The identity \(-\sin\beta_*+t\cos\beta_*=-t\) gives
\[
F_p(\alpha,\beta_*)=q[2p\arctan(\tan\alpha/p)-\tan\alpha-\alpha].
\]
Since \(R=\cos\beta/\cos\alpha\), this also proves the radius formula. The limit cases \(p=1\) and \(p=\infty\) follow directly from the zero/positive interpretations of infinite weights, and each has a unique endpoint optimizer.

**3. Strict convexity in polygon order.** For fixed \(p\), set \(f_p(\alpha)=D_{\pi/\alpha,p}\,\alpha/(2\pi)\), equivalently \(f_p(\alpha)=D_{n,p}/(2n)\). On the inscribed branch \(f_p(\alpha)=p(\alpha-\sin\alpha)\), so \(f_p''(\alpha)=p\sin\alpha>0\). On the finite-weight crossing branch, direct differentiation yields
\[
f_p''(\alpha)=\frac{2p\tan\alpha\sec^2\alpha}{(p-1)(p^2+\tan^2\alpha)^2}
\bigl[p^4-2p^2\sec^2\alpha-\tan^4\alpha\bigr].\tag{2}
\]
Write \(s=\sec\alpha\in(1,2]\) and \(H(p,s)=p^4-2s^2p^2-(s^2-1)^2\). On this branch \(p>1+s\), and
\[
H(1+s,s)=2s(2-s)(s+1)^2\ge0,\qquad
\frac{\partial H}{\partial p}=4p(p^2-s^2)>0\quad(p\ge1+s).
\]
Consequently (2) is strictly positive throughout the crossing branch. At the branch transition, the two explicit expressions for \(f_p\) and their first derivatives agree (or equivalently the optimizer meets the endpoint with vanishing directional derivative). Hence \(f_p\) is continuously differentiable and strictly convex on \((0,\pi/3]\). For \(p=\infty\), \(f_\infty(\alpha)=\tan\alpha-\alpha\) has \(f_\infty''(\alpha)=2\tan\alpha\sec^2\alpha>0\); \(p=1\) is covered by the inscribed branch.

For real \(x\ge3\), set \(G_p(x)=2x f_p(\pi/x)\). On smooth pieces,
\[
G_p''(x)=\frac{2\pi^2}{x^3}f_p''(\pi/x)>0.
\]
The joining point is \(C^1\), so \(G_p\) is strictly convex globally. As \(f_p(0)=0\) and \(f_p\) is strictly convex, \(f_p(\alpha)<\alpha f_p'(\alpha)\), giving \(G_p'(x)=2[f_p(\alpha)-\alpha f_p'(\alpha)]<0\). This proves both strict sequence inequalities.

**4. Unrestricted nonnesting obstruction.** If a convex polygon \(Q\) with at most \(n\) vertices is contained in \(B\), the second bracket is zero and
\(\mathcal D_{p,q}(B,Q)=p(2\pi-\operatorname{per}(Q))\). The classical chord/Jensen argument gives \(\operatorname{per}(Q)\le2n\sin(\pi/n)\), with equality at a regular inscribed polygon. If instead \(B\subseteq Q\), the first bracket vanishes and \(\mathcal D_{p,q}(B,Q)=q(\operatorname{per}(Q)-2\pi)\). Moving supporting edges to tangency and applying Jensen to successive outward-normal gaps gives \(\operatorname{per}(Q)\ge2n\tan(\pi/n)\), with equality at a circumscribed regular polygon. For finite \(p>T_n\), the strictly interior minimizer \(0<\beta_*<\alpha\) has \(F_p(\alpha,\beta_*)\) strictly smaller than *both* endpoint values, because the derivative in step 2 changes sign strictly. Thus a crossing regular polygon beats the entire nested-inscribed and nested-circumscribed classes, proving the obstruction without assuming that an unrestricted optimizer is regular.

**5. Asymptotics.** As \(n\to\infty\), \(T_n\to2\) from above. For fixed \(p\le2\), the inscribed branch gives \(f_p(\alpha)=p\alpha^3/6+O_p(\alpha^5)\). For finite fixed \(p>2\), expansion of the crossing branch gives \(f_p(\alpha)=(p^2-2)\alpha^3/[3p(p-1)]+O_p(\alpha^5)\). For \(p=\infty\), \(f_\infty(\alpha)=\alpha^3/3+O(\alpha^5)\). Multiplying by \(2n\) with \(\alpha=\pi/n\) yields the stated three-branch sharp limit.

## Verification
Run `python3 verify.py` with Python 3 and only its standard library. The program checks the transition polynomial identity using rational arithmetic, tests the claimed optimal radius against deterministic grids for multiple orders and weights, independently approximates the two boundary-measure brackets by sampling actual circle arcs and polygon edges, checks discrete convexity across finite examples including the threshold, and verifies large-order asymptotic constants. These tests are supplements: steps 1–5 give the proof for all admissible real weights, all integer orders, and the nonnesting comparison.

## Relationship to prior work
Basit and Lángi [1], whose public preprint first appeared on 2023-07-08, introduce exactly the weighted perimeter-deviation functional and pose its Dowker-type convexity as Problem 1. Their results concern mainly one-sided and disk-polygon approximation; they do not give the centered regular Euclidean-polygon profile, its weight-driven transition, or the nonnesting obstruction. Fodor [2] recounts Eggleston's classical theorem: for **unweighted** perimeter deviation, the unrestricted closest polygon is inscribed. Here \(p=q=2\) is a positive multiple of that earlier case, so its inscribed optimizer is prior; the new weight-dependent behavior starts beyond that case. The already published exact projection-shadow metric of a disk [3] uses an integral of absolute support-function discrepancy, not the present boundary-arc deviation; the published symmetric disk-polygon result [4] uses intersections of equal disks and a two-sided **area** deviation, rather than line-sided polygons and weighted **perimeter** deviation. Neither asserts or implies the displayed transition and convex sequence.

## Limitations
The exact optimizer is proved only among **centered regular polygons**. The unrestricted conclusion is strictly a sufficient nonnesting criterion for finite weights; no global shape optimizer or necessary threshold is claimed for arbitrary polygons. Convexity is proved for the optimized regular-family sequence, not for the full unrestricted problem posed in [1]. The two endpoint-weight conventions are defined by nonnegative bracket limits. The novelty assessment is subject to unindexed earlier work or alternate formulations of weighted perimeter approximation; independent mathematical audit has not been performed.

## References
[1] B. Basit and Z. Lángi, *Dowker-type theorems for disk-polygons in normed planes*, arXiv:2307.04026v1, first public 2023-07-08; current open HTML https://arxiv.org/html/2307.04026v5 (especially Definition 4 and Section 5).

[2] F. Fodor, *Perimeter Approximation of Convex Discs in the Hyperbolic Plane and on the Sphere*, Discrete & Computational Geometry 66 (2021), 1190–1201, https://doi.org/10.1007/s00454-021-00291-7 (introduction and Theorem 1.1 cite Eggleston's 1957 Euclidean result).

[3] *Sharp first intrinsic-volume shadow distance from a disk to origin-containing polygons*, public mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-sharp-first-intrinsic-volume-shadow-distance-from-a-disk-to-orig--e6bedc320bbd/RESULT.md (different deviation).

[4] *Unique optimal two-sided disk approximation within rotationally symmetric disk-polygons*, public mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-unique-optimal-two-sided-disk-approximation-within-rotationally--f77924764139/RESULT.md (different approximating objects and functional).
