# Exact clique-free extrema and rigidity in tensor powers of complete graphs

## Finding

**Theorem.** Fix integers \(q\ge3\), \(n\ge1\) and \(3\le t\le q\). Define the simple graph \(G_{q,n}\) on \([q]^n\), with distinct words adjacent exactly when they differ in every coordinate. Equivalently, \(G_{q,n}=K_q^{\otimes n}\) is the largest-distance graph of the \(q\)-ary Hamming cube. Then

\[
\max\{|S|:S\subseteq[q]^n,\;G_{q,n}[S]\text{ contains no }K_t\}=(t-1)q^{n-1}.
\]

The **complete equality classification** is

\[
|S|=(t-1)q^{n-1}\iff
S=\{x\in[q]^n:x_i\in A\}
\]

for some coordinate \(i\in[n]\) and some \(A\subseteq[q]\) of cardinality \(t-1\). These descriptions are pairwise distinct. Thus the number of maximizing subsets is exactly

\[
n\binom{q}{t-1}.
\]

For \(t=3\) this determines the previously unisolated maximum-distance endpoint of the exact-distance triangle-free vertex problem:

\[
T_q(n,n)=2q^{n-1},\qquad
\#\{\text{maximizers}\}=n\binom q2.
\]

## Assumptions and scope

Graphs are finite, simple, and undirected. The alphabet \([q]=\{0,1,\ldots,q-1\}\) is merely a set of symbols, with no field assumption. A \(K_t\)-free induced subgraph may contain smaller cliques and arbitrary edges. The theorem includes the one-dimensional case \(n=1\), but requires \(q\ge3\) and \(3\le t\le q\). The statement is about Hamming distance **exactly \(n\)**, not Hamming distance one, and not an upper-distance threshold graph.

A **full transversal clique** means a clique with exactly \(q\) vertices. In such a clique each coordinate takes every alphabet symbol once; conversely any \(q\) words with this coordinatewise permutation property form a full transversal clique. Every clique of size at most \(q\) can be extended to one: in each coordinate complete its pairwise distinct symbols to a permutation of the alphabet.

## Proof

**1. Upper bound and attainability.** Identify the alphabet with the cyclic group \(\mathbb Z/q\mathbb Z\), without requiring \(q\) prime. For each \(x\in[q]^n\), the set

\[
C(x)=\{x+a(1,\ldots,1):a\in\mathbb Z/q\mathbb Z\}
\]

is a full transversal clique. These cliques are either disjoint or identical and hence partition \([q]^n\) into \(q^{n-1}\) cliques. A \(K_t\)-free set \(S\) contains at most \(t-1\) vertices from each, proving \(|S|\le(t-1)q^{n-1}\). Conversely, fixing any coordinate \(i\) and any \((t-1)\)-element alphabet set \(A\), the cylinder \(S=\{x:x_i\in A\}\) has the stated size and contains no \(t\)-clique: its selected words use only \(t-1\) different symbols in coordinate \(i\), while a clique requires pairwise distinct symbols there.

**2. Every full transversal is saturated at equality.** Suppose \(S\) attains the upper bound and write \(f=\mathbf1_S\). In the displayed partition each full transversal contains exactly \(t-1\) selected vertices. Any full transversal clique \(C\) is carried to the diagonal clique \(C(0)\) by a coordinatewise alphabet-permutation automorphism. Applying the inverse automorphism to the displayed clique partition produces a full-transversal partition containing \(C\). The same upper bound forces every member of this new partition, and therefore \(C\), to have exactly \(t-1\) selected vertices. Thus

\[
\sum_{x\in C}f(x)=t-1
\]

for **every** full transversal clique \(C\).

**3. The transversal swap identity.** Assume \(n\ge2\), fix coordinate \(i\), and fix distinct symbols \(a,b\in[q]\). Let \(u,v\in[q]^{n-1}\) be words whose entries differ in every coordinate. Construct two full transversal cliques that agree on their other \(q-2\) vertices. Their two differing vertices, respectively, are \((a,u),(b,v)\) and \((b,u),(a,v)\), where coordinate \(i\) is written first. Such completion is possible because for every coordinate the two displayed values are distinct; fill the unused \(q-2\) values there in arbitrary bijective order. Subtracting the two saturated-clique equalities gives

\[
f(a,u)-f(b,u)=f(a,v)-f(b,v).
\]

Set \(h(u)=f(a,u)-f(b,u)\). The graph on \([q]^{n-1}\) connecting words that differ everywhere has diameter at most two for \(q\ge3\): given any \(u,v\), independently choose in each coordinate a symbol different from both of their symbols, obtaining a word adjacent to each. Therefore \(h\) is constant. This holds for every coordinate \(i\) and every choice \(a\ne b\): **the change in \(f\) when a single coordinate changes is independent of all other coordinates**.

**4. Boolean additivity forces one coordinate.** Fix a reference word \(o\), and for each coordinate \(i\) define \(g_i(a)=f(o_1,\ldots,o_{i-1},a,o_{i+1},\ldots,o_n)-f(o)\). Change the coordinates of \(o\) to those of a general \(x\) one at a time. The context-independence proved in step 3 makes the increment at coordinate \(i\) equal to \(g_i(x_i)\), yielding

\[
f(x)=f(o)+\sum_{i=1}^n g_i(x_i).
\]

If two different functions \(g_i,g_j\) were nonconstant, varying only these two coordinates would produce four Boolean values \(z\), \(z+\alpha\), \(z+\beta\), \(z+\alpha+\beta\) with nonzero integer increments \(\alpha,\beta\). As the first three values are in \(\{0,1\}\), each increment is \(\pm1\). If they have the same sign, the fourth value is outside \(\{0,1\}\); if their signs differ, one of the second or third values is outside \(\{0,1\}\). Contradiction. Hence at most one coordinate matters to \(f\).

Because \(0<(t-1)q^{n-1}<q^n\), the function is nonconstant, so exactly one coordinate matters. The selected symbols on this coordinate form a set \(A\), and the cardinality equality gives \(|A|=t-1\). For \(n=1\) the conclusion follows directly from \(G_{q,1}=K_q\).

**5. Counting.** For fixed \(i\), there are \(\binom q{t-1}\) possible cylinders. Since \(1\le t-1<q\), a nontrivial cylinder depending on coordinate \(i\) cannot equal one depending on a different coordinate \(j\): hold coordinate \(j\) fixed and vary coordinate \(i\) across a selected and an unselected symbol. The number of distinct extremizers is therefore \(n\binom q{t-1}\). This completes the proof.

## Verification

The standalone script `verify.py` uses only the Python standard library and reconstructs edges from coordinatewise inequality, without using the proof's partition argument. Running `python3 verify.py` gives:

```text
DIRECT_EXHAUSTIVE_OK 3 2 3 6 sets 6 forbidden cliques
DIRECT_EXHAUSTIVE_OK 4 2 3 12 sets 96 forbidden cliques
DIRECT_EXHAUSTIVE_OK 4 2 4 8 sets 24 forbidden cliques
TRANSVERSAL_EQUATIONS_OK 3 3 3 9 sets 36 independently generated transversals
TRANSVERSAL_EQUATIONS_OK 4 2 3 12 sets 24 independently generated transversals
SWAP_IDENTITY_OK 3 2
VERIFY_OK
```

The first three checks exhaust **every** size-optimal candidate subset at their stated parameters and compare the observed family with the coordinate cylinders, inspecting forbidden cliques directly. The next two checks independently enumerate all Boolean solutions of the full-transversal equalities via constraint propagation, and recover the same extremizers. These tests are finite consistency checks, not a proof of the all-parameter theorem; the proof above supplies that argument.

## Relationship to prior work

Csajbók, Mukkamala, and Nagy's 2026 study formulates the triangle-free vertex Turán problem in exact-distance Hamming graphs. It proves a distance-one formula and analyzes several fixed smaller distances; the present theorem treats the **distance equal to dimension** endpoint, where the host is instead a categorical product of complete graphs, and adds every forbidden clique order and all equality cases. Its distance-one theorem does not imply the present distance-maximum theorem.

Brakensiek's 2017 paper studies the *same tensor-product host* but investigates vertex isoperimetry and stability of independent sets (the \(K_2\)-free case). Independent-set uniqueness is strictly weaker: a maximizing \(K_t\)-free set for \(t\ge3\) may induce many edges and is larger than an independent set. Popova's 2026 study optimizes maximum and average induced degrees in related products, including the tensor power of a triangle, but does not impose or classify forbidden clique orders. The proof here uses equal intersection with every full transversal, rather than those degree estimates. Searches under the aliases exact-distance Hamming graph, direct/categorical graph product, and generalized forbidden clique revealed no stronger stated classification of this kind; this is a qualified comparison, not a historical-priority certification.

## Limitations

The theorem does not cover \(q=2\), forbidden orders greater than \(q\), intermediate exact distances \(1<r<n\), or quantitative stability of near-extremizers. It does not classify nonmaximum \(K_t\)-free families. The short complete proof gives same-source internal mathematical support; it has not undergone independent mathematical review. Historical priority is provisional, particularly for work describing the same object as a clique-partition hypergraph or a transversal perfect-matching family.

## References

- B. Csajbók, P. Mukkamala, and Z. L. Nagy, *Triangle-Free Sets in Exact-Distance Hamming Graphs*, arXiv:2610.32789v1 (first posted 2026-10-23), https://arxiv.org/abs/2610.32789.
- J. Brakensiek, *Vertex Isoperimetry and Independent Set Stability for Tensor Powers of Cliques*, APPROX/RANDOM 2017, DOI:10.4230/LIPIcs.APPROX-RANDOM.2017.33, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.APPROX-RANDOM.2017.33.
- E. Popova, *On the Minimum Possible Maximum Degree of Induced Subgraphs of Product Graphs*, arXiv:2609.32903v1 (first posted 2026-09-26), https://arxiv.org/abs/2609.32903.
