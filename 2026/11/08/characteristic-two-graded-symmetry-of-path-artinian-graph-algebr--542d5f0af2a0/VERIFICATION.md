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

Run `python verify.py` using Python 3. The verifier constructs the multiplication pairing on nonadjacent path coordinates directly, checks that all images of squared generators and edge products vanish, tests matrix invertibility by elimination, and counts every valid ordered image tuple. Independent finite-field models are used for primes \(2,3\) and for the extension field \(\mathbb F_4\). The covered instances are path lengths \(4,5,6\) over \(\mathbb F_2\), lengths \(4,5\) over \(\mathbb F_3\), and length \(4\) over \(\mathbb F_4\).

The expected verification report is `VERIFY_OK` after matching \(32,32,32,288,576,41472\) graded automorphisms, respectively. These tests do not exhaust all finite fields or all path lengths. The universal theorem rests on the annihilator-dimension characterization in `RESULT.md`, followed by the direct classification of endpoint images. No external certification or independent audit is asserted.
