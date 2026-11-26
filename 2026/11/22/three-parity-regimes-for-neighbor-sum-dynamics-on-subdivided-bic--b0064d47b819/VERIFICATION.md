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

Write F=[[0,B],[B^t,0]], W=im B the zero-total subspace and ker B^t the constant line. The Q=BB^t formula acts by the shore degree parities plus the opposite shore sum. For even/even it has constant-shore image of dimension 2 and squares to zero; for odd/odd the zero-sum subspace on each odd shore is fixed and the two constants carry J2(0); for mixed, writing the even-shore coordinates as x and the odd shore as a constant plus its zero-sum subspace, Q vanishes on the latter and acts on (x,c) as (x+c1,sum x), with characteristic polynomial t(t-1)^e. In the last case im Q misses the global constant line and Q|W has rank e. The L=B^tB ranks follow by restricting B^t to W. The resulting F^k ranks for k=1,2,3,4 are (2(m+n-1),m+n,2,0), (2(m+n-1),2(m+n)-3,2(m+n-2),2(m+n-2)), and (2(e+o-1),2e+o-1,2e,2e). The third ranks use im Q|W and the quotient of im Q by the global constants; the fourth follow from Q^2,L^2. The block determinant gives only the two stated primaries, with unit dimensions 0,2(m+n-2),2e. As a check on unit block sizes, each nonzero Jordan block J_k(1) of Q gives one J_{2k}(1) of F: on the unit primary B^t identifies the two halves and the action is (x,y) -> (Qy,x); if x cyclic for Q, (x,0) gives a cyclic vector for F with annihilator (t^2-1)^k. For mixed parity Q on its image (u,sum u) acts in the u-coordinate as I+1 sum, a rank-one nilpotent perturbation with square zero, yielding one size-four F block. Successive differences of zero-primary ranks give the frozen zero blocks. Counting kernels of powers on the zero primary and fixed spaces of the appropriate powers on the unit primary gives every entry and period census, with full independent fibers of size q^b; an orbit of length j thus has j such fibers. Checked the smallest even and mixed shores, including zero multiplicities at e=2. No finite-size extrapolation was used.

## originality

PASS

Credit the known incidence mechanism, even/even extinction index (obtained by combining previous results), and generic orbit counting. The complete Jordan multiplicities on the fixed once-subdivided biclique adjacency, in particular the mixed unit block of size four together with the three zero-primary profiles, remain a distinct family-specific calculation in the evidence inspected.

## value

PASS

For this natural incidence graph family, parity of the shore sizes decides whether all signals die, synchronize in two steps on the recurrent space, or admit genuine period four, while the Jordan multiplicities give sharp transient and period populations without a state-space search. The full classification, not a single extinction time or the generic conversion from blocks to counts, supplies the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
