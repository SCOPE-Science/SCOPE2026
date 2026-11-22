# Cartier \(a\)-numbers of all 215 excessive genus-three curves over finite fields

## Finding

For the complete list of 215 isomorphism classes of smooth genus-three curves of gonality four over finite fields, classified by Faber, Grantham and Howe, the geometric Jacobian Cartier \(a\)-numbers have exact distribution
\[
\#\{a=0\}=179,\qquad \#\{a=1\}=32,\qquad \#\{a=2\}=4,\qquad \#\{a=3\}=0.
\]
Thus no such curve has a superspecial Jacobian. The four cases with \(a=2\) occur exclusively in characteristic three: one over \(\mathbb F_3\) and three over \(\mathbb F_9\). All curves over fields with at least 13 elements, and also the unique example over \(\mathbb F_{32}\), are ordinary. These are counts of isomorphism classes, not of coefficient-marked equations.

| Field size \(q\) | \(a=0\) | \(a=1\) | \(a=2\) |
|---|---:|---:|---:|
| 2 | 2 | 2 | 0 |
| 3 | 5 | 2 | 1 |
| 4 | 15 | 6 | 0 |
| 5 | 26 | 5 | 0 |
| 7 | 28 | 4 | 0 |
| 8 | 36 | 3 | 0 |
| 9 | 18 | 6 | 3 |
| 11 | 17 | 4 | 0 |
| 13 | 11 | 0 | 0 |
| 16 | 8 | 0 | 0 |
| 17 | 7 | 0 | 0 |
| 19 | 2 | 0 | 0 |
| 23 | 2 | 0 | 0 |
| 29 | 1 | 0 | 0 |
| 32 | 1 | 0 | 0 |
| **Total** | **179** | **32** | **4** |

## Assumptions and scope

For each listed field \(\mathbb F_q\) of characteristic \(p\), use exactly one homogeneous plane quartic \(F(X,Y,Z)=0\) from the publicly released 215-class data. The associated smooth curve has genus three. For a curve \(C\), define \(a(C)=\dim_{\overline{\mathbb F}_q}\operatorname{Hom}(\alpha_p,J(C)[p])\), equivalently the dimension of the kernel of Cartier acting on its three-dimensional space of global regular differentials. This invariant depends on geometric isomorphism class, so the original class census supplies completeness.

The accompanying `coefficients.json` gives one 15-character polynomial-coefficient string per class, in the original source's order for each field. Its alphabet is `0123456789abcdefghijklmnopqrstuv`; the position order is the homogeneous monomials \(X^iY^jZ^{4-i-j}\), first decreasing \(i\), then decreasing \(j\). The coefficient digit is the integer in \([0,q-1]\) representing a finite-field element in a polynomial basis. For extension fields the distinguished generator is defined by \(r^2+r+1\) for \(q=4\), \(r^3+r+1\) for \(q=8\), \(r^2+2r+2\) for \(q=9\), \(r^4+r+1\) for \(q=16\), and \(r^5+r^2+1\) for \(q=32\). Each numeral is the base-\(p\) encoding of its coefficients in powers of \(r\).

## Proof

For a nonsingular plane quartic, the adjunction description \(H^0(C,\Omega^1_C)\cong H^0(\mathbb P^2,\mathcal O(1))\) gives a basis indexed by \(e_1=(1,0,0)\), \(e_2=(0,1,0)\), \(e_3=(0,0,1)\). The plane-hypersurface Hasse–Witt coefficient formula yields the matrix \(H\) whose entry with row \(u\) and column \(v\) is the coefficient
\[
H_{uv}=[X^{pu_X-v_X+p-1}Y^{pu_Y-v_Y+p-1}Z^{pu_Z-v_Z+p-1}]F^{p-1}.
\]
The transpose/Frobenius-semilinear conventions change the representation but not its rank. Duality between Hasse–Witt and Cartier shows \(a(C)=3-\operatorname{rank}(H)\) over the algebraic closure. This is a theorem for every smooth quartic, not a numerical conjecture.

`verify.py` performs exact arithmetic in the defining finite fields, constructs the full sparse polynomial power \(F^{p-1}\), extracts nine specified coefficients, and applies finite-field Gaussian elimination. It checks all 215 encoded curves, verifies each has no rational projective point over its designated field, asserts the complete per-field and global distributions, and identifies all rank-one matrices. The full exhaustive verification terminates with `EXACT_QUARTIC_CARTIER_CENSUS_VERIFIED`. Combining this finite exhaustive calculation with the source's 215-class completeness theorem establishes the claim.

The four matrices of rank one correspond, in the order of the coefficient table, to \((q,i)=(3,5),(9,25),(9,26),(9,27)\). The characteristic-three example is
\[
X^4+XY^3+2Y^4+2Y^2Z^2+Z^4=0.
\]
The three characteristic-nine examples consist of a conjugate pair
\[
X^4+2X^2Y^2+rY^4+r^2Z^4=0
\]
(with the other obtained by \(r\mapsto r^3\)), and the curve
\[
X^4+rX^2Y^2+Y^4+rZ^4=0,
\]
where \(r^2+2r+2=0\) in \(\mathbb F_9\).

## Verification

Run `python3 verify.py coefficients.json` in a directory containing both files; Python 3 standard library suffices. The script checks every input coefficient belongs to its field, all 215 pointlessness claims, and the exact ranks. The finite exhaustive evidence is the actual coefficient table and executable calculation, not an output log alone. Because the published classification proves the source list complete and free of duplicate isomorphism classes, the 215 computations imply a classification rather than a sample.

## Relationship to prior work

Faber–Grantham–Howe, *On the Maximum Gonality of a Curve over a Finite Field* (arXiv:2207.14307, first posted 2022-07-28; journal version 2025), establish the 215-class enumeration, their gonality and equations. Their `AllGenus3.magma` supplementary file (version 1.02) lists defining quartics, real Weil polynomials and arithmetic automorphism-group labels. These are **not** claimed as new. The newly calculated invariant is the classwise Cartier \(a\)-number distribution and its exact four deepest cases. The relevant general coefficient-extraction/Cartier theory is classical, and calculating each row is straightforward, but the complete finite classification and its sharp characteristic-three concentration are additional arithmetic invariants not presented in the inspected classification paper or source's stated output schema.

## Limitations

This does not classify Ekedahl–Oort types, Newton polygons or full geometric \(p\)-torsion group schemes. The curves' smoothness, mutual nonisomorphism and completeness are taken from the established source theorem; the verifier independently rechecks coefficient parsing, pointlessness and every Cartier rank, not exhaustive smoothness or isomorphism testing. The search cannot exclude an unpublished or unindexed independent \(a\)-number table. The coefficient transcription is supplied so this scope and its arithmetic can be independently reproduced.

## References

1. X. Faber, J. Grantham and E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307 (2022), https://arxiv.org/abs/2207.14307 ; published in *Algebra & Number Theory* 19 (2025), 1637–1662, https://doi.org/10.2140/ant.2025.19.1637 .
2. Same authors, publicly released source models in `scripts/AllGenus3.magma`, https://github.com/RationalPoint/excessive/blob/main/scripts/AllGenus3.magma .
3. General Hasse–Witt coefficient formula for smooth plane curves (classical adjunction and Frobenius action).
