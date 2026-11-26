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

The energy and every labeled degeneracy are correct. A direct check is to set h=d−r/2 and write H/J = e_h(s_0)+e_h(s_1)+(r/2) Σ_i(s_{0,i}+s_{1,i})², where e_h(x)=Σ_i x_i x_{i+1}+h Σ_i x_i² is the single-cycle energy. The lower bound twice the ring minimum is attained by (x,−x) for each ring minimizer x; positivity of r forces exactly that form in all ground states. For one partly occupied nonempty ring with q spins, each occupied path costs at least one missing bond relative to −q; the bound e_h≥1+(h−1)q is attained by a single alternating block. For h<1 the best partial block has q=n−1 and for h≥1 all partial blocks lose to empty. Full occupancy has bond energy −n on even rings and −n+2 on odd rings, with precisely the two alternating words or the 2n single-defect words, respectively. For odd n the n−1 branch is attained by precisely the 2n alternating paths with one vacancy; comparing with the full and empty branches gives h=0 and h=(n−2)/(n−1), including n=3 and both coexistences. For even n partial blocks never beat the full or empty minimum; h=1 has only those three states. Doubling energies and counting the bijection, not multiplying independent degeneracies, gives exactly all the stated thresholds and counts. A fresh direct integer/rational enumeration of all prism configurations checked the complete ground sets against separately enumerated single-ring ground sets at 48 parameter instances, including small positive r=1/1000 and all size-specific boundaries for n=3,4,5.

## originality

FAIL

The earlier Resultary spin-one wheel result a9d59ac1a17e contains the decisive exact single-cycle data in its proof, not merely a matching phase name. Fix its hub spin t=0. Its even-rim zero-cost criterion and its odd-rim occupancy bounds B≥1−q and B≥−n+2, with alternating-path and single-defect witnesses, already give the entire required ring lower envelope and its relevant equality states. The prism Hamiltonian is two copies of that very ring problem at h=d−r/2 plus the nonnegative rung square (r/2)Σ(s_0+s_1)². The bound is always attained by antipodal copies of any ring minimizer, and strict positivity of r excludes all other copies. Thus the claimed locking, thresholds, width, and degeneracies are consequences of those earlier exact bounds and a local square completion. The census is true, but the frozen statement is covered as a direct consequence; no separate surviving distinct claim was established.

## value

FAIL

The finite-size benchmark is well motivated, and the formulas may be useful as a check. But in the frozen scope every reported datum is mechanically carried over from the previously proved fixed-zero-hub single-ring sector by an elementary square and antipodal copying. The theorem does not test frustration locking when the rung lower bound cannot be saturated simultaneously, nor supply a distinct invariant. The exact degeneracies alone cannot salvage value as a new result under the narrow-invariant standard. No repair is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
