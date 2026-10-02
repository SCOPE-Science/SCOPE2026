# Review status

Mathematical audit date: 2026-10-01 UTC.

Disposition: **failed**.

Correctness: PASS. If at least one part is non-singleton, three or more white vertices cannot be completely forced, while leaving one white vertex in each of two distinct parts is forceable; hence the zero forcing number is \(N-2\). The general size-\(N-2\) forcing criterion specializes to exactly the pairs in distinct parts, except a pair consisting of two singleton parts, giving coefficient \(\sum_{i<j}n_i n_j-\binom{s}{2}\). Every \(N-1\) subset is forcing in a connected graph, and the full set is forcing, yielding the stated polynomial. The complete-graph case gives \(Nx^{N-1}+x^N\). Repository enumeration agrees on all tested multipartite types.

Originality: FAIL. Boyer et al.'s full primary paper already proves a general theorem for every graph giving \(z(G;N)=1\), \(z(G;N-1)\), and, crucially, an exact neighborhood criterion for \(z(G;N-2)\). The same paper explicitly discusses complete multipartite graphs in its zero-forcing-polynomial context. For a complete multipartite graph, substituting its neighborhood classes into that theorem gives exactly the assigned coefficient: cross-part pairs qualify except pairs of singleton parts. The fact that no smaller set can force when a non-singleton part is present is the standard elementary computation \(Z(G)=N-2\) for this class. Thus the entire polynomial is mechanically determined by established theory.

Scientific value: FAIL. Once the general \(N-2\) coefficient theorem and the elementary complete-multipartite zero-forcing number are in hand, the claimed polynomial is a one-line specialization and bookkeeping count. It is useful as an example but does not clear the stated value bar against routine deductions from an existing graph-polynomial theorem.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
