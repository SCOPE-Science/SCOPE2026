---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For K_m m<=3, direct bond component-size distribution for tagged vertex: at m=3, sizes 1,2,3 with probabilities (1-p)^2,2p(1-p)^2,3p^2-2p^3. If each component is seeded independently with rate s, F_m=m[1-E(1-s)^K]; for m=2 F2=2s(1+(1-s)p). Subtract split 2F2 from concentrated F1+F3 to get p*s*(1-s)[2+6p-6p²-p*s(9-6p)] (p*s term is p times s). For p<=2/3 bracket positive, for p>2/3 exactly one s*=(2+6p-6p²)/(9p-6p²), monotonically decreasing 1 to 2/3. For two-person household gap F2-2F1=2ps(1-s)>0. Independent SymPy checked full polynomial and threshold derivative, matching rational witness at p=s=.9. Proof is exact for all 0<p,s<1 and does not require simulation.

## originality

FAIL

FAIL: a Nov 2 previously published theorem explicitly gives exactly the same two K3 households, 2 vaccine allocation options, exact expected case polynomial, threshold p=2/3, s*(p), and minimal household size. Its directed Reed–Frost contact mechanism differs from static undirected bonds generally, but their tagged ancestor/component-size distributions and therefore EXPECTED infections are exactly identical for up to three unvaccinated people. The earlier theorem also proves a stronger general-size high-seeding expansion; original source commit precedes current assigned source by six days.

## value

FAIL

FAIL as submitted: the complete finding is a recompilation of earlier exact small-household expected-cases boundary, without a new invariant, corrected error, structural extension, or distinct practical mathematical question. Correct reproduction and a bond interpretation alone do not generate independent scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
