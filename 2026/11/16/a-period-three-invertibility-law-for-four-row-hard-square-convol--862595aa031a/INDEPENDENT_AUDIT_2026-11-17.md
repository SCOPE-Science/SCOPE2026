# Independent mathematical audit

## correctness

PASS

For G_n=P4 square P_n with open boundary, its independent column masks are exactly (0,1,2,4,5,8,9,10). The signed 8x8 matrices M_s(a,b)=(-1)^popcount(a&s) if a&b=0 else 0 give W=1^T M_{s_n}...M_{s_1}e for all 16^n column signings. Mod 2, 8 base scalar differences a_{j+3}-a_j vanish; Cayley-Hamilton propagates period three and oddness exactly for n mod3!=1. Exact recomputation verifies P=M14 M0 M11 has 1^T M11 annihilating P^i e for i=0,1,2,3 and P^4 e=e+2Pe+2P^2e, proving all 3k+1 singular. Q=M3 M15 obeys Q^6 e=e and the twelve successive two-mask multipliers (0,1,-1,2,-1,1,0,1,1,0,1,1), giving unit modulus for n mod3!=1. These identities are integer equalities checked independently from the displayed mask formula and do not rely on extrapolation from n<=4 brute force. Walsh diagonalization then proves the exact inverse norm.

## originality

PASS

Bounded search finds no prior covering the final substantive claim as a whole; all identifiable overlapping subresults are disclosed, especially the duplicate two-row parity/gap, and residual historical risks are retained.

## value

PASS

A natural complete all-width classification of Fourier invertibility for independent-set convolution on the nontrivial four-row square-grid strip, including explicit periodic zero and unit-multiplier certificates. Exact signed character testing is far richer than ordinary unsigned hard-square counts, and the all-length inverse norm is useful for finite-group recovery. It is a genuine structural transfer-matrix theorem, not a tiny enumerated instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
