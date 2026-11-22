# Independent mathematical audit

## correctness

PASS

For the loopless degree-normalized walk on K_c join independent K_s, the clique degree is d=c+s-1 and independent degree c. A cut selecting a clique vertices and b independent vertices maps the clique values to (a+b-1)/d for selected and (a+b)/d for unselected, while every independent vertex maps to a/c. The exact output complete-pair Gini F_a(b) is convex in b, and target (s/d)(a+b)(N-a-b) is a concave quadratic; their two endpoint deficits equal a(c-a)(s-1)/d and its chord surplus is s*b*(s-b)/d. This proves the two-deficit inequality for all binary cuts, then nested level sets plus the Gini layer-cake identity and triangle inequality establish it for every real f. The class-contrast signal 1_I has quotient eigenvalue -s/d, so the exact norm of every power is (s/d)^m. Equality rigidity follows from nonnegative within-class deficits for s>=2, and s=1 gives complete graph scalar -1/c on the quotient. The separate sharpness of each deficit coefficient is witnessed by a single vertex in each class when c,s>=2. Independent enumeration checked 3,794 labelled cuts for c,s<=5. This finite check is not the all-size proof.

## originality

PASS

Ipsen–Selee surveys ergodicity coefficients defined through ordinary vector p-norms and De Pasquale et al. develops general induced incidence seminorms, neither evaluates the two sharp classwise Gini deficits for this particular degree-normalized split walk. Published results on optimizing other split-graph kernels or Gini variation on half-lazy bipartite graphs concern different maps/objectives and do not dominate the fixed P theorem. The all-power exact norm and equality rigidity follow here by a nontrivial cut deficit plus spectral witness.

## value

PASS

This is an exact all-size all-positive-power stability law for a canonical Markov operator on a degree-heterogeneous graph family, with two separately sharp within-community dissipation gains and complete equality rigidity. It distinguishes c=1 noncontraction from strict contraction for c>=2 and quantifies how clique-vs-independent oscillations dissipate. Such structural sharp estimates give more information than the spectral gap or a routine generic ergodicity bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
