# Independent mathematical audit

## correctness

PASS

The frozen RESULT.md line 46 incorrectly says the matrix units and zero exhaust every local corner; a corner of rank at least two also contains maps with several arrows. The corrected RESULT.md fixes the sufficiency proof: using the explicit path-label convention, an arrow b→c with label x is transported to the corresponding source endpoints and has label gamma_b x gamma_c^(-1). This applies separately to every arrow of an arbitrary partial map and hence determines the whole output. Loops recover central label ratios; units with label 1 identify those ratios across points. The corrected text also handles the direction of conjugation: composing ordinary right-to-left, u mapped to conjugation by u^(-1) reverses multiplication, while indexing the same image by inverse representatives gives the quotient homomorphism. The fibers and all claimed formulas are unchanged. At each positive rank the common central action is free. Self-inversion forces equal supports and an underlying permutation of square one; for each z in the center an ordered pair of transposition labels has |G| solutions to the two product equations with common value z, and each fixed-point label has rho_G(z) solutions. The common value is unique at positive rank and can change when relabelling, so summation precedes division. Rank zero is a singleton. The abelian squaring fibers and the difference-coordinate description of the local rank-two group give the stated torsion separation. The supplied checker and output, not executed in this review, agree with hand checks (C4, C2² and S3 give 6, 8 and 22 self-inverse elements per rank-two support). The corrected proof establishes the all-rank result; there was no change to the checker or its test scope.

## originality

PASS

The supported claim is the explicit rook-wreath fiber together with the ordinary self-inverse spectrum controlled by central square-root moments. The general partial-inner map, its central-congruence mechanism, and ordinary wreath-product cycle bookkeeping are prior ingredients, not themselves claims of novelty. The repaired proof has the same quantitative scope and clarifies a genuinely different projective involution comparator.

## value

PASS

This gives a natural all-support enumeration in the partial-inner monoid for arbitrary finite label groups. Ordinary rank counts forget central square-root data, whereas the self-inverse spectrum detects them through moments. The two order-four abelian groups witness a difference even when every rank cardinality agrees. Counting a diagonal center globally, rather than quotienting labels independently, is essential to the exact formula. The point is the distribution and its separating power, not the abstract central-congruence theorem alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
