# Rigidity and exact enumeration of minimum length-two single-insertion covering codes

## Finding

Let \(\Sigma\) be any finite alphabet of size \(q\ge2\). A set \(C\subseteq\Sigma^2\) is a *single-insertion cover* when every word in \(\Sigma^3\) has at least one length-two scattered subsequence belonging to \(C\). Then **every minimum-cardinality cover**, without any symmetry assumption, is
\[
C=A^2\cup B^2,\qquad \Sigma=A\mathbin{\dot\cup}B,\qquad \bigl||A|-|B|\bigr|\le1.
\]
Conversely every such balanced bipartition yields a minimum cover. In particular, every optimum is symmetric under coordinate reversal and the exact optimum cardinality, number of labeled optima, and number of optima up to relabeling are, respectively,
\[
\min|C|=\left\lceil\frac{q^2}{2}\right\rceil,\qquad
N_q=\frac{1}{1+\mathbf 1_{\{2\mid q\}}}\binom{q}{\lfloor q/2\rfloor},\qquad
\text{one orbit}.
\]
The full classification and enumeration, rather than the scalar cardinality, is the principal statement. The scalar bound and balanced construction already follow from earlier results [2].

## Assumptions and scope

The alphabet is a finite *set*, not necessarily a field, of integer cardinality \(q\ge2\). A scattered subsequence preserves the original coordinate order; multiple embeddings are not counted separately. Covering is for exactly one insertion from a length-two center to a length-three word. Codebooks are arbitrary subsets of \(\Sigma^2\), with ordered coordinate pairs allowed and **no** assumed closure under reversal. Labeled codebooks distinguish the alphabet symbols; unlabelled types are identified under permutations of \(\Sigma\).

## Proof

**1. Diagonal reduction.** The word \(aaa\) has only the length-two subsequence \(aa\), so any cover contains every diagonal pair \(aa\). Conversely any word of length three with at most two different symbols has two equal positions and therefore contains one of these compulsory pairs. The remaining constraints concern ordered triples \(abc\) of three distinct symbols: at least one of \(ab\), \(ac\), \(bc\) must belong to \(C\).

**2. Complement digraph.** Define a loopless directed graph \(D\) by including the ordered arc \(x\to y\) exactly when \(x\ne y\) and \(xy\notin C\). Such a digraph is feasible if and only if it contains no configuration of three distinct vertices with the three arcs \(a\to b\), \(a\to c\), and \(b\to c\). A pair of opposite arcs may both occur; in particular the digraph need not be oriented. Write \(E\) for its number of directed arcs. Since every diagonal pair belongs to a cover, \(|C|=q^2-E\).

**3. Sharp arc inequality.** For a vertex \(v\), write \(N^+(v)\), \(N^-(v)\) and \(d^+(v)\), \(d^-(v)\) for the out-/in-neighborhoods and degrees. Whenever \(u\to v\) is an arc, \(N^+(u)\cap N^+(v)=\varnothing\): a common out-neighbor would complete a forbidden triple. Likewise \(N^-(u)\cap N^-(v)=\varnothing\). Hence each arc satisfies
\[
d^+(u)+d^+(v)\le q,\qquad d^-(u)+d^-(v)\le q.\]
Summing over all arcs, with \(d(v)=d^+(v)+d^-(v)\), gives
\[
\sum_{v\in\Sigma}d(v)^2
=\sum_{u\to v}\bigl(d^+(u)+d^+(v)+d^-(u)+d^-(v)\bigr)
\le 2qE.
\]
Because \(\sum_vd(v)=2E\), Cauchy--Schwarz also gives \(\sum_vd(v)^2\ge4E^2/q\). Therefore \(E\le q^2/2\), and since \(E\) is an integer, \(E\le\lfloor q^2/2\rfloor\).

**4. Attainability.** Let \(A,B\) partition \(\Sigma\) with sizes as equal as possible, and take \(C=A^2\cup B^2\). Every three-symbol word has two positions from the same part, yielding a two-position subsequence in \(C\). The complementary digraph has every arc in both directions between \(A\) and \(B\), and none inside a part, so \(E=2|A||B|=\lfloor q^2/2\rfloor\). The resulting cover size is \(\lceil q^2/2\rceil\).

**5. Rigidity for even \(q\).** Suppose \(q=2m\) and \(C\) is minimum. Then \(E=q^2/2\), so both inequalities in Step 3 are equalities. In particular, for every arc \(u\to v\) we have \(d^+(u)+d^+(v)=q\) and \(N^+(u)\cap N^+(v)=\varnothing\), whence \(N^+(u)\cup N^+(v)=\Sigma\). Since \(u\notin N^+(u)\), it follows that \(u\in N^+(v)\); thus **every arc has its reverse**. Forgetting orientations now yields a simple undirected graph \(G\) with \(E/2=q^2/4\) edges. Any triangle in \(G\), because every edge is bidirected, would give a forbidden transitive triple in \(D\). Mantel's theorem, including its equality classification, implies that \(G\) is the balanced complete bipartite graph \(K_{m,m}\). Accordingly \(D\) is its bidirected version and \(C=A^2\cup B^2\).

**6. Rigidity for odd \(q\).** Suppose \(q=2m+1\) and \(C\) is minimum. Then \(E=(q^2-1)/2=2m(m+1)\). The average total degree is \(2E/q=q-1/q<q\), so there exists a vertex \(v\) with \(d(v)\le q-1=2m\). Removing \(v\) leaves \(2m\) vertices and \(E-d(v)\) arcs. The bound in Step 3 applies also to the induced graph, giving \(E-d(v)\le (2m)^2/2=2m^2\); hence \(d(v)\ge2m\). It follows that \(d(v)=2m\) and the graph on \(\Sigma\setminus\{v\}\) is an even-order extremizer. By Step 5 this induced graph is the bidirected complete bipartite graph on equal parts \(P,Q\), each of size \(m\).

The two neighborhoods \(N^+(v)\) and \(N^-(v)\) are each directed-edge-free in the induced graph, since an arc between two out-neighbors or between two in-neighbors completes a forbidden transitive triple with \(v\). Every directed-edge-free subset of the bidirected complete bipartite graph lies wholly in one part and has size at most \(m\). Since \(|N^+(v)|+|N^-(v)|=2m\), both neighborhoods have size exactly \(m\) and so each equals either \(P\) or \(Q\). They cannot be different parts: if \(N^+(v)=P\) and \(N^-(v)=Q\), then choosing \(p\in P\) and \(z\in Q\) yields the forbidden triple \(z\to v\to p\) with \(z\to p\). The other ordering is analogous. Thus both neighborhoods are the *same* part; \(v\) joins that part bidirectionally, producing the balanced bidirected complete bipartite graph \(K_{m,m+1}\). Hence \(C=A^2\cup B^2\), as claimed.

**7. Enumeration.** Each balanced unordered bipartition yields one distinct codebook: its two parts are exactly the two equivalence classes of the relation \(xy\in C\) on \(\Sigma\). If \(q\) is odd, selecting the smaller part gives \(\binom{q}{\lfloor q/2\rfloor}\) codes. If \(q\) is even, the two equal parts are unordered and the same binomial coefficient is divided by two. All balanced partitions are related by alphabet permutations, establishing one unlabelled type. This proves all assertions.

## Verification

The standalone standard-library Python program `checker.py` independently enumerates all loopless directed arc sets having the extremal candidate size \(\lfloor q^2/2\rfloor\) for \(q=2,3,4,5\). For each feasible graph it directly checks that the complementary code covers all length-three words, then checks that the complete set of minimizers matches the balanced bipartition construction and the exact labeled count. It returns `CHECKER_OK` on success. The printed optimum sizes are \(2,5,8,13\), and the numbers of labeled minimum codebooks are \(1,3,3,10\). These computations support the finite cases, but the full theorem rests on the proof above, especially the neighborhood double count and Mantel equality classification.

Run `python3 checker.py` in a directory containing this result and the checker; no third-party dependencies are required.

## Relationship to prior work

Xie, Sun and Ge [1], first publicly posted June 13, 2026, study insertion/deletion covering codes and new bounds, using as a key precursor Pikhurko, Verbitsky and Zhukovskii [2]. The latter prove an asymptotic optimal covering density of one half for length-two centers and exhibit the balanced two-part code; their Theorem 3 and nonasymptotic density implication already give the scalar lower bound \(\lceil q^2/2\rceil\) with the standard balanced construction. Thus **the minimum cardinality alone is not new**. Their discussion is an asymptotic-density and extremal-Turán argument; it does not assert that **every finite-alphabet optimum is necessarily symmetric** or enumerate all such codebooks. The finite classification here is the additional statement, obtained from the directed-arc equality conditions and the odd-alphabet deletion step. Lenz, Rashtchian, Siegel and Yaakobi [3] establish the general insertion/deletion covering-code framework, not the finite optimizer rigidity.

## Limitations

The theorem applies only to the one-insertion cover of length-three words by length-two codewords, including all alphabet sizes \(q\ge2\). It neither classifies covers larger than the optimum nor extends to longer centers or multiple insertions. This is a mathematical proof with finite reproducibility checks, not an independent external validation. Historical priority of the rigidity statement remains subject to discovery of earlier equivalent extremal directed-graph formulations.

## References

[1] C. Xie, Y. Sun and G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379, first posted June 13, 2026. https://arxiv.org/abs/2606.15379

[2] O. Pikhurko, O. Verbitsky and M. Zhukovskii, *New bounds for the optimal density of covering single-insertion codes via the Turán density*, IEEE Transactions on Information Theory 71 (2025), 4260–4266, DOI 10.1109/TIT.2025.3557393. Author-accessible full text: https://pikhurko.github.io/E/PikhurkoVerbitskyZhukovskii25tit.pdf

[3] A. Lenz, C. Rashtchian, P. H. Siegel and E. Yaakobi, *Covering Codes Using Insertions or Deletions*, IEEE Transactions on Information Theory 67 (2021), 3376–3388. https://cmrr-star.ucsd.edu/static/pubs/Covering_Codes_Using_Insertions_or_Deletions.pdf

[4] Mantel's classical triangle-free graph theorem with its balanced complete-bipartite equality case (used as a standard result in Step 5).
