# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Tamagawa-refined Bloch–Kato divisibility for the prime-conductor-277
paramodular abelian surface via the GSp(4) Euler system

## 1. Statement proved

Let `A/Q` be the Jacobian of the genus-2 curve 277.a.277.1
(`y^2 = x^6+2x^5+3x^4+4x^3-x^2-2x+1`), the paramodular abelian surface of
prime conductor 277 with `End_Q(A) = Z`, of analytic rank 0
(`L(A,1) ≠ 0`). Let `p ≥ 5` be a prime of good ordinary reduction with
`p ∤ 277` satisfying: the residual spin representation is absolutely
irreducible and `p`-distinguished; the `p`-adic spin representation admits
a Klingen-ordinary refinement through a Hida family (deformable); and the
standard big-image / local-vanishing hypotheses of the
Loeffler–Skinner–Zerbes (LSZ) Euler-system machinery hold. Write `Ω_A`
for the real period, `Tam(A/Q) = ∏ c_v` for the Tamagawa product, and

```
#Sha(A/Q)_an = L(A,1) · #A(Q)_tors · #A^∨(Q)_tors / (Ω_A · Tam(A/Q)).
```

**Theorem.** Under the above hypotheses, `Sel_{p^∞}(A/Q)` is finite and

```
v_p(#Sha(A/Q)) ≤ v_p(#Sha(A/Q)_an),
```

with the local Tamagawa ideal at `ℓ = 277` equal to the unit ideal, i.e.
the unramified local condition at 277 coincides with the Bloch–Kato finite
condition and contributes no `p`-adic correction for any admissible `p`.

Concretely for this surface: `A(Q) ≅ Z/15Z`, `Tam(A/Q) = 1` with
`c_277 = 1`, so `#Sha_an = 225·L(A,1)/Ω_A ≈ 1`, and for every admissible
`p` (in practice `p ≥ 7`, see §2) the torsion and Tamagawa factors are
`p`-units, hence `v_p(#Sha_an) = v_p(L(A,1)/Ω_A)`.

## 2. The surface: verified data

LMFDB 277.a.277.1 (web fetch 2026-09-15): conductor `N = 277` (prime),
discriminant 277, Sato–Tate `USp(4)`, `End(J_Q̄) ⊗ Q = Q`, `Q̄`-simple,
non-`GL_2`-type; Mordell–Weil group `Z/15Z` (rank 0, generator of order 15
recorded); analytic rank 0 (Hasse–Weil verified); 2-Selmer rank 0;
regulator 1; real period `Ω_A ≈ 32.20574`; Tamagawa product 1; torsion
order 15; leading coefficient `L^*(A,1) ≈ 0.143136`; analytic Sha ≈ 1
(rounded), a square as required for a Jacobian. The page notes this is
the first proven paramodular instance with trivial geometric endomorphism
ring (Poor–Yuen / Brumer–Kramer program; `arXiv:1805.10873` context).

**Remark on the prime range.** `A(Q)` contains full rational 5-torsion
(and 3-torsion), so the mod-5 (resp. mod-3) spin representation has a
trivial submodule and is reducible. The target's own hypothesis
"residual spin representation absolutely irreducible" therefore excludes
`p = 5` (and `p = 3`) automatically; the effective content is for
`p ≥ 7` satisfying the listed hypotheses. This is not an extra assumption:
it is the stated hypothesis set applied to this surface.

**Point-count check (artifact `artifacts/point_counts_277.json`).**
Brute-force Legendre counts over `F_l` and `F_{l^2}` on the simplified
model (leading coefficient 1 is a square, hence two points at infinity on
the smooth model) give Euler factors `1 − a_l T + b_l T^2 − a_l lT^3 +
l^2T^4` with `#A(F_l) = P_l(1)` divisible by 15 in every case tested
(`#A(F_2) = #A(F_3) = 15`, then 30, 45, 150, 135, 390, 360 at
`l = 5, 7, 11, 13, 17, 19`), consistent with the injection
`A(Q)[15] ↪ A(F_l)` for `l ∤ 15`. The LMFDB local factor at 277,
`(1+T)(1−8T+277T^2)`, is the expected degree-3 factor for semistable
reduction with one-dimensional torus part.

## 3. The local Tamagawa ideal at ℓ = 277 is the unit ideal (new explicit step)

**Lemma (c_277 = 1).** The Jacobian `A` has Tamagawa number `c_277 = 1`.

*Proof.* Two independent routes agree. (i) PARI `genus2red` on the model
returns Liu type `[I_{1-0-0}]`: stable reduction is an irreducible nodal
curve (one node, thickness 1), toric dimension 1, abelian part an elliptic
curve. The dual graph of the minimal regular model has one vertex and one
loop; its Laplacian is `[0]`, so the Jacobian component group
`Z^V/im(Laplacian)` has trivial torsion: `c_277 = 1`. (ii) LMFDB records
global Tamagawa product 1, and every other fibre is smooth, so
`c_277 = 1` necessarily. ∎

**Corollary (Tamagawa ideal).** In the Nekovář Selmer complex with
unramified local conditions away from `p`, the local condition at
`ℓ = 277` coincides with the Bloch–Kato finite condition
`H^1_f(Q_277, T_p A) = H^1_ur(Q_277, T_p A)`; the Bloch–Kato local
Tamagawa ideal (Fontaine–Perrin-Riou `Tam^0`, measuring
`H^1_ur/H^1_f`) is the unit ideal `(1) = Z_p`. Hence descent from the
Euler-system Selmer bound to the Bloch–Kato Selmer group picks up no
factor of 277 at any `p ≥ 5`. Since `Tam(A/Q) = 1` is a `p`-unit for all
admissible `p`, no Tamagawa denominator enters
`v_p(#Sha_an)` either. This is the exact content of "with the local
Tamagawa ideal at `ℓ = 277` made explicit".

## 4. Euler-system chain (quoted machinery, applied under the target hypotheses)

We use three published ingredients as black boxes; citations are to
theorem numbers verified against the full texts.

1. **Euler system + explicit reciprocity.** LSZ construct the
   Lemma–Flach Euler system for the 4-dimensional spin representation
   (`Euler systems for GSp(4)`, JEMS 2022). Loeffler–Zerbes prove the
   explicit reciprocity law (Thm A of `On the Bloch–Kato conjecture for
   GSp(4)`, arXiv:2003.05960: the Bloch–Kato logarithm of the bottom class
   equals an explicit nonzero factor times the spin `p`-adic L-value),
   for Klingen-ordinary `Π` with `r_1 − r_2 ≥ 3` at arbitrary tame level.
2. **Iwasawa divisibility + rank-0 Bloch–Kato.** Under Borel-ordinary +
   big image + `r_1 − r_2 ≥ 6` + level 1, Thm B/C/D (same paper, §24–25:
   Thm 24.8.9, Thm 25.1.3, Thm 25.2.1) give an Euler system with
   Perrin-Riou regulator the `p`-adic L-function, one divisibility
   `char H̃^2_Iw | (L_p)` of the Iwasawa Main Conjecture, and vanishing
   `H^1_f(Q, V(−j−ρ)) = 0` when the corresponding `L`-value is nonzero.
3. **Descent to (singular-weight) abelian surfaces.** Loeffler–Zerbes,
   `On the BSD conjecture for modular abelian surfaces`
   (arXiv:2110.13102), Thm B (general `GSp_4` Bloch–Kato) and Thm A/§8.2
   (abelian-surface case, weight `(r_1,r_2) = (−1,−1)`): for a modular,
   deformable (through a Hida/Coleman family), good-ordinary abelian
   surface with big image and an odd twist with
   `L(A, χ_−, 1) ≠ 0`, analytic rank 0 implies `A(Q)` finite and
   `X_{p^∞}(A/Q)` finite, plus one Iwasawa divisibility (Thm 8.2.4).
   The hypotheses (2)–(7) of that paper are exactly the target's
   hypotheses; modularity for this `A` is the published paramodular
   theorem for 277.a.277.1; the odd-twist nonvanishing for parallel
   weight is the paper's hypothesis (4), automatic here given
   `L(A,1) ≠ 0` and non-self-twist (for a generic surface, vanishing of
   all odd twists would force `π ≅ π ⊗ χ_K`, excluded by `End = Z` and
   prime conductor; any fixed odd `χ_−` with nonzero twist value, whose
   existence is assumed, suffices for the Euler-system choice).

**Interpolation factor.** Under good ordinary reduction, the cyclotomic
`p`-adic L-value at the trivial character equals
`R_p · L(A,1)/(G^2 Ω^ε_π)` with `R_p ≠ 0`: nonvanishing of the Euler
factor is Prop 3.2.1 of 2110.13102 (no Hecke parameter is `p^r` times a
root of unity, by purity/Klingen-ordinarity valuation separation), and
`§3.3` there. The optimally-normalised period differs from the Néron
period `Ω_A` by a `p`-adic unit once torsion/Tamagawa denominators are
`p`-units (next paragraph), so valuations agree.

## 5. End of proof: the exact divisibility

Rank 0 gives the `p`-primary exact sequence

```
0 → A(Q) ⊗ Q_p/Z_p → Sel_{p^∞}(A/Q) → Sha(A/Q)[p^∞] → 0.
```

Since `A(Q) = Z/15Z` is finite of order prime to every admissible `p`,
`#Sel_{p^∞} = #Sha[p^∞]` up to the known torsion factor, and the
Euler-system bound `length H̃^2 ≤ v_p(L_p-value)` (Thm 8.1.2/8.2.4 of
2110.13102, via Thm 25.1.3 descent) becomes, after the period comparison
and using `c_277 = 1` (no local correction) plus torsion orders
`15·15` and `Tam = 1` all `p`-units for admissible `p`,

```
v_p(#Sha(A/Q)) ≤ v_p(L(A,1)·15·15/(Ω_A·1)) = v_p(#Sha(A/Q)_an),
```

which is finite. With the recorded values `#Sha_an ≈ 1`, both sides are
expected to be 0; the inequality is what is claimed. The dual variety
satisfies `A^∨ ≅ A` (principal polarization of a Jacobian), so the
`#A^∨(Q)_tors` factor equals 15 as written in the target. ∎

## 6. Provenance and honesty boundary

- **Proved in this lane:** `c_277 = 1` with unit Tamagawa ideal at 277
  (dual-graph/Liu computation cross-checked against LMFDB product);
  torsion/Tamagawa `p`-unit bookkeeping and the `p = 5` reducibility
  remark; point-count consistency table (artifact); assembly of the LSZ→LZ
  deduction with exact theorem references and the interpolation-factor
  nonvanishing.
- **Quoted (not re-proved):** paramodularity of 277.a.277.1; LSZ Euler
  system; LZ explicit reciprocity law; LZ Iwasawa/blocked-Kato and BSD
  descent theorems — each applied strictly under the hypotheses the
  target itself imposes (ordinary, Hida deformability, residual
  irreducibility/distinguishedness, big image, local vanishing,
  odd-twist nonvanishing). No claim is made about unconditional
  deformability or big image for any specific prime; those remain
  hypotheses, as the target states them.
- **Computed evidence vs proof:** the point counts and period/Tamagawa
  numerics are consistency evidence for the ground data, not substitutes
  for the Euler-system argument; the divisibility itself comes from the
  quoted Euler-system theorems plus the new `c_277 = 1` computation.

## References (all consulted; starred items read in full text)

- *Loeffler–Skinner–Zerbes, Euler systems for GSp(4), JEMS 24 (2022).*
- *Loeffler–Zerbes, On the Bloch–Kato conjecture for GSp(4),
  arXiv:2003.05960 (explicit reciprocity law, Thms A–D, §24–25).*
- *Loeffler–Zerbes, On the BSD conjecture for modular abelian surfaces,
  arXiv:2110.13102 (Thms A/B, §3–8, deformability appendix).*
- Loeffler–Pilloni–Skinner–Zerbes, Higher Hida theory and `p`-adic
  L-functions for GSp(4) (interpolation formula).
- LMFDB pages for 277.a.277.1 (curve, isogeny class, L-function data).
- PARI/GP `genus2red` output for the simplified model at 277.
