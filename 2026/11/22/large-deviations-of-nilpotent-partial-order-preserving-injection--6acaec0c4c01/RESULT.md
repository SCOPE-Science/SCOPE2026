# Large deviations of nilpotent partial-order-preserving injection ranks

## Finding
Let \(\mathcal I_n^{\uparrow}\) denote the inverse monoid of all order-preserving partial injections on \([n]=\{1,\ldots,n\}\). Choose uniformly among its nilpotent elements, including the empty map, and let \(R_n\) be the domain cardinality (equivalently, image cardinality). Then \(R_n/n\) satisfies a full large-deviation principle on \([0,1]\), with speed \(n\) and explicit good rate function
\[
I(s)=2\bigl(\log 2+s\log s+(1-s)\log(1-s)\bigr),\qquad 0\le s\le1,
\]
where \(0\log0=0\). Moreover,
\[
\frac{R_n-n/2}{\sqrt{n/8}}\ \Longrightarrow\ \mathcal N(0,1).
\]
The rate function has its unique zero at \(s=1/2\), so the typical rank is asymptotically half of the ground-set size; the Gaussian variance is \(n/8\) at leading order. The exact rank-count generating function below is a proof tool, not claimed as historically new.

## Assumptions and scope
Every \(n\ge0\) is allowed; asymptotics refer to \(n\to\infty\). A partial injection \(\alpha:D\to I\) is order-preserving if its elements satisfy \(d_1<\cdots<d_k\) and \(\alpha(d_j)=i_j\) with \(i_1<\cdots<i_k\). It is nilpotent if some positive composition power equals the nowhere-defined map. The finite monoid includes that map and its identity.

## Proof
**Fixed-point criterion.** In a finite partial injection, a nonnilpotent element has a directed cycle. Because \(\alpha\) is strictly order-preserving, a directed cycle of length greater than one is impossible: iterating its minimum would generate a strictly increasing cycle. Thus nilpotence is equivalent to the absence of fixed points \(d_j=i_j\).

**Count by domain rank.** Write \(a_{n,k}\) for the number of nilpotents of rank \(k\), \(P_n(y)=\sum_ka_{n,k}y^k\), and \(F_n(y)=\sum_{k=0}^n\binom nk^2y^k\). Each ordered pair of equally sized subsets determines one increasing partial injection, so \(F_n\) enumerates all maps. Simultaneous binary indicator words for the two subsets mark a fixed point precisely when both indicators equal one and their cumulative counts before that site agree. Inclusion-exclusion over these marked diagonal sites splits the pair into consecutive balanced segments. A marked site contributes \(xy\), while each balanced segment has generating series
\[
F(x,y)=\sum_{n\ge0}F_n(y)x^n=\bigl(1-2(1+y)x+(1-y)^2x^2\bigr)^{-1/2}.
\]
This standard diagonal-binomial identity follows, for instance, by extracting the constant term of \((1-x(1+\sqrt y z)(1+\sqrt y/z))^{-1}\). Therefore the *nilpotent* enumerator, obtained by summing signed marked-site decompositions, is
\[
G(x,y)=\sum_{n\ge0}P_n(y)x^n=\frac{F(x,y)}{1+xyF(x,y)}
=\frac{1}{xy+\sqrt{1-2(1+y)x+(1-y)^2x^2}}.
\]
In particular \(P_0=1\) and, for \(n\ge1\),
\[
P_n(y)=F_n(y)-y\sum_{j=0}^{n-1}F_{n-1-j}(y)P_j(y).
\]

**Uniform singular asymptotic.** For real \(y>0\), put \(\rho(y)=(1+\sqrt y)^{-2}\). The square root has a simple branch point at \(x=\rho(y)\). There is no positive denominator zero before this branch point, so by nonnegative coefficients and analytic continuation this is the dominant singularity. In a complex neighborhood of each positive \(y\), its local expansion is
\[
G(x,y)=\frac1{\rho(y)y}-\frac{2y^{1/4}}{(1+\sqrt y)\rho(y)^2y^2}\sqrt{1-x/\rho(y)}+O(1-x/\rho(y)).
\]
Singularity transfer gives, uniformly for \(y\) in compact neighborhoods of any fixed positive number,
\[
P_n(y)\sim C(y)n^{-3/2}\rho(y)^{-n},\qquad
C(y)=\frac{y^{1/4}}{\sqrt\pi(1+\sqrt y)\rho(y)^2y^2}>0.
\]
In particular \(P_n(1)\sim 8\cdot4^n/(\sqrt\pi n^{3/2})\). By normalization, for every real \(t\),
\[
\Lambda(t):=\lim_{n\to\infty}\frac1n\log \mathbb E(e^{tR_n})
=2\log\frac{1+e^{t/2}}2.
\]
This limit is finite and continuously differentiable on all of \(\mathbb R\). Since \(0\le R_n/n\le1\), exponential tightness is automatic. The Gärtner–Ellis theorem yields the large-deviation upper bound for closed subsets and the lower bound for open subsets of \((0,1)\); approximating endpoint points by interior points gives the full lower bound on \([0,1]\). Its Legendre transform, obtained by solving \(\Lambda'(t)=s\), is precisely \(I(s)\) above. Finally, expanding \(\Lambda(t)\) near zero shows \(\Lambda'(0)=1/2\), \(\Lambda''(0)=1/8\); the uniform analytic singularity expansion under \(y=e^{t/\sqrt n}\) gives the stated central-limit theorem via convergence of moment-generating functions.

## Verification
`CHECK.py` independently enumerates all pairs of increasing domain/image subsets of equal size for each \(0\le n\le10\), checks their no-fixed-point counts against the exact polynomial recurrence, and verifies the resulting scalar totals. All eleven cases passed. These finite checks support, but do not replace, the singularity analysis and probability limit arguments.

## Relationship to prior work
Garba established foundational nilpotence theory for the same planar rook semigroup. Laradji and Umar (2015) explicitly enumerate classes distinguished by height, waist and fixed points, and provide generating functions for nilpotents; their finite enumerative contribution is not claimed here. The unrefined nilpotent total is the previously tabulated sequence A081696. The narrowly assessed claim here is instead the **full rank large-deviation rate and Gaussian conditional-rank law**, neither of which is asserted in the accessible descriptions of the most directly relevant references. The 2015 full paper could not be compared line by line, so historical priority for the limit law remains uncertain. Work on partial chain *isometries*, partial *contractions*, and noninjective partial transformations concerns semigroups with different sampling laws and does not directly imply the stated rate function.

## Limitations
No claim of a new finite rank generating function, total count, or unconditional nilpotence probability is made. The conclusion is for uniform sampling *conditioned on nilpotence*, not for uniformly random elements of the full monoid. The asymptotic normality and large-deviation rate concern the domain/image rank, not the least exponent of nilpotence. The closest 2015 paper is accessible in abstract only; its possible prior treatment of conditional-rank asymptotics is a material residual priority risk. The proof is not an independent external audit.

## References
1. G. U. Garba, *Nilpotents in semigroups of partial one-one order-preserving mappings*, Semigroup Forum 48 (1994), 37–49, https://doi.org/10.1007/BF02573652.
2. A. Laradji and A. Umar, *Combinatorial results for semigroups of order-preserving or order-reversing subpermutations*, J. Difference Equ. Appl. 21 (2015), 269–283, https://doi.org/10.1080/10236198.2015.1005080.
3. R. Kehinde and A. Umar, *On the semigroup of partial isometries of a finite chain*, arXiv:1101.0049, first submitted 2010-12-30, https://arxiv.org/abs/1101.0049.
4. OEIS A081696, scalar nilpotent counts for order-preserving partial injections, https://oeis.org/A081696.
5. G. U. Garba, *Nilpotents in semigroups of partial order-preserving transformations*, Proc. Edinburgh Math. Soc. 37 (1994), 361–377, https://doi.org/10.1017/S001309150001885X.
