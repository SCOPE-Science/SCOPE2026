# A sharp ten-vertex covariance boundary for two-block rooted-tree attachment

## Finding

Let \(B\) be a fixed finite rooted nonplane tree with \(t\ge2\) vertices. Make a new rooted tree by joining the root of a second, disjoint copy of \(B\) to a uniformly chosen vertex \(P\) of the first copy, keeping the first root as the global root. Write \(D\) for the depth of the newly attached root and \(L\) for the total number of leaves (outdegree-zero vertices) in the resulting tree.

For every \(B\), let \(i\) and \(\ell=t-i\) be its numbers of internal vertices and leaves, and let \(U\) and \(Q\) be the sums of the root depths over internal vertices and leaves, respectively. Then

\[
\operatorname{Cov}(D,L)=\frac{\ell U-iQ}{t^2}
\le\frac{i}{2t^2}\bigl(\ell(i-3)-2(i-1)\bigr).
\]

For every feasible pair \(i\ge1\), \(\ell\ge1\), equality is attained by exactly one rooted tree shape: a chain of \(i\) internal vertices, a leaf at the terminal internal vertex, and the other \(\ell-1\) leaves attached directly to the root. This includes the rooted star when \(i=1\). Thus the exact maximum over all rooted \(t\)-vertex blocks is

\[
C_t=\frac{1}{2t^2}\max_{1\le i\le t-1}
 i\left[(t-i)(i-3)-2(i-1)\right].
\]

The sign has a sharp cutoff:

\[
C_t<0\ (2\le t\le8),\qquad C_9=0,\qquad C_t>0\ (t\ge10).
\]

The unique zero-covariance shape at \(t=9\) has \(i=5\) internal vertices and \(\ell=4\) leaves. At \(t=10\), \(C_{10}=3/50\), uniquely attained by the same broom construction with \(i=6\), \(\ell=4\). Furthermore,

\[
\lim_{t\to\infty}\frac{C_t}{t}=\frac{2}{27},
\]

and every sequence of maximizing internal-vertex counts satisfies \(i/t\to2/3\).

## Assumptions and scope

The block is deterministic, rooted, unlabelled and unordered; attaching a second copy uses a new edge, not vertex identification. The parent vertex \(P\) is chosen uniformly over all \(t\) vertices of the first copy. Every copy of \(B\) has \(t\ge2\), so its root is internal and the new copy contributes exactly \(\ell\) leaves. Depth is the graph distance from the original root, and leaves are exactly vertices with zero children (not vertices of undirected degree one). All expectations are with respect to the single uniform attachment choice. No limit in the number of inserted blocks is asserted.

## Proof

**Exact covariance.** Let \(d(v)\) be the original root depth in \(B\), and \(J(v)\) its leaf indicator. The new root is one edge below \(P\); precisely one old leaf disappears if \(P\) was a leaf. Hence \(D=d(P)+1\) and \(L=2\ell-J(P)\). Uniformly sampling \(P\) gives

\[
\mathbb E[d(P)]=\frac{U+Q}{t},\quad
\mathbb E[J(P)]=\frac{\ell}{t},\quad
\mathbb E[d(P)J(P)]=\frac Q t.
\]

Therefore \(\operatorname{Cov}(D,L)=-\operatorname{Cov}(d(P),J(P))=(\ell U-iQ)/t^2\).

**Sharp extremal bound.** The internal vertices of any rooted tree form an ancestor-closed rooted subtree on \(i\) vertices. Its internal-depth sum \(U\) is at most \(0+1+\cdots+(i-1)=i(i-1)/2\): deleting terminal internal branches or using the bound that the \(j\)-th largest internal depth does not exceed \(j-1\) proves this directly. Equality is possible exactly when the internal vertices form a single rooted path.

The \(\ell\) edges incident to leaves contribute \(\ell\) to the sum \(Q\) of leaf depths. For each of the other \(i-1\) (internal) edges, at least one leaf is below that edge; therefore \(Q\ge\ell+i-1\). It follows that

\[
\ell U-iQ\le\ell\binom i2-i(\ell+i-1)
=\frac i2\bigl(\ell(i-3)-2(i-1)\bigr).
\]

Equality requires the internal subtree to be a path and every internal edge to have exactly one descendant leaf; thus there is one leaf below the terminal internal vertex, while all other leaves attach to the root. Conversely, this broom realizes both equalities. This establishes the bound and its uniqueness for each \((i,\ell)\). When \(i=1\), the sole tree is a rooted star and the same conclusion holds.

**Finite-order sign boundary.** The bracket in the sharp bound admits the identity

\[
(t-i)(i-3)-2(i-1)=(t-9)(i-3)-(i-5)^2.
\]

For \(i\le3\), the original expression is strictly negative. For \(i\ge4\) and \(t\le8\), the displayed expression is also strictly negative. At \(t=9\) it is zero if and only if \(i=5\). For every \(t\ge10\), choosing \(i=5\) makes the numerator \(5(t-9)>0\). At \(t=10\), evaluating the finitely many possible \(i\) gives the unique maximum \(\ell U-iQ=6\) at \(i=6\), so \(C_{10}=6/100=3/50\).

**Asymptotic envelope.** Uniformly for \(1\le i<t\), writing \(z=i/t\), the sharp bound divided by \(t\) equals \(z^2(1-z)/2+O(1/t)\). The continuous cubic has a unique maximum \(2/27\) at \(z=2/3\). Uniform approximation on the grid proves both the limiting value and convergence of the maximizing fractions.

## Verification

The standalone `checker.py` constructs all unordered rooted tree shapes with \(1\le t\le11\), including all \(1842\) shapes with eleven vertices. For each nontrivial shape it independently enumerates all parent positions with rational arithmetic and verifies the covariance identity and sharp fixed-\((i,\ell)\) bound. It checks the extremizers, the nine- and ten-vertex boundaries, and the broom construction for orders 10 through 100. Run with `python checker.py` using Python 3 and the standard library. These finite tests corroborate, rather than replace, the all-order proof.

## Relationship to prior work

Gopaladesikan, Mahmoud and Ward introduced random trees assembled from rooted blocks and studied the marginal leaf count, root depth of inserted blocks, total path length and height. Their leaf-update rule and attachment model are used here, but the mixed covariance and its sharp optimization over block shapes are not among the statements in the inspected primary text. Drmota and Hwang studied covariance of *level sizes* in ordinary random recursive trees and binary search trees; that object and distribution differ from the two-copy fixed-block statistic. Known tree leaf-status/extremal depth literature motivates caution about independent priority for the deterministic depth inequalities, which are not claimed separately as new results. The contribution claimed here is the combined sharp stochastic covariance cutoff and exact extremizer description, not novelty of the marginal recurrences or elementary depth sums.

## Limitations

This is a one-step, two-copy result for a deterministic block and a uniform parent. It makes no claim about later block insertions, nonuniform attachment, or the complete joint law. The sharp extremal bound is elementary, and a previously unnoticed derivation from general tree-status inequalities might overlap its deterministic portion. No independent audit or external validation is claimed.

## References

1. M. Gopaladesikan, H. Mahmoud, and M. D. Ward, *Building Random Trees from Blocks*, *Probability in the Engineering and Informational Sciences* 28 (2014), 67–81, first online November 19, 2013; DOI: https://doi.org/10.1017/S0269964813000338. Author-accessible full text: https://the-examples-book.com/personal/mdw/_attachments/paper024.pdf.
2. M. Drmota and H.-K. Hwang, *Profiles of random trees: correlation and width of random recursive trees and binary search trees*, *Advances in Applied Probability* 37 (2005), 321–341.
3. H. Guo and B. Zhou, *On extremal leaf status and internal status of trees*, arXiv:2008.00438 (background on related deterministic tree-status questions; not used for the proof).
