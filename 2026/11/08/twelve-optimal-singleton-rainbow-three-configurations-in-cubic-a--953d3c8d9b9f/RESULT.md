# Twelve optimal singleton rainbow-three configurations in cubic abelian Cayley graphs

## Finding

A **singleton rainbow-three dominating function** on a finite simple graph \(G\) assigns each vertex one of \(0,1,2,3\), with \(0\) meaning uncolored, so that the three neighbors of every uncolored vertex collectively exhibit all three nonzero colors. Its weight is the number of nonzero assignments. Here only **cubic** graphs are considered; thus each uncolored vertex must have three differently colored neighbors.

**Theorem.** Let \(G\) be any connected cubic Cayley graph of a finite abelian group, with a specified labelled vertex set and three **named** colors. The minimum weight equals \(|V(G)|/2\) precisely for the following graph isomorphism types:

1. ordinary prisms \(C_m\square K_2\) with \(m\ge6\) and \(6\mid m\);
2. Möbius ladders \(M_n\), formed from an \(n\)-cycle by joining opposite vertices, with \(n\ge6\) and \(n\equiv6\pmod{12}\).

In every such equality graph there are **exactly twelve** minimum singleton rainbow-three functions. They are all obtained by choosing one of the two bipartition classes to color and assigning the three colors in a forced repeating period-three pattern; the other bipartition class is uncolored. The twelve functions form one orbit under graph automorphisms together with permutations of the three named colors. In particular, the number of minimizers is independent of the graph order along both infinite equality families.

The existence and graph-family classification of the equality cases, and their minimum weights, were established previously. **The new assertion is the exhaustive classification and constant exact count of all minimum singleton assignments, including their orbit rigidity.**

## Assumptions and scope

Graphs are finite, connected, simple, undirected, and 3-regular. A Cayley graph is taken with a symmetric three-element generating set not containing the identity. The vertex-label and color-label distinctions are retained when counting functions; assignments related by permutations are not identified. The prism is defined by vertices \(u_i,v_i\), \(i\in\mathbb Z/m\mathbb Z\), with edges \(u_i u_{i+1}\), \(v_i v_{i+1}\), and \(u_i v_i\). The Möbius ladder \(M_n\) has vertices \(w_i\), \(i\in\mathbb Z/n\mathbb Z\), where \(n\) is even, and edges \(w_iw_{i+1}\) and \(w_iw_{i+n/2}\); when \(n=4\) it is \(K_4\). The primary counting claim concerns equality at the universal half-order lower bound, not minimum functions in the non-equality residue classes.

## Proof

**1. Universal equality rigidity.** Write \(C\) for the colored vertices and \(U\) for the uncolored vertices of any valid function. Since each vertex of \(U\) is adjacent to three vertices of \(C\), edge counting gives \(3|U|\le3|C|\). Thus \(|C|\ge |V(G)|/2\). Equality forces all the neighbors of every colored vertex to belong to \(U\) as well, for otherwise \(3|U|<3|C|\). Hence \(C,U\) are the two classes of a bipartition; the colors on \(C\) must make every neighborhood of a vertex of \(U\) a permutation of \((1,2,3)\). Conversely, any such proper bipartition coloring attains the lower bound. Connected bipartite graphs have exactly two possible choices of the colored side.

**2. Reduction to the two graph types.** Let \(S\) be the inverse-closed three-element generating set of a finite abelian group. If every element of \(S\) is an involution, connectedness implies either a rank-two elementary abelian group, giving \(K_4=M_4\), or a rank-three elementary abelian group, giving the 3-cube \(Q_3\cong C_4\square K_2\). Otherwise \(S=\{b,b^{-1},a\}\), where \(b\) has order \(m\ge3\) and \(a\) is an involution. If \(a\notin\langle b\rangle\), this is a prism \(C_m\square K_2\); if \(a\in\langle b\rangle\), then \(m\) is even, \(a=b^{m/2}\), and the graph is the Möbius ladder \(M_m\). The exceptional small graphs \(K_4\) and \(Q_3\) are covered by the non-equality cases below.

**3. Prism recurrence.** A prism can attain equality only when \(m=2q\) is even, since otherwise it is not bipartite. Choose the colored class \(\{u_{2i},v_{2i+1}:i\in\mathbb Z/q\mathbb Z\}\). Write \(a_i=f(u_{2i})\) and \(b_i=f(v_{2i+1})\), all lying in \(\{1,2,3\}\). The two kinds of uncolored vertices impose, respectively,

\[
\{a_i,a_{i+1},b_i\}=\{1,2,3\},\qquad
\{b_{i-1},b_i,a_i\}=\{1,2,3\}.
\]

Because both triples contain \(a_i,b_i\), their third colors coincide: \(a_{i+1}=b_{i-1}\). Using the first equation at index \(i-1\), every consecutive triple \((a_{i-1},a_i,a_{i+1})\) must consist of three distinct colors. Therefore \(a_{i+3}=a_i\) for every \(i\). This is compatible with a cyclic sequence of length \(q\) if and only if \(3\mid q\); otherwise cyclicity forces the constant sequence, which violates distinctness. If \(3\mid q\), choose an arbitrary ordering of the three colors for \(a_0,a_1,a_2\), exactly \(3!=6\) choices, and repeat it. Each \(b_i\) is then uniquely the missing third color from \(a_i,a_{i+1}\). Both displayed neighborhood constraints are satisfied. Thus there are exactly six functions for this colored side and six for the opposite side. The criterion \(3\mid q\) is equivalent to \(6\mid m\).

**4. Möbius recurrence.** A Möbius ladder \(M_n\), \(n=2L\), is bipartite if and only if \(L\) is odd: its added opposite edges must reverse cycle parity. Choose the even-indexed colored side, put \(x_i=f(w_{2i})\) for \(i\in\mathbb Z/L\mathbb Z\), and let \(h=(L+1)/2\), so \(2h\equiv1\pmod L\). For each uncolored odd vertex the neighborhood requirement is

\[
\{x_i,x_{i+1},x_{i+h}\}=\{1,2,3\}.
\]

As \(h\) is invertible modulo \(L\), reindex \(y_j=x_{jh}\). Then \((j+2)h\equiv jh+1\pmod L\), and the displayed requirement becomes

\[
\{y_j,y_{j+1},y_{j+2}\}=\{1,2,3\}
\quad\text{for every }j\in\mathbb Z/L\mathbb Z.
\]

Successive overlapping triples force \(y_{j+3}=y_j\). The cyclic sequence exists precisely when \(3\mid L\), and is then uniquely fixed by any permutation of \((1,2,3)\) as its first three entries. These give six colorings on the even-indexed side and six on the odd-indexed side. Since \(L\) must be odd, \(3\mid L\) is equivalent to \(n\equiv6\pmod{12}\). This argument also includes \(M_6\cong K_{3,3}\).

**5. Orbit and absence of exceptions.** In each admissible graph, changing the permutation of the named colors moves transitively among the six functions with the same colored side. Rotation by one step along the prism or Möbius ladder exchanges the two bipartition classes, and so moves between the two six-element classes of functions. By Step 1 no other half-order functions exist. The explicit constructions achieve half-order, and Step 2 exhausts the connected cubic abelian Cayley graphs; the two claimed families, count twelve, and orbit assertion follow. \(\square\)

## Verification

Run `python verify.py` with Python 3 and no third-party dependencies. The program constructs graphs from their edges, independently checks the open-neighborhood condition, and enumerates all assignments supported on each bipartition for prisms of circumference 6 and 12 and Möbius ladders of order 6 and 18. It additionally exhausts **all** partial colorings of weight at most half-order for the 12-vertex prism and the 6-vertex Möbius ladder, obtaining twelve minimizers and no smaller solutions; it also tests representative non-equality cases. The last output line is `VERIFY_OK`. These are finite corroborations, not proof of the unrestricted assertions, which come from the recurrence arguments above.

## Relationship to prior work

Kuzman (arXiv:1907.08430, 2019), Section 4, classifies connected cubic abelian Cayley graphs and establishes classical rainbow-domination minima for prisms and Möbius ladders. Lange (arXiv:2610.06906, first public October 1, 2026), Theorem 7 and Theorems 13 and 19, supplies a singleton-rainbow equality criterion and determines exact minimum values in these graph families. Žerovnik (2026, DOI:10.3390/math14162917) studies singleton three-rainbow domination of cylindrical graphs, including prisms. None of the inspected relevant results gives the **total number of named minimum singleton three-rainbow functions**, proves that this number remains twelve in every equality graph, or classifies all such configurations up to symmetry. The known equality value and underlying Cayley classification are credited as prior facts rather than claimed anew.

## Limitations

The count twelve is restricted to the half-order equality cases and to the singleton model with exactly three named colors. This is not a count of classical rainbow functions that may assign multiple colors at a vertex. The theorem does not enumerate optimum functions in non-equality residue classes or for general nonabelian cubic Cayley graphs. Historical priority is provisional; overlapping alternative language (such as perfect neighborhood colorings) is a residual literature risk, and the result has not undergone an independent audit.

## References

1. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906v1 (first public October 1, 2026), Sections 2, 3 and 5.
2. B. Kuzman, *On \(k\)-rainbow domination in regular graphs*, arXiv:1907.08430 (first public July 19, 2019), Sections 3 and 4.
3. J. Žerovnik, *On Singleton 3-Rainbow Domination of Cylindrical Graphs*, Mathematics **14** (2026), 2917, DOI:10.3390/math14162917 (published August 12, 2026).
