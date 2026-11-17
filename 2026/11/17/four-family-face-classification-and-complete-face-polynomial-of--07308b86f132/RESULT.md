# Four-family face classification and complete face polynomial of bipartite symmetric edge polytopes

## Finding

Let \(p,q\geq 2\) be integers and write \(A=[p]\), \(B=[q]\). In the zero-sum hyperplane of \(\mathbb R^{p+q}\), define the complete-bipartite symmetric edge polytope
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_{p+j}):i\in A,\ j\in B\}.
\]
It has dimension \(p+q-1\). All of its nonempty proper faces admit the following four disjoint, exhaustive descriptions by their **actual vertex sets**. Write \(r_{ij}=e_i-e_{p+j}\).

**Type I: one orientation.** For nonempty \(S\subseteq A\), \(T\subseteq B\), and \(\epsilon\in\{+1,-1\}\), take the convex hull of \(\{\epsilon r_{ij}:i\in S,j\in T\}\). It is a product of simplices of dimension \(|S|+|T|-2\).

**Type II: split on both parts.** Choose ordered disjoint nonempty \(S_+,S_-\subseteq A\) and ordered disjoint nonempty \(T_+,T_-\subseteq B\). The face has vertices \(\{r_{ij}:i\in S_+,j\in T_-\}\cup\{-r_{ij}:i\in S_-,j\in T_+\}\). It is a join of the two corresponding products of simplices and has dimension \(|S_+|+|S_-|+|T_+|+|T_-|-3\).

**Type III: first part constant.** Choose ordered disjoint nonempty \(T_+,T_-\subseteq B\). The face has vertices \(\{r_{ij}:i\in A,j\in T_-\}\cup\{-r_{ij}:i\in A,j\in T_+\}\), of dimension \(p+|T_+|+|T_-|-2\).

**Type IV: second part constant.** Choose ordered disjoint nonempty \(S_+,S_-\subseteq A\). The face has vertices \(\{r_{ij}:i\in S_+,j\in B\}\cup\{-r_{ij}:i\in S_-,j\in B\}\), of dimension \(q+|S_+|+|S_-|-2\).

These indexed vertex sets, ordered by containment and with the empty face and whole polytope adjoined, give the **complete face lattice**, not merely its rank numbers. Set
\[
U_r(t)=(1+t)^r-1,\qquad T_r(t)=(1+2t)^r-2(1+t)^r+1.
\]
Then the entire proper-face generating polynomial is
\[
\boxed{\sum_{k=0}^{p+q-2}f_k(P_{p,q})t^k
 =\frac{2U_p(t)U_q(t)}{t^2}
 +\frac{T_p(t)T_q(t)}{t^3}
 +t^{p-2}T_q(t)+t^{q-2}T_p(t).}
\]
All displayed quotients are polynomials. In particular, the formula recovers the known face counts \(f_0=2pq\), \(f_1=pq(pq-1)\), and \(f_{p+q-2}=2^p+2^q-2\), while specifying every previously unaddressed intermediate rank.

As a two-dimensional consistency consequence, all two-faces are triangles or quadrilaterals. Writing \(\binom rs=0\) for \(s>r\), the respective counts are
\[
N_3=2\left(p\binom q3+q\binom p3\right)
+12\left(\binom p2\binom q3+\binom p3\binom q2\right),
\]
\[
N_4=2\binom p2\binom q2
 +\mathbf1_{p=2}q(q-1)+\mathbf1_{q=2}p(p-1).
\]
The low-rank conclusions connect to existing edge and triangular-face criteria; novelty is asserted only for the full four-family rankwise classification and its closed all-rank formula, subject to the literature limitations below.

## Assumptions and scope

Only the Euclidean real convex hull of the explicitly given root vectors is considered, with labeled graph vertices. Every \(p,q\ge2\) is included, including the borderline square \(p=q=2\). Faces mean nonempty proper exposed faces (equivalently nonempty proper faces of a finite polytope); rank \(k\) is affine dimension \(k\). There is no assertion about graph families other than complete bipartite graphs, weighted root sets, lattice-point enumeration, or generic sections.

## Proof

**1. Exact exposed vertex sets.** For a linear supporting functional choose potentials \(h_i\) on \(A\) and \(g_j\) on \(B\). Put \(H_+=\max h_i\), \(H_-=\min h_i\), \(G_+=\max g_j\), \(G_-=\min g_j\). Since \(0\) lies in the relative interior, every proper supporting face has positive support height. The greatest value on a forward vertex is \(M=H_+-G_-\); on a reversed vertex it is \(N=G_+-H_-\). When \(M>N\), precisely the root vertices indexed by the maximum set of \(h\) and minimum set of \(g\) are exposed: Type I. When \(N>M\), Type I with opposite sign follows.

**2. Both signs exposed.** If \(M=N>0\), then \(H_++H_-=G_++G_-\). Subtracting their common midpoint from all potentials makes their ranges \([-a,a]\) and \([-b,b]\) for some \(a,b\ge0\), with \(a+b>0\). If \(a,b>0\), the maxima/minima on each part are disjoint nonempty sets. The forward maxima are the Cartesian rectangle \(S_+\times T_-\), and reverse maxima are \(S_-\times T_+\), giving Type II. If \(a=0\), every first-part index is simultaneously maximal and minimal, giving Type III. If \(b=0\), similarly Type IV. These cases exhaust all possible faces.

**3. Every listed index configuration occurs.** For Type I, put \(h=1\) on \(S\), \(h=0\) outside \(S\), \(g=0\) on \(T\), and \(g=1/3\) outside \(T\); the desired forward roots are the unique maximizers (negate all potentials for the reversed version). For Type II, put \(h=1\) on \(S_+\), \(-1\) on \(S_-\), and \(0\) elsewhere; likewise \(g=1\) on \(T_+\), \(-1\) on \(T_-\), \(0\) elsewhere. For Type III put \(h=0\) on all of \(A\) and \(g=\pm1\) on \(T_\pm\), with \(0\) elsewhere. Type IV is symmetric. Since different listed data yield distinct signed root vertex sets, the enumeration has no duplication. The face lattice is therefore determined by inclusion of these sets.

**4. Affine dimensions.** A Type I face is \(\Delta_{|S|-1}\times\Delta_{|T|-1}\). In Type II the two oriented products occupy disjoint coordinate supports in both parts; their affine hulls join without intersection, so the affine dimension is the sum of their dimensions plus one: \((|S_+|+|T_-|-2)+(|S_-|+|T_+|-2)+1\). In Type III the two components have the same \((p-1)\)-dimensional first-part difference space, disjoint \((|T_-|-1)\)- and \((|T_+|-1)\)-dimensional second-part difference spaces, and one further independent direction joining their affine hulls. Therefore the dimension is \((p-1)+(|T_-|-1)+(|T_+|-1)+1=p+|T_+|+|T_-|-2\). Type IV follows by swapping the parts. In each case the count remains valid when a subset is a singleton, with its internal difference space dimension zero.

**5. Enumerate by dimension.** A nonempty subset of an \(r\)-element set of size \(s\) is encoded with weight \(t^s\) by \(U_r(t)\). Ordered disjoint nonempty pairs of subsets with total size \(s\) are encoded by \(T_r(t)\): assigning each element to the first subset, the second subset, or neither yields \((1+2t)^r\); inclusion-exclusion removes each missing category to give \(T_r(t)=(1+2t)^r-2(1+t)^r+1\). The four dimensions in Steps 1–4 now give, respectively, \(2U_pU_q/t^2\), \(T_pT_q/t^3\), \(t^{p-2}T_q\), and \(t^{q-2}T_p\). Adding these **disjoint exhaustive** counts yields the boxed polynomial. Both \(U_r\) and \(T_r\) have zero constant term, while \(T_r\) also has zero linear term, so every quotient is polynomial.

**6. Face benchmarks and two-face shapes.** The constant term is \(2pq\). The coefficient of \(t\) simplifies to \(pq(pq-1)\). The coefficient of \(t^{p+q-2}\) receives two Type I faces (one full Cartesian product for each sign) and \(2^q-2\) Type III plus \(2^p-2\) Type IV faces, for a total of \(2^q+2^p-2\). Two-dimensional Type I products are triangles (sizes \((1,3)\) or \((3,1)\)) or quadrilaterals \((2,2)\); Type II has three vertices at this rank; Types III and IV can contribute two-dimensional quadrilaterals only when the constant part has size two. Counting the corresponding ordered labels gives \(N_3\) and \(N_4\). This finishes the proof for all integer parameters.

## Verification

The reproducible script `verification/verify_bipartite_faces.py` builds the actual \(2pq\) roots in an intrinsic \((p+q-1)\)-coordinate chart, constructs supporting facets using a convex-hull algorithm, closes them under set intersection to enumerate **all** faces, measures affine ranks independently, and checks them against the formula. It additionally checks that every dimension-two face has three or four vertices and that triangular/quadrilateral counts match their closed forms. The eight pairs \((p,q)\in\{(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)\}\) pass 75 aggregate exact-integer comparisons after numerical facet/rank recovery. Selected full face vectors are \((8,12,6)\) for \((2,2)\), \((18,72,102,60,14)\) for \((3,3)\), and \((32,240,712,1024,752,260,30)\) for \((4,4)\). The script's floating-point convex-hull reconstruction is finite numerical corroboration; the proof in Steps 1–6 is independent and exact for all parameters.

## Relationship to prior work

Higashitani–Jochemko–Michałek, *Arithmetic aspects of symmetric edge polytopes* (arXiv:1807.07678), Proposition 3.4 and Example 3.6, already classify and count facets of complete-bipartite symmetric edge polytopes; their full paper also proves an \(h^*\)-formula for these polytopes. The present formula reduces to their facet count but counts **faces at every rank** and reconstructs the entire lattice from vertex data. An \(h^*\)-polynomial is not the ordinary \(f\)-polynomial of a nonsimplicial polytope, and the earlier facet characterization alone does not provide the displayed enumerations at intermediate ranks. Chen–Davis–Korchevskaia (arXiv:2107.12315, Theorem 3) gives a graph-theoretic correspondence between connected face subgraphs and maximal bipartite subgraphs in their induced graphs; its full text does not enumerate all four vertex-indexed face families or their ranks for complete bipartite graphs.

D'Alì–Delucchi–Michałek, *Many Faces of Symmetric Edge Polytopes* (arXiv:1910.05193), gives full face-vector results for other graph families including even cycles, not the four-family classification here. Higashitani–Mori, *Minkowski decomposability of symmetric edge polytopes* (arXiv:2608.02445, first publicly available 2026-08-03), establishes a Minkowski-decomposability classification and a general triangular-face criterion. That work's decomposability results do not determine a full \(f\)-polynomial for \(K_{p,q}\), particularly when both part sizes exceed two, and the present result credits its triangular-face criterion. Existing one-skeleton, facet, and Ehrhart statements are not claimed as original here.

## Limitations

Historical priority is provisional: the accessible primary papers and record searches did not identify a duplicate full all-rank formula, but this cannot exclude equivalent earlier work under different terminology. The 2026 motivating paper's browser-accessible full text was inspected, while its PDF could not be retrieved; the relevant comparisons are limited to that accessible manuscript material. No independent external audit has been conducted. The numerical verifier does not certify the all-dimensional theorem or replace the proof; no claims are made for arbitrary bipartite graphs, weighted variants, or vertex-unlabeled combinatorial equivalence counts.

## References

1. A. Higashitani and A. Mori, *Minkowski decomposability of symmetric edge polytopes*, arXiv:2608.02445, v1 publicly dated 2026-08-03, https://arxiv.org/abs/2608.02445.
2. A. Higashitani, K. Jochemko, and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, https://arxiv.org/pdf/1807.07678.
3. A. D'Alì, E. Delucchi, and M. Michałek, *Many Faces of Symmetric Edge Polytopes*, arXiv:1910.05193, https://arxiv.org/abs/1910.05193.
4. B. Chen et al., *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, https://arxiv.org/abs/2107.12315.
