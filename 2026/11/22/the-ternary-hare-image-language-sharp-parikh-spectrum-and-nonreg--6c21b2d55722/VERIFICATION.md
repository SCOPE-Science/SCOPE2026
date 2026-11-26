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

Each maximum 2 separates binary input blocks; the hare recursion concatenates their sorted images and appends all twos. Conversely every descent 10 needs a separator in such a factorization, and cutting exactly at the descents and padding by empty blocks realizes any permitted prefix, also when the prefix is empty or c=0. The positive internal runs and optional endpoint runs give precisely binom(a,j) binom(b,j) prefixes with j descents. The maximum j=min(a,b) is realized by alternating, so the cutoff is necessary and sufficient. A deterministic debt counter with finite-state memory of the last symbol accepts at zero debt in a terminal-two phase (or zero at the end of the binary prefix); the prefixes (10)^j have pairwise distinct right quotients. Summing the three binomial-geometric series gives the stated rational functions. The cubic g(t)=1-2t+t^2-t^3 has one simple real root r in (0,1); its conjugate roots have modulus sqrt(1/r), and the additional pole at 1 is farther away. The simple-pole coefficient is -1/[r(1-r)g'(r)], agreeing with the frozen K and lambda. The independent ascending-input stack simulation (pop strictly smaller top, push on equality) exhausted lengths 0–10 and matched all support sets and Parikh counts. All-length and nonregularity assertions are proved, not extrapolated from that run.

## originality

PASS

Pass for the explicit ternary hare support, Parikh spectrum and their language-class and growth consequences. The stack map, recursive machinery, binary sorting fact, and general individual-preimage machinery are already known. The strongest related exact language results checked concern a genuinely different equal-letter convention. The paper by Chen and Luo remains an explicit access risk, not negative evidence.

## value

PASS

The first nonbinary alphabet is the first case where ordinary sorting ceases to explain the hare output space. The characterization gives a useful comparison at exactly the alphabet size where tortoise still has regular image support. It pinpoints one unbounded arithmetic obstruction while giving a sharp threshold at each content and a rational growth law despite nonregularity; this is more useful than merely re-evaluating individual fertilities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
