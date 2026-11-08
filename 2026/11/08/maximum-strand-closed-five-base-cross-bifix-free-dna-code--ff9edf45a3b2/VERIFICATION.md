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

# Reproducing the five-base result

Execute `python3 verify_exact.py` and `python3 verify_independent.py` in the extracted directory. No third-party Python packages, network services or optimized solvers are needed.

The first program rederives 256 canonical candidates, 56 reverse-complement orbits surviving internal checks, 412 pairwise-conflict edges, an exact partition into 18 cliques, and the matching independent 18-orbit witness of 36 DNA words. It checks every required proper overlap (length 1, 2, 3, and 4), including self-pairs.

The second program independently encodes nucleotides as two-bit integers, reconstructs the same admissible orbits and conflict graph, validates the finite clique upper-bound certificate, and independently rechecks all witness-word overlaps.

Both programs must end with `EXACT_CERTIFICATE_OK` and `INDEPENDENT_INTEGER_REPLAY_OK`, respectively. These are complete finite checks for the claim at exactly length five, not evidence for other lengths, other alphabets, or independent scientific certification.
