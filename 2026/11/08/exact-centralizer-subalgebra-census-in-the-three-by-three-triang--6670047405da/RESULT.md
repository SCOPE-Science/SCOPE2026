# Exact centralizer-subalgebra census in the three-by-three triangular matrix algebra

## Finding
For every finite field \(k=\mathbb F_q\), \(q\ge2\), write \(T=T_3(k)\) for the six-dimensional associative algebra of upper-triangular \(3\times3\) matrices and \(C(X)=\{Y\in T:XY=YX\}\). Count *distinct embedded subalgebras* \(C(X)\), rather than matrices \(X\), abstract isomorphism classes, or conjugacy orbits. Then
\[
 |\{C(X):X\in T\}|=\begin{cases}31,&q=2,\\q^3+6q^2+3q+1,&q>2.\end{cases}
\]
More precisely, if \(c_r(q)\) denotes the number of distinct centralizers of codimension \(r\) in \(T\), then
\[
 c_0(q)=c_1(q)=1,\qquad c_2(q)=3q^2+2q,\qquad
 c_3(q)=3q^2+q-1+q^3\mathbf1_{q>2},
\]
and all other \(c_r(q)\) vanish.

## Assumptions and scope
The field can have any prime-power cardinality, including characteristic two. The word *centralizer* always refers to the complete \(k\)-subalgebra inside \(T\). Two centralizers count once if they are literally the same subset of \(T\), regardless of whether their defining matrices are different. The upper-triangular group acts on these subalgebras by conjugation. We use its unitriangular subgroup \(U\), of order \(q^3\).

## Proof
Write
\[
 X=\begin{pmatrix}a&u&v\\0&b&w\\0&0&c\end{pmatrix},\qquad
 Y=\begin{pmatrix}\alpha&s&t\\0&\beta&r\\0&0&\gamma\end{pmatrix}.
\]
The equation \(XY=YX\) consists exactly of
\[
 (a-b)s+u(\beta-\alpha)=0,\quad
 (b-c)r+w(\gamma-\beta)=0,\quad
 (a-c)t+ur-ws+v(\gamma-\alpha)=0.\tag{1}
\]
This gives a direct test for equality and codimension of every centralizer.

**Three pairwise distinct diagonal entries.** When \(a,b,c\) are distinct, an upper unitriangular conjugation removes all upper off-diagonal entries, and \(C(X)\) becomes a conjugate of the diagonal algebra \(D\). Its stabilizer inside \(U\) is trivial: an upper unitriangular matrix normalizing all diagonal matrices must be the identity. Hence this family consists of \(q^3\) distinct centralizers of dimension three, if \(q\ge3\); it is empty if \(q=2\).

**Exactly two equal diagonal entries.** There are three equality patterns, indexed by the pair \(ij\in\{12,13,23\}\) carrying the repeated eigenvalue. By eliminating cross-eigenspace entries through upper unitriangular conjugation, each \(X\) becomes either a diagonal matrix \(D_{ij}\) (the *split* case) or \(D_{ij}+\lambda E_{ij}\) (the *nonsplit* case), for some \(\lambda\ne0\). In the pair \(13\) the cross-eigenspace elimination changes the effective \(E_{13}\) coefficient; its vanishing or nonvanishing remains the only distinction. Substituting these normal forms into (1) shows that the centralizer is independent of the two numerical eigenvalues and, in the nonsplit case, independent of the nonzero \(\lambda\). For each of the six types, its stabilizer under \(U\) is the one-parameter subgroup \(\{I+tE_{ij}:t\in k\}\), of order \(q\). Thus each type contributes precisely \(q^2\) distinct centralizers. Each split type has dimension four and surjective diagonal projection; each nonsplit type has dimension three and diagonal projection \(\{\operatorname{diag}(\alpha,\beta,\gamma):\alpha_i=\alpha_j\}\). The three nonsplit types are distinct by their different projection hyperplanes; the split types are distinct by the unique radical line of their centralizer (its image modulo the square of the radical distinguishes pairs \(12\) and \(23\), and pair \(13\) lies in the radical square). Consequently this stratum yields \(3q^2\) distinct centralizers in each of codimensions two and three.

**All three diagonal entries equal.** Subtract a scalar matrix and write \(N=uE_{12}+wE_{23}+vE_{13}\). Equation (1) now gives the following disjoint list. If \(u=w=v=0\), the centralizer is all of \(T\), one case of codimension zero. If \(u=w=0\), \(v\ne0\), the centralizer is \(C(E_{13})\), one of codimension one. If \(u\ne0,w=0\), its centralizer has dimension four and depends on exactly the ratio \(v/u\), giving \(q\) cases. Symmetrically \(u=0,w\ne0\) gives another \(q\) dimension-four cases, determined by \(v/w\). Finally \(u,w\ne0\) forces all three diagonal entries of every commuting matrix to coincide; its remaining off-diagonal equation is \(ur=ws\), depending on the nonzero ratio \(u/w\), giving \(q-1\) dimension-three cases. These contribute respectively \(1,1,2q,q-1\), a total of \(3q+1\) embedded centralizers.

**No inter-stratum collisions.** The diagonal projection of the full centralizer distinguishes the remaining potential coincidences. The three-distinct centralizers have codimension three and full diagonal projection; the nonsplit two-eigenvalue centralizers have codimension three and a two-dimensional diagonal projection; the regular nilpotent centralizers have codimension three and scalar diagonal projection. Split two-eigenvalue centralizers have codimension two and full diagonal projection; the one-sided nilpotent centralizers have codimension two and a two-dimensional diagonal projection. The dimension-five and dimension-six centralizers are unique. Thus no types from different strata coincide. Summing \(q^3\mathbf1_{q>2}+6q^2+3q+1\) proves the total and the asserted codimension refinement. The proof applies in every characteristic.

## Verification
The accompanying pure-Python file `verify.py` implements the independent equation (1), computes canonical reduced row spaces of the commutator map, and enumerates every element of \(T_3(k)\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\). It checks both the total and each commutator-rank stratum, with totals \(31,91,173,291,659\) respectively, and prints `VERIFY_OK`. The implementation of \(\mathbb F_4\) uses the polynomial relation \(t^2+t+1=0\). Finite enumeration is a check, not a proof for all fields; the preceding classification proves the universal statement.

## Relationship to prior work
Cheraghpour–Ghosseiri–Jafari–Seyfpour (first public February 20, 2024) enumerate commuting-graph parameters for **two-by-two** triangular matrix rings, not this exact three-by-three embedded-centralizer invariant. Słowik (2018) studies **maximal and minimal** triangular centralizers for arbitrary matrix sizes; her theorem statements and relevant proof material do not give the total number of distinct centralizers in \(T_3(\mathbb F_q)\). Bhunia (2019) counts or classifies centralizers **up to conjugacy** in the **invertible triangular group** over an infinite field of characteristic different from two, not literal equality of centralizer subalgebras in this finite ring. A related published enumeration of centralizers for a radical-square-zero Kronecker algebra concerns a different algebra with different multiplication relations. The current calculation is neither the full-matrix-algebra centralizer problem nor a group-centralizer conjugacy census.

## Limitations
This is a fixed-size complete classification for dimension-six triangular algebras and does not extend to larger triangular matrix sizes without further work. The count is of embedded centralizer subalgebras, not their conjugacy classes. No claim is made about full publication priority beyond inspected sources; a broader unlocated classification might imply the number. Independent validation has not been carried out.

## References
1. H. Cheraghpour, N. M. Ghosseiri, M. Jafari, F. Seyfpour, *On Commuting Graphs of Triangular Rings* (first public 2024-02-20), arXiv:2402.12619v1, https://arxiv.org/abs/2402.12619.
2. R. Słowik, *Maximal and Minimal Triangular Matrices*, Results in Mathematics 73 (2018), article 58, DOI:10.1007/s00025-018-0819-4, https://doi.org/10.1007/s00025-018-0819-4.
3. S. Bhunia, *Conjugacy Classes of Centralizers in the Group of Upper Triangular Matrices* (first public 2019-01-23), arXiv:1901.07869, https://arxiv.org/abs/1901.07869.
