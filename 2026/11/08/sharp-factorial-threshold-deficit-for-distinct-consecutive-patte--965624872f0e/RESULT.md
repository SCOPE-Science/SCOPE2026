# Sharp factorial-threshold deficit for distinct consecutive patterns in a random permutation

## Finding
Let \(\Pi_n\) be a uniform random permutation of \(\{1,\ldots,n\}\). Let \(X_n\) be the total number of *different* relative-order patterns occurring in consecutive blocks of \(\Pi_n\), summed over all lengths from \(1\) through \(n\). Count patterns of different lengths as different, and do not count the empty pattern. As \(n\to\infty\),
\[
\boxed{\mathbb E X_n=\frac{n(n+1)}2-(1+o(1))\frac{n\log n}{\log\log n}.}
\]
Equivalently, the expected loss \(D_n\) from the number of available consecutive blocks has the sharp limit
\[
\boxed{\lim_{n\to\infty}\frac{D_n\log\log n}{n\log n}=1,\qquad D_n:=\frac{n(n+1)}2-\mathbb E X_n.}
\]
The leading coefficient is exactly one. The result concerns the expectation, not concentration or a limiting distribution.

## Assumptions and scope
All \(n!\) permutations are equiprobable. For an ordered list of distinct real numbers, its *order type* is the permutation of its ranks in the list. For each \(1\le k\le n\) and \(1\le i\le n-k+1\), denote by \(W_{k,i}\) the order type of positions \(i,\ldots,i+k-1\). Put
\[
U_{n,k}=|\{W_{k,i}:1\le i\le n-k+1\}|,\qquad R_{n,k}=(n-k+1)-U_{n,k}.
\]
Then \(X_n=\sum_{k=1}^{n}U_{n,k}\) and \(D_n=\sum_{k=1}^{n}\mathbb E R_{n,k}\). All logarithms in the theorem are natural. Only the limit \(n\to\infty\) is asserted.

## Proof
**1. Deterministic lower bound.** For every \(k\), there are at most \(k!\) possible order types, so
\[
R_{n,k}\ge(n-k+1)-k!.
\]
We also have \(R_{n,k}\ge0\). Fix \(0<\varepsilon<1\), set \(L_n=(\log n)/(\log\log n)\) and \(a_n=\lfloor(1-\varepsilon)L_n\rfloor\). For sufficiently large \(n\), \(1\le a_n<n\). Summing the lower bound over \(1\le k\le a_n\), using monotonicity of factorial, gives
\[
D_n\ge n a_n-O(a_n^2)-a_n\,a_n!.
\]
By Stirling's formula, \(\log(a_n!)=(1-\varepsilon+o(1))\log n\). Thus \(a_n\,a_n!=n^{1-\varepsilon+o(1)}=o(nL_n)\), while \(a_n^2=o(nL_n)\). Consequently,
\[
\liminf_{n\to\infty}\frac{D_n}{nL_n}\ge1-\varepsilon.
\]

**2. The overlap matching bound.** For any \(k\ge2\) and \(1\le d<k\), compare the two length-\(k\) windows starting at positions \(1\) and \(1+d\). Consider the graph on \(\{1,\ldots,k+d\}\) with edges \(\{j,j+d\}\) for \(1\le j\le k\). Every connected component is a path: consecutive edges move monotonically in a fixed residue class modulo \(d\), so there are no cycles. Color edges alternately on each path. One color class is a matching containing at least \(\lfloor k/2\rfloor\) edges. Let \(J\subseteq\{1,\ldots,k\}\) be the set of its left endpoints. Thus \(|J|\ge\lfloor k/2\rfloor\) and \(J\cap(J+d)=\varnothing\).

If the two full windows have the same order type, then their restrictions to the aligned relative-position set \(J\) have the same order type. The values at the disjoint index sets \(J\) and \(J+d\) have independent uniformly distributed relative orders, each over \(|J|!\) possibilities. It follows that
\[
\Pr(W_{k,1}=W_{k,1+d})\le\frac1{|J|!}\le\frac1{\lfloor k/2\rfloor!}.
\]
For disjoint windows, at separation \(d\ge k\), independence of their order types gives the exact collision probability \(1/k!\). These statements hold for any two valid starting positions by exchangeability of the random permutation.

**3. Collision upper bound.** For each realized permutation, a pattern appearing \(r\ge1\) times causes \(r-1\) repeat occurrences and \(\binom r2\) matching pairs, hence \(R_{n,k}\) is bounded by the number of unordered colliding window pairs. Summing over separations, with at most \(n\) pairs per separation, yields for \(k\ge2\)
\[
0\le\mathbb E R_{n,k}\le\frac{n^2}{2k!}+\frac{nk}{\lfloor k/2\rfloor!}.
\]
The first term bounds the at most \(\binom n2\) pairs of nonoverlapping windows; the second bounds the at most \(nk\) overlapping pairs. Both bounds may exceed one and need not be sharp at fixed \(k\).

**4. Sharp upper bound for the deficit.** Let \(b_n=\lceil(1+\varepsilon)L_n\rceil\). For the shorter lengths, the elementary inequality \(R_{n,k}\le n-k+1\) gives
\[
\sum_{k<b_n}\mathbb E R_{n,k}\le nb_n.
\]
For the longer lengths use Step 3. Since successive factorial terms decrease by successive factors, elementary tail estimates imply, for \(b\to\infty\),
\[
\sum_{k=b}^{\infty}\frac1{k!}=O(1/b!),\qquad
\sum_{k=b}^{\infty}\frac{k}{\lfloor k/2\rfloor!}=O\!\left(\frac{b}{\lfloor b/2\rfloor!}\right).
\]
For the second estimate, group \(k=2j,2j+1\); the resulting sum is bounded by a constant times \(\sum_{j\ge\lfloor b/2\rfloor}(j+1)/j!\), which is at most a constant times \(b/\lfloor b/2\rfloor!\).
Hence
\[
\sum_{k=b_n}^{n}\mathbb E R_{n,k}=O\!\left(\frac{n^2}{b_n!}+\frac{nb_n}{\lfloor b_n/2\rfloor!}\right).
\]
Stirling's formula gives
\[
\log(b_n!)=(1+\varepsilon+o(1))\log n,\qquad
\log(\lfloor b_n/2\rfloor!)=((1+\varepsilon)/2+o(1))\log n.
\]
Therefore \(n^2/b_n!=n^{1-\varepsilon+o(1)}=o(nL_n)\), and \(nb_n/\lfloor b_n/2\rfloor!=n^{(1-\varepsilon)/2+o(1)}=o(nL_n)\). It follows that
\[
\limsup_{n\to\infty}\frac{D_n}{nL_n}\le1+\varepsilon.
\]
Sending \(\varepsilon\downarrow0\) in Steps 1 and 4 proves the theorem. \(\square\)

## Verification
The separate reproducibility program `verify_patterns.py` uses exact integer counts over every permutation through size eight. It checks the definition of each relative-order pattern, the deterministic \(k!\) bound, exact expected totals, the size of disjoint aligned matchings, and the collision bound for feasible small window pairs. In a direct replay it completed \(362934\) assertions. For example,
\[
\mathbb E X_8=\frac{27823}{1260},\qquad D_8=\frac{17537}{1260},
\]
consistent with the published small-size numerical value near \(22.08\). The infinite-size limit is proved analytically above; finite enumeration neither establishes the limit nor an exact error constant.

## Relationship to prior work
Allen, Cruz Fonseca, Dobbs, Downs, Fokuoh, Godbole, Papanikolaou Costa, Soto and Yoshikawa (first public preprint November 24, 2020) established \(\mathbb E X_n=\tfrac12n^2(1-o(1))\) using overlapping-pattern estimates and a cutoff proportional to \(\log n\). Their work also locates the deterministic factorial/window-count crossover at order \(\log n/\log\log n\), but does not identify the corresponding sharp expected deficit. Godbole and Swickheimer (preprint October 21, 2023, journal May 2024) obtained a quantitative lower bound of the form \(\mathbb E X_n\ge \tfrac12n^2-O(n\log n)\), and explicitly posed improving that bound as a question. The present theorem pins down the missing first-order loss, including its coefficient, with a different aligned-matching estimate for overlapping windows. It is not a claim that the overlap-matching method or factorial threshold, individually, is new.

## Limitations
The result requires uniformly random permutations and consecutive order-isomorphism (not ordinary equal substrings or subsequence patterns). It does not assert a variance bound, concentration, convergence in probability, a second correction, or a finite-\(n\) optimal error bound. Historical priority beyond the two closest full-text studies and searched records is not independently established. The method does not address the conjectured distinct *nonconsecutive* pattern count.

## References
1. A. Allen et al., *The Expected Number of Distinct Consecutive Patterns in a Random Permutation*, arXiv:2011.12179 (first posted 2020-11-24); *Pure Mathematics and Applications* 30(4), 2022, DOI:10.2478/puma-2022-0031. https://arxiv.org/abs/2011.12179
2. A. Godbole and H. Swickheimer, *An Alternative Proof for the Expected Number of Distinct Consecutive Patterns in a Random Permutation*, arXiv:2310.14071 (first posted 2023-10-21); *Discrete Mathematics & Theoretical Computer Science* 26(1), 2024, DOI:10.46298/dmtcs.12458. https://arxiv.org/html/2310.14071v4
