# Scientific review

## Correctness — PASS

The confusability criterion has an explicit forward and backward construction of a common output. The interior projection upper bound covers every alphabet of size at least two and every applicable length; it avoids numerical assumptions. For length five the modular-shift family attains the bound for every alphabet. For ternary lengths two to seven, the explicit source words in `codebooks.json` attain their matching projection bounds. One checker generates all channel outputs, the other examines difference supports and interior fibers. Both report a complete successful run on the delivered artifact. No unbounded enumeration is mistaken for an infinite proof.

## Originality — PASS, qualified

The closest general burst-code antecedent is Lastras-Montaño and Blaum, 2012 (DOI:10.1109/ISIT.2012.6284044), whose public abstract concerns structured algebraic code construction, not the exact finite homopolymer-free ternary optimization. The read-profile channel in Kiah–Puleo–Milenkovic (2014) has different observations. Holmes (2016) treats nonrepeating transducer encodings with errors, but the inspected methods and results do not give these exact constrained burst capacities. The subsequent homopolymer-free Hamming-bound study (2023) treats a different error relation. Current indexed-result and prior-claim searches found no equivalent or stronger implication, though this is not a uniqueness guarantee. The primary full text of the 2012 paper was unavailable and remains an acknowledged priority risk.

## Mathematical value — PASS

Requiring local repeat avoidance is a practical model of constrained synthesis. Two-coordinate burst corruption is a distinct adversarial error from ordinary single substitutions or the Hamming-distance condition. The first eight-message threshold and the tight interior-capacity bound are natural finite invariants; the exact lower constructions show the optimal robustness/redundancy tradeoff for the first three nontrivial capacities. The general upper bound and universal length-five equality add a reusable structural explanation, not merely a numerical lookup. The result does not promise performance for longer lengths or other physical channels.

## Scientific limitations

The exact result stops at ternary length seven. No full classification of maximum codes or asymptotic theorem is provided; no independent mathematical audit has been performed. Related unindexed work and an inaccessible plausible 2012 full text remain residual risks.

Self-review: passed. Independent audit: not yet performed.
