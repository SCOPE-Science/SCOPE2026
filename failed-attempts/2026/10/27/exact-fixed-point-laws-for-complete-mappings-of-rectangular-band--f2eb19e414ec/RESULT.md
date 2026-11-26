# Exact fixed-point laws for complete mappings of rectangular bands

## Finding
Let \(a,b\geq1\) be integers. In the rectangular band \(S_{a,b}=[a]\times[b]\), with \((i,j)(k,l)=(i,l)\), a complete mapping is a permutation \(\alpha\) for which \(\theta(x)=x\alpha(x)\) is also a permutation. There are exactly
\[
N_{a,b}=(b!)^a(a!)^b
\]
complete mappings. For a uniformly sampled complete mapping, let \(F_{a,b}=|\{x\in S_{a,b}:\alpha(x)=x\}|\). Its entire probability-generating polynomial is
\[
\mathbb E[t^{F_{a,b}}]=\sum_{T\subseteq[a]\times[b]}(t-1)^{|T|}
 \prod_{i=1}^a\frac{1}{(b)_{d_i(T)}}
 \prod_{j=1}^b\frac{1}{(a)_{e_j(T)}},
\]
where \(d_i(T)=|T\cap(\{i\}\times[b])|\), \(e_j(T)=|T\cap([a]\times\{j\})|\), and \((n)_r=n(n-1)\cdots(n-r+1)\), with \((n)_0=1\). In particular, \(\mathbb E[F_{a,b}]=1\). If \(a,b\ge2\), then
\[
\operatorname{Var}(F_{a,b})=1+\frac{1}{ab}.
\]
If \(\min(a,b)=1<ab\), the variance is \(1\); if \(a=b=1\), it is \(0\). Finally, as \(\min(a,b)\to\infty\),
\[
F_{a,b}\ \xrightarrow{\mathrm d}\ \operatorname{Poisson}(1).
\]
The finite exact law and nontrivial variance correction refine the asymptotic Poisson behavior; the distribution here concerns fixed points of \(\alpha\), not fixed points of its associated orthomorphism \(\theta\).

## Assumptions and scope
All index sets are labeled and nonempty. Each complete mapping is counted once as a function on the labeled \(ab\)-element set. No quotient by automorphisms is taken. The limiting statement requires both side lengths to diverge; it does not assert a uniform convergence rate or analyze the regime where one side length is fixed. The probability generating function is a polynomial, so the coefficient of \(t^r\) gives the exact probability of \(r\) fixed points for each \(0\le r\le ab\).

## Proof
**Canonical parametrization and count.** For any permutation \(\alpha\), write \(\alpha(i,j)=(u(i,j),p_i(j))\). Since \(\theta(i,j)=(i,p_i(j))\), the map \(\theta\) is bijective exactly when each row map \(p_i:[b]\to[b]\) is a permutation. Suppose this holds. For each output column \(l\), the preimages of \([a]\times\{l\}\) are precisely \(\{(i,p_i^{-1}(l)):i\in[a]\}\). Therefore \(\alpha\) is bijective exactly when the maps \(q_l:i\mapsto u(i,p_i^{-1}(l))\) are permutations of \([a]\). Conversely any independent choice of permutations \(p_i\in S_b\), \(q_l\in S_a\) determines a unique complete mapping
\[
\alpha(i,j)=\bigl(q_{p_i(j)}(i),p_i(j)\bigr).
\]
This is a bijection between all complete mappings and \(S_b^a\times S_a^b\), proving \(N_{a,b}\).

**Complete fixed-point law.** Equip the parameter set with the uniform distribution, so all \(p_i\) and \(q_j\) are mutually independent uniform permutations. A cell \((i,j)\) is fixed precisely when \(p_i(j)=j\) and \(q_j(i)=i\). For any set of distinct cells \(T\), a uniform permutation of \(m\) elements fixes a specified set of \(r\) points with probability \((m-r)!/m!=1/(m)_r\). Independence consequently gives
\[
\Pr(T\subseteq\operatorname{Fix}(\alpha))=
\prod_i\frac1{(b)_{d_i(T)}}\prod_j\frac1{(a)_{e_j(T)}}.
\]
The pointwise identity \(t^{F_{a,b}}=\prod_{x\in S_{a,b}}(1+(t-1)\mathbf1_{\{\alpha(x)=x\}})\), expanded and averaged, proves the generating-polynomial formula. In particular each cell is fixed with probability \(1/(ab)\), so \(\mathbb E[F_{a,b}]=1\).

**Variance and its boundaries.** Suppose \(a,b\ge2\). In the second factorial moment \(\mathbb E[(F_{a,b})_2]\), ordered pairs of different cells fall into three disjoint classes. Pairs sharing a row contribute
\[
 a b(b-1)\cdot\frac1{(b)_2a^2}=\frac1a;
\]
pairs sharing a column contribute \(1/b\); pairs with different rows and columns contribute
\[
 a(a-1)b(b-1)\cdot\frac1{a^2b^2}=\frac{(a-1)(b-1)}{ab}.
\]
Hence \(\mathbb E[(F_{a,b})_2]=1+1/(ab)\). Since \(\mathbb E F_{a,b}=1\), the variance equals this second factorial moment. If one side has length one, \(\alpha\) is an unrestricted uniformly random permutation on the other side, with the classical fixed-point variance \(1\) for that side of length at least two. The singleton case is deterministic.

**Poisson limit.** Fix an integer \(k\ge1\). For every set \(T\) of \(k\) distinct cells, uniformly in \(T\) as \(\min(a,b)\to\infty\),
\[
\Pr(T\subseteq\operatorname{Fix}(\alpha))=(ab)^{-k}\bigl(1+O_k(a^{-1}+b^{-1})\bigr).
\]
Indeed, \((m)_r=m^r(1+O_k(m^{-1}))\) for \(0\le r\le k\), and the sum of all row degrees and all column degrees separately equals \(k\), so the total relative error is uniform. Summing over the \((ab)_k\) ordered \(k\)-tuples of distinct cells gives
\[
\mathbb E[(F_{a,b})_k]=\frac{(ab)_k}{(ab)^k}\bigl(1+O_k(a^{-1}+b^{-1})\bigr)\longrightarrow1.
\]
These are exactly the factorial moments of \(\operatorname{Poisson}(1)\). The method of moments applies because all fixed ordinary moments converge to the corresponding Poisson moments, and the Poisson law is moment-determinate (its moment generating function exists near zero). This proves convergence in distribution.

## Verification
The standalone `check.py` independently enumerates all permutations of the underlying grid for side lengths \((1,1)\), \((1,3)\), \((2,2)\), and \((2,3)\), retaining only those whose associated orthomorphism is bijective. It separately computes the exact full fixed-point polynomial through the subset formula and compares the full histograms and variances. For \((3,3)\), it computes the subset formula with exact rational arithmetic: among \(46656\) complete mappings, \(17972\) have no fixed point and \(16515\) have exactly one fixed point. Its terminal assertion is `VERIFY_OK`. These finite verifications do not replace the all-parameter proof or the distributional limit theorem.

## Relationship to prior work
Araújo, Bentz, Cameron, Hendrey and Kinyon [1] introduce a systematic study of complete mappings of finite semigroups. Their Section 6.1 enumerates complete mappings of *combinatorial Brandt semigroups* through Latin squares; these have zero products and are not the zero-free rectangular bands considered here. Their Section 12 establishes existence and rigidity statements for bands, including the fact that identity is a complete mapping of any band. Their Problem 15.6 explicitly asks for cycle-structure information of complete mappings and orthomorphisms. The present fixed-point distribution solves the length-one cycle statistic for the full two-parameter family of rectangular bands, with a finite-size variance correction and a Poisson limit. No earlier existence assertion determines this distribution. Cameron's earlier discussion [2] formulates the overarching Rees-matrix existence problem without this fixed-point law.

## Limitations
The claimed novelty is the **exact distributional law, finite-size covariance effect, and Poisson asymptotics**, not the fact that a rectangular band admits a complete mapping. The enumeration formula is included because it normalizes the random law. The limit treats both side lengths tending to infinity; rates, joint cycle counts, and general Rees matrix semigroups are not treated. As with any literature comparison, equivalent formulations outside the inspected corpus cannot be completely excluded. Independent mathematical validation has not been performed.

## References
[1] J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1, first posted August 25, 2026, Sections 6.1 and 12 and Problem 15.6. https://arxiv.org/abs/2608.25092

[2] P. J. Cameron, *Research trips in February*, March 13, 2020, https://cameroncounts.wordpress.com/2020/03/13/research-trips-in-february/.
