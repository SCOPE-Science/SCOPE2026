# Independent mathematical audit

## correctness

PASS

The recursive three-mask transfer fills the least uncovered row uniquely and yields 18 reachable states with 35 weighted edges. Independent reconstruction of the symbolic 18x18 inverse verified [(I-zT(u))^{-1}]_{00}=((1-z²)(1-z-3z²+z³+z⁴))/Q(z,u), where Q=1-2z-7z²+8z³+17z⁴-4z⁵-9z⁶+z⁸-2u²z⁶(1-z²)². An independently written cell-level tiling recurrence reproduced every square-count histogram for N=1..9 (N=6: 281 zero-square, 2 two-square). The actual checker code was examined, not just its claimed output. Irreducibility and the zero-square self-loop yield a primitive positive transfer matrix. Distinct cycle square densities (0 on one-column loop, 2/6 on six-column return) preclude a zero coboundary variance, and Perron analytic perturbation supplies O(1) cumulant remainders and the CLT for all lengths. Limitations: open height-four strips only, uniform tilings, not full-plane pressure.

## originality

PASS

The specific 18-state rational pressure function, positive square-count variance and Gaussian limit for mixed domino/3x3 tilings are not supplied by Propp’s domino-only reciprocity nor Thorat’s tiling-cocycle criterion. The general transfer/Perron method itself is standard and not an originality claim. The mixed-strip object and square-frequency observable are genuinely more specific than those source statements. Best-of-knowledge priority is bounded because Thorat was accessible only as an abstract during this execution.

## value

PASS

Height four is the first case where a 3x3 square leaves a bypass row, creating a nonrenewal interacting strip. Its exact marked partition function and square-count Gaussian law provide a motivated benchmark for transfer-matrix pressure and large-tile density, not an arbitrary table or recoding of pure domino counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
