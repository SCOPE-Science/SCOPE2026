# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Trigonal genus-6 canonical curve in the scroll S(2,2) with a certified
extra-syzygy witness (exact certificate over F_101)

## Theorem (fallback (b) of lane-373 admission)

Let k = F_101. Let S = S(2,2) ⊂ P^5_k be the rational normal 3-fold scroll,
image of φ: P^1 × P^1 → P^5, |O(1,2)|,

    φ((s:t),(u:v)) = (su² : suv : sv² : tu² : tuv : tv²) = (x0:…:x5).

Let F(s,t,u,v) = Σ_{i≤3,j≤4} c[i][j] s^{3-i} t^i u^{4-j} v^j with the committed
coefficient matrix (seed 606)

    [[94, 7, 46, 85, 55],
     [84, 44, 17, 58, 60],
     [57, 20, 85, 23, 83],
     [38, 2, 96, 42, 52]]

and C = V(F) ⊂ P^1 × P^1, X = φ(C) ⊂ P^5. Then:

1. **Scroll quadrics.** The pullback Sym_2(k^6) → H^0(P^1×P^1, O(2,4)) is
   surjective (rank 15); its kernel has dimension 6 and is spanned by the six
   2×2 minors of [[x0,x1,x3,x4],[x1,x2,x4,x5]]. These six quadrics generate
   the quadric part of the scroll ideal I_S.
2. **Smooth genus-6 canonical curve.** C is geometrically smooth: no
   P^1×P^1(F_101)-point has F = dF = 0 (90 F_101-points lie on C, none
   singular), and in each of the four affine charts 1 ∈ (f, f_x, f_y) via an
   explicit bounded Macaulay matrix (bound B = 14). Hence C is a smooth
   bidegree-(3,4) curve of genus g = (3−1)(4−1) = 6. By adjunction
   K_C = O(1,2)|_C, so X ⊂ P^5 is canonically embedded of degree 10.
3. **Scroll containment with identical quadrics.** X ⊂ S, and
   dim I_X,2 = 6: restriction H^0(O(2,4)) → H^0(C, O(2,4)|_C) is injective
   (kernel H^0(O(−1,0)) = 0), so the quadric kernel of X equals that of S.
   The cubic kernel has dimension h^0(I_X(3)) = 31.
4. **Trigonal.** The second ruling projection C → P^1 has degree 3 and no
   ruling fiber is contained in C (all 102 + 102 fibers checked nonzero), so
   C (hence X) is trigonal of Clifford index 1.
5. **Extra-syzygy witness.** The eight Eagon–Northcott linear relations
   r_a q_bc − r_b q_ac + r_c q_ab = 0 (column triples of the 2×4 matrix,
   both rows) are verified polynomial identities among the six quadrics,
   and their flattenings to 36-vectors have rank 8. Since the quadrics are
   minimal generators and all coefficients are linear, these represent
   nonzero minimal classes in the linear strand Tor_2(−,k)_3 of the
   homogeneous coordinate ring of X: a certified extra syzygy beyond the
   Green generic vanishing range.

## Proof and replay

All items are exact finite-field linear algebra over F_101 plus chart
Jacobian algebra, with no floating point. The single replay script uses
only the Python standard library:

    python3 output/artifacts/verify_fallbackB.py

It re-derives (1)–(5) from the committed file
`output/artifacts/curve_F101.json` and prints `VERIFY_OK`. Section-by-section
it checks: pullback rank 15 / kernel 6 / six minors independent in the
kernel; point smoothness over all 10404 P^1×P^1(F_101) points; cofactors
1 ∈ (f,f_x,f_y) in all four charts; cubic-kernel dimension 31 via
rank([A|M_F]) = 28, rank(M_F) = 3; the eight syzygy identities and their
rank 8. The no-fiber-contained trigonal check is a direct evaluation over
both rulings (also reproducible from the JSON coefficients).

## Remarks and scope

* This is exactly predefined fallback (b): a certified trigonal genus-6
  curve in an explicit rational normal scroll with a verified extra syzygy
  witness. The full generic-vs-trigonal separation (target) is NOT claimed:
  no generic-side vanishing cell is certified here.
* The certificate is over F_101, not Q. The scroll, minors, and syzygies are
  defined over Z (hence lift); the curve's integer lift is smooth over Q by
  openness of smoothness, but that transfer is recorded as a remark, not
  part of the certified claim.
* Minimality/non-boundary status follows from the standard graded-minimal
  argument (linear coefficients against minimal quadric generators), stated
  explicitly rather than by an additional matrix computation.
