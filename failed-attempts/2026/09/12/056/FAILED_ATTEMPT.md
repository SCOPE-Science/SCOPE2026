# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Named quartic Tyurin K3 extension and modulus
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1184
- **Disposition:** AUDIT_2_REJECT
- **Domain:** Hodge theory of K3 Type II degenerations
- **Method:** Schmid nilpotent/SL2 asymptotics with Clemens-Schmid

## Problem

Let F1=x0*x3-x1*x2 and F2=x0^2+x1^2+x2^2+x3^2-x0*x3-x1*x2 in P^3, G=x0^4+x1^4+x2^4+x3^4, and X_t={F1*F2+t*G=0} over D*={0<|t|<epsilon} with smooth quartic K3 fibres Xt for small t!=0 degenerating to the Tyurin central fibre X0=Q1 union Q2 along the smooth elliptic curve E={F1=F2=0}, Qi={Fi=0} rational quadrics. Let Vt=H^2(Xt,Q) with its polarized weight-2 variation, monodromy T and N=log Tu. Decide by Schmid nilpotent-orbit and SL2-orbit asymptotics whether N!=0, N^2=0 of rank two, W=W(N)[2] has dim Gr^W_1=2 identified with H^1(E), dim Gr^W_2=18, dim Gr^W_3=2, and the Carlson extension class of W1 by Gr^W_2 and of Gr^W_2 by Gr^W_3 for this named (F1,F2,G) is nonsplit and recovers the modulus of E. A complete answer proves this rank, weight table and nonsplit extension or disproves it by computing T, N, W, F_lim and the extension invariant on an explicit integral basis.

## Attempted claim

Let F1=x0*x3-x1*x2 and F2=x0^2+x1^2+x2^2+x3^2-x0*x3-x1*x2 in P^3, G=x0^4+x1^4+x2^4+x3^4, and X_t={F1*F2+t*G=0} over D*={0<|t|<epsilon} with smooth quartic K3 fibres Xt for small t!=0 degenerating to the Tyurin central fibre X0=Q1 union Q2 along the smooth elliptic curve E={F1=F2=0}, Qi={Fi=0} rational quadrics. Let Vt=H^2(Xt,Q) with its polarized weight-2 variation, monodromy T and N=log Tu. Decide by Schmid nilpotent-orbit and SL2-orbit asymptotics whether N!=0, N^2=0 of rank two, W=W(N)[2] has dim Gr^W_1=2 identified with H^1(E), dim Gr^W_2=18, dim Gr^W_3=2, and the Carlson extension class of W1 by Gr^W_2 and of Gr^W_2 by Gr^W_3 for this named (F1,F2,G) is nonsplit and recovers the modulus of E. A complete answer proves this rank, weight table and nonsplit extension or disproves it by computing T, N, W, F_lim and the extension invariant on an explicit integral basis.

## Research outcome

Repaired submission: proved core (smooth K3 fibres, Tyurin fibre, 8 cA double points, Kulikov Type II weights (2,18,2), j(E)=35152/9) with N'/weights qualified to base-changed Kulikov model; both Carlson nonsplit claims honestly marked conditional after withdrawing the incorrect E^2=8 argument.

## Why this attempt failed

Failed axes: correctness, originality, value.

correctness: Re-ran exact certificates: det M1=1/16, det M2=9/16; transversality Groebner {1} in all 4 charts (lex recheck, correcting script's grlex print); smoothness of X_{1/100} Groebner {1} in all 4 charts with properness extension to small t!=0 valid; Segre identity G|Q1=(s0^4+s1^4)(t0^4+t1^4) verified (difference 0); Disc_t=-4(s^2-s+1)(s^2+s+1), 8 exact Z points with b=t^4+1=0, mult 2 each totalling 16, rank-2 gradient defect at all 8 points, no points at infinity, j=35152/9 exact (35152/9*9=35152). Computational lemmas 1-3 are correct. However the headline asserts as PROVED that after base change s^m=t the Kulikov limit satisfies N'!=0, (N')^2=0 rank two with weights (2,18,2) and Gr1=H^1(E'). Minimal m, unipotency of original T, resolved central-fibre census, resolved normal-bundle degrees and triple-point/d-semistability check are all explicitly deferred; the Type II inference is stated as plausible ('cannot create K3/abelian or S^2 without non-crepant blow-ups') and the draft invites the auditor to treat it as conditional. A proved Kulikov Type II conclusion cannot rest on a deferred census. Hence the headline overclaims: the computational core is proved but the asserted Kulikov weight theorem is not rigorously established. Correctness FAILS for the headline as stated. originality: The substantive headline content N'!=0, (N')^2=0 rank two with weight table (2,18,2) and Gr1=H^1(E) for a Tyurin (two rational surfaces along smooth elliptic) degeneration is textbook: Clemens-Schmid, Schmid nilpotent/SL2-orbit, Friedman-Scattone Type II (Invent. Math. 1986), Kulikov-Persson-Pinkham. Fused retrieval found Jones arXiv:2502.04301 (2025/2026) explicitly constructing the 'Two quadrics intersecting transversally' degree-4 Tyurin family Bl16(P1xP1) U (P1xP1) with lattice A15+A1^2, covering this geometry as a special case of an 18-dimensional family with d-semistability and period-map relations. No prior source records the exact ad hoc triple (F1,F2,G=sum xi^4) or j=35152/9, but that novelty is only an arbitrary parameter computation on a non-canonical choice, while the weight/rank claim is mechanically implied by the broader theorems. A prior source need not state the headline verbatim to cover it. Originality FAILS. value: The only fully proved new datum is j(E)=35152/9 for the arbitrarily chosen F1=x0x3-x1x2, F2=x0^2+x1^2+x2^2+x3^2-x0x3-x1x2, G=sum xi^4, plus the 8 double-point cA census and smooth-fibre check. The object and invariant were not motivated before computation by any recognized question, benchmark, classification boundary, or downstream use; they are an arbitrary parameter fact. The generic (2,18,2) weight table is a textbook restatement for any Tyurin degeneration. The potentially valuable part of the admitted TARGET — nonsplit Carlson extensions recovering the modulus of E — is explicitly WITHDRAWN as conditional/unproved, as are unipotency, minimal base-change degree, and resolved degrees. Per STANDARD, certification and replayab…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: No explicit integral T/N matrix and no F_lim period matrix; unipotency of the original pencil not proved (only N'=mN_u inheritance). Minimal Mumford base-change degree m and explicit resolved central-fibre census (exceptional components, resolved normal-bundle degrees, triple-point check) not computed. Both Carlson nonsplit-extension statements are conditional/unproved; no explicit extension-invariant computation is given. Precise references supplied for the missing verification (Friedman 1983b…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
