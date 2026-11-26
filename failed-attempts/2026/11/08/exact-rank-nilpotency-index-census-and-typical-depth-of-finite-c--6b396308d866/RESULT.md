# Exact rank–nilpotency-index census and typical depth of finite-chain partial isometries

## Finding

Let \(D_n\) be the monoid of all injective partial maps \(f:E\longrightarrow[n]\), where \([n]=\{1,\ldots,n\}\), satisfying \(|f(x)-f(y)|=|x-y|\) for every \(x,y\in E\). The empty map is the zero. For a nilpotent \(f\in D_n\), write \(\rho(f)=|E|\) and \(\kappa(f)=\min\{k\ge1:f^k=0\}\).

For \(\ell\ge0\) and \(k\ge1\), define the polynomial
\[
A_{\ell,k}(u)=\sum_{E\subseteq[\ell]\,:\,E\text{ has no run of }k\text{ consecutive integers}}u^{|E|}.
\]
In particular \(A_{0,k}(u)=1\), and the following rational generating function determines all coefficients:
\[
\sum_{\ell\ge0}A_{\ell,k}(u)z^\ell
=\frac{\sum_{j=0}^{k-1}(uz)^j}{1-z\sum_{j=0}^{k-1}(uz)^j}.
\]
For each \(1\le d<n\), divide \(n=a_dd+b_d\), where \(a_d\ge1\) and \(0\le b_d<d\). For \(2\le c\le2n\), let
\[
m_c=\min\{c-1,2n+1-c\},\qquad p_c=\lfloor m_c/2\rfloor.
\]
**Exact joint census.** For every \(n\ge1\) and every integer \(k\ge1\), the polynomial
\[
\begin{aligned}
C_{n,\le k}(u)
={}&1+2\sum_{d=1}^{n-1}
\left(A_{a_d,k}(u)^{b_d}A_{a_d-1,k}(u)^{d-b_d}-1\right)\\
&+\mathbf1_{\{k\ge2\}}\sum_{c=2}^{2n}
\left((1+2u)^{p_c}-1-2p_cu\right)
\end{aligned}
\]
satisfies
\[
[u^r]C_{n,\le k}(u)
=\#\{f\in D_n:f\text{ nilpotent},\ \rho(f)=r,\ \kappa(f)\le k\}.
\]
Thus the difference \(C_{n,\le k}(u)-C_{n,\le k-1}(u)\), taking \(C_{n,\le0}(u)=0\), gives **every exact rank–index multiplicity**. For \(k\ge n\), \(C_{n,\le k}\) is the full nilpotent rank polynomial.

**Closed rank and total counts.** Put \(h=\lfloor n/2\rfloor\) and \(\eta_n=1\) for even \(n\), \(\eta_n=3\) for odd \(n\). With binomial coefficients outside their valid ranges equal to zero, the number of nilpotents of rank \(r\) is
\[
N_{n,r}=\begin{cases}
1,&r=0,\\
n(n-1),&r=1,\\
2\binom n{r+1}+2^r\left(4\binom h{r+1}+\eta_n\binom h r\right),&2\le r\le n.
\end{cases}
\]
Consequently the total number \(N_n\) of nilpotent elements is
\[
N_n=\begin{cases}
2^{n+1}+3^{n/2+1}-n^2-3n-4,&n\text{ even},\\
2^{n+1}+5\cdot3^{(n-1)/2}-n^2-3n-4,&n\text{ odd}.
\end{cases}
\]
In particular, the fraction of all elements of \(D_n\) that are nilpotent tends to \(1/3\), using the known full-monoid cardinality \(|D_n|=3\cdot2^{n+1}-(n+2)^2-1\).

**Typical nilpotency depth.** If \(F_n\) is chosen uniformly among the \(N_n\) nilpotent elements, then
\[
\frac{\kappa(F_n)}{\log_2 n}\xrightarrow{\mathbb P}1
\qquad(n\longrightarrow\infty).
\]
The exact joint census and typical-depth result distinguish the rank of the partial map from its nilpotency index; neither is the minimal size of a generating set of the monoid.

## Assumptions and scope

The ground set is the ordinary metric chain \([n]\), with no adjacency-only or induced-subgraph restriction. All domains, including the empty domain, are permitted. Composition is ordinary partial-map composition; a power is zero precisely when its domain is empty. The asserted formulas hold for every positive integer \(n\); there is no fixed-point or order-preserving restriction. The probability theorem concerns uniform sampling from the nilpotent subset, not from the whole monoid conditioned on a prescribed rank.

## Proof

**1. Geometric classification and duplicate control.** If \(|E|\ge2\), any isometry \(f:E\to[n]\) is the restriction of exactly one of a translation \(x\mapsto x+d\) or a reflection \(x\mapsto c-x\): the ordered images of two distinct domain points fix the sign and offset, and the distance equations fix every remaining image. The two types cannot agree on two distinct points. A rank-one nonfixed map \(x\mapsto y\) is counted as the unique nonzero translation with \(d=y-x\); a rank-one fixed map is not nilpotent. The empty map contributes exactly once. The identity translation \(d=0\) has no nonempty nilpotent restrictions. Hence the census may count all nonzero translations and only rank-at-least-two reflections, without overlap.

**2. Translations and binary runs.** Fix \(d>0\). The eligible domain consists of \(1,\ldots,n-d\); choosing any subset specifies a restriction of \(x\mapsto x+d\). Its directed partial-map graph is a disjoint union of finite directed paths, so it is nilpotent. Partition the \(n-d\) eligible starting positions into their residue classes modulo \(d\). From \(n=a_dd+b_d\) one obtains exactly \(b_d\) strings of length \(a_d\) and \(d-b_d\) strings of length \(a_d-1\). Each position is selected or omitted independently in the combinatorial enumerator. There is a chain of \(k\) selected arrows if and only if one of these strings contains \(k\) consecutive selected positions. Therefore \(f^k=0\) precisely when all strings avoid such a run; the polynomial is
\[
A_{a_d,k}(u)^{b_d}A_{a_d-1,k}(u)^{d-b_d}.
\]
Its constant term represents the empty map, already counted separately, and must be subtracted. The negative shift \(-d\) gives the same distribution, supplying the factor two.

For completeness, the displayed generating function for \(A_{\ell,k}\) follows from the unique decomposition of an admissible word into zero-terminated blocks \(1^j0\), where \(0\le j<k\), followed by a final block \(1^j\), where \(0\le j<k\). Summing block weights gives the rational function in the statement. This proves the translation part without numerical extrapolation.

**3. Reflections.** Fix a center \(c\in\{2,\ldots,2n\}\) and write \(s_c(x)=c-x\). Exactly \(m_c\) points lie in \([n]\cap s_c([n])\). Among them there are \(p_c=\lfloor m_c/2\rfloor\) disjoint transposed pairs, and possibly one fixed point. A restriction \(f=s_c|_E\) has \(f^2\) equal to the partial identity on \(E\cap s_c(E)\). Thus it is nilpotent if and only if it selects no fixed point and at most one point from each transposed pair. Every nonempty such restriction has \(f^2=0\). Each pair contributes \(1+2u\), so the candidate polynomial is \((1+2u)^{p_c}\). Removing the empty map and all \(2p_c\) rank-one restrictions leaves \((1+2u)^{p_c}-1-2p_cu\). Every remaining map has index exactly two and a unique center. This proves the full cumulative formula, including the cases \(n=1\) and \(k=1\).

**4. Closed rank distribution.** At rank \(r\ge1\), the translation restrictions contribute
\[
2\sum_{d=1}^{n-1}\binom{n-d}{r}=2\binom n{r+1},
\]
by the hockey-stick identity. At rank \(r\ge2\), reflections contribute \(2^r\sum_{c=2}^{2n}\binom{p_c}{r}\). For each positive \(j<h\), the value \(p_c=j\) occurs four times; the top value \(p_c=h\) occurs once for even \(n\) and three times for odd \(n\). Consequently
\[
\sum_{c=2}^{2n}\binom{p_c}{r}=4\binom h{r+1}+\eta_n\binom h r
\quad(r\ge2).
\]
The exceptional rank one has only the nonzero translations, numbering \(n(n-1)\). Summing over all ranks, or equivalently evaluating the polynomial at \(u=1\), produces the displayed parity-separated formulas. Both are valid at the smallest chain sizes. The previously established cardinality \(|D_n|\) then yields \(N_n/|D_n|\to1/3\) because the reflection correction grows as \(O(3^{n/2})\), strictly more slowly than \(2^n\).

**5. Logarithmic depth.** A uniformly random nilpotent is a translation restriction with probability \(1-o(1)\), because the number of nilpotent reflections is \(O(3^{n/2})\) while the translation total is \(2^{n+1}-2n-2\). Conditional on a positive shift magnitude \(d\), an eligible nonempty subset of \([n-d]\) is uniform; its binary indicators are independent fair bits conditional on not all being zero. For each fixed \(d\ge1\), the conditional distribution of the shift magnitude converges to \(2^{-d}\). Consequently, by controlling the geometric tail, it suffices to prove the run-length statement uniformly for each fixed finite set of shifts.

Fix \(d\) and write \(L\) for the longest consecutive selected run across its residue-class strings. For any fixed \(\varepsilon\in(0,1)\), put \(r_+=\lceil(1+\varepsilon)\log_2 n\rceil\). There are fewer than \(n\) possible run starts, so a union bound gives
\[
\Pr(L\ge r_+)\le n2^{-r_+}=O(n^{-\varepsilon}).
\]
Put \(r_-=\lfloor(1-\varepsilon)\log_2 n\rfloor\). Across the \(d\) strings, there are at least \(n/(2r_-)\) disjoint windows of length \(r_-\), for all sufficiently large \(n\) with fixed \(d\). Their all-selected events are independent and each has probability \(2^{-r_-}\). Therefore
\[
\Pr(L<r_-)\le
\exp\left(-\frac{n}{2r_-}2^{-r_-}\right)
\longrightarrow0.
\]
These bounds are initially for unconditioned fair bits; conditioning on a nonempty chosen domain changes them by a factor tending to one. The maximal length of a path of selected arrows is \(L\), hence the nilpotency index of a nonempty translation is exactly \(L+1\). Letting the finite cutoff on \(d\) grow completes the convergence in probability. This argument uses one sampled partial map throughout all powers, not independent resampling after each iteration.

## Verification

The included standalone `verify.py` generates all partial isometries as actual partial maps and deduplicates their translation/reflection descriptions. It computes nilpotency indices by literal composition, independently of the binary-run formula, and compares every rank and index cell to the displayed cumulative polynomials. It also checks the closed rank counts, closed total counts, and known monoid total for all chain sizes \(1\le n\le9\). Execution produces `JOINT_RANK_INDEX_OK`, `CLOSED_RANK_AND_TOTAL_OK`, and `VERIFY_OK`.

The nilpotent totals at lengths one through nine are \(1,3,9,27,65,151,317,663,1317\). For length eight, the exact nilpotency-index multiplicities, including the empty map, are \(1,368,170,84,24,10,4,2\) for indices one through eight. These are exhaustive finite checks, not a substitute for the proof for arbitrary chain lengths or the asymptotic bound.

## Relationship to prior work

The finite-chain partial-isometry monoids, their structural properties, fixed-point distributions, Green relations, and total cardinalities were studied by Kehinde and Umar (arXiv:1101.0049v1). In particular, their fixed-point-free counts **do not equal nilpotent counts**: a restriction of a reflection may have a two-cycle but no fixed point. Fernandes and Quinteiro (arXiv:1502.04829v1) gave presentations for these same monoids. Neither structural classification nor full-monoid cardinality is claimed to be new here.

Ali, Jada, and Zubairu (arXiv:2206.15299v1) studied generating ranks of larger monoids of order-preserving or order-reversing partial *contractions*. Such a generating rank is different from an element's domain rank or nilpotency index. Related earlier work on order-preserving partial-isometry nilpotents concerns nilpotent-generated subsemigroups and their generating ranks (Ali–Jada–Zubairu, DOI:10.22124/jart.2019.10875.1109). Its full text was not available for detailed comparison; this is a residual priority risk for possible unreported counting refinements. None of these located descriptions supplies the joint cumulative rank/index polynomial stated here.

Classical longest-run bounds for fair binary words are used in the asymptotic argument; those probabilistic techniques are not claimed as new. The specific combination of rank-index refinement, mixed translation/reflection enumeration, and its nilpotent sampling law is the assessed contribution.

## Limitations

The result is about partial bijective distance-preserving maps of the ordinary metric chain, not arbitrary order-preserving contractions, arbitrary partial injections, or graph-induced partial automorphisms. The limit theorem specifies the leading logarithmic scale only; it does not determine a centered extreme-value law or the conditional depth distribution at growing displacement. The 2018 order-preserving-isometry paper's inaccessible full text and potential general semigroup-enumeration results leave publication priority provisional. The mathematical proof and finite computations support the stated theorem but do not constitute external independent validation.

## References

1. R. Kehinde and A. Umar, *On the semigroup of partial isometries of a finite chain*, arXiv:1101.0049v1 (2010-12-30), https://arxiv.org/abs/1101.0049 .
2. V. H. Fernandes and T. M. Quinteiro, *Presentations for monoids of finite partial isometries*, arXiv:1502.04829v1 (2015-02-17), https://arxiv.org/abs/1502.04829 .
3. B. Ali, M. A. Jada, and M. M. Zubairu, *On the Ranks of Semigroup of Order-preserving or Order-reversing Partial Contraction Mappings on a Finite Chain*, arXiv:2206.15299v1 (first public 2022-06-30), https://arxiv.org/abs/2206.15299 .
4. B. Ali, M. A. Jada, and M. M. Zubairu, *On the ranks of certain semigroups of order-preserving partial isometries of a finite chain*, Journal of Algebra and Related Topics 6(2) (2018), 15–33, DOI:10.22124/jart.2019.10875.1109 .
