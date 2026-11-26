# Independent mathematical audit

## correctness

PASS

An eigenvalue is the sum of s_i s_j over unordered nonedges. The sum over all distinct pairs is ((n-2k)^2-n)/2 and the n cycle edges contribute n-2t, yielding the stated multiplier with no scaling. The two constant masks give n(n-3)/2>0 for the stated n>=4. In all other masks t=2j, and any integer 1<=j<=min(k,n-k) is realizable by two alternating positive compositions. Odd n has odd square 1 mod 8, forcing n=3 mod 8; even n forces n=0 mod 4. Conversely, absolute signed sums 0, 2 and 1 at orders 0, 4 and 3 mod 8 yield the displayed valid j; the smallest cases are n=8,4,11 respectively, and the run-count inequalities persist as n increases by 8. For multiplicities, mark a negative run's first vertex: there are n choices for its label and independent positive compositions of k and n-k into j terms. Unmarking divides by j even for words with a smaller period, because labels distinguish all j marked starts. Walsh characters span the full complex function space, so these counts give exactly the nullity and rank.

## originality

PASS

Walsh diagonalization, cyclic run counting and the one-step autocorrelation identity are prior techniques, not new here. The supported contribution is the exact all-length zero-mode classification and weighted nullity for the size-two cycle sector. Examined results do not state or mechanically specialize to the full arithmetic classification; the nonempty residue classes require their own feasible witnesses.

## value

PASS

Two is the first cardinality at which cycle adjacency excludes any incidence patterns. The exact rank of its natural convolution gives a nontrivial all-order recovery boundary and quantifies lost modes even among singular lengths. This is more informative than the unsigned support count and more specific than generic Walsh diagonalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
