# Exact Fourier inertia of singleton-set partition convolution

## Finding
Let \(\Pi_n\) be the set of all set partitions of \([n]\), and send a partition to the binary indicator of its singleton blocks. On \(G_n=(\mathbb Z/2\mathbb Z)^n\), let \(\mu_n(s)\) count partitions with singleton-set indicator \(s\), and let \(T_n f=\mu_n*f\) denote unnormalized convolution. For every integer \(n\ge1\), the complete inertia of the real symmetric convolution operator is:

- \(n=2\): two zero eigenvalues and two positive eigenvalues;
- \(n\in\{1,3,5,7\}\): precisely one negative eigenvalue, at the all-ones Walsh frequency, and no zero eigenvalues;
- every other \(n\ge1\): all \(2^n\) eigenvalues are strictly positive.

In particular, \(T_n\) is invertible except when \(n=2\), and is strictly positive definite for exactly \(n\in\{4,6\}\cup\{8,9,10,\ldots\}\). Thus dimension eight is the sharp threshold for *eventual* strict positive definiteness.

## Assumptions and scope
The block labels of a set partition are immaterial. Its singleton set is the subset of vertices that occur as one-element blocks, represented by its binary incidence vector. Multiplicities are essential: two partitions with the same singleton set contribute twice. For any frequency \(K\subseteq[n]\), the unnormalized Walsh character is \(\chi_K(s)=(-1)^{|K\cap s|}\); no division by \(2^n\) or the Bell number is used in the Fourier multipliers. All eigenvalue multiplicities count the full \(2^n\)-dimensional regular representation.

## Proof
Write \(B_j\) for the number of set partitions of \([j]\), with \(B_0=1\), and set \(k=|K|\). By expanding \(\prod_{i\in K}(1-2\mathbf1_{\{i\}\text{ is a block}})\) and prescribing \(j\) specified singleton blocks, the Walsh multiplier is
\[
\lambda_{n,k}=\sum_{j=0}^{k}\binom{k}{j}(-2)^j B_{n-j}.
\]
Consequently the multiplier depends only on the Hamming weight \(k\) of the frequency and has multiplicity \(\binom nk\).

Dobiński's moment identity \(B_j=\mathbb E[X^j]\) for \(X\sim\operatorname{Poisson}(1)\) gives
\[
\lambda_{n,k}=\mathbb E\bigl[X^{n-k}(X-2)^k\bigr]
=e^{-1}\sum_{r=0}^{\infty}\frac{r^{n-k}(r-2)^k}{r!}.
\]
The convention \(0^0=1\) applies in this polynomial expansion. The absolutely convergent series permits the following strict sign bounds.

If \(k\) is even, the integrand is nonnegative and is strictly positive for every integer \(r\ge3\), so \(\lambda_{n,k}>0\). If \(k\) is odd and \(d=n-k\ge1\), the only negative summand is the term \(r=1\), which equals \(-1/e\); the term \(r=0\) vanishes and \(r=2\) is zero. For \(k\ge3\), the positive contributions at \(r=3,4\), after multiplication by \(e\), are at least
\[
\frac{3^d}{6}+\frac{4^d2^k}{24}\ge\frac12+\frac43>1.
\]
For \(k=1\) and \(d\ge2\), the \(r=3\) contribution alone is at least \(9/6>1\). The remaining case \((k,d)=(1,1)\) is exactly zero because \(\lambda_{2,1}=B_2-2B_1=0\).

It remains to treat odd \(k=n\). Here
\[
e\lambda_{n,n}=-2^n-1+\sum_{r=3}^{\infty}\frac{(r-2)^n}{r!}.
\]
For \(n=1,3,5,7\), exact Bell-number substitution gives, respectively, \(-1,-3,-10,-21\). For every odd \(n\ge9\), the contributions of \(r=5,6\) already exceed \(2^n+1\): at \(n=9\) this follows from the exact inequality
\[
\frac{3^9}{120}+\frac{4^9}{720}>2^9+1;
\]
and after division by \(2^n\), its left-hand side increases strictly with \(n\), while its right-hand side \(1+2^{-n}\) decreases. Every omitted contribution is nonnegative. Therefore \(\lambda_{n,n}>0\) for all odd \(n\ge9\).

Walsh diagonalization of convolution on \(G_n\) now gives the stated eigenvalue signs and multiplicities. The two zero characters when \(n=2\) are precisely the two weight-one characters. All other dimensions have full rank, while strict positive definiteness is equivalent to the absence of negative or zero multipliers. This proves the complete inertia classification.

## Verification
The standalone file `check_singleton.py` reconstructs each set partition as a restricted-growth string, counts exact singleton incidence masks, and independently applies the integer fast Walsh transform. For \(1\le n\le11\), it compares every multiplier with the Bell-number sum and checks the complete eigenvalue sign pattern. For \(1\le n\le7\), it also compares with separate direct character sums. It checks every Bell-sum sign at all \(1\le n\le90\) and the exact finite moment and tail inequalities used in the proof. Run `python3 check_singleton.py`; the recorded run passed 12,652 exact assertions. These finite checks corroborate the algebra but do not substitute for the all-order inequalities in the proof.

## Relationship to prior work
The Poisson representation of Bell numbers and the combinatorics of partitions without singleton blocks are classical. Privault (2011), especially Sections 2–3, develops general Poisson shifted and central moments; this provides a close analytic foundation but does not state the Walsh inertia or the sharp dimension-eight positivity threshold. The 2011 study *The largest singletons of set partitions* supplies singleton enumeration and Bell identities for ordered singleton statistics; it does not identify the Fourier signs of the complete singleton-incidence counting kernel. The new assertion is the complete sign, kernel and strict-positive-definiteness classification, not the Bell or Poisson moment identity itself.

## Limitations
The result concerns the multiplicity-weighted singleton-set pushforward of **all** set partitions, not indicators of partition-equivalence matrices, noncrossing partitions, or fixed-block-count ensembles. It does not give the sharp smallest positive eigenvalue at every dimension, and does not address arbitrary positive singleton weights. The literature comparison is bounded rather than an exhaustive priority guarantee; an older treatment of signed singleton-position enumerators could contain an equivalent statement. No independent external audit has been performed.

## References
1. N. Privault, *Generalized Bell Polynomials and the Combinatorics of Poisson Central Moments*, Electronic Journal of Combinatorics 18(1), P54 (published 11 March 2011), https://doi.org/10.37236/541 .
2. *The largest singletons of set partitions*, European Journal of Combinatorics 32 (2011), 369–382, https://doi.org/10.1016/j.ejc.2010.10.011 .
3. G. Dobiński, *Summirung der Reihe ...*, Grunert's Archiv 61 (1877), 333–336; classical Bell/Poisson moment identity, also discussed in Reference 1.
