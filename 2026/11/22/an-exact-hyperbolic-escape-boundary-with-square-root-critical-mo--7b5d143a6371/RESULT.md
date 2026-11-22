# An exact hyperbolic escape boundary with square-root critical motion in a rational plane map

## Finding

**Theorem (complete positive-quadrant trichotomy).** Consider the rational planar map introduced by Zhang, Liu, Wei, Jiang and Bi, at the natural equilibrium-line parameter boundary \(a=-1\), \(b=d=0\), and arbitrary fixed \(c>0\):
\[
F_c(x,y)=\left(\frac{xy^2}{1+y^2},\ y+cx\right).
\]
For **every** exact-real initial condition \(x_0>0\), \(y_0>0\), write \(u_n=cx_n\) and \(p_n=u_ny_n\). The **exact** curve \(cxy=1\) separates two open, radically different dynamical regimes:

1. If \(p_0<1\), then \((x_n,y_n)\to(0,Y)\) for a finite \(Y>y_0\), and the convergence is exponentially sharp. With \(q=Y^2/(1+Y^2)\in(0,1)\), there is \(K>0\) such that
\[
 u_n=Kq^n(1+o(1)),\qquad
 Y-y_n=\frac{K}{1-q}q^n(1+o(1)).
\]
2. If \(p_0=1\), the entire trajectory stays on the invariant hyperbola \(cxy=1\); its unbounded escape is *subballistic* and has an exact logarithmic correction:
\[
 y_n^2=2n+\tfrac12\log n+C_*(y_0)+O\!\left(\frac{\log n}{n}\right),
 \qquad u_n=\frac{1}{y_n} \quad (n\to\infty).
\]
In particular \(y_n/\sqrt{2n}\to1\), \(\sqrt{2n}\,cx_n\to1\).
3. If \(p_0>1\), then \(u_n\downarrow v>0\), and for some real \(C_+\),
\[
 u_n=v+\frac{1}{vn}+O\!\left(\frac{\log n}{n^2}\right),\qquad
 y_n=vn+\frac1v\log n+C_+ +O\!\left(\frac{\log n}{n}\right).
\]
In particular the initial conditions above the hyperbola escape ballistically, whereas those below it approach the line of equilibria. The three cases are exhaustive and mutually exclusive on the stated quadrant. There are no nonconstant periodic orbits in this quadrant because \(y_{n+1}>y_n\).

## Assumptions and scope

The iteration uses exact real numbers, \(c>0\), and \((x_0,y_0)\in(0,\infty)^2\). The parent four-parameter family is \(x'=x+ax/(1+y^2)+b\), \(y'=y+cx+d\); here \(a=-1\) and \(b=d=0\). The unbounded parameter \(c>0\) is removed from the normal form by the *exact* coordinate change \(u=cx\), yielding
\[
 u'=\frac{uy^2}{1+y^2},\qquad y'=y+u.
\]
No classification is asserted in the other real quadrants, for \(c=0\), or for different forcing/damping parameters. The constants \(K,Y,v,C_+,C_*\) may depend on the initial point, and all asymptotic statements concern integer time \(n\to\infty\); the rates are not claimed uniform near the separating hyperbola.

## Proof

**1. Exact monotonicity and the invariant hyperbola.** Both coordinates remain positive. The first normalized coordinate strictly decreases and the second strictly increases:
\[
0<u_{n+1}=u_n\frac{y_n^2}{1+y_n^2}<u_n,
\qquad y_{n+1}-y_n=u_n>0.
\]
Writing \(p=uy\) gives the exact polynomial-fractional identities
\[
p_{n+1}=p_n\frac{y_n^2+p_n}{1+y_n^2},\qquad
\boxed{p_{n+1}-1=(p_n-1)\left(1+\frac{p_n}{1+y_n^2}\right).}
\]
Thus the sign of \(p_n-1\) is preserved for every iterate; if \(p_0<1\) then \(p_n\) strictly decreases, and if \(p_0>1\) it strictly increases. The equality case \(p_n=1\) is invariant, with \(u_n=1/y_n\). These identities give an **exact global separating curve**, not a local linear-stability approximation.

**2. Bounded convergence below the curve.** Suppose \(0<p_0<1\). Then \(p_n\le p_0<1\). The exact increments satisfy
\[
p_n-p_{n+1}=(1-p_n)\frac{y_n}{1+y_n^2}(y_{n+1}-y_n).
\]
If \(y_n\) tended to infinity, choose \(N\) with \(y_N\ge1\). For \(n\ge N\),
\[
p_n-p_{n+1}\ge\frac{1-p_0}{2}\frac{y_{n+1}-y_n}{y_n}
\ge\frac{1-p_0}{2}\log\frac{y_{n+1}}{y_n}.
\]
Summing would force \(p_N-p_n\to\infty\), impossible because \(0<p_n\le p_N\). Therefore \(y_n\uparrow Y<\infty\) and \(u_n=y_{n+1}-y_n\to0\). Let \(q(t)=t^2/(1+t^2)\). Since \(0<q(y_n)\le q(Y)=q<1\), the recurrence implies \(u_n\le u_0q^n\) and \(Y-y_n=O(q^n)\). The function \(\log q(t)\) is Lipschitz on \([y_0,Y]\), so
\[
\sum_{n\ge0}|\log q(y_n)-\log q(Y)|<\infty.
\]
Consequently \(u_n/q^n=u_0\prod_{k<n}[q(y_k)/q]\to K\in(0,\infty)\). Summing the remaining increments of \(y\) gives \(Y-y_n\sim Kq^n/(1-q)\), establishing the first case.

**3. Exact critical orbit and its logarithmic correction.** At \(p_0=1\), invariance gives \(u_n=1/y_n\). Hence
\[
y_{n+1}=y_n+\frac1{y_n},\qquad
 y_{n+1}^2-y_n^2=2+\frac1{y_n^2}.
\]
In particular \(y_n^2\ge y_0^2+2n\), and summation gives \(y_n^2=2n+O(\log n)\). For integer \(n\ge1\), set \(w_n=y_n^2-2n-(\log n)/2\). Then
\[
w_{n+1}-w_n=\frac1{y_n^2}-\frac12\log\left(1+\frac1n\right)
=O\!\left(\frac{\log n}{n^2}\right).
\]
The increments are absolutely summable, so \(w_n\) tends to a finite constant \(C_*(y_0)\). Summing the remaining tail gives \(w_n=C_*+O((\log n)/n)\), as required. The critical orbit therefore escapes at rate \(\sqrt{2n}\) despite its transverse coordinate tending to zero.

**4. Positive terminal velocity above the curve.** Suppose \(p_0>1\). Then \(p_n\ge p_0\), and
\[
y_{n+1}^2-y_n^2=2p_n+u_n^2\ge2p_0,
\]
so \(y_n\to\infty\). Meanwhile \(u_n\downarrow v\ge0\). We show \(v>0\). Were \(v=0\), the telescoping identity for \(u\) and the relation \(y_{k+1}-y_k=u_k\) would give
\[
u_n=\sum_{k=n}^\infty\frac{y_{k+1}-y_k}{1+y_k^2}.
\]
Because \(t\mapsto(1+t^2)^{-1}\) decreases on the positive axis and \(u_k\le u_n\), its left-endpoint Riemann sum obeys
\[
\phi(y_n)\le u_n\le\phi(y_n)+\frac{u_n}{1+y_n^2},\qquad
\phi(y)=\int_y^\infty\frac{dt}{1+t^2}=\frac\pi2-\arctan y.
\]
Indeed, the overestimate on the interval \([y_k,y_{k+1}]\) is at most \(u_k[f(y_k)-f(y_{k+1})]\), and these differences telescope after replacing \(u_k\) by \(u_n\). Thus \(u_n y_n\to1\) as \(y_n\to\infty\), contradicting the strictly increasing sequence \(p_n\ge p_0>1\). Therefore \(v>0\).

**5. Ballistic and logarithmic asymptotics.** Cesàro summation of \(y_{n+1}-y_n=u_n\to v\) yields \(y_n/n\to v\). Also
\[
u_n-v=\sum_{k=n}^\infty\frac{u_k}{1+y_k^2}.
\]
Since \(u_k\to v\) and \(y_k/k\to v\), the summand is asymptotic to \(1/(vk^2)\). Consequently \(u_n-v=1/(vn)+o(1/n)\). In particular \(u_n-v=O(1/n)\), giving \(y_n=vn+O(\log n)\). Substitution back into the *exact* summand sharpens it to
\[
\frac{u_k}{1+y_k^2}=\frac1{vk^2}+O\!\left(\frac{\log k}{k^3}\right).
\]
Summation of the tails then yields \(u_n=v+1/(vn)+O((\log n)/n^2)\). Define \(z_n=y_n-vn-(\log n)/v\), for \(n\ge1\). Its increments are \(O((\log n)/n^2)\) and hence absolutely summable. Their tail is \(O((\log n)/n)\), so \(z_n\to C_+\) with the claimed error. This proves the last case and completes the trichotomy.

## Verification

The bundled standalone script `verify.py` uses Python's exact `fractions.Fraction` arithmetic to check the fundamental factor identity and coordinate updates on a finite collection of rational initial conditions, and uses floating-point diagnostics to test monotone regimes and the logarithmic critical renormalization. Run `python3 verify.py` with the standard library; the checker does not require external data or network access. Finite checks are supplementary: the proof, not numerical trajectories, establishes the exhaustive all-initial-point theorem and every asymptotic assertion.

## Relationship to prior work

Zhang, Liu, Wei, Jiang and Bi introduced the parent family and identified the line of equilibria for \(b=d=0\). Their Case I and figures discuss the fixed-line regime and numerically observed attractors, but the inspected primary article does not state the exact invariant hyperbola at \(a=-1\), a complete positive-quadrant basin separation, the subballistic logarithmic correction, or the ballistic/logarithmic scattering law. Two related mathematical records address respectively (i) **positive** feedback \(a>0\), \(d=0\), where every off-line orbit has a nonzero terminal velocity, and (ii) \(a>0\), \(d>0\), which has *no* equilibrium line and a different \(n^{2/3}\) separating law. Neither statement, nor its hypotheses, implies the present negative-feedback, zero-forcing hyperbolic boundary. The main ingredients here are the new exact product recurrence and its global consequences; standard comparison and tail-summation tools are acknowledged.

## Limitations

The result covers only exact-real positive-quadrant starts at \(a=-1\), \(b=d=0\), \(c>0\), rather than all parameter choices or the chaotic regimes of the originating study. The finite limit \(Y\), terminal velocity \(v\), and constants in the error terms are orbit dependent and not elementary closed forms. The sharp separatrix claim does not imply a neighborhood of uniform attraction for the noncompact fixed line. The accessible-source and indexed-record comparisons reduce, but cannot eliminate, priority risk from unindexed earlier equivalent work. No independent mathematical audit has been performed.

## References

1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, Q.-S. Bi, *A class of two-dimensional rational maps with self-excited and hidden attractors*, *Chinese Physics B* **31** (2022), 030503. DOI: `10.1088/1674-1056/ac4025`. [Complete accessible article](https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml). [Publisher bibliographic record with 2021-12-05 manuscript-online date](https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ac4025).
2. *Logarithmic ballistic scattering and a uniform velocity gap in a rational planar map*, published mathematical record (2026). [Scientific result](https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-logarithmic-ballistic-scattering-and-a-uniform-velocity-gap-in-a--c216a2b82ab6).
3. *Unique subballistic separatrix in a no-equilibrium rational planar map*, published mathematical record (2026). [Scientific result](https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-unique-subballistic-separatrix-in-a-no-equilibrium-rational-plan--a68c4d4e0fdd).
