# Independent mathematical audit

## correctness

PASS

For independent Y1,Y2~XLindley(theta), let Ni|Yi~Poisson(Yi) independently. Conditional Poisson additivity proves N in law equals N1+N2 and G_PTS(z)=G_PXL(z)^2. The source’s exact squared PGF confirms identity. Mixed-Poisson total variance Var N=E(Y1+Y2)+Var(Y1+Y2)>EN for any nondegenerate finite theta, so DI>1. Independent symbolic algebra confirmed printed rational formula DI(theta)-1=(theta^4+4theta^3+8theta^2+8theta+2)/(theta(1+theta)^2(theta^2+2theta+2))>0 and EN~2/theta as theta→infinity; dispersion approaches 1 only as mean tends to 0. Holds theta>0, not an assertion about observed sample dispersion.

## originality

FAIL

FAIL: the 2026 originating paper explicitly defines the mixing variable as the sum of iid XLindley variables and prints the squared PGF; the 2022 PXL model already is a Poisson–XLindley mixture. Classical Poisson additivity immediately implies the self-convolution, while generic mixed-Poisson total variance automatically gives strict overdispersion of any nondegenerate mixture. These are direct consequences of stronger published definitions, despite no verbatim use of the phrase self-convolution. Thus it is not independently original.

## value

FAIL

FAIL: the convolution and variance are standard textbook deductions from the source generative model and existing PXL family; the statement adds no motivated nontrivial invariant, bound or boundary beyond a routine positivity check. While interpretation of equidispersion is useful pedagogy, it does not survive the scientific-value bar as an independent finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
