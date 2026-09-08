# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Attainable-size spectra of complete arcs in PG(2,5) and PG(2,7) by projective-canonical backtracking, with certified maximal witnesses in PG(2,8) and PG(2,9)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 68
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Finite Geometry
- **Method:** projective-equivalence canonical reduction with collinearity-conflict backtracking and incidence-matrix replay

## Problem

Determine the exact attainable-size spectrum S(q)={k: there exists a complete k-arc in PG(2,q)} for q=5 (31 points) and q=7 (57 points) by exhaustive collinearity-conflict backtracking with PGL(3,q)-canonical reduction, delivering for each k in S(q) one coordinate representative and a machine-checkable completeness proof (every exterior point on a secant) and for each k not in S(q) an exhaustive non-extendability certificate; and construct explicit maximal complete-arc witnesses in PG(2,8) (73 points, 10-point hyperoval) and PG(2,9) (91 points, 10-point oval) with homogeneous coordinates over GF(8)=GF(2)[t]/(t^3+t+1) and GF(9)=GF(3)[t]/(t^2+1), stabilizer order in PGL(3,q), full secant-type distribution, and a blocking-set separation example, all replayable from emitted incidence matrices by a short verifier.

## Attempted claim

Exact spectrum tables S(5) and S(7) with one PGL(3,q)-inequivalent coordinate representative per attainable k, each verified complete and each gap certified incomplete by exhaustive search; plus maximal witnesses: a 10-point hyperoval in PG(2,8) (conic plus nucleus) and a 10-point conic oval in PG(2,9), each with explicit homogeneous coordinates, stabilizer order, complete secant-type distribution (numbers of 0-,1-,2-secants summing to q^2+q+1 lines), and a blocking-set separation instance distinguishing the arc's secant cover from a chosen blocking set; all claims replayable from incidence matrices by verify.py.

## Research outcome

Certified attainable-size spectra of complete arcs in PG(2,5) ({6}) and PG(2,7) ({6,8}) with coordinate representatives, secant/stabilizer data and gap certificates, plus maximal 10-point hyperoval (q=8) and oval (q=9) witnesses with stabilizer orders, secant distributions and blocking-set separation; all replayable by two independent stdlib scripts with verify.py passing in ~3 s.

## Why this attempt failed

Failed axes: originality, value.

originality: All mathematical content is classical/textbook. S(5)={6} and S(7)={6,8}, conic/hyperoval/oval existence via XZ=Y^2 plus nucleus, Segre bounds q+1/q+2, stabilizers PGL(2,q) (120,336,504,720) and secant types (C(k,2) 2-secants, 0 tangents for hyperoval, k tangents for odd oval) are standard finite-geometry folklore (Segre 1955; Hirschfeld PGFF tables; standard group actions). Nearest retrieved priors confirm the space is covered: Davydov et al. arXiv:1004.2817 (small complete arcs, t2 bounds), Bartoli et al. arXiv:1404.0469 (FOP/lexiarc tables for all q<=321007 including q=5,7), Coolsaet-Sticker doi:10.1002/jcd.20211 (exhaustive complete-arc classification method, q=23,25) and Coolsaet PG(2,31) classification — same method family at disjoint orders. DRAFT Limitations explicitly admits 'S(5),S(7) overlap textbook knowledge; novel contribution is replayable certificate bundle, not a new bound.' A replay bundle/re-implementation does not create priority. Blocking-set separation is trivial: T is subset of union of 3 lines with disjoint T-parts after removing vertices; any 10-set in T has >=4 points on one part by pigeonhole (3*3=9<10), hence 3 collinear, so 'T contains no 10-arc' needs no 6215/19019-node DFS and distinguishes nothing. Frame-containing counts (10/116 sets, 40/5 complete) are coordinate-dependent, not isomorphism classification (draft admits orbit-fusion not logged). No substantively new object, bound, construction, or method vs priors. value: Explicit reject categories apply even though correct. (1) Textbook restatement: spectra, hyperoval/oval witnesses, stabilizer orders, secant distributions are all forced classical facts; DRAFT concedes this. (2) Mere parameter substitution / tiny enumeration: exhaustive search over 31- and 57-point planes with standard frame-fixing + collinearity pruning is routine brute force at trivial scale (~2s, 10/116 sets); no new technique, and per-size representatives without orbit classification are unexplained enumeration. (3) Unmotivated/zero gain: triangle-T-no-10-arc is pigeonhole-trivial (see originality) and does not tie arcs to blocking sets in a useful way; secant/stabilizer numbers add no decision relevant to codes beyond standard tables. No independent researcher would need to find this later instead of consulting Hirschfeld/Segre tables or standard PGL(2,q) facts. Certificate bundle (two scripts, CSVs) is good reproducibility practice but does not make a known table independently worth publishing as a new result under SCOPE value bar.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Small-order spectra overlap textbook knowledge; novelty is the replayable certificate bundle, not a new bound. PGL-orbit uniqueness fully fused only implicitly for q=5; q=7 per-size reps are orbit witnesses without separate fusion log. Maximality for q=8,9 rests on classical Segre bounds (completeness itself is machine-checked). Verifier trusts CSV index alignment but re-derives all incidence.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
