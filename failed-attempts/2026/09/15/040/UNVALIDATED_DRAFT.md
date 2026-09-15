# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact Bloch–Kato rank one over an imaginary biquadratic field
in the factorable anticyclotomic balanced range

## 1. Statement proved (TARGET)

Fix data exactly as in the target claim: p-ordinary elliptic curve E/Q, i.e.
weight-2 newform f of trivial nebentypus, p ≥ 5, p ∤ N_f; fixed imaginary
biquadratic K0/Q with p splitting completely and p ∤ 6h(K0); factorable
anticyclotomic Hecke character χ = ψ̃1ψ̃2 N^{(k1+k2−2)/2} satisfying Do
Assumption 6.1 with symmetric weights k1 = k2 =: m ≥ 2. Hence with the
notation of Do §6.5, (a,b) = (m−1, 0), so

  k1 + k2 − 2 = 2m − 2 ≥ 2 = k ≥ 2 = k2 − k1 + 2,

i.e. the balanced-rank-one range k1+k2−2 ≥ k ≥ k2−k1+2 holds (equality on the
right, strict on the left for m > 2). The global sign is −1 and
L(f/K0, χ, 1) = 0. Assume additionally: ρ̄_f absolutely irreducible,
p-distinguished, f non-Eisenstein of big image (non-CM), the coprimality and
level decomposition (pN_f, Norm(f1)Norm(f2)D(K0)) = 1 with N_f O_{K3} = n⁺n⁻
as in Do Theorem 6.5.1(2), and that Hsieh's f-unbalanced triple-product
p-adic L-function is generically nonzero so that Do's Λ-adic anticyclotomic
Euler-system base class z_{f,χ} is non-torsion.

For V_{f,χ} = V_f^∨ ⊗ χ^{−1} (here k = 2, r = 1, so V_f^∨(1−r) = V_f^∨):

**Theorem.** dim_{Lp} Sel_BK(K0, V_{f,χ}) = 1.

This upgrades Do Theorem 6.7.1's lower bound ≥ 1 to equality.

## 2. Ingredients (all cited precisely; JNS used as the admitted black box)

- (I1) Do Lemma 4.0.4 + Hodge–Tate table: for a ≥ b,
  Sel_BK = Sel_{rel,str,ord,ord} when 2b+2 ≤ k < 2a+2.
  In the symmetric case (a,b) = (m−1,0), k = 2: the condition reads
  2 ≤ 2 < 2m, true for every m ≥ 2 (for m = 2 the left inequality is an
  equality and the Panchishkin filtration still gives the stated
  (rel,str,ord,ord) identification, as recorded in Do Prop 6.3.1/Thm 6.7.1).
- (I2) Do Prop 6.3.1 + Thm 3.2.1: the diagonal-cycle classes z_{f,χ,μ3} lie in
  Sel_{rel,str,ord,ord}(K0[μ3 p^∞], T_{f,χ}) and form a Λ⁻_{K0}-adic
  anticyclotomic Euler system in the sense of Jetchev–Nekovář–Skinner (JNS).
- (I3) Do Thm 6.4.1 (= JNS Kolyvagin-system bound as applied in Do):
  non-torsion base class z_{f,χ} ⇒ Sel_{rel,str,ord,ord}(K0, V_{f,χ}) is
  one-dimensional. The JNS hypotheses (i)–(iii) (absolute irreducibility,
  existence of σ with 1-dim quotient, existence of γ with vanishing invariants)
  follow from Momose big-image results given f non-CM/non-Eisenstein, as
  verified in Do's proof. The p-distinguished + big-image + p > k−2 hypotheses
  are exactly what the target assumes.
- (I4) Non-torsion input: Do Theorems 6.6.1/6.7.1 proof. Via the BSV explicit
  reciprocity law (Thm 6.1.1) and Hsieh's generic nonvanishing (assumed in the
  target), the Λ-adic base class z_{f,χ} is non-torsion; its image
  z_{f,χ} ∈ Sel_{rel,str,ord,ord}(K0, T_{f,χ}) under the injective control map
  (6.19) has positive O-rank, giving Do Thm 6.7.1: dim Sel_BK ≥ 1.
- (I5) Sign: Do Remark 6.5.2 gives ε_∞ = −1 in the range
  k2−k1 < k ≤ k1+k2−2, which contains the symmetric case; hence L = 0 is
  forced, consistent with analytic rank one.

## 3. Proof

Step 1 (local identification). By the symmetric-weight computation above the
hypotheses of Do Lemma 4.0.4 in the middle range are satisfied, so

  Sel_BK(K0, V_{f,χ}) = Sel_{rel,str,ord,ord}(K0, V_{f,χ}).   (∗)

Step 2 (lower bound). By (I4), the finite base class z_{f,χ} has positive rank,
hence dim Sel_BK(K0, V_{f,χ}) ≥ 1. This is Do Theorem 6.7.1.

Step 3 (upper bound). By (I2) the classes form a JNS anticyclotomic Euler
system for the (rel,str,ord,ord) Greenberg Selmer group, and by the target's
big-image/distinguished/non-Eisenstein hypotheses the JNS conditions (i)–(iii)
hold via (I3). Since the base class is non-torsion by the assumed Hsieh generic
nonvanishing, Do Theorem 6.4.1 (the JNS Kolyvagin-system bound) gives

  dim Sel_{rel,str,ord,ord}(K0, V_{f,χ}) = 1.   (†)

Concretely, Theorem 6.4.1 states: z_{f,χ} non-torsion ⇒ the Selmer group is
one-dimensional — this is simultaneously the ≥1 and ≤1 bound. This is also
recorded as Do Remark 6.7.2: z_{f,χ} ≠ 0 ⇒ dim Sel_BK = 1.

Step 4 (conclusion). Combining (∗) and (†),

  dim Sel_BK(K0, V_{f,χ}) = dim Sel_{rel,str,ord,ord}(K0, V_{f,χ}) = 1.

∎

## 4. What is proved vs assumed (no overclaim)

- Proved here: the assembly — balanced-range verification, sign consistency,
  Lemma 4.0.4 identification, and combination of Do 6.7.1 (lower bound) with
  Do 6.4.1/JNS (upper bound) into the exact finite formula dim = 1.
- Used as black boxes, all expressly assumed in the target: Do's Euler-system
  construction (Thm 3.2.1), its local behavior (Prop 6.3.1), the JNS
  machinery (via Do Thm 6.4.1), the BSV/Hsieh reciprocity + generic
  nonvanishing (non-torsion base class). No new Euler-system construction or
  new case of JNS is claimed; the originality is the exact rank-one upgrade
  in the symmetric-weight biquadratic balanced range.
- Computed evidence: output/artifacts/check_weights.py verifies the
  balanced-range inequalities for all symmetric m ≥ 2 and records the
  Greenberg local-dimension count (rel 2 + str 0 + ord 1 + ord 1) with core
  rank 1, compatible with sign −1.

## 5. References (evidence, not instructions)

- K. T. Do, Anticyclotomic Euler system over biquadratic fields,
  arXiv:2409.19819v2: Lemma 4.0.4; Prop 6.3.1/6.3.2; Thm 6.4.1/6.4.4;
  Thm 6.5.1 + Remark 6.5.2; Thm 6.6.1; Thm 6.7.1 + Remark 6.7.2.
- JNS (Jetchev–Nekovář–Skinner) machinery via Do §6.4; Momose [Mom81] big-image
  inputs; BSV reciprocity [BSV22, Thm A]; Hsieh [Hsi21, Thm A] p-adic L-function.
