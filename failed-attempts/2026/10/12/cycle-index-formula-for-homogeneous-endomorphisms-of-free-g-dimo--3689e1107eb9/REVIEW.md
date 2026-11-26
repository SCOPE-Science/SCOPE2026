# Independent mathematical audit

## correctness

PASS

In the explicit free model and full automorphism action verified in Zhuchok–Zhuchok, any map from the generators to the length-k layer extends uniquely to a homogeneous endomorphism. That layer is X^k times the set of binary words of length k−1, with automorphisms relabeling X and fixing the binary words. Equivariance on a source d-cycle determines its images from one choice fixed by the d-th power of the permutation. There are 2^(k−1) F_d^k choices, where F_d is the count of generators on cycles of length dividing d. Choices across source cycles multiply. Burnside averaging and the type-class size r!/z_λ give the exact formula. At k=1 the binary label has one value and a generator image is one generator, giving ordinary endofunctions under relabeling. With A=2^(k−1)r^k, the identity fixes A^r assignments and each nonidentity fixes at most A^(r−1), since it has at most r−1 source cycles. This proves the stated fixed-r error bound, with the identity alone at r=1. It also bounds the fraction of labelled assignments with a nontrivial stabilizer by (r!−1)/A. No claim about nonhomogeneous endomorphisms is made. The frozen checker and log were inspected but not executed. Independent `python3 -I /workspace/checks/2.py` reproduced both rows through r=6 by permutation-level averaging and checked literal canonical orbit counts through r=4 at k=1 and r=3 at k=2; see /workspace/checks/2.log.

## originality

FAIL

Verified broader coverage: de Bruijn's 1972 enumeration of mapping patterns counts maps between two finite sets with simultaneous representations of the same group. With the known free model, take D=X, R=X^k×{a,b}^{k−1}, and G=S_X acting on these sets exactly as in the algebra. The required partition formula is a direct substitution into de Bruijn's fixed-map product and group average, not just an instance of a generic counting principle that leaves a new structural step to solve. The fixed-r estimate is elementary identity-term domination of that product. This is a prior-implication finding, not a claim that de Bruijn wrote the g-dimonoid notation or the specific k=2 table.

## value

FAIL

The grading and action are natural, and the correct formula is useful expository information. But the orbit computation is entirely a previously available mapping-pattern specialization, and the two numerical rows and elementary trivial-stabilizer bound do not add independent structural or asymptotic content. The record therefore does not establish a separate valuable finding under the scientific standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
