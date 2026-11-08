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

# Verification record

## Checked claims

The algebraic argument is given in `RESULT.md`. A self-contained checker `check_polygonal.py` independently enumerates the complete residue-fiber map for every order \(3\le s\le140\) and every exponent \(1\le k\le9\), and eleven additional orders at exponent \(k=12\). For even orders congruent to two modulo four it checks bijectivity; for even orders divisible by four it checks each individual square-root count and the exact image-size formula; for odd orders it tests each predicted reflection partner, counts empty/singleton/double fibers, and checks both extremal congruences. Output:

`VERIFY_OK parameter_pairs= 1253 input_residues= 186092 odd_pairing=exact even_square_fibers=exact permutation_and_double_cover=checked`

The checker was also rerun after extraction from the saved package; the stated run checks the actual embedded source, not a path reference.

## Limits

Numerical enumeration is finite and alone does not prove an assertion for all polygonal orders or powers of two. Those claims rely on the explicitly presented difference factorization, parity argument, inverse formula and classical modular square-root count. External priority and independent mathematical validation were not performed. The classification is for the first full block of \(2^k\) indices, not automatically an entire period when the polygonal order is odd.
