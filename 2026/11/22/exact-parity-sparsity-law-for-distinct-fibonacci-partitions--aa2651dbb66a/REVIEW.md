# Independent mathematical audit

## correctness

PASS

The Zeckendorf cutoff F_(k+2) corresponds to words of length k on indices 2 through k+1, with F_2 the only copy of 1. I reconstructed the generating function without relying on the 84-state certificate. Put L=1-z^4 and let A=z^4/L, B=z^5/L, C=z^2/L, D=z^3/L weight allowed gaps congruent to 0,1,2,3 mod 4. With P_10, P_01, P_11 the accepting extension series from the three nonzero parity pairs, the published count recursion modulo two gives P_10=1+(A+B)P_11+(C+D)P_01, P_01=(A+C)P_10, and P_11=1+(A+D)P_01+(B+C)P_11; the zero pair is absorbing and rejecting. The first selection at index j has weight z^(j-1); indices 2,3 mod 4 begin at 11 and 0,1 mod 4 at 01. The empty word and free final zeros give the full series [1+((z+z^2)P_11+(z^3+z^4)P_01)/L]/(1-z)=(1+z)P_11/(1-z). Eliminating the other two states gives P_11=(1-2z^4)/(1-z^2-2z^4-2z^5), which simplifies to the claimed series and implies the recurrence for all k>=5. Separately, a fresh subset-sum DP through cutoff 987 gave B_0 through B_14 as 1,2,3,4,5,8,13,20,29,44,69,108,165,252,389, with the ten recurrence residuals zero. The DP is a finite check only: start with weight 1 at sum zero and add each distinct part through 610 by descending-sum updates, then sum the odd entries below each Fibonacci cutoff. The cubic in the characteristic variable is strictly increasing on the reals and has its real root alpha between sqrt(2) and phi; its complex conjugate roots have modulus sqrt(2/alpha)<alpha. The two remaining characteristic roots are +/-1. The leading pole is simple and uncancelled, hence gives the stated residue and asymptotic; monotone comparison of consecutive Fibonacci cutoffs and Binet's formula give the all-real-cutoff Theta bound, not a universal leading constant. The supplied checker was inspected, not executed; the package does not attest external or formal verification.

## originality

PASS

The theorem under review is the exact odd-support cutoff series (and its sharp power exponent), not the pointwise partition recurrence or the finite-state approach in itself. The strongest inspected comparisons give recurrence ingredients, qualitative parity changes, moment/sum growth, fixed-value fibers, or parity laws for different partition functions. None established coverage of the claimed odd-support count. This is a bounded statement-level assessment, not a priority determination.

## value

PASS

For a classical partition function, parity is a natural arithmetic statistic distinct from its mean and moments. The theorem measures the full odd set, establishes density zero with an exponent close to but below one, and gives an exact count on the natural Fibonacci windows. This is a quantitative conclusion not provided by knowing that parity changes infinitely often or by merely recognizing parity in a finite automaton.

The dated certificate retains the supplied scientific assessment, sources and limitations.
