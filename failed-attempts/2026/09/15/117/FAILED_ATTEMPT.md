# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Floor-diagram correspondence for rational plane descendants with one psi^k line insertion
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20349
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Tropical Geometry
- **Method:** floor diagrams and tropical intersection theory

## Problem

Let Delta_d=conv{(0,0),(d,0),(0,d)} and n=3d-1-k. Let I^{log}_{d,k} be the genus-0 degree-d descendant log Gromov-Witten invariant of P^2 with n point insertions and one psi^k insertion coupled to a line L, and <psi^k L>_d its Blomme-Markwig tropical counterpart with multiplicity |det(u,v)| prod_V m_V. Construct an explicit marked/psi-floor-diagram count F_{d,k} of degree d with one distinguished L-vertex of codegree k, and prove via floor decomposition and tropical intersection theory that F_{d,k} = <psi^k L>_d = I^{log}_{d,k} for all d>=1, 0<=k<=3d-1.

## Attempted claim

Let Delta_d=conv{(0,0),(d,0),(0,d)} and n=3d-1-k. Let I^{log}_{d,k} be the genus-0 degree-d descendant log Gromov-Witten invariant of P^2 with n point insertions and one psi^k insertion coupled to a line L, and <psi^k L>_d its Blomme-Markwig tropical counterpart with multiplicity |det(u,v)| prod_V m_V. Construct an explicit marked/psi-floor-diagram count F_{d,k} of degree d with one distinguished L-vertex of codegree k, and prove via floor decomposition and tropical intersection theory that F_{d,k} = <psi^k L>_d = I^{log}_{d,k} for all d>=1, 0<=k<=3d-1.

## Research outcome

Constructed explicit marked psi-floor diagrams and proved F_{d,k}=tropical=log for all d,k via floor decomposition plus published log-tropical correspondence, with computational verification for d<=3.

## Why this attempt failed

Failed axes: correctness, value.

correctness: TARGET route: Theorem 1.1 claims F_{d,k}=<psi^k L>_d=I^{log}_{d,k} via Lemma 4.1 weight |det|*C(val+k-1,k) and floor stretching. Lemma 4.1 is false: Blomme-Markwig Prop 3.14 multiplicity is |det|*prod m_V with tropical psi-weight 1 for one marking, no binomial; |det|=1 after floor normalization is false (BM conic has det 2, mult 2*2/2=2). Stretching with n=3d-1-k points does not force floor decomposition. Numerically refuted: reran psi_enum2.py reproducing F=(6,32,858) for (d,k)=(1,1),(2,1),(3,1) vs BM hpsiL=(2,4,60), and F=147 vs 29 for (2,2). Hence F=tropical fails; tropical=log leg is only quoted, not proved. value: A correct floor diagram for non-stationary psi-L would be valuable (BM gap), but submitted F is incorrect per above numerical contradiction, so no reliable exact invariant survives. The k=0 case F_{d,0}=d*N_d is a trivial d-fold copy of classical N_d, mechanically implied. The k>=1 tables are wrong-weight enumerations with no independent interpretation; integrality/finiteness certification alone does not create value under STANDARD.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: The tropical=log step assembles published correspondence theorems (Mandel-Ruddat genus-0 descendant correspondence; Blomme-Markwig local psi-line multiplicity) rather than re-proving the degeneration analysis; toric transversality for the stretched configuration is sketched. Lemma 4.1 local weight follows published local computations. Machine verification covers d<=3 for psi counts (d=4 classical only) due to exponential cost; the general-d argument is combinatorial.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
