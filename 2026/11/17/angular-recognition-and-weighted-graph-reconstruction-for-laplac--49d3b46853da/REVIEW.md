# Independent mathematical audit

## correctness

PASS

For connected weighted graph L, Q=L† satisfies QL=I-11^T/n. Thus inward facet normals to conv{Le_i} are Qe_i, and their normalized Gram matrix is C=D_b^-1 Q² D_b^-1 with positive null vector b_i=||Qe_i||. For a=t b one recovers K=D_a C D_a=t²Q², and (K†)^1/2=t^-1 L by spectral calculus, proving necessity, edge weights and uniqueness up to scale. Conversely a rank n-1 PSD cosine candidate C with diag 1 and positive null vector produces R=(K†)^1/2 PSD, row sums zero, and offdiag <=0 implies exactly a connected weighted graph Laplacian. Its facet Gram reconstructed from (R†)²=K returns C, proving sufficiency. Explicit four-path L† and Q² computed in the frozen proof show Q²_{12}=7/16>0 and interior dihedral cosine -7/sqrt(105), establishing that the criterion is not the standard hyperacute/simplex Gram criterion. Checked the submitted checker.py source, which numerically covers 770 connected n<=5 graphs with two weightings each; this is only finite stress testing of an all-dimensional spectral proof.

## originality

PASS

Braun–Meyer 2017 defines and studies the graph Laplacian-column simplex for lattice/Ehrhart properties. Devriendt and Van Mieghem 2018 and Devriendt 2020 characterize a different graph-simplex representation whose vertex Gram matrix equals L; they give the general pseudoinverse angle relation. Here the column simplex has vertex Gram L² and the inverse operation is the positive matrix square root of the pseudoinverse of a rescaled normal Gram. The two sign tests differ, with an explicit obtuse path example. No inspected full source states this exact all-dimensional weighted edge/conductance reconstruction from angle data. Claim is a novel combination beyond only renaming a known standard Laplacian simplex; residual risk of an implicit general result is acknowledged.

## value

PASS

Recovering a weighted connected graph including its zero pattern and all relative edge conductances from geometric facet-angle observations is a natural inverse problem. The if-and-only-if PSD sign criterion and unique reconstructed edge data are reusable in spectral graph geometry and distinguish a genuinely non-hyperacute class. The proof is analytic for all graph orders and not merely n<=5 enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
