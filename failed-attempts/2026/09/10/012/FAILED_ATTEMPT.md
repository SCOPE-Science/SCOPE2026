# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** One Stein-cork twist exoticity decision via Seiberg-Witten adjunction with logged Kirby slides
- **Round:** 2026-09-07-first-light-01
- **Lane:** 522
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Topology
- **Method:** Stein handle-calculus Kirby-diagram tracking with Seiberg-Witten adjunction and involution-extension obstruction

## Problem

Fix one explicit contractible Mazur-type Stein cork (W_2, tau): one dotted 1-handle plus one 0-framed 2-handle in the Yasui Stein family at the smallest parameter lacking a logged decision, with tau the dot-zero-swap boundary involution. Fix one explicit embedding W_2 subset X_2 into a closed simply connected symplectic 4-manifold X_2 with b2+ > 1 and known Seiberg-Witten basic class K0 (rational-elliptic E(1)-type region), and let X'_2 be the cork twist along (W_2, tau). Decide whether X_2 and X'_2 form an exotic pair via a Seiberg-Witten adjunction-inequality transfer across logged Kirby slides, or localize failure to an explicit embedded surface / involution-extension obstruction.

## Attempted claim

The named closed simply connected pair (X_2, X'_2) obtained by twisting the explicit Stein-cork embedding W_2 subset X_2 along tau is homeomorphic (same intersection form, Freedman) but not diffeomorphic: the transferred Seiberg-Witten basic-class pairing <K,[alpha]> evaluated on an explicit surface class [alpha] carried through the logged Kirby slide sequence satisfies the adjunction bound 2g-2 >= |<K,[alpha]>| + [alpha]^2 on X_2 and violates it for the minimal-genus representative on X'_2 (exact integers recorded), certifying exoticity.

## Research outcome

Decided one named closed simply connected Stein-cork twist pair (X_2,X'_2) via logged Kirby slides + H2 transfer T=[1] + SW/Stein adjunction integers (10>=10 HOLD vs -2>=10 FAIL, margin -12; VERIFY_OK 17/17): homeomorphic by explicit cork homeomorphism, not diffeomorphic either orientation by transported square-0 sphere vs SW-nonvanishing.

## Why this attempt failed

Failed axes: correctness.

correctness: Integer/logic layer replays: verify_target.py gives VERIFY_OK 17/17 (Def 5.6 with m0=0,t0=-1,r0=0,g0=0,p=(3,6); g=6,sq=0; c1=2*6-2=10; lines 10>=10 HOLD vs -2>=10 FAIL). Arithmetic is correct. Headline topological claim (closed simply connected X2,X2' homeomorphic but not diffeomorphic either orientation) is NOT proved. Essential gaps: (a) No fixed symplectic b2+>1 minimal cap C_cap is constructed (no diagram, no b2+/signature/minimality/simply-connected computation). Thm 3.6 of [AY] (Lisca-Matic/Akbulut-Ozbagci) gives some embedding of a compact Stein into some closed symplectic, not a fixed cap closing both S+ and S- with identity extension and H2(S)->H2(closed) injectivity. Thm 5.16(4) -2-meridian closure is a different object depending on Stein presentation, not shown to equal S+\cup C_cap / S-\cup C_cap simultaneously. Hence SW(X2)!=0 (Taubes), b2+>1 no-chamber, minimality, and [S']!=0 persistence are assumed, not established. (b) Closed pairing transport |<K',alpha'>|=10 via T=[1] is asserted without proof. Lemma 5.14 concerns c1 of compact Stein piece, not restriction of closed SW basic class K; no lemma shows K|_S equals maximized c1 or that transported coordinates carry a basic class with same pairing. The X2' FAIL line therefore begs the question. Class-free sphere-vs-SW argument inherits (a)+(b). (c) Sphere S' existence/essentialness: cited Lemma 5.13(2) concerns X_{-1}^(n), not the cork-twist S-; band-sum/clasp genus and interior push-in with square preserved plus -2-dual injectivity are not verified for this closure. (d) Homeomorphism h extended by id over cap assumes h|_Y=id. Prop 4.5(3) gives abstract pair homeomorphisms from cork twist, not rel-boundary identity on Y=∂S; C2 interior does not imply this. (e) All handle lemmas (Props 4.2/4.3/4.5, Lemmas 5.13/5.14/5.15, Lemma 4.4 Gluck step, Def 4.6 tb/r=2/1,0/1) are proved in [AY] for W1-mods. Application to W2 2-twist clasp via Def 4.1-generalized + Remark 5.19(2) is a remark, not a proof; tb/r shifts, Prop 4.7 increments, Lemma 5.14 value 10, and Fig.4 12-band genus count are W1-specific. Verifier conservative Delta=1,2 lines assume the correction lies in {0,1,2} without derivation. (f) Either-orientation claim has no closed intersection-form / b2+(-X) / SW-conjugation analysis; Thm 5.16(2)(ii) is a compact-Steinish adjunction statement, not a closed-SW statement. Net: proof vs evidence separation is honest that gauge/topology is CITED, but citations do not entail the closed claims. Machine replay checks only integers, not topology.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Integer/logic layer is machine-replayed; gauge/topological package cited per audit plan, not re-proved: Witten SW setup, Taubes SW!=0 for closed minimal symplectic b2+>1, closed SW adjunction (sq>=0), Stein adjunction incl. g=0, Freedman/contractible-cork extension, Akbulut-Yasui handle lemmas (Props 4.2/4.3/4.5, Lemmas 5.13/5.14/5.15, Thms 3.6/5.16), Gompf c1=r/tb-1, Gluck step in Lemma 4.4. Closure cap existence + H2-injectivity via -2-duals as in Thm 5.16(4) proof. No chamber issue (b2+>1 st…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
