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

Parity forces the lowest digit to be 1 for 2k+1 and allows 0 or 2 for 2k, giving the two stated recurrences and the seed (t,1). The adjacent evaluations follow the stated transitions for every positive index by halving. In the fifth-cyclotomic quotient the coefficients relative to the fifth bucket determine the spread, since the only relation among the five basis powers is their sum. I independently constructed the orbit in a five-integer array representation modulo all-ones, with cyclic rotation for multiplication by t and subtraction of the minimum for normalization. `python3 /workspace/independent_replay.py hyperbinary` checks the 120 exact states against the frozen table, both successors of each, histogram (10,100,10), and 31 distinct first coordinates. Binary-index induction, not a bounded run over indices, proves the full bound. At m=0 the zero expansion is the only one; direct digit enumeration at m=10 gives lengths 2,3,3,4,5 and residue counts (1,0,1,2,1). I separately checked the all-fence transfer without relying on access to the cited corollary: binary digits b_i and hyperbinary digits e_i are linked by e_i+c_i=b_i+2c_{i+1}, with 0/1 carries and boundary carries zero. For b_i=0 the allowed interior carry relation is c_i≤c_{i+1}, and for b_i=1 it is c_i≥c_{i+1}. The length equals the binary popcount plus the number of nonzero carries. Choose an even binary word with leading 1 and trailing 0: both boundary inequalities are automatic, and the internal bits realize any prescribed path of order-ideal membership inequalities. Thus every oriented path occurs (possibly using a dual orientation convention), and the resulting monomial shift, or shift plus exponent reversal in the cited correspondence, preserves spread. The empty fence has one ideal. Digits 1010 yield the three-vertex fence with two minima below a common maximum and ideal counts (1,2,1,1,0), attaining spread two.

## originality

PASS

The distinct claim is the exact uniform spread at most two for all five length residues and its sharp all-fence counterpart, with an explicit exact orbit. The fence/length correspondence and the underlying prospect of finite fifth-root evaluations are not credited as new. In particular, a substantial identified prior group-finiteness theorem already explains existence of a finite specialized orbit, but its available statement neither calculates the normalized coefficient spread nor gives sharpness or the 120-state histogram. Prior statements about modulus three, modular Stern values, and zeros of q-rational denominators are not equivalent to the sharp mod-five length claim. The strongest matching Resultary scientific summary is the frozen record itself.

## value

PASS

The natural length-refined count, not just the Stern total, has an exact uniform bound across all indices. The sharp spread quantifies a gap that group finiteness alone leaves open and gives the same constraint for every rank distribution of an arbitrarily oriented fence. The explicit exact orbit provides a short reusable certificate for the unbounded family, and m=10 is a genuine extremizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
