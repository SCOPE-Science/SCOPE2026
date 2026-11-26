# Dihedral homology representations of triangle-free complexes of squared cycles

## Finding
For every integer \(n\ge7\), let \(C_n^2\) denote the graph with vertices \(\mathbb Z/n\mathbb Z\), with two vertices adjacent exactly when their cyclic distance is at most two. Set
\[
K_n=\operatorname{CF}_3(C_n^2)=\{S\subseteq\mathbb Z/n\mathbb Z:\text{no three vertices of }S\text{ form a triangle in }C_n^2\}.
\]
The dihedral group \(D_n=\langle r,t:r^n=t^2=1,\;trt=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(t(i)=-i\). Define \(q=\lfloor n/4\rfloor\), and let \(V_{n/4}\) for \(4\mid n\) denote the rational two-dimensional representation with \(r\) represented by the quarter-turn matrix \(\begin{pmatrix}0&-1\\1&0\end{pmatrix}\) and \(t\) by \(\operatorname{diag}(1,-1)\).

**Theorem (complete rational dihedral character).** All reduced rational homology of \(K_n\) vanishes except in the following degree, and the nonzero \(\mathbb Q[D_n]\)-module is exactly:
\[
\begin{array}{c|c|c}
n&d_n&\widetilde H_{d_n}(K_n;\mathbb Q)\\ \hline
4q\ (q\ge2)&2q-1& L_q\oplus V_{n/4},\quad L_q(r)=1,\ L_q(t)=(-1)^q\\
4q+1\ (q\ge2)&2q-1& L_q,\quad L_q(r)=1,\ L_q(t)=(-1)^q\\
4q+2\ (q\ge2)&2q& L_q,\quad L_q(r)=-1,\ L_q(t)=(-1)^q\\
4q+3\ (q\ge1)&2q+1& L_q,\quad L_q(r)=1,\ L_q(t)=(-1)^{q+1}
\end{array}
\]
Here \(L_q\) denotes the one-dimensional character specified in its row. In particular, when \(4\mid n\), a genuine two-dimensional quarter-turn summand occurs, and the remaining line alternates its reflection sign as \(n\) increases by four.

The ordinary mod-two Betti-number pattern of this family was already determined for cyclic triple hypergraphs by Kim and Kim (2021, Theorem 3.1); the new assertion is **the entire rational dihedral representation**, not those Betti numbers or an integral homotopy classification.

## Assumptions and scope
All spaces are finite abstract simplicial complexes and all representation equalities are over \(\mathbb Q\). The group action comes from the specified vertex permutations; geometric fixed-point spaces and homology of orbit spaces are not determined here. For \(n\ge7\), the triangles of \(C_n^2\) are exactly \(\{i,i+1,i+2\}\) modulo \(n\). Thus \(K_n\) is precisely the independence complex of the tight three-uniform cyclic hypergraph with those \(n\) edges. No statement is made for \(n<7\), where additional short-cycle coincidences change the graph triangles.

## Proof
**1. The homology is rationally concentrated in a known degree.** Kim and Kim, Theorem 3.1, computes the complete reduced homology of the tight \(k\)-uniform cycle over \(\mathbb F_2\). With \(k=3\), their formula gives zero outside degree \(d_n\) in the table and dimension three for \(4\mid n\) or one otherwise. Because rational Betti numbers cannot exceed mod-two Betti numbers in any degree, all reduced rational homology vanishes outside \(d_n\). We identify its exact rational dimension from Euler characteristic in Step 3; hence the argument does not infer torsion-freeness from mod-two data.

**2. Equivariant Euler trace as an orbit-subset partition function.** For any \(g\in D_n\), partition the \(n\) vertices into permutation orbits \(\mathcal O_g\). Write
\[
Z_g=\sum_{\substack{J\subseteq\mathcal O_g\\ \bigcup J\in K_n}}(-1)^{|J|}.
\]
The trace of \(g\) on an oriented simplex fixed setwise is the sign of its induced vertex permutation. If the simplex is a union of \(j\) permutation orbits containing \(m\) vertices in total, its contribution to the ordinary Lefschetz trace is \((-1)^{m-1}(-1)^{m-j}=-(-1)^j\). Including the empty augmented simplex therefore gives the reduced Lefschetz identity
\[
\widetilde L(g)=\sum_i(-1)^i\operatorname{tr}\bigl(g\mid\widetilde H_i(K_n;\mathbb Q)\bigr)=-Z_g.
\]
Because the rational homology is concentrated in degree \(d_n\), its entire character is
\[
\chi_n(g)=(-1)^{d_n+1}Z_g.\tag{1}
\]

**3. Rotations.** For \(g=r^s\), the orbits consist of the congruence classes modulo \(h=\gcd(n,s)\). Orbit-unions are exactly repetitions of cyclic binary words of length \(h\); avoiding three consecutive selected vertices is the same condition on the length-\(h\) periodic word. Assign weight \((-1)\) to every selected bit. Order the two-bit states as \(00,01,10,11\) and define
\[
M=\begin{pmatrix}1&-1&0&0\\0&0&1&-1\\1&-1&0&0\\0&0&1&0\end{pmatrix},
\]
whose transition from \((a,b)\) to \((b,c)\) has weight \((-1)^c\) unless \(abc=111\). The cyclic-word partition function is \(Z_{r^s}=\operatorname{tr}(M^h)\). Its characteristic polynomial is \(x(x-1)(x^2+1)\), so for positive \(h\),
\[
T(h):=\operatorname{tr}(M^h)=1+i^h+(-i)^h=\begin{cases}3,&4\mid h,\\-1,&h\equiv2\pmod4,\\1,&h\text{ odd}.\end{cases}\tag{2}
\]
For the identity \(h=n\), equations (1)–(2) and the known rational degree imply \(\dim_{\mathbb Q}\widetilde H_{d_n}=(-1)^{d_n+1}T(n)\), equal to three or one as asserted. For all rotations, they yield traces \(1+2\cos(\pi s/2)\) when \(4\mid n\); \((-1)^s\) when \(n\equiv2\pmod4\); and one when \(n\) is odd. In the first case the traces are exactly those of the trivial line plus the quarter-turn representation \(V_{n/4}\), before the line's reflection sign is fixed.

**4. Reflections.** Every reflection is \(r^ct\), carrying position \(i\) to \(c-i\). Its binary invariant assignments form a palindromic word. In the orbit-word coordinates, the three-consecutive-ones condition becomes: no internal substring \(111\), and neither endpoint pair is \(11\). If \(n\) is odd, the orbit-word length is \(\ell=(n+1)/2\). For even \(n\), it is \(\ell=n/2+1\) when \(c\) is even (two fixed vertices), and \(\ell=n/2\) when \(c\) is odd (no fixed vertices). Hence
\[
Z_{r^ct}=F(\ell),\quad F(\ell)=\sum_{\substack{b_1,\ldots,b_\ell\in\{0,1\}\\b_1b_2=b_{\ell-1}b_\ell=0\\b_jb_{j+1}b_{j+2}=0}}(-1)^{b_1+\cdots+b_\ell}.
\]
The restriction \(b_1b_2=b_{\ell-1}b_\ell=0\) means neither pair has both bits one. In terms of the same transfer matrix, put \(a=(1,-1,-1,0)\) and \(b=(1,1,1,0)^\top\); then \(F(\ell)=aM^{\ell-2}b\), for \(\ell\ge2\). Direct matrix multiplication gives \(aM^j(M^2+I)b=0\) for \(j=0,1,2,3\). Cayley–Hamilton then gives this equality for every \(j\ge0\), so \(F(\ell+2)=-F(\ell)\). As \(F(2)=F(3)=-1\),
\[
F(\ell)=\begin{cases}1,&\ell\equiv0,1\pmod4,\\-1,&\ell\equiv2,3\pmod4.\end{cases}\tag{3}
\]
Combining (1), (3) and the three cases for \(\ell\), the reflection trace is \((-1)^q\) for \(n=4q,4q+1\); \((-1)^{q+c}\) for \(n=4q+2\); and \((-1)^{q+1}\) for \(n=4q+3\). This exactly matches the four representations in the table, including both even-cycle reflection classes. Equality of rational characters implies isomorphism of the \(\mathbb Q[D_n]\)-modules in question (the displayed summands are themselves rational representations). This proves the theorem.

## Verification
The standalone standard-library `verification.py` independently checks the graph–hypergraph identification, the signed augmented Lefschetz trace against direct oriented-simplex enumeration for small values, the transfer-matrix identities, all dihedral group elements through \(n=13\), and complete mod-two boundary ranks for \(7\le n\le12\). Invoke `python3 verification.py`. These finite tests check implementation and boundary cases; the all-\(n\) result follows from the symbolic transfer calculation and the cited homology concentration theorem.

## Relationship to prior work
Ghosh and Selvaraja (2026) define and study clique-free complexes, mainly proving shellability/decomposability results for chordal and clique-attached graph classes; they do not determine this squared-cycle dihedral representation. Kim and Kim (2021, Theorem 3.1) compute **mod-two Betti numbers** for the *same* tight cyclic triple hypergraph, and their Theorem 3.4 computes homotopy types for its **Alexander-dual noncover complex**. Those statements provide the concentrated-degree input but do not determine the action of rotations and reflections on the original complex's rational homology. The previously published dihedral orientation theorem for bounded-independence complexes of ordinary cycles treats different faces (forbidding induced independent sets of prescribed cardinality), not these consecutive-triple forbiddances. Similarly, existing cycle matching-complex dihedral calculations concern independent edge sets and do not imply the present character. These comparisons distinguish the exact objects and invariant rather than relying on dissimilar titles alone.

## Limitations
No integral torsion-freeness, sphere-wedge homotopy type, integral dihedral module, equivariant homotopy equivalence, or quotient-space homology is asserted. The homology-concentration input comes from the published mod-two theorem; the character itself is proved here using exact signed face traces. Unindexed prior equivariant formulas or a stronger general cyclic-hypergraph character theorem could subsume the finding; the identified literature does not contain such a statement.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (first posted 2026-02-10), https://arxiv.org/html/2602.09623v1. Definitions, introductory scope, and Sections 3–4.
2. J. Kim and M. Kim, *Domination numbers and noncover complexes of hypergraphs*, arXiv:2101.01850v1 (first posted 2021-01-06), https://arxiv.org/html/2101.01850v1. In particular Theorems 3.1 and 3.4; the paper uses mod-two coefficients.
3. *Dihedral orientation characters of bounded-independence spheres on cycles*, publicly indexed mathematical record (2026). Its bounded-independence complexes forbid induced independent subsets of prescribed size, unlike the present cyclic triple-avoidance complex.
4. *Complete dihedral homology characters of cycle matching complexes*, publicly indexed mathematical record (2026). Its matching-complex object differs from the present clique-free complex.
