---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Eliminate y to get tame Kummer z^9=F=x(x+1)(x^2+x+1)^3 with ramification multiplicities 1,1,3,3,8 and different 8+8+6+6+8=36, so genus10. At finite branch points and infinity, the ten listed x^a H^floor(i/3) z^-i dx are holomorphic, independent by Kummer character/degree, and form a complete basis. The separating parameter x and char-two decomposition G=U^2+xV^2 give Cartier(G z^-2s dx)=z^-s sqrt(G')dx; explicit polynomial images yield 6 distinct first images, 3 second images, none third. Independent GF(2) polynomial and rank computation reproduced the ten images (index map [-1,0,5,6,-1,7,9,-1,1,-1]) and ranks 10/6/3/0. Over F2 the semilinear matrix iterates as ordinary GF2 matrix.

## originality

PASS

The October 2026 closely related Almeida Filho–Tafazolian–Vieira preprint studies a-numbers of characteristic-two covers including GK and reports a-number 4/first Cartier rank 6 in Proposition 6.1 per cited prior work. The exact second-iterate rank and nilpotent block type are a stricter invariant not implied merely by rank 6. Its primary full text was inaccessible in this run (arxiv HTML and PDF disabled, lawful OA unavailable, authorized Oxford VPN disconnected); treat possibility of broader result as a material priority risk, not an invented noncoverage conclusion.

## value

PASS

The first GK curve is a canonical maximal curve; the intermediate nilpotent Cartier filtration is a natural exact invariant of its Jacobian differential structure, finer than the known a-number and relevant to Ekedahl–Oort phenomena. The claim does not pretend to classify the entire curve family or p-divisible group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
