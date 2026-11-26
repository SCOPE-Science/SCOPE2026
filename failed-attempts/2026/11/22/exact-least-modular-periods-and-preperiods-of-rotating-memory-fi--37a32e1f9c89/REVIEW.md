# Independent mathematical audit

## correctness

PASS

At a nonreset index (other than the initial n=2 when n=1 is prescribed rather than computed), subtracting the consecutive recurrence sums shows doubling. A reset adds the last two terms, giving the block multiplier c_k=3·2^(k-2) after the initial block; R_k is 1, 2 or 3·2^(k-4) in the three cases. In the component coprime to 6, all block terms are units and the unique reset in the ratio word has value 3/2, distinct from 2 at any nontrivial modulus. Therefore a period must be ks and is a period exactly when c_k^s=1. For k=2 the unit odd-modulus case is identical, while for an even 3-free modulus the terms at even and odd indices have different parity and the even positions test 3^s=1. The exact 3-adic values by block are q-1 or q as stated. At k=3 the 2-valuation is q+r, including the separate last deficient index n=2 for exponent 1. For k>=4 the last block with any 2-adic deficiency has q=floor((a+1)/(k-2)); if q>=1 the last deficient r is a+1-(k-2)q, while if q=0 the last deficiency is in the initial block at n=a+1. This gives the claimed cutoffs. To check sharpness of the unit start, extrapolate the geometric tail through the initial terms: its predicted preceding term is 1/2 (k>=4), 4/3 (k=3), or 2/3 (k=2, valid even for an even 3-free modulus), not the actual term 1 modulo any nontrivial modulus in its case. On a vanishing component a periodic suffix must be identically zero. CRT gives the maximum of the starts and the least global shift, with T=1 when there is no nontrivial unit component. The frozen script was read, not run, and the proof does not depend on its finite diagnostics.

## originality

FAIL

The exact modular classification was not found stated verbatim as a separate theorem, but is a direct arithmetic corollary of the inspected prior block-shape and valuation formulas for these very sequences. This is a stronger-statement implication, not attribution of a separately stated least-period/preperiod theorem or a claim that mere finite-state periodicity gives the exact formulas.

## value

FAIL

Exact periods and starts at arbitrary composite moduli are natural information about this recurrence, and the presentation is convenient. But for this particular sequence the prior exact geometric blocks already make the least shift a reset-phase check and one multiplicative order; the prior valuations already give the vanishing cutoffs by rounding. The exact start left over is a direct initial-value comparison. The classification is therefore a routine extraction from published specialized formulas, with no surviving independently valuable addition under the standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
