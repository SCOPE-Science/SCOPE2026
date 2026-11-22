# Independent mathematical audit

## correctness

PASS

The complete-pair Gini seminorm admits an exact binary-cut reduction by layer cake and triangle inequality for every real input. The read RESULT.md proves the leakage identity with F(u1,u2)=u1²+2u1u2+2u2² and an all-n endpoint imbalance case split d in {-2,-1,0,1,2}; the second-coordinate spike saturates the n>=9 bound. Independently enumerated all 2^n-2 cuts for each n=2..11, reproducing rational sharp coefficients 0,1/2,1-1/(2 floor(n²/4)) at n=4..8 and 1+(n-9)/(4(n-1)) at n=9..11. Source script check_exact.py exhaustively covers n<=16, but it was inspected, not presumed run. Universal n>=9 is established analytically, not by enumeration.

## originality

PASS

Hopf oscillation/Dobrushin total-variation coefficients are not the primal all-pair Gini seminorm. A different published complete-pair Gini theorem for half-lazy walks on balanced bicliques gives contraction <=3/4, but has different graph and exact coefficient; continuous-time heat results also do not determine a fixed discrete Euler step. The sharp reflecting-path formula and optimizer transition therefore pass best-of-knowledge distinctness.

## value

PASS

The exact induced seminorm of a standard path Markov smoother identifies the sharp threshold n=10 for Gini amplification, optimizer switch at n=9 and limiting gain 5/4, distinguishing unweighted pair dispersion from usual Markov contractions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
