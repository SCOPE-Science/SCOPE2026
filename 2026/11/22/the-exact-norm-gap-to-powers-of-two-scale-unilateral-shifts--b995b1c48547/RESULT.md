# The exact norm gap to powers of two-scale unilateral shifts

## Finding

Let \(S\) denote the unilateral shift on complex \(\ell^2(\mathbb N_0)\). Fix any integer \(k\ge2\), any positive integers \(p,q\) with \(k\mid(p+q)\), and any real \(a,b>0\). On \(H=\ell^2(\mathbb N_0)^{\oplus(p+q)}\) define

\[
T=aS^{\oplus p}\oplus bS^{\oplus q},\qquad
\mathcal P_k=\{X^k:X\in\mathcal B(H)\}.
\]

The exact operator-norm and essential-norm distances are the same:

\[
\boxed{\inf_{X\in\mathcal B(H)}\|T-X^k\|
=\inf_{X\in\mathcal B(H)}\|T-X^k\|_{\mathrm{ess}}
=\begin{cases}
0,&k\mid p,\\
\tfrac12|a-b|,&k\nmid p.
\end{cases}}
\]

Both infima are attained by explicit powers. Because \(k\mid(p+q)\), the condition \(k\mid p\) is equivalent to \(k\mid q\). In the nondivisible case with \(a\ne b\), no bounded \(k\)-th root, even after a perturbation of essential norm strictly smaller than \(|a-b|/2\), can exist. For example, the distance of \(2S\oplus S\) to the set of bounded squares is exactly \(1/2\), in both norms.

## Assumptions and scope

All Hilbert spaces are complex and separable; \(S e_n=e_{n+1}\) for \(n\ge0\). All direct sums here have finite positive multiplicity. The norm \(\|Y\|_{\mathrm{ess}}\) denotes the norm of the image \(\pi(Y)\) in the Calkin algebra \(\mathcal B(H)/\mathcal K(H)\). The root \(X\) is permitted to be any bounded operator on \(H\), with no normality, shift, block-diagonal, positivity, or commutation hypothesis. The formula does not claim a classification for variable weighted shifts or for total multiplicities not divisible by \(k\).

## Proof

**1. Construction of exact roots for divisible multiplicities.** For any positive integer \(h\), the unilateral shift \(S\) on the standard sequence space satisfies \(S^k\cong S^{\oplus k}\): the reducing subspaces of \(S^k\) are the sequences indexed by the residue classes modulo \(k\), and restriction to each residue class is unitarily equivalent to \(S\). It follows by taking \(h\) copies that \((c^{1/k}S)^{\oplus h}\), interpreted before residue-class interleaving, has \(k\)-th power unitarily equivalent to \(cS^{\oplus kh}\) for every \(c>0\). Thus when \(k\mid p\) (and hence \(k\mid q\)), the two scalar blocks separately have bounded \(k\)-th roots. Their direct sum gives \(T\in\mathcal P_k\).

**2. A general Fredholm-index divisibility lemma.** Suppose \(X\in\mathcal B(H)\), \(k\ge2\), and \(R>0\) are such that \(X^k-zI\) is Fredholm for every \(|z|=R\). Then

\[
\operatorname{ind}(X^k-zI)\in k\mathbb Z\qquad(|z|=R).
\]

Indeed, for each \(|w|=R^{1/k}\), the polynomial \(X^k-w^k I\) is Fredholm. By the spectral-mapping theorem in the Calkin algebra, \(\pi(X)-wI\) must be invertible, hence \(X-wI\) Fredholm. The index of \(X-wI\) is locally constant on the connected circle \(|w|=R^{1/k}\), so it is one integer \(d\) there. Every \(z\) of modulus \(R\) has \(k\) roots \(w_j\), all on that circle, and

\[
X^k-zI=\prod_{j=0}^{k-1}(X-w_j I),
\quad
\operatorname{ind}(X^k-zI)=\sum_{j=0}^{k-1}d=kd.
\]

This argument uses only Fredholm multiplicativity and the continuity of index; it applies to completely general bounded \(X\).

**3. The essential-norm obstruction.** Assume \(a>b\) and \(k\nmid p\); if \(b>a\), swap the two summands, noting that \(k\nmid q\) as well. Put

\[
r=\frac{a+b}{2},\qquad \delta=\frac{a-b}{2}>0.
\]

The image \(\pi(S)\) of the unilateral shift in the Calkin algebra is unitary, because \(S^*S=I\) and \(SS^*=I-P_{e_0}\), and its spectrum is the full unit circle. Consequently, the normal element \(\pi(T)\) has two spectral circles, of radii \(a\) and \(b\). For every \(|z|=r\), \(\pi(T)-zI\) is invertible with exact resolvent norm

\[
\big\|(\pi(T)-zI)^{-1}\big\|=\frac1\delta.
\]

The operators \(aS-zI\) and \(bS-zI\) are Fredholm for \(|z|=r\): the former has index \(-1\) because \(r<a\), the latter index \(0\) because \(r>b\). Therefore

\[
\operatorname{ind}(T-zI)=-p\qquad(|z|=r).
\]

Suppose toward a contradiction that some bounded \(X\) satisfies \(\|T-X^k\|_{\mathrm{ess}}<\delta\). For each \(|z|=r\) and \(0\le t\le1\), the Calkin image of

\[
T+t(X^k-T)-zI
\]

is invertible by the Neumann-series estimate

\[
t\,\big\|(\pi(T)-zI)^{-1}\big\|\,\|\pi(X^k-T)\|<1.
\]

This is a norm-continuous path of Fredholm operators. Homotopy invariance of Fredholm index implies \(\operatorname{ind}(X^k-zI)=-p\) on the entire circle. Step 2 forces this index to be divisible by \(k\), contradicting \(k\nmid p\). Thus, for every bounded \(X\),

\[
\|T-X^k\|_{\mathrm{ess}}\ge\delta.
\]

**4. Exact matching upper bound.** Set \(c=(a+b)/2\). Since \(k\mid(p+q)\), Step 1 shows that \(Y=cS^{\oplus(p+q)}\) is a bounded \(k\)-th power. The difference \(T-Y\) is block-diagonal with scalar coefficients \(a-c\) and \(b-c\) multiplying copies of \(S\). Therefore

\[
\|T-Y\|=\|T-Y\|_{\mathrm{ess}}
=\max\{|a-c|,|b-c|\}=\delta.
\]

This matches the lower bound. If \(a=b\), then \(T=aS^{\oplus(p+q)}\) is already a bounded \(k\)-th power, regardless of the individual divisibility of \(p\) and \(q\), giving the claimed zero second branch. This proves all cases, including attainment.

## Verification

The two main independent mechanisms are explicit residue-class interleaving (for the upper bound) and the Fredholm-index lemma (for the lower bound). The Calkin resolvent norm is obtained from the spectrum of a normal element, not from a finite-dimensional approximation. The index obstruction applies simultaneously to all bounded candidate roots, not merely block-preserving ones. The argument establishes an exact infinite-dimensional identity for all admissible integer multiplicities and all positive real scales; it does not depend on numerical testing.

As a concrete boundary check, choosing \(k=2\), \(p=q=1\), \(a=2\), \(b=1\) produces the distance \(1/2\), attained by the square \((\sqrt{3/2}\,S)^2\) after the standard even/odd interleaving. At \(a=b\) the distance vanishes because the two blocks merge into one divisible multiplicity.

## Relationship to prior work

Kottegoda, Le and Rodriguez study the exact existence and classification of square roots for weighted shifts of multiplicity two, including subtle obstructions from the two weight sequences. Mashreghi, Ptak and Ross classify roots of several classical operators, including powers of the unilateral shift. Conway and Morrel give a broad Fredholm-topological characterization of the norm closure of operator \(k\)-th powers; their indexed summary implies the *qualitative* nonapproximability of separated-scale configurations with a nondivisible intermediate index. The present result is more specific in objects but quantitative in a different direction: it gives the **exact** operator and essential norm distance, with a matching kth-power minimizer, for every pair of positive scales and every admissible multiplicity pattern. This is not a claim to originate the Fredholm divisibility obstruction itself.

## Limitations

The result is for finite direct sums of *constant-scale* unilateral shifts with total multiplicity divisible by \(k\). No assertion is made about other weighted shifts, fractional or zero scales, arbitrary multiplicity patterns, or full classifications of near-minimizing roots. The original 1987 Conway–Morrel full article was not available for inspection; while the accessible description does not state the exact distance, it creates a real unresolved historical-priority risk. Independent mathematical validation has not been performed.

## References

1. C. Kottegoda, T. Le and T. M. Rodriguez, “Square roots of weighted shifts of multiplicity two,” *Canadian Mathematical Bulletin* 66 (2023), 791–807. First published online 23 December 2022. https://doi.org/10.4153/S000843952200073X
2. J. Mashreghi, M. Ptak and W. T. Ross, “Square roots of some classical operators,” preprint first publicly posted 28 September 2021. https://arxiv.org/abs/2109.13688
3. J. B. Conway and B. B. Morrel, “Roots and logarithms of bounded operators on Hilbert space,” *Journal of Functional Analysis* 70 (1987), 171–193. https://doi.org/10.1016/0022-1236(87)90129-7
