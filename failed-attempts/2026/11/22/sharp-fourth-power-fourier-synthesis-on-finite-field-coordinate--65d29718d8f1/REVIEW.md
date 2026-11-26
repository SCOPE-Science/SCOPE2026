# Independent mathematical audit

## correctness

PASS

With the counting norm and the stated unitary DFT, modulation at a maximizing frequency and rescaling reduce the quotient to minimization at Fourier value 1 at zero (source mass q). Strict convexity and the independent coordinate dilations and swap force the unique constrained optimizer onto the two support orbits, also for q=2; orthogonality works for any nontrivial additive character and every prime power. If r=q−1, the three Fourier classes have values 1,U,V with 2U−V=1 and multiplicities 1,2r,r². Weighted Hölder gives 1≤(2r|U|⁴+r²|V|⁴)^(1/4)(2r^(−1/3)+r^(−2/3))^(3/4); equality at U=r^(1/3)/(1+2r^(1/3)), V=−1/(1+2r^(1/3)) proves the minimum and fixes phases. Both magnitudes are below 1, so this constrained optimizer attains the original quotient. Inverting the two-level transform gives precisely the mass-q seed, and undoing the normalization gives all modulated and scaled optimizers. The central numerator 2+2(q−1)^(1/3)−q decreases for real q≥2 and changes sign between 5 and 6; 6 is not a prime power. The nonconstant norm term is asymptotic to q/8. The supplied artifacts/check_certificate.py was inspected (character transforms and finite perturbations only) and not run; it is not needed for the exact proof.

## originality

FAIL

Demonstrably equivalent distinct indexed finding: assigned record 2 has the identical theorem, including all complex equality cases. The seed is divided by q to fix source mass 1 rather than q; the quotient, scope, center-sign law and asymptotic are unchanged. This is a finding-level overlap decision, not evidence that either same-date record was first or that either was copied. Two additional same-day indexed generalizations also report scopes covering this case, with full statement details and chronology not verified.

## value

PASS

As mathematics, this is a natural sharp invariant in a basic nontransitive support family. The optimizer's center sign switch and full equality classification are useful beyond obtaining a numerical norm, and are not mechanical consequences of the older transitive theorem. This is value of the common theorem, not a separate contribution over record 2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
