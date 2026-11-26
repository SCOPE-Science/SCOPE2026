# Independent mathematical audit

## correctness

PASS

For a chosen quadrangulation diagonal, either polygon cut off by it has even boundary length by the face-side count 4F = n_side + 2I. Thus its endpoints have opposite cyclic parity. Conversely a noncrossing subset of (N−4)/2 opposite-parity diagonals gives (N−2)/2 regions with even side counts at least four, and the total side count forces each to be four. This supplies the parity justification for the geometric reduction. My independent replay /workspace/replay/audit_5.py, run with Python 3, enumerates recursively by the unique quadrilateral incident to a fixed root edge and computes signed sums directly. It obtained 1,3,12,55 configurations at side counts 4,6,8,10. At eight it confirmed the stated cycle and opposite chords, all signed multiplicities and the nullity weights {2:16,4:40,6:16}. Each compatible pair is one edge of the cubic Wagner graph, so its sign is negative precisely across the cut. A singleton gives 6 and a two-coordinate sign gives 4 on compatible pairs and zero exactly on crossing pairs. The replay summed the nonzero-frequency characters independently, confirming the entire kernel table and absolute sum 944, which divides by 256 to give 59/16. Translating and averaging a projection preserves its identity on the invariant range and keeps its image in that range. The resulting translation-commuting projection is the unique Fourier cutoff, so the endpoint absolute row/column sum minimizes over all projections, real or complex. At the decagon the replay confirmed 28 positive and 27 negative terms at the specified witness on 15 coordinates; odd cardinality forces all modes nonzero, hence the minimum magnitude is 1 and the maximum is 55. The square and hexagon are also zero-free by odd cardinality; no extrapolation to larger polygons is made.

## originality

PASS

The inspected prior work covers ordinary Fuss–Catalan counts and supplies related geometry or graph theory, not the octagon diagonal compatibility identification with its labeled Walsh zeros and exact endpoint projection cost, or the explicit decagon gap witness. The cut transform, averaging argument and odd-count invertibility criterion are standard; the novelty assessment rests on the specific geometry and exact additional invariants, not on those general identities.

## value

PASS

The first singular quadrangulation convolution is a naturally motivated finite boundary. The compatibility model identifies which physical pairs cause the first cancellations, and the exact projection constant quantifies the unavoidable cost of extracting the recoverable range at this boundary. The next polygon size shows recovery of invertibility rather than persistence, with an attained worst frequency. The value is in that geometric and recovery classification, not the already known number of dissections or a generic computation of a cut distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
