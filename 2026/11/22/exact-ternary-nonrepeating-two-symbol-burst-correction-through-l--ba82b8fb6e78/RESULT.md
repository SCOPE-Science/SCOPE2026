# Exact ternary nonrepeating two-symbol-burst correction through length seven

## Finding

Let \(M_3(n;2)\) be the largest code of ternary length-\(n\) words with unequal neighboring letters that corrects any one nonwrapping substitution burst supported on at most two consecutive coordinates. The error may change both letters, one letter, or neither; the received word need not satisfy the source constraint. The exact capacity profile for \(2\le n\le7\) is
\[
(M_3(2;2),M_3(3;2),M_3(4;2),M_3(5;2),M_3(6;2),M_3(7;2))=(1,1,1,3,6,12).
\]
In particular, seven is the shortest admissible blocklength capable of representing eight different messages with these source and error constraints. For any alphabet of size \(q\ge2\), a structural upper bound holds at every \(n\ge5\):
\[
M_q(n;2)\le q(q-1)^{n-5},
\]
and the bound is sharp for every \(q\ge2\) when \(n=5\).

## Assumptions and scope

The alphabet \(\Sigma\) has \(q\ge2\) *labeled* letters. The source \(H_{q,n}\subseteq\Sigma^n\) consists exactly of words \(x=(x_1,\ldots,x_n)\) satisfying \(x_i\ne x_{i+1}\) at every \(1\le i<n\). A channel output \(z\in\Sigma^n\) is allowed from \(x\) if there is an index \(1\le j<n\) such that \(z_i=x_i\) at every \(i\notin\{j,j+1\}\). There is no requirement that the output be nonrepeating. The channel does not wrap from coordinate \(n\) to coordinate \(1\). Distinct codewords must have disjoint sets of allowed outputs; this means correcting *at most one* such error, including the zero-error output. We consider \(n\ge2\), since this channel is defined using a two-coordinate window.

For two words \(x,y\), let \(\Delta(x,y)=\{i:x_i\ne y_i\}\). Then they are confusable if and only if \(\Delta(x,y)\) is contained in the union of two (not necessarily distinct) windows of consecutive positions, each of length two. This characterization is for arbitrary \(q\) and does not assume either word is in \(H_{q,n}\).

## Proof

**Confusability lemma.** If an output \(z\) is possible from both \(x\) and \(y\), choose windows \(I,J\) on which their respective changes are supported. Outside \(I\cup J\), both sources equal \(z\), so \(\Delta(x,y)\subseteq I\cup J\). Conversely, suppose \(\Delta(x,y)\subseteq I\cup J\). Define \(z_i=y_i\) on \(I\setminus J\), define \(z_i=x_i\) on \(J\setminus I\), and set \(z_i=x_i=y_i\) off \(I\cup J\); on \(I\cap J\) choose either letter. Then \(z\) differs from \(x\) only in \(I\), and differs from \(y\) only in \(J\). Thus the criterion is necessary and sufficient.

**Universal upper bound.** For \(2\le n\le4\), the first and last possible two-coordinate windows together cover the whole word, so any two source words are confusable and the maximum size equals one. For \(n\ge5\), project a source word onto its *interior*, coordinates \(3,4,\ldots,n-2\). Any two sources with the same interior differ only in coordinates \(\{1,2,n-1,n\}\), which are covered by the first and last two-coordinate windows. They are confusable by the lemma. Therefore a correcting code uses at most one source per interior pattern. The interior has \(n-4\) letters, with no equal consecutive letters, so there are exactly \(q(q-1)^{n-5}\) possible interiors. This establishes the stated upper bound for all \(q\ge2\) and \(n\ge5\).

**Sharpness at five symbols for every alphabet.** Identify the alphabet with \(\mathbb Z/q\mathbb Z\) and choose, for each \(a\), the length-five word \((a,a+1,a+2,a+3,a+4)\) modulo \(q\). Every neighboring pair differs, and any two different chosen words differ at all five coordinates. Two windows of length two cover at most four coordinates, hence these \(q\) words are mutually nonconfusable. The universal upper bound at \(n=5\) is \(q\), proving equality.

**Ternary equality through seven symbols.** The supplied `codebooks.json` gives complete concrete codebooks of sizes \(1,1,1,3,6,12\) at lengths \(2,3,4,5,6,7\), respectively. Every listed codeword has no identical neighboring letters. For each length, both `verify_balls.py` and `verify_structure.py` independently check that no two listed codewords are confusable. Thus the displayed sizes are valid lower bounds. The first three match the universal upper bound of one. At lengths five, six, and seven, the universal upper bounds are respectively \(3,6,12\); hence all six entries are exact. Because six is less than eight and twelve is at least eight, seven is the shortest length carrying eight messages.

## Verification

Both accompanying scripts use only the Python standard library, read `codebooks.json` from their own directory, and return nonzero on a failed assertion. Run `python3 verify_balls.py` to enumerate actual received words after every possible two-symbol overwrite and test disjointness; it prints `VERIFY_OK`. Run `python3 verify_structure.py` for an independently implemented difference-support nonconfusability check, interior-fiber count and coverage test for all six ternary lengths, and a modular-alphabet check of the length-five all-alphabet construction over sizes two through eleven; it prints `ALTERNATE_OK`. The general bound and length-five construction are proved above and do not rest on an unbounded computer experiment.

## Relationship to prior work

Lastras-Montaño and Blaum's 2012 paper develops codes against structured bursts; its publicly available abstract focuses on modifying Fire, Burton and Gilbert check matrices and gives no exact ternary nonrepeating short-block capacity. The primary full text was not accessible for a complete comparison. Kiah, Puleo and Milenkovic (2014) analyze DNA sequence **profile/read** channels with different observation objects. Holmes (2016) develops modular transducers combining nonrepeating-source generation and error tolerance, with simulation rather than the present exact adversarial finite capacity. These works motivate jointly imposing a repeat restriction and burst correction, but the checked statements do not imply the exact maxima proved here. Subsequent general Hamming-distance bounds for homopolymer-free codes address a distance metric rather than this two-coordinate-window confusability relation.

## Limitations

No claim of exact capacity is made for \(n\ge8\), and no claim of sharpness for all alphabets is made at lengths six or seven. Codebook counts, all equality cases, optimal encoders, physical error probabilities, and cyclic or multiple-burst channels are not classified. The source restriction applies to transmitted codewords only.

## References

- L. A. Lastras-Montaño and M. Blaum, "On codes for structured bursts," IEEE ISIT (2012), https://doi.org/10.1109/ISIT.2012.6284044; publicly dated overview: https://research.ibm.com/publications/on-codes-for-structured-bursts.
- H. M. Kiah, G. J. Puleo and O. Milenkovic, "Codes for DNA Storage Channels," arXiv:1410.8837 (first posted October 31, 2014), https://arxiv.org/abs/1410.8837.
- I. Holmes, "Modular non-repeating codes for DNA storage," arXiv:1606.01799 (first posted June 6, 2016), https://arxiv.org/abs/1606.01799.
- K. G. Benerjee and A. Banerjee, "Bounds on Size of Homopolymer Free Codes," arXiv:2305.10741 (2023), https://arxiv.org/abs/2305.10741.
