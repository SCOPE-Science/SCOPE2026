# Independent mathematical audit

## correctness

PASS

The externally proved three-branch James profile in Mizuguchi (2020) Theorem4.1 was checked against the full source. Differentiation independently gives F1’=(2b²−1)/(2b²)<0 up to r, F2’=−(b²+4b−3)/(b²−b+1)² with exactly one interior maximum on [r,2/3], F3’=−2b(b−1)/(b²+2b−1)²>0 on [2/3,1). Values at junctions are F1(r)=F2(r)=(3sqrt5−1)/4 and F2(2/3)=F3(2/3)=10/7, latter strictly larger. At k=(1−r)/r=r the six consecutive decagon vertices satisfy v_(j+1)=(1/r)v_j−v_(j−1), with 1/r=2cos(pi/5); the central opposites complete an invertible image of a regular decagon. SymPy independently reproduced all rational derivative formulas and the exact endpoint comparison; the proof depends on the cited full published source profile, not a finite parameter scan.

## originality

FAIL

Decisive stronger-coverage comparison: Mizuguchi’s fully inspected Theorem 4.1 already gives EXACT J(X_beta) at EVERY beta in [1/2,1], including both golden-ratio and two-thirds boundaries. The proposed unique minimum and numerical value follow by routine differentiation and evaluating these known branches, and the regular-decagon identification follows from the explicitly known family vertices and the same golden-ratio relation. The claim is a direct elementary corollary of the fully published all-parameter formula, not an original mathematical assertion even though the paper does not spell out the argmin. The separate Banach–Mazur record shares an exact value but does not affect this stronger prior-implication verdict.

## value

PASS

The source computes an entire natural 1-parameter *complete* decagonal Radon family without identifying its optimal member. Picking out the unique affine-regular decagon by globally minimizing a classical geometric constant is a motivated extremal/rigidity result, rather than evaluating an arbitrary slice or repeating a tabulated number. Its significance is bounded to this family and does not require paper-sized generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
