# Independent mathematical audit

## correctness

PASS

Adding and subtracting the two log-swap equations gives (1−a)(X−Y)=2z and (1+a)(X+Y)=2ρ, where z=log(X/Y)>0. The ratio (X−Y)/(X+Y)=tanh(z/2) yields ρ=(1+a)C(z)/(1−a), whose strict increase from 2(1+a)/(1−a) establishes exactly the existence and uniqueness domain. At the first phase, the symmetry-reduced Jacobian P·DF has trace −aS and determinant −D, with S=X+Y and D=1−S+(1−a²)XY. The two-step derivative is its square. The quadratic Schur conditions reduce to 1+D>0 and 1−aS−D>0; the third follows as aS>0. Since S/(XY)=(1−a)sinh(z)/z and J=Cz/sinh(z), the inequalities become exactly a<A(z) and C−(1+a)J<1−a. A and C increase strictly while J decreases, giving unique boundaries. At z₋ the latter left side is aC, so the window closes only where A=1/(1+C), an intersection of strictly opposed curves. At the lower endpoint the reduced root is −1 with the other in (−1,1); at the upper endpoint D=−1 and 0<aS<2 for each nonempty window, so the reduced roots are conjugate unit-modulus with nonzero real part and their squares are also a conjugate pair. At collision the reduced polynomial is (λ+1)². A bounded independent numeric evaluation using the equivalent collision equation cosh(z)−1=C(z) gives z≈1.953977972619354 and a≈0.277839040264087. The frozen witness satisfies the exact swap equations, and the positive-term log(4) series with its geometric tail bound validates its two strict Schur inequalities.

## originality

FAIL

The distinct Resultary record c3fcc7a39530 covers the same existence, uniqueness, full attracting window, universal cutoff and spectral mechanism, under an invertible change of variables. It even gives the same exact attracting witness. This is demonstrated equivalent catalogue coverage, not identification with the frozen record itself or a claim about who proved it first. The comparator's indexed path is dated November 2, whereas the assigned source path is dated October 19; these labels do not establish historical priority or derivation.

## value

FAIL

A sharp global-in-parameters classification of this local exchange mode is mathematically useful in itself. In the reviewed record it adds no independently useful exact result beyond the equivalent measured-amplitude classification already in the catalogue: the entire window, collision, boundary spectra and even the rational-logarithmic witness are there or follow immediately. The change of variables and an alternative certificate for the same witness are not enough for a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
