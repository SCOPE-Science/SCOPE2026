# Sharp \(\ell_4\) stability of metric projection onto a probability simplex

## Finding

For each integer \(n\ge2\) and each \(1<p<\infty\), define the metric projection \(\Pi_{p,n}:\mathbb R^n\to\Delta_{n-1}\) by minimizing \(\|x-z\|_p\) over the standard probability simplex
\[
\Delta_{n-1}=\left\{z\in\mathbb R^n:z_i\ge0,\ \sum_{i=1}^n z_i=1\right\}.
\]
The map is independent of the exponent \(p\). Its sharp global Lipschitz constant **measured in the real \(\ell_4\) norm** is
\[
\operatorname{Lip}_4(\Pi_{p,n})^4
=\max_{2\le k\le n}\max_{1\le j<k}
\frac{j(k-j)^4+(k-j)j^4}{k^4}
\left(j^{-1/3}+(k-j)^{-1/3}\right)^3.
\]
Consequently the exact best dimension-free constant is
\[
\sup_{n\ge2}\operatorname{Lip}_4(\Pi_{p,n})
=\lim_{n\to\infty}\operatorname{Lip}_4(\Pi_{p,n})
=\left(1+\frac2{\sqrt3}\right)^{1/4}
\approx1.211565031277261.
\]
Every *finite* value is strictly smaller than this uniform limit. In dimension \(n=3\), the projection is not \(\ell_4\)-nonexpansive: its sharp constant is approximately \(1.064165862858\).

## Assumptions and scope

All coordinates and optimization variables are real. The exponent \(p\) describes the norm defining best approximation, whereas \(\operatorname{Lip}_4\) measures input and output differences in \(\ell_4\) regardless of \(p\). The statement is global on all of \(\mathbb R^n\). No assertion is made for the non-unique metric projections potentially arising when \(p=1\) or \(p=\infty\).

For each \(x\in\mathbb R^n\), there is exactly one threshold \(\tau\in\mathbb R\) satisfying \(\sum_i(x_i-\tau)_+=1\), and \(\Pi_{p,n}(x)_i=(x_i-\tau)_+\). The only external mathematical input to the sharp constant is the established symmetric-quartic half-degree principle [2].

## Proof

**1. The metric projection is independent of \(p\).** Minimize \(\frac1p\sum_i|z_i-x_i|^p\) under the simplex constraints; strict convexity ensures a unique solution. The scalar map \(g(s)=|s|^{p-2}s\) is strictly increasing on \(\mathbb R\). The stationarity and complementary-slackness conditions imply that all positive coordinates of the minimizer have the same displacement \(z_i-x_i=-\tau\), while all inactive coordinates satisfy \(x_i\le\tau\). This yields the stated positive-part formula, with its unique threshold fixed by the sum constraint. Thus \(\Pi_{p,n}=\Pi_{2,n}\) as maps, not as assertions about distances.

**2. Reduction to linear mean-centering blocks.** On any open polyhedral region with active set \(A\subseteq\{1,\ldots,n}\) of size \(k\), the threshold is \(\tau=(\sum_{i\in A}x_i-1)/k\). Consequently the Jacobian sends a perturbation \(h\) to
\[
(D\Pi_{p,n}(x)h)_i=
\begin{cases}
 h_i-\frac1k\sum_{a\in A}h_a,&i\in A,\\
 0,&i\notin A.
\end{cases}
\]
This is the direct sum of \(C_k=I_k-k^{-1}\mathbf1\mathbf1^T\) and the zero operator. Every nonempty active set occurs on a full-dimensional region (choose active input coordinates \(1/k\) and inactive input coordinates \(-2\)). The piecewise-affine map is continuous; joining arbitrary inputs by line segments (or generic approximations of boundary segments) gives the upper Lipschitz bound by the largest Jacobian norm, and local perturbations inside each open cell give the reverse bound. Since \(C_1=0\),
\[
\operatorname{Lip}_4(\Pi_{p,n})
=\max_{2\le k\le n}\|C_k\|_{\ell_4^k\to\ell_4^k}.
\]

**3. Exact centering norm for every finite size.** Fix \(k\ge2\) and write \(\bar x=k^{-1}\sum_i x_i\). For a proposed fourth-power norm bound \(R\), the homogeneous quartic polynomial
\[
F_R(x)=R\sum_{i=1}^k x_i^4-\sum_{i=1}^k(x_i-\bar x)^4
\]
is invariant under all coordinate permutations. Riener's half-degree principle [2, Theorem 1.3] says that a symmetric quartic is nonnegative on all of \(\mathbb R^k\) exactly when it is nonnegative on vectors with at most two distinct coordinate values. Constant vectors give zero numerator. If \(x\) has \(j\) entries equal to \(u\) and \(k-j\) entries equal to \(v\), then
\[
\sum_i(x_i-\bar x)^4
=\frac{j(k-j)^4+(k-j)j^4}{k^4}(u-v)^4,
\qquad
\sum_i x_i^4=ju^4+(k-j)v^4.
\]
The dual form of the two-variable Hölder inequality gives the **attained** exact scalar maximum
\[
\sup_{(u,v)\ne(0,0)}\frac{(u-v)^4}{ju^4+(k-j)v^4}
=\big(j^{-1/3}+(k-j)^{-1/3}\big)^3;
\]
one can choose \(u=j^{-1/3}\) and \(v=-(k-j)^{-1/3}\). Applying the half-degree principle to the sharpest \(R\) gives the claimed finite \(\ell_4\) centering norm. Combining this with step 2 proves the finite-dimensional Lipschitz formula for **every** integer \(n\ge2\).

**4. Dimension-free optimization and strict finite gap.** Write \(t=j/k\in(0,1)\), \(r=(t/(1-t))^{1/3}>0\), and \(q=r+r^{-1}\ge2\). The fourth-power ratio from step 3 becomes
\[
 f(r)=\frac{r^6-r^3+1}{(r^2-r+1)^3}
=\frac{q^3-3q-1}{(q-1)^3}.
\]
A direct derivative gives
\[
\frac{d}{dq}\frac{q^3-3q-1}{(q-1)^3}
=\frac{3(-q^2+2q+2)}{(q-1)^4}.
\]
The unique maximum on \(q\ge2\) occurs at \(q_*=1+\sqrt3\), with \(f_*=1+2/\sqrt3\). This establishes the universal upper bound. Conversely, split ratios \(j/k\) range over rational points of \((0,1)\) as \(k\) varies, and hence approximate the maximizing real split. The supremum is therefore attained only as the dimension increases. For either maximizing real split \(t_*\),
\[
t_*(1-t_*)=\frac{1}{q_*^3-3q_*+2}
=\frac{3-\sqrt3}{18},
\]
which is irrational; no finite rational ratio \(j/k\) can yield equality with \(f_*\). This also proves strictness for every finite \(n\).

## Verification

The standalone file `verify.py` checks, with symbolic arithmetic, the general two-level centering identity, the rational-function derivative, its algebraic critical point and optimal value, and the irrationality-relevant product. It also checks explicit equality witnesses and soft-threshold conditions in finite dimensions. Run `python verify.py` with Python 3 and SymPy; successful execution prints `VERIFY_OK`. Symbolic identities and finite diagnostics **do not replace** the all-dimensional half-degree theorem or the line-segment argument, which are spelled out in the proof.

## Relationship to prior work

Wang and Carreira-Perpiñán [1] give the soft-threshold algorithm and a KKT proof for **Euclidean** simplex projection, without computing the sharp global \(\ell_4\)-Lipschitz modulus. Riener's half-degree principle [2] gives the two-level reduction for symmetric quartics, but does not itself compute the nonlinear simplex projection modulus. Lewicki and Skrzypek [3] study relative norms of **linear** projections onto hyperplanes; their general formula may subsume the linear centering-block subproblem. Its full text was unavailable for a decisive comparison, so [3] is a remaining bibliographic risk rather than a claimed exclusion. The contribution here is the exact stability profile for the whole piecewise-affine nonlinear simplex retraction, including all possible active sizes, and its sharp dimension-free limit.

## Limitations

The theorem is restricted to real coordinates and \(\ell_4\) measurement, with best approximation defined by \(1<p<\infty\). It does not compute Lipschitz moduli in arbitrary \(\ell_q\) measurement or characterize finite-dimensional maximizing active sizes by a closed formula without the displayed finite maximum. It does not assert a new formula for minimal linear hyperplane projection constants. Broader unindexed literature and an unavailable full text of [3] remain possible overlap risks.

## References

[1] W. Wang and M. A. Carreira-Perpiñán, *Projection onto the probability simplex: An efficient algorithm with a simple proof, and an application*, arXiv:1309.1541, first publicly posted 2013-09-06, https://arxiv.org/pdf/1309.1541.

[2] C. Riener, *On the degree and half degree principle for symmetric polynomials*, arXiv:1001.4464, first publicly posted 2010-01-25, Theorem 1.3, https://arxiv.org/pdf/1001.4464.

[3] G. Lewicki and L. Skrzypek, *Minimal projections onto hyperplanes in \(\ell_p^n\)*, *Journal of Approximation Theory* 202 (2016), 42–63, DOI 10.1016/j.jat.2015.11.005. The bibliographic abstract was available, but its full article was not inspected.
