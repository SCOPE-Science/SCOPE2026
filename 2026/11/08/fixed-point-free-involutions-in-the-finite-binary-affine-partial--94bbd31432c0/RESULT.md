# Fixed-point-free involutions in the finite binary affine-partial inverse monoid: a half-density law

## Finding

Let \(V_d=\mathbb F_2^d\), for every integer \(d\ge0\), and let \(\mathcal A_d\) be the inverse monoid comprising the empty partial map and every affine bijection between nonempty affine subspaces of \(V_d\). An element \(f\in\mathcal A_d\) is *self-inverse* when \(f=f^{-1}\), where the inverse is the partial-bijection inverse. Define \(\rho(f)=|\operatorname{dom}f|\) and \(\nu(f)=|\{x\in\operatorname{dom}f:f(x)=x\}|\). Let \(N_d(a,b)\) count self-inverse elements with \((\rho,\nu)=(a,b)\).

Write \({n\brack k}_2=\prod_{i=0}^{k-1}(2^{n-i}-1)/(2^{k-i}-1)\) for the Gaussian binomial coefficient, \(G_r=\prod_{i=0}^{r-1}(2^r-2^i)\) (with \(G_0=1\)), and
\[
T(k,r)={k\brack r}_2{k-r\brack r}_2G_r,\qquad A(d,k)=2^{d-k}{d\brack k}_2.
\]
The complete joint rank–fixed-point enumerator is
\[
\boxed{\sum_{a,b}N_d(a,b)X^aY^b=1+\sum_{k=0}^{d}A(d,k)X^{2^k}\sum_{r=0}^{\lfloor k/2\rfloor}T(k,r)\left[2^{k-r}-2^r+2^rY^{2^{k-r}}\right].}
\]
In particular, every nonempty self-inverse partial affine map with a \(k\)-dimensional domain has either zero fixed points or exactly \(2^{k-r}\) fixed points for some \(0\le r\le\lfloor k/2\rfloor\). Every value in this list is realized, so the nonzero fixed-point gap is sharp. For \(d=0,1,2,3,4\), the total counts of self-inverse elements (including the empty map) are \(2,5,27,297,6113\); the fixed-point-free counts are \(1,2,10,120,2656\), respectively.

There are two asymptotic results. Set \(P_s=\prod_{i=1}^{s}(1-2^{-i})\), \(P_0=1\), \(P_\infty=\prod_{i\ge1}(1-2^{-i})\), and \(F=\prod_{j\ge0}(1+2^{-j})\). Sample a self-inverse element \(F_d\) uniformly from \(\mathcal A_d\). Apart from the negligible empty-map event, write its domain as an affine subspace of dimension \(K_d\), and put \(C_d=d-K_d\). Then for each fixed \(c\ge0\),
\[
\boxed{\Pr(C_d=c)\longrightarrow\frac{2^{-c(c-1)/2}}{P_cF}.}
\]
Furthermore,
\[
\boxed{\Pr(\nu(F_d)=0)\longrightarrow\tfrac12.}
\]
The conditional fixed-point-free probabilities among self-inverse *affine permutations* of an individual \(k\)-dimensional affine space have distinct parity limits:
\[
\boxed{\lim_{j\to\infty}\Pr(\nu=0\mid k=2j)=\tfrac12-\delta,\quad
\lim_{j\to\infty}\Pr(\nu=0\mid k=2j+1)=\tfrac12+\delta,}
\]
where \(\delta=P_\infty/F=0.06056210400129026\ldots\). The domain-codimension law balances the two parities, producing the exactly one-half global limit. The total number of self-inverse partial affine maps satisfies
\[
\boxed{\#\{f\in\mathcal A_d:f=f^{-1}\}\sim \frac{F^2}{2}\,2^{(d^2+d)/2}.}
\]

## Assumptions and scope

All vector spaces and affine maps are over \(\mathbb F_2\). Affine subspaces include singleton cosets, and the monoid contains the empty map. An inverse-monoid self-inverse element means \(f=f^{-1}\), equivalently \(f^2=\operatorname{id}_{\operatorname{dom}f}\); this is not the universal categorical dagger identity \((f^{-1})^{-1}=f\) and does not mean merely \(f^2=f\). Fixed points are counted only within the domain. The ambient space has \(2^d\) elements; \(\rho\) records domain cardinality, not affine dimension. The asymptotic law concerns \(d\to\infty\) with the field fixed.

## Proof

**Step 1: reduction to one affine subspace.** If \(f^2=\operatorname{id}_{\operatorname{dom}f}\), then both its image and domain are the same affine subspace \(W\); otherwise some point would be outside the domain of its second application. Conversely, every affine involution \(W\to W\) gives such a partial map. The number of \(k\)-dimensional affine subspaces is \(A(d,k)\): choose a linear direction with \({d\brack k}_2\) possibilities, then choose one of its \(2^{d-k}\) cosets. Thus it suffices to count involutions \(x\mapsto Mx+b\) on \(\mathbb F_2^k\).

**Step 2: square-zero classification.** The equation \((Mx+b)^2=x\), interpreted as composition, is equivalent to \(M^2=I\) and \((I+M)b=0\). In characteristic two write \(M=I+N\); these conditions become \(N^2=0\) and \(Nb=0\). If \(r=\operatorname{rank}N\), then \(0\le r\le\lfloor k/2\rfloor\), since \(\operatorname{im}N\subseteq\ker N\). To count such \(N\), first choose \(U=\operatorname{im}N\), an \(r\)-space, then choose \(K=\ker N\), a \((k-r)\)-space containing \(U\), then choose the induced isomorphism \(\mathbb F_2^k/K\to U\). These choices number \({k\brack r}_2{k-r\brack r}_2G_r=T(k,r)\), with no multiplicities or omissions. Such \(N\) exists for every allowed \(r\) by taking \(r\) nilpotent Jordan blocks of length two and \(k-2r\) zero blocks.

**Step 3: fixed-point refinement.** For each \(N\), the admissible translations are exactly \(b\in\ker N\), of which there are \(2^{k-r}\). The fixed-point equation is \(Nx=b\). Exactly \(|\operatorname{im}N|=2^r\) allowed translations make it solvable, each with \(|\ker N|=2^{k-r}\) fixed points. The other \(2^{k-r}-2^r\) translations yield no fixed points. Multiply by the number \(A(d,k)\) of possible affine domains and add the empty partial map. This proves the joint polynomial and the sharp gap.

**Step 4: exact normalized weights.** Put \(s=k-2r\) and \(P_j=\prod_{i=1}^{j}(1-2^{-i})\). Using \(|\mathrm{GL}_j(2)|=2^{j^2}P_j\) and the Gaussian formula, the number of affine involutions with \(r\) rank-two Jordan blocks is
\[
T(k,r)2^{k-r}=2^{(k^2+k)/2}\,a_s\,\frac{P_k}{P_{(k-s)/2}},\quad a_s=\frac{2^{-s(s-1)/2}}{P_s}.
\]
The probability of no fixed points conditional on this \(s\) is \(1-2^{-s}\). Let \(h_k\) denote the total affine-involution count divided by \(2^{(k^2+k)/2}\). Then
\[
h_k=\sum_{\substack{0\le s\le k\\s\equiv k\pmod2}}a_s\frac{P_k}{P_{(k-s)/2}}.
\]
The factors \(P_k/P_{(k-s)/2}\le1\) tend to one for each fixed \(s\); \(a_s\) has a summable Gaussian tail. Hence dominated convergence applies separately to even and odd \(k\).

**Step 5: Euler identity and parity constants.** The elementary finite \(q\)-binomial product identity, with \(q=1/2\), gives
\[
\sum_{s\ge0}a_s u^s=\prod_{j\ge0}(1+u2^{-j})=F(u).
\]
Here \(F(1)=F\), \(F(-1)=0\), \(F(1/2)=F/2\), and \(F(-1/2)=P_\infty\). Thus each parity class has the same weight \(F/2\), proving \(h_k\to F/2\) and yielding the conditional limits \(\tfrac12\mp P_\infty/F\) by weighting the \(s\)-class with \(1-2^{-s}\).

**Step 6: partial domains and the half-density limit.** Set \(c=d-k\). The count of nonempty self-inverse partial maps with domain codimension \(c\) equals \(A(d,d-c)2^{((d-c)^2+(d-c))/2}h_{d-c}\). Rewriting with Gaussian coefficients gives exactly
\[
2^{(d^2+d)/2}\,a_c\,\frac{P_d}{P_{d-c}}\,h_{d-c}.
\]
For each fixed \(c\), the final two factors tend to \(1\) and \(F/2\). Uniformly they are bounded by \(1\) and \(F\), respectively. Since \(\sum_c a_c=F\), dominated convergence yields the stated codimension distribution and total-count asymptotic. The limiting mass of even and odd \(c\) is \(1/2\) each because \(F(-1)=0\). Conditional on fixed \(c\), the domain dimension \(k=d-c\) tends to infinity, so averaging the two parity-dependent fixed-point-free limits with equal parity masses gives \(1/2\). The single empty map is negligible compared with the count growing as \(2^{(d^2+d)/2}\).

## Verification

The companion `verify.py` is standalone Python 3 code. It enumerates all invertible binary matrices in dimensions \(0\) through \(4\), their affine translations, checks the literal composition identity \(f(f(x))=x\), and counts fixed points directly. Independently, it enumerates all affine subspaces of ambient dimensions \(0\) through \(4\) as actual subsets, compares counts to Gaussian coefficients, and reconstructs all partial-map strata. The exact observed totals and fixed-point-free totals are those displayed above; every cell agrees with the theorem. Additional exact-formula calculations in dimensions up to \(20\) check numerical convergence and Euler-product constants. Run `python3 verify.py` in the package directory; expected final output is `VERIFY_OK`. These bounded tests are corroboration, not a substitute for Steps 1–6.

## Relationship to prior work

Cockett, Comfort and Srinivasan [1] identify the category of CNOT/ancilla circuits with affine partial isomorphisms of finite binary torsors, explaining the natural inverse monoid studied here; their work establishes this categorical description, not the present joint self-inverse fixed-point distribution or limiting half-density. Fulman, Guralnick and Stanton [2, Proposition 3.1] record the established number of involutions in finite general linear groups, including the square-zero Jordan-block ingredient. Their counts concern linear groups, not affine translations, their fixed points, arbitrary partial affine domains, or the balancing of parities. The Euler product used in Steps 4–5 is classical; it is not presented as new. The exact polynomial is a joint refinement built from these ingredients, and the parity cancellation is its asymptotic consequence.

## Limitations

The theorem applies only to binary affine partial bijections; it does not count arbitrary partial permutations, non-binary fields, general CNOT circuits with domain and image of unequal size, or non-self-inverse elements. The codimension law and half-density are limits, not uniform finite-dimensional equalities. Sources consulted do not establish publication priority against every possible broader theorem on affine groups or affine inverse monoids; an unlocated equivalent enumeration remains a risk. No independent mathematical validation has been performed.

## References

[1] R. Cockett, C. Comfort and P. Srinivasan, *The Category CNOT*, arXiv:1707.02348, first posted 2017-07-05, especially Sections 3–4 and Theorem C.27. https://arxiv.org/abs/1707.02348

[2] J. Fulman, R. Guralnick and D. Stanton, *Asymptotics of the number of involutions in finite classical groups*, arXiv:1602.03611, first posted 2016-02-11, especially Proposition 3.1. https://arxiv.org/abs/1602.03611
