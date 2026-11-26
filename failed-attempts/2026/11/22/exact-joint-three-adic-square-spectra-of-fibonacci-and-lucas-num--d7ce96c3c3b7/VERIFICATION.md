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

The Fibonacci state determines M^n, so any common period must be a matrix period. M^4≡−I mod 3, and M^8=I+3A with A nonzero mod 3. For d≥1, binomial terms of degree m≥2 have valuation at least v_3(d)+m−v_3(m)≥v_3(d)+2, proving the exact lift of the matrix order. On the four singular branches the relevant entry or trace of M^j A is respectively 1,2,1,2 mod 3, so dividing the difference by 3 leaves exactly v_3(t−u). Each normalized map therefore permutes the residues at every precision. For k≥2 a square divisible by 3 is a multiple of 9, and after removing this factor its square residue is taken modulo 3^(k−2), including zero. The four branches thus each contribute B_k; the j=1 branch contributes T_k to the joint count, and the singular additions there are j=2,4. The two marginal counts are 3T_k+2B_k, giving the four cells. At k=1 zero is included and B_1=1. For the infinite claim, the h-th nonzero singular square cylinder is one class modulo 3^(2h+2). For a prefix of length X choose the first tail index H with 3^(2H+1)>X. All h≥H and the zero belong to one class modulo 3^(2H+1), so at most one index is counted there; the expected nonzero tail count is bounded. The earlier classes cost at most one unit of discrepancy each. This makes the cutoff argument precise when a first omitted cylinder has modulus >X but its containing ball might not. Summing the geometric measures gives 1/8 on each singular branch, hence the stated densities and covariance −9/1024.

## originality

FAIL

The exact table is not stated in the strongest earlier paper, but it is mechanically implied by the branch-lifting assertion of Bundschuh–Bundschuh (2011), Lemma 3.5, and the indexed residue classes in the proof of Lemma 3.6. Lemma 3.5 retains the index alignment omitted by the marginal frequency statements. Every ternary lift stays in its same mod-8 branch and runs through all three next output digits. The singular Fibonacci branches are allowed by its n≠2 mod 4 condition, and the singular Lucas branches by n≠0 mod 4. Induction separately on each branch gives a bijection onto the multiples of 3. Because no branch has two singular coordinates, neither the finite joint count nor its limiting pattern requires any further simultaneous lift. The square counts, covariance, and logarithmic prefix estimate follow by standard unit-square counting and nested residue-cylinder counting.

## value

FAIL

The aligned local-square spectrum is a natural statistic and the self-contained matrix proof and covariance make it easy to use. But for these two sequences at three, the singular branches never compete at the same index, and the evaluated law and standard cylinder discrepancy use only the already covered one-branch bijections. There is no independently useful unknown exact invariant beyond that mechanical specialization in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
