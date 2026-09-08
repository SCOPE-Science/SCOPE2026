# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# WLP failure in characteristic 2 for an explicit non-monomial (3,3,4) complete intersection

## Status of this note
Self-contained report of a finite, exactly verified computation over F2.
Section 1 states the theorem. Section 2 gives the human-checkable certificate.
Section 3 describes the machine verification. Section 4 separates what is proved,
what is computed evidence, and what remains open. A one-term repair of the
originally admitted ideal is disclosed explicitly (see §1 and §4).

## 1. Theorem

Work over F2. Let

    f1 = x^3 + y^2 z + y z^2,
    f2 = y^3 + x^2 z + x z^2,
    f3' = z^4 + x y^3 + x^3 y + x^4,

and A' = F2[x,y,z]/(f1,f2,f3').

**Theorem.** (a) A' is an Artinian complete intersection of type (3,3,4):
its Hilbert function is exactly

    (1, 3, 6, 8, 8, 6, 3, 1, 0, 0, ...),

so dim A'_3 = dim A'_4 = 8, total length 36 = 3·3·4, socle degree 7.

(b) For ell = x+y+z, the multiplication map ×ell : A'_3 -> A'_4 has rank 7 < 8
(maximal rank). Hence A' fails the Weak Lefschetz Property in characteristic 2,
witnessed in degree 3 -> 4.

(c) The failure is ell-specific, not a collapse: ×x : A'_3 -> A'_4 is an
isomorphism (rank 8, det 1); x and y are strong Lefschetz elements (full rank
in every degree), while z, x+y, x+y+z fail somewhere.

**Disclosure.** The originally admitted triple used f3 = z^4+xy^3+x^3y (no x^4
term). That triple is *not* a complete intersection over F2: its quotient has
Hilbert values [1,3,6,8,8,6,3,2,2,2,...], tail-stabilizing at 2, hence not
Artinian. The addition of x^4 to f3 is the minimal committed repair restoring
the CI property (f3+y^4 and f3+x^2y^2 work as well; f3+x^3z does not). All
statements above concern the repaired ideal (f1,f2,f3').

## 2. Human-checkable certificate for (b)

Let k = y^2 z + x y^2 + x^2 z + x^2 y (exponents (0,2,1),(1,2,0),(2,0,1),(2,1,0)).

(i) k is nonzero in A'_3. Indeed I_3 is spanned by f1, f2 (f3' has degree 4),
so its four elements are 0, f1, f2, f1+f2; k equals none of them by direct
monomial comparison. So [k] != 0 in A'_3.

(ii) ell·k lies in the ideal. Over F2:

    (x+y+z)(y^2 z + x y^2 + x^2 z + x^2 y) = y·f1 + x·f2.

Both sides expand to

    x^3 y + y^3 z + y^2 z^2 + x y^3 + x^3 z + x^2 z^2,

checkable by hand (12 monomial products on the left, 6 on the right; all
arithmetic in F2). Hence ×ell([k]) = 0 in A'_4 while [k] != 0, so ×ell has
nontrivial kernel and rank <= 7 < 8 = maximal rank.

The machine computation sharpens this to rank exactly 7 (det 0; integer lift
of the 8×8 matrix has det -2), with kernel coords [0,1,0,0,1,1,1,0] on the
quotient basis below and cokernel functional [0,1,1,0,1,1,1,0].

## 3. Machine verification (exact F2 linear algebra, stdlib only)

Replayer: `output/artifacts/verify.py` (no third-party imports), prints VERIFY_OK.

- Monomial bases of each degree d; rows of the Macaulay matrix of I_d from
  multiples m·fi; rank over F2 by exact elimination; dim A_d = ncols − rank.
  Result: [1,3,6,8,8,6,3,1,0] for d = 0..8 (proving (a) together with the
  observation that I_8 = whole space implies A_d = 0 for d >= 8).
- Quotient bases by rref free columns:
  A3 = {z^3, y^2z, xz^2, xyz, xy^2, x^2z, x^2y, x^3},
  A4 = {xz^3, xy^2z, x^2z^2, x^2yz, x^2y^2, x^3z, x^3y, x^4}.
- Multiplication matrices ×L : A3 -> A4 built by reducing L·m through the rref
  of I_4. For L = x: identity matrix (rank 8, det 1). For L = x+y+z: the rows
  00000001 / 01000010 / 11100001 / 00010001 / 01101100 / 00110100 / 00011010 /
  00000111, rank 7, det 0.
- Full-degree profiles for all 7 nonzero F2 linear forms computed; x, y, x+z,
  y+z have full rank in every degree (strong Lefschetz); z, x+y, x+y+z do not.
- Cross-checks: sympy lex Gröbner basis over GF(2) contains the pure powers
  y^6 and z^8 (consistent with zero-dimensionality); brute-force projective
  common zeros of (f1,f2,f3') are empty over F2, F4, F8, F16.

## 4. Proof vs computed evidence vs conjecture vs uncertainty

- **Proved (hand-checkable):** the kernel identity of §2, hence ×(x+y+z) :
  A'_3 -> A'_4 is not injective *conditional on* (a); non-membership k ∉ I_3
  (§2(i)) is also hand-checkable.
- **Computed evidence (machine, exact, replayable):** part (a) (Hilbert
  function via Macaulay ranks), exact rank values 7 vs 8, quotient bases,
  full-form profiles, Gröbner/zero-count cross-checks.
- **Conjecture (not claimed):** that the 2-parameter determinantal
  non-Lefschetz locus around this point has any stated closed form — no
  formula is claimed here.
- **Uncertainty / limitations:**
  (1) The verdict applies to the repaired ideal (f1,f2,f3'+x^4 form), not the
  as-written non-Artinian triple; the repair is minimal and disclosed but it
  is a deviation from the admitted object.
  (2) Only characteristic 2 and the named forms are treated; no claim over Q
  (Harima–Migliore–Nagel–Watanabe show height-3 CIs have WLP in char 0) and no
  claim for all linear forms (indeed x is Lefschetz).
  (3) No claim that the Li–Zanello/Brenner–Kaid classifications are wrong in
  their stated (monomial/diagonal) scope; the point is only that this
  non-monomial deformation lies outside them and fails WLP at ell = x+y+z.
  (4) Syzygy-splitting cross-check from the audit plan was replaced by the
  stronger full-profile Lefschetz-element contrast (×x an isomorphism);
  no splitting-type statement is claimed.

## References (nearest prior art; scope restrictions verified)

- Harima–Migliore–Nagel–Watanabe, arXiv:math/0208201 (char 0 only; every
  height-3 CI has WLP — hence no Q-side claim is made here).
- Li–Zanello, arXiv:1002.4400 (monomial CIs only, via plane partitions).
- Brenner–Kaid, arXiv:1003.0824 (diagonal monomials (X^d,Y^d,Z^d) only).
- Boij–Migliore–Miró-Roig–Nagel, arXiv:2212.09890 (height-4 equigenerated
  frontier; downstream relevance, not an overlapping verdict).
