# Automorphism groups of three-step star Lie algebras and a characteristic-two symmetry jump

## Finding

Let \(k=\mathbb F_q\), \(m\ge3\), and \(w=\binom m2\). The full group of \(k\)-linear automorphisms of the star Lie algebra \(L_m(k)\) has order
\[
|\operatorname{Aut}_k(L_m(k))|=q^{(m+1)(w+1)}(q-1)
\begin{cases}
m!(q-1)^m,&\operatorname{char}k\ne2,\\
\prod_{i=0}^{m-1}(q^m-q^i),&\operatorname{char}k=2.
\end{cases}
\]
Its image on the abelianization is the block-diagonal group \(k^\times\times H_m(k)\), where \(H_m(k)\) is the monomial subgroup in odd characteristic and \(\operatorname{GL}_m(k)\) in characteristic two. The kernel has order \(q^{(m+1)(w+1)}\) in both characteristics.

## Algebra and scope

The star algebra has basis \(h,u_1,\ldots,u_m,a_1,\ldots,a_m,w_{ij}\ (1\le i<j\le m)\). The nonzero brackets, up to antisymmetry, are
\[
[h,u_i]=a_i,\qquad [u_i,a_j]=w_{ij}\quad(i\ne j),\qquad w_{ji}=w_{ij}.
\]
The bracket is alternating, also in characteristic two. The only Jacobi identity on distinct basis entries with possibly nonzero terms is for \(h,u_i,u_j\); the terms cancel because \(w_{ij}=w_{ji}\). Write \(U=\langle u_i\rangle\), \(A=\langle a_i\rangle\), \(W=\langle w_{ij}\rangle\). Then \(L_m'=A\oplus W\) and \([L_m,L_m']=W\). The center is exactly \(W\): bracketing with \(h\) detects the \(U\)-component, while bracketing with the leaves detects the \(h\)-component in \(A\) and the \(A\)-component in \(W\). This is the star specialization of Gallo and Videla [1]. The statement concerns \(k\)-linear Lie automorphisms for \(m\ge3\); it is not a statement about other graphs or abstract group automorphisms.

## Proof

On \(V=L_m/L_m'\), the bracket with values in \(L_m'/W\simeq U\) is
\[
[\alpha h+u,\beta h+v]\pmod W=\alpha v-\beta u.
\]
An isotropic subspace containing a vector with nonzero \(h\)-coefficient has dimension at most one: the bracket with that vector vanishes only on its own line. Thus the image of \(U\) is the unique maximal isotropic subspace of dimension at least two and is characteristic. A candidate automorphism on \(V\) has \(h\mapsto\lambda h+t\), \(u\mapsto Mu\), with \(\lambda\ne0\), \(t\in U\) and \(M\in\operatorname{GL}_m(k)\). With arbitrary lifts \(h',u_i'\) of these vectors, \([h',[h',u_i']]=\lambda[t,Ma_i]\), where the matrix on \(A\) is written using the identification \(u_i\leftrightarrow a_i\). The left radical of \(U\times A\to W\) is zero: if the coefficient of \(u_i\) is nonzero, pair with \(a_j\) with \(j\ne i\) and read the \(w_{ij}\)-coefficient. The defining relation \([h,[h,u_i]]=0\) and invertibility of \(M\) now force \(t=0\).

For \(u=\sum_i x_i u_i\),
\[
[u,[h,u]]=2\sum_{i<j}x_ix_jw_{ij}.
\]
Terms from changing lifts in \(L_m'\) do not affect this triple bracket. Thus each column of \(M\) must belong, in odd characteristic, to one of the coordinate axes. Invertibility makes \(M\) monomial. In characteristic two the triple bracket is identically zero on \(U\).

For sufficiency, set \(h'=\lambda h\), \(u_i'=Mu_i\), \(a_i'=[h',u_i']\) and \(w_{ij}'=[u_i',a_j']\) for \(i<j\). The images of the leaves commute; \([h',a_i']=0\), and \([u_i',a_i']=0\) holds by the column condition in odd characteristic and by the factor of \(2\) in characteristic two. The mixed bracket is symmetric in the two leaf indices, and the \(a_i'\) commute and the \(w_{ij}'\) are central. This checks all brackets. On \(W\) the map has the following two descriptions:

- In odd characteristic, if \(Mu_i=d_i u_{\sigma(i)}\), then \(w_{ij}'=\lambda d_i d_j w_{\sigma(i)\sigma(j)}\), with **unordered** index pairs. It permutes the pair basis up to nonzero scalars; no permutation sign occurs.
- In characteristic two the \(w_{ab}\)-coefficient of \(w_{ij}'\) is \(\lambda(M_{ai}M_{bj}+M_{bi}M_{aj})\) for \(a<b\). This is \(\lambda\bigwedge^2 M\) under \(w_{ij}\leftrightarrow u_i\wedge u_j\), because minus and plus agree.

Both actions on \(W\) are invertible. The actions on \(L_m'/W\) and \(V\) are also invertible (respectively \(\lambda M\) and \(\operatorname{diag}(\lambda,M)\)). The lifts give automorphisms, proving the stated quotient image.

For the kernel, the possible generator lifts are
\[
h'=h+b+z,\qquad u_i'=u_i+\sum_j c_{ji}a_j+z_i,
\qquad b\in A,\quad z,z_i\in W.
\]
For distinct \(i,j,k\) the coefficient of \(w_{ik}\) in \([u_i',u_j']\) is \(c_{kj}\); hence all off-diagonal entries vanish, using \(m\ge3\). The \(w_{ij}\)-coefficient is \(c_{jj}-c_{ii}\), so the matrix is \(cI\) in either characteristic. Conversely those choices give commuting leaves, \(a_i'=[h',u_i']=a_i-[u_i,b]\), and \([u_i',a_j']=[u_i,a_j]\). The images satisfy all other defining zero brackets since \(A\) is abelian, \([h,A]=0\) and \(W\) is central. They induce the identity on all three lower-central quotients, so each choice gives an automorphism. Since the generators determine the map, the \(m\) coordinates of \(b\), the \((m+1)w\) central coordinates and the one scalar \(c\) give exactly \(q^{(m+1)(w+1)}\) choices. Multiplication by the quotient order gives the formula. The proof applies to nonprime as well as prime fields of the stated characteristics.

## Verification

The accompanying standard-library script `verify_star_aut.py` tests bracket preservation for seeded lifts at \((q,m)=(2,3),(2,4),(3,3),(3,4),(5,3)\) and computes the linear kernel constraint rank for the leaf corrections. Enumerating the three-by-three matrices over \(\mathbb F_2\) and \(\mathbb F_3\) gives respectively 168 and 48 admissible invertible leaf actions. Run `python3 verify_star_aut.py`; the expected marker is `STAR_AUTOMORPHISM_GROUP_OK`. These are finite consistency checks; the proof gives the all-field statement.

## Prior work and limitations

Gallo and Videla [1, §§2–3] give the graph construction, including the star brackets in characteristic two. Their Theorem 4.5 establishes graph-isomorphism rigidity in characteristic different from two; it does not describe automorphisms of a single fixed algebra. The automorphism results of Chakrabarti, Mainkar and Swiatlowski [2] concern a different, class-two graph construction. The exact quotient image and kernel order above are distinct from those results; historical priority relative to unindexed classifications remains provisional. The kernel calculation uses three distinct indices and is not asserted for \(m=2\).

## References

1. A. L. Gallo and D. E. Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, [arXiv:2610.33963v1](https://arxiv.org/abs/2610.33963).
2. D. Chakrabarti, M. Mainkar and S. Swiatlowski, *Automorphism Groups of nilpotent Lie algebras associated to certain graphs*, [arXiv:1812.09439](https://arxiv.org/abs/1812.09439), *Communications in Algebra* 48 (2020), 263–273, [doi:10.1080/00927872.2019.1640239](https://doi.org/10.1080/00927872.2019.1640239).
