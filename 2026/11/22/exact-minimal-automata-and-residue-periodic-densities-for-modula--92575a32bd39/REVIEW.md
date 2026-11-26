# Independent mathematical audit

## correctness

PASS

The group law follows by counting crossings of a word concatenation and the cocycle is bilinear over Z/mZ. Each letter generator has order m and positive powers give its inverse. The commutator for i<j gives the single central (i,j) coordinate generator, so every possible tuple is reached even for composite m. For a pair of different letters the two counts sum to the product of the corresponding letter counts, so acceptance requires exactly the stated zero pair coordinates and pairwise-zero products. Since every suffix image is available, indistinguishability of g,g′ is equivalent to equality of g^(-1)F and g′^(-1)F, i.e. stabilization of F on the left by h=g′g^(-1). Such an h belongs to F and has zero pair part. Testing h times the last letter forces the first q−1 letter coordinates of h to vanish by the (i,q) pair counts, and testing h times the first letter forces the final coordinate to vanish by the reverse-count product condition. Nothing requires cancellation by arbitrary residues, and the argument includes q=2. The faithful regular action gives the stated transition group (up to the right-action convention). For the uniform-letter random walk, every step increments total residue by one, all states communicate, and the m-fold power of one letter gives a return of length m; the period is therefore exactly m. Each probability block for the m-step walk on a length fiber is finite, irreducible and aperiodic, with uniform stationary law from double stochasticity. It converges exponentially. Every fiber has m^(d−1) elements, with exactly E_s accepting points, and over a prime field these have at most one nonzero letter coordinate, giving the two distinct limits. Frozen finite tests and outputs were inspected, not executed; they are not the basis for the general claims.

## originality

PASS

Best-of-knowledge pass for this exact simultaneous directed modular predicate's minimal DFA and its length-residue density. The class-two mechanism has published structural antecedents and nearby catalog analogues; the full recognition/minimality statement and accepting-fiber counts are distinct.

## value

PASS

The simultaneous two-orientation test is a natural uniform modular subsequence constraint. The result resolves whether the whole finite counting group is needed when only a single Boolean signal is observed, including all composite moduli where zero divisors change the accepting set. It also gives the exact long-word acceptance profile and shows that prime modulus yields genuinely different limiting densities rather than a single frequency. Together these are a structural and quantitative description for the whole parameter family, not a catalog of small automata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
