# Exact eight-element Boolean census of fundamental preconditionals

## Finding

On the eight-element Boolean algebra \(B=\mathcal P(\{1,2,3\})\), there are exactly **1,021** binary operations \(\to\) for which \((B,\to)\) is an \(\mathsf F\)-algebra in the sense of Chen: the five preconditional inequalities of Holliday, conditional identity, semicomplementation and double-negation inflation. Under the natural six-element automorphism group \(\operatorname{Aut}(B)\cong S_3\), these operations form precisely **194** isomorphism classes; their orbit-size distribution is \(4,3,37,150\) for orbit sizes \(1,2,3,6\), respectively.

There is a natural eight-fibre refinement. The derived negation \(\nu(A)=A\to\varnothing\) is the graph polarity of a unique reflexive symmetric graph on the three atoms. For graphs with \(e=0,1,2,3\) nonloop edges, the number of operations extending each fixed graph is, respectively, \(1,16,81,729\). Thus the labelled total is \(1+3\cdot16+3\cdot81+729=1021\).

## Assumptions and scope

All carriers and operations are finite. For the underlying bounded lattice, write \(0=\varnothing\), \(1=\{1,2,3\}\), \(\wedge=\cap\), and \(\vee=\cup\). In general, a *preconditional* obeys all five inequalities, for arbitrary \(a,b,c\):

\[
\begin{aligned}
\mathrm{(P1)}&\quad 1\to a\le a,\\
\mathrm{(P2)}&\quad a\wedge b\le a\to b,\\
\mathrm{(P3)}&\quad a\to b\le a\to(a\wedge b),\\
\mathrm{(P4)}&\quad a\to(b\wedge c)\le a\to b,\\
\mathrm{(P5)}&\quad a\to((a\wedge b)\to c)\le(a\wedge b)\to c.
\end{aligned}
\]

An \(\mathsf F\)-algebra in this paper means a preconditional with \(\mathrm{(ID)}\ a\to a=1\), \(\mathrm{(SC)}\ a\wedge\nu(a)=0\), and \(\mathrm{(DNI)}\ a\le\nu(\nu(a))\), where \(\nu(a)=a\to0\). This is the exact algebraic signature of Chen's \(\mathsf F\), without adding modus ponens or weak monotonicity. Operations are counted as all functions \(B^2\to B\), not up to term equivalence. Isomorphism means conjugation by a Boolean-algebra automorphism.

## Proof

**1. Row reduction and Galois negation.** Axioms P3 and P4 imply \(a\to b=a\to(a\wedge b)\); P4 also makes the map \(b\mapsto a\to b\) monotone. ID forces \(a\to b=1\) whenever \(a\le b\), and P1–P2 force \(1\to b=b\). For each \(a\), it therefore suffices to specify \(f_a(d)=a\to d\) on \(d\le a\), with \(d\le f_a(d)\), monotonicity, \(f_a(a)=1\), and \(a\wedge f_a(0)=0\). P5 gives the remaining compatibility condition
\[
 f_a\bigl(a\wedge f_d(c)\bigr)\le f_d(c)\quad(d\le a,\ c\le d).
\]
Indeed this is just P5 after renaming \(d=a\wedge b\), and every such \(d\) arises.

The negation \(\nu\) is antitone: if \(a\le b\), then by P4 \(\nu(b)=b\to0\le b\to\nu(a)\), and P5 with \(d=a,c=0\) gives \(b\to\nu(a)\le\nu(a)\). Together with DNI, antitonicity yields the symmetric Galois law \(a\le\nu(b)\iff b\le\nu(a)\). It follows that on a power-set lattice \(\nu\) sends unions to intersections. Defining an atomic relation by \(iRj\iff j\notin\nu(\{i\})\), Galois symmetry makes \(R\) symmetric and SC makes it reflexive. Therefore
\[
\nu(A)=\{j:\text{for all }i\in A,\ \neg(iRj)\}.
\]
Conversely, every reflexive symmetric graph produces such a negation. It also produces an \(\mathsf F\)-preconditional: set \(a\to b=1\) when \(a\le b\), and otherwise set \(a\to b=\nu(a)\vee(a\wedge b)\). P1–P4 and ID, SC, DNI are immediate. For P5 put \(d=a\wedge b\). If \(d\le c\), the right side is \(1\). Otherwise \(t=d\to c=\nu(d)\vee(d\wedge c)\). Choose \(i\in d\setminus c\); reflexivity gives \(i\notin\nu(d)\), so \(i\notin t\) and \(a\not\le t\). Consequently \(a\to t=\nu(a)\vee(a\wedge t)\le\nu(d)\vee t=t\), proving P5. Thus all eight graphs occur.

**2. Exact row count conditional on a graph.** Fix the derived graph. Rows at \(0\) and \(1\) are forced by ID/P1–P2; each singleton row is forced by its value at \(0\), by ID, and by P3. Only the three two-atom antecedent rows have free values. For \(a=\{i,j\}\) with remaining atom \(k\), the values of \(a\to\{i\}\) and \(a\to\{j\}\) must contain their respective singleton and \(\nu(a)\). P5 first rules out all other choices except \(\{i\},\{i,k\},1\) and \(\{j\},\{j,k\},1\), subject to \(\nu(a)\), and then the inner-singleton conditions enforce the graph's nonadjacencies. The allowed numbers of choices for the three two-atom rows, up to atom permutation, are

| Nonloop edges | Two-atom row-choice counts | Operations per fixed graph |
| --- | --- | ---: |
| \(0\) | \((1,1,1)\) | \(1\) |
| \(1\) | \((4,2,2)\) | \(16\) |
| \(2\) | \((9,9,1)\) | \(81\) |
| \(3\) | \((9,9,9)\) | \(729\) |

To obtain the table without relying on code, examine each pair \(\{i,j\}\). An edge \(iRj\) permits all three aforementioned values for each singleton consequent when the third vertex touches the pair; a nonedge forces \(a\to\{i\}\subseteq\nu(\{j\})\) and \(a\to\{j\}\subseteq\nu(\{i\})\) by P5. If the third atom is isolated from the entire pair, \(\nu(a)=\{k\}\) forces inclusion of \(k\). Applying these elementary rules to the four three-vertex graph types gives the row counts displayed. The constraints for distinct two-element antecedents do not interact: they are incomparable and all remaining P5 cases have already been checked in the row analysis. This proves \(1+3\cdot16+3\cdot81+729=1021\).

**3. Orbits.** Each permutation of the three atoms acts by simultaneous relabelling on the operation table. Directly applying the row choices to a transposition fixes \(1+4+9+27=41\) operations: those whose graph has respectively \(0,1,2,3\) edges and is invariant under the transposition, with corresponding symmetric row assignments. A three-cycle fixes \(1+9=10\): only the empty and complete graphs are invariant, and their row choices must cycle together. Hence Burnside's lemma gives
\[
 \frac{1021+3\cdot41+2\cdot10}{6}=194.
\]
Enumerating stabilizers further yields precisely \(4\) orbits of size \(1\), \(3\) of size \(2\), \(37\) of size \(3\) and \(150\) of size \(6\); their weighted sum is \(1021\).

## Verification

The accompanying standalone standard-library `checker.py` represents subsets by three-bit masks. It first generates every row satisfying the local necessary conditions, combines them under all P5 compatibility constraints, and **independently re-evaluates P1–P5, ID and SC on each of the resulting 7,820 T-operations**. Of these, exactly \(1,021\) satisfy DNI. It groups by induced graph, checks the four graph-fibre sizes, and enumerates the six automorphisms to verify the orbit census and Burnside fixed-point counts. Executing `python checker.py` prints `F_PRECONDITIONAL_BOOLEAN3_OK` and all specified counts. Enumeration is exhaustive only for the eight-element Boolean carrier; the structural argument above proves the graph-polarity statement for arbitrary finite Boolean carriers.

## Relationship to prior work

Holliday's preconditional axioms and the classical algebraic theory of weak pseudocomplementation supply the starting identities, including the familiar self-adjoint antitone negation. Chen's 2026 introduction of \(\mathsf F\)-algebras specifies exactly ID, SC and DNI and provides relational semantics and finite-model results, rather than this small Boolean expansion census. The graph-polarity characterization is treated as standard background, not as the novelty claim. Work on stronger Boolean expansion subclasses incorporating modus ponens and normality is not a count of Chen's unrestricted \(\mathsf F\)-class; these axiom sets are not interchangeable. Finite-chain classifications also have a different underlying lattice.

## Limitations

The exact census and orbit distribution apply to a single eight-element Boolean carrier, not all finite Boolean algebras. The graph construction is not asserted to classify every conditional operation on larger carriers. Computational completeness is backed by a finite exhaustive generator and cross-checks, not independent machine-certified proof. An unindexed earlier equivalent enumeration remains a historical-priority risk; independent external audit has not been performed.

## References

1. Zhicheng Chen, *Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations*, arXiv:2607.20221, first submitted 2026-07-22, especially §3.1–3.2.
2. Wesley H. Holliday, *Preconditionals*, arXiv:2402.02296, first submitted 2024-02-03, especially axioms P1–P5 and the discussion of involutive derived negation.
3. Wesley H. Holliday, *A Fundamental Non-Classical Logic*, Logics 1(1) (2023), on fundamental lattices and antitone self-adjoint negation; DOI 10.3390/logics1010004.
