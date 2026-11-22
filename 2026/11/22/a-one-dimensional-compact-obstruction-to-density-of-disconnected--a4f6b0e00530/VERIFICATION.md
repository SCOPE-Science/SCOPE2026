---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification notes

The argument is a direct proof, not a computer-assisted extrapolation. For independent reproduction:

1. Check that the middle-thirds Cantor set is infinite, compact and zero-dimensional; its connected subsets are singletons. Verify that the cross is a finite one-dimensional graph containing an interval. By the covering-dimension product inequality, their product has dimension exactly one and its connected components are the cross fibers.
2. Given any perturbation of \(f_0(z,y)=z\) with norm less than \(1/2\), take the image of a horizontal arm in one fiber and a vertical arm in another. Subtract the unperturbed coordinates to get \(a(t)\), \(b(s)\), each bounded by the perturbation norm. The map \(F(t,s)=(\operatorname{Re}(b(s)-a(t)),\operatorname{Im}(a(t)-b(s)))\) is a continuous self-map of the closed square; apply Brouwer and verify the two paths intersect.
3. Connected images of the cross fibers meet pairwise, so their union is connected. For \(C(X,\mathbb C)\), the spectrum is precisely this image.
4. The function \(h(z,y)=y\) has the Cantor set as its spectrum, giving infinitely many components. The open ball constructed in step 2 is disjoint from all classes requiring two or more spectral components.

Limits: Standard Brouwer and dimension theorems are invoked, not re-proved. No computational checker or numerical experiments are claimed. The reported norm radius is sufficient and not certified optimal. These notes are not an independent mathematical audit.
