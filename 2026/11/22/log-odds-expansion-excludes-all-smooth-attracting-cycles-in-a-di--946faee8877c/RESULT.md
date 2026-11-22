# Log-odds expansion excludes all smooth attracting cycles in a discontinuous quadratic population map

## Finding
For the two-discontinuity quadratic population map of Abdurakhimova and Rozikov, **every nonconstant interior periodic orbit which avoids both discontinuity thresholds is hyperbolically repelling, for every allowed triple of parameters and for every prime period**. More precisely, for any such cycle \(x_0,\ldots,x_{n-1}\) with \(x_n=x_0\),
\[
(f_{a,b,c}^{\,n})'(x_0)=\prod_{j=0}^{n-1}\left(1+\frac{(x_{j+1}-x_j)^2}{x_{j+1}(1-x_{j+1})}\right)>1.
\]
In particular, the multiplier has the parameter-free quantitative lower bound
\[
(f_{a,b,c}^{\,n})'(x_0)\ge 1+4\sum_{j=0}^{n-1}(x_{j+1}-x_j)^2>1.
\]
The strictly positive factor is an exact log-odds expansion, not an assertion that all ordinary one-step derivatives exceed one.

## Assumptions and scope
The map is defined on \([0,1]\) by \(f_{a,b,c}(x)=x+(2p(x)-1)x(1-x)\), where \(a,b,c\in[0,1]\) and
\[
p(x)=\begin{cases}
a,&0\le x\le 1/3,\\
b,&1/3<x<2/3,\\
c,&2/3\le x\le1.
\end{cases}
\]
All assertions about differentiability concern cycles contained in \((0,1)\setminus\{1/3,2/3\}\). A *nonconstant cycle* is a periodic orbit with at least two distinct points. The parameters may equal zero, one, or one half. The theorem makes no ordinary derivative claim at either discontinuity or at the endpoints.

## Proof
Fix one smooth branch, and put \(s=2p(x)-1\in[-1,1]\), \(y=f_{a,b,c}(x)\). Then \(y=x+sx(1-x)\). Since \(x^2\le y\le 2x-x^2\) for \(0<x<1\), the image lies in \((0,1)\). On the branch, \(f'(x)=1+s(1-2x)\). Expanding the product \(y(1-y)\) gives the exact algebraic identity
\[
 x(1-x)f'(x)=y(1-y)+(y-x)^2.
\]
For the increasing log-odds diffeomorphism \(h(x)=\log(x/(1-x))\), \(h'(x)=1/[x(1-x)]\). Thus the derivative of the conjugated branch \(h\circ f\circ h^{-1}\), evaluated at \(h(x)\), is
\[
\frac{x(1-x)f'(x)}{y(1-y)}=1+\frac{(y-x)^2}{y(1-y)}\ge1,
\]
with equality if and only if \(y=x\). Because a cycle avoiding both thresholds stays inside smooth branches, the chain rule applies to every step. The derivatives of \(h\) and \(h^{-1}\) cancel over one complete cycle since \(x_n=x_0\), yielding exactly the multiplier product stated above. If every factor were one, every step would be stationary, contradicting nonconstancy; hence the product is strictly greater than one.

For the lower bound, \(0<x_{j+1}(1-x_{j+1})\le1/4\), so each factor is at least \(1+4(x_{j+1}-x_j)^2\). The elementary inequality \(\prod_j(1+u_j)\ge1+\sum_j u_j\) for \(u_j\ge0\) completes the proof. Hyperbolic repulsion follows from the one-dimensional derivative criterion. No finite computational sample is used to infer the infinite-period assertion.

## Verification
An exact rational two-cycle is obtained by setting \(a=15/16\), \(b=211/1122\), \(c=1/2\): \(x_0=1/5\) lies in the first branch and \(x_1=17/50\) lies in the middle branch, with \(f(x_0)=x_1\) and \(f(x_1)=x_0\). Its two-step derivative is precisely \(27389/22440>1\), matching the product formula. Exact-rational verification of the critical polynomial identity and the example is provided in `CHECK.py`.

The distinction from naive pointwise expansion is substantive: with \(c=1\), the ordinary derivative on the right branch at \(x=3/4\) is only \(1/2\), although every smooth nontrivial cycle remains repelling in the metric sense proved here.

## Relationship to prior work
Abdurakhimova and Rozikov, *Dynamical system of a quadratic stochastic operator with two discontinuity points* (2021 preprint; 2022 journal article), define this three-parameter map and prove existence of two-cycles in their Theorem 5, together with several parameter-dependent convergence assertions. Their 2021 preprint does not state an all-period cycle multiplier formula or this hyperbolic-repulsion theorem.

Rozikov and Usmonov, *Dynamics of a Population with Two Equal Dominated Species* (2019 preprint; 2020 article), establish repulsion of every periodic orbit for a **different one-discontinuity** quadratic population map. Their argument relies on ordinary derivatives greater than one on both half-interval branches. That hypothesis fails in the present two-discontinuity family (as the example above shows). The general log-odds identity here extends the stability obstruction to this different family without claiming that the earlier one-discontinuity theorem was new.

## Limitations
The claim does not cover a periodic orbit containing \(1/3\) or \(2/3\), for which a differentiable return may fail to exist, nor does it claim that endpoints \(0,1\) are repelling; these fixed points can be attracting. The result neither proves existence of cycles of every prime period nor classifies all invariant sets, global basins, or chaotic behavior. It does not exclude attracting invariant sets which are nonperiodic or discontinuity-supported. A broader pre-existing all-partition log-odds theorem not located by the literature comparison remains an originality risk; no independent audit has been performed.

## References
1. Sh. B. Abdurakhimova and U. A. Rozikov, *Dynamical system of a quadratic stochastic operator with two discontinuity points*, arXiv:2103.14834v1 (public March 27, 2021), https://arxiv.org/abs/2103.14834 ; journal version *Mathematical Notes* 111 (2022), 676–687, https://doi.org/10.1134/S0001434622050029 .
2. U. A. Rozikov and J. B. Usmonov, *Dynamics of a population with two equal dominated species*, arXiv:1909.07106 (2019); *Qualitative Theory of Dynamical Systems* 19, article 62 (2020), https://doi.org/10.1007/s12346-020-00399-w .
