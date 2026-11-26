# Exact Littlestone dimension of closed radius-two Hamming-ball concepts

## Finding

Let \(Q_d=\{0,1\}^d\), with Hamming distance \(\operatorname{dist}(x,c)\), and let \(\mathcal B_{d,2}\) be the concept class on domain \(Q_d\) consisting of all labelled closed radius-two balls:
\[
\mathcal B_{d,2}=\{x\mapsto\mathbf 1[\operatorname{dist}(x,c)\le 2]:c\in Q_d\}.
\]
For every integer \(d\ge1\), the Littlestone dimension of this concept class is exactly
\[
\operatorname{Ldim}(\mathcal B_{d,2})=\begin{cases}
0,&d=1,2,\\
1,&d=3,\\
3,&d=4,\\
4,&d=5,\\
5,&d\ge6.
\end{cases}
\]
Thus the optimal worst-case number of mistakes for deterministic realizable online learning from this class is at most five in every dimension, with five necessary from dimension six onward.

## Assumptions and scope

All sets, points, centres and queries are finite. Identify \(Q_d\) with subsets of \([d]\), write \(u\triangle v\) for symmetric difference, and set \(B_2(u)=\{v:|u\triangle v|\le2\}\). A complete Littlestone tree of depth \(r\) is a binary tree with \(r\) query nodes on every root-to-leaf path, each path's zero/one labels simultaneously realizable by some center. Its maximum possible depth is \(\operatorname{Ldim}\). Repeated queries are permitted by the definition but cannot occur on a successfully shattered path with incompatible labels. No distributional or asymptotic assumptions are needed.

## Proof

**Lemma 1 (centred small star).** For a fixed centre \(t\) and an index set \(J\subseteq[d]\), let \(R(t,J)=\{t\}\cup\{t\triangle\{j\}:j\in J\}\). Every subfamily of centres contained in \(R(t,J)\) has Littlestone dimension at most two, with radius-two-ball query labels.

*Proof.* Translate \(t\) to \(\varnothing\) and let a query have support \(W\). If \(|W|\le1\), every available star centre answers positively. If \(|W|=2\), the centre \(\varnothing\) and at most two singleton centres answer positively. If \(|W|=3\), at most three singleton centres answer positively and \(\varnothing\) answers negatively. If \(|W|\ge4\), every answer is negative. Thus any query that genuinely splits the star has a positive child containing at most three hypotheses. Such a child has Littlestone dimension at most one by the elementary leaf bound: a depth-two shattered tree needs four distinct consistent hypotheses. Hence a depth-three shattered tree cannot exist in the star. This also applies to every subset. \(\square\)

**Lemma 2 (one-coordinate double-ball intersection).** Let \(P=B_2(\varnothing)\), and let \(A=P\cap B_2(\{1\})\), assuming the corresponding coordinates exist. Then \(\operatorname{Ldim}(A)\le3\).

*Proof.* Exactly the following centres occur:
\[
A=\{\varnothing,\{1\}\}\cup\{\{i\},\{1,i\}:2\le i\le d\}.
\]
Queries \(\varnothing\) and \(\{1\}\) have no negative branch. For a query \(\{j\}\) with \(j\ne1\), its negative branch is \(\{\{1,i\}:i\ne1,j\}\), a subset of a translated star. For a query \(\{1,j\}\) with \(j\ne1\), the negative branch is \(\{\{i\}:i\ne1,j\}\), another star subset. A direct support-count for every other query gives at most five positive centres: if the query has two elements and omits 1, or has three and contains 1, the maximum is five; all remaining cases give at most three positive centres (or no genuine split). Indeed only the supports of cardinalities at most four can meet any centre of \(A\) within distance two. A five-element family has Littlestone dimension at most two. By Lemma 1 the exceptional negative branches also have dimension at most two. Hence no root split of \(A\) can have both children of dimension at least three, so \(\operatorname{Ldim}(A)\le3\). \(\square\)

**Lemma 3 (two-coordinate double-ball intersection).** With \(P\) as above, let \(B=P\cap B_2(\{1,2\})\). Then \(\operatorname{Ldim}(B)\le3\).

*Proof.* Its centres are
\[
B=\{\varnothing,\{1\},\{2\},\{1,2\}\}\cup\{\{1,i\},\{2,i\}:3\le i\le d\}.
\]
Queries \(\varnothing\) and \(\{1,2\}\) answer positively at every centre. For \(\{1\}\) and \(\{2\}\), the negative branches consist of doubletons \(\{2,i\}\) and \(\{1,i\}\), respectively, each a star subset. For \(\{1,j\}\) with \(j\ge3\), its negative branch is \(\{\{2\}\}\cup\{\{2,i\}:3\le i\le d,\ i\ne j\}\), and the symmetric case applies to \(\{2,j\}\). These are translated stars. Every other query meets at most five members of \(B\) within distance two: singleton queries outside \(\{1,2\}\) give five; outsider pairs give five; queries comprising both distinguished coordinates and one or two outsiders give five; the other supports give at most three. Lemma 1 and the five-hypothesis leaf bound establish that every genuine split has a child of dimension at most two. Therefore \(\operatorname{Ldim}(B)\le3\). \(\square\)

**Lemma 4 (a full ball has dimension at most four).** For every \(d\), \(\operatorname{Ldim}(P)\le4\).

*Proof.* Consider a query \(z\). If \(|z|=0\), all centres in \(P\) answer positively. If \(|z|=1\) or two, the positive branch is a coordinate permutation of the family in Lemma 2 or Lemma 3 and has dimension at most three. If \(|z|=3\), the positive branch contains precisely the three singleton and three doubleton subsets of \(z\); if \(|z|=4\), it contains precisely the six doubleton subsets of \(z\). Either family has only six hypotheses and hence dimension at most two. If \(|z|>4\), the positive branch is empty. Thus no query can give two children both of Littlestone dimension at least four, ruling out a depth-five tree. \(\square\)

**All-dimensional upper bound.** At the root of a shattered tree for \(\mathcal B_{d,2}\), a query \(z\) has a positive child consisting of centres in \(B_2(z)\), a translate of \(P\). Lemma 4 bounds this child's Littlestone dimension by four, proving \(\operatorname{Ldim}(\mathcal B_{d,2})\le5\).

**Sharper small-dimensional upper bounds.** For \(d=1,2\), every radius-two ball is all of \(Q_d\), so the dimension is zero. For \(d=3\), the negative branch of every query has just one centre (the antipode), ruling out shattered depth two. For \(d=4\), the negative branch of any root query has \(2^4-(1+4+\binom42)=5\) centres, fewer than the eight required for depth three; therefore total depth four is impossible. For \(d=5\), the positive branch of any root has exactly sixteen centres. To contain a depth-four shattered subtree, it would need an internal query partitioning those sixteen centres into two sets of at least eight. But the intersection cardinalities \(|B_2(\varnothing)\cap B_2(z)|\) for \(|z|=0,1,2,3,4,5\) are respectively \(16,10,10,6,6,0\); none yields an eight/eight split. Thus depth five is impossible when \(d=5\).

**Constructive lower bounds.** The supplementary `witnesses.json` lists a complete labelled decision tree with a consistent centre at every leaf in each of the cases \((d,r)=(3,1),(4,3),(5,4),(6,5)\). The separate `verify.py` checks each labelled path by direct Hamming-distance computation. Their existence gives all four lower bounds. Padding every query and centre by zero coordinates preserves every distance and produces an equally deep tree in every larger dimension. Combined with the upper bounds, the displayed formula follows. \(\square\)

## Verification

Run `python3 verify.py` in the folder containing `verify.py` and `witnesses.json`. The script independently checks the labelled paths of four complete witness trees (two, eight, sixteen and thirty-two leaves), checks the exact recursive Littlestone dimension for all \(1\le d\le6\), and corroborates the double-ball-branch structural classification for \(5\le d\le8\). `verification_output.txt` records the observed successful checks. The all-dimensional assertions depend on the preceding arguments, not on finite enumeration.

## Relationship to prior work

Adler, Benediktsson and Macpherson analyze Vapnik–Chervonenkis dimensions and densities for Hamming and Johnson adjacency structures (arXiv:2007.16042). Their graph-neighbourhood VC bounds neither calculate nor imply the online mistake-tree dimension of closed radius-two hypercube balls. Malliaris and Moran link Littlestone dimension and model-theoretic stability (arXiv:2108.05569) but do not specialize that theory to this exact metric class. Chase, Freitag and Reyzin study general Littlestone-based query learning and compression (arXiv:2310.04812), not this precise finite-dimensional threshold. In other published work, the expression “\(r\)-Hamming balls” sometimes denotes **hypothesis families** of binary functions differing from one fixed function on at most \(r\) domain points; this is not the present class of **metric-ball indicator functions** on \(Q_d\).

## Limitations

The result concerns binary Hamming cubes, closed radius exactly two, unrestricted centre and query positions and realizable online learning. It does not assert analogous formulas for higher radii, nonbinary alphabets, probabilistic mistake bounds or noisy labels. The finite checking code does not certify the infinite case by itself. An independent scientific audit and definitive global publication-priority check have not been performed.

## References

- Adler, H., Benediktsson, S. S., and Macpherson, D. M., *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, first publicly posted 2020-07-31. https://arxiv.org/abs/2007.16042
- Malliaris, M. and Moran, S., *Agnostic Online Learning and Excellent Sets* (subsequently *Model Theory and Agnostic Online Learning via Excellent Sets*), arXiv:2108.05569, first publicly posted 2021-08-12. https://arxiv.org/abs/2108.05569
- Chase, Z., Freitag, J., and Reyzin, L., *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812, first publicly posted 2023-10-07. https://arxiv.org/abs/2310.04812
