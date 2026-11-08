# Self-review

## Correctness — PASS

The claim is an all-prime-power identity, not a computational extrapolation. The proof derives the additive collision equation \((z-w)(z+w-2zw)=0\) after normalizing each nonzero first-coordinate sum, and verifies the diagonal \(2q-5\) and zero-sum contribution \(2(q-1)\) separately. The involution \(w=z/(2z-1)\) has the specified three exclusions; its quadratic-character product equals the elliptic trace for characteristics at least five. In characteristic three, the cubic becomes singular and is evaluated directly; in characteristic two, Frobenius reduction to the inverse graph is valid. Fourier orthogonality then proves the moment identity. A pure-Python verifier checks the predicted energy for 32 explicitly constructed finite fields, including extension fields, and two Frobenius recurrences. The proof does not rely on any finite test to cover infinitely many fields.

## Originality — PASS, historical priority qualified

Relevant public literature: Katz–Koester (arXiv:0802.4371v1) proves general additive-energy structure; Bourgain–Garaev (arXiv:1211.4184v1) studies reciprocal **interval** sums; Kowalski (2010) discusses the elementary inverse graph \(x\mapsto x^{-1}\) and its exact fourth moment. The 2011 article of Calderón–de Velasco–Zárate considers a moment involving additional Dirichlet-character averages and a differently parametrized family, not the fixed unweighted two-coordinate sum here, as far as its available abstract establishes. Exact previously published finite-field quartic and inverse graphs are distinct: neither their statements nor their elementary collision equations imply the nonsingular cubic correction here. The published sources and relevant prior mathematical findings were compared by formulas and implication, not titles alone. Full-text access to the 2011 paper was not obtained, and unlocated broader generalized-Kloosterman moment formulas remain a risk. Searches cannot prove historical priority.

## Mathematical value — PASS

The graph is a canonical nearby deformation of the well-studied reciprocal graph. The exact ordered energy measures additive coincidences and simultaneously gives a complete global fourth exponential-sum moment; it unexpectedly introduces a specific elliptic curve, an arithmetic Frobenius recurrence over extension fields, and a sharp square-root-sized oscillatory correction. The distinct characteristic-two and characteristic-three degeneration mechanisms are structurally necessary. This is a motivated exact arithmetic invariant rather than an arbitrary finite slice or a restatement of a known upper bound.

## Scope and limits

The proof covers every prime power, only for the inverse-square graph and unweighted global moment. It does not establish more general rational graphs or individual exponential-sum evaluations. The finite verifier is independent implementation of the finite predictions but is not independent mathematical validation of the complete proof. Historical originality is provisional pending further full-text checks.

Self-review: passed. Independent audit: not yet performed.
