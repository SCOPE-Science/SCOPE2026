# Hasse–Witt and Newton strata of the 48-symmetry plane quartic in every characteristic at least five

## Finding
For every prime \(p\geq5\), let \(C_p\) denote the smooth projective plane quartic over \(\overline{\mathbb F}_p\) defined by
\[
X^4+Y^4+XZ^3=0.
\]
The following table gives the \(p\)-rank \(f\), the \(a\)-number \(a\) of its Jacobian, and the multiset of slopes of its Newton polygon. Exponents after slopes denote multiplicities.

| \(p\bmod 12\) | \(f\) | \(a\) | Newton slopes |
|:--:|:--:|:--:|:--|
| \(1\) | \(3\) | \(0\) | \(0^{[3]},1^{[3]}\) |
| \(5\) | \(2\) | \(1\) | \(0^{[2]},(1/2)^{[2]},1^{[2]}\) |
| \(7\) | \(1\) | \(2\) | \(0^{[1]},(1/2)^{[4]},1^{[1]}\) |
| \(11\) | \(0\) | \(3\) | \((1/2)^{[6]}\) |

The superspecial case \(p\equiv11\pmod{12}\) was previously known; the assertion here is the complete four-class stratification, in particular the two intermediate Newton polygons and their \(a\)-numbers.

## Assumptions and scope
The field is algebraically closed of prime characteristic \(p\geq5\). The \(p\)-rank is \(\dim_{\mathbb F_p}J[p](\overline{\mathbb F}_p)\). The \(a\)-number is \(\dim\operatorname{Hom}(\alpha_p,J[p])\). Newton slopes count the height-six rational Dieudonné isocrystal of the principally polarized threefold \(J=\operatorname{Jac}(C_p)\). No statement is made for characteristics two or three or for other quartics.

The partial derivatives of the defining quartic are \(4X^3+Z^3\), \(4Y^3\), and \(3XZ^2\). If all vanish at a projective point, then \(Y=0\) and \(XZ=0\), while the first derivative cannot vanish in either case. Thus the curve is smooth and has genus three.

## Proof
For a nonsingular plane quartic \(F=0\), the standard coefficient description of Frobenius on \(H^1(C,\mathcal O_C)\), using the basis of Cech monomials indexed by
\[
\alpha_1=(2,1,1),\qquad\alpha_2=(1,2,1),\qquad\alpha_3=(1,1,2),
\]
gives a matrix \(H=(h_{ij})\) in which \(h_{ij}\) is the coefficient in \(F^{p-1}\) of the monomial with exponent vector \(p\alpha_i-\alpha_j\). Transposing conventions does not change any rank.

In this case
\[
F^{p-1}=\sum_{u+v+w=p-1}\binom{p-1}{u,v,w}X^{4u+w}Y^{4v}Z^{3w}.
\]
Consequently a potential nonzero entry corresponds exactly to a nonnegative integer solution
\[
4v=p\alpha_{i,2}-\alpha_{j,2},\quad
3w=p\alpha_{i,3}-\alpha_{j,3},\quad
4u+w=p\alpha_{i,1}-\alpha_{j,1},\quad
u+v+w=p-1.
\]
Write \(p=12k+r\) with \(r\in\{1,5,7,11\}\). Solving these three exponent congruences and the sum condition produces the following exhaustive supports; tuples list \((u,v,w)\), and subscripts are matrix indices.

| \(r\) | Nonzero entries and their multinomial indices |
|:--:|:--|
| \(1\) | \(h_{11}:(5k,3k,4k)\), \(h_{22}:(2k,6k,4k)\), \(h_{33}:(k,3k,8k)\) |
| \(5\) | \(h_{13}:(5k+2,3k+1,4k+1)\), \(h_{31}:(k,3k+1,8k+3)\) |
| \(7\) | \(h_{22}:(2k+1,6k+3,4k+2)\) |
| \(11\) | no entries |

For every displayed entry, all three indices are nonnegative and sum to \(p-1\). Since \(p-1<p\), their multinomial coefficient is nonzero modulo \(p\), as are all factorials involved. Hence \(H\) is respectively a nonzero diagonal matrix of rank three; an invertible two-by-two off-diagonal block on coordinates one and three, with rank two; one nonzero central diagonal entry of rank one; or zero.

These matrices have the same ranks under every positive power (the rank-two off-diagonal block has nonzero product of its two entries). Since the coefficients lie in \(\mathbb F_p\), semilinear Frobenius iteration has the same stable ranks. Its stable rank therefore gives \(f=3,2,1,0\) respectively. The Cartier kernel has dimension \(3-\operatorname{rank}H\), giving \(a=0,1,2,3\).

For a principally polarized abelian threefold of \(p\)-rank at least one, the \(2f\) ordinary slopes \(0,1\) leave a symmetric nonordinary remainder of height at most four with zero \(p\)-rank. A symmetric height-two factor has slopes \(1/2,1/2\); a height-four factor of \(p\)-rank zero must also have four slopes \(1/2\), because any distinct positive rational slope below \(1/2\) would require an isoclinic factor whose denominator is at least three, and its dual would make the total height at least six. Thus the first three Newton polygons follow. In the final case, \(a=3=\dim J\) implies superspeciality, and its slopes are all \(1/2\).

## Verification
The self-contained `verify.py` independently forms the coefficient matrix by full multinomial expansion and by direct solution of the exponent equations for every prime between five and 109. It verifies equality of both matrices, the stated support and the stable ranks of the first three powers. The program exits with `VERIFY_OK` on success. This is a finite check; the all-prime theorem rests on the exhaustive symbolic support computation in the proof above, not on extrapolation.

Run with `python3 verify.py` (Python standard library only).

## Relationship to prior work
Janasz [1] studies the complex geometric incidence properties of precisely this 48-automorphism plane quartic; his results motivate the arithmetic reduction question, rather than determining its \(p\)-rank stratification. The curve is equivalent under a swap of coordinates to the quartic \(X^4+Y^4+YZ^3=0\). Ohashi [2, introduction], citing Brock [3], explicitly records the already known superspecial criterion \(p\equiv11\pmod{12}\); that endpoint is not claimed as new. Moriya and Kudo [4] give arithmetic tools for genus-three curves and superspecial Howe curves, not the four-line classification proved here in the inspected sections. The calculation is an exact specialization of the standard Hasse–Witt coefficient method, not a new general algorithm.

## Limitations
This determines Newton slopes, \(p\)-rank, and \(a\)-number, not full zeta functions, isogeny factors over \(\mathbb F_p\), or Ekedahl–Oort types beyond the stated invariants. An exhaustive examination of Brock's 1993 thesis was not possible, so overlap with unpublished or unindexed tables remains a residual risk. The characterization of the 48-automorphism model is taken from the characteristic-zero literature; no claim is made about the full automorphism group after reduction in every characteristic.

## References
1. Marek Janasz, *On symmetric plane quartic curves*, arXiv:2406.07015v1 (submitted 2024-06-11), especially the section on the quartic with 48 automorphisms. https://arxiv.org/abs/2406.07015
2. Ryo Ohashi, *Superspecial plane quintics with large automorphism groups*, arXiv:2605.29624 (2026), introduction and bibliography. https://arxiv.org/abs/2605.29624
3. B. W. Brock, *Superspecial curves of genera two and three*, PhD thesis, Princeton University (1993), as cited in [2]; full text not inspected.
4. Tomoki Moriya and Momonari Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926. https://arxiv.org/abs/2209.02926
