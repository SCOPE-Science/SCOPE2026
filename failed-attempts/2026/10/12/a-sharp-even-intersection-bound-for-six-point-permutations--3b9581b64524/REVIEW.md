# Independent mathematical audit

## correctness

PASS

The 48-element pair-block preserving subgroup S2 wr S3 is even-intersecting because each fixed block contributes 0 or 2 fixed points. Independent Python enumeration reconstructed the subgroup, all pairwise even agreement, and conjugacy-class sizes |(5,1)|=144 and |(3,2,1)|=120. The nonnegative central matrix W=3A_(5,1)+2A_(3,2,1) has degree 672, vanishes on family pairs, and its complete irreducible character-table spectrum has least eigenvalue -48. The eleven character rows yield dimension-squared total 720 and Hoffman inequality |F|≤720·48/(672+48)=48. The two verifier character evaluations were read as corroboration, not substituted for the representation-theoretic derivation.

## originality

FAIL

Decisive statement-level prior coverage in Banerjee–Dewan–Mishra, arXiv:2609.21645v1: the authors present the wreath-product lower construction n!! and explicitly report solving and verifying their relevant dual linear-program optimization in Sage for even n=6 through 16. Their Hoffman ratio then yields M(n)≤n!! in those computed instances, hence M(6)=6!!=48. The specific number need not be separately printed for that implication. The audited explicit two-class character matrix is a transparent alternate certificate, but the final claim M(6)=48 is already a published consequence of stronger computed coverage. The subject of the 1988 source need not be resolved to reach this failure.

## value

FAIL

The final stated mathematical target is the exact finite extremal number M(6)=48, already implied by a previously published verified n=6 dual optimization and wreath lower bound using weighted Hoffman methods. The new sparse two-class certificate is a succinct alternate proof but supplies no additional unknown invariant or new structural classification; as submitted it is a recomputation of covered finite-case optimum, not a separately motivated new mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
