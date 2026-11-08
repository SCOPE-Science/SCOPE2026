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

# Verification of the conservation moment hierarchy

The algebraic proof is equations (1)–(4) of RESULT.md: every protected-leaf gain is a sum of joint extinction probabilities of descendant clades; the two perturbations annihilate all factorial moments through degree \(n-2\), leave the \(n\)-th extinction probability fixed, and shift the \((n-1)\)-way probability by exactly \(2\varepsilon/n\). The length-one clade isolates this shift in a single protection-vs-protection comparison. Uniqueness follows by continuity and a sufficiently small strictly positive branch length.

Run `python3 check.py` from the extracted package using Python 3.8 or later, without third-party packages. It constructs fully supported exchangeable laws for each integer \(n=3,\dots,10\) and verifies the corresponding factorial moment identities with exact `Fraction` values. For the four-taxon example it enumerates **all sixteen extinct subsets**, computes expected intervention gains from the actual rooted-PD survivor set definition, and independently computes them by descendant-edge joint-extinction events. The rational outputs agree and verify both different unique optimizers. This finite replay is not the infinite proof; equations (1)–(4) cover all \(n\ge3\).

Independent external validation was not performed.
