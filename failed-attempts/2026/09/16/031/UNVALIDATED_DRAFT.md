# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Non-fillability of the max-tb T(−7, 6): ruling rigidity plus the signature bound

## 1. Setting and claim

Let Λ be a maximal Thurston–Bennequin Legendrian representative of the torus
knot T(−7, 6), with the max-tb front of Figure 17 of
Chen–Crider-Phillips–Reinoso–Sabloff–Yao (arXiv:2203.16605), hereafter CCPRSY.
Its classical invariants are tb(Λ) = pq = −42 (Etnyre–Honda, via CCPRSY §6).

**Theorem.** Λ admits no decomposable exact non-orientable Lagrangian filling
in (B⁴, ω₀). In particular, the smallest open case q ≡ 2 mod 4 left unresolved
by CCPRSY Theorem 1.5 and Conjecture 6.3 is non-fillable; the unoriented
resolution-linking obstruction vanishes there (rlk₂ = 0), so a new obstruction
is required, supplied here by the knot signature.

Since the argument uses only the smooth topology forced by the unique ruling,
it in fact rules out any (not necessarily Lagrangian) Möbius-band spanning
surface with the same normal Euler number; the Lagrangian structure is used to
pin down (χ, e) via the canonical ruling and tb = −χ − e.

## 2. Step 1 — the unique ruling forces (χ, e) = (0, 42)

By CCPRSY Lemma 6.1 (Kauffman-polynomial coefficient = z, via Yokota), a
max-tb front of T(p, q) with p < 0 and q even has a *unique* normal ruling ρ.
The proof of CCPRSY Lemma 6.2 records the numerics of the Figure-17 front:
|p|(q − 1) crossings and |p| right cusps, with |p| ruling disks and |p|
switches. For (p, q) = (−7, 6): 35 crossings, 7 right cusps, 7 disks,
7 switches. Hence, with χ(ρ) = c(Λ) − s(ρ) (CCPRSY Def. 3.1),

χ(ρ) = 7 − 7 = 0.

If L were a decomposable exact filling, its canonical ruling (Atiponrat;
CCPRSY §3.3) would equal this unique ρ, and by CCPRSY Prop. 3.11,
χ(L) = χ(ρ) − χ(∅) = 0. A filling of a knot with χ = 0 is either a
connected Möbius band (b₁ = 1) or a disk plus a closed component; the latter
is impossible for an *exact* Lagrangian in B⁴ (Gromov: no closed exact
Lagrangians in ℂ²), so L would be a Möbius band. By CCPRSY Prop. 2.5,
tb(Λ) = −χ(L) − e(L), giving

e(L) = −(−42) − 0 = 42.

## 3. Step 2 — the Gordon–Litherland bound

For a (possibly non-orientable) compact surface F ⊂ B⁴ with ∂F = K, let e(F)
be the relative normal Euler number (Seifert-framed pushoff convention, as in
CCPRSY §2.1) and σ(K) the classical Murasugi signature. Gordon–Litherland
(Invent. Math. 47 (1978), Theorem 2′ / Corollary 2″; see also §2A: the bound
|σ(K) − e(F)/2| ≤ b₁(F) for the Goeritz-form signature) gives: with the
conventions in which the formula reads σ(K) = sign(G_F) − e(F)/2,

|σ(K) − e(F)/2| ≤ b₁(F).       (†)

*Sign-variant selection.* Two sign variants of (†) circulate depending on
orientation/Euler conventions, differing by e ↦ −e. We fix ours empirically on
a known-fillable control in the same family: T(−5, 2) admits a decomposable
non-orientable filling (CCPRSY Thm. 1.5(2)); its unique ruling likewise forces
a Möbius band with e = |pq| = 10, and its signature is σ = +4 (computed
below). The variant |σ − e/2| ≤ b₁ gives |4 − 5| = 1 ≤ 1 ✓, while the flipped
variant gives |4 + 5| = 9 > 1 ✗ (which would falsely rule out a proven
filling). Hence |σ − e/2| ≤ b₁ is the correct variant under our (σ, e)
conventions, and it is the one applied to T(−7, 6).

## 4. Step 3 — signature of T(−7, 6) and contradiction

Reproducible computation (artifact `artifacts/goeritz_sig.py`, Sage-free
Goeritz/Gordon–Litherland code replicating spherogram's white-graph +
Goeritz-matrix + `signature(new_convention=True)` pipeline) gives, in the
convention where positive torus knots have negative signature:

σ(T(−7, 6)) = +18.

Verification: (i) white-graph and black-graph (complementary checkerboard)
computations agree on every input; (ii) calibrations T(2,3) → −2,
T(2,−3) → +2, T(3,4) → −6, T(−5,2) → +4 (the latter equals p − 1, the known
T(−p, 2) formula); (iii) swap symmetry T(6,7) = T(7,6) → −18 on a different
(35-crossing) projection; (iv) mirror antisymmetry σ + σ̄ = 0 and double-mirror
stability; (v) determinant cross-checks via the Alexander polynomial at t = −1
(det T(7,6) = 7). Eigenvalue signatures use tolerance 1e−8; all Goeritz
matrices here are nonsingular on the reduced block (det = knot determinant,
odd), so no near-zero ambiguity. Full table in `artifacts/sig_table.txt`.

Insert σ = 18, e = 42, b₁ = 1 into (†):

|18 − 42/2| = |18 − 21| = 3 > 1 = b₁(F),

a contradiction. Therefore no Möbius-band surface in B⁴ with e = 42 bounded by
T(−7, 6) exists smoothly; a fortiori no decomposable exact non-orientable
Lagrangian filling of Λ exists.

## 5. Scope, limitations, and what is not claimed

- The theorem covers the *smallest* (and flagship) q ≡ 2 mod 4 case, T(−7, 6),
  where all previously published obstructions (Kauffman sharpness, oriented vs.
  unoriented ruling polynomials, rlk₂) vanish. It does not settle the whole
  family: the same test passes for e.g. T(−5, 6) (|16 − 15| = 1) and T(−11, 6),
  while it also obstructs T(−13, 6), T(−19, 6), T(−11, 10), T(−9, 10),
  T(−5, 14). The family question as stated hence remains open in general.
- The proof assumes the max-tb front numerics as recorded in CCPRSY Lemma 6.2
  (|p| cusps, |p| switches); the tb = −42 count is consistent (writhe −35 minus
  7 right cusps). The connectedness appeal uses Gromov's theorem (standard).
- The "any exact filling is decomposable" converse is not used; the claim is
  restricted to *decomposable* exact fillings, matching the target's wording.
- Signature computations are machine-assisted but cross-validated as above;
  the single mathematical input beyond CCPRSY + Gordon–Litherland is σ = 18,
  corroborated by five independent consistency checks.

## References

- L. Chen, G. Crider-Phillips, B. Reinoso, J. M. Sabloff, L. Yao,
  Non-orientable Lagrangian fillings of Legendrian knots, Math. Proc. Camb.
  Philos. Soc. (2023); arXiv:2203.16605. (Props. 2.5, 3.11; Lemmas 6.1–6.2;
  Thm. 1.5; Conj. 6.3; Fig. 17.)
- J. B. Etnyre, K. Honda, Knots and contact geometry I: torus knots and the
  figure eight knot, J. Symplectic Geom. 1 (2001), 63–120. (max-tb = pq.)
- C. McA. Gordon, R. A. Litherland, On the signature of a link, Invent. Math.
  47 (1978), 53–69. (signature bound (†).)
- M. Gromov, Pseudo-holomorphic curves in symplectic manifolds, Invent. Math.
  82 (1985). (No closed exact Lagrangians in ℂ²; used only to exclude a
  disconnected disk ⊔ closed-surface alternative.)
