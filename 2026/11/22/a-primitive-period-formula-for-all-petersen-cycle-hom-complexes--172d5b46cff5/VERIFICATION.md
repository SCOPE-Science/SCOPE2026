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

# Verification instructions and scope

Run `python3 verify.py` from this directory using Python 3 and no third-party dependencies. It constructs the Petersen graph from two-element subsets of a five-element set, the 30-state nonbacktracking transition relation, exact trace counts and Möbius inversion, then independently enumerates and recolors *every* cyclic graph-homomorphism for \(3\le n\le12\). The complete component-size and reduced-length distributions are compared with the formula; actual standard output is in `verification_output.txt`.

The source length twelve test contains 547,830 maps, 3,360 isolated rigid vertices, 364 circular components and one null sector. The 264 circles of cyclically reduced length ten include both 240 primitive ten-cycle instances with the two parity lifts and 24 twice-wound primitive pentagons with just one parity orbit. This is a direct check of the critical parity correction.

The checker does not calculate homotopy from cell boundaries, nor prove the formula for unbounded lengths. The mathematical proof depends on a tree-lift normal-form argument and the published universal-cover contractibility theorem of Matsushita (https://arxiv.org/abs/2412.19144), and square-free-target component theorem of Fujii--Kimura--Nozaki (https://arxiv.org/abs/2412.19039). No independent audit has been performed.
