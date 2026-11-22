# Independent mathematical audit

## correctness

PASS

The measurement rows are Frobenius-normalized symmetric rank-one projectors with 1/2 diagonal and +/-1/sqrt2 off-diagonal components. Absence of any edge-pair makes an off-diagonal column zero, and doubling five of ten pairs reduces invertibility to the 5-by-5 unsigned incidence graph with every component odd-unicyclic. Enumeration of all C(10,5)=252 doubled-edge choices independently found 162 invertible graph choices with class counts 12,60,30,60, each with 32 singleton sign choices, hence 5184 bases. Their row-Gram determinants independently equal 1/256 for all four representatives, and independently formed exact 5-by-5 characteristic determinants passed rational Sturm tests in four graph classes; numerical symmetric eigensolver confirmed four class minimum eigenvalues: 0.075171201059 (two classes), 0.049327534803 and 0.043850023016. Exact package gives graph Schur-complement determinant polynomials and rational Sturm isolates, proving the stated ordering beyond numerics and the 2304 optimizer count.

## originality

PASS

Signless incidence and odd-unicyclic determinants are established graph facts and not the claimed novelty. The full earlier Walsh matching D-optimal theorem optimizes determinants of a different frame; it does not imply the D5 Frobenius-normalized least-eigenvalue trichotomy and two optimal graph topologies.

## value

PASS

An E-optimal (noise-amplification/conditioning) design over a natural complete finite root-system sampling set is an independently useful exact classification. The spectrum separates frames with identical determinant and makes the least-singular-value optimization nontrivial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
