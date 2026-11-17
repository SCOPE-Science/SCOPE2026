---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For q,k>=2 and n=kq+1 the cyclic-gap inequality for the distance power C_n^{q-1} gives alpha=k. In a maximum independent k-set the k cyclic steps are q except one q+1, so the complete list is I_j={j,j+q,...,j+(k-1)q} and contains n distinct sets. Since gcd(q,n)=1, the step-q cyclic relabelling sends these to all length-k intervals. Their hitting sets are exactly the subsets with positive cyclic gaps <=k. Rooted circular gap counting gives H_{q,k}(z)=sum_{t=q+1}^n (n/t)[u^n](u+...+u^k)^t z^t. The min t=q+1 case has deficits summing k-1, hence coefficient n/(q+1)*binom(k+q-1,q). Boundaries q=k=2 and all t up to n are covered. Independent brute-subset enumeration and a separately written bounded-composition count agreed on five (q,k) pairs, including (2,3,7) with 14 minimum transversals and (3,3,10) with 25. These finite tests corroborate but do not prove universal quantifiers.

## originality

PASS

The exact full maximum-stable-set hypergraph of one-defect cycle distance powers is transported to the circular interval transversal hypergraph, yielding the all-size enumeration and sharp minimum count. The cyclic-gap enumeration itself is classical and receives no standalone priority credit. Published dense cyclic-block transversal work applies in a special long-block regime and to domination of cycle powers; it does not give this uniform maximum-independent-set transversal formula. General hitting maximum independent sets results supply bounds not the exact size distribution. A same-statement derivation hidden in older cycle-power or circulant literature remains a risk.

## value

PASS

The first order n=kq+1 departing from perfect q-spaced packing has exactly one surplus gap, making a natural structural boundary. Its complete labelled minimum-maximal-independent-set hitting polynomial is an independently useful invariant of cycle-power graphs, beyond an arbitrary numerical slice. It gives all hitting-set sizes and sharp extremal multiplicities, not only a known chromatic or independence number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
