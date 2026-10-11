# Zero forcing in generating graphs of two-generated finite p-groups

## Finding

Let \(G\) be a finite noncyclic \(p\)-group with minimal generator number \(d(G)=2\), let \(\Phi(G)\) be its Frattini subgroup, put \(f=|\Phi(G)|\), \(s=(p-1)f\), and let \(\Gamma(G)\) be the generating graph on \(G\setminus\{1\}\), where two distinct vertices are adjacent exactly when they generate \(G\). Then \[\Gamma(G)\cong (f-1)K_1\;\dot\cup\;K_{s,s,\ldots,s},\] with \(p+1\) equal multipartite parts. Writing \(N=|G|-1=p^2f-1\) and \(m=(p^2-1)f\), if \(s=1\) then \(G\cong C_2^2\) and \[\mathcal Z(\Gamma(G);x)=3x^2+x^3,\qquad \operatorname{mr}(\Gamma(G))=1.\] If \(s\ge2\), then \[\mathcal Z(\Gamma(G);x)=\binom{p+1}{2}s^2x^{N-2}+mx^{N-1}+x^N,\qquad Z(\Gamma(G))=N-2.\] The minimum zero forcing sets are exactly the complements of unordered generating pairs. Over the real symmetric minimum-rank model, \[\operatorname{mr}(\Gamma(G))=2\text{ if }s=2,\qquad \operatorname{mr}(\Gamma(G))=3\text{ if }s\ge3.\] Consequently \(Z=M\) exactly when \(s\le2\), while \(Z=M+1\) for \(s\ge3\). The zero forcing polynomial determines \(p\) and \(|\Phi(G)|\): its degree gives \(|G|\), and the coefficient of \(x^{N-1}\) gives \(m=|G|-f\).

Thus a graph polynomial coming from forcing dynamics records two classical generation invariants: the prime \(p\) and the Frattini size \(|\Phi(G)|\). Its lowest nonzero coefficient is exactly the number of unordered generating pairs.

## Assumptions and scope

Let \(G\) be a finite noncyclic \(p\)-group with
\[
d(G)=2.
\]
Let \(\Phi(G)\) be its Frattini subgroup and put
\[
f=|\Phi(G)|,
\qquad
s=(p-1)f.
\]
The generating graph \(\Gamma(G)\) has vertex set \(G\setminus\{1\}\); distinct vertices \(x,y\) are adjacent exactly when
\[
\langle x,y\rangle=G.
\]

For a finite simple graph \(X\), write
\[
\mathcal Z(X;x)=\sum_{k=0}^{|V(X)|}z(X;k)x^k
\]
for its zero forcing polynomial. The real symmetric minimum rank is
\[
\operatorname{mr}(X)=\min_{A\in\mathcal S(X)}\operatorname{rank}A,
\]
where \(\mathcal S(X)\) consists of real symmetric matrices whose off-diagonal nonzero pattern is exactly \(X\), and
\[
M(X)=|V(X)|-\operatorname{mr}(X).
\]

## Proof

Burnside's basis theorem gives
\[
G/\Phi(G)\cong \mathbb F_p^2,
\]
and two elements generate \(G\) exactly when their images form a basis of this quotient.

Every nonidentity element of \(\Phi(G)\) is therefore isolated in \(\Gamma(G)\). The remaining elements are partitioned by the one-dimensional subspaces of \(G/\Phi(G)\). There are
\[
p+1
\]
such projective lines, and the preimage of the nonzero points of each line has size
\[
(p-1)f=s.
\]
Two non-Frattini vertices generate \(G\) exactly when their images lie on different lines. Hence
\[
\Gamma(G)\cong (f-1)K_1\;\dot\cup\;H,
\qquad
H=K_{s,s,\ldots,s},
\tag{1}
\]
with \(p+1\) equal parts. In particular
\[
|V(H)|=m=(p^2-1)f,
\qquad
N=|V(\Gamma(G))|=p^2f-1.
\]

Every isolated vertex must belong to every zero forcing set. It therefore remains to analyze \(H\).

If \(s=1\), then necessarily \(p=2\) and \(f=1\), so \(H=K_3\). Thus
\[
\mathcal Z(H;x)=3x^2+x^3
\]
and
\[
Z(H)=2.
\]

Assume now \(s\ge2\). Color all but two vertices blue. If the two white vertices lie in distinct multipartite parts, choose a blue vertex in the part of one white vertex. It is nonadjacent to that white vertex and adjacent to the other, so it has a unique white neighbor and forces it. A blue vertex in the other part then forces the remaining white vertex. Hence the complement of any cross-part pair is zero forcing.

If the two white vertices lie in the same part, every blue vertex is adjacent either to both of them or to neither, so no force is possible. More generally, no coloring with at least three white vertices can complete: a first force can occur only when all but one white vertex lie in one part, and after that force at least two indistinguishable white vertices remain in that part. Consequently
\[
Z(H)=m-2,
\]
and its minimum zero forcing sets are exactly the complements of cross-part pairs.

A cross-part pair is precisely an unordered generating pair of \(G\). Their number is
\[
\binom{p+1}{2}s^2.
\tag{2}
\]
Every set of size \(m-1\) in \(H\) is zero forcing because the sole white vertex has a blue neighbor, and the whole vertex set is zero forcing. Therefore
\[
\mathcal Z(H;x)
=
\binom{p+1}{2}s^2x^{m-2}
+mx^{m-1}
+x^m.
\tag{3}
\]
Adding the forced \(f-1\) isolated vertices shifts every exponent by \(f-1\), giving
\[
\mathcal Z(\Gamma(G);x)
=
\binom{p+1}{2}s^2x^{N-2}
+mx^{N-1}
+x^N.
\tag{4}
\]

We next compute real symmetric minimum rank. Isolated vertices contribute zero blocks, so it is enough to compute \(\operatorname{mr}(H)\).

For \(s=1\), \(H=K_3\), and an all-ones matrix shows
\[
\operatorname{mr}(H)=1.
\]

For \(s=2\), use the symmetric bilinear form
\[
B((a,b),(c,d))=ad+bc.
\]
For multipartite part \(i\), choose distinct positive numbers \(t_i\), for example \(t_i=2^i\), and assign its two vertices the vectors
\[
(1,t_i),\qquad(1,-t_i).
\]
The two vectors in the same part are orthogonal, while vectors from different parts have pairings \(\pm t_i\pm t_j\ne0\). The resulting real symmetric pattern matrix has rank \(2\), so
\[
\operatorname{mr}(H)\le2.
\]
The graph is not a disjoint union of a clique and isolated vertices, so rank \(1\) is impossible; hence
\[
\operatorname{mr}(H)=2.
\]

For \(s\ge3\), use the Lorentz form
\[
L(u,v)=-u_0v_0+u_1v_1+u_2v_2.
\]
For distinct real parameters \(t_i\), assign every vertex in part \(i\) the isotropic vector
\[
v_i=(1+t_i^2,\,1-t_i^2,\,2t_i).
\]
Then
\[
L(v_i,v_i)=0,
\qquad
L(v_i,v_j)=-2(t_i-t_j)^2\ne0
\]
for \(i\ne j\). Three distinct \(v_i\) span \(\mathbb R^3\), so this gives a rank-three pattern matrix and
\[
\operatorname{mr}(H)\le3.
\]

Rank \(2\) is impossible when \(s\ge3\). Indeed, a rank-two real symmetric pattern matrix factors through a nondegenerate symmetric bilinear form on a two-dimensional real space. Within any multipartite part there would be at least three nonzero vectors pairwise orthogonal. The orthogonal complement of a nonzero vector is one-dimensional, so all vectors in that part must lie on one isotropic line. A nondegenerate symmetric form in dimension two has at most two isotropic lines, whereas \(H\) has \(p+1\ge3\) parts and different parts cannot use the same isotropic line because cross-part pairings must be nonzero. Hence
\[
\operatorname{mr}(H)=3.
\]

Thus
\[
\operatorname{mr}(\Gamma(G))=
\begin{cases}
1,&s=1,\\
2,&s=2,\\
3,&s\ge3.
\end{cases}
\]
Since \(M=N-\operatorname{mr}\) and \(Z=N-2\) for \(s\ge2\),
\[
Z=M
\quad\Longleftrightarrow\quad
s\le2,
\]
while
\[
Z=M+1
\]
for \(s\ge3\).

Finally, the polynomial recovers the Frattini data. Its degree gives
\[
|G|=N+1.
\]
For \(s\ge2\), the coefficient of \(x^{N-1}\) is
\[
m=(p^2-1)f=|G|-f,
\]
so
\[
f=|G|-m,
\qquad
p=\sqrt{\frac{|G|}{f}}.
\]
The exceptional \(s=1\) polynomial is uniquely the \(C_2^2\) case.

## Verification

The accompanying `verify.py` constructs the graph directly from its Frattini/projective-line decomposition for representative pairs \((p,f)\). It exhaustively enumerates the entire zero forcing polynomial for the cases of graph order at most eight, and for larger test cases it checks every possible two-vertex complement against the theorem's minimum-set classification.

The verifier also constructs the rank-one, rank-two, and rank-three real symmetric witnesses using exact integer arithmetic and computes their ranks exactly over the rationals.

Exact replay output:

```text
p=2, f=1: n=3, exhaustive polynomial={2: 3, 3: 1}, mr=1
p=2, f=2: n=7, exhaustive polynomial={5: 12, 6: 6, 7: 1}, mr=2
p=2, f=4: n=15, structural Z=13, min_sets=48, mr=3
p=3, f=1: n=8, exhaustive polynomial={6: 24, 7: 8, 8: 1}, mr=2
p=3, f=2: n=17, structural Z=15, min_sets=96, mr=3
p=5, f=1: n=24, structural Z=22, min_sets=240, mr=3
VERIFY_OK
```

The finite checks are corroborative only. The arbitrary-group theorem follows from Burnside's basis theorem, the complete multipartite decomposition, the forcing classification, and the explicit bilinear-form witnesses.

## Relationship to prior work

Breuer, Guralnick, Lucchini, Maróti, and Nagy use this generating graph on nonidentity elements, with two vertices adjacent when they generate the group. Their 2010 paper has primary Mathematics Subject Classification \(20P05\) and studies Hamiltonian cycles and generation structure. The inspected full text uses Frattini-subgroup arguments but does not discuss zero forcing or graph minimum rank.

Crestani and Lucchini later study the generating graph of finite soluble groups and prove connectivity properties for the nonisolated component. Their accessible abstract does not state the zero forcing or minimum-rank conclusions considered here.

General zero-forcing-polynomial theory already gives universal facts about the top coefficients and multiplicativity over components, and zero forcing of complete multipartite graphs is a standard special case. Accordingly, the claim here is not that those graph-theoretic ingredients are new in isolation. The new algebraic content is the exact identification of minimum forcing sets with generating pairs, recovery of \(p\) and \(|\Phi(G)|\) from the polynomial, and the sharp real minimum-rank transition at \((p-1)|\Phi(G)|=1,2,\ge3\).

## Limitations

The theorem is restricted to finite noncyclic \(p\)-groups with minimal generator number two. Higher generator rank replaces the projective-line decomposition by a more complicated independence graph on \(G/\Phi(G)\).

The minimum rank is over real symmetric matrices. Other coefficient fields may have different isotropic-line behavior.

The bare zero forcing number of the complete multipartite component follows from standard graph-theoretic results; the value of the present statement lies in the group-theoretic interpretation, exact minimizer identification, polynomial recovery, and minimum-rank phase transition.

The 2013 finite-soluble-group generating-graph paper was available through abstract/repository material rather than full text in the accessible path, so it remains a residual source-comparison risk.

## References

1. T. Breuer, R. M. Guralnick, A. Lucchini, A. Maróti, and G. P. Nagy, “Hamiltonian cycles in the generating graphs of finite groups,” *Bulletin of the London Mathematical Society* 42 (2010), 621–633. DOI: 10.1112/blms/bdq017. First published 8 June 2010.
2. E. Crestani and A. Lucchini, “The generating graph of finite soluble groups,” *Israel Journal of Mathematics* 198 (2013), 63–74. DOI: 10.1007/s11856-012-0190-1.
3. B. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910. DOI: 10.1016/j.dam.2018.11.033.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
