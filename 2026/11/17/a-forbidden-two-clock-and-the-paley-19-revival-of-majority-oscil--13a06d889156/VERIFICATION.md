---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For a proposed tournament period-two pair x,y, summing strict voting inequalities over changed 1-to-0 set A and 0-to-1 set B yields e(A,B)+e(B,A)-e(A,A)-e(B,B)>=|A|+|B|, but tournament arc counts make the left side (|A|+|B|-(|A|-|B|)^2)/2, impossible. For a regular tournament each class in a mixed fixed state would require at least 2ceil(k/2)+1 vertices, exceeding 2k+1 in total. The special Paley prime cases are finite, explicitly all 2^3+2^7+2^11+2^19=526472 labelled states. Separately written Python functional-graph enumeration from quadratic-residue adjacency recovered orbit counts p3 {1:2,3:2}, p7 {1:2,7:6}, p11 {1:2}, p19 {1:2,4:342,19:18}, and sharp entry depths 0,3,5,7. Independently generated affine-square/complement/temporal group orbit closures at p19 give exactly the four classes (0,period1,size2), (511,period19,size342), (3543,period4,size684), (5751,period4,size684). The finite exhaustive verification is not extrapolated to other primes.

## originality

PASS

General voting/threshold-dynamics papers and Paley tournament spectral/combinatorial studies do not give this exact p=19 attraction, primitive-period and symmetry classification. The universal no-two-cycle lemma is elementary structural context, not separately relied on as a nontrivial novelty claim. Jørgensen defines the Paley construction, while Benjamini et al. require undirected networks for their period-two restriction, hence cannot cover these oriented orbits. Goles 1985 is a plausible general threshold-automata precursor; full text was inaccessible through authorized access, so priority remains qualified.

## value

PASS

The first canonical doubly-regular tournament sizes yield a complete exact recurrent/entry/symmetry classification, with all-consensus p=11 followed by period-four and period-nineteen oscillators at p=19. The finite cutoff and symmetry collapse are natural complete invariants, not isolated numerical experiments; no all-prime conjecture is presented as proved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
