# Independent mathematical audit

## correctness

PASS

In the exact inclusion–exclusion numerator 15!D the odd-j coefficients are positive and the even-j coefficients negative. The factorial has valuation 11. For the odd bases x_j=j^(2^n)-1 has valuation at least n+2, and q_j=x_j/2^n obeys q_(j,n+1)=q_(j,n)+2^(n-1)q_(j,n)^2; the increment is a multiple of 8192 for n>=10. Direct powers give the listed eight residues and their weighted sum 4096 mod 8192, so the linear odd moment has valuation n+12. For d=a-b, Vandermonde and h*binom(d,h)=d*binom(d-1,h-1) show that the binomial-coefficient difference at order t has valuation at least r-floor(log2 t) whenever nonzero. For t>=2 the bound t(n+2)-floor(log2 t)>=2n+3>=n+13 forces every higher term above the linear term, hence the odd numerator has valuation n+r+12. Among even j, bases with just one factor of two give their binomial coefficients modulo 128 after division by 2^(b*2^n), because odd units raised to 2^n are 1 mod 128 and j^(d*2^n) vanishes mod 128. Higher-valuation bases do not contribute modulo 128. The coefficient sum 8128 gives valuation b*2^n+6 in the even numerator. Unequal valuations give the lower one; equality gives at least one more factor of two and no exact boundary value is asserted. T increases without bound for fixed b, giving the eventual fixed-pair formula. Independent replay: python3 -B /workspace/reproduce_frozen.py 5 evaluates the base powers with integer arithmetic, checks the even sum, probes both strict regimes and resonance, and checks small pairs by the Stirling recurrence. An infinite displayed diagnostic means zero at the test precision, not an infinite valuation of D.

## originality

FAIL

A distinct earlier-dated catalogue record states the identical full theorem, including all quantified bounds, the parity-collision lower bound, and the eventual fixed-pair corollary. This is demonstrated exact coverage, not a tentative search hit or an inference from a record date. The earlier proof also uses the same odd/even numerator split and the same normalized modular certificate. The classical sources separately credit the conjectural target and special cases but are not the reason for failure.

## value

FAIL

The competition between the odd- and even-base terms and its exact saturation threshold are mathematically worthwhile, but these are already fully computed for the same parameters in the earlier record. Rewriting the same law in terms of r-T and scaling the same modular certificate do not yield an independent useful invariant, a new range, or an exact result at equality. There is no distinct valuable remainder in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
