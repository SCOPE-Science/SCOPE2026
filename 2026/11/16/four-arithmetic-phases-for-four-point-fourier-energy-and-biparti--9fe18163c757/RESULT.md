# Four arithmetic phases for four-point Fourier energy and bipartite collision-optimal labels

## Finding
Let \(N\ge 8\) be an integer and \(A\subset\mathbb Z_N\) have exactly four elements. Its ordered additive energy is
\[
 E_+(A)=\#\{(a,b,c,d)\in A^4:a+b=c+d\}.
\]
Then the exact largest energy is
\[
 M_N=\max_{|A|=4}E_+(A)=
 \begin{cases}
 64,&4\mid N,\\
 52,&4\nmid N,\ 5\mid N,\\
 48,&4\nmid N,\ 5\nmid N,\ 2\mid N,\\
 44,&2\nmid N,\ 5\nmid N.
 \end{cases}
\]
Every maximizing \(A\) has exactly the following form, up to translation: a coset of the subgroup of order four in the first case; a five-element subgroup coset minus one point in the second; the union of two distinct cosets of the order-two subgroup in the third; or a four-term arithmetic progression \(\{x,x+d,x+2d,x+3d\}\), with \(d\) of additive order at least seven, in the fourth. These descriptions are exhaustive.

For the complete bipartite graph \(K_{4,N-4}\), label its four-vertex shore by \(A\) and the other shore by its complement. Let \(f_A(x,y)\) indicate its directed edges on \(\mathbb Z_N^2\), and define its Fourier collision dimension by
\[
 D_4(f_A)=\frac{\big(\sum_{u,v}|\widehat f_A(u,v)|^2\big)^2}{\sum_{u,v}|\widehat f_A(u,v)|^4},\qquad
 \widehat f_A(u,v)=\frac1N\sum_{x,y}f_A(x,y)e^{-2\pi i(ux+vy)/N}.
\]
Set \(T_N=NM_N-256\). The sharp minimum, over every cyclic labeling of this graph, is
\[
 \boxed{\displaystyle
 \min_A D_4(f_A)=
 \frac{N^4[8(N-4)]^2}
 {[8(N-4)]^4+2(N-8)^4T_N+16T_N^2}.}
\]
All minimizers are exactly the four-set configurations listed above. This is a collision-dimension result, not a claim to optimize the distinct Fourier \(\ell^1/\ell^2\) ratio.

## Assumptions and scope
All sums, differences, and subgroup cosets are in the cyclic additive group \(\mathbb Z_N\). Four-point sets have four *distinct* elements. Both orientations of each bipartite edge are included; the transform on \(\mathbb Z_N^2\) is unitary under counting measure. The enumeration of maximizers concerns every integer \(N\ge8\), with no primality or generic-position assumption. The stated classification uses the additive order of a progression step, not necessarily a unit modulo \(N\).

## Proof
For \(t\in\mathbb Z_N\) let \(r(t)=|A\cap(A+t)|\). By counting ordered differences,
\[
 E_+(A)=\sum_t r(t)^2,\quad r(0)=4,\quad r(-t)=r(t),\quad \sum_{t\ne0}r(t)=12.
\]
The translation stabilizer \(H=\{t:A+t=A\}\) is a subgroup, with \(r(t)=4\) exactly when \(t\in H\). Its order divides four, so it has order one, two, or four.

If \(|H|=4\), the four-point set is a coset of \(H\), with energy \(64\), the universal bound \(E_+(A)\le |A|^3\). If \(|H|=2\), then \(A\) is the inverse image of a two-point set in \(\mathbb Z_N/H\). The quotient two-point set has no nontrivial stabilizer, otherwise \(|H|=4\). Its additive energy is \(6\). Each additive quadruple lifts in \(|H|^3=8\) ways, so \(E_+(A)=48\). Conversely every union of two order-two cosets not forming a single order-four coset has energy \(48\).

Suppose \(|H|=1\). For nonzero \(t\), \(r(t)\le3\). At an involution \(h\) of order two, if one exists, \(r(h)\) is even and therefore belongs to \(\{0,2\}\). Pair every remaining nonzero difference with its negative, and write its common multiplicity as \(s_j\in\{0,1,2,3\}\). When \(N\) is odd, or when \(N\) is even and \(r(h)=0\), the positive multiplicities sum to six, yielding
\[
 E_+(A)=16+2\sum_j s_j^2\le16+2(3^2+3^2)=52.
\]
The maximum requires exactly two pairs of multiplicity three. Apart from this maximum, the largest possible sum of squares of positive integers at most three summing to six is \(3^2+2^2+1^2=14\); hence every such nonmaximal configuration has energy at most \(44\). When \(N\) is even and \(r(h)=2\), the remaining paired multiplicities sum to five and
\[
 E_+(A)=16+2^2+2\sum_j s_j^2\le16+4+2(3^2+2^2)=46.
\]

It remains to analyze \(r(d)=3\), which any energy-\(52\) configuration must possess and every odd-order energy-\(44\) configuration must possess. The directed arrows \(x\mapsto x+d\) internal to \(A\) number three, and every vertex has internal indegree and outdegree at most one. Therefore they form either a path through all four vertices, or a directed triangle and an isolated vertex. In the triangle case \(d\) has additive order three. The other six nonzero ordered differences from/to the isolated vertex have multiplicity one if the quotient by the triangle subgroup is of odd order; if that quotient has an element of order two and the isolated vertex is in its corresponding coset, coincidences can raise their multiplicities to two. In all cases this configuration has energy at most \(46\), and on odd-order groups its energy is \(40\). Thus it never gives energy \(52\), nor energy \(44\) for odd \(N\).

In the path case \(A\) is a progression of four terms with step \(d\). Let \(q\) be the additive order of \(d\); then \(q\ge4\). Direct difference counting in this four-term progression gives energy \(64\) if \(q=4\), energy \(52\) if \(q=5\), energy \(46\) if \(q=6\), and energy \(44\) if \(q\ge7\). In the trivial-stabilizer case \(q\ne4\). Hence energy \(52\) occurs exactly for a four-of-five subgroup coset; at odd order without a subgroup of order five the maximal energy is \(44\) and its equality cases are exactly the claimed progressions. At even order without four- or five-torsion, the trivial-stabilizer energy is at most \(46\), strictly below the available order-two construction of energy \(48\). Together these facts prove all four branches and their complete equality classifications.

For the graph assertion let \(S(u)=\sum_{a\in A}e^{-2\pi iua/N}\). Fourier transformation of
\[
 f_A(x,y)=\mathbf1_A(x)+\mathbf1_A(y)-2\mathbf1_A(x)\mathbf1_A(y)
\]
gives \(\widehat f_A(0,0)=8(N-4)/N\), two coordinate-axis families \(\widehat f_A(u,0)=\widehat f_A(0,u)=(N-8)S(u)/N\) for \(u\ne0\), and \(\widehat f_A(u,v)=-2S(u)S(v)/N\) when both indices are nonzero. By character orthogonality,
\[
 \sum_{u\ne0}|S(u)|^4=NE_+(A)-256=:T(A).
\]
Consequently
\[
 \sum_{u,v}|\widehat f_A(u,v)|^4=
 \frac{[8(N-4)]^4+2(N-8)^4T(A)+16T(A)^2}{N^4}.
\]
Parseval gives \(\sum_{u,v}|\widehat f_A(u,v)|^2=8(N-4)\). The fourth-power sum increases strictly with \(T(A)>0\) (and in particular at \(N=8\), because of its positive quadratic term), so its collision dimension is minimized exactly when \(E_+(A)=M_N\). Inserting \(T_N=NM_N-256\) proves the formula and the equality class.

## Verification
The companion Python script `checker.py` uses exact integers to enumerate all \(278200\) four-element sets for cyclic orders \(8\) through \(33\), independently evaluates energy by ordered differences, and compares every optimum and equality configuration with the four-case formula. It also checks \(60\) examples of the bipartite graph energy identity through direct edge-pair difference counting, independently of the Fourier derivation. These finite checks are additional reproducibility evidence; the all-order theorem follows from the above argument, not from enumeration.

## Relationship to prior work
Gupta, Ferguson, Iosevich, Iosevich, Tian and Song introduced the graph collision-dimension framework and exact edge-energy identity (2026, arXiv:2610.31807). Ferguson and collaborators subsequently derived complete-bipartite Fourier-ratio reduction formulas and treated two- and three-vertex small shores, while posing further questions for four-vertex shores (2026, arXiv:2610.36276). Their minimization concerns Fourier \(\ell^1\), whereas this finding solves the exact fourth-moment/collision objective. Standard four-point additive-energy identities are used but not claimed as novel. Existing four-point Wiener-minimizer results address a different Fourier moment. Possible equivalent older classifications in additive combinatorics remain a priority risk.

## Limitations
The result concerns only four-point subsets and only the collision dimension \(D_4\), not the minimum Fourier ratio or arbitrary graph families. The theorem's equality classifications are up to translation and do not count label permutations. Related small-set energy classifications outside the inspected sources might imply this result. The computations cannot independently establish infinite-order assertions; no independent mathematical or priority audit has been performed.

## References
- V. Gupta, S. Ferguson, A. Iosevich, J. Iosevich, H. Tian, B. Song, *Additive energy and Fourier complexity of graphs*, publicly posted 22 October 2026, https://arxiv.org/abs/2610.31807 .
- S. Ferguson, V. Gupta, A. Iosevich, J. Iosevich, C. Kelly, G. Smith, S. Yang, *Edge complexity of complete bipartite and complete multipartite graphs*, publicly posted 26 October 2026, https://arxiv.org/abs/2610.36276 .
- T. Tao and V. Vu, *Additive Combinatorics*, Cambridge University Press, 2006, background on additive energy and finite abelian groups.
