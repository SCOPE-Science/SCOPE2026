# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Distal cell-bound transfer to henselian fields via one explicit RV-adapted Wilkie preparation step
- **Round:** 2026-09-07-first-light-01
- **Lane:** 663
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Mathematical Logic
- **Method:** valued-field cell decomposition with Ax-Kochen-Ershov RV analysis and NIP-distal transfer

## Problem

Fix one two-sorted henselian theory T = Th(RCVF, L_RV) in equicharacteristic 0 with residue sort admitting restricted-exp Wilkie preparation and Presburger/DOAG value group. Isolate one Wilkie-type preparation normal form for exponential-polynomial RV-terms of degree <=2 and prove the fiberwise distal cell counts on residue and value-group sorts imply an explicit distal cell bound for valued-field formulas phi(x;y) with |x|=2, |y|=1 of RV-complexity <=2.

## Attempted claim

In T = Th(RCVF, L_RV) henselian of residue characteristic zero, every valued-field formula phi(x;y) with |x|=2, |y|=1 built from at most two exponential-polynomial RV-terms of total degree <=2 admits a distal cell decomposition with at most N=48 cells and distal exponent at most 2*(d_k+1), where d_k is the o-minimal distal exponent of the corresponding residue-field fiber, via the stated RV-adapted Wilkie preparation normal form.

## Research outcome

Proved TARGET transfer lemma: explicit RV-adapted Wilkie normal form NF2 for degree<=2/<=2-term formulas yields 8 residue cells x 6 value-group cells = 48 VF distal cells with exponent <=2*(d_k+1); all numbers certified by verify_transfer.py (VERIFY_OK). Original bookkeeping (2-cell grouping, 6-sector count, product assembly); standard theorems cited.

## Why this attempt failed

Failed axes: correctness.

correctness: Arithmetic certificates re-ran VERIFY_OK (2x4=8, 2m=6 sectors, 8x6=48, d_k+2<=2(d_k+1)), but they verify only arithmetic from displayed formulas, not the model-theoretic inferences. Essential inferences fail or are unproved: (1) Lemma 1 2-cell grouping: C_unbdd={|R|>K} is R>K \/ R<-K, a disjunction, not a conjunction of two literals as claimed for cells; the uniform sign rule H=m_inf*u_inf*(1+eps) uses direction-dependent factorization (dominant monomial differs for E->+inf vs E->-inf / c>0 vs c<0); proof does not distinguish realized cells per parameter B from potential formulas, and invokes restricted-exp Wilkie preparation for total exp-polynomial H with unbounded argument where restricted exp is undefined (restricted vs total exp mismatch; topic assumes restricted-exp but unbounded asymptotics need total exp). (2) Lemma 2 <=8: assumes any RV-definable D_k reduces to at most two degree<=2 polynomial signs (sign(H) plus jointly F1,F2). Arbitrary D_k from Pas QE rv(F) in D can be any residue-definable set of unbounded complexity (high-degree P unrelated to F); term bound on VF-terms does not bound D_k. Jointly needing signs of F1,F2,H is three conditions (2^3=8 patterns), not two. Zero absorption {x_i=0}/{H=0} via < vs >= costs no cells unproved: v=oo outside DOAG, rv undefined at 0, pullback covers VF^x only. Sign-vector = distal cell (not crossed) not shown. (3) Lemma 3 <=6: assumes Gamma-condition reduces to three concurrent forms L1,L2,L1-L2 through common point with quadrant count 2+1+2+1=6. Arbitrary D_Gamma in DOAG is arbitrary Boolean combination of many linear inequalities, unbounded by VF-term count; concurrency through common point and exhaustiveness not derived. Exponent t_Gamma<=2 via Anderson 2|x|-2 cited but Anderson induction hypothesis (k parameters for |x|=1) not verified for RV maps. (4) Combination: Pas QE gives Boolean combination of rv(H) in D=D_k x D_Gamma; product K_k*K_Gamma assumes single atom. Number of atoms/Boolean connectives unbounded by term count; intersecting decompositions for distinct H (F1,F2,F1-F2) multiplies cells, ignored by 'up to Boolean structure single H' claim. Preimage/product preservation (Chernikov-Simon) for xi o rv / gamma o rv with rv-sections/centers: global definable sections do not exist without choice; parameter absorption unproved. Exponent addition d_k+t_Gamma assumed without verifying subadditivity hypotheses for this fibration. Hence headline N=48 / exponent transfer not proved; proof vs computation not distinguished (script proves arithmetic only).

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: ['Bounded-complexity lemma only (|x|=2,|y|=1, <=2 terms, degree<=2); not a general transfer theorem.', 'Residue sort assumed restricted-exp o-minimal (Wilkie applies); mixed char and unrestricted exp excluded.', 'd_k taken as input exponent of residue fiber, not computed.', '48 is an upper bound with known slack (single-difference case gives 24); sharpness not claimed.', 'Heavy inputs (preparation existence, Pas QE, distal preimage/product, Anderson caps) cited, not re-derived; original part is…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
