# A balanced terminal-size contrast removes logarithmic variance in random composition trees

## Finding

In the original binary uniform weak-composition tree, let \(X_n\) and \(Y_n\) count terminal chunks of respective positive sizes one and two, starting from a root of size \(n\). Define \(D_n=2X_n-5Y_n\). For every integer \(n\ge6\),

\[
\boxed{\mathbb E D_n=0,\qquad \operatorname{Var}(D_n)=\frac{253}{105}(n+2).}
\]

In contrast, their individual variances grow superlinearly:

\[
\operatorname{Var}(X_n)\sim\frac19 n\log n,\quad
\operatorname{Var}(Y_n)\sim\frac4{225}n\log n,\quad
\operatorname{Cov}(X_n,Y_n)\sim\frac2{45}n\log n.
\]

Consequently \(\operatorname{Corr}(X_n,Y_n)\to1\), even though the counted terminal chunks have different, mutually exclusive sizes. The balanced contrast has an *exactly linear* rather than logarithmically enhanced variance. Also \(\mathbb E X_n=(n+2)/6\) and \(\mathbb E Y_n=(n+2)/15\) for \(n\ge4\).

## Assumptions and scope

Each node of positive mass \(j\ge2\) independently selects a uniformly random ordered weak binary composition \((i,j-i)\) among \(j+1\) options. If \(i=0\) or \(i=j\), that node terminates with its current mass; otherwise its two children independently follow the same splitting rule. Mass-one nodes terminate. Zero-mass children of trivial splits are not counted. \(X_n\) counts mass-one terminal nodes; \(Y_n\) counts mass-two terminal nodes. There are no further restrictions or conditioning. This is the original, not the resplitting, variant.

## Proof

Let \(G_n(s)=\mathbb E\exp(sD_n)\), and \(G(s,t)=\sum_{n\ge1}G_n(s)t^n\). A mass-one root has \(G_1(s)=e^{2s}\). A mass-two root either terminates (probability \(2/3\), contributing \(D=-5\)) or splits into two singleton children (probability \(1/3\), contributing \(D=4\)). For every \(n\ge3\), a trivial root split contributes \(D=0\), and any nontrivial split gives independent additive contrasts. Therefore, as a formal power series in \(t\),

\[
t\partial_tG+G=\frac{2t}{1-t}+G^2+2t(e^{2s}-1)+2t^2(e^{-5s}-1).
\tag{1}
\]

At \(s=0\), \(G(0,t)=t/(1-t)\). Write \(M(t)=\partial_sG(0,t)\) and \(H(t)=\partial_s^2G(0,t)\). Differentiating (1), with zero integration constants at \(t=0\), gives

\[
\big[t(1-t)^2M(t)\big]'=(1-t)^2(4t-10t^2),
\qquad M(t)=2t(1-t).
\tag{2}
\]

Thus \(\mathbb ED_1=2\), \(\mathbb ED_2=-2\), and \(\mathbb ED_n=0\) for every \(n\ge3\). A second derivative gives

\[
\big[t(1-t)^2H(t)\big]'=(1-t)^2(8t+50t^2)+2(1-t)^2M(t)^2
=(1-t)^2(8t+50t^2)+8t^2(1-t)^4.
\tag{3}
\]

Let \(J(t)\) be the integral from zero to \(t\) of the last polynomial. It has degree seven, \(J(0)=J'(1)=0\), and

\[
J(1)=\int_0^1\!\left[(1-u)^2(8u+50u^2)+8u^2(1-u)^4\right]du=\frac{253}{105}.
\]

Since \(H(t)=J(t)/[t(1-t)^2]\), for every \(n\ge6\) all monomials of \(J\) contribute their full coefficient tails, yielding

\[
[t^n]H(t)=(n+2)J(1)-J'(1)=\frac{253}{105}(n+2).
\]

This is the exact variance since \(\mathbb ED_n=0\). For the individual counts, put \(F(u,v,t)=\sum_{n\ge1}\mathbb E[u^{X_n}v^{Y_n}]t^n\). The same recurrence as (1), with forcing \(2t(u-1)+2t^2(v-1)\), yields first derivative generating functions

\[
\sum_{n\ge1}\mathbb EX_n t^n=\frac{t-\frac43t^2+\frac12t^3}{(1-t)^2},\qquad
\sum_{n\ge1}\mathbb EY_n t^n=\frac{\frac23t^2-t^3+\frac25t^4}{(1-t)^2}.
\tag{4}
\]

Denote their numerators by \(A(t)\) and \(B(t)\), respectively. The second factorial moment generating function of either count with numerator \(C(t)\) is

\[
\frac{1}{t(1-t)^2}\int_0^t\frac{2C(u)^2}{(1-u)^2}\,du.
\tag{5}
\]

For each displayed numerator polynomial \(C\), direct differentiation gives \(C'(1)=-C(1)\). Decomposing the integrand at its double pole at one therefore gives the logarithmic term \(-4C(1)^2\log(1-t)\). Coefficient extraction from \(-\log(1-t)/(1-t)^2\) gives \((n+1)H_n-n\), with \(H_n=\sum_{j=1}^n 1/j\). The other terms contribute polynomial-in-\(n\) corrections, and cancellation with squared means removes the quadratic terms. Hence the leading variance coefficients are \(4A(1)^2=1/9\) and \(4B(1)^2=4/225\), respectively. Finally the exact identity

\[
\operatorname{Var}(D_n)=4\operatorname{Var}(X_n)+25\operatorname{Var}(Y_n)-20\operatorname{Cov}(X_n,Y_n)
\]

yields the displayed covariance asymptotic and correlation limit. All expansions are formal-power-series identities for finite coefficients; the asymptotics follow from exact harmonic coefficients, not simulations.

## Verification

Run `python3 verify.py`. It constructs the exact joint law by rational convolution from the defining splitting rule through finite root sizes, checks normalization, means, and exact contrast variance, and separately checks the rational integral in (3). Its finite checks do not prove the all-size formula; the generating-function proof above does.

## Relationship to prior work

Sivan, Zhong, Can, Katkov, and Tsodyks (2026), Sections 1 and 5 and Appendix F, establish the underlying random composition tree, mean-size profiles and concentration of fixed-size node counts, but not this two-size covariance cancellation. Their information-content variance is a different observable. Standard additive-tree and generating-function tools motivate the calculation; the assertion here is the exact model-specific cancellation of a logarithmic fluctuation and the asymptotic perfect correlation of *distinct terminal sizes*. An earlier exact single-size mass-one variance formula is consistent with the \(n\log n\) component and is not claimed anew.

## Limitations

This theorem is specific to the binary original stopping rule; other branching factors or resplitting rules require different analysis. It gives second moments and correlation, not a joint central limit theorem. Search cannot exclude every unindexed equivalent, and no independent mathematical audit has been conducted.

## References

1. D. Sivan, W. Zhong, T. Can, M. Katkov, M. Tsodyks, *Information Theory of Random Composition Trees*, arXiv:2610.24788, first public version October 17, 2026, https://arxiv.org/abs/2610.24788.
2. P. Flajolet, R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), https://algo.inria.fr/flajolet/Publications/book.pdf (general generating-function coefficient methods; not an attribution of the model-specific result).
