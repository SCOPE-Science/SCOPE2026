---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independently re-derived Rudin–Shapiro recursion r(2q)=r(q), r(2q+1)=r(q) xor (q mod2) and the eight-state maps T0,T1. Verified all states are reachable and the 4-step child transition matrix is positive, giving uniform state frequencies. Exhausted 8*16=128 state-residue cases for every n=1..16, reproducing exactly the 36 listed palindromes, their per-word multiplicities 64,32,16,4,8,4,2,2,2,1,1 and zero at lengths 9,11,13,15,16. Every longer palindrome contains central 15/16 palindrome, hence excluded. Pair density 1/128, so every listed density and position rule follow for infinitely many starts. A finite 32768-start sample was slightly nonuniform (n=1: 16512 versus 16256), as expected for a prefix and not contrary to the limiting density theorem.

## originality

PASS

PASS best of knowledge. The 2001 Allouche–Baake–Cassaigne–Damanik paper gives palindrome-length cutoff; Schaeffer–Shallit determine maximal palindromic words; the earlier cyclic-prefix published Resultary paper lists the same 36-word language. None of those inspected source statements provides all per-factor limiting starting-position densities or the eight-state exact starting-position rule, and mere knowledge of factor existence cannot imply the frequency of occurrence. Older inaccessible 1997 source remains a bounded priority risk.

## value

PASS

PASS. The uniform density across every palindromic word at a fixed length is a nontrivial quantitative structure of a canonical automatic sequence; the explicit 128-case rule supplies natural exact occurrence measures and positions, useful beyond mere language complexity or known length cutoffs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
