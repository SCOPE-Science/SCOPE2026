# Independent mathematical audit

## correctness

PASS

Put u=P², f_t=U_{2t}/P and g_t=U_{2t+1}. The two-step recurrence or powers of [[0,1],[1,P]] give A^{2t}=[[g_t−u f_t,P f_t],[P f_t,g_t]], including t=0. Its diagonal entries are 1 mod u and g_t is odd. Squaring gives f_{2t}=f_t(2g_t−u f_t) and H_{2t}=2H_t+uH_t²+f_t² with H_t=(g_t−1)/u. Since 4 divides u, induction gives valuations k for f_{2^k} and k−1 for H_{2^k} when k≥1 (H_2=3+u), with no cancellations. Multiplying A^{2t} by A^{2n} yields the claimed shift valuations, and telescoping an odd number of shifts preserves each exact valuation. Thus the isometries are for U_{2m}/P and (U_{4m+1}−1)/P², not for all normalized odd indices at once. Each isometry permutes residues at every level, and all other odd indices lie in the same odd ball by the diagonal congruence. The balls are disjoint already mod 2, including N≤h; counting reductions and summing Haar measures proves the remaining statements for either sign of P. The symbolic check, not the frozen reported finite modular checks, establishes the universal claim.

## originality

FAIL

The exact two-ball wording was not located in the relevant earlier papers. However both claimed isometries, hence the entire image/count/density statement, are direct corollaries of Sanna’s general valuation theorem and the standard Lucas factorization of a difference with even half-gap. The even isometry is also covered directly by the power-of-two discriminator theorem. No distinct surviving claim is established.

## value

FAIL

The explicit image is useful as a worked consequence of the valuation and discriminator theory, but the proposed new invariant, isometries and counts are mechanically determined by that theory and the usual product identity. No separate nonroutine consequence or distinction remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
