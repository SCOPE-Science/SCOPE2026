---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

Every cell has eight distinct neighbors; its live-neighbor count is s_j−x_{r,j}, where s_j is the total of the three adjacent columns. Checking the precise B3678/S34678 birth/survival table proves full inversion iff every s_j∈{3,6}, including all-zero/all-one columns. The sixteen pair-column-weight states with T_(a,b),(b,c)=binom(3,b)1_{a+b+c∈{3,6}} enumerate all labelled cycles via trace(T^n). Independently rebuilt this weighted matrix, all n=1..16 traces, and all 16 Newton identities: characteristic polynomial t^4(t−3)^2(t³−18)^2(t²−t−1)(t²+t+1), implying the all-n Lucas/root-of-unity formula. Independently enumerated weighted column words for n=3..8. Complement equivariance yields F²(x)=x and no binary state equals its complement; hence exact least period 2. Dominant classes each have 3^n possibilities; all remaining eigenvalues grow at most 18^(1/3)<3.

## originality

PASS

Bell 1997 explicitly introduced B3678/S34678 and sample oscillators; Eppstein 2009 gives complement symmetry and a strobing dual B01245/S0125. Therefore F(x)=~x can be viewed as a fixed state of the dual, and that alias was searched, but neither inspected primary description computes the three-row toroidal fixed-state count. Resultary search found the same self-record and unrelated Rule 150, hard-square, and other automata; their global matrices/counts do not imply this update-specific formula. Prior abstract symmetry credited, exact spectral census best-of-knowledge new.

## value

PASS

Inversion under the natural self-complementary Day & Night rule is a canonical strict subset of primitive period-two behavior, not an arbitrarily chosen toy slice. An all-circumference exact census with two matched exponential-density phases, an arithmetic mod-three resonant term and sharp entropy growth is an independently informative invariant of the width-three torus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
