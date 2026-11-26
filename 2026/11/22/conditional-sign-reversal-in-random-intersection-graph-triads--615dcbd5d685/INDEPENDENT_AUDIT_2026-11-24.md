# Independent mathematical audit

## correctness

PASS

For one attribute, an empty triad has probability a, each specified singleton edge probability b=p^2(1-p), and the full triangle probability p^3. Thus u=a+b and v=a+2b give u^2-av=b^2>0, while direct subtraction gives u-v^2=p^3(1-p)>0. Multiplication over the independent attributes gives B^2>AC and B>C^2. Inclusion–exclusion gives the stated per-pattern masses; using joint and marginal zero probabilities in the two conditional rows yields exactly the three displayed covariance formulas. In the present-edge row, put r=B/C. Since A/B and C are both smaller than r<1, (B-A)(1-C)>B(1-r)^2>C^2(1-r)^2=(C-B)^2. Both rows have positive total mass. At p=1/2 and m=1, the per-pattern masses are (1/2,1/8,0,1/8), giving 1/16, -1/36, and 1/4. Increasing maps of the independent membership bits preserve association by Harris's inequality. The absent-edge lattice minor AC-B^2 is strictly negative even when some masses vanish, excluding MTP2 on the triad and hence on the full edge vector by marginalization. Positive product edge activities multiply both terms in each conditional determinant by the same positive factor before row normalization.

## originality

PASS

The distinct result is the strict conditional sign classification for every finite sequence of attribute probabilities, including the resulting association/MTP2 separation in this model. Prior clustering calculations contain substantial triad probability information; neither the compared clustering results nor the closest local dependence results establish the two opposite strict conditional covariance signs for the same pair uniformly in heterogeneous probabilities. The determinant tilt rule and MTP2 marginalization are standard and not separately original.

## value

PASS

Three vertices are the smallest graph on which this contrast in dependence can be posed. The classification is uniform over every finite number of latent attributes and every admissible heterogeneous probability vector; it identifies exactly how fixing a third edge changes the dependence of the same two observables. It also gives a model-wide obstruction to applying stronger MTP2-based conditional conclusions, despite association, and a robust sign under changes of the three edge activities. These are substantive finite-model conclusions, not a one-parameter plug-in or a single enumerated witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
