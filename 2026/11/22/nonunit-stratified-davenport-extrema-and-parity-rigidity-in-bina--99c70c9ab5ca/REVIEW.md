# Independent mathematical audit

## correctness

PASS

For total nonunit valuation V<n, removing any nonunit lowers the valuation and cannot preserve the product. After cancelling the unit part and t^V at the reduced precision, a deletion is possible exactly when a nonempty unit sublist multiplies to 1 modulo t^(n-V). For V>=n the product is zero: a unit could always be deleted, and otherwise it is enough to test whether a single deletion still gives zero. This gives r<=n and forces all valuations to be one at r=n (including the case n=1, where t represents zero). The generators 1+t^j for odd j have orders 2^e_j; their binary power factors give one lowest-degree pivot at each m=1,...,n-1, proving a unique cyclic-coordinate presentation. Truncated powers of the augmentation generators then give the upper Davenport bound, while order-minus-one repetitions of each cyclic generator give the lower bound. At fixed r<n, V>=r gives the upper bound, attained by r copies of t and lifted extremal units at precision n-r. Subtracting from the all-unit maximum leaves the sum of 2^v2(m)-1 on the last r degrees: it vanishes for positive r exactly at r=1 and even n. The separate zero-product maximum n ties at depths 3 and 4, wins at 1 and 2, and loses from 5 onward. Strict growth of d_j forces V=1 in every tied one-nonunit case. Inspected verify.py and verification_output.txt: their finite checks are supplementary (all small-depth profiles only through n=4; group generation through n=12); the deletion and group arguments establish the all-depth result. The bundled code was inspected, not replayed.

## originality

PASS

The unrestricted scalar length is known and is not credited as new. Earlier stabilizer/relative-constant arguments supply tools for controlling unit deletions but the inspected results do not give sharp length at each exact nonunit count, or the parity classification and valuation-one equality cases. The pass is limited to that refinement, not the group constant or the use of stabilizers.

## value

PASS

The new profile answers an inverse question left open by the scalar cutoff: precisely how much length is lost by prescribing noninvertible factors and which such strata can tie the maximum. The parity dichotomy, small-depth exceptions, and the explicit reduced-unit criterion give usable structural information without claiming a full classification of the unit lists.

The dated certificate retains the supplied scientific assessment, sources and limitations.
