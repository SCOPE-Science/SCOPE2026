# Exact random-ranking SD-EF1 reliability with multipartite conflicts and a Gaussian transition

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph of conflicting indivisible goods, with \(r\ge2\), integer part sizes \(n_i\ge1\), and \(N=\sum_{i=1}^r n_i\). Let \(\ell\) be a positive number of **labeled** agents, restricted throughout the counting formulas to \(N/2<\ell\le N\). All agents have the same **strict** preference ranking. Every good must be assigned, each agent's bundle must be independent in \(G\), and the allocation must satisfy stochastic-dominance envy-freeness up to one good (SD-EF1).

Put \(t=N-\ell\). For any ranking, write \(L\) for the set of its bottom \(t\) goods and \(x_i=|L\cap V_i|\), where \(V_i\) is graph part \(i\). Define \((a)_{\underline b}=a(a-1)\cdots(a-b+1)\) if \(0\le b\le a\), and zero if \(b>a\).

**Exact allocation count and feasibility:** The number of labeled complete, feasible SD-EF1 allocations is
\[
F(G,\ell,L)=\ell!\prod_{i=1}^r(n_i-x_i)_{\underline{x_i}}.
\]
There is at least one such allocation if and only if \(2x_i\le n_i\) for all \(i\). The number depends only on the set \(L\), not on its internal ranking or the ranking of the first \(\ell\) goods.

**Random-ranking probability:** If the common strict ranking is uniform among all \(N!\) permutations, then
\[
P_G(\ell)=\frac{[z^t]\displaystyle\prod_{i=1}^r\left(\sum_{j=0}^{\lfloor n_i/2\rfloor}\binom{n_i}{j}z^j\right)}{\binom Nt}.
\]
The expected number of labeled feasible SD-EF1 allocations is, in the same parameter range,
\[
\mathbb EF=\frac{\ell!}{\binom Nt}[z^t]\prod_{i=1}^r\left(\sum_{j=0}^{\lfloor n_i/2\rfloor}\binom{n_i}{j}(n_i-j)_{\underline j}z^j\right).
\]

**Worst-case all-ranking threshold:** For all common weak orders (including the strict orders above), the least number of agents guaranteeing a feasible SD-EF1 allocation is
\[
\chi_s^1(K_{n_1,\ldots,n_r})=N-\left\lfloor\frac{\min_i n_i}{2}\right\rfloor.
\]
This general formula includes the previously established value \(\chi_s^1(K_{m,m})=\lceil 3m/2\rceil\) of Haviv (2026, Lemma 3.8).

**Gaussian critical window:** Specialize to \(G=K_{m,m}\), \(m\ge2\), and \(\ell=m+s\) with \(1\le s\le m\). Then \(t=m-s\), and
\[
P_{m,s}=\frac{\displaystyle\sum_{x=\max(0,t-\lfloor m/2\rfloor)}^{\min(t,\lfloor m/2\rfloor)}\binom mx\binom m{t-x}}{\binom{2m}{t}}.
\]
For integer sequences \(s_m\in[1,m]\) satisfying \(s_m/\sqrt m\to c\in[0,\infty)\),
\[
\lim_{m\to\infty}P_{m,s_m}=2\Phi(\sqrt 2c)-1=\operatorname{erf}(c),
\]
where \(\Phi\) is the standard normal distribution function. If \(s_m/\sqrt m\to\infty\), then \(P_{m,s_m}\to1\). In particular, the success probability tends to zero for \(s_m=o(\sqrt m)\), to a nontrivial value in \((0,1)\) for \(s_m\sim c\sqrt m\), and to one for \(s_m\gg\sqrt m\). This typical-case requirement is substantially weaker than the all-ranking bound \(m+s\ge\lceil3m/2\rceil\).

## Assumptions and scope
A graph edge denotes two goods that cannot belong to the same agent. Graph parts \(V_i\) are independent internally and mutually complete across distinct parts. All agents have **one common strict preference** over goods; there are no valuations, random allocations, independent agent rankings, or distributional assumptions beyond a uniform random **common** ranking in the probability statements. An allocation is a partition into \(\ell\) labeled bundles, empty bundles permitted in general but ruled out here by SD-EF1 and the given size range. For agents \(a,b\), SD-EF1 means that there exists a good \(g\) in bundle \(b\) (or no removal if \(b\)'s bundle is empty) such that the number of goods in \(a\)'s bundle within each preference prefix is at least the number in \(b\)'s bundle after removing \(g\). The exact counting and probability results assume \(N/2<\ell\le N\); the all-ranking threshold concerns all positive agent counts via the monotonicity of type-one strong colorability.

## Proof
**1. Prefix criterion.** Under a common strict order, SD-EF1 is equivalent to the condition that for every prefix of the ranking, any two agents' cumulative assigned-good counts differ by at most one. Necessity: if some agent \(b\) has at least two more top-prefix goods than \(a\), removing any one good cannot remove the deficit. Sufficiency: for a fixed ordered pair \((a,b)\), if \(b\) is nonempty remove its earliest (highest-ranked) good. Before that good, \(b\)'s prefix count is zero; after it, the bound on count differences ensures that \(a\)'s prefix count is at least \(b\)'s remaining count. If \(b\) is empty, there is nothing to remove.

**2. Allocation structure and exact count.** At the prefix of length \(\ell\), exactly \(\ell\) goods have been assigned. The prefix criterion forces each agent to hold exactly one of these goods. Because the remaining \(t=N-\ell<\ell\) goods are lower ranked, no agent may receive two of them: that would give one agent three goods, while at least one other agent has only one, violating the full-prefix criterion. Conversely, any bijective placement of the first \(\ell\) goods among agents and any injective placement of the last \(t\) goods among those agents preserves the prefix criterion. Conflict feasibility further requires a bottom good in part \(i\) to be assigned to an agent whose top good also belongs to part \(i\). Among the top \(\ell\) goods there are \(n_i-x_i\) in part \(i\); hence precisely \((n_i-x_i)_{\underline{x_i}}\) injections exist for the \(x_i\) distinct bottom goods of that part. Multiplying over parts and over the \(\ell!\) bijections from top goods to labeled agents yields the claimed count. Each factor is positive exactly when \(x_i\le n_i-x_i\).

**3. Uniform random ranking.** A bottom set \(L\) of size \(t\) occurs with probability \(1/\binom Nt\). For every vector \((x_1,\ldots,x_r)\) with sum \(t\), there are \(\prod_i\binom{n_i}{x_i}\) choices of \(L\). Summing over the vectors satisfying \(2x_i\le n_i\) produces the stated coefficient formula. Multiplying the summands by the exact allocation count before summing gives the expectation formula.

**4. Worst-case threshold.** Let \(a=\min_i n_i\) and \(\ell_0=N-\lfloor a/2\rfloor\). Because \(a\le N/2\), we have \(\ell_0>N/2\). Every bottom set at \(\ell_0\) has size \(\lfloor a/2\rfloor\), so each \(x_i\le \lfloor a/2\rfloor\le\lfloor n_i/2\rfloor\); Step 2 therefore constructs a fair complete allocation for **every** strict ranking. For any weak ranking, refine tied goods into a strict order; all weak upper-contour sets are strict-order prefixes, so the same allocation is SD-EF1 for the original weak order.

For the lower bound consider \(\ell=\ell_0-1\). If \(\ell>N/2\), arrange for \(\lfloor a/2\rfloor+1\) bottom goods to belong to a smallest graph part. Then the necessary same-part pairing condition fails. If \(\ell\le N/2\), the constraints \(a\le N/2\) and \(\ell=N-\lfloor a/2\rfloor-1\) imply \(N\le4\); for \(N=4\) the only remaining case is the balanced graph \(K_{2,2}\), for which two agents and the strict ranking placing the two goods of one part first, followed by the other part, are incompatible with conflict-free SD-EF1. For \(N=2\) the graph is \(K_{1,1}\), and one agent cannot receive both adjacent goods; \(N=3\) gives \(\ell>N/2\) and was already treated. Hence at \(\ell_0-1\) there exists a common strict ranking with no feasible SD-EF1 allocation. Monotonicity of type-one strong colorability (Haviv, Lemma 3.4), combined with Haviv's general correspondence between the universal SD-EF1 guarantee and type-one strong colorability (Theorem 1.1), extends this lower bound to every smaller positive agent count.

**5. Gaussian window.** For \(K_{m,m}\), let \(X\) be the number of bottom \(t=m-s\) goods in the first part. Then \(X\) has the hypergeometric law \(\mathrm{Hypergeom}(2m,m,t)\) with
\[
\mathbb EX=\frac{m-s}{2},\qquad\operatorname{Var}X=\frac{m^2-s^2}{4(2m-1)}.
\]
Feasibility is \(t-\lfloor m/2\rfloor\le X\le\lfloor m/2\rfloor\). The interval is centered at \(\mathbb EX\) and has radius \(s/2+O(1)\). For \(s/\sqrt m\to c<\infty\), the hypergeometric central limit theorem gives \((X-\mathbb EX)/\sqrt{m/8}\Rightarrow N(0,1)\). The rescaled interval tends to \([-\sqrt2 c,\sqrt2 c]\), yielding \(2\Phi(\sqrt2 c)-1\); when \(c=0\), continuity of the limiting normal law gives limit zero even though the interval shrinks. For \(s/\sqrt m\to\infty\), variance is at most \(m/8+O(1)\) and Chebyshev's inequality bounds failure by \(O(m/s^2)\), which vanishes. No finite enumeration is used to infer the infinite limit.

## Verification
Run `python3 verify.py` using Python 3. The checker directly implements the existential one-good-removal definition and compares it with the prefix criterion on 71,110 candidate assignments; independently enumerates every allocation on 181 small multipartite instances and compares with the exact formula; checks the all-order threshold across seven graph-size families by enumerating bottom sets; and evaluates exact hypergeometric probabilities at sizes \(m=100,400,1600\) for scaled surpluses \(c=0.5,1,2\) against the Gaussian limit. These finite tests corroborate the algebra and conventions but are not an exhaustive proof of the all-size assertions or the limit. The derivation above supplies the all-size proof.

## Relationship to prior work
Haviv, *Fair Allocation under Conflict Constraints via Strong Colorability* (arXiv:2607.01059v1, July 1, 2026), already proves the general SD-EF1 versus type-one strong-colorability correspondence (Theorem 1.1), the block/prefix structure (Lemmas 4.1–4.3), and the balanced-bipartite worst-case threshold (Lemma 3.8). These facts are used, not presented as novel. The new claimed result counts all feasible labeled SD-EF1 allocations for each strict common ranking on arbitrary complete multipartite conflict graphs, computes their probability under a uniform random ranking, and identifies the exact Gaussian success transition and its separation from worst-case requirements. The multipartite worst-case formula generalizes Haviv's particular balanced-bipartite computation but is secondary to the probabilistic reliability theorem. Equbal et al., *Fair Allocation under Conflict Constraints* (arXiv:2605.09930v1, May 11, 2026), study primarily EF1 with maximal possibly incomplete allocations; Hummel–Hetland (2021) study EF1, MMS and related fairness with conflicts. Neither inspected work gives the stated random-ranking probability law. The normal approximation itself is a classical hypergeometric central limit theorem, not asserted to be new independently.

## Limitations
The allocation-count and random-order formulas assume \(N/2<\ell\le N\), all agents have a **shared strict** ranking, and the conflict graph is complete multipartite. They do not describe heterogeneous preferences, ties in randomly sampled rankings, EF1 for arbitrary cardinal valuations, or an agent count at most half the number of goods. The Gaussian limit is for balanced bipartite graphs in the stated scaling. No independent mathematical audit is claimed. An unindexed equivalent calculation or an implicit prior consequence remains a residual originality risk.

## References
1. Ishay Haviv, *Fair Allocation under Conflict Constraints via Strong Colorability*, arXiv:2607.01059v1, first publicly available July 1, 2026. https://arxiv.org/abs/2607.01059
2. S. Equbal, R. Gurjar, A. Igarashi, Y. Kumar, P. Manurangsi, S. Nath, R. Saxena, R. Vaish, H. Yoneda, *Fair Allocation under Conflict Constraints*, arXiv:2605.09930v1, May 11, 2026. https://arxiv.org/abs/2605.09930
3. H. Hummel and M. L. Hetland, *Fair allocation of conflicting items*, Autonomous Agents and Multi-Agent Systems 36, article 8 (first online December 23, 2021). https://doi.org/10.1007/s10458-021-09537-3
