# Independent mathematical audit

## correctness

PASS

In the unnormalized L² convention, decomposing m=qℓ+j and applying Parseval over ℓ and the integer translations gives F=Σ_j |Zg(x,ω+j/q)|², a sum rather than its density-normalized average. Zak unitarity makes the optimal constants the essential extrema; continuity makes those the ordinary extrema. Put r=e^(−2πw). Poisson summation of the Fourier exponential gives the two geometric tails with common denominator 1+r²−2r cos(2πx) and nonnegative real coefficients a_s,b_s. With C=Σ(a_s²+b_s²)>0 and E=2Σa_sb_s>=0 the derivative of (C+Eu)/(1+r²−2ru)² in u=cos(2πx) has positive numerator E(1+r²+2ru)+4rC. This forces x=1/2 for the minimum and x=0 for the maximum. On these fibers the ω-dependent part is proportional to r^(2ω)+r^(2/q−2ω), strictly convex and symmetric, giving the unique minimum at 1/(2q) and maximum at the identified endpoints modulo 1/q. At the minimum the sum of q squares cannot vanish because the q frequency translates are distinct and an individual square vanishes only at s=1/2. With c=2πw and R=sinh(c)/sinh(c/q), the extrema simplify to (π/w)²(R−q)/(2 cosh²(c/2)) and (π/w)²(R cosh(c/q)+q)/(2 sinh²(c/2)). Expanding R=q+(q−1/q)c²/6+O_q(c⁴) at zero and using R~exp(c(1−1/q)) at infinity gives all stated leading coefficients and ratios, for fixed q. Replay is analytic in RESULT.md:31–84; VERIFICATION.md and verify.py were inspected, not rerun. Their finite numerical checks cannot establish these global extrema.

## originality

FAIL

Verified current equivalent coverage: a distinct indexed later-dated Poisson record supplies the exact all-q constants and extremizing fibers with the same conventions. The width limits follow directly from its formulas and do not leave a separate result. An earlier indexed two-coset calculation already covers q=2, and the 2022 two-sided-exponential formulas give the same condition-number profile via the Fourier/dilation equivalence even though their absolute constants as printed differ by a common factor. The later catalogue match does not establish that the frozen Oct. 26 all-q claim was already known when written or that the later result is independent of it.

## value

PASS

Exact unnormalized spectral extrema for a natural reconstruction window simultaneously quantify conditioning at every integer density; the two width-degeneration regimes are mathematically informative. This is intrinsic value of the package, not a claim that its re-expression or its immediate asymptotic corollaries are distinct from verified existing coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
