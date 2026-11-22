# Binary–ternary ordinal comparisons: exact static and online shattering

## Finding

**Theorem (finite-palette comparison capacity).** Let \(a,b\) be nonnegative integers, \(k=a+b\geq 1\), and let \(X=\{0,1,2\}^{a}\times\{0,1\}^{b}\). On \(X\), let \(\mathcal H_{a,b}\) consist of the two Boolean constants and, for each coordinate \(i\), all the one-sided threshold predicates \(h_{i,t}(x)=[x_i\leq t]\), with \(t\) strictly below that coordinate's maximum value. Then

\[
\operatorname{Ldim}(\mathcal H_{a,b})=\left\lfloor\log_2(2a+b+2)\right\rfloor.
\]

For \(k\geq2\), **the exact same formula holds for the ordinary VC dimension**:

\[
\operatorname{VCdim}(\mathcal H_{a,b})=\operatorname{Ldim}(\mathcal H_{a,b})
=\left\lfloor\log_2(2a+b+2)\right\rfloor.
\]

For \(k=1\), the VC dimension is \(1\); the online dimension is \(1\) for a binary feature and \(2\) for a ternary feature. The theorem also has a sharp palette boundary: on two four-valued features, with the same two constants and one-sided thresholds, the VC dimension is \(2\) but the Littlestone dimension is \(3\). Thus the equality for all mixtures of two- and three-valued features does not extend uniformly to four-valued features.

The result is about *single atomic comparisons*, not arbitrary Boolean combinations, negated comparisons, role quantification or full description-logic concepts.

## Assumptions and scope

Every coordinate has its full stated finite ordered alphabet; all Cartesian-product feature vectors are allowed examples. Each predicate has one chosen coordinate and one threshold, always with the **same polarity** \(\leq\). The two Boolean constants are genuine additional concepts. Examples used in VC shattering are pairwise distinct. Both dimensions have their conventional definitions: static shattering of \(s\) examples realizes all \(2^s\) labelings by concepts, while online shattering of depth \(d\) realizes all root-to-leaf binary transcripts in a complete depth-\(d\) example-query tree. The finite-case theorem holds for all \(a,b\ge0\) with \(a+b\ge1\), including either homogeneous alphabet and mixed alphabets.

More generally, with arbitrary finite ordered coordinate alphabets of sizes \(q_i\ge2\), on their full product, the same one-sided atomic comparison class with both constants has the exact online dimension

\[
\operatorname{Ldim}=\left\lfloor\log_2\left(2+\sum_i(q_i-1)\right)\right\rfloor.
\]

No general VC-dimension equality is claimed for arbitrary \(q_i\).

## Proof

**1. Every version space can be split to any required size.** For any nonempty subset \(S\) of distinct hypotheses, write \(S_i\) for its thresholds on coordinate \(i\), and let \(c_1,c_0\in\{0,1\}\) indicate whether the always-true and always-false hypotheses belong to \(S\). As the query value \(x_i\) moves along its alphabet, precisely \(j\) of the hypotheses in \(S_i\) evaluate true for every integer \(0\le j\le |S_i|\): these thresholds are strictly ordered, so a cut between consecutive listed thresholds realizes any such \(j\), and the extreme alphabet values realize \(0\) and \(|S_i|\). Different coordinates can be chosen independently. Hence, at one example, the possible numbers of positive hypotheses in \(S\) include every integer from \(c_1\) through \(|S|-c_0\). In particular, every \(S\) with \(|S|\ge2\) admits a split with both branches nonempty and sizes \(\lfloor|S|/2\rfloor\), \(\lceil|S|/2\rceil\). This builds by induction a complete mistake tree of depth \(\lfloor\log_2|S|\rfloor\). The reverse bound is cardinality: a depth-\(d\) complete tree requires at least \(2^d\) distinct hypotheses. With \(|\mathcal H|=2+\sum_i(q_i-1)\), the online formula follows, including the binary–ternary case.

**2. Static upper bound from chain capacity.** Fix \(s\ge3\) distinct putatively shattered examples. The two constants supply only the empty and full labeling patterns. The thresholds on any binary coordinate supply at most one other subset of \([s]\). The two thresholds on a ternary coordinate supply at most two other subsets, and these are nested. Thus realizing all \(2^s-2\) nonempty proper subsets requires

\[
2a+b\ge2^s-2.
\]

For \(s=2\), the two singleton subsets are incomparable, so two different coordinates are needed: a single coordinate, even a ternary one, cannot shatter a pair. For \(s=1\), both constants suffice to shatter any example. This proves the asserted upper bound and the one-coordinate exception.

**3. Pairing all proper nonempty subsets.** For every integer \(s\ge3\), there exists a perfect pairing of the \(2^s-2\) nonempty proper subsets of \([s]\) in which each pair consists of two strictly nested subsets. Here is a complete explicit construction. Initially pair \(U\) with \(U\cup\{1\}\) for each \(U\subseteq\{2,\ldots,s\}\), omitting \(U=\varnothing\) and \(U=\{2,\ldots,s\}\). These pairs cover everything except \(\{1\}\) and \(\{2,\ldots,s\}\). Remove the pair \(\{2\},\{1,2\}\), and replace it with \(\{1\},\{1,2\}\) and \(\{2\},\{2,\ldots,s\}\). All new pairs are strictly nested because \(s\ge3\); the result is a perfect pairing. In particular, its size is \(2^{s-1}-1\). The construction does not invoke any unproved matching existence theorem.

**4. Static attainment for mixed palettes.** Set \(N=2^s-2\) and suppose \(s\ge3\), \(2a+b\ge N\). From the explicit perfect pairing, choose \(r=\min(a,N/2)\) nested pairs. Realize each chosen pair \(U\subset V\) on a distinct ternary coordinate by setting the coordinate of sample \(j\) to \(0\) if \(j\in U\), \(1\) if \(j\in V\setminus U\), and \(2\) otherwise. Thresholds at \(0\) and \(1\) realize \(U\) and \(V\). The \(N-2r\) remaining nonempty proper subsets are assigned individually to the remaining \(a-r\) ternary coordinates and the \(b\) binary coordinates. On an assigned ternary coordinate, use value \(0\) for members and value \(2\) elsewhere, and on an assigned binary coordinate use value \(0\) for members and value \(1\) elsewhere. There are enough coordinates because, for \(a\le N/2\), the inequality reduces to \(N-2a\le b\); for \(a>N/2\), all subsets have already been paired. Fill any unused coordinates with their maximal alphabet value. These points are distinct, since all singleton patterns occur, and they realize all \(2^s\) patterns. For \(s=2\), two distinct coordinates can realize the two singleton patterns; the constants give the other two. This proves the equality when \(k\ge2\), with the exceptional one-coordinate case explicitly handled.

**5. Sharp four-symbol boundary.** For two four-valued features, there are \(2+2(4-1)=8\) distinct hypotheses, so Part 1 gives online dimension \(3\). A feature's threshold traces form one chain under inclusion. Two chains cannot cover the three singleton subsets on a putative three-example shattered sample. Thus VC dimension is at most \(2\). Two coordinates realize two opposite singleton subsets, so VC dimension is exactly \(2\). This example proves that the binary–ternary equality has a genuine alphabet boundary.

## Verification

The standalone standard-library program `verify.py` is a supplemental finite test, not a replacement for the all-parameter argument. It reconstructs the explicit comparable-subset pairing for \(3\le s\le10\), builds and checks independently realizable shattered samples for several mixed palettes through \(s=6\), computes exact online dimensions by a recursive complete mistake-tree algorithm for selected grids, and exhaustively checks VC dimensions for selected grids. Run `python verify.py`; the observed output was `VERIFY_OK 67`. Its finite enumeration does not establish untested infinite parameter cases: those are established by Parts 1–5 above.

## Relationship to prior work

Funk, Jung and Voellmer (arXiv:2605.07452v1, first public 2026-05-08) study fitting expressive description-logic concepts including numeric feature comparisons. Their feature-comparison syntax explicitly includes \((f\leq v)\); they analyze Occam bounds and generalization in substantially larger concept languages, rather than the exact static/online shattering capacity of the one-atom, fixed-alphabet fragment here.

Gey (arXiv:1203.0193, originally 2012) gives the exact VC dimension for one-sided axis-parallel cuts on an unrestricted continuous domain, namely the largest \(s\) with \(\binom{s}{\lfloor s/2\rfloor}\le k\). This is not an exact finite-alphabet result: for example, six real-valued coordinates support four-point shattering, while six ternary coordinates in the present one-sided fragment have VC dimension three.

Leboeuf, LeBlanc and Marchand (arXiv:2210.10781v1, 2022), especially Section 5.2 and Theorem 9, give upper bounds on two-sided ordinal decision-stump partitioning functions, without proving their realizability in general; their analysis does not give the exact Littlestone law or the mixed binary–ternary one-sided criterion here. These sources provide foundational comparison results, not a claimed general independence or priority certificate.

## Limitations

The calculations rely on independent, fully populated ordinal feature coordinates. They do not extend as stated to correlated database attributes, absent feature values, only-positive-label hypotheses without the two constants, or to formulas with negations, conjunctions, role restrictions, or several comparisons. The four-symbol result is a boundary witness, not an all-alphabet VC classification. Historical priority is provisional because indexed search and the inspected primary sources cannot exclude every older equivalent statement under chain-covering or online-learning terminology. No independent review has been performed.

## References

1. Maurice Funk, Jean Christoph Jung and Tom Voellmer, *Bounded Fitting for Expressive Description Logics*, arXiv:2605.07452v1 (2026-05-08), https://arxiv.org/html/2605.07452v1.
2. Jean-Samuel Leboeuf, Frédéric LeBlanc and Mario Marchand, *Generalization Properties of Decision Trees on Real-valued and Categorical Features*, arXiv:2210.10781v1 (2022), Section 5.2 and Theorem 9, https://arxiv.org/pdf/2210.10781.
3. Servane Gey, *Vapnik-Chervonenkis Dimension of Axis-Parallel Cuts*, arXiv:1203.0193 (first circulated 2012), Section 3, https://arxiv.org/pdf/1203.0193.
