# Sharp Lipschitz contraction of interval-normalized Laplace localization

## Finding

For real \(a<b\) and \(\lambda>0\), define the normalized exponential-distance averaging operator

\[
T_\lambda f(x)=\int_a^b f(y)\,P_x(dy),\qquad
P_x(dy)=\frac{e^{-\lambda|x-y|}}{Z(x)}\,dy,\qquad
Z(x)=\int_a^b e^{-\lambda|x-y|}\,dy.
\]

On real Lipschitz functions with seminorm \(\operatorname{Lip}(f)=\sup_{x\ne x'}|f(x)-f(x')|/|x-x'|\), the sharp coefficient is

\[
\boxed{\sup_{\operatorname{Lip}(f)>0}\frac{\operatorname{Lip}(T_\lambda f)}{\operatorname{Lip}(f)}
=\sup_{x\ne x'}\frac{W_1(P_x,P_{x'})}{|x-x'|}
=1-\frac{z}{e^z-1},\qquad z=\frac{\lambda(b-a)}2.}
\]

This coefficient is strictly between zero and one. For \(f(y)=y\), its maximum derivative is attained uniquely at \(x=(a+b)/2\); the sharp two-location quotient is approached by distinct locations converging to that midpoint. Moreover, the unique stationary law is \(\pi(dy)=Z(y)\,dy/\int_a^b Z(t)\,dt\), and every integer \(k\ge0\) satisfies

\[
\|T_\lambda^k f-\pi(f)\|_\infty\le (b-a)\left(1-\frac{z}{e^z-1}\right)^k\operatorname{Lip}(f).
\]

## Assumptions and scope

The state space is the closed, nondegenerate real interval \([a,b]\), with its ordinary distance; the kernel rate is any finite \(\lambda>0\). Inputs \(f:[a,b]\to\mathbb R\) are Lipschitz and the output uses the same seminorm, with constants quotiented out. The \(W_1\) distance uses cost \(|y-y'|\). The invariant law and convergence claim are for the single homogeneous Markov operator \(T_\lambda\) with these fixed parameters, not an arbitrary kernel or a varying data distribution. All integrals are Lebesgue integrals.

## Proof

**1. Ordered kernel locations.** For \(x<x'\), the likelihood ratio \(p_{x'}(y)/p_x(y)\) of the strictly positive densities is nondecreasing in \(y\), since

\[
\log\frac{p_{x'}(y)}{p_x(y)}=\lambda\bigl(|y-x|-|y-x'|\bigr)+\log\frac{Z(x)}{Z(x')}
\]

is nondecreasing as a function of \(y\). A nondecreasing likelihood ratio with equal total masses implies that \(P_{x'}\) stochastically dominates \(P_x\): the density difference has at most one change of sign, from negative to positive. Consequently, with \(m(x)=\int y\,P_x(dy)\), the one-dimensional quantile coupling and the identity test function give, exactly,

\[
W_1(P_x,P_{x'})=m(x')-m(x).
\]

In particular, by the Lipschitz dual formula for \(W_1\), the operator seminorm equals \(\operatorname{Lip}(m)\): one inequality holds for every Lipschitz test function, and equality is witnessed by \(f(y)=y\).

**2. Exact derivative.** For \(x\in(a,b)\), write \(u=x-a\), \(v=b-x\), \(F(t)=1-e^{-\lambda t}\). The probabilities of the two half-intervals are

\[
A=\frac{F(u)}{F(u)+F(v)},\qquad B=\frac{F(v)}{F(u)+F(v)},\qquad A+B=1.
\]

The respective conditional means are \(x-H(u)\) and \(x+H(v)\), where the mean distance under a truncated exponential law is

\[
H(t)=\frac1\lambda-\frac{t}{e^{\lambda t}-1}\quad(t>0),\qquad H(0)=0.
\]

For almost every \(y\), differentiating the unnormalized kernel with respect to its center contributes \(-\lambda\) when \(y<x\) and \(+\lambda\) when \(y>x\). Subtracting the normalizing logarithmic derivative gives score values \(-2\lambda B\) and \(+2\lambda A\), respectively. Differentiation under the finite integral is valid by domination, and thus

\[
m'(x)=2\lambda AB\bigl(H(u)+H(v)\bigr).
\]

**3. Sharp optimization.** The arithmetic-geometric mean inequality yields \(AB\le1/4\), with equality only for \(u=v\) because \(F\) is strictly increasing. The function \(H\) is strictly concave on \((0,\infty)\). Indeed, putting \(r=\lambda t>0\),

\[
H''(t)=-\lambda\frac{e^r\bigl((r-2)e^r+r+2\bigr)}{(e^r-1)^3}<0.
\]

For \(h(r)=(r-2)e^r+r+2\), one has \(h(0)=h'(0)=0\) and \(h''(r)=re^r>0\) for \(r>0\), which proves the sign. Consequently Jensen's inequality gives \(H(u)+H(v)\le2H((b-a)/2)\), with equality only at the midpoint. Hence

\[
0\le m'(x)\le \lambda H((b-a)/2)
=1-\frac{z}{e^z-1},\qquad z=\lambda(b-a)/2.
\]

Equality occurs at the midpoint. Continuity of \(m\) on the closed interval, differentiability in the interior, and the mean-value theorem establish the global sharp coefficient. The strict inequalities \(0<q(z)<1\) follow from \(0<z<e^z-1\) for \(z>0\).

**4. Invariant distribution and quantitative mixing.** Symmetry of \(e^{-\lambda|x-y|}\) gives detailed balance for the strictly positive transition density with \(\pi(dx)\propto Z(x)\,dx\). Thus \(\pi\) is stationary; strict positivity and the contraction below imply uniqueness. Iterating the sharp one-step seminorm inequality yields \(\operatorname{Lip}(T_\lambda^k f)\le q(z)^k\operatorname{Lip}(f)\). Since \(\pi(T_\lambda^k f)=\pi(f)\), for any \(x\in[a,b]\),

\[
|T_\lambda^k f(x)-\pi(f)|
=\left|\int(T_\lambda^k f(x)-T_\lambda^k f(y))\,\pi(dy)\right|
\le(b-a)q(z)^k\operatorname{Lip}(f).
\]

The mixing bound is not claimed to be a sharp \(k\)-step coefficient for \(k\ge2\).

## Verification

The separate standalone file `checker.py` evaluates closed analytic kernel means, score-derived derivatives, independent composite-midpoint quadratures of the original kernel, finite differences, reflection symmetries and the midpoint optimizer. It passed 2,532 assertions over multiple positive interval lengths and rates; numerical experiments supplement, rather than replace, the analytic proof. Reproduce by running `python checker.py` with Python 3 and no third-party packages. Direct symbolic differentiation independently confirms the displayed formula for \(H''\).

The exact coefficient has the boundary-scale expansions \(q(z)=z/2-z^2/12+O(z^4)\) as \(z\downarrow0\), and \(q(z)=1-ze^{-z}+O(ze^{-2z})\) as \(z\to\infty\). These express strict boundary-induced contraction for every finite positive interval and rate.

## Relationship to prior work

Mémoli, Smith and Wan (2019; initial public preprint 2018) develop probability-measure localization and Wasserstein distances and study stability under perturbations of the underlying data distribution, without the exact center-to-center coefficient computed here for an interval-normalized Laplace kernel. Tosatto, Akrour and Peters (2020) analyze bias bounds for Nadaraya–Watson smoothing under Lipschitz hypotheses, primarily with Gaussian regression kernels, rather than this sharp Lipschitz operator norm. Qu, Blanchet and Glynn (2023) study computable Wasserstein contraction bounds for broader Markov chains; their general framework is not an explicit calculation for the present continuous interval kernel. Classical stochastic-order and Wasserstein duality facts are used as tools, not claimed new. The particular exact sharp constant, unique worst center and reversible stationary-law consequence are the proposed result.

## Limitations

The sharp formula is specific to a uniform base measure on one interval and to the exponential absolute-distance kernel; it does not assert the same coefficient for nonuniform design measures, Gaussian kernels, higher-dimensional convex bodies or periodic domains. The rate for individual iterates may be better than the upper bound \(q(z)^k\). Possible previously unindexed exact formulas for truncated Laplace location families or equivalent Markov-transport settings are a residual originality risk. No independent mathematical audit has been performed.

## References

1. F. Mémoli, Z. Smith and Z. Wan, *The Wasserstein Transform*, Proceedings of Machine Learning Research 97 (2019), 4496–4504. Public preprint arXiv:1810.07793, first posted 2018-10-17. https://proceedings.mlr.press/v97/memoli19a.html
2. S. Tosatto, R. Akrour and J. Peters, *An Upper Bound of the Bias of Nadaraya–Watson Kernel Regression under Lipschitz Assumptions*, arXiv:2001.10972, first posted 2020-01-29. https://arxiv.org/abs/2001.10972
3. Z. Qu, J. Blanchet and P. Glynn, *Computable Bounds on Convergence of Markov Chains in Wasserstein Distance*, arXiv:2308.10341 (2023). https://arxiv.org/abs/2308.10341
