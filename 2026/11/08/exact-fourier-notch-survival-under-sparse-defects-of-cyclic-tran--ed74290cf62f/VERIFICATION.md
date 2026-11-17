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

PASS: A primitive p^t root annihilates an integer coefficient polynomial of degree <p^t precisely if its p coefficients in each length-p cyclotomic fiber agree, by divisibility by Phi_{p^t}. For t>b an untouched residue class (guaranteed 2r<p^b) has one occupied point in its high-order fiber, excluding zero. For t<=b the original complete-residue transversal Fourier sum vanishes, and the changed signed sum vanishes only when the A,B multiplicities agree modulo p^t: with r<p no nonzero constant signed difference across a full p-cycle is possible. Such t form initial depths 0..V, giving the exact zero set at indices a*h with p^(b-V)|h and p^V-1 zeros. Residue-matching equivalence, single-relocation sharp attainable depths, lost notches, and r=p counterexample follow directly. Independently classified Fourier zeros for all 92 permitted single-relocation configurations at (p,k,b)=(3,3,2),(5,2,1) and all 756 two-relocation A,B pairs for (3,3,2) by coefficient-fiber arithmetic; no infinite claim rests on these cases.

## originality

PASS

PASS with material modest-increment risk. The prime-power cyclotomic coefficient criterion and group-ring kernel are classical, and general recent Gabor block-equivalence and cyclotomic divisibility sources may decide each instance. None inspected states the uniform, lift-independent complete Fourier-zero set of a residue transversal after <p moves into distinct occupied residue classes, the exact optimal p-adic matching depth, and the sharp r=p breakdown. The cutoffs and all-depth enumeration form a motivated family theorem rather than a fixed single polynomial test.

## value

PASS

PASS: complete-residue transversals are natural cyclic sampling supports with p^b-1 spectral notches. The theorem precisely quantifies fault robustness under count-preserving but residue-misregistered positions, using an intrinsic congruence-matching invariant; it gives an optimal destroyed-notch lower bound, all attainable single-fault profiles, and a sharp threshold counterexample. This is a structural finite Fourier classification potentially useful beyond the numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
