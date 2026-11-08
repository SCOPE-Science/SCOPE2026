# Complete subsequential covering-time laws for random Fibonacci tilings

## Finding
Fix an integer \(d\ge2\) and use the cyclic, fair-bit random Fibonacci block tiling of Amit et al. [1]. Let \(T(a)\) be the first move covering a lattice target \(a\in\mathbb Z^d\), and let \(B(a)\) be the earliest move at which covering is geometrically possible. As the target recedes (\(\delta_\infty(a)\to\infty\)), the **complete set** of weak subsequential limits of \(T(a)-B(a)\) is the family below; every member of that family is realized.

Choose an anchor coordinate \(s\in\{0,\dots,d-1\}\). Set \(h_s=0\). For each \(r\ne s\), independently choose either \(h_r=\infty\), or a positive integer satisfying \(h_r\equiv s-r\pmod d\). For every \(r\) with finite \(h_r\), independently choose \(\kappa_r\in[1/2,1]\). Then the corresponding nonnegative integer-valued limit \(Y\) has distribution
\[
\Pr(Y\le z)=\prod_{r:h_r<\infty}\left(1-\kappa_r2^{-\lfloor(z+h_r)/d\rfloor}\right),\qquad z=0,1,2,\ldots,
\]
with \(\Pr(Y\le z)=0\) for \(z<0\). There are **no further restrictions** on these parameters. All values \(\kappa_r=1\) are allowed as limits, although not as finite-scale canonical ranks.

Moreover, if each finite \(\kappa_r\) is dyadic in \([1/2,1)\), the law of \(T(a)-B(a)\) can be made **exactly equal** to this limiting law for infinitely many targets whose distance from the initial cube tends to infinity. In particular the collection of limit laws is uncountable, and there is no universal centered limit law.

## Assumptions and scope
The initial block is \([0,1]^d\). Coordinates are updated in cyclic order \(0,1,\ldots,d-1\); each update adds a block on the positive or negative face with independent equal probabilities. Let \(F^{(d)}_0=\cdots=F^{(d)}_{d-1}=1\), and \(F^{(d)}_j=F^{(d)}_{j-1}+F^{(d)}_{j-d}\) for \(j\ge d\). For a target coordinate \(a_r\), put
\[
\delta_r=\max\{a_r-1,-a_r,0\},\qquad \delta_\infty(a)=\max_r\delta_r.
\]
If \(\delta_r>0\), define \(w_{r,j}=F^{(d)}_{d-1+r+jd}\) and \(W_{r,m}=\sum_{j=0}^{m-1}w_{r,j}\). The least feasible number of updates is \(m_r=\min\{m\ge1:W_{r,m}\ge\delta_r\}\). The coordinate's least feasible global move is \(b_r=r+1+d(m_r-1)\), and \(B(a)=\max_{r:\delta_r>0}b_r\). Define \(R_r\) as the binary rank of the first length-\(m_r\) placement word whose weighted sum is at least \(\delta_r\), and \(\kappa_r=R_r/2^{m_r}\). Inactive coordinates (\(\delta_r=0\)) have no covering delay. All limits in this statement concern fixed \(d\), varying integer targets, and the centered variable \(T(a)-B(a)\).

## Proof
**1. Exact finite-scale reduction.** The coordinate weights are strictly superincreasing: \(w_{r,j}>\sum_{i<j}w_{r,i}\). Consequently binary rank and weighted-sum order coincide. The exact finite-scale theorem of [1, Theorem 3.4] states
\[
T_r=b_r+dG_r,\quad \Pr(G_r>k)=\kappa_r2^{-k}\quad(k\in\mathbb Z_{\ge0}),
\]
where the coordinate delays \(G_r\) are independent across distinct \(r\), \(0\le G_r\), and \(1/2\le\kappa_r<1\). Also \(T(a)=\max_r T_r\). If \(s\) is the coordinate attaining \(B(a)\), define \(h_r=B(a)-b_r\) for active coordinates and \(h_r=\infty\) otherwise. The anchor \(s\) is unique: \(b_r\equiv r+1\pmod d\), and distinct coordinates have different residues. Hence \(h_s=0\), while each other finite \(h_r\) is positive and congruent to \(s-r\pmod d\). For each integer \(z\ge0\), independence gives the exact identity
\[
\Pr(T(a)-B(a)\le z)=\prod_{r:h_r<\infty}\left(1-\kappa_r2^{-\lfloor(z+h_r)/d\rfloor}\right).
\]
The integer in each exponent is nonnegative. This identity is exact for each target, not an asymptotic assertion.

**2. Necessity of the displayed limit family.** Consider any sequence of targets with \(\delta_\infty(a)\to\infty\); then \(B(a)\to\infty\) because all cumulative coordinate weights are finite at each fixed update count. From any subsequence, extract a further subsequence on which the unique anchor \(s\) is fixed. Since there are finitely many coordinates, for each \(r\ne s\) either \(h_r\to\infty\), or \(h_r\) is eventually a fixed positive admissible integer after extracting again. For every finite-offset coordinate, compactness of \([1/2,1]\) gives a limit \(\kappa_r\in[1/2,1]\). A coordinate with \(h_r\to\infty\) disappears from the limiting maximum: for fixed \(z\ge0\), its chance of violating \(dG_r-h_r\le z\) is bounded by \(2^{-\lfloor(z+h_r)/d\rfloor}\to0\). Taking limits in the finite product proves the stated CDF for every integer \(z\). The limit is a proper distribution since its finite product tends to one as \(z\to\infty\); pointwise convergence on the integer lattice gives weak convergence.

**3. Every parameter family occurs.** For each finite-offset coordinate, and any integer \(m\ge1\), define the weighted subset sum
\[
V_{r,m}(R)=\sum_{j=0}^{m-1}\mathbf1_{\{\text{binary digit }j\text{ of }R\text{ is }1\}}w_{r,j},\quad 0\le R<2^m.
\]
Strict superincreasingness makes \(V_{r,m}(R)\) strictly increasing in \(R\). For every rank \(2^{m-1}\le R<2^m\), setting \(\delta_r=V_{r,m}(R)\) gives \(W_{r,m-1}<\delta_r\le W_{r,m}\), so that \(m_r=m\), the first successful rank is exactly \(R\), and \(\kappa_r=R/2^m\).

Choose an increasing integer sequence \(M\to\infty\). Give the anchor \(s\) update count \(m_s=M\) and therefore earliest move \(B=s+1+d(M-1)\). For each other finite-offset coordinate set
\[
m_r=M+\frac{s-r-h_r}{d}.
\]
The offset congruence ensures that this is an integer; it is positive for all sufficiently large \(M\). For each such coordinate choose ranks \(R_{r,M}\) in the upper half of \(\{0,\ldots,2^{m_r}-1\}\) with \(R_{r,M}/2^{m_r}\to\kappa_r\); take \(R=2^{m_r}-1\) for endpoint \(\kappa_r=1\). Put \(a_r=1+V_{r,m_r}(R_{r,M})\) and put \(a_r=0\) for coordinates with infinite offset. These are legitimate lattice targets, their canonical offsets and ranks have the desired limits, and \(\delta_\infty(a)\to\infty\) because the anchor requires ever larger weights. The exact finite-scale product from step 1 converges to the prescribed distribution.

**4. Exact repetition at dyadic parameters.** When each finite \(\kappa_r\) is a dyadic rational strictly below one, choose \(M\) sufficiently large that all \(R_{r,M}=2^{m_r}\kappa_r\) are integers. The ranks then realize the parameters exactly, all offsets are fixed, and the exact centered CDF in step 1 agrees with the displayed limiting CDF for every such \(M\), proving exact repetition at arbitrarily distant targets. With only the anchor active, varying \(\kappa_s\) over \([1/2,1]\) makes \(\Pr(Y=0)=1-\kappa_s\), proving uncountably many distinct laws.

## Verification
The independent Python 3 checker `check.py`, using only the standard library and exact fractions, verifies the strictly ordered rank construction against enumerated subsets, the permanent failing-word count, directly enumerated full placement-word covering probabilities for small \(d\), and multi-coordinate exactly repeated centered laws at dyadic parameters. Run `python3 check.py`. The reported assertion count is recorded in `VERIFICATION.md`. None of these finite checks substitutes for the preceding proof for arbitrary targets and unbounded scales.

## Relationship to prior work
Amit et al. [1] introduce precisely this random block-tiling model. Their Theorems 3.1 and 3.4 prove the superincreasing rank law and one-coordinate geometric delay; their Theorem 4.3 gives the fixed-target distribution, and Section 5.3 proves tightness and notes parameter dependence without identifying every possible centered limit. Their Conclusion expressly identifies classification of subsequential centered laws as a natural remaining question. The present theorem adds the **necessary and sufficient parameter space** for *all* possible limits, the congruence constraints on active coordinate offsets, independent attainability of every parameter including boundary values, and infinitely repeated exact laws for dyadic parameters. Those sufficiency and realization assertions are not stated in [1]. The deterministic rectangle-game precursor [2] establishes Fibonacci geometry but contains no independent random placements or covering-time limit classification.

## Limitations
The dimension \(d\) must be fixed; no simultaneous \(d\to\infty\) classification is claimed. The placement choices must be independent and fair. Weak limit laws are classified for centering by the earliest possible covering move \(B(a)\); centering by exact expectations or by the real-valued logarithmic target distance is not classified here. This proof uses the existing exact finite-scale law of [1]; it does not claim that law as new. Priority comparisons with literature beyond the inspected work cannot exclude all unpublished or differently titled derivations. No independent mathematical audit has been performed.

## References
[1] Y. Amit, A. Gebre, C. Housholder, J. Khan, S. Miller, E. Upton, and C. Yau, *Random Fibonacci Tilings*, arXiv:2611.08317v1 (first posted 2026-11-05), https://arxiv.org/html/2611.08317v1 . Relevant: Theorems 3.1, 3.4, 4.3; Sections 5.3 and 7.

[2] D. L. Engholm and S. J. Miller, *The Fibonacci Rectangle Game: Two First-Move Classes and a Triangle-Induced Choice*, arXiv:2607.19960v1 (first posted 2026-07-22), https://arxiv.org/html/2607.19960v1 .
