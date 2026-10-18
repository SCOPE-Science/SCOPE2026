# Affine rigidity of binary 2 by 3 maximum-rank-distance codes
## Finding
In the rank metric on \(\mathbb F_2^{2\times3}\), every code \(C\) with \(\operatorname{rank}(A-B)\ge2\) for all distinct \(A,B\in C\) has \(|C|\le8\). Exactly \(384\) labeled size-eight codes attain equality, and every one is an affine \(3\)-flat. Exactly \(48\) equality cases contain the zero matrix; these are linear \(3\)-dimensional MRD subspaces, and they form one orbit under \(\operatorname{GL}_2(\mathbb F_2)\times\operatorname{GL}_3(\mathbb F_2)\), with stabilizer order \(21\).

A representative zero-containing maximum is
\[
\left\{\begin{pmatrix}0&0&0\\0&0&0\end{pmatrix},
\begin{pmatrix}0&1&0\\1&0&0\end{pmatrix},
\begin{pmatrix}0&0&1\\0&1&0\end{pmatrix},
\begin{pmatrix}0&1&1\\1&1&0\end{pmatrix},
\begin{pmatrix}1&1&0\\0&0&1\end{pmatrix},
\begin{pmatrix}1&0&0\\1&0&1\end{pmatrix},
\begin{pmatrix}1&1&1\\0&1&1\end{pmatrix},
\begin{pmatrix}1&0&1\\1&1&1\end{pmatrix}\right\}.
\]
Every nonzero difference inside this set has rank \(2\).

## Assumptions and scope
Matrices are labeled \(2\times3\) matrices over \(\mathbb F_2\). The rank distance is \(d_R(A,B)=\operatorname{rank}(A-B)\). Codes are arbitrary subsets; linearity or additivity is not assumed. “Affine” means a translate of a binary linear subspace of the six-dimensional ambient vector space. The orbit statement uses the natural left-right action \(M\mapsto AMB\) of \(\operatorname{GL}_2(\mathbb F_2)\times\operatorname{GL}_3(\mathbb F_2)\) on zero-containing linear codes.

## Proof
Delete either one of the two rows of every codeword. If two codewords have the same surviving row, their difference is supported in one row and has rank at most \(1\), contradicting the distance condition. Thus puncturing one row is injective into \(\mathbb F_2^3\), so \(|C|\le2^3=8\). This is the rectangular rank-metric Singleton bound in this parameter.

For equality classification, form the graph on all \(64\) binary \(2\times3\) matrices, joining two distinct matrices exactly when their difference has rank \(2\). An equality case is exactly an eight-clique. Exact Bron–Kerbosch enumeration gives \(384\) such cliques. Exactly \(48\) contain zero, and direct closure testing shows that every one of those \(48\) sets is closed under binary addition. Hence each is a three-dimensional linear subspace. Independently, enumerating all \(1395\) three-dimensional subspaces of \(\mathbb F_2^6\) finds exactly the same \(48\) subspaces whose seven nonzero elements all have matrix rank \(2\).

Each of those \(48\) linear spaces has exactly eight affine cosets. Direct coset generation gives \(384\) distinct sets, exactly the complete clique census. Therefore every maximum code is affine. Finally, the verifier enumerates all \(6\) elements of \(\operatorname{GL}_2(\mathbb F_2)\) and all \(168\) elements of \(\operatorname{GL}_3(\mathbb F_2)\). The left-right orbit of the displayed representative contains all \(48\) linear equality cases, and its stabilizer has order \(21\).

## Verification
Run `python3 artifacts/verify.py`. The program uses only the Python standard library and reconstructs the \(64\)-vertex rank-distance graph from binary Gaussian elimination. It exhaustively enumerates all maximum cliques, independently enumerates all three-dimensional binary subspaces, compares both lists, generates all affine cosets, and recomputes the complete left-right group orbit. The saved output in `artifacts/verification_output.txt` ends with the exact counts stated above.

## Relationship to prior work
Delsarte introduced the rank metric on bilinear forms and proved the corresponding Singleton bound, together with linear Singleton-system constructions for all parameters. Specializing his bound to \(2\times3\) binary matrices and minimum rank distance \(2\) gives the size bound \(8\), but the inspected paper does not classify all equality cases or assert that every nonlinear candidate is affine. Later work demonstrates that genuinely non-additive or non-affine MRD codes occur in broader parameter ranges, so affinity is not a formal consequence of merely attaining the rank-metric Singleton bound. The result here isolates a small binary rigidity boundary: at this parameter every unrestricted optimum collapses to one affine type.

## Limitations
The classification is finite and only concerns \(\mathbb F_2^{2\times3}\) at minimum rank distance \(2\). The group orbit statement is for the stated natural left-right linear rank isometries; no separate claim about all abstract automorphisms is needed. The exhaustive computation proves the complete finite classification for this domain, but literature searches cannot exclude an obscure or unindexed prior enumeration, which remains the principal originality risk.

## References
1. Ph. Delsarte, “Bilinear Forms over a Finite Field, with Applications to Coding Theory,” *Journal of Combinatorial Theory, Series A* 25 (1978), 226–241, doi:10.1016/0097-3165(78)90015-8.
2. A. Cossidente, G. Marino, and F. Pavese, “Non-linear maximum rank distance codes,” *Designs, Codes and Cryptography* 79 (2016), 597–609, doi:10.1007/s10623-015-0108-0.
3. K. Otal and F. Özbudak, “Some new non-additive maximum rank distance codes,” *Finite Fields and Their Applications* 50 (2018), 293–303, doi:10.1016/j.ffa.2017.12.003.
