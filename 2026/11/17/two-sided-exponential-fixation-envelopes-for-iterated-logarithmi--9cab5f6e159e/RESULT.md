# Two-sided exponential fixation envelopes for iterated logarithmic Bernstein operators

## Finding

Let \(\mu>0\), set \(\beta=(1+\mu)^{-1}\in(0,1)\), and consider the logarithm-preserving Bernstein operators of Angeloni, Costarelli, and Darielli. Their fixed-degree long-time iterates select an endpoint interpolation law whose coefficient is an absorption probability. That coefficient is trapped *strictly* between two explicit exponential functions at every interior point, and the resulting entire limit profile has a uniform error bounded by \(\beta^2/(n+\beta)\).

For every integer \(n\ge1\), define
\[
a_n(x)=\frac{\log(1+\beta x/n)}{\log(1+\beta/n)},\quad
(P_ng)(x)=\sum_{k=0}^{n}\binom nk a_n(x)^k(1-a_n(x))^{n-k}g(k/n),\qquad x\in[0,1].
\]
For \(\gamma>0\), write \(\Phi_\gamma(x)=(1-e^{-\gamma x})/(1-e^{-\gamma})\). The limit \(h_{n,\beta}(x)=\lim_{m\to\infty}(P_n^m x)(x)\) exists uniformly and is the absorption probability at endpoint \(1\) for the associated finite binomial chain. For every \(0<x<1\),
\[
\boxed{\quad \Phi_{\beta/(1+\beta/n)}(x)<h_{n,\beta}(x)<\Phi_\beta(x).\quad}
\]
All three functions equal \(0\) at \(x=0\) and \(1\) at \(x=1\); in particular
\[
0\le\Phi_\beta(x)-h_{n,\beta}(x)\le
\frac{\beta^2}{n+\beta}\qquad (0\le x\le1).
\]
These are finite-degree inequalities, not only an asymptotic diffusion approximation.

## Assumptions and scope

All functions are real-valued and continuous on \([0,1]\). The parameters satisfy \(\mu>0\), \(0<\beta=(1+\mu)^{-1}<1\), \(n\in\mathbb N\) with \(n\ge1\), and \(m\in\mathbb N\). Define \(L_\mu(x)=\log(1+\mu+x)>0\). The original operator is
\[
\mathscr L_n f(x)=L_\mu(x)P_n(f/L_\mu)(x).
\]
Convergence for \(m\to\infty\) and \(n\to\infty\) below is in the uniform norm. Let \(I_n\) denote the endpoint projection \(I_ng=g(0)(1-h_{n,\beta})+g(1)h_{n,\beta}\); this notation emphasizes that its coefficient depends on \(n\).

## Proof

**1. Absorption and convergence.** Since \(a_n(0)=0\), \(a_n(1)=1\), and \(0<a_n(x)<1\) for \(0<x<1\), the finite-state Markov matrix \(Q_{jk}=\binom nk a_n(j/n)^k(1-a_n(j/n))^{n-k}\), \(0\le j,k\le n\), has absorbing endpoints \(0,n\). Every interior state has strictly positive probability of jumping to an endpoint in one step. If \(n\ge2\), the maximum over the finite interior states of the one-step probability of remaining interior is strictly below \(1\); for \(n=1\), all states are already endpoints. Thus the probability of remaining interior after \(m\) steps decays geometrically. A first transition from any \(x\in[0,1]\) enters this finite state space, so \(P_n^m g\to I_ng\) uniformly for every continuous \(g\). Taking \(g(x)=x\) identifies \(h_{n,\beta}\) with absorption at \(1\), and \(P_n h_{n,\beta}=h_{n,\beta}\).

**2. Exact exponential tests.** Set \(c=\beta/n>0\) and \(d=\gamma/n>0\), and put \(F_d(x)=(1-e^{-dx})/(1-e^{-d})\). The binomial generating function gives
\[
P_n(e^{-\gamma\cdot})(x)=\big(1-a_n(x)(1-e^{-d})\big)^n.
\]
Consequently
\[
P_n\Phi_\gamma(x)\ge\Phi_\gamma(x)
\quad\Longleftrightarrow\quad a_n(x)\ge F_d(x),
\]
with the reverse comparison likewise equivalent. This equivalence follows by subtracting the displayed exponential expression from \(1\) and using positivity of \(1-e^{-\gamma}\).

**3. The normalized-derivative comparison.** Both \(a_n\) and \(F_d\) increase from \(0\) to \(1\), and
\[
\frac{d}{dx}\log\frac{a_n'(x)}{F_d'(x)}
=d-\frac{c}{1+cx}.
\]
If \(d\ge c\), this derivative is nonnegative and is positive for \(x>0\), so \(a_n'(x)/F_d'(x)\) increases strictly. Because the integrals of both derivatives over \([0,1]\) equal \(1\), the increasing ratio crosses \(1\) once and hence \(a_n(x)<F_d(x)\) for \(0<x<1\). If \(d\le c/(1+c)\), the ratio decreases strictly and the same normalized-integral argument gives \(a_n(x)>F_d(x)\) for \(0<x<1\). Specifically, \(d_+=\beta/n=c\) and \(d_-=[\beta/(1+\beta/n)]/n=c/(1+c)\) satisfy these two comparisons. Therefore
\[
P_n\Phi_{\beta/(1+\beta/n)}\ge\Phi_{\beta/(1+\beta/n)},
\qquad P_n\Phi_\beta\le\Phi_\beta,
\]
with strict inequalities in the interior. Positivity of \(P_n\) permits iteration; the absorbing limit of each test function is \(h_{n,\beta}\), because its endpoint values are \(0,1\). Thus the claimed barriers follow, including strictness and boundary equalities.

**4. Uniform bound.** The function \(\Phi_\gamma\) is the distribution function on \([0,1]\) of the normalized density proportional to \(e^{-\gamma t}\). Differentiating its ratio of integrals gives
\[
\partial_\gamma\Phi_\gamma(x)=\Phi_\gamma(x)
\Big(\mathbb E_\gamma[t]-\mathbb E_\gamma[t\mid t\le x]\Big),
\]
which lies in \([0,1]\) for \(0<x\le1\): the conditional mean on \([0,x]\) does not exceed the unconditional mean, and both means lie in \([0,1]\). At \(x=0\), the derivative vanishes. Hence \(\Phi_\gamma(x)\) increases with \(\gamma\) with global Lipschitz constant at most \(1\). The gap in the comparison parameters is exactly \(\beta-\beta/(1+\beta/n)=\beta^2/(n+\beta)\). The displayed uniform bound follows.

**5. Logarithmic operator and noncommutation of limits.** The positive multiplication operator \(M_{L_\mu}\) is invertible on \(C([0,1])\), and \(\mathscr L_n=M_{L_\mu}P_nM_{1/L_\mu}\). Thus
\[
\lim_{m\to\infty}\mathscr L_n^m f(x)
=L_\mu(x)\left[\frac{f(0)}{L_\mu(0)}(1-h_{n,\beta}(x))
+\frac{f(1)}{L_\mu(1)}h_{n,\beta}(x)\right]
\]
uniformly. As \(n\to\infty\), the bound above yields uniform convergence to the same expression with \(h_{n,\beta}\) replaced by \(\Phi_\beta\); the uniform error is at most \(\|L_\mu\|_\infty\left|f(1)/L_\mu(1)-f(0)/L_\mu(0)\right|\beta^2/(n+\beta)\). Conversely, for each fixed \(m\), the known uniform approximation \(\mathscr L_n\to I\) (or the binomial law plus \(a_n\to\mathrm{id}\)) and uniform boundedness of these operators imply \(\mathscr L_n^m f\to f\), so the reverse iterated limit is \(f\). For \(f(x)=L_\mu(x)x(1-x)\), the first iterated limit is \(0\) while the reverse is \(f\ne0\).

## Verification

A standalone pure-Python checker in `verify.py` builds the exact finite-node transition matrix numerically, solves the absorption linear system using partial-pivot elimination, and checks the two exponential bounds plus the uniform gap for \(n\in\{1,2,3,5,8,12,20\}\), \(\beta\in\{0.1,0.4,0.8\}\), and multiple interior points. It also checks binomial normalization, the endpoint probabilities, the exponential-generator identity, and the signs of the derivative-ratio comparison on a grid. Run `python3 verify.py` with Python 3.10+ and no third-party modules. These are diagnostic finite calculations, not proofs of the infinitely many parameter cases.

## Relationship to prior work

Angeloni, Costarelli, and Darielli [1, equations (3)–(8), Theorem 3.1, Sections 4–7] introduce \(\mathscr L_n\), derive its Bernstein conjugacy, and establish one-step convergence, saturation and shape preservation. They do not compute fixed-degree iteration limits or two-sided exponential absorption bounds. The classical Kelisky–Rivlin iteration theorem [2] gives the endpoint limit for the *ordinary* Bernstein operator, which is not the present logarithmically deformed kernel. Work on iterates of Bernstein-type operators [3] and their diffusion limits [4] provides context but does not supply these finite-\(n\) comparison functions. The paper of Gavrea–Ivan [5] studies general iterates of positive operators without this explicit barrier. The core contribution here is the structural inequality valid for each finite \(n\), which in turn yields the quantitative uniform approximation and order-of-limits distinction.

## Limitations

The envelope need not be sharp at either finite \(n\) endpoint of the comparison, and no claim is made of the optimal constant in the uniform \(O(n^{-1})\) bound. Finite numerical tests cannot establish the theorem; its proof relies on exact inequalities. The result concerns this binomial logarithmic deformation with \(\mu>0\), not arbitrary King-type operators or multivariate analogues. Some older iteration literature is not available in full open text; the priority comparison remains qualified, and independent validation has not been performed.

## References

[1] L. Angeloni, D. Costarelli, C. Darielli, *A new class of positive linear operators preserving logarithmic functions*, arXiv:2602.06168, first submitted February 5, 2026; full text https://arxiv.org/html/2602.06168v2 .

[2] R. P. Kelisky and T. J. Rivlin, *Iterates of Bernstein polynomials*, Pacific Journal of Mathematics 21 (1967), 511–520.

[3] J. A. Adell, F. G. Badía, J. de la Cal, *On the iterates of some Bernstein-type operators*, Journal of Mathematical Analysis and Applications (1997), DOI:10.1006/jmaa.1997.5371.

[4] T. Hirano and R. Namba, *Iterates of multidimensional Bernstein-type operators and diffusion processes in population genetics*, arXiv:2310.13983 (2023).

[5] I. Gavrea and M. Ivan, *Asymptotic behaviour of the iterates of positive linear operators*, 2011, DOI:10.1155/2011/670509.
