---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

I checked the continuous-path classification, including ties and endpoints, in RESULT.md lines 27–59. Present labels form an interval by intersecting the two threshold inequalities. At a first entrance, an interior label strictly between two newly present labels would have both threshold inequalities strict at that time and would have been present earlier by continuity. Thus the first block has size one or is a consecutive pair. Once the interval is nonempty, a new label to either side is unlocked by just the coordinate serving that side; continuity forces distinct integer thresholds on a given side to be met at distinct times. A double event adds the two outside neighbors, which need not themselves be consecutive. The first straight segment and subsequent unit horizontal, vertical, or diagonal moves realize each allowable block exactly, including n=1, and constant segments introduce no extra births. Reindexing entrance times identifies precisely the ordered labelled blocks. Essential degree-zero multiplicities after reindexing record only the ordered block sizes. Choosing left or right at each post-initial singleton and moving both sides at every post-initial pair determines the initial interval uniquely from the final interval [1,n], proving the fiber size. Independently of the Delannoy identity, peeling the last block for n≥3 gives two copies of S_{n−1} and one of S_{n−2}; S₁=1, S₂=3, yielding the stated closed form. The ordered compositions of 1s and 2s give the Fibonacci count and asymptotic ratio. VERIFICATION.md and check_antichain.py describe finite exact regression evidence; the script was inspected, not executed, and grid enumeration alone would not cover all continuous paths. Definitions 4.3 and 4.10 of the source support the order/multiplicity interpretation.

## originality

PASS

Pass for the tie-inclusive class enumeration, the isolated-vertex Fibonacci barcode quotient, and the full ordered-composition fiber formula. The same-day rectangular-closure result really does cover the strict all-singleton restriction of the claim; no priority is inferred within the day, and that special case is not credited separately. The Delannoy and Fibonacci arithmetic is classical.

## value

PASS

This is a complete test family for the motivating extended-barcode class-enumeration problem. It isolates why allowing continuous paths with simultaneous births changes both the class count and which class distinctions survive persistence. The exact fibers and explicit representatives quantify a loss of labelled information that strict-path counts alone would miss. It does not resolve the general directed-cubical conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
