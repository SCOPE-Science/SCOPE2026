# Independent mathematical audit

## correctness

PASS

Under \(M_n(\mathbb F_q\times\mathbb F_r)\cong M_n(\mathbb F_q)\times M_n(\mathbb F_r)\), the trace equations separate by factor. For a nonzero matrix over \(\mathbb F_u\), the functional \(C\mapsto\operatorname{tr}(AC)\) is nonzero and has kernel size \(u^{n^2-1}\); a zero component contributes \(u^{n^2}\). Deleting the zero vertex and, exactly for self-orthogonal vertices, the vertex itself gives the six formal degrees. \(E_{12}\) and \(E_{11}\) realize both square-trace types. The minimum gives \(B_0\), graph order gives \(qr=(v+1)/B_0\), and the degrees for which \(B_0\mid d+2\) recover \(\{1,q,r\}\); the product distinguishes the equal-factor case. The exponent in \(v+1=(qr)^{n^2}\) then recovers \(n\). The actual verifier blob was inspected and checks finite fields \(2,3,4,5\) and several factor pairs.

## originality

FAIL

The complete 2018 primary article gives, for every finite commutative ring \(R\), \(\deg(A)=|R|^{n^2}/|I(A)|-1\) or \(-2\) according to \(\operatorname{Tr}(A^2)\), and Corollary 3.7 states the full degree list for finite reduced rings in terms of nonzero ideal sizes. Applying this directly to \(R=\mathbb F_q\times\mathbb F_r\), whose nonzero ideals have sizes \(q,r,qr\), gives exactly the assigned degree fingerprint. Once that list is known, the recovery of \(qr\), then \(q,r\), and finally \(n\) is a short divisibility/exponent calculation. Thus the 2024 survey's direct-product problem is answered here by a routine specialization of an earlier stronger general degree theorem; under implication-level originality the record is covered despite the survey presenting direct products as open.

## value

PASS

Recovering the two simple factors from graph invariants is a natural reconstruction question highlighted by the direct-product survey problems. The record is rejected because this useful classification is too direct a specialization and arithmetic consequence of the pre-existing general degree formula, not because the invariant lacks mathematical interest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
