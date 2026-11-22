# A doubled middle Lefschetz quintic in a Penrose forty-point Artinian section

## Finding
Let \(I\) be the homogeneous Penrose forty-point ideal in \(S=\mathbb Q[x,y,z,w]\):
\[
I=(xyzw,\,w(x^3-y^3+z^3),\,z(x^3+y^3+w^3),\,y(-x^3+z^3+w^3),\,x(y^3+z^3-w^3)).
\]
Put \(h=x+2y+3z+w\), \(A=S/(I,h)\), and \(\ell=Ux+Vy+Wz\). The finite-dimensional Gorenstein algebra \(A\) has Hilbert function \((1,3,6,10,10,6,3,1)\). Its middle multiplication determinant is
\[
\det(\ell:A_3\longrightarrow A_4)=Q(U,V,W)^2/27,
\]
in the bases below, where
\[
Q(U,V,W)=15U^{4}V-47U^{4}W+36U^{3}V^{2}-34U^{3}VW+54U^{3}W^{2}-18U^{2}V^{3}-18U^{2}W^{3}+45UV^{4}-54UV^{3}W+30UVW^{3}-7UW^{4}-27V^{4}W+54V^{3}W^{2}-36V^{2}W^{3}+7VW^{4}.
\]
The quintic \(Q\) is squarefree and irreducible over \(\mathbb Q\). Therefore the middle non-Lefschetz determinantal divisor is **twice a reduced quintic**, not a reduced decic. The rank is \(8\) at \([U:V:W]=[1:0:0],[0:1:0],[0:0:1],[1:2:3]\) and \(10\) for general linear forms.

## Assumptions and scope
Work over \(\mathbb Q\) (or extend scalars to \(\mathbb C\)); the assertion is for the **one specified** regular hyperplane section, not every or a generic section. The determinantal scheme is the closed subscheme of \(\mathbb P^2\) cut out by the sole determinant of the square middle multiplication map. The scalar \(1/27\) depends on basis; the divisor does not.

## Proof
Eliminate \(w=-x-2y-3z\) and let \(J\subset\mathbb Q[x,y,z]\) be the resulting five-generated quartic ideal. An exact homogeneous Gröbner basis over \(\mathbb Q\) has zero-dimensional quotient; quotient ranks in degrees \(0\) through \(8\) are respectively \(1,3,6,10,10,6,3,1,0\). The original ideal is a height-three Pfaffian Gorenstein ideal by Chiantini et al., Proposition 5.17. Hence its regular linear section \(A\) is Gorenstein.

For \(A_3\) use the ten monomials \(x^iy^jz^{3-i-j}\), ordered by \(0\le i\le3\), then \(0\le j\le3-i\). For \(A_4\) use the ordered basis
\[
(z^4,yz^3,y^2z^2,y^3z,y^4,xz^3,xyz^2,xy^2z,xy^3,x^2y^2).
\]
Reduce \(x m\), \(y m\), \(z m\) for each cubic basis monomial \(m\) by the exact Gröbner basis; form the \(10\times10\) matrix whose columns are the reduced coefficients of \(Uxm+Vym+Wzm\). Its determinant is an explicit polynomial in three independent indeterminates. Exact polynomial expansion and cancellation gives \(27\det M-Q^2=0\) identically. The embedded executable checker reconstructs both the Gröbner basis and this entire symbolic matrix and proves the identity by exact rational arithmetic: no finite sampling of \(\ell\) substitutes for the polynomial proof. Exact factorization of \(Q\) over \(\mathbb Q\) proves its irreducibility; the nonzero gcd test with its first derivative proves squarefreeness. Finally, exact matrix ranks for the stated five test directions give four ranks of \(8\) and the full-rank witness \((U,V,W)=(2,3,5)\).

## Verification
Run `python3 checker.py` with SymPy installed. It checks zero dimensionality, all nine graded quotient dimensions, the symbolic determinant identity, factorization, squarefreeness, four corank-two cases and a full-rank witness. All calculations use exact \(\mathbb Q\) arithmetic and the named generators.

## Relationship to prior work
Hanumanthu, Huizenga, Kettinger, Merta, Szemberg and Szpond (2026, arXiv:2611.13108v1) give this Penrose ideal and the Hilbert vector while studying Waldschmidt constants. Chiantini and collaborators (2022, arXiv:2209.04820v1, Proposition 5.17) already establish the general Pfaffian/Gorenstein family, and their Chapter 2.5 discusses Lefschetz loci for **different quotients by powers of linear forms**. Almeida et al. (2026) provide general Lefschetz criteria, but do not state this explicit Penrose-section determinant. None of those antecedents is claimed as new.

## Limitations
Only this specified rational Artinian section is calculated. Irreducibility is over \(\mathbb Q\), not independently over the algebraic closure. The new factorization is an exact finite algebraic identity, not a statement about all Penrose sections. Priority against unindexed equivalent calculations and independent mathematical audit remain open.

## References
- K. Hanumanthu et al., *Waldschmidt constants and invariant geometry for exceptional rank-four complex reflection groups*, arXiv:2611.13108v1, first posted November 9, 2026. https://arxiv.org/abs/2611.13108
- L. Chiantini et al., *Configurations of points in projective space and their projections*, arXiv:2209.04820v1, Proposition 5.17 and Chapter 2.5. https://arxiv.org/abs/2209.04820
- C. Almeida et al., *On higher Jacobians, Laplace equations, and Lefschetz properties*, Bulletin of the London Mathematical Society 58 (2026). https://doi.org/10.1112/blms.70208
