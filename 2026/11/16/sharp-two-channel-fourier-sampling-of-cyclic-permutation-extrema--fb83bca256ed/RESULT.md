# Sharp two-channel Fourier sampling of cyclic permutation extrema

## Finding
Let \(n\ge5\), sample a uniformly random permutation \(\pi\) of \(\{1,\ldots,n\}\), and read its entries cyclically. At site \(i\), let \(P_i\) and \(V_i\) indicate respectively a strict local maximum and a strict local minimum. In the Euclidean coordinate order \((P_0,\ldots,P_{n-1},V_0,\ldots,V_{n-1})\), the covariance matrix \(K_n\) has rank exactly \(2n-1\). Its only null direction is the constant peak-minus-valley contrast: the numbers of cyclic peaks and valleys are equal in every realization.

For \(0\le j<n\), put \(c_j=\cos(2\pi j/n)\). The two squared-energy Fourier sampling eigenvalues, in the normalized peak-plus-valley and peak-minus-valley channels respectively, are exactly
\[
\lambda_j^{+}=\frac{19-5c_j+2c_j^2}{180},\qquad
\lambda_j^{-}=\frac{(1-c_j)(3-2c_j)}{12}.
\]
Every \(\lambda_j^+\) is positive, and \(\lambda_j^-\) vanishes exactly when \(j=0\).

Define \(\kappa_n\) as the ratio of the largest to the smallest **positive** eigenvalue of \(K_n\). Set \(a_n=\cos(2\pi/n)\) and \(b_n=-1\) for even \(n\), or \(b_n=-\cos(\pi/n)\) for odd \(n\). Then
\[
\kappa_5=\frac{45(1-b_5)(3-2b_5)}{48},\qquad
\kappa_n=\frac{(1-b_n)(3-2b_n)}{(1-a_n)(3-2a_n)}\quad(n\ge6).
\]
In particular, the exact limiting law is
\[
\lim_{n\to\infty}\frac{\kappa_n}{n^2}=\frac{5}{\pi^2}.
\]
This quadratic deterioration is a **two-channel effect**: using only peak coordinates, the covariance has full rank \(n\) and its condition number tends to \(11\).

## Assumptions and scope
The permutation entries are distinct and sampled uniformly from all \(n!\) linear orderings, but the adjacent comparisons defining extrema wrap around the cycle, with indices modulo \(n\). This is **not** the cycle-decomposition notion of cyclic peaks. All statements apply to every integer \(n\ge5\) and do not assume any limiting approximation. The covariance uses raw \(0\)-\(1\) indicators without variance-standardization. Eigenvalues use a unitary spatial discrete Fourier transform, with channel vectors \((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\). The condition number excludes the exactly zero eigenvalue.

## Proof
**1. Exact local moments.** Replace the permutation with ranks of independent continuous uniform random variables \(U_0,\ldots,U_{n-1}\); all strict comparison indicators have the same joint law. Each site is a peak with probability \(1/3\), and also a valley with probability \(1/3\). For an offset \(d\in\{0,1,2\}\), enumeration of the orderings of the at most five involved variables gives the following joint probabilities:

| Offset \(d\) | \(\mathbb P(P_0=P_d=1)\) | \(\mathbb P(P_0=V_d=1)\) |
| ---: | ---: | ---: |
| \(0\) | \(1/3\) | \(0\) |
| \(1\) | \(0\) | \(5/24\) |
| \(2\) | \(2/15\) | \(11/120\) |

The offset-one counts involve all \(4!\) relative orders, and offset-two counts all \(5!\). In particular, each probability above is the exact number of satisfying local orders divided by the respective factorial; these integer counts are reproduced by the accompanying checker. Complementing the ranks exchanges peaks and valleys, while reversing site order changes the sign of the offset. Hence the peak/peak and valley/valley covariances coincide, and the peak/valley cross-covariance is symmetric in the offset. For cyclic distance at least three, the corresponding triples involve disjoint variables and their patterns are independent. This remains valid at \(n=5\), where every pair lies within cyclic distance two.

It follows that the nonzero covariance kernels, indexed by cyclic displacement, are
\[
\begin{aligned}
A_0&=\frac29,& A_{\pm1}&=-\frac19,&A_{\pm2}&=\frac1{45},\\
B_0&=-\frac19,&B_{\pm1}&=\frac7{72},&B_{\pm2}&=-\frac7{360},
\end{aligned}
\]
where \(A_d=\operatorname{Cov}(P_0,P_d)=\operatorname{Cov}(V_0,V_d)\) and \(B_d=\operatorname{Cov}(P_0,V_d)\). All other offsets have zero covariance. The matrix \(K_n\) is the block-circulant matrix \(\begin{psmallmatrix}A&B\\B&A\end{psmallmatrix}\).

**2. Exact diagonalization and nullspace.** A unitary Fourier transform of the spatial offset followed by the two normalized channel vectors gives eigenvalues \(\widehat A(j)\pm\widehat B(j)\). The above five-diagonal kernels yield
\[
\widehat A(j)+\widehat B(j)=\frac19-\frac{\cos(2\pi j/n)}{36}+\frac{\cos(4\pi j/n)}{180},
\]
\[
\widehat A(j)-\widehat B(j)=\frac13-\frac5{12}\cos(2\pi j/n)+\frac1{12}\cos(4\pi j/n).
\]
Replacing \(\cos(4\pi j/n)\) with \(2c_j^2-1\) gives the stated two bands. For \(-1\le c\le1\), \(19-5c+2c^2\ge16\) and \((1-c)(3-2c)\ge0\), with equality in the latter precisely when \(c=1\). Thus exactly one eigenvalue is zero. Independently, writing \(S_i=\operatorname{sgn}(U_{i+1}-U_i)\), one has the pointwise discrete-divergence identity \(P_i-V_i=(S_{i-1}-S_i)/2\), so the constant contrast is indeed a deterministic conservation law.

**3. Sharp positive extremal modes.** Both band polynomials strictly decrease as functions of \(c\in[-1,1]\): their derivatives are \((4c-5)/180<0\) and \((4c-5)/12<0\). The plus band therefore lies between \(4/45\) and \(13/90\); the minus band, away from the constant mode, is smallest at \(c=a_n\). Its maximum is attained at the Fourier frequency closest to \(\pi\), where \(c=b_n\). Since \(n\ge5\) implies \(b_n<-1/2\), that maximum exceeds \(1/2>13/90\), so it is the largest eigenvalue of the full covariance. At \(n=5\), \(a_5<1/3\), so \(\lambda_1^->7/54>4/45\); the smallest positive eigenvalue is then \(4/45\). At \(n=6\), \(a_6=1/2\) and \(\lambda_1^-=1/12<4/45\). Since \(a_n\) increases with \(n\), the same minus-channel minimum prevails for every \(n\ge6\). Division gives the exact displayed formulas.

**4. Asymptotics and the single-channel comparison.** As \(n\to\infty\), \(1-a_n\sim2\pi^2/n^2\) and \(b_n\to-1\). Therefore the smallest positive eigenvalue is asymptotic to \(\pi^2/(6n^2)\), while the largest tends to \(5/6\), proving the factor \(5/\pi^2\). In the peak-only covariance, the Fourier eigenvalue is \(\widehat A(j)=(8-10c_j+4c_j^2)/45\), strictly decreasing in \(c_j\). The smallest value is always \(2/45\), and the largest tends to \(22/45\), so the peak-only ratio tends to \(11\). The rank and conditioning conclusions are exact, not inferred from finite examples.

## Verification
Run `python3 check_peak_valley.py` using Python 3 and no external dependencies. It enumerates all permutations at lengths \(5,6,7,8\), compares every rational entry of the resulting \(2n\times2n\) covariance matrices against the five-diagonal kernel, verifies each Fourier eigenvalue, checks extrema at every length from \(5\) through \(600\), and samples the asymptotic limit. The program passed \(1964\) explicit assertions. The exact all-length proof is the local-order enumeration, cyclic disjointness and monotonicity argument above; finite computations are corroboration only.

## Relationship to prior work
Fu (2018, arXiv:1801.04397) develops generating functions for exterior peaks and double descents of linear permutations. Bandt (2022, arXiv:2212.14386, Section IV) gives the full long-run covariance of six length-three ordinal-pattern **aggregate frequencies** in a linear i.i.d. time series, including the turning-rate variance and a telescoping peak/valley balance. Crane, DeSalvo and Elizalde (2016, arXiv:1609.01370) establish weak dissociation and exact overlap-based variances for individual consecutive-pattern counts. Hivert, Nechaev, Oshanin and Vasilyev (2005/2006, arXiv:cond-mat/0509584) give exact peak-count and no-intervening-peak gap statistics in random-permutation landscape models. These contributions motivate and cover the known aggregate turning-rate statistics and local-order ingredients; no priority is claimed for them.

A related published study, *Exact covariance spectrum of the six consecutive triple patterns in uniform permutations* (2026), diagonalizes a six-dimensional covariance of **aggregate non-wrapped pattern counts**. Its exact local overlap tables can supply ingredients here but do not state the \(2n\)-dimensional spatial covariance, cyclic extrema channel decomposition, rank, or sharp inverse-quadratic mode collapse. The new claim is the full **position-resolved cyclic two-channel spectral and conditioning theorem** above, not the general fact that finite-range covariance kernels are Fourier-diagonalizable. A second related published result, *Exact covariance nullspaces of three-point generalized ordinal patterns* (2026), classifies asymptotic nullspaces of aggregate tie-aware ordinal patterns from a finite alphabet; it does not give the cyclic, continuous-rank position-resolved spectral bands. Chavez and Martínez (2025) propose an empirically estimated ordinal-symbol spectrum from symbolic autocovariances and surrogate comparisons, but no exact two-channel cyclic permutation spectrum. Bandt’s long-run aggregate covariance can be recovered from the zero-frequency blocks of a corresponding **linear** setting but does not imply the present complete finite cyclic spatial spectrum, whose smallest positive frequency is nonzero. An earlier specialized cyclic peak/valley point-process spectrum remains a possible priority risk.

## Limitations
The result concerns uniform permutations and exact local rank comparisons, not a Mallows deformation, phase retrieval from nonlinear intensities, asymptotic independence of Fourier scores, or a limit theorem for the maximum observed Fourier coefficient. The condition number is for the Euclidean covariance restricted to its positive eigenspace; including the conserved zero mode would make it infinite. Historical priority has not received an independent audit.

## References
1. A. M. Fu, *A Context-free Grammar for Peaks and Double Descents of Permutations*, arXiv:1801.04397, first posted 2018-01-13, https://arxiv.org/abs/1801.04397.
2. J. Borga and R. Penaguiao, *The feasible region for consecutive patterns of permutations is a cycle polytope*, arXiv:1910.02233, first posted 2019-10-05, https://arxiv.org/abs/1910.02233.
3. H. Crane, S. DeSalvo, S. Elizalde, *The probability of avoiding consecutive patterns in the Mallows distribution*, arXiv:1609.01370, first posted 2016-09-06, https://arxiv.org/abs/1609.01370.
4. F. Hivert, S. Nechaev, G. Oshanin, O. Vasilyev, *On the distribution of surface extrema in several one- and two-dimensional random landscapes*, arXiv:cond-mat/0509584, first posted 2005-09-22, https://arxiv.org/abs/cond-mat/0509584.
5. C. Bandt, *Statistics and modelling of order patterns in univariate time series*, arXiv:2212.14386, first posted 2022-12-29, https://arxiv.org/abs/2212.14386, Section IV.
6. *Exact covariance spectrum of the six consecutive triple patterns in uniform permutations*, published research finding dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-covariance-spectrum-of-the-six-consecutive-triple-patterns--b3ad3b36c62e.
7. *Exact covariance nullspaces of three-point generalized ordinal patterns*, published research finding dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-covariance-nullspaces-of-three-point-generalized-ordinal-p--09ebdb81d232.
8. M. Chavez and J. H. Martínez, *Ordinal Spectrum: Mapping Ordinal Patterns into Frequency Domain*, Entropy 27(10):1027 (2025), https://doi.org/10.3390/e27101027.
