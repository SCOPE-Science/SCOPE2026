---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For a chord (a,b), other chords contribute 0, 1 or 2 endpoints strictly between a and b, with 1 exactly for a crossing. Thus all degrees even is exactly opposite endpoint parity, giving a uniform n! permutation space. Each r-edge matching of the cycle forces r prescribed permutation cells, of probability (n−r)!/n!; cycle matching enumeration gives the stated binomial moments even at r=n, when two subsets contribute. The stated moment ratio after scaling by 2^r/r! follows by factor cancellation. For r≤n/2 each product deficit is at most (r−j)/n, and the prefactor is at most 2 with excess at most r/n; for r>n/2 the product bound 0≤A≤2 suffices (A=0 past support). Absolute binomial inversion is summable against 4^r/r!; the r² error weights sum to 20e^4, giving the claimed 30e^4/n. For the witness, an outside chord avoiding a connected component separates the circle into two arcs. Each chord of the component lies entirely to one side, and by crossing connectivity all lie on the same side. Hence the outside chord lies within a single gap of that component, each gap is closed, and an outside connected component occupies just one such gap. Two nonsingleton components give a closed gap and its closed complement each with at least two chords, so take the smaller. If an isolated chord is nonsimple, the two open arcs formed by deleting its endpoints are both nonempty and closed. For n≥4, if the smaller arc contains just one chord, adjoining the two endpoints of the enclosing chord gives a closed interval of two chords; otherwise take the smaller arc itself. This also handles the case of no nonsingleton component and too many nonsimple isolates. At n=2,3 there is no non-all-simple failure of the target pair relation (direct finite check). For any length 2k window, the k-by-k parity-preserving restriction has probability k!(n−k)!/n!, not the unrestricted double-factorial ratio. Union bounding and comparing k≥3 with binomial(n,3) yields O(1/n). The two all-simple cases contribute 2/n!. Outside the exceptional event, taking all chords other than the simple isolates as the unique remainder gives precisely (K,n−L)=(1+S,S), including when that remainder is a singleton. Coupling and the pushforward of the Poisson approximation give the joint TV bound; testing (1,0) gives the connectivity corollary. Frozen code and supporting evidence were inspected as text, not executed.

## originality

PASS

Pass is specific to the asymptotic joint component-count/largest-deficit law with the one-giant/simple-isolate estimate in the parity-reversing model. The model, exact connected counts, deterministic closed-block method, and Poisson approximation of the simple-chord marginal all have substantial prior coverage. In particular the latter marginal is classical restricted-position counting in the ménage problem; that overlap is stronger than the unrestricted simple-chord comparison in the frozen record and should be cited explicitly in future presentations. None of these inspected results establishes the required joint conditional component coupling with rate.

## value

PASS

The conditioning is canonical and exponentially rare, so it is not a parameter relabeling of the unrestricted model. The worthwhile output is that the global giant-component deficit and the number of other components coincide up to a shift with quantified high probability, and follow one shared Poisson(2) variable. This identifies the structure left after conditioning, rather than just recomputing classical ménage counts or reporting the known mean of adjacent chords.

The dated certificate retains the supplied scientific assessment, sources and limitations.
