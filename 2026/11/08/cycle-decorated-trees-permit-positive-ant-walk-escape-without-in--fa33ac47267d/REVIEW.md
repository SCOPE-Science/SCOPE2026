# Independent mathematical audit

## correctness

PASS

For a strictly outward path the newly reached level-i gate has exactly b_i unvisited children and two unused private-cycle neighbors (all directed weights 1); when i>=1 the just-used parent edge has reverse signed crossing -1 and weight exp(-beta), while at root there is no parent. Multiplication gives P(E)=b_0/(b_0+2)*product_{i>=1} b_i/(b_i+2+exp(-beta)). Because 2+exp(-beta) lies between 2 and 3, the logarithms of factors are comparable to 1/b_i; continuity for nested cylinder events gives the infinite-product iff. The infinite graph is locally finite, and on E the tree depth and graph distance grow exactly one at each step. With b_i=2^(i+2), sum_{i>=1}1/b_i=1/4 and the log inequality gives (2/3)exp(-3/4)>0. Every vertex lies on a private cycle, including frontier vertices; the proof does not require increasing cycle length.

## originality

PASS

No inspected stronger work implies positive escape with every vertex lying in a finite cycle and constant triangle attachments; the motivating ant-walk paper poses a closely matching construction heuristically rather than proving it. Exact outward-event product/positive branching criterion are additional explicit statements, with unindexed priority risk.

## value

PASS

Constructs a mathematically motivated counterexample to the apparent necessity of an infinite leaf for ant-walk escape, precisely in a graph where every vertex is on a finite cycle. Its universal beta bound and sharp reciprocal branching criterion for the monotone event reveal which aspect of tree growth defeats reinforcement; constant triangle blocks strengthen the motivating heuristic. This is a structural witness and threshold result, not an unmotivated instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
