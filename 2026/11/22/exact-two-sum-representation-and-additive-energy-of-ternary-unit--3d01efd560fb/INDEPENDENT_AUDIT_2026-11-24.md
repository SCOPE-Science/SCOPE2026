# Independent mathematical audit

## correctness

PASS

The starting Deutsch–Sagan condition is on n+1 with its units digit unrestricted. Thus A_r is exactly the disjoint union of 3K_m+s, s=−1,0,1, with binary-digit ternary K_m, in the cyclic ring. The −1 residue at n=3^r−1 is included: n+1=3^r has one permitted leading 1. Binary-digit summands in K_m add without carries and with digit multiplicities 1,2,1, so w_m is the full ordered convolution. The offset sum has multiplicities 1,2,3,2,1 at −2,…,2, giving precisely the two successor terms in the indicated residue classes, including wraparound. Maximal w_m is unique at the all-ones word when m>0; adjacent weights can both be 1 only at the all-twos to all-zeros wrap. These arguments give the extrema and cover m=0 with all three counts equal. Squaring and summing gives 19H_m+8P_m with H_m=6^m and P_0=1; on low digits 0 and 1 the products contribute 2H_(m−1) each, while low digit 2 contributes P_(m−1) by carry. This proves E_r=(127·6^m+8)/5. The compatible law is S+3X with S uniform on −1,0,1 and X an independent fair binary-digit ternary integer. The digits of X_1+X_2 are i.i.d. with probabilities (1/4,1/2,1/4). Their strong-law typical frequency set for digit 1 is Haar-null, and finite affine images scaled by 3 are still Haar-null. Each conditional component is nonatomic and has full support on its corresponding coset, and the offsets cover the three cosets. Finally the cylinder collision sum is E_r/(3·2^m)^4 with rate 3/8 per digit, giving log_3(8/3). A fresh exact Catalan recurrence and ordered modular enumeration checked every target through r=7, not relying on the digit criterion for its input.

## originality

PASS

The distinct contribution supported is the explicit successor-weight formula for ordered cyclic sums of Catalan unit indices at every depth and its exact energy, with the collision-dimension consequence. The digit characterization, product-measure singularity mechanism, and the use of carry states are not asserted to be original independent results.

## value

PASS

The all-target finite law supplies exact extremal fibers and collision energy for a natural nondivisibility set, with an application to the cylinder dimension of its limiting convolution. These quantitative values distinguish arithmetic coverage from probabilistic uniformity and cannot be recovered from the given density or basis information alone. The weighted successor term is what makes this more than a restatement of the binary digit sum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
