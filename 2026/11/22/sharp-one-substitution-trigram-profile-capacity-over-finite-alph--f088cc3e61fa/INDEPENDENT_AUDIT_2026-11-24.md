# Independent mathematical audit

## correctness

PASS

For all q≥2 and n≥5, profile equality from a fixed source is equality of the signed local trigram changes. A fresh exhaustive six-letter calculation by full local histogram subtraction reproduced 38,880 input operations, 38,580 distinct interior differences, 38,280 singleton fibers and 300 double fibers in seven orbits (six of size 30 and one of size 120), and checked that every input symbol remains visible after cancellations. Equal differences therefore share their entire symbol set, and no collision or larger fiber over any alphabet escapes by using more than six letters. The three slot marginals, each e_f−e_c in the interior, identify the ordered change even in a double fiber. They fix the two letters of every two-letter template and the two edited letters of the three-letter template, leaving no orbit stabilizer. The loss is consequently 6q(q−1)+q(q−1)(q−2) globally. At the four ends the nonzero slot-marginal sets are respectively {1}, {1,2}, {2,3}, {3}, giving exactly q−1 results per boundary position and no intertype or interior collision. Adding these to the interior inventory gives the stated capacity. An order-five Euler/de Bruijn linearization covers every context, and right padding preserves it; n(q−1) gives the stated lower bracket. The exact first length is not claimed. Independent certificate: /workspace/branches/63d13ad0-20fd-4ad1-9e9d-8854ad43c2df/audit_local_changes.py. The supplied scripts and recorded verification were inspected, not executed.

## originality

PASS

The supported advance is the exact q-ary, fixed-source, one-change image cardinality for oriented trigrams, with the seven collision types and global sharpness. The histogram identity and existence of de Bruijn words are established tools. No inspected equivalent or stronger result covers the collision census or capacity.

## value

PASS

The raw number of single substitutions does not measure the number of distinguishable short-read histogram observations. The result measures the loss exactly via collision classes and gives optimal sources at every sufficiently large length. The all-alphabet finite-support argument and sharp construction make this a useful benchmark beyond a small-alphabet census; no code cardinality, reconstruction theorem, or exact first length is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
