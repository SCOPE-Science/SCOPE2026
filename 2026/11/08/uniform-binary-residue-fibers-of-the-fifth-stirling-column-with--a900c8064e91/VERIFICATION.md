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

Inclusion-exclusion yields 120S(n,5)=5^n+10*3^n+5-5*4^n-10*2^n, and splitting n=r+2t gives G_r(t)=(5^r25^t+10*3^r9^t+5)/120 plus error -(2^(2n-3)+2^(n-2))/3 of valuation n-2 for n>=5. For s!=t in Z_2, the 25^h-1 and 9^h-1 lifting identities give v2=3+v2(h); their two terms in the difference 120(G_r(t)-G_r(s)) have valuations 3+v2(h) and 4+v2(h), so division by v2(120)=3 yields v2(G_r(t)-G_r(s))=v2(t-s) without possible cancellation. Finite quotients therefore permute every residue separately on each parity. For n>=k+2 the correction vanishes mod2^k and each period 2^(k+1) visits all half-indices modulo 2^k once per parity. Mod-2 pattern (1,1,0,0) excludes odd eventual shifts, and isometry forces all even eventual shifts divisible by 2^(k+1). At n=k+1 for k>=4, the period fails because the correction difference has valuation k-1, proving sharp onset; for k<=3 earliest allowable n=5. Independently generated the Stirling triangle and verified exact balanced parity fibers and onset for k=1..7 and three offset blocks. The all-precision theorem rests on the 2-adic proof, not the checks.

## originality

PASS

The minimum eventual period length is known from Kwong 1989 and is acknowledged. The closest full primary research on fifth-column Stirling numbers describes 2-adic valuations and congruence classes, not all output residues and unique parity preimages. Periodicity and valuation strata alone do not force uniform unit residues; the new full 2-adic isometry and sharp preperiod are a distinct complete fiber result, subject to historical search limitations.

## value

PASS

Complete residue distribution and earliest periodic onset for a natural fixed Stirling column are meaningful arithmetic invariants beyond previously known period lengths and valuations. The fifth column is the first with uniform full binary residue support, and the explicit 2-adic isometry is a structural explanation rather than a finite counting curiosity. A future researcher can use its exact one-per-parity fiber counts and cutoff when studying Stirling congruences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
