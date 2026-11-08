# Third-order strong-bias adsorption response on alternating cycles

## Finding
Consider irreversible nearest-neighbor-excluding monomer adsorption on the even cycle \(C_{2m}\), \(m\ge2\). Give every even vertex one independent exponential attempt time of rate \(\lambda>0\), and every odd vertex one of rate one. A site becomes permanently occupied on its attempt precisely when no neighbor was previously occupied. Write \(J_m(\lambda)\) for the expected number of occupied sites after all attempts. With \(\varepsilon=\lambda^{-1}\), the fixed-size strong-contrast expansions through third order are
\[
J_2(\lambda)=2,
\]
\[
J_3(\lambda)=3-\frac32\varepsilon+\frac{15}{4}\varepsilon^2-\frac{63}{8}\varepsilon^3+O(\varepsilon^4),
\]
\[
J_4(\lambda)=4-2\varepsilon+\frac{10}{3}\varepsilon^2-\frac{49}{18}\varepsilon^3+O(\varepsilon^4),
\]
and, for **every integer** \(m\ge5\),
\[
\boxed{J_m(\lambda)=m\left(1-\frac{\varepsilon}{2}+\frac{5\varepsilon^2}{6}-\frac{119\varepsilon^3}{144}\right)+O_m(\varepsilon^4).}
\]
Thus the per-two-site-cell coefficients stabilize exactly from the ten-vertex cycle onward. The shorter cycles of lengths four, six, and eight are explicit exceptions. The remainder is for each fixed \(m\); no bound uniform in \(m\) is asserted.

## Assumptions and scope
The graph is a simple, labelled cycle with alternating colors and even order at least four. Each vertex makes exactly one successful-or-rejected attempt; repeated attempts would have no effect after its first. All exponential clocks are independent. After rescaling time by \(\lambda\), the even-color rate is one and the odd-color rate is \(\varepsilon\). The claimed expectations are terminal, not finite-time occupation profiles. The strong-bias limit fixes \(m\) before letting \(\varepsilon\downarrow0\).

## Proof
Let \(E_k\) be the expected terminal occupancy of an alternating path of length \(2k\) (either orientation), \(A_k\) the expectation for a path of length \(2k+1\) whose endpoints have rate one, and \(B_k\) for the corresponding path with endpoint rate \(\varepsilon\). These are rational functions of \(\varepsilon\). Initialize \(E_0=0\), \(A_0=B_0=1\). The first-attempt exponential race, deletion of the first successful site's closed neighborhood, and reflection of the remaining path yield, for every \(k\ge1\), the **exact** recurrences
\[
E_k=1+\frac{\displaystyle\sum_{j=1}^{k-1}\bigl(A_{j-1}+E_j+\varepsilon(B_{j-1}+E_j)\bigr)}{k(1+\varepsilon)},
\]
\[
A_k=1+\frac{2\left(\displaystyle\sum_{j=0}^{k-1}A_j+\varepsilon\sum_{j=1}^{k-1}E_j\right)}{k+1+k\varepsilon},
\qquad
B_k=1+\frac{2\left(\displaystyle\sum_{j=1}^{k-1}E_j+\varepsilon\sum_{j=0}^{k-1}B_j\right)}{k+(k+1)\varepsilon}.
\]
All denominators have nonzero constant terms. Comparing Taylor coefficients at \(\varepsilon=0\), direct substitution gives the following three coefficient identities for **every** \(k\ge4\):
\[
E_k=k+\frac{2-k}{2}\varepsilon+\frac{5(2k-3)}{12}\varepsilon^2-\frac{119k}{144}\varepsilon^3+O_k(\varepsilon^4),
\]
\[
A_k=k+1-\frac{k}{2}\varepsilon+\frac{5(k-1)}6\varepsilon^2-\frac{119k-122}{144}\varepsilon^3+O_k(\varepsilon^4),
\]
\[
B_k=k+\frac{3-k}{2}\varepsilon+\frac{5(k-1)}6\varepsilon^2-\frac{119k+241}{144}\varepsilon^3+O_k(\varepsilon^4).
\]
Here is a finite algebraic induction proof, not an inference from finitely many numerical tests. The recurrences directly give these three identities at \(k=4,5,6,7\). For each coefficient through degree three, substitute the displayed affine-in-\(k\) expressions for all lower indices at least four; lower indices zero through three contribute fixed constants. Multiplying the recurrence by its denominator leaves a residual polynomial in \(k\) of degree at most two: each summand of the coefficient recurrences is affine in its index, and summing such terms over a consecutive interval is quadratic. The residual is zero for \(k=5,6,7\) by the exact base calculations. A polynomial of degree at most two with those three distinct roots is identically zero. Hence every simultaneous induction step with \(k\ge8\) holds, proving all three expansions for all \(k\ge4\). The included standard-library checker exactly tests the base and interpolation identities and also cross-checks the recurrences against an independent vertex-mask algorithm. The polynomial-degree argument, rather than the finite check range, proves the arbitrary-length statement.

Finally, the first accepted event on \(C_{2m}\) occurs at a rate-one vertex with probability \(1/(1+\varepsilon)\), or at a rate-\(\varepsilon\) vertex with probability \(\varepsilon/(1+\varepsilon)\). Its deletion leaves a path of length \(2m-3\) with endpoints having the same rate as the first event. Consequently
\[
J_m(\lambda)=1+\frac{A_{m-2}+\varepsilon B_{m-2}}{1+\varepsilon}.
\]
For \(m\ge6\), substitution of the preceding path identities proves the universal cycle formula. For \(m=5\), the same identity holds because \(A_3\) has the displayed expansion through degree three and \(B_3\) has the required coefficients through degree two, as follows directly from the exact recurrences. Direct evaluation at \(m=2,3,4\) gives the three short-cycle cases above. This completes the proof.

## Verification
Run `python3 verify_rsa.py` using Python 3 and the standard library. It calculates the exact rational Taylor coefficients for alternating paths, checks the closed expressions across 33 path sizes, verifies the exceptional cycle coefficients, and compares independent full rational first-event and vertex-mask recursions at 18 rate-and-size combinations. The polynomial-degree-and-three-roots argument is explained above and in the checker. The program is an auxiliary calculation; it is not used to replace the infinite induction.

## Relationship to prior work
Penrose and Sudbury (2005) establish general deposition dynamics on graphs, including blocking RSA, with explicit calculations for other geometries. Penrose and Rosoman (2011) study exponentially rate-biased checkerboard RSA on the two-dimensional square lattice, focusing on percolation thresholds rather than strong-bias terminal coverage on finite one-dimensional rings. Fan and Percus (1991, 1992) develop general series/duality methods for RSA, but the accessible descriptions do not state these evaluated alternating-rate ring coefficients or their sharp short-cycle exceptions. Do Amaral and dos Santos (2023) study a distinct two-species antagonistic adsorption rule on the infinite line: deposition of the same particle species is not forbidden at adjacent sites. General methods are acknowledged as prior, and the claimed contribution is the explicit arbitrary-ring third-order expansion plus the finite-size stabilization threshold, not a new adsorption formalism.

## Limitations
The result covers the first three strong-bias corrections only and makes no assertion about monotonicity at all rates, about joint large-ring/large-bias scaling, or about fluctuations. Standard general RSA recurrences can in principle produce further coefficients. Historical priority beyond the examined sources has not been independently certified; earlier specialized or unindexed expansions may exist.

## References
- M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs* (first publicly available arXiv version 2005-03-24), https://arxiv.org/abs/math/0503519.
- M. D. Penrose and T. Rosoman, *Percolation of even sites for random sequential adsorption* (first publicly available arXiv version 2011-02-02), https://arxiv.org/abs/1102.0532.
- Y. Fan and J. K. Percus, *Asymptotic coverage in random sequential adsorption on a lattice*, Phys. Rev. A 44 (1991), https://doi.org/10.1103/PhysRevA.44.5099.
- Y. Fan and J. K. Percus, *Duality for Random Sequential Adsorption on a Lattice*, Combin. Probab. Comput. 1 (1992), https://doi.org/10.1017/S0963548300000250.
- C. S. do Amaral and D. C. dos Santos, *One-dimensional AB random sequential adsorption with one deposition per site* (arXiv 2023-06-16), https://arxiv.org/abs/2306.09786.
