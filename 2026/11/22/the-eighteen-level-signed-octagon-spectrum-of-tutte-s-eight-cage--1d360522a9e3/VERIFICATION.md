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

# Reproducibility checks

Run `python3 verify_octagons.py` using Python 3.10 or newer. The program reconstructs the graph and all 90 eight-cycles without external graph datasets or network access. It independently enumerates octagons as simple graph cycles and as four-duad quadrangles, checks girth eight and 16 occurrences of every edge, and uses spanning-tree switching to enumerate exactly 65,536 sign classes.

A direct exact character-sum implementation and a separate integer Walsh–Hadamard transform agree at each sign class. Additional checks cover the 18 signed levels and their multiplicities, no zero frequencies, every multiplier congruent to two modulo four, the exact least modulus two, the maximum modulus 90, the explicit mask 85 attaining negative two, and Parseval's identity. No floating-point arithmetic, statistical extrapolation or inaccessible external certificate is involved.

The certificate concerns only this finite graph. An independent human or external mathematical audit has not been performed.
