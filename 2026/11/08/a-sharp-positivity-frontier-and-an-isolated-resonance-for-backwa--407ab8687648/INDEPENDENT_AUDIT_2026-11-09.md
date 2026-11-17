# Independent mathematical audit

## correctness

PASS

For d=1+3r/5, the discriminant of dz^3-(3/2)z^2+(3/5)z-1/10 is -27(9r^2-12r+5)/2500<0, so there is one positive real root and a complex pair. Their modulus tie occurs at s=2/5, corresponding to r=15/16. Independently reconstructed the degree-12 Bernstein expansion for -P12(s) on s∈[2/5,1] and found all 13 coefficients positive, from 7443/78125 to 360, implying A>2|B| even at the boundary; hence every y_n>0 below/equal threshold. Direct polynomial substitution gives p_d((1+r)^-1)=-r^2(r-3)/(10(1+r)^3), so for r>15/16 the oscillatory coefficient vanishes only at r=3 and y_n=4^-n. Otherwise the conjugate complex pair dominates and elementary rational/irrational phase rotation ensures infinitely many terms of each sign. This includes r=0 and nonrobust isolated resonance.

## originality

PASS

Jensen–Lóczi–Ketcheson 2026 specifies the BDFL3_2 scheme and studies A/L-stability and error optimization, not the fixed BE-started all-index positivity classification or the exact isolated r=3 cancellation. Vatsa et al. 2010 discuss equivalent BDF2OPT(4) for unsteady flow, not this scalar positivity theorem. Related published five-step BDFL resonance is on another recurrence with r=sqrt(5), not a covering theorem.

## value

PASS

The exact positivity frontier and isolated cancellation of otherwise dominant oscillatory modes are a sharp, motivated example distinguishing scalar trajectory positivity from absolute and SSP stability of an implicit multistep scheme.

The dated certificate retains the supplied scientific assessment, sources and limitations.
