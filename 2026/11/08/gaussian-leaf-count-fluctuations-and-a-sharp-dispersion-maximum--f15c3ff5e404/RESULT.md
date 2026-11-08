# Gaussian leaf-count fluctuations and a sharp dispersion maximum in leaf-driven preferential attachment

## Finding

For the leaf-degree preferential-attachment tree with parameter \(a>0\), let \(L_n\) be its number of degree-one vertices after \(n\) vertices have arrived. Define
\[
r(a)=\frac12-a+\sqrt{a^2+\frac14},\qquad
\kappa(a)=\left(\frac{a}{a+r(a)}\right)^2,
\qquad V(a)=\frac{r(a)(1-r(a))}{1+2\kappa(a)}.
\]
Then
\[
\frac{L_n}{n}\longrightarrow r(a)\quad\text{almost surely},\qquad
\frac{L_n-nr(a)}{\sqrt n}\ \xrightarrow{\mathrm d}\ \mathcal N(0,V(a)),\qquad
\frac{\operatorname{Var}(L_n)}n\longrightarrow V(a).
\]
Moreover, the dispersion \(V(a)\) has exactly one global maximum for \(a>0\). Writing \(u\) for the unique root in \((1/2,1)\) of
\[
6u^3-15u^2+16u-6=0,
\]
the maximizer and maximum are
\[
a_* =\frac{u(1-u)}{2u-1}=0.444733634547268\ldots,\quad
V(a_*)=\frac{u^3(1-u)}{3u^2-4u+2}=0.154824661525657\ldots.
\]
The limiting variance increases from zero as \(a\) moves away from zero, then decreases after \(a_*\) to \(1/12\) as \(a\to\infty\). The variance is exactly \(1/12\) at a unique finite \(a_c=0.104822024581779\ldots\), obtained by substituting into \(a=r(1-r)/(2r-1)\) the unique \(r\in(1/2,1)\) satisfying \(6r^3-3r^2-2=0\). Thus the variance exceeds its uniform-recursive-tree limit throughout \(a>a_c\) for finite \(a\). The dispersion maximum lies strictly within the \(0<a<1\) power-law leaf-degree regime and differs from the model's previously identified \(a=1\) structural threshold.

## Assumptions and scope

All trees are simple and labelled by arrival order. Begin with the edge joining vertices 1 and 2. At an arrival step, let \(\ell_v\) be the number of degree-one neighbors of vertex \(v\), and independently select the older endpoint \(v\) with probability proportional to \(\ell_v+a\). Attach the new vertex by an edge to the selected endpoint. The parameter \(a>0\) is fixed, not dependent on \(n\). The claim concerns the number of degree-one vertices, not the count of vertices having a specified *leaf degree*. For \(n\ge3\), this construction has \(L_3=2\) deterministically. All statements have their usual meaning on the natural probability space of this sequential growth process.

## Proof

**1. An exact scalar Markov reduction.** Every degree-one vertex in a tree of at least three vertices has no degree-one neighbor; hence its attachment weight is exactly \(a\). Each leaf contributes once to the total sum of leaf degrees \(\sum_v\ell_v=L_n\). Therefore the total attachment weight is \(an+L_n\), and the probability of attaching to a leaf is \(aL_n/(an+L_n)\). An attachment to a leaf replaces one old leaf by the new leaf, leaving the total unchanged; an attachment to a nonleaf produces one additional leaf. Consequently, for every \(n\ge3\),
\[
L_{n+1}=L_n+B_{n+1},\qquad
\mathbb P(B_{n+1}=1\mid\mathcal F_n)=F(L_n/n),\qquad F(x)=1-\frac{ax}{a+x}.
\tag{1}
\]
The map \(F\) is continuously differentiable, strictly decreasing on \([0,1]\), and has exactly one fixed point there, namely the displayed \(r=r(a)\in(1/2,1)\). Its fixed-point equation is \(r^2+(2a-1)r-a=0\).

**2. Law of large numbers and moment bounds.** Put \(e_n=L_n-nr\), \(z_n=e_n/n\), and \(\xi_{n+1}=B_{n+1}-F(L_n/n)\). Then \(\xi_{n+1}\) is conditionally mean zero and \(|\xi_{n+1}|\le1\). Subtracting the fixed-point equation from (1) gives the *exact* identity
\[
e_{n+1}=\left(1-\frac{b_n}{n}\right)e_n+\xi_{n+1},\qquad
b_n=\frac{a^2}{(a+L_n/n)(a+r)}.
\tag{2}
\]
Because \(0<L_n/n\le1\), the coefficient satisfies \(0<b_0\le b_n<1\), with \(b_0=a^2/((a+1)(a+r))\). Thus for \(n\ge3\),
\[
\mathbb E[z_{n+1}^2\mid\mathcal F_n]\le
\left(1-\frac{1+b_0}{n+1}\right)z_n^2+\frac{1}{4(n+1)^2}.
\tag{3}
\]
The nonnegative almost-supermartingale convergence lemma applied to (3) shows that \(z_n^2\) converges almost surely and that \(\sum_n z_n^2/n<\infty\); hence its limit is zero. This proves \(L_n/n\to r\) almost surely.

For later \(L^2\) control, equation (2), \(|1-b_n/n|\le1\), and the bounded noise give \(\mathbb E e_n^2=O(n)\). Expanding the fourth power of (2) conditionally, the cubic term in \(\xi\) has expectation zero when multiplied by the cube of the predictable part, and the remaining mixed terms are bounded by constants times \(\mathbb E e_n^2+\mathbb E|e_n|+1=O(n)\). Induction yields \(\mathbb E e_n^4=O(n^2)\). These bounds require no asymptotic normality assumption.

**3. Linear martingale approximation.** Set \(\kappa=b(r)=a^2/(a+r)^2\in(0,1)\). The nonlinear drift differs from its linearization by
\[
R_{n+1}=\frac{\kappa-b_n}{n}e_n,
\qquad |R_{n+1}|\le C_a\frac{e_n^2}{n^2},
\qquad \|R_{n+1}\|_2=O(n^{-1}),
\tag{4}
\]
using the fourth-moment estimate above. Define a linear comparison recursion \(\widetilde e_3=e_3\),
\[
\widetilde e_{n+1}=(1-\kappa/n)\widetilde e_n+\xi_{n+1}.
\]
The deterministic product weights
\[
w_{n,j}=\prod_{i=j}^{n-1}(1-\kappa/i),\qquad
w_{n,j}=\left(\frac jn\right)^\kappa(1+o(1))
\quad\text{when }j/n\text{ stays away from zero}
\]
satisfy \(0\le w_{n,j}\le1\). Summing the perturbations (4) with Minkowski's inequality gives \(\|e_n-\widetilde e_n\|_2=O(\log n)=o(\sqrt n)\). The initial deterministic term \(w_{n,3}e_3\) also vanishes after division by \(\sqrt n\).

The dominant term in \(\widetilde e_n\) is therefore the triangular martingale sum \(\sum_{j=4}^n w_{n,j}\xi_j\). Its conditional variance is
\[
\frac1n\sum_{j=4}^n w_{n,j}^2
 F(L_{j-1}/(j-1))\bigl[1-F(L_{j-1}/(j-1))\bigr]
\xrightarrow{\mathrm{a.s.}}
\frac{r(1-r)}{1+2\kappa},
\tag{5}
\]
by the established strong law, the weight-product asymptotics, and a Riemann-sum argument (the first \(\varepsilon n\) terms are at most \(\varepsilon\) of the normalized sum). Since \(|w_{n,j}\xi_j|\le1\), the conditional Lindeberg condition is automatic. The triangular martingale central limit theorem yields the Gaussian limit. Bounded convergence of the normalized conditional variance in (5), followed by the \(L^2\)-small approximation in (4), yields \(\mathbb E e_n^2/n\to V(a)\); the normalized means tend to zero, so \(\operatorname{Var}(L_n)/n\to V(a)\) too.

**4. Exact optimization and comparison with the uniform-tree limit.** The fixed-point identity rearranges to
\[
a=\frac{r(1-r)}{2r-1},\qquad
\frac{a}{a+r}=\frac{1-r}{r},\qquad
V(a)=v(r)=\frac{r^3(1-r)}{3r^2-4r+2}.
\]
The map \(a\mapsto r(a)\) is a decreasing bijection from \((0,\infty)\) to \((1/2,1)\). Direct polynomial differentiation gives
\[
\frac{dv}{dr}=\frac{-r^2(6r^3-15r^2+16r-6)}{(3r^2-4r+2)^2}.
\]
The cubic \(H(r)=6r^3-15r^2+16r-6\) has \(H(1/2)<0\), \(H(1)>0\), and \(H'(r)=18r^2-30r+16>0\) on the real line (its discriminant is negative). Thus the unique zero yields the unique global maximum as \(a\) increases. Finally,
\[
12v(r)-1=\frac{-(2r-1)(6r^3-3r^2-2)}{3r^2-4r+2},
\]
and the cubic \(6r^3-3r^2-2\) is strictly increasing on \((1/2,1)\), with opposite signs at the two endpoints. This proves the unique finite crossing of \(1/12\), and the endpoint limits follow by continuity in \(r\). All parameter comparisons are for fixed positive \(a\); no simultaneous \(a,n\) limit is asserted.

## Verification

The standalone `check_leafpa.py` uses exact rational arithmetic to propagate the complete labelled-tree distribution and independently the reduced leaf-count Markov recurrence. For \(a\in\{1/5,1/2,1,2,5\}\), all leaf-count distributions agree through eight vertices. It also verifies attachment-weight identities tree by tree, finite-step mass conservation, exact polynomial derivative coefficients, the unique-critical-point bracket, the fixed-point algebra, and independent numerical evaluations of the variance curve. It reports 8,919 passed finite checks. This finite enumeration is a consistency check only; the strong law, central limit theorem and optimization are proved analytically above.

To reproduce: use Python 3 (standard library only) and execute `python3 check_leafpa.py` from the directory containing this document and the script. No external dataset or random seed is required.

## Relationship to prior work

Hartle and Krapivsky, *Statistics of leaves in growing random trees* (arXiv:2511.04085; first posted November 6, 2025), introduced this precise leaf-degree-driven attachment model and calculated its first-order leaf fraction, leaf-degree distribution and the \(a=1\) tail-type transition. Their treatment of **total leaf-count variance** concerns the different, uniformly attaching random recursive tree (whose limiting variance coefficient is \(1/12\)), rather than the nonuniform leaf-driven process treated here. General one-dimensional stochastic-approximation central limit theorems, such as Renlund (arXiv:1102.4741), provide an alternative method for the Gaussian step once the exact scalar drift is recognized; they do not supply this model-specific rational variance or its unique global maximizer. The affine **ordinary-degree** preferential-attachment degree-count CLT of Baldassarri and Bet (arXiv:2102.07570) has a different attachment rule and does not directly identify this leaf-neighbor-driven process. Thus the contribution is the sharp model-specific fluctuation and dispersion phase diagram, not a new general martingale CLT method.

## Limitations

The parameter is fixed and strictly positive; no CLT is claimed at \(a=0\) or uniformly as \(a\) varies with \(n\). The variance result concerns the **number of leaves**, not higher-dimensional leaf-degree counts, their covariances, maximum degree, or tree height. Neither a local limit theorem nor a finite-size optimality statement is asserted. The finite checker does not certify an infinite theorem; historical priority of a possible unlocated broader result requires independent literature evaluation.

## References

1. H. Hartle and P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085 (first public version November 6, 2025); journal version, *Journal of Statistical Mechanics: Theory and Experiment* (2026), article 023210, DOI: 10.1088/1742-5468/ae3a6a. https://arxiv.org/abs/2511.04085
2. H. Renlund, *Limit theorems for stochastic approximation algorithms*, arXiv:1102.4741 (2011). https://arxiv.org/abs/1102.4741
3. A. Baldassarri and G. Bet, *Asymptotic normality of degree counts in a general preferential attachment model*, arXiv:2102.07570. https://arxiv.org/abs/2102.07570
