# Independent mathematical audit

## correctness

PASS

The two copies of the largest label are adjacent, with a unique parent word and gap. Restrict equal erasures for i<j to standardized labels ≤j−1, obtaining Δ_i(w_≤j)=w_≤(j−1). At the birth step, let p count the letters before the old maximum pair in w_≤(j−1), and g be the insertion gap of jj in that word. To match the position of the maximal pair in the two descendants one must have g−(number of copies of i before g)=p. When i=j−1, its three solutions are the gaps immediately before, inside and after ii; after deleting the surviving maximum, both lower words coincide. Otherwise the lower words coincide by induction; with the inductively prescribed configurations through j−1, the gap equation has a unique solution in each case: inside the old maximum pair on a nested chain, just after it on the increasing row, and just before it on the decreasing row. For a later inserted pair equality survives exactly when equal numbers of copies of i and j precede the insertion gap, since deletion standardizes that new pair to the maximum in both descendants. In a chain this excludes only the two stretches between corresponding opening and closing endpoints, 2(j−i) gaps; in a sibling row it excludes all 2(j−i)+1 internal gaps. An insertion cannot restore an already failed collision because one can erase the later maximum from equal descendants. This establishes necessity, sufficiency and the gap product, starting with one extension per geometry for each order-i word. In each displayed geometry all adjacent pairs collide, hence the interval equivalence and L formula. For the expected number of nested adjacent pairs, the birth probability 1/(2i+1) times the telescoping survival probability (2i+1)/(2n−1) gives (n−1)/(2n−1) in total. For siblings the update multiplier is (2n−4)/(2n−1) and the birth term 2/(2n−1), giving the fixed mean 2/3 from n=2. The extreme pair i=1,j=n gives precisely the three one-output words.

## originality

PASS

The full interval classification and fixed-pair law for standardized erasure of an arbitrary repeated label, together with the resulting all-order mean, are supported as distinct. Largest-pair deletion, plateau counting and standardization for ordinary permutations are prior techniques or different statistics. The same-channel finite capacity record already reports the order-five deck-size-one count; that finite instance is not credited as novel.

## value

PASS

The geometry identifies exactly which labels a receiver cannot distinguish under complete-label deletion, not merely how often some ambiguity occurs. The products and mean quantify typical loss of distinct outputs, while the extreme three words identify complete ambiguity; these are natural channel-specific invariants independent of the harder packing question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
