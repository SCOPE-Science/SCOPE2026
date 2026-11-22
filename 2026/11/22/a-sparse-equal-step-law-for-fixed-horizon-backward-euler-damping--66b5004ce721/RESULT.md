# A sparse-equal-step law for fixed-horizon backward-Euler damping

## Finding

Consider a real planar, normal, damped oscillator, integrated over a prescribed total duration by at most \(N\) backward-Euler steps. The exact global minimum squared Euclidean amplification, including every equality case and every active-step transition, is determined below. For oscillatory-to-damping ratio \(b/a>1\), minimizing numerical amplification can optimally use fewer than the available steps; all active steps nevertheless have exactly the same length. The optimal active count increases in an ordered staircase as the prescribed duration increases. If \(b/a\leq1\), every optimal schedule uses all \(N\) steps equally.

## Assumptions and scope

Let \(a>0\), \(b\geq0\), \(H>0\) and integer \(N\geq2\). Let
\[
 A=\begin{pmatrix}-a&-b\\ b&-a\end{pmatrix},\qquad r^2=a^2+b^2.
\]
For a schedule \(h_1,\ldots,h_N\geq0\) with \(\sum_{i=1}^N h_i=H\), the numerical endpoint is
\[
 u_N=\prod_{i=1}^N(I-h_i A)^{-1}u_0.
\]
Zero step lengths represent unused solve opportunities. Define the worst-initial-state squared norm multiplier
\[
 \mathcal R(h_1,\ldots,h_N)=\sup_{u_0\ne0}\frac{\|u_N\|_2^2}{\|u_0\|_2^2}.
\]
Set \(q(t)=1+2at+r^2t^2\) for \(t\geq0\). Then \(\mathcal R=\prod_iq(h_i)^{-1}\).

**Exact classification.** If \(0\leq b\leq a\), the unique minimizer is \(h_1=\cdots=h_N=H/N\), with \(\mathcal R_*=q(H/N)^{-N}\).

If \(b>a\), define \(g(t)=\log q(t)\). There exists exactly one \(\ell=\ell(a,b)>0\) satisfying
\[
 \frac{2\ell(a+r^2\ell)}{1+2a\ell+r^2\ell^2}=\log(1+2a\ell+r^2\ell^2).
\]
For every \(k=1,\ldots,N-1\), there is exactly one \(H_k\in(k\ell,(k+1)\ell)\) satisfying
\[
 q(H_k/k)^k=q(H_k/(k+1))^{k+1}.
\]
These thresholds are strictly ordered. For \(H\) strictly between successive thresholds, the unique optimal multiset consists of exactly \(k\) copies of \(H/k\) and \(N-k\) zeros, where \(k=1\) before \(H_1\) and \(k=N\) after \(H_{N-1}\). At \(H_k\), exactly the two adjacent multiplicities \(k\) and \(k+1\) are optimal. Thus
\[
 \boxed{\mathcal R_*(a,b,H,N)=\min_{1\leq k\leq N}q(H/k)^{-k}.}
\]
Equivalently, only the two integers nearest to \(H/\ell\), clamped into \(\{1,\ldots,N\}\), ever need comparison. Every optimizer is a permutation of one of these equal-on-positive-support schedules. For fixed \(a,b>a\), if the allowable number of steps grows so that \(N\geq H/\ell+o(H)\) as \(H\to\infty\), the optimal active count satisfies \(k_*/H\to1/\ell\).

## Proof

The matrix \(I-hA\) represents multiplication by \(1+(a-ib)h\) on \(\mathbb C\simeq\mathbb R^2\). Thus every backward-Euler step multiplies squared Euclidean norm by \(1/q(h)\), independently of the initial direction. The objective is therefore to maximize \(\prod_iq(h_i)\) over the compact simplex of step lengths.

**Pair replacement.** For fixed \(s=x+y\) and \(p=xy\), direct expansion gives the exact identity
\[
 q(x)q(y)=q(s)+2(a^2-b^2+ar^2s)p+r^4p^2.
\]
The product is a *strictly convex* quadratic in \(p\in[0,s^2/4]\). Its maximum occurs only at an endpoint, corresponding to either \((x,y)=(0,s)\), up to permutation, or \((x,y)=(s/2,s/2)\). Hence an optimal schedule cannot contain two unequal, strictly positive lengths: if it did, replacing those two while retaining their sum would strictly increase the objective. Consequently, **every** global optimizer consists of \(k\) equal positive steps \(H/k\) and \(N-k\) zeros for some integer \(1\leq k\leq N\). This already proves the finite candidate formula and all its equality cases, provided ties between integer candidates are treated explicitly.

**The nonoscillatory branch.** Differentiation yields
\[
 g''(t)=\frac{2\bigl(b^2-a^2-2ar^2t-r^4t^2\bigr)}{q(t)^2}.
\]
If \(b\leq a\), \(g\) is strictly concave on \([0,\infty)\) in the Jensen sense. Thus \(\sum_i g(h_i)\leq N g(H/N)\), with equality only at uniform lengths. This includes \(b=a\).

**The oscillatory branch.** Assume \(b>a\). The numerator of \(g''\) has exactly one positive root \(c\); \(g''>0\) on \((0,c)\) and \(g''<0\) on \((c,\infty)\). Define \(U(t)=tg'(t)-g(t)\), with continuous extension \(U(0)=0\). We have \(U'(t)=tg''(t)\), so \(U\) first increases strictly and then decreases strictly. As \(t\to\infty\), \(tg'(t)\to2\) while \(g(t)\to\infty\), giving \(U(t)\to-\infty\). Consequently exactly one \(\ell>c\) satisfies \(U(\ell)=0\), and \(f(t)=g(t)/t\) strictly increases on \((0,\ell)\) and strictly decreases on \((\ell,\infty)\). But \(k g(H/k)=H f(H/k)\). As the integer \(k\) increases, \(H/k\) decreases; the sequence first increases and then decreases, with its maximizing index in the two integers bracketing \(H/\ell\) (clamped to the allowed range).

For uniqueness of the staircase thresholds, put \(D_k(H)=(k+1)g(H/(k+1))-k g(H/k)\), and abbreviate \(x=H/(k+1)\), \(y=H/k\). Direct algebra gives
\[
 D_k'(H)=g'(x)-g'(y)=\frac{2(y-x)\bigl(a^2-b^2+ar^2(x+y)+r^4xy\bigr)}{q(x)q(y)}.
\]
The parenthesized factor is strictly increasing in \(H>0\), initially negative and eventually positive. Thus \(D_k\), starting from \(D_k(0)=0\), first decreases and then increases strictly. At \(H=k\ell\), candidate \(k\) is uniquely optimal and \(D_k<0\); at \(H=(k+1)\ell\), candidate \(k+1\) is uniquely optimal and \(D_k>0\). The single positive root therefore exists uniquely in \((k\ell,(k+1)\ell)\). Distinct intervals prove ordered thresholds and exclude nonadjacent ties. At every threshold both indicated active counts are globally optimal; between thresholds exactly one active count is optimal. Finally, when \(N\) grows beyond the continuum-optimal active count, the bracketing rule gives \(k_*/H\to1/\ell\), completing the proof.

## Verification

The supplementary standalone file `check.py` uses exact SymPy simplification for the pair identity, logarithmic curvature identity and derivative comparison, checks 1,500 parameter choices against 25 arbitrary simplex schedules per choice, and reproduces exact rational example values and two transition roots. Run using `python check.py` with Python, SymPy and SciPy. The accompanying `verification_output.txt` is its actual output. The quantified theorem is proved analytically above, not inferred from the finite tests.

For \(a=1\), \(b=4\), \(H=1/2\), \(N=4\), the unique optimal schedule up to permutation is \((1/4,1/4,0,0)\). It yields squared amplification \(256/1681\approx0.1522903034\), against \((64/97)^4\approx0.1895103610\) from four equal steps, a relative reduction of \(21636735/110166016\approx19.64\%\). With \(a=1\), \(b=2\), \(N=3\), numerical transition values are \(H_1\approx0.464911064067\) and \(H_2\approx0.818285116490\).

## Relationship to prior work

Gander, Halpern, Ryan and Tran, *A direct solver for time parallelization*, Theorem 1, prove unique uniform backward-Euler partition optimality for **real scalar decay** \(u'=-au\); that result directly covers the \(b=0\) case but does not imply the oscillatory sparse-support staircase. Song and collaborators (arXiv:2206.04183, first posted 2022-06-08) study controllable high-frequency dissipation of mixed-order Padé integrators with a step-size guideline; their abstract, time-step discussion and conclusions address a different integrator and do not assert an exact fixed-horizon all-allocation optimality theorem. Sun and Shu (arXiv:1912.11596, first posted 2019-12-25) obtain strong-stability improvements for explicit Runge–Kutta schemes by superviscosity, rather than fixed-budget backward-Euler step allocation. A published fixed-budget two-periodic variable-step BDF2 result optimizes a memory-bearing two-step Floquet map, not the commuting backward-Euler product with arbitrary \(N\). A related previously indexed two-step implicit-midpoint allocation uses the Cayley stability function, not backward Euler.

## Limitations

The optimized quantity is **numerical squared-norm damping**, not accuracy relative to the exact state at physical time \(H\), phase accuracy, general matrix-norm growth, or operation-count savings. Additional damping may be undesirable in a physical simulation. The result applies to the specified normal two-dimensional damped rotation; it does not automatically extend to nonnormal dynamics or multi-frequency systems. If the model instead requires all \(N\) lengths strictly positive, the same value is an unattained infimum whenever the optimal support size is less than \(N\); it is attained when all \(N\) steps are optimal. The exact algebraic threshold equations do not imply that numerical roots have rational closed forms. A historical equivalence not located in the checked literature remains possible; no independent publication-priority assessment has been performed.

## References

1. C. Song, X. Zhang, S. Eisenträger, A. Ankit, *High-order implicit time integration scheme with controllable numerical dissipation based on mixed-order Padé expansions*, arXiv:2206.04183 (first public posting 2022-06-08), https://arxiv.org/abs/2206.04183.
2. Z. Sun, C.-W. Shu, *Enforcing strong stability of explicit Runge–Kutta methods with superviscosity*, arXiv:1912.11596 (first public posting 2019-12-25), https://arxiv.org/abs/1912.11596.
3. M. J. Gander, L. Halpern, J. Ryan, T. T. B. Tran, *A direct solver for time parallelization*, section 2, Theorem 1, https://www.unige.ch/~gander/Preprints/gander_contrib.pdf.
4. W. Layton, W. Pei, C. Trenchea, *Refactorization of a variable step, unconditionally stable method of Dahlquist, Liniger and Nevanlinna*, arXiv:2108.09339 (first public posting 2021-08-20), https://arxiv.org/abs/2108.09339.
