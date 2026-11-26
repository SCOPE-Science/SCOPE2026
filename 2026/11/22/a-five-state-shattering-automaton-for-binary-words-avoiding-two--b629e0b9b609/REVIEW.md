# Independent mathematical audit

## correctness

PASS

The subset-of-subsets invariant treats each labeling separately: unqueried bits union the two images for that labeling, queried bits split into two images, and an empty image means some labeling cannot occur even if the word is extended. I independently reconstructed the support language using three zero-run phases instead of the frozen seven suffix states. With phases A (ready), B (one zero), C (two zeros), the 0/1 transition rows are (B,A), (C,dead), (dead,A). All three start phases are allowed and all terminal phases accept. The recognized finite words are exactly those with each internal zero run of length two and each endpoint zero run of length at most two (the all-zero words have length at most two), equivalently avoiding 000 and 101. A leading run of one zero can start in B; a run of two starts in A. Encode subsets of A,B,C by bitmasks 1,2,4. Starting with the family [7], applying the above union/split rules breadth-first for input 0 then 1 gives these nine families with 0/1 successors (dash = rejection): [7]:(0,1); [1,6]:(2,3); [3,5]:(4,5); [1,2,4]:(6,−); [3,7]:(0,1); [1,2,6]:(7,−); [1,3,4]:(8,−); [3,4,5]:(8,−); [1,3,7]:(4,5). These are numbered 0..8 in order, with equivalence classes {0,4},{1},{2,8},{3,5},{6,7}. The quotient is exactly the published table. Minimality can be seen without software: continuation 1 separates {0,1,2} from {3,4}; 01 separates 3 and 4, 11 separates 0 from 1 and 2, and 011 separates 1 and 2. All states are reachable (empty, 1, 10, 11, 110). Independently evaluated the two transfer-matrix determinants: for M_ij=sum_{i→j} t z^b the first component of (I−M)^−1 1 uses det(I−M) and its determinant with column 0 replaced by all ones; expansion gives exactly the displayed denominator and numerator. The h inequality holds for every listed edge; the two witness prefixes 11 and 10011 end at 3 and 00011 is a loop there. The minimal lengths certified for weights k≥2 are ceil((5k−6)/2), and zero-padding is always permitted. n=0 has only the empty support and n=1 has VC dimension 1. Independently enumerated five-letter words and found [1,5,10,2], versus [1,5,10,7] for 000/111. The frozen code and captured output were read, not executed; their direct checks through n=11 are corroboration, not the all-length proof. The nine-family table is a bounded replay certificate: compute each subset image under A,B,C for a bit, union for mask 0 or retain both for mask 1, then compare the displayed classes and distinguishing suffixes.

## originality

PASS

Best of knowledge for this exact combination of forbidden factors, all-length support language and sharp count/dimension. Standard regular-language closure and transfer-matrix techniques are not claimed as new. The finite set of explicit right-language classes and the sharp periodic law are not supplied by the prior generic framework or the other forbidden-word calculations checked.

## value

PASS

In a natural two-forbidden-factor shift, querying with label-dependent completions yields many shattered masks even though fixed-background freedom in the bi-infinite shift is absent. The result goes beyond a density estimate and beyond finite examples: minimal right-language classes characterize all masks, the rational series counts them by weight, and a tight universal potential with exact witnesses gives the finite endpoint corrections. These are useful concrete invariants for comparing existential shattering across finite-type constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
