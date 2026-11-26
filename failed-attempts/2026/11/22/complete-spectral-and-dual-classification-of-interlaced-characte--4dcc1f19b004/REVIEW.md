# Independent mathematical audit

## correctness

PASS

For each coordinate interlace u and Fourier label a, use the unit vector p^(−1/2)ζ^((σ(u)+a)t) on that interlace and zero on all others. These are an orthonormal basis. A translated/modulated atom with ℓ≡a mod p lies in the a-subspace; its u-coordinate there is √p exp(2πiℓu/N)ζ^(−bσ(u)) for translation bm. Summing its outer products over b annihilates all terms with distinct u,v by injectivity and finite character orthogonality, also for composite p. Hence each ℓ contributes p²P_a exactly, giving the spectrum, rank, spanning test and the scalar canonical inverse and inverse square root. Tight-frame occupancy is constant and positive; the paragraph in item 2 is read under its opening spanning hypothesis. The empty mask has the stated zero spectrum but is not a frame. Isospectral classes correspond exactly to occupancy histograms; multiplication of independent binomial choices and multinomial placement gives their census. At k=pq+s, the pigeonhole bounds min c≤q and max c≥q+1 when s>0 force the ratio bound, with equality requiring both extremal occupancies to attain the bounds; s=0 requires constancy. The number of guaranteed frequency-label deletions is min c−1, yielding the maximum q−1. Independent SVD and direct linear solves tested 35 masks with composite periods and widths up to m=p, and exact rational comparisons checked 43 size/design cases.

## originality

FAIL

The frozen result credits the prior block framework but does not account for its mechanical coverage. Asipchuk–De Carli–Rodriguez already give the entrywise factorization for arbitrary L, the translation-correlation formula for these interlaced windows, and the exact Fourier transform for the frame blocks. Substituting the stated characters and evaluating the character delta in those formulas gives exactly the claimed spectral data and eigenspaces for every mask. The dual and the remaining design and census formulas are then immediate rescaling and elementary counts on independent residue bins. This is an explicit presentation of the specialization, not an independently distinct scientific claim.

## value

FAIL

The occupancy summary is convenient as an expository corollary. But the existing operator formulas already give each eigenvalue by a character delta for this example family. The additional exact enumerations are binomial choices in indistinguishably populated residue classes with labelled items; the optimization is the elementary balanced-bin max/min bound, and the deletion guarantee counts the labels in the smallest bin. These do not solve a remaining substantive design problem beyond that substitution. No independently useful unknown invariant or nonroutine surviving subclaim is established in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
