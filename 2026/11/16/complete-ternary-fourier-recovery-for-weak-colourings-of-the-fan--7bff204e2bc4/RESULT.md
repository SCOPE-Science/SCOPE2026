# Complete ternary Fourier recovery for weak colourings of the Fano plane

## Finding

Let \(V=\mathbb F_2^3\setminus\{0\}\), with its seven points labelled by the binary integers \(1,\ldots,7\). Its seven Fano lines are the triples \(\{a,b,a\oplus b\}\), where \(a\ne b\) and \(\oplus\) denotes binary XOR. Let \(\mathcal C\subseteq(\mathbb Z/3\mathbb Z)^V\) be the colour assignments with no monochromatic line. These are weak proper colourings of the three-uniform line hypergraph (and are conflict-free on each three-element line).

Put \(\omega=\exp(2\pi i/3)\) and define the unnormalized Fourier multiplier
\[
 W(k)=\sum_{x\in\mathcal C}\omega^{\sum_{v\in V} k_vx_v},\qquad k\in(\mathbb Z/3\mathbb Z)^V.
\]
There are exactly \(882\) colourings. Every \(W(k)\) is an integer. The complete spectrum, counting frequency multiplicity, is

| Fourier multiplier | Multiplicity |
|---:|---:|
| \(882\) | 1 |
| \(-171\) | 14 |
| \(-90\) | 42 |
| \(72\) | 56 |
| \(18\) | 252 |
| \(-9\) | 364 |
| \(0\) | 1458 |

**Precisely the non-balanced characters vanish**: \(W(k)=0\) if and only if \(\sum_vk_v\not\equiv0\pmod3\). In particular, the additive counting-convolution operator \(T f=\mathbf1_{\mathcal C}*f\) on the full ternary group has rank \(729\) and nullity \(1458\). On the subspace of functions invariant under simultaneous translation of all seven colours, \(T\) is invertible. With counting convolution and the standard unnormalized Fourier multipliers, its sharp \(\ell^2\) inverse norm is \(1/9\), and the ratio of largest to smallest positive singular value is \(98\).

A stronger labelled classification records the complete balanced spectrum in twelve orbits under the \(168\) automorphisms of the Fano plane and the simultaneous frequency negation. In the table, each representative is a seven-digit base-three vector, in point order \(1,\ldots,7\).

| Frequency representative | Orbit size | Multiplier |
|---|---:|---:|
| `0000000` | 1 | 882 |
| `1110000` | 14 | -171 |
| `2100000` | 42 | -90 |
| `1101000` | 56 | 72 |
| `2211000` | 168 | 18 |
| `0221100` | 42 | 18 |
| `2211111` | 42 | 18 |
| `1211100` | 168 | -9 |
| `2122110` | 84 | -9 |
| `2221110` | 56 | -9 |
| `2111100` | 42 | -9 |
| `1111110` | 14 | -9 |

The orbit sizes sum to \(729\), the complete set of balanced characters.

## Assumptions and scope

All colour assignments are labelled, all seven lines of the unique seven-point projective plane are required to be nonmonochromatic, and each vertex can take any of three named colours. This is *not* proper colouring of the fourteen-vertex Heawood incidence graph, nor a requirement of distinct colours at all three points of every line. Fourier characters use the additive group \((\mathbb Z/3\mathbb Z)^7\); no probability or cardinality normalization is put in the convolution operator. The \(\ell^2\) norms are equivalent whether counting or uniform measure is used on both its input and output.

## Proof

For each subset \(J\) of the seven Fano lines, make the vertices of each line in \(J\) equivalent, and let \(\pi(J)\) be the resulting partition of \(V\) into equivalence classes. Its size is \(c(J)\). By inclusion-exclusion, the indicator of having no monochromatic line is the alternating sum of indicators that all lines of \(J\) are monochromatic. For a given \(J\), the character sum over its monochromatic assignments factors over the blocks \(B\in\pi(J)\). Summing a constant ternary colour over a block gives \(3\) if its frequency total is divisible by three, and zero otherwise. Therefore the following finite *integer* identity holds for every frequency:
\[
 W(k)=\sum_{J\subseteq\mathcal L}(-1)^{|J|}\,3^{c(J)}
 \prod_{B\in\pi(J)}\mathbf1_{\{\sum_{v\in B}k_v\equiv0\pmod3\}}. \tag{1}
\]
It requires only \(2^7=128\) line subsets; there is no floating-point evaluation or cancellation tolerance. In particular, evaluating (1) at zero gives \(|\mathcal C|=882\). Every summand is integral, proving integrality of all Fourier coefficients.

Simultaneously translating all colours by \(t\in\mathbb Z/3\mathbb Z\) preserves \(\mathcal C\), whereas a character picks up the factor \(\omega^{t\sum_vk_v}\). This proves \(W(k)=0\) whenever the total frequency is nonzero. For the reverse implication, use the full automorphism group \(\mathrm{GL}(3,2)\) acting on the seven nonzero binary vectors, together with frequency negation. Every invertible binary linear transformation is determined by an ordered independent triple of images of the standard basis; their number is \(7\cdot6\cdot4=168\). Enumerating the resulting images of the \(729\) balanced frequency vectors yields exactly the twelve disjoint orbits listed above. Formula (1) is invariant under these transformations. Substituting one representative from each orbit into (1) yields the twelve nonzero values displayed. Hence no balanced coefficient vanishes. All representative substitutions, group generation, orbit sizes, and partition operations are supplied in `check_inclusion_exclusion.py` and verified by exact arithmetic.

Finite-group character orthogonality diagonalizes counting convolution: its eigenvalues are \(W(k)\), up to replacing \(k\) by \(-k\), which leaves the table unchanged. The balanced characters are exactly those trivial on the diagonal global-colour-shift subgroup, hence form a Fourier basis of the invariant subspace. The smallest absolute nonzero multiplier is \(9\), while the largest is \(882\), giving the stated sharp inverse norm and condition number.

## Verification

Run `python3 check_direct.py` and `python3 check_inclusion_exclusion.py` in the same directory. Both use only the Python standard library. The first independently enumerates all \(3^7=2187\) colour vectors, selects the \(882\) allowed ones, and applies an exact seven-axis ternary Fourier transform in \(\mathbb Z[\omega]\) using pairs of ordinary integers. The second evaluates (1) for all \(2187\) frequencies, explicitly constructs all \(168\) binary linear automorphisms, and verifies the twelve orbit representatives and multiplicities. Both agree with the seven-level coefficient table, the nonzero-spectrum gap, and the total rank.

As a separate consistency identity, the exact values satisfy Parseval:
\[
882^2+14(171)^2+42(90)^2+56(72)^2+252(18)^2+364(9)^2=3^7\cdot882=1{,}928{,}934.
\]
The executable finite certificates provide exhaustive verification because they cover all colour vectors, all Fourier vectors, and all line-subset partitions; a partial sample or finite-range extrapolation is not used.

## Relationship to prior work

General studies of nonmonochromatic and conflict-free hypergraph colourings, including Cheilaris–Keszegh–Pálvölgyi (2013), motivate this smallest projective-plane colouring problem, but do not imply the six nonzero Fourier levels or the sharp deconvolution theorem. Henning–Löwenstein (2015) investigate strong independence of the same Fano hypergraph, a different invariant. Other literature studies Heawood-graph colourings, requiring different vertices and edges, and lean colourings of Fano configurations, which impose different monochromatic-edge objectives. Those do not imply the frequency-resolved table. The standard group-character diagonalization supplies the interpretation of the new explicit multipliers, not their values. The literature search did not identify an earlier complete signed Fourier classification; this is bounded evidence rather than a proof of historical priority.

## Limitations

The theorem is specific to three named colours and the seven-point Fano line hypergraph. It does not classify arbitrary Steiner triple systems, different palette sizes, or weighted colourings. Its finite verification uses full exhaustive exact integer arithmetic with supplied source; independent review has not been performed. Indexed searches may miss unpublished computations, historical tables, or alternative Fourier terminology. A 2015 Fano-related journal article was accessible at abstract level rather than in full, though its stated subject is strong independence, not Fourier colouring recovery.

## References

1. A. Cheilaris, B. Keszegh, D. Pálvölgyi, *Unique-Maximum and Conflict-Free Coloring for Hypergraphs and Tree Graphs*, SIAM Journal on Discrete Mathematics 27 (2013), 1775–1787. Published online 24 October 2013. DOI: https://doi.org/10.1137/120880471 . Author manuscript: https://real.mtak.hu/15173/1/cfumhyptjsiam.pdf .
2. M. A. Henning and C. Löwenstein, *The Fano Plane and the Strong Independence Ratio in Hypergraphs of Maximum Degree 3*, Journal of Graph Theory, first online 9 October 2015. DOI: https://doi.org/10.1002/jgt.21993 .
3. Elementary finite-abelian-group character orthogonality and inclusion-exclusion are used in their standard forms; equation (1) gives the self-contained specialized calculation.
