# Scientific review: uniform symmetric-group homology of two-subset Kneser neighborhood complexes

## Correctness — PASS

For every integer \(n\ge5\), simplex membership is equivalent to an edge set on \([n]\) having at least two isolated vertices. The signed chain-Lefschetz contribution of a set fixed by a permutation is \((-1)^{o(F)-1}\), with \(o(F)\) its edge-orbit count. The complete Boolean-lattice inversion in RESULT.md yields the excluded-face sum \((-1)^c(f^2-3f+1)\); hence the top-degree character is \(\operatorname{sgn}(\sigma)(f^2-3f+1)\). The independent, previously established nonequivariant theorem [3] supplies concentration in degree \(n-4\). The standard pair-permutation and exterior-square character identities yield the stated multiplicity-one rational Specht decomposition. Averaging then proves rationally acyclic full- and alternating-group quotients. Independent finite exact checks reproduce the character for 85 permutation cycle types through \(n=9\), including chain-orientation trace cross-checks for \(n=5,6\). The infinite result follows from proof rather than extrapolation.

## Originality — PASS on inspected evidence

The 2018 theorem [3] supplies the exact same nonequivariant homotopy type but does not supply the group representation. A previously indexed exact calculation [4] already determines the representation at \(n=6\), which is explicit prior coverage and is **not** claimed independently new. The 1997 representation theorem [1] concerns the larger, different complex of graphs that are not two-connected and does not imply the character here; the 2011 stable Kneser complexes [2] have a different graph and symmetry. Targeted research-index and literature searches sought full \(S_n\)-characters, two-isolated-vertex formulations, larger-covering graph complexes and quotient descriptions. None of the available statements implies the uniform all-\(n\) polynomial, decomposition or quotient vanishing. The exact six-label source was only indexed and its full text unavailable; equivalent unindexed work remains possible. These limitations preclude claiming definitive priority.

## Mathematical value — PASS

The previously known sphere count cannot recover the module structure or group-quotient homology. This result uniformly identifies exactly two rational irreducible families and determines quotient acyclicity for a natural Kneser family across arbitrary sizes, rather than a one-graph table recomputation. The proof additionally clarifies a structural link between graph-edge supports and equivariant Lefschetz counting.

## Limitations and reproducibility

The statement is rational, not an integral-lattice or equivariant-homotopy classification. Finite checks via `python3 verify.py` use the Python standard library; `verification_output.txt` records their exact outcomes. The literature comparison acknowledges incomplete material access to the indexed six-point source. Independent mathematical audit and publication-priority certification are not performed.

Self-review: passed. Independent audit: not yet performed.
