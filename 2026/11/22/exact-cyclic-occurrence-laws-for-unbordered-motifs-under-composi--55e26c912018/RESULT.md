# Exact cyclic occurrence laws for unbordered motifs under composition and iid sampling

## Finding

For a finite alphabet \(\Sigma\), let \(u=u_0\dots u_{m-1}\in\Sigma^m\) be **unbordered**, with \(m\ge2\). Thus no nonempty proper prefix equals a suffix. For \(n\ge1\), let \(X_u(w)\) count the starts \(i\in\mathbb Z/n\mathbb Z\) such that \(w_iw_{i+1}\dots w_{i+m-1}=u\), with all indices interpreted cyclically. Words are **indexed circles**, not necklaces.

Put \(c_a=|u|_a\), and define
\[
H_{n,m}(j)=\begin{cases}1,&j=0,\\\dfrac{n}{n-(m-1)j}\binom{n-(m-1)j}{j},&1\le j\le\lfloor n/m\rfloor.\end{cases}
\]
For every nonnegative composition vector \(K=(K_a:a\in\Sigma)\) of sum \(n\), the **exact number** of circles with this composition and \(X_u(w)=r\), for \(0\le r\le\lfloor n/m\rfloor\), is
\[
\boxed{B_{n,K,u}(r)=\sum_{j=r}^{\lfloor n/m\rfloor}(-1)^{j-r}\binom jr H_{n,m}(j)\binom{n-jm}{(K_a-jc_a)_{a\in\Sigma}}.}
\]
A multinomial coefficient is zero if any lower entry is negative. Consequently **all unbordered motifs with identical letter compositions have the same full occurrence-count distribution in every fixed-composition class**.

For independently sampled letters of strictly positive probabilities \(p_a\) summing to one, put \(\pi=\prod_a p_a^{c_a}\). Then
\[
\boxed{\mathbb E[t^{X_u}]=\sum_{j=0}^{\lfloor n/m\rfloor}H_{n,m}(j)\pi^j(t-1)^j.}
\]
For \(n\ge m\), this is a **Poisson–binomial probability generating polynomial**: \(X_u\) is distributed as a sum of exactly \(\lfloor n/m\rfloor\) independent, nondegenerate Bernoulli variables. For \(n<m\), \(X_u=0\). Both assertions include all wrap-around positions.

## Assumptions and scope

The alphabet is finite of size at least two and \(m\ge2\). An unbordered word is necessarily nonconstant. A composition class is the set of all indexed words of length \(n\) with exactly \(K_a\) occurrences of each letter \(a\). The iid statement assumes every \(p_a>0\). The theorem does not concern sampling uniformly from *necklaces* or nonindependent stationary sources. The multinomial formula remains valid even when some \(K_a=0\).

## Proof

**1. Compatibility of prescribed starts.** Write \(E_i\) for the event that \(u\) occurs at cyclic position \(i\). If \(n<m\), such an occurrence would make \(u\) periodic with period \(n\), and hence give a proper border of length \(m-n\), contradiction. Hence \(X_u=0\) in this case. Assume \(n\ge m\). Two intervals of \(m\) cyclic positions intersect precisely when their starts have circular distance less than \(m\). If \(E_i\) and \(E_{i+d}\) hold with \(1\le d<m\), comparing their common positions forces the suffix of \(u\) of length \(m-d\) to equal its prefix of that length, contradiction. The same holds in the opposite direction. Thus every simultaneously realizable set of starts is \(m\)-separated around the circle. Conversely, prescribing any such set of starts fixes disjoint position intervals, so the constraints are compatible.

**2. Exact cyclic placement multiplicities.** Given \(j\ge1\) distinct cyclic start positions separated by at least \(m\), list their clockwise positive gaps \(g_1,\dots,g_j\). They satisfy \(g_i\ge m\) and \(\sum_i g_i=n\). The number of ordered gap vectors is \(\binom{n-mj+j-1}{j-1}\). There are \(n\) choices of marked first start and each unmarked \(j\)-set is thereby represented exactly \(j\) times. Therefore the count is
\[
\frac nj\binom{n-mj+j-1}{j-1}=H_{n,m}(j).
\]
The empty set contributes one. No such nonempty set exists for \(j>\lfloor n/m\rfloor\). This identity also applies to \(n=m\), where the graph is complete.

**3. Composition-refined inclusion–exclusion.** Fix \(K\), and for each admissible set \(S\) of \(j\) starts impose the occurrences \(E_i\) for \(i\in S\). Exactly \(jc_a\) positions are set to symbol \(a\); the other \(n-jm\) free positions can be filled in \(\binom{n-jm}{(K_a-jc_a)_a}\) ways. For each word \(w\), expand \(t^{X_u(w)}=\prod_i(1+(t-1)\mathbf1_{E_i}(w))\). Summing over all words of composition \(K\) gives the polynomial in \(t-1\); taking its coefficient at \(t^r\) proves the boxed formula. Because it only uses \(m\) and \(c\), it proves the asserted anagram invariance.

**4. Iid exact law.** Each compatible \(j\)-start prescription has probability \(\pi^j\), since it uses disjoint letters; incompatible prescriptions have probability zero. The same indicator-product expansion proves the iid generating-polynomial identity.

**5. Real-rootedness and the Bernoulli representation.** Form a graph with vertices the \(n\) starts; join two vertices when their length-\(m\) circular intervals overlap. Its independent sets are precisely the admissible start sets from step 2. It is the \((m-1)\)-st power of a cycle (under the natural convention that it is complete when all starts conflict). Crucially, this graph is **claw-free**. Indeed, a neighbor of a fixed start \(i\) must lie among the \(2m-2\) starts at offsets \(-(m-1),\dots,-1,1,\dots,m-1\). Three pairwise nonadjacent such neighbors, in increasing offset order, would require two successive gaps of at least \(m\), hence span at least \(2m\), but their available offset span is only \(2m-2\). For \(n<3m\), no three disjoint \(m\)-arcs exist anywhere, giving the same conclusion.

By the established theorem of Chudnovsky and Seymour, the independence polynomial of any finite claw-free graph has only real zeros. Its coefficients are nonnegative and its constant term is one, hence its zeros are strictly negative. Since \(\mathbb E[t^{X_u}]=I_G(\pi(t-1))\), every zero of the probability generating polynomial is real and less than one. Because this polynomial has nonnegative probability coefficients and positive constant term, its zeros cannot be nonnegative; thus all are strictly negative. The constant term is indeed positive: any constant-letter circle avoids the nonconstant unbordered \(u\), and has positive iid probability. The leading coefficient is positive as any maximal \(m\)-separated set of starts can occur with positive probability. Hence the degree is exactly \(\lfloor n/m\rfloor\). Normalizing the linear factors at \(t=1\) yields
\[
\mathbb E[t^{X_u}]=\prod_{h=1}^{\lfloor n/m\rfloor}\bigl(1-\theta_h+\theta_ht\bigr),\qquad0<\theta_h<1,
\]
which is the distribution of a sum of independent Bernoulli variables. This is an equality in distribution, not an assertion that the original occurrence indicators are independent.

## Verification

The standalone script `verify.py` exhaustively enumerates indexed binary and ternary circles with several sampling distributions. It compared the fixed-composition formula against **36,984** direct computations, the biased iid probability law against **1,968** direct computations, and the cyclic placement formula against **187** independent subset enumerations. All passed. A boundary illustration: for uniform binary circles of length four, the unbordered motif `001` has count frequencies \((8,8,0)\) at occurrence counts \(0,1,2\), while the bordered motif `010` has \((10,4,2)\). The program is a finite sanity check; the infinite quantified claims rest on the preceding proof.

Run `python verify.py` in a standard Python 3 environment. The required output appears in `verification_output.txt`.

## Relationship to prior work

Chudnovsky and Seymour (2007) prove the general claw-free independence-polynomial real-rootedness theorem used as an ingredient. Brown and Hoshino (2009), Theorem 3.3, give the independent-set coefficients \(H_{n,m}(j)\) for powers of cycles; those graph coefficients are **not claimed to be new**. Earlier word-occurrence frameworks of Régnier and Bassino–Clément–Fayolle–Nicodème concern ordinary finite linear texts, while Arnoux (2016) proves deterministic relations among counts on circular words. Bóna–Maga–Richey (first public version 2026-06-04) study forbidden-pattern shifts and limiting letter frequencies, motivating finite cyclic conditioned questions. A published 2026 result, *A Poisson–binomial universality boundary for pattern counts in independent words*, proves a related **linear-text** result. The present theorem singles out the simultaneous **cyclic**, **full fixed-composition**, and **iid Poisson–binomial** laws and the anagram-equidistribution consequence. It does not claim originality for the underlying general graph or linear-text results.

## Limitations

No converse is proved for bordered motifs, no assertion about independence of occurrence indicators is made, and no Poisson–binomial claim is made under fixed-composition sampling. The formula counts indexed circles, not necklace classes. This is a self-review only; no independent audit has been performed. A decisive publication-priority risk remains if an earlier cyclic pattern-occurrence specialization, perhaps derivable immediately from existing general enumerators, already states the same complete distribution. The full text of the motivating June 2026 paper and one especially close published 2026 linear-case record was not accessible for exhaustive comparison; only their published descriptions were available.

## References

1. M. Bóna, B. Maga and J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655v1 (first public 2026-06-04), https://arxiv.org/abs/2606.06655.
2. M. Chudnovsky and P. Seymour, *The roots of the independence polynomial of a clawfree graph*, Journal of Combinatorial Theory B **97** (2007), 350–357, https://doi.org/10.1016/j.jctb.2006.06.001.
3. J. Brown and R. Hoshino, *Independence polynomials of circulants with an application to music*, Discrete Mathematics **309** (2009), 2292–2304, https://www.mscs.dal.ca/~hoshino/music.pdf, Theorem 3.3.
4. P. Arnoux, *Note on occurrences of factors in circular words*, RAIRO TIA **50** (2016), 167–170, https://doi.org/10.1051/ita/2016019.
5. F. Bassino, J. Clément, J. Fayolle and P. Nicodème, *Counting occurrences for a finite set of words: an inclusion-exclusion approach*, DMTCS, 2007, https://doi.org/10.46298/dmtcs.3543.
6. *A Poisson–binomial universality boundary for pattern counts in independent words*, published October 18, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-poisson-binomial-universality-boundary-for-pattern-counts-in-i--f2d2b4ad711f.
