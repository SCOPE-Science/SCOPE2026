# Maximal Engel index and modular coordinate strata in strictly upper-triangular Lie algebras

## Finding

Let \(q=p^e\) be a prime power and \(n\geq3\). In the Lie algebra \(\mathfrak n_n(\mathbb F_q)\) of strictly upper-triangular \(n\times n\) matrices, write \(T_X=\operatorname{ad}_X\), where \(T_X(Y)=[X,Y]\). Set \(N=\binom n2\), \(a_i=X_{i,i+1}\) for \(1\leq i\leq n-1\), and
\[
S_p(n)=\{i:1\leq i\leq n-1,\;\tbinom{n-2}{i-1}\not\equiv0\pmod p\},\qquad K_p(n)=|S_p(n)|.
\]
If the base-\(p\) expansion of \(n-2\) has digits \(d_0,d_1,\dots\), Lucas's congruence gives \(K_p(n)=\prod_j(d_j+1)\). Every \(T_X\) has nilpotency index at most \(n-1\), and it attains this index **if and only if** either all \(a_i\) are nonzero, or precisely one \(a_i\) is zero and its index belongs to \(S_p(n)\). In the maximal case there is exactly one Jordan block of length \(n-1\).

The exact number of maximal-index elements is
\[
q^{\binom n2-n+1}\Big((q-1)^{n-1}+K_p(n)(q-1)^{n-2}\Big).
\]
Its complement, viewed as a reduced affine algebraic set over \(\mathbb F_q\), is the union of the coordinate hyperplanes \(\{a_i=0\}\) for \(i\notin S_p(n)\) and the coordinate codimension-two flats \(\{a_i=a_j=0\}\) for distinct \(i,j\in S_p(n)\). These are exactly its irreducible components (with all higher-superdiagonal coordinates free). Thus the nonmaximal-index locus has precisely \(n-1-K_p(n)\) hypersurface components and \(\binom{K_p(n)}2\) codimension-two components. Its codimension is two precisely when \(n-1=c p^t\) for integers \(t\geq0\) and \(1\leq c<p\); otherwise it is one.

## Assumptions and scope

All fields are finite of characteristic \(p\); no restriction on the extension degree \(e\). The nilpotency index of an endomorphism is the least positive exponent killing it. The matrix units are \(E_{ij}\). The algebraic locus is the set of matrices over an algebraic closure satisfying the displayed coordinate equations, while the counting statement concerns its \(\mathbb F_q\)-points. The title's word *Engel* refers to the nilpotency index of each adjoint map, not the coadjoint index of a Lie algebra. No classification of all lower Jordan blocks is claimed.

## Proof

Let \(\mathfrak n^{(r)}\) denote the space of matrices supported on superdiagonals at distance at least \(r\), so \(\mathfrak n^{(1)}=\mathfrak n_n\) and \(\mathfrak n^{(n)}=0\). Multiplication gives \([\mathfrak n^{(r)},\mathfrak n^{(s)}]\subseteq\mathfrak n^{(r+s)}\). Hence \(T_X^{n-1}=0\) for every \(X\).

Left and right multiplication by \(X\) commute as operators on matrices. The binomial identity for their difference therefore gives, for every integer \(k\geq0\),
\[
T_X^k(Y)=\sum_{h=0}^k(-1)^h\binom{k}{h} X^{k-h}Y X^h.
\]
Set \(k=n-2\). By the superdiagonal filtration, \(T_X^k\) kills all \(E_{ij}\) with \(j-i\geq2\); on the simple-root matrix unit \(E_{i,i+1}\), its result lies in the single coordinate \(\mathbb F_q E_{1n}\). A nonzero term \(X^{k-h}E_{i,i+1}X^h\) contributing to this coordinate has a path from row \(1\) to \(i\) of length \(k-h\), and a path from \(i+1\) to column \(n\) of length \(h\). Since the distances total \(n-2=k\), both paths must use only the consecutive first-superdiagonal entries. This forces \(k-h=i-1\), \(h=n-i-1\), and yields the exact identity
\[
T_X^{n-2}(E_{i,i+1})=(-1)^{n-i-1}\binom{n-2}{i-1}\left(\prod_{\substack{1\leq j\leq n-1\\j\neq i}}a_j\right)E_{1n}.
\]
The equality of the two binomial indices uses their symmetry. This argument holds unchanged in every characteristic, including two. Since the image of \(T_X^{n-2}\) is a subspace of \(\mathbb F_q E_{1n}\), its rank is either zero or one. Nonzero rank means at least one displayed scalar is nonzero, precisely when all \(a_j\ne0\), or exactly one vanishes at an eligible position \(i\in S_p(n)\). Moreover, for \(n\geq3\), the endpoint binomial coefficients are one, so \(S_p(n)\) is nonempty. Whenever the top power has rank one, its rank equals the number of Jordan blocks of size \(n-1\), proving uniqueness of that block.

Exactly \(n-1\) scalar first-superdiagonal coordinates affect the criterion; the remaining \(N-(n-1)\) coordinates are free. All-nonzero assignments contribute \((q-1)^{n-1}\), and exactly-one-zero eligible assignments contribute \(K_p(n)(q-1)^{n-2}\). Multiplying by the number \(q^{N-n+1}\) of free choices proves the count. Lucas's theorem says \(\binom{k}{j}\not\equiv0\pmod p\) exactly when every base-\(p\) digit of \(j\) is at most the corresponding digit of \(k\). Applied to \(k=n-2\) it gives \(K_p(n)=\prod_j(d_j+1)\).

For the geometric statement, failure of the above criterion means either some ineligible coordinate \(a_t\), with \(t\notin S_p(n)\), is zero, or at least two eligible coordinates vanish. This is exactly the displayed union of coordinate subspaces. Every such coordinate subspace is irreducible, and none of the listed components contains another, so the list is irredundant. The complement has codimension two if and only if **every** index is eligible, namely all coefficients \(\binom{n-2}{j}\) are nonzero modulo \(p\). By Lucas's theorem, this holds precisely when the base-\(p\) digits of \(n-2\), except perhaps its highest digit, are all \(p-1\). Equivalently \(n-1=c p^t\) with \(1\leq c<p\); the case \(n-1=1\) is excluded by \(n\geq3\). Otherwise the ineligible-coordinate hypersurfaces give codimension one.

## Verification

The accompanying self-contained C++ program `verify.cpp` constructs each strictly upper-triangular matrix, applies iterated matrix commutators to every first-superdiagonal matrix unit, and compares **every** terminal coefficient to the formula above. It exhaustively checks all matrices for the ten cases: \((q,n)=(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(4,3),(4,4),(5,4)\). The characteristic-two degree-two extension uses \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\). Compile using `g++ -O3 -std=c++17 verify.cpp -o verify` and run `./verify`; every test reports zero classification and coefficient mismatches and ends with `VERIFY_OK`.

In particular, the exhaustive observed counts for \((q,n)=(2,5),(3,5),(2,6)\) are respectively \(320\), \(23328\), and \(3072\). These tests are independent finite corroborations, not a substitute for the general proof.

## Relationship to prior work

Classical Engel theory explains nilpotence of adjoint maps, but not the finite-field distribution of the **largest possible nilpotency index of an individual inner derivation**. Righi and Yu's 2009 work on ad-nilpotent ideals of Borel subalgebras studies a *coadjoint index of quotients*, not the present elementwise maximal-adjoint-index locus. Yip's 2012/2013 work gives Jordan-form counts for \(X\) acting on its **natural** \(n\)-dimensional module, whereas the present theorem concerns the Jordan form of \(\operatorname{ad}_X\) on the much larger Lie algebra \(\mathfrak n_n\). These invariants are not equivalent: over \(\mathbb F_2\), for \(n=4\), \(X=E_{23}+E_{34}\) and \(Y=E_{13}+E_{34}\) both have natural Jordan partition \((3,1)\), but \(\operatorname{ad}_X\) has nilpotency index three while \(\operatorname{ad}_Y\) has index at most two. The finite-field count and modular component stratification are not implied by those natural-Jordan or coadjoint-index statements.

## Limitations

This establishes the maximal-index locus, its geometry, its cardinality, and top-block multiplicity; it does not determine all Jordan partitions or the distributions of smaller indices. Existing specialized literature on modular adjoint Jordan types could conceivably imply the formula without using the same terminology. No independent mathematical validation or priority certification is claimed.

## References

1. C. Righi and R. W. T. Yu, *On the index of the quotient of a Borel subalgebra by an ad-nilpotent ideal*, arXiv:0908.4201v1 (public 28 August 2009), subsequently Journal of Lie Theory 20 (2010), 49–63. https://arxiv.org/abs/0908.4201
2. M. Yip, *q-Rook placements and Jordan forms of upper-triangular nilpotent matrices*, Discrete Mathematics & Theoretical Computer Science, FPSAC 2013 proceedings, DOI:10.46298/dmtcs.2362 (public-date record: 31 December 2012). https://dmtcs.episciences.org/en/articles/2362
3. É. Lucas, *Théorie des fonctions numériques simplement périodiques*, American Journal of Mathematics 1 (1878), 184–240; classical binomial-coefficient congruence used here.
