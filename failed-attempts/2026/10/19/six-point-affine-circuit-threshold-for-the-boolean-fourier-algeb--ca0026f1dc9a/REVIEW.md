# Independent mathematical audit

## correctness

PASS

Translate one point to zero and restrict to the affine span, since each local character repeats equally often in the ambient Fourier sum. Six distinct points have affine rank 3, 4, or 5. At rank 3 they are the complement of two points in an eight-point flat. At rank 5 they are an affine basis. At rank 4 the dependence space on the six augmented columns (1,a) is one-dimensional, and its nonzero support has size four or six. Equivalently one can average the absolute sum of six signs over the uniform affine-character sign vectors: the rank-4 types impose a product +1 constraint on four or all six signs, respectively, and rank 5 imposes no constraint. This gives the stated Walsh histograms and norms; rank 3 follows by complementing a pair. For at most five points, the affinely independent cases give norms 1,1,3/2,3/2,15/8 in order of size, and the dependent cases are an affine plane at size four or a complement of a three-set in an affine three-flat at size five, with norms 1 and 7/4. The empty set has norm zero. The count of six-circuits per four-flat is the count of unordered five-point affine bases divided by six: the additional point needed to make the full six-set an affine circuit is the sum of those five points. The phrase 'unique affine-dependent sixth point' in the census proof means unique completing point making a six-circuit, not unique point making the union dependent. Counts for the other types follow from the number of r-flats, complementing pairs in 3-flats, subtracting the rank-3 and six-circuit cells inside each four-flat, and counting independent six-tuples. The formulas have the requisite zeros in dimensions three and four. Independent exact Walsh butterfly enumeration of all weight ≤6 functions in dimension four gave the count triples (840,6720,448) in norm order (3/2,7/4,9/4) at weight six and confirmed the lower-weight maxima. The original `checker.cpp` was inspected but not executed; its documented replay is `g++ -O2 -std=c++17 checker.cpp -o checker` followed by `./checker` in the package or a copy of it.

## originality

FAIL

The primary public affine-orbit tables of Philippe Langevin (page dated 2009) cover the entire finding by a direct extraction, not just the number of bent functions. Every support of at most six points lies in an affine space of dimension at most five. I evaluated the published five-variable affine representatives of weights zero through six and used their tabulated stabilizer orders. At weight six the four rows already encode every stated affine type, Walsh norm and orbit count. The all-dimension census follows by multiplying per-flat counts by the number of flats of the relevant rank. The lower-weight rows likewise give the exact bound and hence the sharp support threshold. The frozen proof is correct, but its claimed profile and census are mechanically recoverable from a pre-existing broader classification.

## value

FAIL

The support threshold and its affine geometry are natural, and the proof is an informative compact derivation. But the scientific finding as claimed is a mechanically extractable slice of an existing exact five-variable affine classification, with the dimension-general counts given by routine affine-flat multiplication. The exact invariant and all cases are already determined by that evidence; the record does not establish a separate structural contribution beyond the extraction and elementary reproof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
