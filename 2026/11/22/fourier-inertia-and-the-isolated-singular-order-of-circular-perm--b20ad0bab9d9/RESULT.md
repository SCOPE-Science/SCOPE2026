# Fourier inertia and the isolated singular order of circular permutation-successions

## Finding
For each integer \(n\ge2\), write positions and values as \(\mathbb Z/n\mathbb Z\). Given a permutation \(\pi\), its circular-succession set is
\[
U_n(\pi)=\{i:\pi(i+1)=\pi(i)+1\pmod n\}.
\]
Let \(f_n(x)=\#\{\pi:1_{U_n(\pi)}=x\}\) for \(x\in G_n=(\mathbb Z/2\mathbb Z)^n\), and let \(T_n g=f_n*g\), with counting-measure convolution. Each binary Walsh character of weight \(k\) has eigenvalue \(\Lambda_{n,k}\) given by
\[
\Lambda_{n,k}=n\sum_{j=0}^{k}\binom{k}{j}(-2)^j(n-j-1)!\quad(0\le k<n),
\]
\[
\Lambda_{n,n}=n\sum_{j=0}^{n-1}\binom nj(-2)^j(n-j-1)!+n(-2)^n.
\]
The precise inertia \((N_+,N_-,N_0)\) is \((2,2,0)\) at \(n=2\), \((4,0,4)\) at \(n=3\), \((11,5,0)\) at \(n=4\), \((63,1,0)\) at \(n=6\), and \((2^n,0,0)\) at \(n=5\) and every \(n\ge7\). Hence \(T_n\) is invertible except at \(n=3\), when the kernel has dimension four, and strictly positive definite precisely at \(n=5\) or \(n\ge7\). For \(n\ge7\), the smallest eigenvalue equals \(\min\{\Lambda_{n,n-1},\Lambda_{n,n}\}\), while the largest is \(n!\), yielding the exact \(\ell^2\) condition number \(n!/\min\{\Lambda_{n,n-1},\Lambda_{n,n}\}\).

## Assumptions and scope
All permutations are counted individually. Modulo \(n\) applies both to cyclic position successors and cyclic value successors. There is no probability normalization: \(\sum_x f_n(x)=n!\). Fourier characters are \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\). Only dimensions \(n\ge2\) are asserted. The eigenspace multiplicity of each weight-\(k\) eigenvalue is \(\binom nk\), counted with frequency multiplicity even if distinct weight classes share a value.

## Proof
**1. Joint circular-succession constraints.** For a specified set \(J\) of \(j<n\) positions, the number of permutations satisfying all constraints is \(n(n-j-1)!\), with \(n!\) for \(j=0\). Contract the directed selected cyclic adjacencies into disjoint ordered runs, arrange the resulting \(n-j\) blocks in a circle (\((n-j-1)!\) circular orders), then select one of the \(n\) cuts. This independent-of-shape count appears in Diaconis–Evans–Graham, Proposition 5.1. For \(j=n\), all edges force a rotation, hence exactly \(n\) permutations. Expanding \(\prod_{i\in S}(1-2\,1_{\{i\in U_n(\pi)\}})\) proves the stated eigenvalue formulas and exchangeability.

**2. Proper frequency weights.** Set \(F_{r,k}=\sum_{j=0}^k\binom kj(-2)^j(r-j)!\) for \(0\le k\le r\). We have \(\Lambda_{n,k}=nF_{n-1,k}\) for \(k<n\). Binomial subtraction gives \(F_{r,k}-F_{r,k+1}=2F_{r-1,k}\). Also \(F_{r,r}=r!S_r\), where \(S_r=\sum_{j=0}^r(-2)^j/j!\). By the alternating-series bound, \(1/15\le S_r\le1/3\) for every \(r\ge5\); in particular \(S_r>0\). Directly \(F_{4,k}\), for weights zero through four, equals \((24,12,8,4,8)\), all positive. Induction using the subtraction identity now shows \(F_{r,k}>0\) for every \(r\ge4\) and \(0\le k\le r\): for \(r\ge5\), the strictly positive row below makes \(F_{r,k}\) strictly decreasing in \(k\), and the terminal \(F_{r,r}\) is positive. Hence every proper-weight eigenvalue is positive for \(n\ge5\); at \(n\ge6\) these eigenvalues decrease strictly with character weight. Direct proper-weight lists for \(n=2,3,4\) are handled in step 4.

**3. Full-weight character.** Define \(b_n=\sum_{j=0}^{n-1}(-2)^j/[j!(n-j)]\), for \(n\ge1\). Then \(b_1=1\), and multiplication of \(-\log(1-z)\) by \(e^{-2z}\) gives the exact recurrence \(n b_n=S_{n-1}-2b_{n-1}\). By the character formula, \(\Lambda_{n,n}/n!=n(b_n+(-2)^n/n!)\). The exact values \(b_9=11/756\) and \(0<b_9<1/30\), together with \(1/15\le S_m\le1/3\) for all \(m\ge5\), prove inductively \(0<b_n<1/30\) for all \(n\ge9\). Thus \(\Lambda_{n,n}>0\) for every even \(n\ge10\). For odd \(n\ge13\), use \(b_{n-1}<1/[3(n-1)]\) (from the recurrence and positivity of \(b_{n-2}\)) to obtain
\[
 b_n>\frac{1/15-2/[3(n-1)]}{n}\ge\frac1{90n}.
\]
For \(n\ge13\), \(2^n/n!<1/(90n)\): check at \(n=13\), then the ratio of consecutive quantities \(n2^n/n!\) is \(2/n\), less than one. Therefore \(b_n-2^n/n!>0\) at every odd \(n\ge13\). The exact full-weight eigenvalues for \(n=7,8,9,10,11,12\) are respectively \(1008,2944,42912,394880,4535168,54927360\), all positive. At \(n=5\), the full-weight eigenvalue is \(60\). At \(n=6\), it is \(-96\). This settles all orders.

**4. Exceptional small inertia.** Applying the exact formula at \(n=2\) yields the weight-indexed list \((2,-2,2)\); at \(n=3\), \((6,0,6,0)\); at \(n=4\), \((24,8,8,-8,-8)\); at \(n=5\), \((120,60,40,20,40,60)\); and at \(n=6\), \((720,432,288,192,144,48,-96)\). Weight multiplicities \(\binom nk\) produce exactly the claimed inertia triples. For \(n\ge7\) steps 2 and 3 give strict positivity. Walsh diagonalization gives invertibility, positivity and, since all \(f_n(x)\ge0\), \(|\Lambda_{n,k}|\le n!\) with equality at the trivial character. At \(n\ge7\), the strict monotonicity in proper weights proves the sharp minimum eigenvalue formula in the Finding.

## Verification
Run `python3 cyclic_verify.py` using Python's standard library. It recomputes the full multiset of circular-succession incidence vectors by independent brute-force permutation enumeration for all \(2\le n\le9\), transforms them by an integer Walsh butterfly, and compares all frequencies with the closed formulas. Additional exact-integer formula and sign checks cover every \(2\le n\le200\), and a separate rational generating-series recurrence checks the full-weight formula through \(n=200\). The checker passed **21,975 assertions**. The finite computation supplements, but does not replace, the all-order proof in steps 1–4.

## Relationship to prior work
Diaconis, Evans and Graham (2013), Proposition 5.1, already established exchangeability and the **complete circular-succession-set distribution**, including the joint constraint enumeration used in step 1. That is acknowledged as prior work, not asserted novel. Their statements concern enumeration, bijections and limiting Poisson laws rather than the sign of every Walsh multiplier or an all-order convolution-inertia criterion. Du and Ji (2024) refine the linear (noncircular) succession–fixed-point bijection and associated statistics, not the present binary Fourier inertia. The present spectral classification adds the sign and positivity theorems that are not visibly stated in these inspected texts. It remains possible that an unindexed signed generating-function or cyclic-permutation paper contains an equivalent classification.

## Limitations
The statement concerns the complete symmetric group at the uniform counting weight and specifically cyclic value-and-position successions. It does not classify other permutation distributions or mixed weighted statistics. Formula-based spectral values and finite checks are not claims of independent validation; no independent audit has been performed. The prior publication of the entire circular-succession distribution makes the spectral theorem a consequence of known enumeration plus an additional all-order sign argument; historical priority remains bounded by the sources inspected.

## References
- Persi Diaconis, Steven N. Evans and Ron Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822 (1 August 2013), https://statistics.berkeley.edu/tech-reports/822 ; arXiv:1308.5459v1 (25 August 2013), https://arxiv.org/abs/1308.5459 . See Proposition 5.1 and Section 5.
- Lora R. Du and Kathy Q. Ji, *A Refinement of a Theorem of Diaconis-Evans-Graham*, arXiv:2404.00607 (31 March 2024), https://arxiv.org/abs/2404.00607 . See introduction and Theorem 1.4.
