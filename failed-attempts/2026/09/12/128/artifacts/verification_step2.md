# Verification note for DRAFT §4 Step 2 (auditor repair)

Scope: exact theorem numbers + hypothesis checklist for the
preprojective-invariance step. No scope change, no new direction.

## (i) Minamoto–Mori [MM11] (Adv. Math. 226 (2011), 4061–4095;
DOI 10.1016/j.aim.2010.11.004; verified via Crossref/OpenAlex and the
Shizuoka repository copy hdl:10297/5853, whose PDF text was extracted
with pdftotext and searched)
- Prop. 4.4: Ext^q(E,E) = 0 (q ≥ 1) for the Beilinson object
  E = A ⊕ A(1) ⊕ … ⊕ A(ℓ−1). With ℓ = 3 this is the tilting
  vanishing used in §1. Confirmed in extracted text
  ("Since E compactly generates D(Tails A) and we have Ext^q_A(E,E)
  = 0 for q ≥ 1 by Proposition 4.4").
- Lemma 4.11: B(D(Tails A), E, (ℓ)) ≅ A^[ℓ] (quasi-Veronese) and
  End(E) ≅ ∇A (Def. 4.7: r = |ℓ|, ∇A = degree-0 part of A^[r]).
- Thm 4.12(1)(2)(3)(4): (1) ∇A quasi-Fano dim n−1; (2) ν(A^[ℓ]) ≅ Π(∇A)
  as graded algebras (ν = generalized Nakayama; twist explicit);
  (3) GrMod A ≃ GrMod Π(∇A); (4) D(Tails A) ≃ D(Mod ∇A) via
  RHom(E,−) (Keller [8, Thm 4.3] cited there). Confirmed in text.
- Thm 4.14: graded right coherence of A ⇔ ∇A extremely Fano, and then
  Db(tails A) ≃ Db(mod ∇A). Covers the Noetherian (hence coherent)
  generic Sklyanin case. Thm 4.16 is the dim-2 coherence model.
- Coverage of generic Type A Sklyanin over alg.-closed char-0 k with
  infinite-order translation: S is connected N-graded over R = k
  (semisimple base), AS-regular dim 3, Gorenstein parameter ℓ = 3,
  Noetherian domain, balanced dualizing complex, Hilbert series
  1/(1−t)^3. Infinite-order σ is not a hypothesis of Thm 4.12; it only
  secures the generic point-module picture and infinite-order ν.
  Hence Thm 4.12 applies on the whole generic Type A locus, giving
  ∇S quasi-Fano dim 2 (= 2-RI in [HIO14] sense), dim_k = 15,
  gldim 2, and ν(S^[3]) ≅ Π_3(∇S) graded. The twist ν (≈ σ^3) is
  retained, not dropped.

## (ii) Keller [Kel09] (arXiv:0908.3499; verified live: title page
"Deformed Calabi-Yau completions", abstract states compatibility with
derived equivalences and localizations; contents list §§4–6 with
Prop. 4.2, Thm 4.6, Thm 4.8, Thm 5.8, §§6.7–6.9) + [HIO14]
(Adv. Math. 252 (2014), 292–342; verified via OpenAlex:
title/authors/biblio) + Rickard standardness
- Exact statements used: Keller Prop. 4.2 (A ↦ Π_n(A) equivariant under
  derived Morita equivalences), Thm 4.6 (localizations), Thm 4.8 (Π_n
  is n-CY as bimodule), Thm 5.8 (deformed), §§6.7–6.9 (3-CY completion
  of gldim-≤2 algebra quasi-isomorphic to Ginzburg dg algebra;
  H^0 = classical preprojective).
- Checklist for B = ∇S, B′ = ∇S′:
  (a) Smoothness + Noetherian: finite-dim, gldim 2 ⇒ homologically
      smooth + proper; as dg algebras in degree 0 satisfy Keller's
      cofibrant-over-field hypotheses.
  (b) Twisted vs untwisted: S twisted 3-CY (Nakayama ν ∼ σ^3); B twisted
      2-CY/quasi-Fano with (ω, σ = ν^[3]|_B); Keller's Π_3(B) untwisted
      3-CY dg; [MM11] identifies it with ν-twisted S^[3]. No untwisted
      Π_3(B) ≅ S claim is made.
  (c) dg concentration degree 0: θ = shifted inverse dualizing cofibrant
      bimodule; Π_3(B) = T_B(θ) Adams-graded; H^0 classical.
  (d) Rickard standardness: Db(mod B) ≃ Db(mod B′) between finite-dim
      algebras over alg.-closed k is −⊗^L_B T for a two-sided tilting
      complex (Rickard JLMS 1989; JPAA 1991 Thm 3.3) ⇒ lifts to derived
      Morita equivalence of dg enhancements ⇒ Keller Prop. 4.2 applies.
  (e) Graded H^0 iso: undeformed (c = 0) Morita-induced map preserves
      Adams grading (Keller §§4–5) ⇒ graded dg quasi-isomorphism ⇒
      graded H^0 iso; Adams degree ↔ Veronese degree via [MM11] (4-7).

## (iii) Graded isomorphism derived explicitly
Db(qgr S) ≃ Db(qgr S′) → (Step 1) Db(mod B) ≃ Db(mod B′) → (Rickard,
standard tilting bimodule) Keller Prop. 4.2 ⇒ graded dg
quasi-isomorphism Π_3^dg(B) ≃ Π_3^dg(B′) → (graded H^0) classical
preprojectives ν(S^[3]) ≅ ν′(S′^[3]) graded (via [MM11] Thm 4.12(2))
→ (Serre-functor commutation, Bondal–Kapranov: Nakayama data
correspond) ν/ν′-twisted graded iso S^[3] ≅ S′^[3] → (untwist by Zhang
twist along ν, i.e. along σ^3, which stays in the ATV triple class)
twisted graded identification of S, S′. Twist tracked, not hidden.

## (iv) ATV recovery retained with precise reference
[ATV90] Artin–Tate–Van den Bergh, "Some algebras associated to
automorphisms of elliptic curves", Grothendieck Festschrift I,
Birkhäuser 1990, + "Modules over regular algebras of dimension 3":
geometric quadratic dim-3 AS-regular ⇔ triple (E, σ, L); graded iso
⇔ triple iso (Zhang twists accounted). Gives (E,σ,L) ≅ (E′,σ′,L′),
hence pair iso; ±1 only weakens (inversion already triple
automorphism per §2 lemma).

## What was checked mechanically vs by citation
- Mechanically (check_beilinson.py, ALL CHECKS PASSED): Hilbert series,
  dim B = 15, Ext-vanishing range, Euler numbers, Hesse j variation,
  t_p ↔ t_{−p} conjugacy via ι.
- By exact citation (this note + DRAFT bibliography): tilting/generation
  framework, 2-RI/preprojective recovery, CY-completion invariance,
  standardness, ATV triple step. Not re-proved; applied in stated scope.
