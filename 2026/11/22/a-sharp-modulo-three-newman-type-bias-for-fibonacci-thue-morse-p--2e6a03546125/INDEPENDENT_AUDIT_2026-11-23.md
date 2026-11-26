# Independent mathematical audit

## correctness

PASS

The zero word is included, and legal length-L words cover the half-open cutoff: those with a leading zero represent [0,F_(L+1)), and those with a leading one force the next digit to be zero and shift [0,F_L) by F_(L+1); the length zero and one cases start the induction. Weighting by digit parity therefore yields Q_L=Q_(L-1)-z^{F_(L+1)}Q_(L-2) with Q_0=Q_(-1)=1. At a primitive cubic root omega, modulo-three Fibonacci weights are 1,2,0,2,2,1,0,1, repeating since the Fibonacci pair returns. Exact arithmetic with omega^2=-1-omega gives M=[[8+omega,-1-3omega],[3+omega,-omega]], trace 8 and determinant 1. Each phase is a fixed prefix of the periodic transfer times M^t, so Cayley–Hamilton gives the same second-order recurrence; the phase-seven first values 3 and 23 make that subsequence real and strictly positive (the recurrence preserves strict increase). At z=1 the values repeat 1,0,-1,-1,0,1, giving b_t along L=8t+7. Fourier inversion of (b_t,q_t,q_t) gives the exact signed histograms and strict signs. The two distinct eigenvalues 4±sqrt(15) bound all eight phases by a constant times (4+sqrt(15))^t, and F_(L+2) is comparable to phi^L. The positive coefficient (23-3(4-sqrt(15)))/(2sqrt(15)) at phase seven gives a matching positive-order term in D_L(0), excluding every smaller exponent on Fibonacci cutoffs. Independent signed-word concatenation gave (2,-1,-1), (15,-8,-8), (121,-60,-60) at L=7,15,23; independent ring arithmetic and a residue DP also reproduced the matrix and base/phase checks. The unbounded result uses the proof, not the table.

## originality

PASS

The same parity word and sublinear arbitrary-prefix cancellation in each residue class are already covered. The distinct result supported here is the exact phase-seven histogram and sign law and the sharp explicit Fibonacci-cutoff exponent. Neither the inspected multiplicative-orthogonality theorem nor a fixed-weight conditional count determines them. The exact Resultary search self-match is excluded as independent evidence.

## value

PASS

The classical parity word and the first Newman-style modulus motivate the statistic independently of its numerical value. The exact conditional sign pattern contrasts with the bounded total cancellation, and the established exponent is an optimal order along a natural numeration cutoff family rather than a fitted or finite asymptotic constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
