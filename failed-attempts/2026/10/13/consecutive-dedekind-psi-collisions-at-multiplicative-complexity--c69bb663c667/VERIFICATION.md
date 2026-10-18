---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The factorization types with Ω≤2 are 1, primes, prime squares p², and distinct-prime semiprimes pq. The identities ψ(p)=p+1, ψ(p²)=p²+p, ψ(pq)=(p+1)(q+1) prove primes on the left impossible; the only prime-square/prime orientation is (4,5). Mixed prime-square/semiprime orientations are excluded by product-versus-sum inequalities. The squarefree semiprime pairs obey (q-2)(s-2)=3 when the even member is first and =-3 when it is second, yielding exactly (14,15). Independent direct low-Ω enumeration through n=120000 reproduced n=4,14. The proof exhausts Ω≤2 without relying on a finite search.

## originality

FAIL

FAIL for this final claim as an independently original mathematical contribution. Published Resultary 2026-10-04 "Unique two-almost-prime solution of the Erdős–Sierpiński equation" proves for the identical Ω(n),Ω(n+1)≤2 condition that σ(n)=σ(n+1) has only n=14, by exactly the same squarefree semiprime parity factorization (q-2)(r-2)=3 or -3. Because ψ=σ for squarefree integers, it covers the only mathematically substantive squarefree/semiprime case. The sole additional ψ-specific collision ψ(4)=ψ(5)=6 and the elementary exclusion of prime-square orientations follow immediately from textbook ψ(p^a) formulas, and both n=4,14 are in OEIS A291043. The earlier sigma theorem is not asserted alone to imply ψ for nonsquarefree inputs: the correct implication is published sigma classification PLUS elementary low-Ω ψ identities, yielding all claims. This is prior-implication-plus-routine-deduction coverage, not a mere unsuccessful novelty search.

## value

FAIL

FAIL. The full two-almost-prime squarefree branch and unique nontrivial semiprime collision were already settled by the published σ classification under the exact same Ω bound, and the only difference is the single trivial ψ prime-square collision (4,5) already listed in OEIS. The mixed branches are direct one-line AM–GM or factor-count inequalities, so the submitted theorem supplies neither a substantively new invariant nor an independently useful nontrivial classification beyond known work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
