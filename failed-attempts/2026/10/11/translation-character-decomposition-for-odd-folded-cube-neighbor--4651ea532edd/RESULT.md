# Translation-character decomposition for odd folded-cube neighborhood complexes

## Finding
For every odd integer \(n\ge 3\), write \(T_n=\mathbb F_2^n/\langle\mathbf 1\rangle\), where \(\mathbf 1=(1,\ldots,1)\), and let \(FQ_n\) be the graph on \(T_n\) with edges \([x]\sim[x+e_i]\) for the \(n\) standard basis vectors. The group \(T_n\) acts on the ordinary Lovász open-neighborhood complex \(K_n=\mathcal N(FQ_n)\) by translation.

The only nonzero reduced rational homology of \(K_n\) is in degree \(2\). The complete \(\mathbb Q[T_n]\)-module decomposition is
\[
\widetilde H_2(K_n;\mathbb Q)\cong
\bigoplus_{\substack{y\in\mathbb F_2^n\\|y|\text{ even}}}
\mathbb Q_{\chi_y}^{\oplus m_n(y)},
\qquad \chi_y([t])=(-1)^{\langle y,t\rangle},
\]
where \(\mathbb Q_{\chi_y}\) is the one-dimensional rational sign representation, \(|y|\) is Hamming weight, and
\[
m_n(0)=\frac{(n-1)(n-2)}2,\qquad
m_n(y)=\frac{(n-2|y|)^2+n^2-6n+8}{4}\quad(y\ne0,\ |y|\text{ even}).
\]
Every multiplicity is a nonnegative integer. For example, the sixteen-vertex Clebsch graph \(FQ_5\) has multiplicity \(6\) for the trivial character, multiplicity \(1\) for each of the ten weight-two characters and multiplicity \(3\) for each of the five weight-four characters. Their dimensions sum to \(31\). For \(FQ_7\), the multiplicities at weights \(0,2,4,6\) are respectively \(15,6,4,10\), giving total dimension \(351\).

## Assumptions and scope
The graph is the antipodal quotient of the \(n\)-cube, not the halved cube or the complement of \(FQ_5\). The neighborhood complex uses *open* neighborhoods: a nonempty vertex set is a simplex exactly when all its vertices share a graph neighbor. All statements concern odd \(n\ge3\) and rational representations of the translation subgroup \(T_n\), not the full graph automorphism group or equivariant homotopy type. Character labels are precisely the even-weight vectors \(y\), because only these define characters on the quotient by \(\mathbf1\).

## Proof
**1. Neighborhood intersections.** Put \(v=|T_n|=2^{n-1}\). Each neighborhood consists of the \(n\) distinct vertices \([x+e_i]\). Two distinct vertices \([a],[b]\) have a common neighbor exactly when \([a+b]=[e_i+e_j]\) for distinct \(i,j\). The \(\binom n2\) such nonzero classes are all distinct for odd \(n\ge3\), and for each of them there are exactly two common neighbors. Consequently distinct neighborhood simplices intersect in either zero or two vertices. In particular, every simplex on at least three vertices has one and only one neighborhood center.

**2. Homology concentration.** Choose one distinguished vertex \(b_c\) in each neighborhood \(N(c)\). On the face poset, pair every simplex \(A\subseteq N(c)\) of cardinality at least three that excludes \(b_c\) with \(A\cup\{b_c\}\). By the unique-center property each such face belongs to only one \(N(c)\), so these pairs are unambiguous. The toggle matching within each simplex is acyclic, and a directed alternating path involving cells of dimension at least two cannot change neighborhood center without descending to an unmatched edge. There are no matches involving edges or vertices, so the global matching is acyclic. All its unpaired cells have dimension at most two: hence Forman's theorem gives a CW model of dimension at most two.

For simple graphs, Matsushita's neighborhood-complex theorem identifies \(\pi_1(\mathcal N(G))\) with the even-length subgroup of the fundamental group of the graph two-complex obtained by filling four-cycles (Reference 1, Theorems 1.1 and 3.2). In \(FQ_n\), every four-cycle lifts to a four-cycle of \(Q_n\): a length-four path in the cube has even total coordinate parity, whereas a nonclosed lift ending at its antipode would have odd parity because \(n\) is odd. Each cube four-cycle is a coordinate square. Thus that two-complex has the same fundamental group as the antipodal quotient of the cubical two-skeleton of \(Q_n\). The latter skeleton is simply connected, and the antipodal action is free, so the quotient has fundamental group \(\mathbb Z/2\). Its nontrivial class is represented by a path of length \(n\) between antipodal cube vertices; since \(n\) is odd, the even subgroup is trivial. The graph \(FQ_n\) is connected and nonbipartite (it has the projected odd path), so its even-walk neighborhood complex is connected. Therefore \(K_n\) is simply connected.

The face counts are \(f_0=v\), \(f_1=v\binom n2/2\), and \(f_{k-1}=v\binom nk\) for \(3\le k\le n\), by the unique-center property. Its reduced Euler characteristic is
\[
\widetilde\chi(K_n)=-1+2^{n-3}(n^2-5n+8)=:\beta_n.
\]
Simple connectivity and the two-dimensional CW model imply that reduced integral homology is concentrated in degree two, is free, and has rank \(\beta_n\). In particular, the same degree concentration holds rationally; no result about a higher-dimensional attaching map is used.

**3. Translation traces.** Every nonzero translation \(t\in T_n\) is a fixed-point-free involution on vertices. An invariant nonempty simplex must be a union of two-element translation orbits. If \(t\) is not one of the \(\binom n2\) classes \([e_i+e_j]\), no two-element orbit is an edge and no nonempty invariant simplex exists. Its trace on \(\widetilde H_2\) is then \(-1\) by the reduced Hopf trace formula.

If \(t=[e_i+e_j]\), all \(v/2=2^{n-2}\) translation orbits are edges of \(K_n\). No invariant simplex can contain two such orbits, since each neighborhood \(N(c)\) contains precisely one pair of vertices differing by \(t\). Hence the only invariant nonempty simplices are these \(v/2\) edges. Translation reverses their orientations, so each contributes \(+1\) to the alternating chain trace. Subtracting the augmented empty-face trace \(1\) gives
\[
\operatorname{tr}\bigl(t\mid\widetilde H_2(K_n;\mathbb Q)\bigr)=
\begin{cases}
\beta_n,&t=0,\\
2^{n-2}-1,&t=[e_i+e_j],\ i\ne j,\\
-1,&\text{otherwise}.
\end{cases}
\]

**4. Fourier multiplicities.** Since \(T_n\) is elementary abelian, all irreducible rational representations are the sign characters \(\chi_y\) indexed by even-weight \(y\). Fourier inversion states
\[
m_n(y)=2^{1-n}\sum_{t\in T_n}\operatorname{tr}(t\mid\widetilde H_2)\chi_y(t).
\]
The signed sum over the weight-two classes is the degree-two Krawtchouk value
\[
K_2(|y|)=\binom{n-|y|}{2}+\binom{|y|}{2}-|y|(n-|y|)
=\frac{(n-2|y|)^2-n}{2}.
\]
For \(y\ne0\), character orthogonality gives \(\sum_{t\ne0}\chi_y(t)=-1\), yielding the displayed nontrivial-character formula. For \(y=0\), the sum is \(2^{n-1}-1\), yielding \((n-1)(n-2)/2\). For odd \(n\) and even \(|y|\), the formulas are integers; nonnegativity follows from the representation construction. The sum of all dimensions reproduces \(\beta_n\).

## Verification
The accompanying standalone scripts use exact integer arithmetic and require only the Python standard library. Run `python verify_translation.py` and `python verify_local.py` from the directory containing those files. The first enumerates every face of \(K_n\) for \(n=3,5,7\), evaluates signed fixed-simplex traces for every translation, performs Fourier inversion for every character, and computes full mod-two simplicial boundary ranks in those cases. The second independently checks every pairwise neighborhood intersection, translation orbit incidence and multiplicity sum in the same cases. Additional arithmetic checks cover \(n=9,11,13,15\). The computed reduced Betti vectors have one nonzero entry of ranks \(1,31,351\) in dimension two for \(n=3,5,7\).

The finite checks corroborate the uniform mathematical proof; they are not presented as proofs for infinitely many values of \(n\).

## Relationship to prior work
Matsushita (Reference 1) gives the fundamental-group identification used in step 2; that theorem by itself does not compute homology representations. Csorba (Reference 2) studies simple equivariant homotopy equivalences among several graph-complex constructions under an involution; it does not supply the displayed translation-character formula in its accessible abstract. A nonequivariant homotopy classification, even for every odd folded cube, specifies the dimension of \(\widetilde H_2\) but does not specify its \(T_n\)-action. The new claim is the explicit full family of character multiplicities, not the dimension or an equivariant homotopy equivalence.

## Limitations
The representation is over \(\mathbb Q\), not a classification of integral \(\mathbb Z[T_n]\)-lattices. The nontrivial action of the larger permutation automorphism group and all equivariant attaching maps remain uncomputed. Exact bibliographic priority is subject to unindexed or inaccessible equivalent literature; an abstract-only equivariant graph-complex source was not fully inspected. The finite programs check only specified odd dimensions.

## References
1. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803 (first posted 2012-10-10), J. Math. Sci. Univ. Tokyo 24 (2017), 321–353; particularly Theorems 1.1 and 3.2. Full text: https://www.ms.u-tokyo.ac.jp/journal/jms240302.pdf.
2. P. Csorba, *On the Simple Z2-homotopy Types of Graph Complexes and Their Simple Z2-universality*, Canadian Mathematical Bulletin 51 (2008), 535–544, doi:10.4153/CMB-2008-053-9.
3. D. Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008, discrete Morse and equivariant simplicial-chain background.
