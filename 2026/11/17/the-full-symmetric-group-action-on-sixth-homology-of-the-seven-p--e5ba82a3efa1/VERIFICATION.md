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

# Reproducible checks

Run `python3 verify_kg7_character.py` with Python 3 and its standard library. The source constructs the \(35\) triple vertices of \(\operatorname{KG}(3,1)\), enumerates the orbits of each of \(15\) conjugacy-class representatives, excludes internally incompatible orbits, builds the inter-orbit incompatibility graph, and evaluates its independence polynomial at \(-1\) in two independent ways: dynamic-programming deletion and direct signed enumeration of compatible orbit subsets.

The source separately computes the degree-nine trace from \([t^6]\prod_{c}(1-(-t)^{|c|})\), obtains sixth-degree traces by the reduced Hopf trace identity, evaluates all \(15\) Specht characters by an explicit Murnaghan–Nakayama rim-hook recursion, and verifies every class value and every irreducible multiplicity. Its output is embedded verbatim in `VERIFIER_OUTPUT.txt`.

**Limits.** The checker does not recompute the full chain homology of the independence complex. The identification of the two rational homology degrees and ranks uses Feng (2026), and the independent embedded ninth-degree sphere generators use Feng–Wang (2024). Integer coefficients in intermediate signed traces are exact; the final homology representation and quotient conclusions concern \(\mathbb Q\). No independent external mathematical audit is asserted.
