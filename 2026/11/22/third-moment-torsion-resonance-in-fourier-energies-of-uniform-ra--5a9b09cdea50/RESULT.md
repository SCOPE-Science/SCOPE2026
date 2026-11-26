# Third-moment torsion resonance in Fourier energies of uniform rank permutations

## Finding
Let \(n\ge 7\) be odd. For \(n\) i.i.d. observations of a pair of independent continuous scalar variables, the paired ranks induce a uniform permutation \(\pi\) of \(\{0,\ldots,n-1\}\). For every pair \(1\le k,\ell\le(n-1)/2\), put
\[
\omega=e^{2\pi\mathrm i/n},\qquad
A_{k,\ell}=\sum_{j=0}^{n-1}\omega^{kj+\ell\pi(j)},\qquad
Q_{k,\ell}=\frac{|A_{k,\ell}|^2}{n}.
\]
Write \(r=\mathbf1_{\{n\mid 3k\}}+\mathbf1_{\{n\mid 3\ell\}}\). The first two null moments are independent of the frequencies:
\[
\mathbb E Q_{k,\ell}=\frac{n}{n-1},\qquad
\operatorname{Var}(Q_{k,\ell})=\frac{n(n^2-3n+3)}{(n-2)(n-1)^2}.
\]
The **third centered moment** instead has precisely three arithmetic classes,
\[
\boxed{\mathbb E\left(Q_{k,\ell}-\frac{n}{n-1}\right)^3=K_r(n),}
\]
where
\[
\begin{aligned}
K_0(n)&=\frac{2(n^4-6n^3+14n^2-16n+5)}{(n-3)(n-1)^3},\\
K_1(n)&=\frac{2n^3-6n^2+9n-3}{(n-1)^3},\\
K_2(n)&=\frac{(n-3)(2n^5-21n^4+80n^3-148n^2+135n-36)}{(n-5)(n-4)(n-2)(n-1)^3}.
\end{aligned}
\]
For all permitted indices, \(K_1(n)<K_0(n)<K_2(n)\) whenever the three classes can occur (that is, whenever \(3\mid n\), so \(n\ge9\)). For \(3\nmid n\), every positive-frequency pair is in class zero. At \(n=9\), all three classes occur and yield \(K_0(9)=1591/768\), \(K_1(9)=525/256\), and \(K_2(9)=20871/8960\). Each of the three expressions tends to \(2\) as \(n\to\infty\) along allowable orders.

## Assumptions and scope
The observations are \(n\) i.i.d. copies of a pair whose two marginal coordinates are independent and **continuous**; the common margins are allowed to be unknown. Almost surely there are no ties, and after sorting by the first-coordinate rank, the second-coordinate ranks give an exactly uniform permutation. The moment identities apply directly whenever the pairing permutation is uniform. The frequencies are positive, at most \((n-1)/2\), and the sample size is odd and at least seven. These restrictions avoid order-two Fourier characters and isolate the order-three resonance without additional exceptional classes. The statistic \(Q_{k,\ell}\) is the squared, scaled, nonzero two-dimensional discrete Fourier coefficient of the rank-pairing permutation matrix. This is a null-moment result for **one** component, not a power theorem for an omnibus independence test.

## Proof
**1. Rank-null reduction and low moments.** Within each continuous marginal sample, exchangeability makes all rank orders equally likely. The two marginal samples are independent, so ordering by one leaves the rank permutation of the other uniform. For any nontrivial character \(\chi(j)=\omega^{kj}\), \(\sum_j\chi(j)=0\); similarly for \(\omega^{\ell j}\). Standard without-replacement averaging yields
\[
\mathbb E|A_{k,\ell}|^2=\frac{n^2}{n-1},\qquad
\mathbb E|A_{k,\ell}|^4=\frac{n^3(2n-3)}{(n-2)(n-1)}.
\]
The second identity can also be recovered by the four-position version of the partition formula below; its zero-sum character sums have no dependence on the character order for odd \(n\ge7\). Division by \(n\) and \(n^2\) respectively gives \(\mathbb EQ\) and \(\mathbb EQ^2=n(2n-3)/[(n-2)(n-1)]\), hence the stated variance.

**2. An exact six-position partition identity.** Let \(\varepsilon=(1,1,1,-1,-1,-1)\), and let \(\mathfrak P_6\) be the \(203\) set partitions of the six labeled positions. For a partition \(P\) with blocks \(B\), define \(s(B)=\sum_{t\in B}\varepsilon_t\). For a character of exact order \(d\ge3\), define the integer polynomial
\[
F_d(P;z)=\sum_{R\succeq P}\left[\prod_{C\in R}(-1)^{m_C-1}(m_C-1)!\right]
 z^{|R|}\prod_{C\in R}\mathbf1_{\{d\mid\sum_{B\subseteq C}s(B)\}},
\]
where \(R\succeq P\) coarsens \(P\), and \(m_C\) counts the blocks of \(P\) merged into the block \(C\) of \(R\). This is partition-lattice Möbius inversion applied to the sum over distinct indices assigned to the blocks of \(P\). By character orthogonality, the unrestricted sum for a merged block contributes \(n\) if its signed multiplicity is divisible by \(d\), and zero otherwise.

Set \(d_k=n/\gcd(n,k)\) and \(d_\ell=n/\gcd(n,\ell)\). When expanding three copies each of \(A_{k,\ell}\) and its conjugate, classify the six row indices by their **exact** equality partition \(P\). The corresponding column values are uniformly ordered distinct indices, with probability \(1/(n)_{|P|}\). Thus
\[
\mathbb E|A_{k,\ell}|^6
=\sum_{P\in\mathfrak P_6}
\frac{F_{d_k}(P;n)F_{d_\ell}(P;n)}{(n)_{|P|}},
\qquad(n)_m=n(n-1)\cdots(n-m+1).
\tag{1}
\]
The sign sum of any block is between \(-3\) and \(3\). Since \(n\) is odd and the frequencies are nonzero, every relevant character order is \(3\) or at least \(5\); orders at least \(5\) are indistinguishable in (1). Write \(d=3\) or \(d=7\) as representatives of these two classes, with \(7\) representing **all** orders \(\ge5\).

**3. Polynomial evaluation, with an exact reproducible certificate.** Evaluate (1) by enumerating \(\mathfrak P_6\), enumerating coarsenings of each \(P\), and applying the displayed Möbius coefficient. Clearing the common denominator \((n)_6\) gives identities in the integer polynomial ring, not pointwise numerical checks. The outcomes are:
\[
\mathbb E|A|^6=\begin{cases}
\dfrac{n^3(6n^3-27n^2+34n-20)}{(n-3)(n-2)(n-1)},&d_k,d_\ell\ge5,\\[5pt]
\dfrac{3n^3(2n^2-3n+2)}{(n-2)(n-1)},&\text{exactly one of }d_k,d_\ell\text{ equals }3,\\[5pt]
\dfrac{n^3(6n^4-62n^3+201n^2-225n+108)}{(n-5)(n-4)(n-2)(n-1)},&d_k=d_\ell=3.
\end{cases}
\tag{2}
\]
The included `check.py` implements the finite, transparent polynomial arithmetic of (1) and verifies **all three identities (2) coefficient-by-coefficient** after multiplication by \((n)_6\). Because there are precisely 203 set partitions and every coarsening is included, this is an exhaustive symbolic certificate valid for every admissible integer \(n\). No extrapolation from sample sizes is used. It also independently enumerates all permutations at sample sizes \(7\) and \(9\) as a cross-check.

**4. Centering and strict separation.** Use \(Q=|A|^2/n\) and
\[
\mathbb E(Q-\mathbb EQ)^3=\mathbb EQ^3-3(\mathbb EQ)(\mathbb EQ^2)+2(\mathbb EQ)^3.
\]
Substituting the second-, fourth-, and sixth-order results gives the three stated rational expressions. Direct factorization shows
\[
K_1-K_0=-\frac1{(n-3)(n-1)},\qquad
K_2-K_0=\frac{n^4-10n^3+38n^2-77n+76}{(n-5)(n-4)(n-3)(n-2)(n-1)}.
\]
Writing \(t=n-9\ge0\), the numerator of the second difference becomes \(t^4+26t^3+254t^2+1093t+1732>0\). This proves strict class ordering whenever order-three characters are present. Leading terms give the common limit \(2\).

## Verification
Run `python check.py` from a directory containing the standalone supplied script, using Python 3 and no additional packages. It independently builds all \(203\) partitions, their coarsenings, the integer-polynomial identity for each of the three order patterns, and exhaustive full permutation enumerations at \(n=7\) and \(n=9\). The symbolic computation is a finite exhaustive proof of the nontrivial polynomial identity in (2); numerical complex-root enumeration is an independent finite sanity check, not an infinite proof. The character-orthogonality and conditioning arguments outside the symbolic identity are given above.

## Relationship to prior work
Shi, Drton, and Han (2019) derive distribution-free rank-based independence procedures and asymptotic permutation-statistic null laws; their stated test and theory do not present the particular finite-sample sixth-moment classification for the individual rank-permutation Fourier coefficient. Shi, Hallin, Drton, and Han (2020) develop a broader distribution-free rank-testing framework, again directed at asymptotic representations rather than the finite-frequency order-three correction. The existing published exact **real rank-one permutation fourth-moment optimization** establishes related order-four information but does not supply order-six coefficients or the third centered moment of a **complex Fourier energy**. A published order-three periodic autocorrelation result also has equal low-order moments but an exceptional third moment; it counts occupied edges of fixed-weight binary cyclic subsets, not Fourier energies of uniform permutations, and its formulas neither imply nor match the present character-sum law. The equality-partition method is classical in combinatorial moments; no novelty is claimed for Möbius inversion or Fourier orthogonality themselves. The proposed specific contribution is the full finite-sample third-moment arithmetic classification and its strict ordering.

## Limitations
The formulas are restricted to odd \(n\ge7\) and positive nonzero frequencies in the stated range. They do not give mixed moments among distinct rank-Fourier modes, an exact full null distribution, critical values, power guarantees, estimation results, or even-sample extensions. The individual statistics are dependent, even when their first two marginal moments agree. A complete historical priority check cannot rule out equivalent sixth-moment formulas expressed in general permutation or representation-theoretic notation. Independent external mathematical validation has not been performed.

## References
1. H. Shi, M. Drton, and F. Han, *Distribution-free consistent independence tests via center-outward ranks and signs*, arXiv:1909.10024, first publicly posted 2019-09-22, https://arxiv.org/html/1909.10024v4.
2. H. Shi, M. Hallin, M. Drton, and F. Han, *On universally consistent and fully distribution-free rank tests of vector independence*, arXiv:2007.02186, first publicly posted 2020-07-04, https://arxiv.org/abs/2007.02186.
3. *Order-three arithmetic resonance in fixed-weight periodic autocorrelation*, published 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-order-three-arithmetic-resonance-in-fixed-weight-periodic-autoco--a4bc711bf23f (distinct fixed-weight binary-subset law).
4. *Sharp fourth moments of rank-one permutation matrix coefficients*, publicly available 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fourth-moments-of-rank-one-permutation-matrix-coefficients--4f870a695087 (prior fourth-order result, not a sixth-order source).
