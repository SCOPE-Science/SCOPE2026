---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In unrolling the source of a copied bit, following a neighbor already updated strictly decreases visit rank until the next clockwise rise; the source is exactly the first member of S strictly clockwise. There is at least one rise and one fall. Between successive members of S the output is a constant block holding the old bit at the next member. Its restriction to the k source sites therefore rotates the image, proving periodic entry in at most one sweep, exactly 2^k recurrent states, and 2^{n−k} preimages per recurrent state. For p dividing k a length-k rotation word of least period p is determined by its length-p primitive block, counted by Möbius inversion; a rotation period cannot fail to divide k if least. Multiplying the fibers by orbit size or by the primitive-state count gives the two basin formulas. Rooting the cyclic rank list at its maximum gives one fixed cyclic ascent plus the ordinary ascents of a permutation of n−1 entries. This yields the schedule factor and the joint count, with k=1 exactly the all-fixed-after-one-sweep class (a one-hot core realizes period k otherwise). For independent continuous ranks the cyclic ascent count has variance n/12 from adjacent covariance −1/12, and the usual bounded one-dependent CLT applies after dropping the wraparound comparison. Bounded differences gives an exponential lower-tail bound for k<n/4, and a uniform core word has proper period with probability at most k·2^{−k/2}; thus the stated Gaussian law follows. Inspected both supplied verification scripts and archived outputs (symbolic n=3–8, exhaustive states n=3–7); not rerun. The failure is not a mathematical counterexample.

## originality

FAIL

The decisive prior is not just a sensitivity classification or an O(n) period bound. The proof of Theorem 9 of de Oliveira et al. (arXiv:2004.07128, §4.2.1) gives exactly the copy-through-to-the-first-stopping-edge formula for Rule 170 in the broader block-sequential setting. Its singleton-block specialization is the frozen copy-source lemma. The asserted core, uniform basins and period census are direct consequences of that known map and classical rotation counting, with the schedule factor separately present in the Rule 150 record and independent of the cellular rule. No distinct nonmechanical mathematical remainder was established. This credits an implication of an available proof, not an assumption that the prior authors wrote all of the same formulas.

## value

FAIL

The census is a useful exposition of the Rule 170 map, but as a new finding it supplies no nonmechanical invariant beyond the prior exact coordinate map. The fiber sizes are powers of two from unused coordinates, the orbit sizes are those of an ordinary binary rotation, and the schedule census and CLT add standard permutation and random word calculations. The work does not clear the value standard for a distinct exact result as submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
