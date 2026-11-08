# Dihedral homology characters of three-cut complexes of complementary cycles

## Finding
For each integer \(n\ge5\), let \(G_n=\overline{C_n}\) be the graph on \(\mathbb Z/n\mathbb Z\) in which two distinct vertices are adjacent precisely when they are not cyclic neighbors. Let \(X_n=\Delta_3(G_n)\) be the **ordinary three-cut complex**: its facets are the complements of three-vertex sets inducing disconnected subgraphs of \(G_n\). The dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(s(i)=-i\) modulo \(n\).

Write \(n=4p+t\), \(0\le t<4\). All reduced rational homology of \(X_n\) vanishes except in degree
\[
q_n=\begin{cases}2p-2,&t=0,\\2p-1,&t=1,2,3.\end{cases}
\]
The surviving vector space has dimension three when \(4\mid n\), and dimension one otherwise. These **dimensions were previously known** through complementary path-complex homology; the finding here is the complete dihedral action.

If \(4\nmid n\), the unique nonzero rational homology is a line on which \(r\) acts by \(+1\), while \(s\) acts by \(+1\) for \(n\equiv1,2,3\pmod8\) and by \(-1\) for \(n\equiv5,6,7\pmod8\).

If \(4\mid n\), the unique nonzero rational homology decomposes as \(L_n\oplus W\), where \(L_n\) is a line on which
\[
r|_{L_n}=-1,\qquad s|_{L_n}=(-1)^{n/4+1},
\]
and \(W\) is a two-dimensional rational module represented by
\[
r|_W=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
s|_W=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
These matrices satisfy the dihedral relations because \(4\mid n\). In particular, the three-dimensional module is not the sum of three real one-dimensional characters: its two-dimensional constituent has quarter-turn eigenvalues \(\pm i\).

## Assumptions and scope
All complexes are finite, abstract, and include the empty simplex; homology is reduced simplicial homology over \(\mathbb Q\), with the standard signed permutation action on oriented simplices. The cyclic adjacency defining \(C_n\) is by steps \(\pm1\) modulo \(n\). The statement includes every integer \(n\ge5\) and every element of \(D_n\). It asserts no integral module decomposition, shellability, or homotopy classification of the cut complex.

## Proof
**1. Identify the dual.** A disconnected three-vertex induced subgraph of \(G_n\) must have an isolated vertex (there are only three vertices). That vertex has both of the other two among its two cyclic neighbors. Conversely, the three cyclic consecutive vertices centered at any vertex induce one edge and an isolated vertex in \(G_n\). Thus the disconnected triples are exactly \(\{i-1,i,i+1\}\) as \(i\) runs modulo \(n\). Define \(Y_n\) to be the simplicial complex of subsets containing no three cyclically consecutive vertices. By the definition of combinatorial Alexander duality, \(X_n=Y_n^*\).

**2. Homological concentration.** Alilooee--Faridi, Theorem 4.6, applies to the complementary facet complex of the length-three path ideal of \(C_n\). That complex is precisely \(X_n\): its facets are the complements of the cyclic consecutive triples. Substituting \(3\) for their path length \(t\), their theorem gives \(\widetilde H_{2p-2}(X_n;\mathbb Q)\cong\mathbb Q^3\) when \(n=4p\), and \(\widetilde H_{2p-1}(X_n;\mathbb Q)\cong\mathbb Q\) when \(n=4p+1,4p+2,4p+3\), with all other reduced groups zero. Combinatorial Alexander duality similarly concentrates \(\widetilde H_*(Y_n;\mathbb Q)\) in degree \(d_n=n-q_n-3\) with the same rank.

**3. Signed Lefschetz enumeration.** For a dihedral permutation \(g\), the reduced Lefschetz number of \(g\) on \(Y_n\) is
\[
\widetilde\Lambda(g;Y_n)=\sum_{\substack{F\in Y_n\\gF=F}}(-1)^{|F|-1}\operatorname{sgn}(g|_F).
\]
The empty face contributes \(-1\). Every fixed face is a union of \(k\) vertex orbits of \(g\). Since the permutation on an orbit of size \(h\) has sign \((-1)^{h-1}\), its total contribution is \((-1)^{k-1}\), independent of the orbit lengths. Therefore \(\widetilde\Lambda(g;Y_n)=-Z_g\), where \(Z_g\) sums \((-1)^k\) over selections of \(k\) vertex orbits whose union contains no cyclic consecutive triple. As homology is concentrated in one degree, its character on \(Y_n\) is \(\chi_Y(g)=(-1)^{d_n+1}Z_g\).

**4. Rotations.** For \(g=r^a\) put \(h=\gcd(n,a)\), with \(\gcd(n,0)=n\). Its vertex orbits are the congruence classes modulo \(h\). Thus orbit selections correspond exactly to length-\(h\) binary cyclic words with no run of three ones, weighted by \((-1)^{\text{number of ones}}\), including the natural periodic interpretations when \(h=1,2\). On the ordered two-bit states \(00,01,10,11\), the signed transfer matrix is
\[
T=\begin{pmatrix}
1&-1&0&0\\
0&0&1&-1\\
1&-1&0&0\\
0&0&1&0
\end{pmatrix}.
\]
Consequently \(Z_{r^a}=\operatorname{tr}(T^h)\). The characteristic polynomial of \(T\) is \(\lambda(\lambda-1)(\lambda^2+1)\), hence for every positive \(h\),
\[
Z_{r^a}=1+2\cos(\pi h/2)=
\begin{cases}3,&h\equiv0\pmod4,\\-1,&h\equiv2\pmod4,\\1,&h\text{ odd}.\end{cases}
\]

**5. Reflections.** Let \(f_a(i)=a-i\), so \(f_a=r^as\). For odd \(n=2m+1\), all reflections are conjugate, and an invariant cyclic word is encoded by \(m+1\) successive orbit bits. For even \(n=2m\), the reflection \(f_0\) fixes two vertices and similarly has \(m+1\) orbit bits; \(f_1\) fixes no vertices and has \(m\) orbit bits. In every case, the orbit-bit string has no three consecutive ones and also forbids \(11\) at each endpoint (these two extra restrictions come from repeated orbit bits at the mirror axes). Put
\[
v=(1,-1,-1,0),\qquad e=(1,1,1,0)^{\mathsf T},\qquad F_j=vT^je.
\]
The weighted count of a permitted string of length \(j+2\) is exactly \(F_j\). Direct multiplication gives \((T^2+I)e=0\) and \(F_0=F_1=-1\); hence \(F_{j+2}=-F_j\) and the values repeat \((-1,-1,1,1)\). Therefore
\[
Z_{f_a}=\begin{cases}
F_{(n-3)/2},&n\text{ odd},\\
F_{n/2-1},&n\text{ even},\ a\text{ even},\\
F_{n/2-2},&n\text{ even},\ a\text{ odd}.
\end{cases}
\]
This covers every reflection for \(n\ge5\).

**6. Transport through the duality.** The signed chain-complement map in combinatorial Alexander duality intertwines a vertex permutation \(g\) with its action on the dual complex up to the sign of \(g\) on the full ordered vertex set. Thus
\[
\chi_X(g)=\operatorname{sgn}_{\mathfrak S_n}(g)\,\chi_Y(g)
\]
(the cohomology dual does not change the rational character). For \(r\), the ambient sign is \((-1)^{n-1}\). For \(f_a\), it is \((-1)^{(n-1)/2}\) if \(n\) is odd, \((-1)^{n/2-1}\) if \(n\) is even and \(a\) even, and \((-1)^{n/2}\) if \(n\) is even and \(a\) odd. Substitute the rotation and reflection values of Steps 4--5. For \(4\nmid n\), the result is the stated one-dimensional character. For \(4\mid n\), the rotation traces are \(3,-1,-1,-1\) as \(a\equiv0,1,2,3\pmod4\), and the reflection traces are \((-1)^{n/4+1+a}\). These are precisely the character of \(L_n\oplus W\). Rational characters determine rational representations of finite groups, completing the proof.

## Verification
The standalone `verify.py` enumerates all faces of \(X_n\) and computes signed reduced Lefschetz traces for **every element of \(D_n\)** for each \(5\le n\le15\), comparing against the closed-form character of the theorem. For \(5\le n\le10\) it additionally forms exact mod-two boundary matrices and checks the previously known homology ranks. The recorded output is `verification_output.txt`. These finite tests are independent cross-checks, **not substitutes for the preceding all-parameter proof**. Run `python3 verify.py` with the standard library.

## Relationship to prior work
Bayer--Denker--Jelić Milutinović--Rowlands--Sundaram--Xue (first publicly posted 2023-04-26) introduce and study ordinary cut complexes, including cyclic homology representations for \(\Delta_k(C_n)\). Their cyclic theorem treats the **cycle graph itself**, whereas the present result treats the **complement graph** and computes the full dihedral action. Alilooee--Faridi (preprint dated 2013-01-03; published 2015) already determine the nonequivariant field-homology ranks of the identical complementary path complex; these dimensions are explicitly inherited, not new. Björner--Tancer provide the combinatorial Alexander-duality framework; the equivariant sign is tracked explicitly here. No consulted result gives the stated representation for the complementary cycles. An unindexed equivalent calculation remains possible.

## Limitations
Only rational representations are classified. No claim is made about integral torsion in homology, integral representations, equivariant homotopy type, or independence of the cited nonequivariant homology theorem. The finite executable check covers \(5\le n\le15\); the all-\(n\) conclusion relies on the transfer-matrix proof plus the published homology calculation. The completeness of searches cannot exclude all unpublished or unindexed equivalent results.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted 2023-04-26), especially Definition 2.7 and Theorem 7.16. https://arxiv.org/abs/2304.13675
2. A. Alilooee, S. Faridi, *On the Resolution of Path Ideals of Cycles*, preprint dated 2013-01-03, Theorem 4.6; *Communications in Algebra* 43 (2015), 5413--5433. https://www.mathstat.dal.ca/~faridi/research/newpath.pdf
3. A. Björner, M. Tancer, *Combinatorial Alexander Duality -- a Short and Elementary Proof*, arXiv:0710.1172 (first posted 2007-10-05), especially Sections 3--4. https://arxiv.org/abs/0710.1172
