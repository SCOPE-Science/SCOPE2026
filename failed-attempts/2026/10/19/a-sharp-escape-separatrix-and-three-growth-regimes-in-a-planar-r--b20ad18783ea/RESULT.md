# A sharp escape separatrix and three growth regimes in a planar rational map

## Finding

For the positive-quadrant slice of the Zhang–Liu–Wei–Jiang–Bi rational map,
\[
 x_{n+1}=x_n\left(1-\frac{q}{1+y_n^2}\right),\qquad y_{n+1}=y_n+c x_n,
 \quad 0<q\le1,\ c>0,\ x_0>0,\ y_0>0,
\]
there is, for every fixed \(q,c,y_0\), a **unique** critical initial velocity \(x_*(q,c,y_0)>0\). If \(0<x_0<x_*\), the orbit converges exponentially to a point of the fixed line \(x=0\); if \(x_0>x_*\), then \(x_n\to v/c>0\) and \(y_n\to+\infty\) ballistically; at \(x_0=x_*\), both \(x_n\to0\) and \(y_n\to+\infty\), at the universal critical scale
\[
 \frac{y_n}{\sqrt{2qn}}\to1,\qquad
 \frac{c x_n}{\sqrt{q/(2n)}}\to1.
\]
Moreover, writing \(u_*=c x_*\) and \(I(y)=\pi/2-\arctan y\),
\[
 qI(y_0)<u_*<\frac{qI(y_0)}{1-q/(1+y_0^2)},
 \qquad \lim_{q\downarrow0}\frac{u_*}{q}=I(y_0).
\]
At \(q=1\) the critical curve is **exactly** \(c x_0y_0=1\). On that curve the further logarithmic law is
\[
 y_n^2=2n+\frac12\log n+C(y_0)+o(1),
\]
with a finite real constant \(C(y_0)\). Above the threshold, writing \(v=\lim_{n\to\infty}cx_n>0\),
\[
 cx_n=v+\frac{q}{vn}+O\left(\frac{\log n}{n^2}\right),\qquad
 y_n=vn+\frac{q}{v}\log n+C+o(1).
\]
These statements apply to every real initial pair in the explicitly stated positive domain and no others are claimed.

## Assumptions and scope

The paper's general map is \(x'=x+ax/(1+y^2)+b\), \(y'=y+cx+d\). Here \(a=-q\), \(b=d=0\), \(0<q\le1\), \(c>0\) and \(x_0,y_0>0\). Define \(u_n=c x_n\), \(g_q(y)=1-q/(1+y^2)\), and \(f(y)=1/(1+y^2)\). Then
\[
 u_{n+1}=g_q(y_n)u_n,\qquad y_{n+1}=y_n+u_n.
\]
Since \(0<g_q(y_n)<1\), the sequence \(u_n\) decreases strictly to some \(v\ge0\), while \(y_n\) increases strictly to a limit in \((y_0,\infty]\). A bounded \(y_n\) necessarily entails \(v=0\).

## Proof

**1. Integral comparison.** Because \(u_k=y_{k+1}-y_k\) decreases, the left-Riemann sum of the decreasing function \(f\) on the consecutive intervals \([y_k,y_{k+1}]\) obeys, for all \(n\ge0\),
\[
 \int_{y_n}^{Y} f(t)\,dt
 \le \sum_{k=n}^{\infty}u_k f(y_k)
 \le \int_{y_n}^{Y} f(t)\,dt+u_n(f(y_n)-f(Y)),
\]
where \(Y=\lim y_k\), with \(f(+\infty)=0\). The right inequality follows by bounding the left-rectangle excess on each interval by \(u_n[f(y_k)-f(y_{k+1})]\) and telescoping. Since
\(u_n-v=q\sum_{k=n}^{\infty}u_kf(y_k)\), it follows that if \(Y=\infty\),
\[
 qI(y_n)\le u_n-v\le qI(y_n)+q u_n f(y_n),\quad
 I(y)=\int_y^\infty f(t)\,dt=\frac\pi2-\arctan y.
\]
For finite \(Y\), the same upper inequality (with \(I(y_n)\)) remains valid.

**2. The two open outcome sets.** Fix \(q\) and \(y_0\), and vary \(u_0>0\). Let \(B\) be the set for which \(Y<\infty\), and \(E\) the set for which \(v>0\). They are disjoint. Both are open: if for some iterate and some \(R>y_n\),
\[
 u_n<\frac{q(R-y_n)}{1+R^2},
\]
then the geometric majorant \(u_{n+j}\le u_n(1-q/(1+R^2))^j\) keeps \(y_{n+j}<R\) forever. Conversely, every orbit with finite \(Y\) eventually satisfies this strict certificate for any fixed \(R>Y\), proving openness of \(B\).

The integral comparison gives the strict sufficient escape certificate
\[
 u_n\left(1-\frac{q}{1+y_n^2}\right)>qI(y_n)\quad\Longrightarrow\quad v>0.
\]
Every orbit with \(v>0\) eventually satisfies this certificate, because then \(y_n\to\infty\), \(u_n\to v\), and \(I(y_n)\to0\). Thus \(E\) is open. The set \(B\) is nonempty: choose \(R=y_0+1\) and \(u_0<q/(1+R^2)\). The set \(E\) is nonempty: as \(u_0\to\infty\), after one step \(y_1=y_0+u_0\to\infty\) and \(u_1=g_q(y_0)u_0\to\infty\), so the escape certificate holds. The positive half-line is connected; hence \((0,\infty)\setminus(B\cup E)\ne\varnothing\). Its orbits necessarily have \(Y=\infty\) and \(v=0\).

**3. Uniqueness and the sharp threshold.** For any such critical orbit, the comparison with \(v=0\) implies
\[
 qI(y_n)\le u_n\le\frac{qI(y_n)}{1-q/(1+y_n^2)},
\]
so \(y_nu_n/q\to1\). Hence
\(y_{n+1}^2-y_n^2=2y_nu_n+u_n^2\to2q\), proving the claimed square-root limits. To prove uniqueness, take two supposed critical orbits with the same \(y_0,q\) and \(0<u_0<\widetilde u_0\). The map is coordinatewise order preserving for positive \(y,u\); therefore \(\widetilde y_n\ge y_n\) and
\[
 \frac{\widetilde u_n}{u_n}
 =\frac{\widetilde u_0}{u_0}
 \prod_{k=0}^{n-1}\frac{g_q(\widetilde y_k)}{g_q(y_k)}
 \ge\frac{\widetilde u_0}{u_0}>1.
\]
The critical asymptotic would instead give \(\widetilde u_n/u_n\sim y_n/\widetilde y_n\le1\), a contradiction. Thus there is exactly one critical \(u_*\). By coordinatewise ordering, \(B\) is downward closed and \(E\) upward closed, proving the claimed three-way classification.

**4. Strict threshold bounds.** At the critical initial state, the Riemann-sum comparison with \(Y=\infty,v=0\) gives \(qI(y_0)\le u_*\le qI(y_0)+q u_*f(y_0)\). Both inequalities are strict because all steps are positive and \(f\) strictly decreases; rearrangement yields the displayed bounds. Letting \(q\downarrow0\) proves \(u_*/q\to I(y_0)\).

**5. Rates on both sides.** If \(Y<\infty\), put \(r=g_q(Y)\in(0,1)\). Then \(u_{n+1}/u_n\to r\), and for sufficiently large \(n\), \(u_n\le C\rho^n\) for some \(\rho<1\). Hence \(\sum_n|Y-y_n|<\infty\). The convergence of \(\sum_n[\log g_q(y_n)-\log r]\) yields \(u_n=A r^n(1+o(1))\) with \(A>0\), and \(Y-y_n\sim A r^n/(1-r)\).

If \(v>0\), then \(Y=\infty\) and the integral bound yields \(u_n-v=q/y_n+O(y_n^{-2})\). Cesàro averaging first gives \(y_n/n\to v\); summation then yields \(y_n=vn+(q/v)\log n+o(\log n)\). Substitution back into the estimate gives \(u_n-v=q/(vn)+O((\log n)/n^2)\). The latter remainder is summable, so \(y_n-vn-(q/v)\log n\to C\in\mathbb R\).

**6. Exact endpoint curve and squared-height correction.** At \(q=1\), the variable \(V_n=y_nu_n\) obeys the exact identity
\[
 V_{n+1}-1=(V_n-1)\left(1+\frac{V_n}{1+y_n^2}\right).
\]
Thus \(V=1\) is an invariant curve. On it, \(u_n=1/y_n\), \(y_n\to\infty\), and \(u_n\to0\). Uniqueness of the critical orbit identifies \(u_*=1/y_0\), or \(cx_*y_0=1\). With \(w_n=y_n^2\), the exact recurrence is
\[
 w_{n+1}=w_n+2+\frac1{w_n}.
\]
Consequently \(w_n=2n+O(\log n)\) and, for all large \(n\), \(1/w_n-1/(2n)=O((\log n)/n^2)\). This difference is summable; comparing with harmonic sums proves \(w_n-2n-\tfrac12\log n\to C(y_0)\).

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. It checks 48 exact rational one-step identities, rational capture and escape certificates, invariance of the endpoint critical curve at six initial configurations, and a finite squared-height logarithmic scaling diagnostic. The assertions passed in the package preparation environment. These finite calculations check implementation and algebra; they do not replace Steps 1–6, which prove the quantified infinite-time claims.

## Relationship to prior work

Zhang, Liu, Wei, Jiang and Bi introduced the full two-dimensional rational map and identified its fixed-line parameter case, its linear multipliers, and numerically observed basins of fixed points, chaotic motion and unbounded trajectories. Their relevant complete online article (model, Case I, figures and conclusion) does not state this positive-sector sharp separator, its exact \(q=1\) equation, or its three asymptotic laws. The contribution here is the global basin threshold and critical/ballistic growth classification in a rigorously specified monotone parameter regime, not a claim of new chaotic dynamics. Generic monotone-map observations or local fixed-line eigenvalues alone do not imply the unique separating orbit and asymptotic coefficients. Equivalence through second-order damping recurrences remains a literature priority risk.

## Limitations

The theorem does not cover \(y_0\le0\), \(x_0\le0\), positive forcing \(b,d\), \(q>1\), or the chaotic parameter examples of the source paper. It does not give a closed expression for the critical threshold when \(0<q<1\); only uniqueness, computable rigorous enclosure and its small-\(q\) limit are proved. Equivalent earlier analyses of second-order damping recurrences have not been exhaustively excluded.

## References

1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang and Q.-S. Bi, “A class of two-dimensional rational maps with self-excited and hidden attractors,” *Chinese Physics B* **31** (2022), 030503. DOI: https://doi.org/10.1088/1674-1056/ac4025. Publisher full text: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml.
