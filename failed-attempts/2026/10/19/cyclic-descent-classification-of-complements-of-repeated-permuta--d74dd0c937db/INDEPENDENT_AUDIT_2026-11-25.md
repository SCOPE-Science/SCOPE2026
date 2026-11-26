# Independent mathematical audit

## correctness

PASS

With i deletions and j retained letters so far, the next source letter has phase i+j modulo q, while the next required deleted letter has phase i. Pairwise distinct letters force all deletions to occur at retained counts j divisible by q. The intervening retained blocks are rotations determined by i modulo q. To obtain given phases, the minimal gaps are the least residues of consecutive phase differences, from initial phase 0 and with a return to terminal phase 0. Their sum is q times the number of descents including the last return; any excess full periods may be put in a gap. The cut into q-letter blocks is unique, including the empty case. For an independent check of the polynomial, count weakly sorted r-tuples of integers in [0,qj] by their residues s_i modulo q. Their quotients must increase by one at each internal descent and the final quotient is <= j-1 if s_r>0. Removing those shifts gives binom(j-d(s)+r,r) possibilities for j>=d(s), zero otherwise. Summation over phases and then j gives F_{q,r}(z)/(1-z)^(r+1)=sum_{j>=0}binom(qj+r,r)z^j. Summing in r by the geometric series gives the stated rational form; the coefficient of z^k in F_{q,r}/(1-z) yields the finite count. This is a classification of distinct linear remainder words for whole powers, not embedding multiplicity or cyclic equivalence of the remainders.

## originality

FAIL

Verified distinct indexed statements already cover the mathematical content. The bounded-digit theorem gives the same classification and all counts for q>=3, and the alternating-word run theorem covers q=2. Their equivalence uses an exact telescoping change of cost, not parameter resemblance. Every claimed enumerator then follows mechanically from the bounded-digit counts, including the formal descent series. This is a finding of equivalent coverage in the checked material, not a conclusion about which author or version was first: the equivalent catalog paths have later displayed dates than the assigned frozen path, and that observation alone neither establishes priority nor changes the statement comparison.

## value

PASS

A rotation-block classification is useful for a natural infinite family of complement sets: it replaces many possible deletion embeddings with a short exact membership certificate and a count of distinct outputs. The descent presentation explains the terminal constraint cleanly. This value of the mathematical classification is separate from the originality failure: the same mathematical information is already available in the checked equivalent formulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
