# Sharp six-cell onset and seven classes of nonresonant double-Hopf network spectra

## Finding
Let \(A\) be the adjacency matrix of an \(n\)-cell homogeneous directed multigraph with exactly two incoming arrows of one type per cell; entries are nonnegative integers and each row sums to \(2\). A *nonresonant double-imaginary spectrum* means that \(A\) has two *distinct* conjugate pairs \(\pm i\omega_1,\pm i\omega_2\), with positive \(\omega_1\ne\omega_2\) and irrational \(\omega_1/\omega_2\). At the minimal size \(n=6\), exactly seven unlabeled networks have this property. The complete spectra and counts are:

| Characteristic polynomial | Nonzero frequency ratio (greater/smaller) | Labeled matrices | Isomorphism classes |
|---|---|---:|---:|
| \((z^2-4)(z^4+3z^2+1)\) | \((3+\sqrt5)/2\) | 720 | 1 |
| \((z^2-4)(z^4+3z^2+2)\) | \(\sqrt2\) | 3600 | 5 |
| \((z^2-4)(z^4+4z^2+2)\) | \(1+\sqrt2\) | 720 | 1 |

Each of the seven classes has trivial vertex automorphism group and is strongly connected and period-two bipartite. No network of five or fewer cells has two nonzero purely imaginary pairs. Hence six cells is the sharp size threshold for this double-Hopf *linear spectral coincidence*. For example,

\[
A=\begin{pmatrix}0&0&0&2&0&0\0&0&0&0&0&2\0&0&0&1&1&0\0&1&1&0&0&0\1&1&0&0&0&0\2&0&0&0&0&0\end{pmatrix}
\]

has characteristic polynomial \((z^2-4)(z^4+3z^2+2)\) and is strongly connected.

## Assumptions and scope
All integer adjacency matrices are allowed, including repeated incoming arrows and self-arrows. Isomorphism means simultaneous relabeling of rows and columns, i.e. \(A\mapsto P A P^-1\) for a permutation matrix. The count does not distinguish formal ordering of two indistinguishable inputs, and it does not impose symmetry of outgoing degrees. The spectral property concerns the adjacency and hence the linearizations of scalar-cell smooth admissible ODEs. It does not imply nonlinear invariant tori or classify their unfoldings.

## Proof
**Size obstruction.** Since every row sums to \(2\), \(2\) is an eigenvalue. Fewer than five dimensions cannot accommodate it and two imaginary pairs. In dimension five, the characteristic polynomial would have to be \((z-2)(z^4+Sz^2+P)\), where \(S=\omega_1^2+\omega_2^2\) and \(P=\omega_1^2\omega_2^2\) are positive integers by integrality of the characteristic polynomial. The arithmetic-geometric mean inequality gives \(S\ge 2\sqrt P\ge2\). The trace is \(\operatorname{tr}A=2\), hence \(\operatorname{tr}A^2=4-2S\le0\). But \(\operatorname{tr}A^2\ge\sum_i A_{ii}^2\ge\sum_i A_{ii}=2\), a contradiction.

**Forced bipartite spectral factor.** For six cells, two distinct imaginary pairs force the remaining real eigenvalue to be an integer \(r=\operatorname{tr}A-2\), and
\[
\chi_A(z)=(z-2)(z-r)(z^4+Sz^2+P).
\]
The coefficients \(S,P\) are positive integers. Distinct positive squared frequencies require \(S^2>4P\), so \(S\ge3\). Since \(A\) is nonnegative with row sum two, all eigenvalues have modulus at most two, hence \(-2\le r\le2\). Also
\[
4+r^2-2S=\operatorname{tr}A^2\ge\operatorname{tr}A=2+r,
\]
which forces \(r=-2\) for every integer \(r\) in this range. Consequently all admissible spectra factor as \((z^2-4)(z^4+Sz^2+P)\), have trace zero (hence no self-loops), and \(S\in\{3,4}\) because \(\operatorname{tr}A^2=8-2S\ge0\).

**Exact finite classification.** Every row of a six-by-six valency-two adjacency matrix is one of \(\binom{7}{2}=21\) unordered multisets of two incoming vertices. The exact checker `CHECKER.cpp` enumerates all \(21^6=85,766,121\) matrices once. It uses integer Faddeev–LeVerrier coefficients and keeps a matrix if and only if its polynomial has the required factorization with \(S,P>0\) and \(S^2>4P\). It independently calculates reachability for directed strong connectivity and exact canonical representatives under all \(6!=720\) simultaneous relabelings. The complete accepted table contains exactly the three polynomials above; the three labeled counts are \(720,3600,720\), with one, five, one canonical classes, all strongly connected, and each orbit has size \(720\). This is a finite exhaustive proof, not an inference from a sample.

**Reduced independent count.** The discovered strong connectivity, the eigenvalue \(-2\), and Perron–Frobenius periodicity imply a bipartition of period two. Since \(\det A\ne0\), the two vertex classes each have size three and, after relabeling, \(A=\begin{pmatrix}0&B\C&0\end{pmatrix}\), where each \(3\times3\) nonnegative integer row of \(B,C\) sums to two. The reduced checker `CROSSCHECK.py` independently enumerates the \(6^6=46,656\) ordered block pairs and uses integer invariants of \(BC\) to recover counts \(72,360,72\) for the same three polynomials per fixed ordered bipartition. There are ten unordered three-plus-three bipartitions, giving precisely \(720,3600,720\) labeled networks; uniqueness of the bipartition follows from strong connectivity. The reduced count independently reproduces the full enumeration.

**Dynamical meaning.** If an admissible smooth scalar coupling is \(f(u;v,w;\mu)=\mu u +b(v+w) -u^3\) with \(b>0\), then at its synchronous equilibrium the Jacobian is \(\mu I+bA\). At \(\mu=0\) the two distinct imaginary pairs cross transversely and simultaneously with derivative one. The remaining eigenvalues \(2b,-2b\) make the full equilibrium saddle-type. This is a network-forced simultaneous imaginary-spectrum crossing, not a claim about a generic nonlinear double-Hopf normal form.

## Verification
Compile `CHECKER.cpp` with `g++ -O3 -std=c++17 CHECKER.cpp -o checker` and execute `./checker`. It prints seven total spectral strata (four additional equal-frequency or disconnected strata), and three strictly unequal-frequency strata with the exact labeled and isomorphism counts above. Run `python3 CROSSCHECK.py` for an independent fixed-bipartition enumeration. A third exact symbolic computation on the displayed witness gives \((z-2)(z+2)(z^2+1)(z^2+2)\). Both included checkers ran successfully. No floating-point root test is used to decide spectral membership.

## Relationship to prior work
Aguiar, Dias and Mokhtari (2026) introduce the spectral network bifurcation framework and classify **four-cell zero-Hopf networks**, defined using one zero eigenvalue and one imaginary pair. That question is different from the two *distinct* imaginary pairs here, and their study does not present these six-cell double-imaginary spectra or counts. The established broader Hopf–Hopf theory for coupled-cell networks includes different network types, dimensions and mode structures; the assertion here is limited to this exact homogeneous, indistinguishable-input valency-two family and the sharp first-size spectral census.

## Limitations
The claims are about spectra, enumeration and a linear crossing, not the nonlinear emergence of cycles or tori. Counts are only for six cells and depend on allowing repeated arrows, as in the source's adjacency conventions. The exact enumeration is reproducible with the two independent methods; historical priority outside indexed or inspected literature remains open. No independent mathematical audit has been performed.

## References
1. M. Aguiar, A. Dias, F. Mokhtari, *Zero-Hopf Networks*, arXiv:2611.15221v1, first posted 2026-11-11. https://arxiv.org/html/2611.15221v1
2. B. Rink and J. A. Sanders, *Coupled cell networks: semigroups, Lie algebras and normal forms*, Trans. Amer. Math. Soc. 367 (2015), 3509–3548. https://arxiv.org/abs/1209.3209
