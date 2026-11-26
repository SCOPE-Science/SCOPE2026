# Independent mathematical audit

## correctness

PASS

The horizontal and vertical coordinate steps give precisely twelve distinct transpositions. The connected site graph generates all permutations; parity changes with each move, and token relabeling gives transitivity. An independent exact layer traversal packs each placement into nine four-bit fields, swaps fields by XOR, and constructs each next set as all legal neighbors not yet seen. Induction makes each layer the set at its stated minimum distance. Enumeration reaches all 9! placements, reproduces every claimed layer, and terminates with only 876543210 at depth 16. Relabeling the identity by p transports that last state to p composed on the right with the positional half-turn. This involution has no fixed configuration and pairs the states, giving 181440 unordered diametral pairs; transitivity gives radius 16. Each swap moves two tokens one edge and hence can reduce the total Manhattan distance by at most two. Computing the bound on every reached state reproduces the full six-bin excess distribution, with twenty maximizing states at excess five.

## originality

PASS

The exact graph and its shortest-path computation by BFS are already the CSES Swap Game. The supported distinct contribution is not the model, search procedure or standard displacement bound, but the exact extremal and census results, especially the unique geometric maximizer and the complete quantitative deficit of the displacement bound. The strongest inspected same-model sources solve a given input and do not supply the claimed extrema and histograms.

## value

PASS

The established Swap Game is a natural fixed routing benchmark rather than an arbitrary subset of states. The all-state diameter gives its exact worst routing budget, while the unique half-turn identifies the configuration needed to test the extremal case. The second census independently measures sharp error of a standard lower bound (including the number of maximizers), giving exact benchmarks for pruning and lower-bound improvements beyond rerunning one known puzzle input. Value belongs to these precise invariants, not to the textbook use of BFS.

The dated certificate retains the supplied scientific assessment, sources and limitations.
