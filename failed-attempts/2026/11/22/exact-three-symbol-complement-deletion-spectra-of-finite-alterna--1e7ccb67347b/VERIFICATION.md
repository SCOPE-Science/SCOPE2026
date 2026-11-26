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

Independently proved the table without extrapolation or executing the frozen scripts. A residual fixes the parity of every deletion gap (initial, between surviving letters, and terminal) because the host alternates and both endpoints are prescribed. For the empty residual there is just one odd gap. Three deletions therefore give either three odd gaps, all singletons, or one odd gap. With three odd gaps the embedding is unique, and counting isolated deletion positions reduces to three nonnegative slack variables: the first position starts at 1+u1, the minimal successive distances are 2+[u1≠u2] and 2+[u2≠u3], and the last allowable position is the largest index of parity carrying u3. Increments come in twos. With one odd gap q (number of retained letters before it), the base pattern is the bit b=q mod 2. The extra pair can be in q (giving b,1−b,b), in an earlier gap j<q (giving j mod 2, its opposite, b), or in a later gap j>q (giving b, (j+1) mod 2, its opposite). Count distinct q, not the positions of the extra pair. In order 000,001,010,011,100,101,110,111 the one-odd-gap counts are (0,n−1,n−1,n−1,n−2,n−1,n−2,0) on E_n and (0,n−1,n,n−1,n−1,n−1,n−1,0) on O_n. Adding the isolated counts gives the stated 16 polynomials via Pascal, including O_1 and E_2. Multiplying the resulting binomial series by (1−z)^4 gives the frozen numerators, and subtracting the indicated rows gives the unit gaps. The frozen interleaving DFA and Cayley–Hamilton certificate also correctly distinguish residuals from embeddings.

## originality

FAIL

The distinct same-day Resultary records 4b5c91af95ea and 762092a60cc7 jointly cover the cardinality classification via forced endpoints, bit complement, reversal, and elementary one-letter-position counting. This is demonstrated mathematical coverage, not a claim that publication order or authorship can be inferred from the date. The generating functions and unit gaps follow mechanically from the covered cardinalities. No independent all-pattern mathematical remainder remains within the Finding.

## value

FAIL

Order-sensitive residual cardinalities are a natural statistic and the table can be handy as a reference. As a proposed distinct finding, however, all entries and both gap identities mechanically follow from the stronger exact spectra and elementary bijections. The frozen claim does not establish a substantive new invariant or general deletion method to repair around.

The dated certificate retains the supplied scientific assessment, sources and limitations.
