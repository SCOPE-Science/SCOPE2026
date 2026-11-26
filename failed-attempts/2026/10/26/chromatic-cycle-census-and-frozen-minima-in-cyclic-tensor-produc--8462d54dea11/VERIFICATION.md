---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Under the stated adjacency, two or more selected colors force both neighboring fibers to be empty and hence force the original fiber to be full by domination. Singleton runs are monochromatic of length ≥2. A singleton's omitted colors are dominated by a neighbor whose selected singleton is the same color as the singleton in the original fiber, not the omitted color. An empty fiber has a full neighbor or two unequal singleton neighbors. Charging the latter type to the next singleton run is injective, giving e≤2f+s/2, hence |S|≥2k+(q−2)f. A periodic two-singleton/one-empty pattern with cyclically proper colors exists for k≥2 and q≥3. At equality f=0, there are k isolated empty fibers with 2k singleton fibers between them, so every run has length two. The three labeled residues give the trace count using eigenvalues q−1 and −1; k=2 counts ordered pairs of distinct colors. Different residues change at least k vertices from each set and changing any one run color changes both of its vertices, proving the two-removal and two-insertion bound. The supplied checker was read, not executed. Independent replay `python3 /workspace/audit_replay.py 3` exhausts actual vertex subsets up through size 2k for (k,q)=(2,3),(2,4),(3,3), obtains 18,36,18 minima, and checks exact configuration and all pairwise symmetric differences. The proof, not the replay, covers all stated k,q.

## originality

FAIL

A distinct indexed result, e9f31746918a, gives every minimum configuration and its exact labeled multiplicity for all n≥6 and q≥3 in precisely the same product. Its specialization n=3k gives the exact structure and count, and the two-removal and two-insertion bound then follows directly from that same structure. This is present coverage, not a finding that the distinct record preceded the frozen one.

## value

FAIL

The full labeled classification is a natural structural question, but relative to the available all-length result this exact slice and its trace count are parameter substitutions. The frozen reconfiguration conclusion uses only the immediate pairwise difference of the already classified configurations, so it does not leave an independent exact invariant or structural gap under the review standard. This is not a mathematical error or a claim about the merit of the broader classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
