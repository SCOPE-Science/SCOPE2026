# Reflection-fixed chordal models for cycle-power independence complexes

## Finding

For integers \(k\ge1\) and \(n\ge2k+2\), write \(C_n^k\) for the graph on \(\mathbb Z/n\mathbb Z\) joining distinct vertices of cyclic distance at most \(k\). Its independence complex is \(\operatorname{Ind}(C_n^k)\). The natural dihedral group acts by \(r(i)=i+1\), \(s(i)=-i\).

**Theorem.** Let \(H\le D_n\) be any subgroup containing a reflection. Write uniquely \(H=\langle r^t,r^a s\rangle\), where \(t\mid n\) and \(0\le a<t\). If \(t\le k\), then \(|\operatorname{Ind}(C_n^k)|^H=\varnothing\). For \(t>k\), normalize the reflection on the residue cycle of length \(t\) by a cyclic relabeling, so its equation is \(i\mapsto-i\) (type zero), or, when \(t\) is even and \(a\) is odd, \(i\mapsto1-i\) (type one). Define:

\[
V_0=\{0\}\cup\bigl(\{t/2\}\text{ if }2\mid t\bigr)\cup
\{j\in\mathbb Z:1\le j<t/2,\ k<2j<t-k\},
\]

\[
V_1=\{j\in\mathbb Z:1\le j\le t/2,\ k<2j-1<t-k\}
\quad(2\mid t).
\]

Let \(P_{M}^{k}[V]\) denote the induced subgraph of the \(k\)-th power of the integer path on \(\{0,\ldots,M-1\}\) (type zero), or the integer path on \(\{1,\ldots,M\}\) (type one). Then there is a **piecewise-linear homeomorphism**

\[
|\operatorname{Ind}(C_n^k)|^H\cong_{\mathrm{PL}}
\begin{cases}
|\operatorname{Ind}(P_{\lfloor t/2\rfloor+1}^{k}[V_0])|,&\text{type zero},\\
|\operatorname{Ind}(P_{t/2}^{k}[V_1])|,&\text{type one}.
\end{cases}
\]

In particular, every reflection-containing subgroup-fixed space is **empty, contractible, or a finite wedge of spheres** (not necessarily of equal dimensions), and its integral homology is torsion-free. The following terminating recursion gives the exact wedge multiplicity in every dimension.

For a finite induced subgraph \(Q\) of a path power, define its augmented sphere polynomial \(B_Q(z)\). Set \(B_{\varnothing}(z)=z^{-1}\), and set \(B_Q(z)=0\) if \(Q\) has at least one isolated vertex. Otherwise select a vertex \(v\) whose open neighborhood is a clique, and put

\[
B_Q(z)=z\sum_{u\in N_Q(v)} B_{Q-N_Q[u]}(z).
\]

Then, for each \(d\ge0\), the coefficient of \(z^d\) equals the number of \(d\)-sphere summands in the fixed space's homotopy type. No coefficient depends on the choices of simplicial vertices.

**Mixed-dimensional example.** For \(n=22\), \(k=3\), and the edge-axis reflection \(s'(i)=1-i\), the type-one index set is \(\{3,4,5,6,7,8,9\}\), and the fixed space is \(|\operatorname{Ind}(P_7^3)|\simeq S^0\vee S^1\). The independence complex has seven vertices, six one-dimensional faces, two connected components, and no two-dimensional faces; one component has one cycle.

## Assumptions and scope

The original graph is a simple cyclic distance power, with no loops. The topology is the **geometric fixed-point set** of the stated dihedral action, not a fixed-vertex induced subcomplex and not an orbit-space quotient. The group \(H\) must contain a reflection; no claim is made here that all purely rotational fixed spaces are chordal or that all cycle-power independence complexes are wedges of spheres. The parameters \(t\) and \(a\) describe the rotation and reflection generators, respectively. A reflection parameter can be changed by conjugation without changing the fixed-space PL type.

## Proof

**1. Reduce by rotations.** The positive generator of \(H\cap\langle r\rangle\) is \(r^t\) for exactly one divisor \(t\mid n\). Its vertex orbits consist of congruence classes modulo \(t\). When \(t\le k\), each orbit contains adjacent vertices: since the rotation is nontrivial, its successive vertices have cyclic distance \(t\le k\). Hence no nonempty union of orbits is independent, and the geometric fixed set is empty.

Suppose \(t>k\). Each residue class is independent. Two such classes have an edge between them if and only if their residues have circular distance at most \(k\) modulo \(t\). On each simplex fixed barycentric coordinates are constant on rotation orbits. Sending a residue vertex to the barycenter of its rotation orbit therefore gives a PL homeomorphism from \(|\operatorname{Ind}(C_t^k)|\) to the rotation-fixed locus, intertwining the induced reflection. This remains valid for the trivial rotation subgroup, \(t=n\).

**2. Normalize the reflection.** On residue classes, the reflection is \(i\mapsto a-i\). Translation by \(b\) changes \(a\) to \(a-2b\). For odd \(t\) it becomes zero; for even \(t\), its even and odd cases become zero and one. These are the two displayed types.

**3. Identify admissible reflected orbits.** In type zero the reflected orbits are \(\{0\}\), possibly \(\{t/2\}\) for even \(t\), and the pairs \(\{j,t-j\}\) at integers \(1\le j<t/2\). The pair's two vertices are adjacent exactly when \(\min(2j,t-2j)\le k\). This proves the formula for \(V_0\). In type one (even \(t\)), the orbits are the pairs \(\{j,1-j\}\), with \(1\le j\le t/2\); their internal circular distance is \(\min(2j-1,t-(2j-1))\). This gives \(V_1\).

**4. Identify all inter-orbit conflicts.** For two admissible paired orbits with indices \(i<j\), the direct vertex distances have minimum \(j-i\). In type zero the alternative reflected distances involve \(i+j\) and \(t-i-j\); both are strictly greater than \(k\) because \(2i>k\) and \(t-2j>k\). In type one they involve \(i+j-1\) and \(t-i-j+1\), also both greater than \(k\) by admissibility. Thus two pairs conflict exactly when \(j-i\le k\). A singleton endpoint in type zero conflicts with a retained pair exactly when their index distance is at most \(k\); two singleton endpoints conflict exactly when their index distance is at most \(k\). Consequently the orbit-conflict graph is precisely the stated induced subgraph of a path power.

**5. Prove the topological and homological conclusions.** As in Step 1, the barycenters of **all** admissible reflection-orbits form a simplex precisely when their union is an independent set. This gives the displayed PL homeomorphism. Each path power is an interval graph (represent index \(j\) by the closed interval \([j,j+k]\)); induced subgraphs remain interval graphs and therefore chordal. The classical simplicial-vertex splitting for chordal graphs proves that their independence complexes are contractible or wedges of spheres. A simplicial vertex \(v\) has clique neighborhood, and the splitting is

\[
\operatorname{Ind}(Q)\simeq\bigvee_{u\in N_Q(v)}\Sigma\operatorname{Ind}(Q-N_Q[u]).
\]

With the augmented convention \(\operatorname{Ind}(\varnothing)=S^{-1}\), induction gives the stated exact sphere polynomial. Every subproblem strictly loses vertices, so the recursion terminates. Wedges of spheres have torsion-free integral homology.

**6. Check the mixed example.** For the edge-axis reflection of \(C_{22}^3\), the retained labels are \(3,\ldots,9\). Independent two-element subsets of their path-power model are exactly \(\{3,7\},\{3,8\},\{3,9\},\{4,8\},\{4,9\},\{5,9\}\); no triple is independent. The one-dimensional complex has two components, with one independent first-homology cycle, proving \(S^0\vee S^1\).

## Verification

The complete standalone script `verify.py` constructs vertex orbits from the actual generators on the original \(n\)-cycle, independently enumerates orbit conflicts, and compares them to the explicit interval-index models. It checks 3,340 distinct graph-and-subgroup parameter instances, including 668 rotation-only control cases and 2,672 reflection-containing cases, for \(4\le n\le32\) and admissible \(k\le7\). It checks 452,220 actual invariant-orbit subsets directly against source-graph independence and the model. It also independently verifies the mixed-dimensional example's face graph. Execute `python verify.py`; expected output is recorded in `verification_output.txt`.

These bounded experiments corroborate, but do not prove, the all-parameter statement. The proof is the orbit-coordinate argument above, together with the cited chordal splitting theorem.

## Relationship to prior work

Adamaszek's 2011 paper establishes nonequivariant splitting recurrences for independence complexes of powers of cycles and quotes/proves the simplicial-vertex splitting for chordal graphs. Those are the source of the prior structural tools; they do not identify reflection-subgroup fixed spaces. His 2015 paper treats chordal independence complexes, dismantling and sphere behavior; it does not give the reflection-orbit model. The present claim contributes the explicit **all-reflection-subgroup PL compression** into a chordal interval graph, with a complete integer-homology recursion and a mixed-dimensional example.

The general observation that invariant independent sets correspond to compatible vertex orbits is elementary and not asserted as independently novel. Novelty resides in the reflection-specific *path-power induced-subgraph identification* and its full topological consequences. Different graph complexes built from cycles (such as higher-independence, Morse, and cut complexes) are not assumed to be equivalent to ordinary cycle-power independence complexes.

## Limitations

The theorem does not give equivariant homotopy equivalences of the entire ambient complexes, integral actions of arbitrary automorphism groups, or quotient-space homotopy types. The recursion is finite and exact but not a closed congruence formula. Published-source searches and indexed-result comparisons are evidence of noncoverage, not proof of global publication priority. Independent mathematical validation has not been performed.

## References

1. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250, first publicly posted 2011-06-30; particularly Theorem 1.1, Corollaries 5.4 and 5.6, and Remark 6.6. https://arxiv.org/abs/1106.6250
2. M. Adamaszek, *A note on independence complexes of chordal graphs and dismantling*, arXiv:1508.02426, first publicly posted 2015-08-10; particularly the introduction and Lemma 5. https://arxiv.org/abs/1508.02426
3. K. Kawamura, *Independence complexes of chordal graphs*, Discrete Mathematics 310 (2010), 2204–2211. DOI:10.1016/j.disc.2010.04.021. Prior chordal wedge theorem, not the reflection-fixed classification.
