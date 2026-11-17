# Independent mathematical audit

## correctness

PASS

W=AD^-1 has spectrum [-1,1] via reversible similarity, so det(I-αW)>0 for 0<α<1. Tree determinant equals matching polynomial, adjugate and Neumann recurrence yield exact numerator coefficients. Exhaustive NetworkX nonisomorphic-tree representatives 1,1,2,3,6,11,23,47,106,235 for n2..11 tested with exact Fractions; interval Descartes sign variation <=1 for every pair n<=10. For n11 exactly 30 pairs are Descartes candidates; independent symbolic exact root counting after removing forced endpoint factors leaves exactly 3 actual two-crossing pairs, one automorphism orbit (3,10),(4,10),(5,10) in one tree. Witness F(α)=3α^6+4α^5-18α^4-16α^3+26α²+12α-12 has exactly two interval roots by sign samples/Descartes. Fresh independent n2..11 census and exact witness rational evaluations reproduced all counts; any roots at 0 or1 were excluded.

## originality

PASS

General PageRank damping dependence (Boldi 2005), arbitrary rankings (Bressan/Peserico 2010), and directed-network rank reversals (Son 2012) precede the study, but no checked source covers the precise first repeated crossing cutoff on undirected trees or the unique 11-node pair orbit. Katz centrality related result does not imply degree-normalized PageRank.

## value

PASS

Sharp graph-order boundary for double PageRank ranking reversals and unique witness classification is a motivated exact structural invariant showing limits of damping robustness on the simplest connected graphs. Full finite census is meaningful, not an arbitrary small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
