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

# Reproducibility of the exact two-boson spectrum

The two adjacent source files are standalone Python 3 programs requiring only the standard library. Run:

```text
python3 verify_characteristic.py
python3 verify_resonance.py
```

The first program constructs the full two-boson Hamiltonian for six \((m,n,U)\) cases, computes exact characteristic polynomials by integer traces and checks their equality to the proposed product. The second checks six distinct asymmetry-threshold identities in exact rational arithmetic and evaluates two modular ranks for the 55-state \(K_{8,2}\) example at \(U=3\) and \(E=2\). In that example the rank of \(H-2I\) is 47 modulo each of the primes 101 and 103, consistent with the proven eight-dimensional eigenspace. This modular test does not, by itself, establish all-size exact nullity or spectral simplicity.

Critical symbolic checks in the proof are the incidence Gram formula \(R_mR_m^{\mathsf T}=(m-2)I+J\), the symmetric-block determinant \((x-U)xF_0(x)\), the two standard-block factors, and \(F_0(x)-F_A(x)=m[(3n-2)U-3nx]\) with the shore-swapped companion. The Hilbert-space dimension count closes all missing-block possibilities; root signs and positivity prove the crossing classification for every \(m,n\ge2\), not just for enumerated instances.

Only the stated onsite-only Hamiltonian, two bosons, positive interaction and uniform unit hopping are verified. Full independent scientific assessment and historical-priority certification have not been carried out.
