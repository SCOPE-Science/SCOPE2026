# Twelve habitat patches are sharp for two reversals of expected pair connectivity

## Finding

Consider a connected tree of habitat patches, each independently functional with a common probability \(p\in(0,1)\). Two distinct patches are counted as connected if they and every intermediate patch on their unique tree path remain functional. Let \(Z_T(p)\) be the number of unordered connected pairs among the functional patches and \(F_T(p)=\mathbb E[Z_T(p)]\).

**Theorem.** Among all pairs of trees with the same number \(n\) of patches, two strict reversals in the ranking of \(F_T(p)\) as \(p\) increases are impossible for \(n\le 11\), but occur for \(n=12\). Thus twelve is the least order at which two strict expected-pair-connectivity ranking reversals can occur. This is an onset result: it does not assert existence at each order above twelve.

For twelve patches labeled \(0,\ldots,11\), the following adjacency lists (unordered edges) define a witness:

\[
\begin{aligned}
E(A)=\{&(0,1),(0,7),(0,11),(1,2),(1,6),(2,3),\\
        &(2,5),(3,4),(7,8),(8,9),(8,10)\},\\
E(B)=\{&(0,1),(0,6),(0,10),(1,2),(2,3),(2,4),\\
        &(2,5),(6,7),(7,8),(7,9),(10,11)\}.
\end{aligned}
\]

Their expected connected-pair counts differ by

\[
F_A(p)-F_B(p)=p^3(p-1)(2p-1)(p^3+p^2-1).
\]

Therefore the ranking reverses exactly twice, at \(p=1/2\) and at the unique root \(r\in(1/2,1)\) of \(r^3+r^2-1=0\), namely \(r\approx0.7548776662\). The sign is negative for \(0<p<1/2\), positive for \(1/2<p<r\), and negative for \(r<p<1\).

## Assumptions and scope

The habitat network is a finite, undirected, simple, connected **tree** on \(n\) distinguishable equal-weight patches. Each patch is retained independently with common probability \(p\); there are no alternative routes outside the tree. Connectivity counts pairs of *distinct* retained patches, not singles, not expected resident population size, and not long-term species persistence. A ranking reversal means a strict sign change of the difference of two response curves at a point strictly inside \((0,1)\). Both trees in a comparison have the same patch count; arbitrary topologies and not just the displayed witness are allowed in the lower bound.

## Proof

Let \(d_T(u,v)\) be the unique tree-path length in edges and let \(a_j(T)\) count unordered vertex pairs at distance \(j\). A particular pair is connected after patch loss precisely when all \(d_T(u,v)+1\) vertices on its path survive. Independence gives

\[
F_T(p)=\sum_{\{u,v\}\subset V(T)}p^{d_T(u,v)+1}
      =\sum_{j=1}^{n-1}a_j(T)p^{j+1}.
\]

For equal-order trees, \(a_1(T)=n-1\) and \(\sum_j a_j(T)=\binom n2\). Consequently the difference \(D(p)=F_A(p)-F_B(p)\) is divisible by \(p^3(1-p)\). Set \(b_j=a_j(A)-a_j(B)\), with \(b_1=0\), and write \(D(p)/p^3=\sum_{k=0}^{n-3}b_{k+2}p^k\). For \(t>0\), define the integer polynomial

\[
G(t)=(1+t)^{n-3}\left(D\left(\frac{t}{1+t}\right)\Big/\left(\frac{t}{1+t}\right)^3\right).
\]

Its coefficient of \(t^j\) is precisely \(\sum_{k=0}^{j} b_{k+2}\binom{n-3-k}{j-k}\). The map \(p=t/(1+t)\) is a bijection from \((0,\infty)\) to \((0,1)\); \(D\) and \(G\) have exactly the same interior positive zeros and strict sign changes. Descartes' rule bounds the number of positive zeros by the number of coefficient sign variations of \(G\), after zeros are discarded.

The finite lower-bound certificate in `CHECK.py` generates *every* unlabeled tree through eleven vertices. It begins at the one-vertex tree; every larger tree has a leaf, so attaching a leaf at each vertex of every tree at the preceding size is surjective onto all shapes. Standard recursively sorted rooted-tree encodings at the one or two centers deduplicate exactly up to isomorphism. An independent breadth-first search yields every \(a_j\); equal distance profiles are grouped because they produce identical \(F_T\) responses. All transformed coefficient vectors and sign variations are computed in integer arithmetic, with no floating-point root decisions.

The exact counts of unlabeled tree shapes for sizes \(4,\ldots,11\) are \((2,3,6,11,23,47,106,235)\), giving respectively \((2,3,6,11,23,45,104,215)\) distinct distance profiles. Every pair of distinct profiles has at most one transformed sign variation except one pair at eleven vertices. For that pair, up to global sign,

\[
D(p)=p^3(p-1)(3p^3+p^2-3p+1).
\]

The cubic \(g(p)=3p^3+p^2-3p+1\) has discriminant \(-76<0\), hence exactly one real root; because \(g(-2)<0<g(0)\), its real root is negative. Thus it is strictly positive on \([0,1]\) and even this sole exceptional profile pair cannot reverse twice. The finitely enumerated domain therefore proves the universal lower bound for every \(n\le11\). Smaller sizes \(n\le3\) have only one tree shape per order.

For the twelve-vertex witness, breadth-first distance counting gives

\[
\begin{aligned}
(a_1(A),\ldots,a_7(A))&=(11,14,14,12,8,5,2),\\
(a_1(B),\ldots,a_7(B))&=(11,15,11,13,10,6,0),
\end{aligned}
\]

and all larger-distance counts vanish. Substituting them into the expectation formula gives the claimed factorization. The factor \(2p-1\) has one simple root at \(1/2\), and \(p^3+p^2-1\) is strictly increasing on \((0,1)\), negative at \(1/2\), positive at \(1\), and therefore has one distinct simple root there. The remaining factors are nonzero for \(0<p<1\). Exactly two strict reversals follow.

## Verification

Run `python3 CHECK.py` using Python 3 and no third-party modules. It exhaustively generates all unlabeled trees to order twelve; checks the numbers of tree shapes and distinct distance profiles; evaluates all distinct-profile pairs through eleven; isolates the unique possible two-variation exception; checks the rational witness distance counts, factorization and strict signs at \(p=1/4,2/3,9/10\).

Those exact witness differences are respectively \(-177/32768\), \(56/6561\), and \(-392931/12500000\). The analytic argument above, not floating-point grids or a runtime limit, supplies the sign-change count and establishes completeness of the finite enumeration.

## Relationship to prior work

Graph-based habitat connectivity and sensitivity to fragmentation are classical (Keitt, Urban and Milne, 1997; Saura, Bodin and Fortin, published online in 2013). The distance enumerator \(\sum_j a_j(T)p^j\) is the established Wiener/Hosoya polynomial; the identity \(F_T(p)=p\sum_j a_j(T)p^j\) is not claimed as a new polynomial or new connectivity model. Mowshowitz and Dehmer (2015) analyze Hosoya distance profiles and entropy. Brown, Oellermann and Mol (2018) explicitly recognize the Wiener polynomial as the expected pair connectivity under independent **edge** survival on trees, and study roots of *individual* Wiener polynomials, not positive roots of pairwise polynomial differences. Accordingly the vertex-loss expectation here is a simple known polynomial equivalence, not an independent new graph invariant or new reliability framework. Neither inspected article establishes the minimum twelve-vertex onset for two crossings of comparisons. The contribution here is the sharp twelve-patch onset and its exhaustive integer certificate in the stated ecological independent-patch-loss model.

## Limitations

This mathematical baseline assumes homogeneous independent patch loss, a tree-shaped landscape, equal patch weight, and perfect connectivity along a wholly surviving path. It does not prove behavior for weighted, cyclic, directed or correlated habitat networks, does not estimate actual ecological dispersal, and does not assert the phenomenon for every number of patches greater than twelve. The lower-bound certificate relies on the standard center-rooted canonical encoding and a finite, reproducible enumeration. Historical priority remains open to further independent review; a more comprehensive paper on Wiener-polynomial partial orders might contain equivalent results.

## References

- Keitt, T. H., Urban, D. L., and Milne, B. T. (1997). *Detecting critical scales in fragmented landscapes*. Conservation Ecology 1(1):4. https://doi.org/10.5751/ES-00015-010104 (publication year verified, precise first-public day not established).
- Saura, S., Bodin, Ö., and Fortin, M.-J. (2014; first published online 2013-10-01). *Stepping stones are crucial for species' long-distance dispersal and range expansion through habitat networks*. Journal of Applied Ecology 51:171–182. https://doi.org/10.1111/1365-2664.12179.
- Mowshowitz, A., and Dehmer, M. (2015; published 2015-03-05). *The Hosoya Entropy of a Graph*. Entropy 17:1054–1062. https://doi.org/10.3390/e17031054.
- Brown, J. I., Oellermann, O. R., and Mol, L. (2018; arXiv preprint 2018-01-11). *On the Roots of Wiener Polynomials of Graphs*. arXiv:1801.03985. https://arxiv.org/abs/1801.03985.
