# Independent mathematical audit

## correctness

PASS

Fixed recovery equations yield x2=gamma and independent G_i(x_i)=d_i with G_i=x-A_i x^2 exp(-Kx); each derivative has at most two positive zeros, giving at most 3 positive roots per outer neuron. Reconstructed full six-variable Jacobian characteristic determinant Q1 Q2 Q3-(lambda-a)(lambda-1)(s1 t1 Q3+s3 t3 Q1). At lambda=1 the two G_i derivatives determine the sign, and with two descending branches the largest >1 root of a Q_i forces a real spectral root >1; at most two ascending roots per outer neuron can be sinks. At rational witness the three root positions are 0.0020489380177,0.0923303627250,2.1888643904714; independent full Jacobian eigensolver across all nine pairs gives precisely four spectral radii <1 (about 0.9141) and five >1 (about 1.8587). Read original check.py exact-rational exponential enclosure and Rouché strict 0.00011239816 < 0.0005184; the rigorous universal result comes from sign/root arguments, not the numerical eigenvalue check. At folds eigenvalue 1 excludes hyperbolic sinks. No global basin theorem.

## originality

PASS

The named 2024 origin paper already gives the exact chain and steady-state reduction; reduction is NOT new. Its inspected Sections 3–5 study numerical fixed points and bifurcations, not sharp all-positive-coupling nine/four ceilings and an exact four-sink rational witness. An indexed three-node different-coupling system and isolated Chialvo models have different maps; no implication to this all-parameter six-dimensional ceiling. This is best-of-knowledge, not novelty certification.

## value

PASS

The natural coupled-neuron equilibrium/multistability counting question is unresolved by the founding numerical scan; ruling out stabilization of decreasing branches for arbitrary return couplings and attaining four coexisting local sinks in a positive bidirectional example is a nontrivial network constraint, useful for phase studies without claiming biological efficacy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
