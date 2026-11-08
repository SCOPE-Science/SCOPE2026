# Review of the fixed-point descent covariance phase transition

## Correctness — PASS

The count of conditioned involutions and the four-vertex completion ratio are elementary factorial identities. The proof explicitly sums 43 partial matching configurations and seven nonzero weighted types; a symbolic checker verifies cancellation of arbitrary interval-size variables. SymPy also verifies the exact covariance identity and root expansion, while exhaustive involution enumeration through ten vertices independently tests each admissible fixed-point class and disjoint position pair (618 assertions). The derivative has negative discriminant for every integer \(n\ge4\), and the upper boundary \(k=n\) is treated separately. These checks support the all-size analytic proof; they do not amount to independent certification.

## Originality — PASS, with priority qualifications

Compared with Reutenauer's general cycle-type/descent-set enumerator, Guo–Zeng's unconditioned descent distribution, Kim's fixed-point-free two-point computations, and Kim–Lee's conjugacy-class total-descent CLT, the claimed novel content is a closed fixed-point-conditioned *nonoverlapping pair* covariance across all positions together with its unique rare \(n^{2/3}\) sign switch and the next two root terms. Kim's \(k=0\) case is not new. The general 1989 enumeration can encode every finite conditional descent probability, and a previous unretrieved specialization or asymptotic analysis could contain the threshold. Fulman's full 1998 text was not obtained. The 1989 primary theorem, the 2005 recurrence treatment, and the 2017/2018 related primary HTML texts were materially inspected, but the absence of a matching formula is not proof of priority.

## Value — PASS

A nonlocal pair of descent indicators has a position-independent dependence determined by the rare fixed-point count. The sign switch at the intermediate scale \(n^{2/3}\), well above the usual \(\sqrt n\) fixed-point scale, yields a complete finite sign classification and a nontrivial limiting covariance profile. The explicit correction terms sharpen the transition for finite integer sizes. This is more than a relabeling of a fixed-point-free calculation, although it does not establish a general joint limit theorem.

Self-review: passed. Independent audit: not yet performed.
