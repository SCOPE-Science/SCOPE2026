# Kemeny-optimal walks on gear graphs: a four-spoke saturation threshold and a square-root baseline gap

## Finding

Let \(G_n\) be the gear graph with \(n\ge3\) rim vertices, a central hub, and one degree-two vertex inserted in each of the \(n\) original rim edges. Thus \(G_n\) has \(2n+1\) vertices and \(3n\) edges. Among **all** irreducible, symmetric, nonnegative, stochastic transition matrices \(P\) supported on the edges and diagonal of \(G_n\), the spectral Kemeny objective
\[
\mathcal K(P)=\sum_{j=2}^{2n+1}\frac{1}{1-\lambda_j(P)}
\]
has a unique global minimizer. Let \(x_n\) denote the common probability on each hub-to-rim spoke, and \(y_n\) the common probability on each rim-to-inserted-vertex edge. The complete solution is
\[
 y_n=\frac{1-x_n}{2},\qquad
 x_n=\begin{cases}
 \xi,&n=3,\\[2pt]
 1/n,&n\ge4,
 \end{cases}
\]
where \(\xi\in(0,1/3)\) is the **unique** root in that interval of
\[
9\xi^4-40\xi^3-16\xi^2-4\xi+3=0,
\qquad \xi\approx0.270681307640681.
\]
Consequently the hub has positive holding probability only at \(n=3\), every uninserted rim vertex has zero holding probability, and every inserted vertex has positive holding probability. For \(n\ge4\), the hub and original rim vertices have zero holding, while each inserted vertex holds with probability precisely \(1/n\).

For \(n\ge4\), the unique optimal value admits the exact closed form
\[
\mathcal K_n^*=
\frac{n(3n-1)}{(2n+1)(n-1)}+
\frac{n(2n-1)}{n-1}\left[
\sqrt n\,\coth\left(n\operatorname{arsinh}\frac1{\sqrt{n-1}}\right)-1\right].
\]
It has the sharp expansion
\[
\mathcal K_n^*=2n^{3/2}-2n+\sqrt n+\frac12+O(n^{-1/2}).
\]
For the maximum-degree symmetric walk \(P^{\mathrm{md}}\), each of the \(3n\) graph edges instead carries probability \(1/n\); its Kemeny sum satisfies
\[
\mathcal K(P^{\mathrm{md}}_n)\sim\frac{5}{2\sqrt3}n^2,
\qquad
\frac{\mathcal K(P^{\mathrm{md}}_n)}{\mathcal K_n^*}\sim\frac{5}{4\sqrt3}\sqrt n.
\]
In particular, the relative improvement grows unboundedly with the number of rim vertices.

## Assumptions and scope

All parameters are real, all edge transition weights are nonnegative and symmetric, and any remaining probability is assigned to vertex self-loops. The graph is the usual gear graph (also called a bipartite wheel or a \(J_{2,n}\) Jahangir graph); no edges directly join consecutive uninserted rim vertices. Irreducibility is required, but no aperiodicity assumption is needed. The normalization is the **nontrivial-eigenvalue spectral sum** above; conventions that add one return-time contribution shift the objective by a constant and do not change its optimizer. The asserted uniqueness permits completely unequal edge probabilities before optimization; it is not merely uniqueness within an orbit-invariant ansatz. The asymptotics concern integer \(n\to\infty\).

## Proof

**1. Unrestricted uniqueness and orbit reduction.** Write \(L=I-P\), \(N=2n+1\), and \(\Pi=\mathbf1\mathbf1^T/N\). For any irreducible feasible walk,
\[
\mathcal K(P)=\operatorname{tr}(L+\Pi)^{-1}-1.
\]
The map \(A\mapsto\operatorname{tr}(A^{-1})\) is strictly convex on positive definite symmetric matrices: for a nonzero symmetric direction \(H\), its second derivative is \(2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0\). Distinct edge-weight assignments give distinct Laplacians because their off-diagonal entries recover every weight. Disconnected assignments have infinite extended objective. Thus a global minimum exists and is unique; averaging a minimizer over the dihedral automorphism group preserves feasibility and cannot increase the objective. Uniqueness forces the minimizer to use just two edge weights, \(x\) on spokes and \(y\) on the subdivided rim, with
\[
0<x\le1/n,\qquad 0<y\le(1-x)/2.
\]
For fixed \(x\), increasing \(y\) adds a nonzero positive-semidefinite Laplacian and strictly decreases the inverse trace. Therefore every optimum satisfies \(y=(1-x)/2\).

**2. Exact spectral reduction.** Apply the cyclic Fourier transform to the original rim and inserted rim vertices. For modes \(j=1,\ldots,n-1\), set \(\theta_j=2\pi j/n\). The nontrivial \(2\times2\) Laplacian blocks are
\[
M_j=\begin{pmatrix}
x+2y&-y(1+e^{-i\theta_j})\\
-y(1+e^{i\theta_j})&2y
\end{pmatrix},
\quad
\operatorname{tr}(M_j^{-1})=
\frac{x+4y}{2xy+4y^2\sin^2(\pi j/n)}.
\]
The remaining three-dimensional invariant space (hub, constant original-rim vector, constant inserted-rim vector) has one zero eigenvalue, trace \((n+1)x+4y\), and product of its two positive eigenvalues \(2(2n+1)xy\). Thus
\[
\mathcal K_n(x,y)=
\frac{(n+1)x+4y}{2(2n+1)xy}+
\sum_{j=1}^{n-1}\frac{x+4y}{2xy+4y^2\sin^2(\pi j/n)}.
\]
After \(y=(1-x)/2\), put \(s_j=\sin^2(\pi j/n)\) and \(d_j=x+(1-x)s_j\). The strictly convex one-variable objective is
\[
F_n(x)=\frac{2}{(2n+1)x}+
\frac{n+1}{(2n+1)(1-x)}+
\sum_{j=1}^{n-1}\frac{2-x}{(1-x)d_j},
\qquad 0<x\le1/n.
\]
Every summand is finite for \(x>0\), while \(F_n(x)\to\infty\) as \(x\downarrow0\).

**3. Exact saturation threshold.** Differentiating the Fourier terms gives
\[
\frac{d}{dx}\frac{2-x}{(1-x)d_j}
=\frac{(3-x)d_j-(2-x)}{(1-x)^2d_j^2}.
\]
For \(n\ge7\), evaluate at \(x=1/n\). The mean of the \(n-1\) numbers \(d_j\) equals \((n+2)/(2n)\), because \(\sum_{j=1}^{n-1}s_j=n/2\). Let \(S_1=\sum d_j^{-1}\) and \(S_2=\sum d_j^{-2}\). Jensen and Cauchy–Schwarz yield
\[
\frac{S_1}{n-1}\ge\frac{2n}{n+2}>
\frac{3n-1}{2n-1}=\frac{3-x}{2-x},
\qquad S_2\ge\frac{S_1^2}{n-1}.
\]
The strict middle inequality follows from \(n^2-7n+2>0\) for integers \(n\ge7\). It follows that the sum of all Fourier derivatives is strictly negative at \(x=1/n\). The derivative of the radial contribution is
\[
\frac{n^2}{2n+1}
\left[\frac{n+1}{(n-1)^2}-2\right]<0
\]
for every integer \(n\ge3\). Therefore \(F_n'(1/n)<0\) for \(n\ge7\). For the remaining cases direct exact Fourier arithmetic gives
\[
F_4'(1/4)=-\frac{2176}{2025},\quad
F_5'(1/5)=-\frac{875}{121},\quad
F_6'(1/6)=-\frac{6063464}{351975}.
\]
Strict convexity implies the unique minimum lies at the upper endpoint \(x=1/n\) for every \(n\ge4\). For \(n=3\), exact simplification yields
\[
F_3(x)=\frac{6(9x^2-20x-1)}{7x(x-1)(x+3)},\quad
F_3'(x)=
-\frac{6(9x^4-40x^3-16x^2-4x+3)}
{7x^2(x-1)^2(x+3)^2}.
\]
Here \(F_3'(1/3)=81/35>0\), whereas \(F_3'(x)<0\) near zero. Strict convexity gives precisely one interior critical point and proves the stated quartic characterization.

**4. Exact optimum and sharp asymptotics.** The elementary cyclic resolvent identity, for \(a>0\), is
\[
\sum_{j=0}^{n-1}\frac1{a+\sin^2(\pi j/n)}=
\frac{n}{\sqrt{a(a+1)}}\,
\coth\!\left(n\operatorname{arsinh}\sqrt a\right).
\]
For completeness, put \(t=2\operatorname{arsinh}\sqrt a\) and use the absolutely convergent Poisson-kernel Fourier expansion
\(1/(\cosh t-\cos\theta)=
(1+2\sum_{k\ge1}e^{-kt}\cos k\theta)/\sinh t\).
Summing over the \(n\)-th roots of unity retains exactly the multiples of \(n\), giving the stated identity. Applying it with \(a=1/(n-1)\), subtracting the \(j=0\) term, and adding the radial contribution proves the closed form in the Finding. Since
\(n\operatorname{arsinh}(1/\sqrt{n-1})=\sqrt n+O(n^{-1/2})\), the \(\coth\) term equals \(1+O(e^{-c\sqrt n})\) for any fixed \(0<c<2\). Elementary expansion then gives the displayed four terms with remainder \(O(n^{-1/2})\).

For the maximum-degree walk, \(x=y=1/n\); the same Fourier decomposition gives
\[
\mathcal K(P_n^{\mathrm{md}})=
\frac{n(n+5)}{2(2n+1)}+
5n\sum_{j=1}^{n-1}\frac1{2+4\sin^2(\pi j/n)}.
\]
The Riemann-sum limit is
\(\int_0^1(2+4\sin^2\pi u)^{-1}\,du=1/(2\sqrt3)\).
This proves the baseline law and the exact asymptotic ratio.

## Verification

Run `python verify_gear.py` with NumPy and SymPy installed. The checker independently builds the \((2n+1)\times(2n+1)\) weighted Laplacian, compares direct eigenvalue sums against the Fourier expression, checks derivatives against finite differences, confirms exact symbolic endpoint derivatives for \(n=3,4,5,6\), checks the unique \(n=3\) root, replays the hyperbolic closed form and tests the asymptotic constants. The distributed checker passed **528 finite assertions**. These finite diagnostics are not relied on to prove the infinite-family inequalities; those are proved in the preceding steps.

## Relationship to prior work

Boyd, Diaconis and Xiao develop symmetric stochastic edge-probability optimization for the fastest-mixing (second-largest-eigenvalue-modulus) objective, whereas this result optimizes the full nontrivial inverse spectral trace. Boyd, Diaconis, Parrilo and Xiao explain automorphism-based reductions for mixing. Patel, Agharkar and Bullo establish convex optimization and SDP frameworks for the Kemeny objective on general fixed graphs, but do not give this gear-graph allocation or its exact size threshold. Classic tabulations of the gear graph's unweighted Kirchhoff index describe one fixed conductance assignment, not the constrained optimal symmetric walk.

A sunlet/helm has pendant leaves off the rim, whereas this gear inserts degree-two vertices *within* the alternating rim and leaves no pendant vertices. Consequently previous helm/wheel, leaf-corona and squared-cycle formulas do not imply this threshold, the \(1/n\) inserted-vertex holding law, or the stated constants merely by relabeling. The comparison is based on the inspected mathematical statements; it does not establish a global novelty guarantee.

## Limitations

The theorem is restricted to symmetric stochastic walks and a uniform stationary distribution, not arbitrary reversible walks with freely chosen stationary mass, nor all directed chains. The comparison baseline is specifically the maximum-degree symmetric walk, not an optimal second-largest-eigenvalue-modulus chain. The root at \(n=3\) is specified algebraically, not by radicals. The asymptotic statement does not give a uniform finite-size relative-error bound. Independent mathematical review has not been performed. Unindexed or inaccessible research could contain an equivalent formulation.

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689. https://doi.org/10.1137/S0036144503423264 ; open manuscript https://stanford.edu/~boyd/papers/pdf/fmmc.pdf
2. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819; first arXiv version 2007-09-06, https://arxiv.org/abs/0709.0955
3. R. Patel, P. Agharkar, F. Bullo, *Robotic Surveillance and Markov Chains with Minimal Weighted Kemeny Constant*, publicly available full manuscript, https://motion.me.ucsb.edu/pdf/2014b-pab.pdf
4. J. J. Hunter, *The Role of Kemeny's Constant in Properties of Markov Chains*, first arXiv submission 2012-08-23, https://arxiv.org/abs/1208.4716
5. E. W. Weisstein, *Gear Graph*, MathWorld, https://mathworld.wolfram.com/GearGraph.html ; *Kirchhoff Index*, https://mathworld.wolfram.com/KirchhoffIndex.html
