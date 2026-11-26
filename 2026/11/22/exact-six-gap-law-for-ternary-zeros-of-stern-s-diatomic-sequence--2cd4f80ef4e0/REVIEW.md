# Independent mathematical audit

## correctness

PASS

Both binary updates on the consecutive residues are invertible and start at (0,1), including the zero index. Projectivizing those pairs gives the independent four-letter substitution A→AC, B→CB, C→DD, D→BA, for [0:1], [1:0], [1:1], [1:2]. Three expansions give the claimed zero offsets for each letter, with at least one zero per block. The independent exact adjacent-letter enumeration closes on AC, CD, DD, DB, BA, AB, CB, CC, DC, AD; all ten communicate and AC has a self-loop. Their unique frequencies in that order are (4,2,4,1,7,2,4,1,2,1)/28. Counting internal gaps and the gap to the next block's first zero gives counts per block (4,2,2,4,1,1)/7 at lengths 2,3,4,5,6,8. Positivity and exact closure prove realization and exclusion. Primitivity gives uniform convergence of frequencies over aligned dyadic blocks of increasing size, independently of the starting letter pair. Any prefix is a disjoint union of such blocks, with at most one of each dyadic length, so blocks shorter than a fixed threshold have bounded total size and do not affect the limit. Partial terminal eight-index blocks alter only boundedly many gap counts; dividing by the total asymptotic rate 2 per block gives the claimed relative frequencies, mean 4 and variance 3. The proof covers the gaps from z_0=0 onward and does not infer an infinite conclusion from finite index sampling.

## originality

PASS

The zero-index set, an automaton for it, and its one-point density are known. The supported distinct claim is the complete first-return support and relative frequency law. The strongest inspected descriptions recognize the individual zeros and thus determine the entire sequence, but do not give the successive-return analysis; that requires additional adjacency information and an exact weighted count.

## value

PASS

The first-return law on a natural divisibility set is a local spatial invariant distinct from its known density. A sharp maximum of eight, the exclusion of interior gap length seven, and exact relative weights make a usable arithmetic benchmark for comparing different zero sets or moduli. The variance captures spacing variation missed by the known density and mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
