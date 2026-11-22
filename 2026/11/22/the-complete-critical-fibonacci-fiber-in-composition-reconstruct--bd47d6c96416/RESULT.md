# The complete critical Fibonacci fiber in composition reconstruction

## Finding

For each integer \(k\geq1\), let \(\mathcal C_m\) be the set of all finite ordered compositions of \(m\), and define the **set-valued** deletion observation
\[
\mathcal D_k(w)=\{u\in\mathcal C_{2k}:u\preceq w\},\qquad w\in\mathcal C_{3k},
\]
where \(u\preceq w\) means that \(u\) embeds componentwise into a subsequence of the parts of \(w\). Put
\[
\mathcal F_k=\{u\in\mathcal C_{2k}:\text{every part of }u\text{ is }1\text{ or }2\}.
\]
Then the **complete inverse fiber** of this observation is
\[
\boxed{\ \mathcal D_k^{-1}(\mathcal F_k)=\{(1,2)^i(2,1)^{k-i}:0\leq i\leq k\}\ },
\]
where concatenation and ordinary word powers denote ordered lists of composition parts. In particular, this natural extremal observation has exactly \(k+1\) different preimages, whereas \(|\mathcal F_k|=F_{2k+1}\) with \(F_1=F_2=1\). The assertion does **not** classify every other deletion-observation fiber or claim that this is the maximum fiber size.

## Assumptions and scope

All compositions have strictly positive integer parts and retain their left-to-right order. For \(u=(u_1,\ldots,u_s)\) and \(w=(w_1,\ldots,w_t)\), write \(u\preceq w\) when there exist \(1\leq j_1<\cdots<j_s\leq t\) with \(u_r\leq w_{j_r}\) for every \(r\). The requirement \(\sum u_r=2k\) ensures that such an embedding is equivalent to making exactly \(k\) unit deletions: decrease a part at least two by one, or erase a unit part. Repetitions in the observation are discarded. The parameter \(k\) ranges over all positive integers, not just tested small values.

## Proof

**Step 1: Every preimage has exactly \(k\) ones and \(k\) twos.** Assume first \(k\geq2\) and \(\mathcal D_k(w)=\mathcal F_k\). If a part \(t\geq3\) occurs in \(w\), choose
\[
s=\max\{3,t-k\}.
\]
Since \(3\leq t\leq3k\) and \(k\geq2\), we have \(3\leq s\leq\min(t,2k)\). The remaining parts have total weight \(3k-t\geq2k-s\geq0\); by successively lowering or removing parts they have a subcomposition of **every** nonnegative weight up to this total. Consequently \(w\) has a subcomposition of weight \(2k\) retaining a part equal to \(s\geq3\), contrary to \(\mathcal D_k(w)=\mathcal F_k\). Thus all parts of \(w\) lie in \(\{1,2\}\). If it contains \(t\) twos, its total number of parts is \(3k-t\). Because the observation contains both \((2)^k\) and \((1)^{2k}\), we have \(t\geq k\) and \(3k-t\geq2k\), hence \(t=k\), with precisely \(k\) unit parts. For \(k=1\), direct inspection of the four compositions of three gives precisely \((1,2)\) and \((2,1)\).

**Step 2: Two empty unit-gaps give an explicit missing read.** Write any remaining candidate uniquely as
\[
w=1^{a_0}2\,1^{a_1}2\cdots2\,1^{a_k},\qquad a_i\geq0,\quad\sum_{i=0}^{k}a_i=k.
\]
Suppose \(a_p=a_q=0\) for \(0\leq p<q\leq k\). The composition
\[
u_{p,q}=2^p1\,2^{q-p-1}1\,2^{k-q}
\]
has weight \(2k\), has \(k-1\) twos and two ones, and belongs to \(\mathcal F_k\). Any embedding must use \(k-1\) out of the source's \(k\) twos as the target twos, thus skipping exactly one source two. After the skip, the two target ones must occupy the source gaps at indices \(p\) and \(q-1\) among the retained twos (the indices coincide when \(q=p+1\)). A skipped two can fill or merge only the original two unit-gaps on its sides; it cannot simultaneously fill the separated empty gaps \(a_p,a_q\). If they are adjacent, omitting their separating two creates only a **single** available source symbol in the merged gap, while the target requires two. In all cases \(u_{p,q}\not\preceq w\), contradicting the hypothesis. Thus at most one of \(a_0,\ldots,a_k\) is zero. As these \(k+1\) nonnegative integers sum to \(k\), exactly one is zero and all others equal one. If the zero is at gap \(i\), the resulting composition is precisely \((1,2)^i(2,1)^{k-i}\), including the two boundary cases.

**Step 3: Every listed composition really realizes the entire observation.** Clearly no part above two can appear in a descendant of the listed compositions, so their decks are subsets of \(\mathcal F_k\). To prove the reverse inclusion, define \(d(v)\) for a word \(v\) on the ordered part alphabet \(\{1,2\}\) as the minimum total part sum of a nonempty \(\{1,2\}\)-word that does *not* embed componentwise into \(v\). Greedy leftmost embedding is optimal for this order. In particular
\[
d(\varnothing)=1,\quad d(2v)=1+d(v),\quad d(12v)=2+d(v),\quad d(21)=3.
\]
The identity for \(12v\) follows by considering the first absent target letter: a target beginning with one takes the initial \(1\), and a target beginning with two takes the following \(2\), giving in both cases the same minimum cost \(2+d(v)\). Similarly, a leading source \(2\) accepts either target letter, with weight one cheaper than two. For \(r\geq1\), these identities imply by induction
\[
d((21)^r)=2r+1:
\]
for \(r>1\), write \((21)^r=21(2z)\), use \(d(21(2z))=1+d(12z)=3+d(z)=2+d(2z)\), then induct. Repeatedly stripping initial \(12\) blocks yields
\[
d((12)^i(21)^{k-i})=2i+2(k-i)+1=2k+1.
\]
Thus every composition of total weight \(2k\) with parts at most two embeds into each listed source. Therefore the deck of every listed source is exactly \(\mathcal F_k\). Together with Steps 1 and 2 this establishes the claimed fiber equality for all \(k\geq1\).

The cardinality \(|\mathcal F_k|=F_{2k+1}\) is the standard two-part composition recurrence: the number of compositions of \(m\) into ones and twos satisfies \(f_m=f_{m-1}+f_{m-2}\), with \(f_0=f_1=1\), so \(f_{2k}=F_{2k+1}\).

## Verification

Run the standalone standard-library program `python3 check.py`. It forms the literal full deletion sets of all \(2^{3k-1}\) compositions of \(3k\), for \(1\leq k\leq5\), independently confirming that the specified fiber has respective cardinalities \(2,3,4,5,6\). It also computes the shortest missing weight for every prescribed source through \(k=13\), and checks the explicit two-zero obstruction against every balanced nonfamily source through \(k=8\). Output ends with `VERIFY_OK`. Finite checks are supporting reproducibility only; the preceding argument establishes the infinite theorem.

## Relationship to prior work

Raykova (2006) introduced the layered-permutation reconstruction setting and studied sets and multisets of deletion minors. Vatter (arXiv version dated October 16, 2006; later journal 2008) proved the sharp general threshold \(n\geq3k+1\) for recovery from the set of \(k\)-deletions of compositions and explicitly observed that \((1,2)^k\) and \((2,1)^k\) have the same deck \(\mathcal F_k\). The present theorem credits that existence example and determines its **entire** inverse fiber, including the \(k-1\) intermediate compositions, using a two-empty-gap obstruction and a weighted shortest-missing-subsequence calculation. Neither the published threshold statement nor the cited pair equality alone specifies this complete fiber.

A separately posted classification of edges in a *two-common-one-deletion-read* graph for layered permutations addresses an overlap criterion, not equality of complete \(k\)-deletion sets. The graph relation is strictly weaker and does not imply the present fiber equality. The present theorem makes no claim about multiset decks.

## Limitations

This is one explicitly specified inverse fiber at the tight reconstruction boundary, not a classification of all nonreconstructible pairs of compositions of \(3k\) or proof of a global maximum list size. The proof uses set observations and would not apply unchanged to multiplicity-preserving observations. Similar all-length complete-fiber formulas might exist in unindexed or differently framed literature; the priority assessment is provisional pending broader expert review. No independent audit has been performed.

## References

1. M. Raykova, *Permutation Reconstruction from Minors*, Electronic Journal of Combinatorics 13 (2006), #R66, published August 3, 2006. https://www.cs.columbia.edu/~mariana/papers/perm_reconstruct.pdf
2. V. Vatter, *Reconstructing Compositions*, first arXiv submission October 16, 2006, arXiv:math/0610477; Discrete Mathematics 308 (2008), 1524–1530. https://arxiv.org/abs/math/0610477
3. Prior posted scientific note on two-common-minor edges of layered permutations (distinct observation model), identifier `4137b273-33a1-4c3d-a664-c0469228518d`.
