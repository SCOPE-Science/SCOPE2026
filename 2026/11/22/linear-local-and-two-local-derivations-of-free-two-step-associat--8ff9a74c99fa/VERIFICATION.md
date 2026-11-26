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

The square ideal W=V tensor V is invariant under derivations by Leibniz on products, and annihilates the algebra. Therefore the V-to-V block A and arbitrary shear F determine the W action rho(A), and conversely these maps satisfy Leibniz. Injectivity of rho follows by applying it to e_i tensor e_i, reading off the off-diagonals and then dividing the diagonal coefficient by two. Locality keeps W invariant. For its W-block C, the tested image of u tensor v lies in V tensor v + u tensor V. Coefficients of e_i tensor (e_j+e_l) imply the first-factor off-diagonal coefficients are independent of the second index, and the transposed comparison does the same for the second factor. After subtracting these tensor-sum actions, the four-entry test on (e_i+e_h) tensor (e_j+e_l) forces additive diagonal coefficients d_ij=alpha_i+beta_j. Thus C=A_0 tensor I + I tensor B_0; flip symmetry on u tensor u forces (A_0-B_0)u proportional to u for every u, hence scalar by basis sums. Division by two gives the unique common parameter S. At nonzero v an arbitrary shear can prescribe its value at v and correct any difference on z, so A and S are truly independent for one-point locality. The two-point argument is valid because D^{-1}(T-S) is skew-symmetric when (T-S)D+D(T-S)^T=0, and e_i and e_i+e_j with diagonal signs 1 and -1 eliminate every mismatch entry over any field of characteristic not two. A shorter independent check of the same rigidity uses the pair v,v^2: the shared derivation enforces rho(S-A)(v tensor v)=0. Testing v=e_i forces (S-A)e_i=0 from the off-diagonal tensor coefficients and twice the diagonal coefficient. Counting free blocks gives the stated dimensions and defect. These arguments do not require an infinite field or a rank beyond the stated m>=2.

## originality

PASS

The distinctive result is the pointwise evaluation hull of the ordered tensor-square action and the corresponding exact local derivation classification. The ordinary normal form is prior, and the two-local collapse is a substantive contrast with the Lie case but follows efficiently once the local classification is known (the pair v,v^2 suffices). Neither a same-algebra idempotent census nor the associative filiform classification establishes the local hull for this multiplication.

## value

PASS

The cube-zero free associative algebra is a natural benchmark outside the commonly treated one-generated filiform families. The classification explains which parameters can vary independently under one-point interpolation and why that freedom disappears at two points. It gives a complete all-rank invariant, with a meaningful difference from the exterior-square Lie model, rather than a finite-field sample or an ordinary-derivation recount.

The dated certificate retains the supplied scientific assessment, sources and limitations.
