# Global coalition numbers of complete tripartite graphs
## Finding
Let \(G=K_{a,b,c}\) be a finite complete tripartite graph with \(a\ge b\ge c\ge1\) and \(N=a+b+c\). For the global coalition number \(GC(G)\),
\[GC(K_{a,b,c})=\begin{cases}a+1,&c=1,\\N-2,&c=2,\\N-3,&c\ge3.\end{cases}\]
Moreover, a vertex set of \(K_{a,b,c}\) is globally dominating if and only if it meets all three partite sets. Thus global-coalition partners are governed exactly by union of part-supports, and the displayed formula resolves the complete tripartite case beyond the previously available complete-multipartite lower bound \(GC(K_{n_1,\ldots,n_m})\ge n_1+n_m\).

The three regimes are attained by explicit global-coalition partitions. When \(c=1\), put the unique vertex of the smallest part together with all vertices of the middle part and leave every vertex of the largest part singleton. When \(c=2\), use one \(A C\)-block and one \(B C\)-block, each of size two, and leave all remaining vertices singleton. When \(c\ge3\), use one two-vertex block of each support type \(A B\), \(A C\), and \(B C\), and leave all remaining vertices singleton.

## Assumptions and scope
The graph is finite, simple, connected, and complete tripartite with nonempty partite sets \(A,B,C\) of cardinalities \(a,b,c\), ordered so that \(a\ge b\ge c\ge1\). A global dominating set dominates both the graph and its complement. A global coalition is a pair of disjoint sets that are individually not global dominating but whose union is global dominating. A global-coalition partition is a vertex partition in which every block is not global dominating and has a coalition partner among the other blocks. The global coalition number \(GC(G)\) is the maximum number of blocks in such a partition.

## Proof
First characterize global domination. In the complement of a complete tripartite graph, the three partite sets induce three disjoint cliques. Hence a set \(S\) dominates the complement only if it meets every partite set; conversely, if \(S\) meets all three parts, then it dominates the complement, and it also dominates the original complete tripartite graph because every omitted vertex has a selected neighbor outside its own part. Therefore \(S\) is globally dominating if and only if its support contains all three partite classes.

It follows that every block in a global-coalition partition has a proper nonempty support among \(\{A,B,C\}\), and two blocks are coalition partners exactly when the union of their supports is \(\{A,B,C\}\).

Let \(\Pi\) be a global-coalition partition and define its defect by
\[d=N-|\Pi|=\sum_{X\in\Pi}(|X|-1).\]
Thus each nonsingleton block contributes at least one unit of defect.

If \(c=1\), let \(z\) be the unique vertex of \(C\) and let \(Z\) be its block. Since \(Z\) is not global dominating, it misses at least one of \(A\) and \(B\), say \(P\). Every other block must have a partner containing \(C\), and \(Z\) is the unique such block, so every other block must meet \(P\). Disjointness therefore gives \(|\Pi|-1\le |P|\le a\), hence \(|\Pi|\le a+1\). Equality is attained by the partition consisting of \(B\cup\{z\}\) and all \(a\) singleton vertices of \(A\).

If \(c=2\), suppose for contradiction that \(d\le1\). Then there is at most one nonsingleton block. Singleton blocks cannot occur in two different partite sets: a single nonsingleton partner would then have to contain the other two parts for each singleton type and hence meet all three parts, which would make it globally dominating. Thus singleton blocks occur in at most one part, so all vertices of the other two parts lie in the unique nonsingleton block. Since both of those parts have size at least two, that block has size at least four and contributes defect at least three, a contradiction. Hence \(d\ge2\), so \(|\Pi|\le N-2\). For equality, choose \(a_1\in A\), \(b_1\in B\), and write \(C=\{c_1,c_2\}\). Use the blocks \(\{a_1,c_1\}\) and \(\{b_1,c_2\}\), leaving every other vertex singleton. Because \(a,b\ge2\), each mixed block has a singleton partner from its missing part, while each singleton has the complementary mixed block as a partner.

Now assume \(c\ge3\). We show \(d\ge3\). First note that if a part \(P\) of size at least three contains no singleton block, then already \(d\ge3\). Indeed, if all vertices of \(P\) lie in one block, then a pure \(P\)-block has defect at least two and needs a mixed partner of defect at least one, while a mixed block containing all of \(P\) has size at least four and defect at least three. If the vertices of \(P\) lie in at least two nonsingleton blocks, then under \(d\le2\) there can be exactly two such blocks; one contains at least two vertices of \(P\). If that block is mixed it contributes defect at least two and the other contributes at least one. If it is pure, it needs a partner meeting both other parts, which cannot be the other \(P\)-containing nonglobal block, so a third nonsingleton block is necessary. Each case contradicts \(d\le2\).

Therefore, under a hypothetical \(d\le2\), every one of \(A,B,C\) has a singleton block. An \(A\)-singleton needs a block of support \(B C\); a \(B\)-singleton needs support \(A C\); and a \(C\)-singleton needs support \(A B\). These are three distinct nonsingleton blocks, so \(d\ge3\), again a contradiction. Hence \(|\Pi|\le N-3\). Equality follows by choosing two-vertex blocks of the three support types \(A B\), \(A C\), and \(B C\), using distinct vertices, and leaving all other vertices singleton; \(a,b,c\ge3\) ensures that a singleton remains in each part to partner the complementary mixed block.

Combining the three cases proves the formula.

## Verification
The proof above is analytic for all positive integer triples in the stated order. As a finite corroboration, `verify.py` enumerates every set partition for every sorted tripartite profile of order from \(3\) through \(10\), checks the global-coalition condition directly from the definition, and compares the exact maximum with the theorem. Running the packaged verifier prints:

`ALL CHECKS PASSED; profiles=31; orders=3..10`

The finite computation is not used as a proof of the infinite statement.

## Relationship to prior work
The defining 2025 preprint introduces global coalitions and the global coalition number. Its inspected first public version gives \(GC(K_n)=2\), \(GC(K_{n,m})=n+m\), and, for complete multipartite graphs with ordered part sizes, the lower bound \(GC(K_{n_1,\ldots,n_m})\ge n_1+n_m\). The present theorem resolves the first multipartite level beyond complete bipartite graphs. When \(c=1\), the earlier lower bound is sharp; when \(c=2\), the exact value is \(N-2=a+b\); and when \(c\ge3\), it is \(N-3\).

Targeted searches for global-coalition, complete-tripartite, complete-multipartite, and support-equivalent formulations did not locate an exact tripartite theorem. The closest indexed complete-multipartite records found in the same searches concern different invariants, such as global offensive alliances, and do not imply this result.

## Limitations
The theorem concerns complete tripartite graphs only; it does not give the global coalition number for arbitrary complete multipartite graphs with four or more parts. The finite verifier checks only orders at most \(10\) and is corroborative, not exhaustive evidence for the infinite theorem.

The current arXiv record for the defining preprint is withdrawn, with the withdrawal note referring to problems in a later revision. This result uses only the definitions and lower-bound context read in version 1 and independently proves every claim used here. A poorly indexed equivalent theorem under different coalition terminology remains a residual literature risk. A conference abstract appears to predate the arXiv posting, but its online publication date was not independently established; the source date recorded here is therefore the earliest public date that was verified directly.

## References
1. A. Besharati, M. A. Mojdeh, and P. Samadzadeh, *Global coalition sets in graphs*, arXiv:2509.15386v1, first public 2025-09-18. The inspected version lists 2020 MSC 05C69.
