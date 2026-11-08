# Dihedral low-degree cohomology of polygonal moment-angle manifolds

## Finding

For every integer \(n\ge 4\), the complex moment-angle manifold \(Z_n=(D^2,S^1)^{C_n}\) associated with the simplicial cycle on \(n\) vertices carries a natural action of the dihedral group \(D_n\) by permutation of its disk-circle coordinates. All statements below use rational coefficients.

Put \(r(i)=i+1\) and \(s_a(i)=a-i\) modulo \(n\). The complete characters in degrees three and four are:

\[
\chi_3(r^a)=\begin{cases}
\frac{n(n-3)}2,&a\equiv0\pmod n,\\
\frac n2,&n\text{ even and }a\equiv n/2\pmod n,\\
0,&\text{otherwise},
\end{cases}
\]

\[
\chi_3(s_a)=\begin{cases}
\frac{n-3}2,&n\text{ odd},\\
\frac n2,&n\text{ even and }a\text{ even},\\
\frac n2-2,&n\text{ even and }a\text{ odd};
\end{cases}
\]

\[
\chi_4(r^a)=\begin{cases}
\frac{n(n-2)(n-4)}3,&a\equiv0\pmod n,\\
-\frac n3,&r^a\text{ has exact order }3,\\
0,&\text{otherwise},
\end{cases}
\qquad
\chi_4(s_a)=\begin{cases}-1,&n\text{ odd},\\0,&n\text{ even}.
\end{cases}
\]

For the **finite coordinate-permutation quotient** \(Y_n=Z_n/D_n\), the degree-three and degree-four rational Betti numbers are

\[
\boxed{b_3(Y_n)=\lfloor n/2\rfloor-1,\qquad
b_4(Y_n)=\frac{(n-2)(n-4)-3\mathbf1_{2\nmid n}-2\mathbf1_{3\mid n}}6.}
\]

In particular, \(b_4(Y_n)=0\) exactly when \(n=4\) or \(5\), while \(b_3(Y_n)>0\) for every \(n\ge4\). Here \(\chi_j\) denotes trace on the **ordinary cohomology** \(H^j\), not an equivariant Borel-cohomology group.

## Assumptions and scope

Label the polygon vertices by the integers modulo \(n\). Its simplicial complex \(C_n\) has exactly its vertices, empty face, and edges \(\{i,i+1\}\). Define \(Z_n\) as the union, over faces \(\sigma\in C_n\), of \(\prod_{i\in\sigma}D^2\times\prod_{i\notin\sigma}S^1\), inside \((D^2)^n\). Rotations and reflections of the polygon permute coordinates and preserve this union. The dihedral group has \(2n\) elements and \(s_a\) is a reflection through two opposite vertices when \(n\) is even and \(a\) even, or through two opposite edges when \(n\) is even and \(a\) odd.

The quotient is a topological orbit space; stabilizers can be nontrivial. For a finite group acting cellularly, barycentric subdivision and transfer over \(\mathbb Q\) give \(H^*(Z_n/D_n;\mathbb Q)\cong H^*(Z_n;\mathbb Q)^{D_n}\). No freeness is asserted. The real moment-angle complex \((D^1,S^0)^{C_n}\) is a different space and is not the object studied here.

## Proof

**Natural cellular model.** Use the standard graded differential algebra for the complex moment-angle construction. It has odd generators \(u_i\) of degree one and even generators \(v_i\) of degree two, differential \(d u_i=v_i\), \(d v_i=0\), and relations \(u_i^2=v_i^2=u_i v_i=0\). A product of two distinct \(v\)'s vanishes unless its two labels form an edge in \(C_n\); all products of three distinct \(v\)'s vanish. The permutation action sends \(u_i\) to \(u_{g(i)}\) and \(v_i\) to \(v_{g(i)}\), so signs from reordering the exterior \(u\)'s are essential. This model computes ordinary rational cohomology naturally under relabeling: it is the product-cellular reduction of the Koszul construction of Buchstaber–Panov. Decomposing by the common index support \(I\) isolates finite-dimensional subcomplexes.

**Two-index support.** For any \(I=\{i,j\}\), the degree-two, degree-three, and degree-four cochains of support \(I\) are respectively \(\langle u_i u_j\rangle\), \(\langle u_i v_j,u_j v_i\rangle\), and \(\langle v_i v_j\rangle\) if \(I\) is an edge (zero otherwise). The first differential has rank one, and the second has rank one exactly for an edge. Therefore degree-three cohomology has one generator for each nonedge, with the two representatives \([u_i v_j]=[u_j v_i]\); a symmetry that interchanges the labels fixes this generator, without a minus sign. Thus \(H^3\) is the permutation module on the unordered nonedges.

A rotation preserves a nonedge pair only if it is the identity or the antipodal half-turn. For odd \(n\), each reflection preserves exactly \((n-3)/2\) nonedge pairs. For even \(n\), vertex-axis reflections preserve \(n/2\) and edge-axis reflections preserve \(n/2-2\). This proves the formulas for \(\chi_3\).

**Three-index support and the sign check.** For \(|I|=3\), the relevant cochains in degrees three, four and five are spanned by \(u_I\), by the three monomials \(u_{I\setminus\{j\}}v_j\), and by \(u_{I\setminus e}v_e\) for induced edges \(e\subseteq I\), respectively. Since a three-vertex induced subgraph of \(C_n\) is a forest, the first differential has rank one and the second is surjective: the latter is a signed incidence matrix with independent rows indexed by its induced edges. Consequently the only cohomology in this support occurs in degree four, and for every symmetry stabilizing the support,

\[
\operatorname{tr}(g\mid H^4_I)=
\operatorname{tr}(g\mid C^4_I)-
\operatorname{tr}(g\mid C^3_I)-
\operatorname{tr}(g\mid C^5_I).
\]

For a symmetry \(g\), the three global cochain traces in this identity are exact counts with signs:

\[
\begin{aligned}
T_3(g)&=\sum_{|I|=3,\ gI=I}\operatorname{sgn}(g\mid I),\\
T_4(g)&=\sum_{j:g(j)=j}\ \sum_{\substack{B\subseteq[n]\setminus\{j\},\ |B|=2,\ gB=B}}
\operatorname{sgn}(g\mid B),\\
T_5(g)&=\sum_{\substack{e\in E(C_n),\ ge=e}}\#\bigl(\operatorname{Fix}(g)\setminus e\bigr).
\end{aligned}
\]

Here \(\operatorname{sgn}(g\mid I)\) is the parity of the permutation induced by \(g\) on the specified finite set. The character is \(\chi_4(g)=T_4(g)-T_3(g)-T_5(g)\).

At the identity the three terms are \(n\binom{n-1}{2}\), \(\binom n3\), and \(n(n-2)\), giving \(\chi_4(1)=n(n-2)(n-4)/3\). A nonidentity rotation fixes no vertex; its only invariant triples occur at exact order three, where the triples consist of the \(n/3\) three-element orbits, each with positive permutation sign. Thus \(\chi_4=-n/3\) for those two rotations and zero for all other nonidentity rotations.

For odd \(n\), every reflection fixes one vertex, swaps \((n-1)/2\) pairs, and fixes one edge opposite its fixed vertex. Its degree-four and degree-three cochain traces agree, while the fixed edge together with the fixed vertex contributes \(T_5=1\). Hence \(\chi_4=-1\). For even \(n\), an edge-axis reflection fixes no vertex and no invariant triple; although it preserves two edges, neither has a fixed external vertex. For a vertex-axis reflection, two vertices are fixed and its invariant triples are one fixed vertex together with a swapped pair. The degree-three and degree-four traces cancel, and no edge is fixed. In either even case \(\chi_4=0\).

**Quotient invariant dimensions.** Averaging each character over the \(2n\) elements of \(D_n\) yields the displayed two formulas. The correction \(-2\mathbf1_{3\mid n}\) comes from the two order-three rotations, while \(-3\mathbf1_{2\nmid n}\) comes from the odd-cycle reflections. The displayed numerator is an integer multiple of six, as the character average also proves. Direct evaluation gives \(b_4=0\) only for \(n=4,5\), and \(b_4>0\) for \(n\ge6\).

## Verification

The independent standalone script `polygon_dihedral_verify.py` enumerates every rotation and reflection for \(4\le n\le18\), constructs the exact signed cellular cochain traces in support size two and three, and checks each against the closed character formulas. It performs 660 individual exact character comparisons and all quotient-character averages. For \(4\le n\le12\) it also checks the critical differential ranks and that consecutive differentials compose to zero, using exact integer entries and prime-field rank as an independent finite check of ranks. These computations verify instances only; the proof above supplies the all-\(n\) argument.

The script uses Python 3 standard library only; execute `python3 polygon_dihedral_verify.py`. Expected output is embedded separately as `polygon_dihedral_verify.out`.

## Relationship to prior work

Buchstaber and Panov (public arXiv version December 24, 1999) give the natural Koszul model and, in their Example 3.11, ordinary Betti numbers for the complex moment-angle manifold of an \(n\)-gon. Neither these ordinary Betti numbers nor the model itself are claimed as new. The present contribution is the full dihedral character in its first two nonzero cohomological degrees and the resulting finite-coordinate-quotient Betti formulas, including distinct reflection-axis and order-three effects.

Kamiyama's 2013 work determines dihedral quotient homology for the **real** moment-angle polygon construction; it does not identify the present complex moment-angle spaces. Lü and Zhang's 2022 paper on (co)homology of certain polygonal moment-angle quotients is the most plausible close comparison. Only its published abstract was accessible; the full text could not be inspected, so any overlap with its specific quotient families remains an explicit priority risk. Yu's general quotient Hochster theorem concerns quotients specified by partitions of vertices, and is not, by itself, this complete dihedral character calculation.

## Limitations

The result is rational, confined to degrees three and four, and does not classify integral homology of the quotient, higher-degree characters, cohomology rings, or equivariant homotopy types. The finite group action is not required to be free. Full comparison against every unindexed treatment of polygonal moment-angle coordinate symmetries has not been established; in particular the Lü–Zhang full text remains uninspected. No independent mathematical audit has been conducted.

## References

1. V. M. Buchstaber and T. E. Panov, *Torus actions, equivariant moment-angle complexes, and coordinate subspace arrangements*, arXiv:math/9912199v1, December 24, 1999, especially Theorem 3.3 and Example 3.11. https://arxiv.org/html/math/9912199v1
2. Y. Kamiyama, *The real moment-angle complex of a polygon and necklace sequences*, Surveys in Mathematics and Mathematical Sciences 3(2) (2013), 77–95. https://www.pphmj.com/abstract/8024.htm
3. Z. Lü and S. Zhang, *On the (co)homology of (quotients of) moment-angle manifolds over polygons*, Acta Mathematica Scientia 42(6) (2022), 2204–2222. https://doi.org/10.1007/s10473-022-0602-1
4. L. Yu, *On Hochster's formula for a class of quotient spaces of moment-angle complexes*, arXiv:1406.7392 (first posted June 28, 2014). https://arxiv.org/abs/1406.7392
