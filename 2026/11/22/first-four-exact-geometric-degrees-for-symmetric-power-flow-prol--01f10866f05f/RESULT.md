# First four exact geometric degrees for symmetric power-flow prolongations

## Finding

For every integer \(n\ge3\), let \(X_n^{(m)}\subset\mathbb A^{2(m+2)}_{\mathbb C}\) be the order-\(m\) algebraic prolongation of the polynomial differential system
\[
x_1'=x_2^n,\qquad x_2'=x_1^n.
\]
Then **all four first prolongation degrees are determined uniformly in the exponent**:
\[
\boxed{\deg X_n^{(m)}=(m^2+1)n^2-m^2\qquad (0\le m\le3,\ n\ge3).}
\]
Equivalently, for \(m=0,1,2,3\) the degrees are \(n^2,\ 2n^2-1,\ 5n^2-4,\ 10n^2-9\), respectively.

More precisely, whenever \(1\le m\le3\) and \(n>m\), generic projective plane slices of degree \(d=1+(m+1)(n-1)\) have exactly two intersections at infinity, at \([1:0:0]\) and \([0:1:0]\), each of intersection multiplicity
\[
\boxed{m(n-1)(n-m).}
\]
When \(m=0\), or \((n,m)=(3,3)\), there are no intersections at infinity.

## Assumptions and scope

Work over an algebraically closed field \(k\) of characteristic zero, with integer \(n\ge3\) and \(m\in\{0,1,2,3\}\). The degree means the projective degree of the closure in the standard projective compactification of the jet-coordinate affine space (equivalently, the number of intersection points with a generic codimension-two affine linear space). No equality at orders \(m\ge4\) is asserted.

Set \(a=x_1(0)\), \(b=x_2(0)\), and define \(D=b^n\partial_a+a^n\partial_b\). Let \(A_j=D^j(a)\) and \(B_j=D^j(b)\). The jet parametrization \((a,b)\mapsto(a,b,A_1,B_1,\ldots,A_{m+1},B_{m+1})\) is an algebraic isomorphism onto the prolongation variety because the first two coordinates are retained. Each \(A_j,B_j\) is homogeneous of degree \(d_j=1+j(n-1)\).

## Proof

**1. Exact top jets and all potential points at infinity.** Differentiating the first three jets gives
\[
\begin{aligned}
&A_1=b^n,\quad A_2=na^nb^{n-1},\\
&A_3=na^{n-1}b^{n-2}\big((n-1)a^{n+1}+nb^{n+1}\big),\\
&A_4=na^{n-2}b^{n-3}\big((n-1)(n-2)a^{2n+2}
+n(4n-3)a^{n+1}b^{n+1}+n(n-1)b^{2n+2}\big).
\end{aligned}
\]
The \(B_j\) are obtained by exchanging \(a\) and \(b\). In particular,
\[
\gcd(A_1,B_1)=1,\qquad
\gcd(A_2,B_2)\sim(ab)^{n-1},\qquad
\gcd(A_3,B_3)\sim(ab)^{n-2},\qquad
\gcd(A_4,B_4)\sim(ab)^{n-3}.
\]
To verify the last two equalities beyond the visible monomial factor, put \(u=a^{n+1}\), \(v=b^{n+1}\). For \(A_3,B_3\), the nonmonomial factors correspond to the two linear forms \((n-1)u+nv\) and \(nu+(n-1)v\), whose determinant is \(1-2n\ne0\). For \(A_4,B_4\), write
\[
P(u,v)=(n-1)(n-2)u^2+n(4n-3)uv+n(n-1)v^2.
\]
The two residual factors are \(P(u,v)\) and \(P(v,u)\), and their difference is \(-2(n-1)(u^2-v^2)\). A common projective zero would require \(u=v\) or \(u=-v\), but
\[
P(1,1)=6n^2-7n+2\ne0,\qquad P(1,-1)=-2n^2-n+2\ne0
\]
for all \(n\ge3\). The explicit remaining factors \(a\) and \(b\) do not introduce any further common component. Thus the common zero locus of the highest forms on the line at infinity consists precisely of the two coordinate points for \(1\le m<n\), and is empty when \(m=0\) or \((n,m)=(3,3)\).

**2. Exact local intersection multiplicities.** Let \(1\le m\le3\), \(n>m\), \(r=n-m\), \(M=m(n-1)\), and \(d=d_{m+1}\). A generic pair of affine hyperplane sections can be normalized, by row operations on their two highest-jet coefficients, to
\[
F=A_{m+1}+U,\qquad G=B_{m+1}+V,
\]
where \(U,V\) are independent generic linear combinations of \(1,A_0,B_0,\ldots,A_m,B_m\). Homogenize them to degree \(d\), and use local coordinates \(t=b/a\), \(z=Z/a\) near \([1:0:0]\). Give \(t\) weight \(M\) and \(z\) weight \(r\). The displayed jet formulas, with the lower-jet degrees, show that their minimal weighted components are
\[
\operatorname{in}(F)=c_1t^r+c_2z^M,\qquad
\operatorname{in}(G)=c_3z^M,
\]
with \(c_1c_3\ne0\) for a generic choice. Indeed, the \(t^r\) term comes from \(A_{m+1}\), the \(z^M\) term from \(B_1=a^n\), and all other monomials have larger weight: the earlier homogeneous jets have degrees \(1+j(n-1)\) and at least the displayed powers of \(b\). This last finite comparison only uses \(m\le3\), not a hypothesis on the size of \(n\). The two displayed initial forms form a homogeneous regular sequence in \(k[t,z]\); their initial ideal is equivalent to \((t^r,z^M)\), so the completed local intersection has length \(rM\). Equivalently, the flat weighted initial degeneration has length \(rM\). The symmetric calculation at \([0:1:0]\) has the same length. This proves the stated contribution \(m(n-1)(n-m)\) at each point.

**3. Bézout and generic reducedness.** The two normalized hyperplanes still describe a generic codimension-two affine linear slice of the graph. Since the graph is a smooth closed embedded copy of \(\mathbb A^2\) and the linear system contains \(1,a,b\), a generic slice has finitely many reduced points in the affine plane in characteristic zero. The two degree-\(d\) projective plane curves have no common component: otherwise their finite generic affine intersection or their relatively prime highest forms away from the two isolated points would fail. Bézout's theorem therefore gives
\[
\deg X_n^{(m)}=d^2-2m(n-1)(n-m)
=((m^2+1)n^2-m^2).
\]
For \(m=0\) and \((n,m)=(3,3)\), the highest forms are relatively prime, and Bézout gives the same formula without an infinity correction. This completes the proof.

## Verification

The attached `verify.py` builds the jets by exact symbolic differentiation and independently compares the fourth-jet closed form, all four binary gcds, the weighted initial monomials of representative generic hyperplane sections at infinity, and the degree identities for \(3\le n\le8\). The checker is a finite consistency test; the universal theorem follows from the preceding algebraic argument, not from these six tested exponents.

Reproduce with Python 3 and SymPy: `python verify.py`.

## Relationship to prior work

Puddu [1], Proposition 0.1 and Conjecture 4.1, establishes the graph parametrization and proposes the exact general two-parameter degree law. Its Section 4 explicitly states that extending its squarefree-transversality criterion is insufficient already for \((n,m)=(3,1)\) and \((3,2)\), and reports extensive computational checks of the gcd prediction. The present result proves **only** the uniform, geometrically nontrivial first four columns \(m\le3\), including exact nontransverse local multiplicities; the general conjecture is not claimed. Pogudin [2], Section 2, reports finite numerical values for the cubic-flow special case and poses the degree problem; these numerical values are not claimed as new. Lanciano [3] provides general upper bounds for certain prolongation varieties, not the displayed exact initial-order formula in the available abstract; its full text was not verified in this comparison.

## Limitations

There is no assertion for \(m\ge4\), where higher residual factors can be difficult to control. Characteristic-zero is used for the generic reducedness statement and to exclude exceptional coefficients. The numerical checker is finite; it is not an independent mathematical audit. A complete external priority examination of all unpublished and inaccessible literature has not been performed.

## References

1. Mattia Puddu, *On the geometric degree of the prolongation varieties of the differential system \(x_1'=x_2^2\), \(x_2'=x_1^2\)*, arXiv:2611.06638v1 (first public 2026-11-04), especially Proposition 0.1 and Section 4, Conjecture 4.1. https://arxiv.org/abs/2611.06638
2. Gleb Pogudin, *Some Open Problems in Differential Algebra* (2025), Section 2, Questions 5–7 and numerical examples. https://www.lix.polytechnique.fr/Labo/Gleb.POGUDIN/files/da_problems.pdf
3. Leonardo Lanciano, *Degrees and directional defects of embedded algebraic vector bundles*, arXiv:2609.27047 (2026), general bounds and related prolongation context. https://arxiv.org/abs/2609.27047
