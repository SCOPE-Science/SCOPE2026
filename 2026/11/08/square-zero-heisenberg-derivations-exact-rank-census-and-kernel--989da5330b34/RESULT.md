# Square-zero Heisenberg derivations: exact rank census and kernel symplectic conservation

## Finding

Let \(k\) be any field and \(n\geq1\). On the Heisenberg Lie algebra \(H_n=V\oplus kz\), with \(\dim_kV=2n\) and a nondegenerate alternating bilinear form \(\omega\), put \([u,v]=\omega(u,v)z\). Every ordinary derivation \(D\) with \(D^2=0\) is uniquely determined by an isotropic subspace \(W\subseteq V\) of dimension \(r\leq n\), a nondegenerate symmetric bilinear form on \(W^*\) (equivalently, a symmetric isomorphism \(W^*\to W\)), and a covector \(f\in V^*\) annihilating \(W\). The zero-\(W\) case includes all central derivations.

The ranks of such derivations are exactly \(0,1,\ldots,n\). Write \(K_D=\ker(D)/kz\), with its alternating bracket form \(\omega_D\). Then every square-zero derivation obeys the conservation identity
\[
\operatorname{rank}\omega_D+2\operatorname{rank}D=2n.
\]

For every prime power \(q\), define \(I_{n,r}(q)\) to be the number of totally isotropic \(r\)-subspaces of a \(2n\)-dimensional symplectic space and \(S_r(q)\) the number of nonsingular symmetric \(r\)-by-\(r\) matrices, with \(I_{n,0}=S_0=1\). Explicitly,
\[
I_{n,r}(q)=\frac{\prod_{i=0}^{r-1}(q^{2n-i}-q^i)}{\prod_{i=0}^{r-1}(q^r-q^i)},\qquad
S_r(q)=q^{r(r+1)/2}\prod_{\substack{1\le j\le r\\j\text{ odd}}}(1-q^{-j}).
\]
The complete labeled rank polynomial is
\[
\boxed{\mathcal P_{n,q}(t)=1+\sum_{d=1}^{n}\left[I_{n,d}(q)S_d(q)q^d+I_{n,d-1}(q)S_{d-1}(q)(q^{2n-d+1}-q^{d-1})\right]t^d.}
\]
Each rank-\(d\) locus, for \(1\le d\le n\), has an explicit disjoint decomposition into **two nonempty smooth geometrically irreducible locally closed strata**. Their dimensions are \(d(2n-d+2)\) and \(d(2n-d+2)-1\), respectively. No assertion is made that these are irreducible components of the entire rank locus.

## Assumptions and scope

All fields and all \(n\ge1\) are allowed in the structural theorem, including characteristic two. The finite-field formula counts distinct labeled ordinary derivations, not orbits, and no restricted-Lie-derivation condition is imposed. A symplectic form is alternating also in characteristic two. All rank notions are ordinary vector-space ranks. The bracket form on \(K_D\) is well-defined because \(z\) is central and belongs to \(\ker D\).

## Proof

**Step 1: Derivation equations.** Since \(z\) spans the derived algebra, any derivation has unique blocks
\[
D(z)=az,\qquad D(v)=Tv+f(v)z
\]
with \(T\in\operatorname{End}(V)\), \(f\in V^*\), and
\[
\omega(Tu,v)+\omega(u,Tv)=a\omega(u,v)\quad\text{for all }u,v\in V.
\]
The square-zero condition on \(z\) gives \(a^2=0\), hence \(a=0\) over a field. Squaring on \(V\) then gives precisely \(T^2=0\) and \(f\circ T=0\). Thus \(T\) belongs to the symplectic Lie algebra, in the infinitesimal sense, and is square-zero.

**Step 2: Isotropic-image parametrization.** Put \(W=\operatorname{im}T\) and \(r=\dim W\). For all \(u,v\),
\[
\omega(Tu,Tv)=-\omega(u,T^2v)=0,
\]
so \(W\) is isotropic and \(r\le n\). The infinitesimal symplectic identity also gives \(\ker T=W^\perp\). The pairing identifies \(V/W^\perp\) with \(W^*\), via \(p(v)(w)=\omega(v,w)\). Accordingly, \(T=B\circ p\), where \(B:W^*\to W\) is invertible. The infinitesimal symplectic identity is equivalent to symmetry of the bilinear form \((\alpha,\beta)\mapsto\alpha(B\beta)\). Conversely, every isotropic \(W\) and every such symmetric isomorphism \(B\) yields a square-zero symplectic \(T\). Finally, \(fT=0\) is equivalent to \(f\in\operatorname{Ann}(W)\), a vector space of dimension \(2n-r\). These conditions are necessary and sufficient, and the representation is unique.

**Step 3: Ranks and kernel bracket.** Set \(U=W^\perp=\ker T\). The row space \(\operatorname{Ann}(U)\) has dimension \(r\) and lies in \(\operatorname{Ann}(W)\). If \(f\in\operatorname{Ann}(U)\), the central part is determined by the image under \(T\), so \(\operatorname{rank}D=r\) and \(K_D=U\). Because the radical of \(\omega|_U\) is \(W\), its rank is \(2(n-r)\).

If \(f\notin\operatorname{Ann}(U)\), then \(\operatorname{rank}D=r+1\) and \(K_D=U\cap\ker f\). Since \(f(W)=0\), this induces a hyperplane \(K_D/W\) in the symplectic quotient \(U/W\) of dimension \(2(n-r)\). A hyperplane in a nonzero symplectic space has restricted alternating form of rank two less than that of the whole space. Thus \(\operatorname{rank}\omega_D=2(n-r-1)\). The claimed conservation identity follows in both cases. For \(r=n\), the second case is impossible. For \(r=0\), the first case is the zero map and the second consists of the nonzero central derivations. This proves exactly the possible ranks.

**Step 4: Finite-field counting.** Ordered bases \(w_1,\ldots,w_r\) of an isotropic subspace can be selected successively in \(q^{2n-i}-q^i\) ways when \(i\) basis vectors have been chosen. Dividing by \(|\mathrm{GL}_r(q)|\) gives \(I_{n,r}(q)\). The number \(S_r(q)\) of nonsingular symmetric matrices satisfies the independently justified kernel-subspace recurrence
\[
q^{r(r+1)/2}=\sum_{j=0}^r{r\brack j}_q S_{r-j}(q).
\]
Indeed, every symmetric form has a unique radical of dimension \(j\), and descends to a nonsingular symmetric form on the quotient. With \(S_0=1\), this recurrence determines all \(S_r\); the displayed product is its classical solution (equivalently obtained by the finite Gaussian-binomial identity). For each \(W\) and \(B\), exactly \(q^r\) covectors annihilate \(U\), while exactly \(q^{2n-r}-q^r\) annihilate \(W\) but not \(U\). Summing the first contributions at \(r=d\) and the second at \(r=d-1\) yields the coefficient in \(\mathcal P_{n,q}\). There is exactly one rank-zero map.

**Step 5: Geometric strata.** The isotropic Grassmannian of \(r\)-spaces has dimension \(r(2n-r)-r(r-1)/2\), and is smooth and geometrically irreducible. Over it, the invertible symmetric isomorphisms form an open subbundle of a rank-\(r(r+1)/2\) vector bundle. The allowable \(f\)'s form a rank-\((2n-r)\) vector bundle, inside which \(\operatorname{Ann}(U)\) is a rank-\(r\) subbundle. The inside and outside loci are smooth geometrically irreducible, the outside being nonempty exactly for \(r<n\). For rank \(d\), the inside locus has \(r=d\) and dimension \(d(2n-d+2)\); the outside has \(r=d-1\) and dimension one less. The two constructions are disjoint by \(\operatorname{rank}T\).

## Verification

The accompanying standalone `checker.py` directly enumerates all linear blocks \(T\) satisfying the original symplectic derivation identity over \(\mathbb F_2\), \(\mathbb F_3\), and the genuine extension field \(\mathbb F_4\) in dimension three, and over \(\mathbb F_2\) in dimension five. It then tests \(T^2=0\), all permissible \(f\), the original basis Leibniz equations, the square-zero equations, the full map rank, and the induced kernel alternating-form rank. These finite independent checks reproduce all coefficients.

For \(n=1\), the complete rank polynomials at field orders \(2,3,4\) are \(1+9t\), \(1+32t\), and \(1+75t\). For \(n=2\) over \(\mathbb F_2\), it is \(1+45t+330t^2\). The exact direct enumeration output is in `verification_output.txt`; it records the marker `DIRECT_HEISENBERG_SQUARE_ZERO_DERIVATION_AND_KERNEL_FORM_OK`. The arbitrary-field proof is independent of these finite tests.

## Relationship to prior work

Feldvoss, Siciliano and Weigel (first submitted February 13, 2011) prove **existence** of square-zero outer restricted derivations of nilpotent restricted Lie algebras, with an exceptional three-dimensional characteristic-two Heisenberg case. They neither classify ordinary square-zero derivations nor count them by rank. The restricted condition matters and is deliberately not imposed here. Brouwer, Gow and Sheekey (2014) count nilpotent symplectic-Lie-algebra matrices in aggregate and study symmetric nilpotent matrices. Their work supplies the relevant broader nilpotent-matrix setting, but their results inspected here do not state the present two-layer rank census, kernel-form conservation law, or geometric strata for derivations of Heisenberg extensions. Classical fixed-rank nilpotent-matrix and orbit methods (including Lusztig 1976) remain relevant and may simplify some underlying counts; a universal priority claim is not made.

## Limitations

This result concerns ordinary square-zero derivations, not all nilpotent derivations, restricted derivations, conjugacy orbits, or scheme-theoretic nonreduced structures. It concerns only the standard finite-dimensional Heisenberg Lie algebras, not general two-step nilpotent algebras. The smoothness statement concerns the specified locally closed strata, not the global scheme cut out by the original equations. Exact independent literature-priority validation has not been performed.

## References

1. J. Feldvoss, S. Siciliano, and T. Weigel, *Outer restricted derivations of nilpotent restricted Lie algebras*, arXiv:1102.2629v1 (February 13, 2011), later *Proceedings of the American Mathematical Society* **141** (2013), 171–179. https://arxiv.org/abs/1102.2629
2. A. E. Brouwer, R. Gow, and J. Sheekey, *Counting Symmetric Nilpotent Matrices*, *Electronic Journal of Combinatorics* **21** (2014), P2.4. https://doi.org/10.37236/3810
3. G. Lusztig, *A Note on Counting Nilpotent Matrices of Fixed Rank*, *Bulletin of the London Mathematical Society* **8** (1976), 77–80. https://doi.org/10.1112/blms/8.1.77
