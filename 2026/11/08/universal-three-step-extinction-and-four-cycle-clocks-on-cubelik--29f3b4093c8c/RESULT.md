# Universal three-step extinction and four-cycle clocks on cubelike edge networks

## Finding
Let \(r\ge2\), \(S\subset\mathbb F_2^r\setminus\{0\}\) be a set of \(s\) distinct nonzero binary vectors spanning \(\mathbb F_2^r\), and let their vector sum be nonzero. Put \(G=\operatorname{Cay}(\mathbb F_2^r,S)\); its vertices are binary vectors, and \(u,v\) are adjacent exactly when \(u+v\in S\). Set \(v=2^r\) and \(m=s2^{r-1}\), the numbers of vertices and edges of \(G\). Regard the \(m\) edges as sites, with two sites neighboring when their edges share a vertex in \(G\). Over any field \(\mathbb F_q\) with \(q\) a power of two, denote by \(B\) the adjacency matrix of this line graph.

**Theorem (complete edge-state dynamics).** The exact Jordan partition is
\[
 B\sim J_3(0)^{\oplus(v/2-2)}\oplus J_2(0)^{\oplus2}\oplus J_1(0)^{\oplus((s-3)v/2+2)}.
\]
The exponents are nonnegative integers. In particular, \(\operatorname{rank}B=v-2\), \(\operatorname{rank}B^2=v/2-2\) and \(B^3=0\).

For the neighbor-only synchronous rule \(x(t+1)=Bx(t)\), define extinction time \(\tau(x)=\min\{j\ge0:B^jx=0\}\). Its **exact population distribution** is
\[
\begin{array}{c|cccc}
 j&0&1&2&3\\\hline
 \#\{x:\tau(x)=j\}&1&q^{m-v+2}-1&q^{m-v/2+2}-q^{m-v+2}&q^m-q^{m-v/2+2}.
\end{array}
\]
All other extinction-time populations vanish. The maximum is exactly two when \(r=2\) and exactly three for \(r\ge3\).

For the self-inclusive rule \(y(t+1)=(I+B)y(t)\), every state is periodic immediately and its least period is in \(\{1,2,4\}\). The exact respective **numbers of labelled states of primitive periods** 1, 2, and 4 are
\[
 q^{m-v+2},\qquad q^{m-v/2+2}-q^{m-v+2},\qquad q^m-q^{m-v/2+2}.
\]
Dividing by the corresponding period gives primitive orbit counts. The global permutation has order two for \(r=2\), and order four for every \(r\ge3\).

## Assumptions and scope
The underlying cubelike graph is finite, simple, connected and undirected; connectedness is equivalent to \(S\) spanning. Sites in the dynamics are **edges of the original graph**, not its vertices. Distinctness of generators ensures no parallel edges. All adjacency sums use the finite field's characteristic-two addition. The generating-vector sum is \(c=\sum_{a\in S}a\) computed in \(\mathbb F_2^r\), not the scalar degree \(s\bmod2\). The results hold uniformly for every characteristic-two extension field; they do not assert a corresponding statement in odd characteristic.

## Proof
**Step 1 (incidence reduction).** Let \(M\) be the unsigned \(v\times m\) vertex-edge incidence matrix of \(G\). Each column has exactly two ones. Hence, over characteristic two, the edge-line adjacency is \(B=M^{\mathsf T}M\) (its diagonal is zero, since \(2=0\)). Write \(T=MM^{\mathsf T}\). Because \(G\) is \(s\)-regular, \(T=sI+A_G\), its mod-two Laplacian. Let \(R_a\) translate vertex functions by \(a\). Then
\[
T=\sum_{a\in S}(I+R_a).
\]
Each \((I+R_a)^2=0\), and the translations commute. Therefore \(T^2=0\), so \(B^3=M^{\mathsf T}T^2M=0\), without using the generator-sum condition.

**Step 2 (the exact rank of the vertex Laplacian).** Identify the group algebra \(\mathbb F_q[\mathbb F_2^r]\) with \(R=\mathbb F_q[z_1,\ldots,z_r]/(z_1^2,\ldots,z_r^2)\), where \(z_i=1+g_i\) for any binary group basis \(g_i\). Its augmentation ideal \(\mathfrak m=(z_1,\ldots,z_r)\) consists of elements with coefficient sum zero. The translation operator \(T\) acts by multiplication by
\[
 t=\sum_{a\in S}(1+g_a)\in\mathfrak m.
\]
Modulo \(\mathfrak m^2\), the linear part of \(t\) is \(\sum_{i=1}^r c_i z_i\), with \(c=\sum_{a\in S}a\ne0\). Complete this linear form to an invertible basis of \(\mathfrak m/\mathfrak m^2\). Choose \(y_1=t\) and \(y_2,\ldots,y_r\in\mathfrak m\) with these independent linear terms. In characteristic two every element of \(\mathfrak m\) has square zero, and an endomorphism sending \(z_i\) to \(y_i\) is an automorphism: it is invertible on \(\mathfrak m/\mathfrak m^2\), hence on every associated graded piece and therefore on the finite filtered algebra. Consequently, multiplication by \(t=y_1\) has rank \(v/2\) and satisfies \(\ker T=\operatorname{im}T\subset\mathfrak m\).

**Step 3 (incidence and the top monomial).** Since \(G\) is connected, \(\operatorname{im}M=\mathfrak m\) has dimension \(v-1\), and \(\ker M^{\mathsf T}\) is spanned by the all-one vertex vector \(\omega=\sum_{g\in\mathbb F_2^r}g\). As \(v\) is even, \(\omega\in\mathfrak m\). Thus \(\operatorname{rank}B=\dim\mathfrak m-1=v-2\).

Now \(\ker T\subset\mathfrak m\) and \(\dim\ker T=v/2\), so \(\dim T(\mathfrak m)=v/2-1\). The vector \(\omega\) equals the socle monomial \(z_1\cdots z_r\). Under the above invertible change of variables it is a nonzero multiple of \(y_1\cdots y_r\). Because \(r\ge2\), the product \(y_2\cdots y_r\) lies in \(\mathfrak m\), whence \(\omega\in T(\mathfrak m)\). It follows that
\[
\operatorname{rank}B^2=\dim T(\mathfrak m)-\dim(\ker M^{\mathsf T}\cap T(\mathfrak m))=v/2-2.
\]

**Step 4 (Jordan counts).** Write \(a_j\) for the number of zero Jordan blocks of size \(j\). Since \(B^3=0\),
\[
 a_3=\operatorname{rank}B^2=v/2-2,\quad a_2=\operatorname{rank}B-2\operatorname{rank}B^2=2,
\]
\[
 a_1=m-2a_2-3a_3=(s-3)v/2+2.
\]
These identities prove the Jordan partition, including the case \(r=2\), for which the size-three multiplicity is zero.

**Step 5 (all labelled temporal populations).** The ranks give \(\dim\ker B=m-v+2\), \(\dim\ker B^2=m-v/2+2\), and \(\ker B^3=\mathbb F_q^m\). Successive differences of powers of \(q\) give the extinction-time counts. For \(U=I+B\), characteristic two gives \(U^2=I+B^2\) and \(U^4=I\). Moreover \(\ker(U-I)=\ker B\) and \(\ker(U^2-I)=\ker B^2\), giving primitive-period counts at periods 1, 2, 4. The nonzero rank \(B^2=v/2-2\) for \(r\ge3\) forces global period four.

**Boundary illustrating the hypothesis.** Take \(r=3\), \(S=\{100,010,001,111\}\), whose xor sum is zero. Its cubelike graph is \(K_{4,4}\), and its line graph is the 16-vertex rook graph \(K_4\square K_4\); over characteristic two its adjacency is \(J_4\otimes I_4+I_4\otimes J_4\), whose square vanishes. The size-three blocks from the theorem are absent. This does not claim a general classification for zero-xor generating sets.

## Verification
The standalone script `check_matrix.py` constructs the actual line graph and checks powers and ranks over \(\mathbb F_2\), independently of the group-ring proof. It checks every connected binary generating set in dimensions two and three (96 cases), plus 200 pseudorandom deterministic samples in dimensions four and five. Its captured output is in `check_matrix.out`.

Independently, `check_orbits.py` enumerates all labelled initial states for four small eligible examples (including the three-cube and two distinct four-regular cubelike graphs on eight vertices), comparing each transient depth and each primitive period with the displayed counts, and verifies that the excluded \(K_{4,4}\) example has square-zero edge adjacency. Its captured output is `check_orbits.out`. These finite checks are corroboration; the proof above establishes the quantified all-dimensional claim. All scripts use standard Python 3 only.

## Relationship to prior work
Wolfram's 1983 work introduced systematic study of finite cellular-automaton state transitions. Martin, Odlyzko and Wolfram's 1984 algebraic development treats additive rules and periodic one- and multidimensional site lattices, but its proved multidimensional results do not compute the characteristic-two Jordan partition for **line graphs of arbitrary connected cubelike graphs**. Mančinska, Pivotto, Roberson and Royle's 2018 primary work defines and studies cubelike graph cores and graph coverings; their subject is homomorphisms, not edge-state automaton orbit counts. The group-algebra, incidence and rank methods used here are standard; originality is asserted only for the exact joint cubelike-edge Jordan and temporal census conditional on nonzero generator sum.

Published mathematical-research records were compared for line-graph dynamics, zero-primary Jordan forms and parameter-covering results, as well as related parity automata on distance-two cubes and complete multipartite graphs. Those concern different state graphs or give no implication of the present Jordan partition. Search is not proof of absence of prior publication.

## Limitations
This is a mathematical proof and self-review, not an independent validation. An earlier unindexed identity or theorem on modular ranks of line graphs or Cayley graph algebras may subsume the result; a comprehensive historical-priority determination is not claimed. The classification assumes connectedness, distinct nonzero generators, nonzero generator xor and characteristic-two finite fields. The excluded zero-xor case can have a different Jordan partition. No claims concern arbitrary fields, nonlinear rules, asynchronous updates or physical realizations. The precise date July 1, 1983 is the verified day-specific public anchor for the classical cellular-automaton research line, not a claimed publication date of the result above.

## References
1. S. Wolfram, *Statistical mechanics of cellular automata*, Reviews of Modern Physics 55 (1983), 601–644. DOI: 10.1103/RevModPhys.55.601. Publisher identifies July 1, 1983.
2. O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics 93 (1984), 219–258. DOI: 10.1007/BF01223745. Author-hosted lawful full text: https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf.
3. L. Mančinska, I. Pivotto, D. E. Roberson and G. F. Royle, *Cores of Cubelike Graphs*, arXiv:1808.02051v1 (August 6, 2018), https://arxiv.org/abs/1808.02051.
