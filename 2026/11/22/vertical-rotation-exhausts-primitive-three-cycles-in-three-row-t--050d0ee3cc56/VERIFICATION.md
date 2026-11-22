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

# Verification and scope

The self-contained `verify_transfer.py` reconstructs every one of the 512 three-time column histories, evaluates all 262144 candidate directed adjacency pairs using the Boolean majority formula, and checks all recurrent vertices via two-pass strong components and separate directed return reachability. The expected recurrent components consist of two stationary uniform histories, six stationary nonuniform histories, and six vertical-rotating histories. A separate exact integer determinant computation on the displayed six-by-six rotating adjacency matrix gives \(z(z-2)(z^2-z+1)(z^2+3z+3)\); repeated integer matrix multiplication checks counts through circumference 20. The captured output is `verify_transfer_output.txt`.

The independent `verify_direct.py` uses the original three-neighbor update without referring to the history graph. It enumerates all \(2^{3n}\) binary initial configurations for \(n\in\{3,4,5,6\}\), checks that every primitive three-periodic state satisfies the asserted vertical-rotation equation, and agrees with exact point counts \(6,6,60,12\). The captured output is `verify_direct_output.txt`.

Run both with the standard-library Python interpreter from the same folder as these files. The exhaustive finite-graph decomposition, rather than sampled spatial circumferences, is the exact computer-assisted lemma supporting the all-length theorem. A finite direct simulation alone cannot prove the theorem. Neither the proof nor the scripts establish transient basin sizes, periods other than three, or any independently audited result.
