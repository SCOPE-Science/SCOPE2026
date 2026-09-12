# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Insertion-automaton growth separation of Av(1342,1423) versus Av(1342,1432)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1073
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Permutation Pattern Theory
- **Method:** insertion-encoding regular-language automata with transfer-matrix growth analysis

## Problem

Decide whether the sibling 1342-type classes Av(1342,1423) and Av(1342,1432) have distinct Stanley-Wilf growth rates by constructing their insertion-encoding automata and proving disjoint transfer-matrix spectral-radius enclosures.

## Attempted claim

The Stanley-Wilf growth rate of Av(1342,1423) is strictly smaller than that of Av(1342,1432), certified by regular insertion-encoding DFAs whose transfer-matrix spectral radii admit disjoint rigorous interval enclosures proving gr(Av(1342,1423)) < gr(Av(1342,1432)).

## Research outcome

Certified Wilf-collapse pocket: Av(1342,1423) and Av(1342,1432) coincide exactly through n=14 with balanced differences and matching profiles.

## Why this attempt failed

Failed axes: originality, value.

originality: Originality FAIL. EMERGENT_FINDING genuinely arose from target work on the same pair (deeper census after blocked separation), not a convenient replacement, so route is legitimate — but the headline is not new. ADMISSION_DEFECT: Admission claimed no database/theorem covers Av(1342,1423) vs Av(1342,1432), yet Kremer (2000) via Homberger Ch.9 proves Av(1342,1423) is counted by the large Schröder numbers with gf (1-x-sqrt(1-6x+x^2))/2, and the public TileScope/PermPAL record (June 2019) explicitly lists BOTH Av(1342,1432) and Av(1342,1423) among 2x4 classes enumerated by the Schröder numbers, with PermPAL claiming all 56 two-pattern length-4 classes have specifications. Same Schröder gf implies identical counts for ALL n, so coincidence to n=14, balanced differences (|A\B|=|B\A| follows automatically from equal finite totals), and routine witnesses are a recomputation/certificate of a known stronger infinite enumeration, not a new boundary. A timestamp or failed OEIS literal-title search does not establish priority. value: Value FAIL under the shared STANDARD with no preset presumption for EMERGENT_FINDING. The object pair was motivated, but the invariant (exact counts to n=14: 1,1,2,6,22,90,394,1806,8558,41586,206098,1037718,5293446,27297738,142078746) is already known and mechanically implied: termwise it equals the large Schröder sequence OEIS A006318 (verified: submitted[n]=A006318[n-1] for n>=1, b-file to n=2000 contains 142078746 and beyond). This is known-database recomputation / arbitrary finite slice of a known infinite enumeration, explicitly rejected by the STANDARD. Certification (dual engines, witnesses, symmetry check) strengthens evidence but does not create value by itself, and no new general theorem, boundary, redirect, or downstream use survives once Schröder coverage is recognized — the redirect was already available from Kremer/TileScope.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Growth-rate equality gr(Av(1342,1423)) = gr(Av(1342,1432)) is conjectured but not proved: coincidence through n=14 does not logically determine Stanley-Wilf limits, and no bijection, generating function, or DFA enclosure certificate is exhibited. The n=11..14 counts rest on the single OpenMP engine (cross-validated by the independent engine only to n=10) plus detector unit validation. Wilf-equivalence for all n remains an open conjecture with several natural bijections refuted.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
