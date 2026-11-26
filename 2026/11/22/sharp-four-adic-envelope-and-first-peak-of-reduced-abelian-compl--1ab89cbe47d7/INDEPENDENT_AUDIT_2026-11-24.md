# Independent mathematical audit

## correctness

PASS

The alternation-count interval is filled by unit changes on sliding windows. Complement closure gives both initial bits for each count, hence one Parikh class for an odd count and two for an even count, with no collision across counts. Independently, the adjacent-difference sequence C satisfies C(2k)=1 and C(2k+1)=1−C(k); splitting windows by initial parity gives the even/odd extrema recurrences used in the proof, including the separate length-two base. For the width recursion any index n≤4^(m+1) reduces to s≤4^m+1 with gain at most one, and the possible extra index has width one by odd reduction. The proposed first width maximum occurs at 4(q_m−1); every earlier index reduces below q_m. The minimum alternation parity flips on q_m. Consequently for odd m≥3, q_m falls one below the complexity peak, q_m+1 has smaller width, and q_m+2 has the right width and even starting count; for even m, q_m itself suffices. At 4^j the width is two and the minimum is odd, giving four classes and the liminf; the envelope and first peaks give the 3/2 limsup. Independent tests reproduced maxima, first times and troughs through m=9 and scanned all factor classes through length 512. The scan is exhaustive there because each such factor lies in at most two length-512 substitution blocks, and all four adjacent block types occur in the scanned prefix.

## originality

PASS

The supported distinct contribution is the sharp all-scale prefix maximum together with its first attaining length and the resulting exact oscillation. Neither the definition, alternation identities, known candidate lengths, nor a pointwise formula is credited as new. A reported stronger pointwise source could not be read; its possible sharp-optimization coverage is a material but unresolved priority risk, not established overlap.

## value

PASS

The invariant is a natural established factor statistic. The theorem determines where its highest complexity first occurs at every scale, distinguishes the first alternation-width peak from the first reduced-Parikh peak, and quantifies logarithmic peaks coexisting with exact constant troughs. These are structural facts about a familiar word, not just pointwise reevaluations or a finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
