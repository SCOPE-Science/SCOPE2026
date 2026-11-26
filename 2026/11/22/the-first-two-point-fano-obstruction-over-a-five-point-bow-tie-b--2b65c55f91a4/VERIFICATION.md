---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A free amalgam introduces no mixed triples across the two exclusive sides; a Fano copy cannot straddle them because every pair of Fano vertices is in a line. The Fraïssé extension property realizes every legal finite diagram over the individually named base, and homogeneity identifies diagrams with complete ordered injective pair types. Free copies give infinitely many realizations. With up to four old points and two new points, or five old points and one new point, there are fewer than seven vertices, hence no restriction. With five old and two new points every Fano copy spans them; deleting the two new points removes 3+3-1=5 distinct lines, leaving two lines meeting in one old point. Conversely that bow tie extends, so on named sets the 15 bow ties are all minimal obstructions and form one isomorphism type. For exactly those two old lines, the line through their common vertex and the two new points is forced. The four other new lines must use opposite arms, with each arm vertex seeing each new point once. They are precisely the two alternating colorings of a 2x2 array. The two five-bit completion requirements intersect in exactly the central mutual bit (their union uses nine bits); after fixing it on, the four-bit requirements are disjoint and their union uses eight bits. This verifies the intended count despite the informal word 'overlap' in the conditional proof. The valid-diagram count is 2^25-2*2^20+2^16=31522816. Given the five mutual bits, the link count is 2^12 times 256 when the center bit is off and 225 when on, independent of the four other bits. Thus K is the sum of an independent Binomial(4,1/2) and Bernoulli(225/481). Its total variation from Binomial(5,1/2) is |225/481-1/2|*max_k binom(4,k)/16=93/7696 by telescoping the variation of the unimodal four-bit mass. An independent exact relabelling enumeration from the binary projective plane gives 30 designs, 15 old restrictions each with two completions, and the critical-bit counts 256 and 225. Replay: python3 /workspace/reproduce_reviews.py 1.

## originality

PASS

The supported contribution is the first ordered-pair obstruction with its exact conditioned type and mutual-link distributions. General free amalgamation, the seven-point Fano plane, and its 30 relabellings are known. Neither the available global reliability count nor the inspected one-point or tetrahedron-free analogues give the conditioned law. The strongest possible stronger overlap would be a multivariate Fano reliability specialization, not a global scalar probability.

## value

PASS

Five is not an arbitrary truncation: it is exactly the earliest base size where two-point restrictions can coexist with completely unrestricted one-point extensions. A single minimal old-edge configuration explains the onset, together with the sharp and nonobvious localization of the mutual-link bias to just one bit while the others remain fair and independent. The value is that structural boundary and law, not the standalone count of known Fano relabellings or the arithmetic for total variation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
