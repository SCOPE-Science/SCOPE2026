# Sharp exponential absence laws for terminal unary chains in random recursive trees

## Finding

For each fixed integer \(r\ge2\), let \(E_{n,r}\) be the event that a uniformly random recursive tree on \(n\) vertices contains **no** fringe subtree that is a rooted path on exactly \(r\) vertices (every nonterminal vertex has exactly one child). Write
\[
F_r(z)=\int_0^z\exp(-t^r/r!)\,dt,
\qquad F_r(\rho_r)=1,\quad 1<\rho_r<3/2.
\]
There is a unique such positive root \(\rho_r\). For every fixed \(r\ge2\) and every \(R\) satisfying \(\rho_r<R<3/2\),
\[
\boxed{\Pr(E_{n,r})=\rho_r^{-n}+O_{r,R}(nR^{-n}).}
\]
The leading multiplicative constant is exactly one. The rates obey \(\rho_{r+1}<\rho_r\), and
\[
\rho_r=1+\frac1{(r+1)r!}+O\big((r!)^{-2}\big)
\qquad(r\to\infty).
\]
This concerns a fixed-pattern, exponentially small **absence** probability, not the asymptotic normality of its occurrence count. In fact, the previously known fringe-mean formula gives the expected number of such chain occurrences as \(n/((r+1)r!)\) for \(n>r\), which grows linearly for every fixed \(r\). The absence probability is therefore a genuine rare-event tail.

## Assumptions and scope

A recursive tree on \(\{1,\ldots,n\}\) is a rooted tree in which the parent of each nonroot vertex has a smaller label. Its root has label \(1\), its children are unordered, and each of the \((n-1)!\) recursive trees has probability \(1/(n-1)!\). Equivalently, each new vertex independently chooses a uniformly distributed earlier parent.

The fringe subtree rooted at vertex \(v\) consists of \(v\) and all its descendants. The forbidden shape is a complete fringe subtree equal to a single unary path with \(r\) vertices. This is equivalent to demanding that no leaf have \(r-1\) consecutive one-child ancestors. It is **not** the event that the entire tree contains no path of length \(r-1\) as a graph-theoretic subpath. For \(n<r\) avoidance holds automatically. No uniform estimate in varying \(r=r(n)\) is claimed.

Let \(t_{n,r}\) count allowable recursive trees, and let
\[
T_r(z)=\sum_{n\ge1}\frac{t_{n,r}}{n!}z^n,
\qquad u_r(z)=\exp(-T_r(z)).
\]

## Proof

**1. Exact enumeration.** A recursive tree is a root with an unordered set of recursively labelled child subtrees. For allowable child trees, the root construction contributes \(\exp(T_r(z))\) to the derivative of the exponential generating function. The only root construction to exclude is the single forbidden unary chain of size \(r\), because any proper fringe subtree of that chain has size strictly less than \(r\) and remains allowable. That chain has exactly one increasing labelling. Thus
\[
T_r'(z)=\exp(T_r(z))-\frac{z^{r-1}}{(r-1)!},
\qquad T_r(0)=0.
\]
With \(u_r(z)=e^{-T_r(z)}\), this becomes the linear equation
\[
u_r'(z)=\frac{z^{r-1}}{(r-1)!}u_r(z)-1,
\qquad u_r(0)=1.
\]
Solving by an integrating factor gives
\[
\boxed{u_r(z)=\exp(z^r/r!)\left(1-\int_0^z e^{-t^r/r!}\,dt\right),\qquad T_r(z)=-\log u_r(z).}
\]
The second equality holds as formal power series around zero. Since the total number of recursive trees is \((n-1)!\), exact coefficient extraction yields
\[
\boxed{\Pr(E_{n,r})=n[z^n]T_r(z)=[z^{n-1}]\frac1{u_r(z)}-\frac{{\bf1}_{\{n=r\}}}{(r-1)!}.}
\]
The final indicator is necessary at \(n=r\).

**2. A uniform complex zero-free disk.** For real \(z\in[0,3/2]\), \(F_r'(z)>0\) and \(F_r(1)<1\). Since \(r\ge2\) and \(0\le t\le3/2\),
\[
\frac{t^r}{r!}\le\frac{t^2}{2},
\qquad F_r(3/2)\ge F_2(3/2)>1.
\]
One explicit rigorous bound is
\[
F_2(3/2)\ge\frac32-\frac{(3/2)^3}{6}+\frac{(3/2)^5}{40}-\frac{(3/2)^7}{336}>1.
\]
Hence the asserted positive root exists and is unique.

For each complex \(z\) with \(|z|<3/2\),
\[
\left|\operatorname{Im}\frac{z^r}{r!}\right|
\le\frac{(3/2)^r}{r!}\le\frac98<\frac\pi2.
\]
Therefore \(\operatorname{Re}F_r'(z)=\operatorname{Re}e^{-z^r/r!}>0\) throughout this convex disk. For any two distinct points \(z,w\) there, the integral of \(F_r'\) along their straight segment has strictly positive real part; thus
\[
\frac{F_r(z)-F_r(w)}{z-w}
=\int_0^1F_r'(w+t(z-w))\,dt\ne0.
\]
Consequently \(F_r\) is injective on \(|z|<3/2\), and \(1-F_r(z)\) has precisely one zero there, namely \(\rho_r\). Since \(u_r'(\rho_r)=-1\), this zero is simple.

**3. Dominant logarithmic singularity.** On the same disk, define
\[
g_r(z)=\frac{u_r(z)}{1-z/\rho_r},
\]
with its removable singularity filled in at \(z=\rho_r\). It is holomorphic and nowhere zero, with \(g_r(0)=1\). Since the disk is simply connected, it has an analytic logarithm \(\log g_r\) normalized by \(\log g_r(0)=0\). Therefore near zero and by analytic continuation on the slit disk,
\[
T_r(z)=-\log(1-z/\rho_r)-\log g_r(z).
\]
For \(\rho_r<R<3/2\), Cauchy's coefficient estimate gives \([z^n]\log g_r(z)=O_{r,R}(R^{-n})\). Since \([z^n]-\log(1-z/\rho_r)=\rho_r^{-n}/n\), multiplying by \(n\) proves the stated probability formula with its unit leading constant.

**4. Dependence on chain length.** For real \(0<t\le3/2\),
\[
\frac{t^{r+1}}{(r+1)!}<\frac{t^r}{r!},
\quad\text{hence}\quad F_{r+1}(t)>F_r(t).
\]
Strict monotonicity of each \(F_r\) shows \(\rho_{r+1}<\rho_r\). Moreover,
\[
1-F_r(1)=\int_0^1(1-e^{-t^r/r!})\,dt
=\frac1{(r+1)r!}+O((r!)^{-2}).
\]
As \(r\to\infty\), \(F_r(1+\varepsilon)\to1+\varepsilon\) for each fixed positive \(\varepsilon\), so \(\rho_r\downarrow1\). By the mean-value theorem and \(F_r'(z)=e^{-z^r/r!}\), initially \(\rho_r-1=O(1/(r r!))\), and then \(F_r'(\xi)=1+O(1/r!)\) uniformly between \(1\) and \(\rho_r\). This yields the displayed rate expansion.

## Verification

The standalone `verify.py` uses exact rational recurrence arithmetic and exhaustive parent-array enumeration for all recursive trees through \(n=9\), testing \(r=2,3,4,5,6\). It reports `VERIFY_OK 100 comparisons including exhaustive recursive trees through 9 vertices`.

Independently of the analytic proof, the formal recurrence
\[
u_0=1,\quad u_1=-1,\quad
u_{m+1}=\begin{cases}u_{m-r+1}/((m+1)(r-1)!),&m\ge r-1,\\0,&1\le m<r-1,\end{cases}
\]
with \(u(z)=\sum_{m\ge0}u_mz^m\) computes the exact avoidance probabilities from the reciprocal-series coefficients. Finite enumeration checks this recurrence; it does not prove the singularity or asymptotic arguments.

## Relationship to prior work

Seelbach Benkner and Wagner (first public version 2021) establish the general recursive-tree increasing-species differential equation and count distinct fringe shapes on the scale \(n/\log n\). Their Section 5.2 also counts fixed shapes among the immediate root branches, but does not state the all-vertex *absence* law or its complex-analytic error estimate. Those general constructions are used and credited, not presented as novel.

Holmgren and Janson (2014) give means, covariances and Gaussian limit theorems for counts of fixed fringe shapes in recursive trees. Feng and Mahmoud (2010) give a normal limit for fixed fringe-shape multiplicities. These results are compatible with the present theorem but do not imply its exponentially small zero-event probability: Gaussian convergence concerns centered fluctuations on a much larger probability scale. Fuchs (2008) treats subtree-size limit laws, whereas here a specified terminal path shape is forbidden.

The scoped contribution is the explicit solvable avoidance equation for every chain length together with the all-length zero-free disk, unique dominant singularity, unit constant, exponentially small remainder, and strict rate ordering. Priority beyond the inspected works is not certified; an equivalent fixed-pattern-avoidance analysis in other analytic-combinatorics literature remains possible.

## Limitations

The theorem is for uniformly random unordered recursive increasing trees only, with a fixed integer \(r\ge2\) before \(n\to\infty\). The estimate's implicit constant can depend on \(r\) and \(R\). It is not a uniform extreme-value theorem for terminal chains of length varying with \(n\), and it does not imply a full distribution for the number of forbidden fringe shapes. No independent external audit has been performed.

## References

- L. Seelbach Benkner and S. Wagner, *Distinct Fringe Subtrees in Random Trees*, first public arXiv version 2021-05-10, https://arxiv.org/abs/2105.04231 ; especially Sections 2.2 and 5.2.
- C. Holmgren and S. Janson, *Limit Laws for Functions of Fringe Trees for Binary Search Trees and Recursive Trees*, arXiv 2014, https://arxiv.org/abs/1406.6883 ; Sections 1 and 3.
- Q. Feng and H. M. Mahmoud, *On the Variety of Shapes on the Fringe of a Random Recursive Tree*, Journal of Applied Probability 47 (2010), 191–200, https://doi.org/10.1239/jap/1269610825 .
- M. Fuchs, *Subtree Sizes in Recursive Trees and Binary Search Trees: Berry–Esseen Bounds and Poisson Approximations*, Combinatorics, Probability and Computing 17 (2008), 661–680, https://doi.org/10.1017/S096354830800915X .
