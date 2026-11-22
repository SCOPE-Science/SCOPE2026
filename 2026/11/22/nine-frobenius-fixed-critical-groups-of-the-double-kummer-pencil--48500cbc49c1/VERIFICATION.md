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

# Reproducibility and boundaries

Run `python3 verify_kummer.py` from this directory. Python 3.8 or newer suffices; there are no external dependencies and no network calls. The program constructs the 24 graph vertices and 32 edges from the displayed product incidence rule, deletes the fixed root \(C_{00}\), computes the reduced Laplacian, determines each of the nine Frobenius orbit partitions, and calculates exact integer determinant and two-primary elementary divisors using its own arithmetic implementations. It verifies independently the square orbit-cokernel and rectangular \([R\mid P-I]\) presentations. It also checks \(Rx=32e_{H_0}\) with \(x_{H_0}=23\) and the four-generator full-invariant quotient. All nine checks and the final marker must succeed.

Exact outputs: ordinary critical group \(C_2^4\oplus C_8^4\oplus C_{32}\); nine case orders \(2^{21},2^{16},2^{11},2^{16},2^{13},2^8,2^{11},2^8,2^7\) in lexicographic \(I,T,C\) order; entire label group fixed \(C_{32}\). The module computes only finite integral presentations; the proof explains their equivalence to the graph group and group invariants. There is no assertion about geometric liftability of individual smoothing thicknesses or a full classification of all twists of Kummer K3 surfaces.
