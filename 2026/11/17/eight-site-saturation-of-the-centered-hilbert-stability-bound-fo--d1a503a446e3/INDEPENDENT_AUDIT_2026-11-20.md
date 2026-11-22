# Independent mathematical audit

## correctness

PASS

The operator has row-selector branches because strict local maxima copy their larger neighbor. Each input coordinate feeds at most three rows. Orthogonal centering P gives ||PAh||^2 <= sum_j c_j h_j^2 <= 3||h||^2. Equality requires a nonzero centered h on multiplicity-three coordinates, hence two such columns; h=e_r-e_s proves sufficiency. Two triple columns require four separate nonadjacent local maxima, impossible for n<=7. At n>=8 values 3 at sites 1,3,5,7; 1 at 2,6; 0 elsewhere and epsilon(e_2-e_6) replicate the centered perturbation into six rows, exactly reaching sqrt(3). n=2 is constant output; the single-peak selector with h=e_2-e_0 has squared quotient (3-1/n)/2>1 for n>=3. Independent enumeration of every distinct-order selector for n=3..8 reproduced no two triple columns below 8 and their existence at 8; the analytic argument, not finite enumeration, handles all n.

## originality

PASS

Best-of-knowledge new centered-Hilbert threshold. Same operator has a published sharp Gini-amplification formula but that uses the pairwise-difference seminorm and cannot imply the centered-Euclidean operator norm. The related running-median theorem changes the operator. Classical morphology establishes definition and generic properties but not this sharp norm/equality cutoff.

## value

PASS

A sharp saturation threshold for the elementary morphological opening in the natural quotient-by-constants Hilbert metric, with a structural two-source equality obstruction. It diagnoses genuine worst-case two-input amplification, not an arbitrary small-instance check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
