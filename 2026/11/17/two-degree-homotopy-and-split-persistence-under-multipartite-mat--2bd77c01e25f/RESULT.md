# Two-degree homotopy and split persistence under multipartite matching defects

## Finding

Let integers \(q\ge4\), \(s\ge q-1\), \(c\ge2\), and \(a,b\ge c\) be given. Start with the complete multipartite graph with shores \(A,B,\{z_1\},\ldots,\{z_s\}\), where \(|A|=a\) and \(|B|=b\). Choose pairwise distinct \(a_1,\ldots,a_c\in A\) and \(b_1,\ldots,b_c\in B\). For \(0\le t\le c\), let \(G_t\) be obtained by deleting exactly the edges \(a_i b_i\), \(1\le i\le t\). Let \(X_t=\mathsf{CF}_q(G_t)\) be the simplicial complex of vertex subsets inducing no clique of size \(q\).

Put \(h=\binom{s}{q-1}\) and \(d=\binom{s}{q-2}\). Then the **integral homotopy types** are

\[
|X_0|\simeq\bigvee^{h+d}S^{q-2},\qquad
|X_t|\simeq\bigvee^h S^{q-2}\vee\bigvee^{(t-1)d}S^{q-1}\quad(1\le t\le c).
\]

The natural inclusions \(X_t\hookrightarrow X_{t+1}\) have the following **split integral persistence behavior**. In degree \(q-2\), the first map is surjective with free kernel of rank \(d\), and each subsequent map is an isomorphism. In degree \(q-1\), every map after the first is a split injection with free cokernel of rank \(d\); all other reduced integral homology groups vanish. Thus, over any field, there are \(h\) permanent degree-\(q-2\) bars, \(d\) degree-\(q-2\) bars ending at index one, and \(d\) new permanent degree-\(q-1\) bars at each index \(2,\ldots,c\). No torsion occurs.

## Assumptions and scope

Graphs are finite, simple and undirected. Edges inside shores are absent; all cross-shore edges are present before the specified deletions. The graph edges deleted in \(A\times B\) are pairwise vertex-disjoint. The threshold \(q\) is the forbidden clique *order*, not the number of graph shores. The condition \(s\ge q-1\) makes both sphere dimensions occur whenever \(t\ge2\). All homotopy equivalences are nonequivariant, and the persistence statements concern inclusion-induced maps over \(\mathbb Z\).

## Proof

**1. The intact multipartite complex.** A subset of the undeleted graph induces no \(q\)-clique precisely when it meets at most \(q-1\) shores. In \(X_0\), every vertex other than a chosen representative of each non-singleton shore is dominated: adjoining its shore's representative preserves every face. Deleting dominated vertices gives a strong simplicial collapse onto the \((q-2)\)-skeleton \(L\) of the simplex with vertices \(\{A,B,z_1,\ldots,z_s\}\). Write \(k=q-2\). As the \(k\)-skeleton of an \((s+1)\)-simplex, \(L\) is homotopy equivalent to \(\bigvee^{\binom{s+1}{q-1}}S^k\); this can be seen by coning a fixed vertex onto the \((k-1)\)-skeleton on the remaining vertices. Pascal's identity gives \(\binom{s+1}{q-1}=h+d\). The collapsing map \(\rho:X_0\longrightarrow L\), replacing each vertex by its shore representative, is a homotopy equivalence.

**2. Precisely the new faces.** A face of \(X_t\) not in \(X_0\) must meet at least \(q\) shores. If it meets more than \(q\), or meets \(q\) without using both \(A\) and \(B\), it contains a \(q\)-clique. With exactly \(q\) shores including \(A,B\), the only way not to contain a \(q\)-clique is to select exactly the two endpoints \(a_i,b_i\) of one deleted edge in these two shores, together with \(q-2\) singleton shores. The presence of a further vertex in either \(A\) or \(B\) would restore a \(q\)-clique. Therefore the new faces at stage \(t\) are **exactly** the \(d\) simplices \(\{a_t,b_t\}\cup S\) with \(S\subseteq\{z_1,\ldots,z_s\}\) and \(|S|=q-2\). They are \((q-1)\)-simplices, and their entire boundaries belong to \(X_0\). Consequently each stage attaches \(d\) cells of dimension \(q-1=k+1\), with no other added faces.

**3. The integral attaching classes are a basis summand.** Orient every \(\{a_i,b_i\}\cup S\) in the order \(a_i,b_i\), then the ordered elements of \(S\). Under \(\rho\), the oriented attaching sphere maps to the simplicial cycle

\[
z_S=\partial[A,B,S]\in\widetilde H_k(L;\mathbb Z).
\]

A standard integral basis for the top reduced homology of \(L\) is the family \(\partial[A,T]\), where \(T\) ranges over the \((q-1)\)-subsets of \(\{B,z_1,\ldots,z_s\}\). In this basis the \(d\) vectors \(z_S\) are exactly those indexed by \(T=\{B\}\cup S\). Thus they form a primitive direct summand of rank \(d\), and their classes do not depend on the matched-edge index \(i\). This establishes both their integral independence and the absence of any finite-index ambiguity.

**4. Attach the cells and track inclusions.** Since \(k\ge2\), \(L\) is simply connected and \((k-1)\)-connected, and its \(k\)-sphere wedge has \(\pi_k\cong H_k\cong\mathbb Z^{h+d}\). The first set of \(d\) cells attaches along a subset of an integral basis in \(\pi_k\), killing exactly those \(d\) summands; hence \(|X_1|\simeq\bigvee^h S^k\). For each subsequent matched edge, every attaching map becomes nullhomotopic in \(X_1\): its class is the image of an already killed \(z_S\), and the Hurewicz map \(\pi_k(X_1)\to H_k(X_1;\mathbb Z)\) is an isomorphism. Attaching these nullhomotopic \((k+1)\)-cells wedges on \(d\) copies of \(S^{k+1}\) at each step, compatibly with the inclusions. This proves the homotopy formulas, split integral inclusion maps, and barcode description.

## Verification

The accompanying standalone Python program `verify_matching_clique.py` independently enumerates all vertex subsets, tests the forbidden-\(q\)-clique predicate from graph edges, and checks it against the structural face criterion. It then constructs every mod-two simplicial boundary matrix and checks reduced Betti numbers at every stage. Its four parameter families contain thirteen stages, including unequal non-singleton shore sizes and thresholds four and five. It also confirms that exactly \(d\) facets and no lower faces appear at each deletion. The checker uses no external dependencies. Run `python3 verify_matching_clique.py` and compare with `verify_matching_clique_output.txt`. These finite checks corroborate but do not replace the unrestricted integral proof above.

A sample mixed-dimensional case is \(q=4\), \(s=3\), \(a=b=c=3\):

\[
|X_0|\simeq\bigvee^4 S^2,\quad
|X_1|\simeq S^2,\quad
|X_2|\simeq S^2\vee\bigvee^3S^3,\quad
|X_3|\simeq S^2\vee\bigvee^6S^3.
\]

## Relationship to prior work

Ghosh and Selvaraja (2026) introduce and study shellability conditions for forbidden-clique complexes, including chordal and clique-attachment settings. Their full public manuscript was inspected, including its definitions and principal results; it does not state the mixed-dimensional matching-fault homotopy or the inclusion maps here. An earlier all-shore forest-defect calculation considers the different cutoff in which the clique order equals the number of shores, producing a single sphere degree; the present range has strictly more shores than the forbidden-clique order and **simultaneous nonzero homology in two adjacent degrees**. An intact complete-multipartite equivariant compression statement does not cover graphs with deleted cross-shore edges. A triangle-specific matched-part result concerns a different matched structure and a different cutoff. These are comparisons of mathematical scope, not claims of exhaustive uniqueness.

## Limitations

The formula assumes only two potentially non-singleton shores, all other shores singleton, and deleted cross-shore edges forming one matching. It does not cover intersecting deleted edges, deleted edges across several shore pairs, arbitrary non-singleton additional shores, equivariant splittings, or general clique-complex filtrations. The recorded computations are mod-two and finite; integral conclusions follow from the primitive attaching-basis proof. Independent mathematical validation has not been performed.

## References

- Rakesh Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1, first publicly submitted 2026-02-10, https://arxiv.org/html/2602.09623v1 .
- Standard simplicial facts used with proofs in the text: dominated-vertex strong collapse; the integral basis for the top homology of a simplex skeleton; attachment of cells along an integral sphere-wedge basis.
