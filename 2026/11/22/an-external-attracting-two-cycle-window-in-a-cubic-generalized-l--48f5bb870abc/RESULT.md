# An external attracting two-cycle window in a cubic generalized logistic map

## Finding

Let \(f_\eta:\mathbb R\to\mathbb R\) be \(f_\eta(x)=\eta x(1-x)^2\), with \(\eta>0\). Count a primitive period-two orbit as one unordered pair of *distinct* real points \(\{x,y\}\) satisfying \(f_\eta(x)=y\) and \(f_\eta(y)=x\). The exact number of such orbits is

\[
N_2(\eta)=\begin{cases}
0,&0<\eta\le4,\\
1,&4<\eta<8,\\
2,&\eta=8,\\
3,&\eta>8.
\end{cases}
\]

For \(\eta>4\), the unique *inner* primitive two-cycle is

\[
\{x_0,y_0\}=\left\{\frac{1-\sqrt{1-4/\eta}}2,\frac{1+\sqrt{1-4/\eta}}2\right\},
\qquad (f_\eta^2)'(x_0)=9-2\eta.
\]

At \(\eta=8\), one further, neutral two-cycle appears, namely \(\{(3-\sqrt3)/4,(3+\sqrt3)/4\}\), with multiplier \(+1\). For each \(\eta>8\), put \(\delta=\sqrt{1-8/\eta}\), \(s_\pm=(3\pm\delta)/2\) and \(r_\pm=\sqrt{s_\pm(2-s_\pm)}\). The two *external* primitive cycles are

\[
\{x_\pm,y_\pm\}=\left\{\frac{s_\pm+r_\pm}{2},\frac{s_\pm-r_\pm}{2}\right\},
\quad x_\pm>1,\quad 0<y_\pm<1,
\]

with return multipliers

\[
\Lambda_\pm=9-\eta\mp3\sqrt{\eta(\eta-8)}.
\]

Consequently the **complete parameter set admitting a hyperbolically attracting real primitive two-cycle** is the union of two disjoint open windows

\[
\boxed{\quad(4,5)\;\cup\;\left(8,\frac{13+3\sqrt{41}}4\right).\quad}
\]

On the first window the inner cycle attracts locally; on the second window the external plus cycle attracts locally. For all \(\eta>8\) the external minus cycle is repelling. At \(\eta=5\) and \(\eta=(13+3\sqrt{41})/4\), the corresponding multipliers equal \(-1\), so these endpoints are not hyperbolically attracting. No claim is made about nonhyperbolic attraction at the boundary values.

## Assumptions and scope

All parameters \(\eta\) are positive real numbers, and the phase space for this census is the **whole real line**, not only the customary population interval \([0,1]\). The map preserves the sign of every nonzero argument, except that \(x=1\) maps to zero and then stays fixed. The interval \([0,1]\) is forward invariant exactly when \(0<\eta\le27/4\), because its maximum image is \(4\eta/27\). Thus the second attracting window, which requires \(\eta>8\), is external to that natural invariant interval. Its orbit alternates between \((0,1)\) and \((1,\infty)\). The assertion concerns primitive two-cycles and their local multipliers, not global basins, positive Lyapunov exponents or higher-period orbit counts.

## Proof

**1. Reduction to positive pairs.** For \(x<0\), \(f_\eta(x)<0\) and \(f'_\eta(x)=\eta(1-x)(1-3x)>0\). A strictly increasing self-map of the negative half-line cannot admit a pair of distinct points that swap: if \(x<y\), then \(f_\eta(x)<f_\eta(y)\), contrary to \(f_\eta(x)=y>x=f_\eta(y)\). Zero and one cannot belong to primitive two-cycles since \(f_\eta(0)=f_\eta(1)=0\). Every primitive real two-cycle therefore consists of two strictly positive points distinct from one.

**2. Exact two-case dichotomy.** For a primitive pair \(x,y>0\),

\[
\frac yx=\eta(1-x)^2,\qquad \frac xy=\eta(1-y)^2.
\]

Multiplying gives \(\eta|(1-x)(1-y)|=1\). Dividing and taking positive square roots gives \(y|1-y|=x|1-x|\). If \((1-x)(1-y)>0\), then \(x(1-x)=y(1-y)\). Because \(x\ne y\), necessarily \(x+y=1\), whence \(x,y\in(0,1)\) and \(xy=1/\eta\). The two roots of \(t^2-t+1/\eta=0\) are distinct exactly when \(\eta>4\). Conversely each such pair swaps because \(\eta xy=1\), so it is precisely the inner cycle.

If \((1-x)(1-y)<0\), reorder the points so \(x>1>y>0\). Now \(y(1-y)=x(x-1)\), equivalent to \(x^2+y^2=x+y\). With \(s=x+y\) and \(p=xy\), obtain \(p=s(s-1)/2\) and \(\eta(s-1)(2-s)=2\). The positive-product and mixed-interval requirements force \(1<s<2\). This last quadratic equation for \(s\) has no solution for \(0<\eta<8\), the single solution \(s=3/2\) for \(\eta=8\), and the two distinct solutions \(s_\pm=(3\pm\sqrt{1-8/\eta})/2\) for \(\eta>8\). The unordered pair at each solution has roots

\[
t^2-st+\frac{s(s-1)}2=0,
\qquad t=\frac{s\pm\sqrt{s(2-s)}}2.
\]

For \(1<s<2\) these are distinct positive roots, one below and one above one: \(p>0\), and \((1-x)(1-y)=(s-1)(s-2)/2<0\). The two defining equations are sufficient for swapping: they imply \(\eta(x-1)(1-y)=1\) and \(x(x-1)=y(1-y)\); hence \(\eta x(x-1)^2=y\) and \(\eta y(1-y)^2=x\). Therefore every constructed pair is an actual primitive two-cycle, not a spurious algebraic solution. The strict signs also exclude double-counting of the inner pair. This proves the complete census including both threshold values.

**3. Exact multipliers and local stability.** For any primitive pair write \(s=x+y\), \(p=xy\). Since \(f'_\eta(t)=\eta(1-t)(1-3t)\), the common multiplier of the return map is

\[
(f_\eta^2)'(x)=f'_\eta(x)f'_\eta(y)
=\eta^2(1-s+p)(1-3s+9p).
\]

For the inner pair, \(s=1\) and \(p=1/\eta\), giving \(9-2\eta\). It lies strictly between \(-1\) and \(+1\) exactly for \(4<\eta<5\). For an external pair, substitute \(p=s(s-1)/2\), \(\eta(s-1)(2-s)=2\), and \(s=(3\pm\delta)/2\) to obtain \(\Lambda_\pm=9-\eta\mp3\sqrt{\eta(\eta-8)}\). At \(\eta=8\) both give \(+1\). If \(\eta>8\), then \(\Lambda_->1\) because \(3\sqrt{\eta(\eta-8)}>\eta-8\). Meanwhile \(\Lambda_+\) is strictly decreasing from \(+1\) at \(\eta=8\) to \(-\infty\): its derivative is \(-1-3(\eta-4)/\sqrt{\eta(\eta-8)}<0\). Solving \(\Lambda_+=-1\) with \(8<\eta<10\), then squaring the equivalent positive identity \(3\sqrt{\eta(\eta-8)}=10-\eta\), gives \(2\eta^2-13\eta-25=0\) and the unique permissible root \(\eta_*=(13+3\sqrt{41})/4\). Thus the external plus cycle is hyperbolically attracting exactly for \(8<\eta<\eta_*\). At all other nonboundary parameters each cycle is hyperbolic and its stability follows from the displayed multipliers.

**4. Algebraic cross-check of completeness.** The ninth-degree polynomial of all fixed points of the second iterate factors exactly as

\[
\begin{aligned}
f_\eta(f_\eta(t))-t={}&t\,[\eta(t-1)^2-1]\,[\eta t^2-\eta t+1]\\
&\cdot[\eta^2t^4-3\eta^2t^3+3\eta^2t^2-\eta^2t-\eta t+\eta+1].
\end{aligned}
\]

The first two factors describe fixed points, the quadratic describes the inner pair, and the quartic describes the external pairs. This identity confirms that the real-cycle dichotomy has no missing algebraic component, even at degenerate thresholds.

## Verification

Run \(`python verify.py`\) with Python 3.9+ and SymPy as specified in \(`requirements.txt`\). The symbolic checker expands the complete second-iterate factorization and verifies the inner and external multiplier reductions and threshold equation exactly, rather than inferring infinite-time claims from floating-point sampling. The hand proof above is independent of these computations. Representative parameter values below, at, and above both existence thresholds are also checked in the script. The script does **not** establish originality or provide independent mathematical review.

## Relationship to prior work

Nandi, *Bifurcation and chaotic behavior of two parameter family of generalized logistic maps* (2024), introduces the full family \(g_{\eta,n}(x)=\eta x(1-x)^n\) on the real domain and presents numerical higher-period observations for \(n=2\) in Section 4. The exact whole-real-line three-phase primitive-two-cycle census, the additional external fold at \(\eta=8\), and the second attracting window are not given in the inspected article. Franco-Medrano and Solis (2015), Section 2.2, study general cubic polynomial dynamics through canonical conjugacy and fixed-point stability; they explicitly do not provide general exact values of periodic points of period at least two. A separately indexed generalized Allee-logistic result assumes nonnegative cubic growth coefficients and so does not apply directly to \(\eta x(1-x)(1-x)\), whose second linear factor has negative slope. No assertion of worldwide priority is made.

## Limitations

The reentrant window exists for the real polynomial on \(\mathbb R\) and is **not** a physical attracting window for trajectories constrained to the usual invariant population interval. The result gives only local linear stability when the multiplier is strictly within the unit circle; it does not settle nonlinear stability at neutral thresholds, basin size, or periods beyond two. Earlier unindexed work or a more general cubic-map theorem could still imply parts of this algebraic classification. Self-review are not an independent audit.

## References

1. S. Nandi, *Bifurcation and chaotic behavior of two parameter family of generalized logistic maps*, Advances in Fixed Point Theory 14 (2024), article 20. Published 2024-05-21. DOI: https://doi.org/10.28919/afpt/8562. Primary text: https://scik.org/index.php/afpt/article/download/8562/3988.
2. F. Franco-Medrano and F. J. Solis, *Stability of Real Parametric Polynomial Discrete Dynamical Systems*, Discrete Dynamics in Nature and Society (2015), article 680970. DOI: https://doi.org/10.1155/2015/680970.
