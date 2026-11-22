# The full symmetric-group Hodge character and a K3-type factor of the Grossi–Moretti surface

## Finding

Let \(X=W/K\) be a smooth complex Lagrangian surface in the general family of Grossi–Moretti [1]. The symmetric group \(S_3\) acts by permutation of the three sheets of the underlying Galois closure and commutes with the free translation group \(K\cong(\mathbb Z/3)^2\). Write \(\mathbf1\), \(\varepsilon\), and \(V\) for the trivial, sign, and two-dimensional standard rational representations of \(S_3\). Then its entire equivariant Hodge diamond is given by the following table of complex representation multiplicities:

| Hodge bidegree | \(S_3\)-module |
| --- | --- |
| \((0,0),(2,2)\) | \(\mathbf1\) |
| \((1,0),(0,1),(2,1),(1,2)\) | \(2V\) |
| \((2,0),(0,2)\) | \(4\varepsilon\oplus V\) |
| \((1,1)\) | \(\mathbf1\oplus5\varepsilon\oplus4V\) |

In particular,
\[
H^2(X,\mathbb Q)\simeq\mathbf1\oplus13\varepsilon\oplus6V,
\qquad
\operatorname{tr}((12)|H^2)=-12,
\quad
\operatorname{tr}((123)|H^2)=8.
\]

The rational Hodge structure
\[
M=\operatorname{Hom}_{\mathbb Q[S_3]}(V,H^2(X,\mathbb Q))
\]
is six-dimensional of K3 type, with \(h^{2,0}(M)=h^{0,2}(M)=1\), \(h^{1,1}(M)=4\), and polarization signature \((2,4)\). This asserts a canonical Hodge-theoretic factor, not its realization as the cohomology of a K3 surface.

## Assumptions and scope

Work over \(\mathbb C\). Take the generic smooth Galois-closure construction in [1], resolving the degree-three rational morphism of a \((1,6)\)-polarized abelian surface at its nine basepoints, then dividing by the free diagonal translation group \(K\). All representations are semisimple over \(\mathbb Q\); for a finite quotient the rational cohomology of the quotient is canonically the invariant cohomology of its smooth cover. We do not claim that the quotient itself is smooth.

The input numerical invariants are \(q(X)=4\), \(p_g(X)=6\), \(c_2(X)=12\). The transposition quotient is the blow-up of an abelian surface at one point; the full symmetric quotient is \(\mathbb P^2/K\). The cyclic subgroup \(A_3\) fixes precisely eighteen isolated points on \(X\), all locally of type \(\tfrac13(1,2)\), as established in [2]. These are previously known input facts, not new singularity claims.

## Proof

**1. Total and invariant second cohomology.** The surface Betti number is
\[
b_2(X)=c_2(X)-2+4q(X)=12-2+16=26.
\]
Its full symmetric quotient has the rational cohomology of \(\mathbb P^2\) invariant under \(K\), so \(\dim H^2(X,\mathbb Q)^{S_3}=1\). Its transposition quotient is a one-point blow-up of an abelian surface, hence \(\dim H^2(X,\mathbb Q)^{\langle(12)\rangle}=6+1=7\).

For the cyclic subgroup \(A_3\), the fixed-point count of eighteen gives
\[
\chi_{\mathrm{top}}(X/A_3)=\frac{c_2(X)+2\cdot18}{3}=16.
\]
The known \(S_3\)-character \(H^{1,0}(X)=2V\) [1,2] has no \(A_3\)-fixed vectors, so \(b_1(X/A_3)=0\) and \(\dim H^2(X,\mathbb Q)^{A_3}=16-2=14\).

A rational \(S_3\)-module \(U=a\mathbf1\oplus b\varepsilon\oplus cV\) has invariant dimensions \(a\), \(a+c\), \(a+b\) under the whole group, a transposition, and \(A_3\), respectively. Solving \((a,a+c,a+b)=(1,7,14)\) gives
\[
H^2(X,\mathbb Q)=\mathbf1\oplus13\varepsilon\oplus6V.
\]

**2. Holomorphic two-forms.** The quotient by \(S_3\) is rational, hence \(H^{2,0}(X)^{S_3}=0\). The transposition quotient is birational to an abelian surface, giving a one-dimensional invariant subspace of holomorphic two-forms. Grossi's computation of the minimal model of \(X/A_3\) gives \(p_g=4\) [2], so \(\dim H^{2,0}(X)^{A_3}=4\). Since \(p_g(X)=6\), the same character equations yield
\[
H^{2,0}(X)=4\varepsilon\oplus V.
\]
Complex conjugation supplies \(H^{0,2}\). Subtraction from \(H^2\) yields
\[
H^{1,1}(X)=\mathbf1\oplus5\varepsilon\oplus4V.
\]
The known one-form representation is \(H^{1,0}(X)=2V\). Hodge symmetry and Serre duality supply the four remaining Hodge bidegrees, completing the table.

**3. The polarized K3-type factor.** Because \(V\) is an absolutely irreducible rational \(S_3\)-representation with \(\operatorname{End}_{\mathbb Q[S_3]}(V)=\mathbb Q\), the multiplicity \(M=\operatorname{Hom}_{\mathbb Q[S_3]}(V,H^2(X,\mathbb Q))\) carries a natural rational weight-two Hodge structure. The above representations give its Hodge numbers \((1,4,1)\).

Average an ample class over \(S_3\) to obtain an invariant ample class. The \(V\)-isotypic component of \(H^2\) is orthogonal to it under the cup product, because there are no invariant vectors in \(V\). The Hodge index and Hodge–Riemann relations therefore make the \((1,1)\)-part of \(M\) negative definite while its real \((2,0)+(0,2)\)-plane is positive definite. Factoring the invariant intersection pairing through the standard positive-definite rational \(S_3\)-form induces a polarization of signature \((2,4)\) on \(M\).

## Verification

The standalone `CHECKER.py` uses only exact integer and rational arithmetic. It checks all three subgroup-invariant equations in degrees two and \((2,0)\), the full character values \((26,-12,8)\) for \(H^2\), and the Lefschetz Euler characters \((12,-10,18)\) of the identity, transposition and three-cycle. The latter agree with the known genus-six fixed curve of the transposition and the eighteen isolated cyclic fixed points. The checker confirms numeric consistency; the geometric input and polarization argument are proved above using [1,2].

## Relationship to prior work

Grossi–Moretti [1] establish the smooth Lagrangian family, the translation quotient, its cohomological invariants and \(H^{1,0}(X)=2V\). Grossi [2, Chapter 6] explicitly determines the eighteen \(A_3\)-fixed points and numerical invariants of the minimal model of \(X/A_3\). These quotient numerical invariants are **not claimed here as new**. The resulting *full* \(S_3\)-equivariant Hodge diamond and the naturally polarized six-dimensional standard-multiplicity Hodge factor are the asserted refinement. The earlier Bastianelli–Pirola–Stoppino [3] study a different \((1,2)\)-polarized Galois-closure family and motivate the representation-theoretic approach.

## Limitations

This is a rational Hodge-theoretic and representation-theoretic statement, not an integral lattice classification. It does not assert the existence of an associated K3 surface, Hodge conjecture consequences, or the size of the rational Néron–Severi group. All conclusions use smoothness and the cited quotient inputs; they need not hold for degenerate family members. The earlier sources supply numerical ingredients, so older unpublished equivariant calculations and implicit priority remain possible.

## References

[1] P. Grossi and F. Moretti, *An explicit class of Lagrangian surfaces*, arXiv:2502.13087, initially publicly submitted 2025-02-18, https://arxiv.org/abs/2502.13087 (see Sections 4–8).

[2] P. Grossi, *Galois closure and Lagrangian surfaces*, doctoral thesis, Università di Pavia (2025), Chapter 6, especially Proposition 6.11 and Theorem 6.13, https://iris.unipv.it/retrieve/98dda247-b314-45ad-a25e-2a0835c86d16/GrossiPaoloTesiDottoratoConforme.pdf .

[3] F. Bastianelli, G. P. Pirola and L. Stoppino, *Galois closure and Lagrangian varieties*, arXiv:0912.3377, https://arxiv.org/abs/0912.3377 .
