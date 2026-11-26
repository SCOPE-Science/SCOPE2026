---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a fixed word the product of the three sign indicators is eight times its indicator on the admissible set, and lies between zero and four at each of at most five omitted parameters. The two monic quadratic single sums equal -1 (count solutions to (t-y)(t+y)=±1) and the linear single sum is zero. All composite polynomials are squarefree in odd characteristic: their indicated factors have disjoint roots, and t^4-1 has nonzero derivative at its roots. The two cubics have one point at infinity in genus one; t^4-1 has two rational points at infinity in genus one, so its sum has absolute value <=2sqrt(p)+1. The degree-five 2t(t^4-1) has genus two and one rational point at infinity. This gives 8N_p>=p-23-10sqrt(p), which is positive at 149 and increasing thereafter. The remaining primes were exhausted independently, not by executing the frozen checker. Replay: sieve 0 through 148, discard prime 2, and for each remaining prime form a boolean table marking x² mod p for x=1..p-1. For all t=0..p-1, form the three residues (t²+p-1,2t,t²+1) mod p; skip a zero and store the sign word from the table. This visits 2125 t over 33 primes. In lexicographic order the six words are --+, -+-, -++, +--, +-+, ++-. Missing: all six for 3 and 5; words 1,3,5 for 7; 2,3,4,5 for 13; 3,5,6 for 17; 1,6 for 29. The first witnesses at 31 are 21,4,2,6,3,8 respectively. The analytic and finite ranges cover every odd prime, and failure at 29 makes 31 the first prime from which all subsequent primes work. This confirms the claim in RESULT.md lines 5–18 and 26–57, independently of the frozen checker and recorded output.

## originality

FAIL

On the best available evidence, Li–Wang's previously published two exact monochromatic counts for this normalized family already determine the six mixed counts by elementary parameter symmetries, not merely by a conjectural further Jacobi-sum calculation. The publisher-deposited abstract explicitly confirms exact counts for both monochromatic cases over odd primes, and the frozen record (line 65, reporting its reading of the opening page) identifies their parameter as this exact normalized family. The article cites the database entry A344620 for the same polynomials; that entry itself has an extra height restriction and is not the coverage relied on. The metadata render the formulas as placeholders, so the parameter match is based on the frozen opening-page report together with the publisher evidence, not an independent reading of the inaccessible article text. The decisive overlap is the explicit reconstruction below; a merely inaccessible article or a shared title was not treated as a reason to fail.

## value

FAIL

The normalized six-word threshold is a natural and interpretable sharp statistic, and the supplied proof of it is sound. On the available prior-coverage evidence, however, this exact statistic is obtained by elementary reconstruction from the earlier same-family exact monochromatic counts, followed by a bounded zero check. The checked special cases and effective Hasse–Weil bound make that computation explicit but do not establish an independently unknown exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
