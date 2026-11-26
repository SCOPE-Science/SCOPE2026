# Complete dyadic residue fibers of the eighth Stirling-number column

## Finding
Let \(S(n,8)\) denote the number of partitions of an \(n\)-element labelled set into exactly eight nonempty blocks. For an integer \(k\ge 1\), put \(q=2^k\) and \(N_k=\max\{8,k+5\}\). For every \(n\ge N_k\), the residue \(S(n,8)\bmod q\) has least eventual period exactly \(2q\). For each residue \(y\in\mathbb Z/q\mathbb Z\), the number of representatives in **any** block of \(2q\) consecutive indices starting at \(n\ge N_k\) is
\[
R_k(y)=
\begin{cases}
1+4\mathbf1_{y\equiv0\pmod4},&k\ge2,\\
3,&k=1\text{ and }y=0,\\
1,&k=1\text{ and }y=1.
\end{cases}
\]
In particular, every residue is attained infinitely often. The natural index distribution in \(\mathbb Z_2\) has a density relative to normalized additive Haar measure given by
\[
\rho(y)=\frac12+2\mathbf1_{4\mathbb Z_2}(y).
\]
This exactly distinguishes a universally distributed even-index branch from a fourfold-concentrated odd-index branch.

## Assumptions and scope
The Stirling numbers satisfy \(S(0,0)=1\), \(S(n,0)=0\) for \(n>0\), \(S(n,j)=0\) for \(n<j\), and \(S(n+1,j)=jS(n,j)+S(n,j-1)\). The valuation \(\nu_2\) is the exponent of two dividing a nonzero rational or integer. All congruences and counts refer to ordinary nonnegative integer indices, unless explicitly extended to the ring \(\mathbb Z_2\) of 2-adic integers. The cutoff \(N_k\) is sufficient; it is not claimed to be the smallest possible preperiod.

## Proof
**1. Exact eventual interpolation.** Inclusion-exclusion gives
\[
8!S(n,8)=8^n-8\cdot7^n+28\cdot6^n-56\cdot5^n+70\cdot4^n-56\cdot3^n+28\cdot2^n-8
\]
for \(n\ge1\). Since \(8!=2^7\cdot315\), set
\[
F(n)=-\frac{7^n+7\cdot5^n+7\cdot3^n+1}{16\cdot315}.
\]
Its numerator is divisible by \(16\) for every nonnegative integer \(n\). The omitted even-base terms show, for \(n\ge8\),
\[
\nu_2\bigl(S(n,8)-F(n)\bigr)\ge n-5,
\]
where the left side is understood as infinite for zero. Indeed each of the four omitted summands, divided by \(8!\), has valuation at least \(n-5\). Hence \(S(n,8)\equiv F(n)\pmod{2^k}\) once \(n\ge N_k\).

**2. Two 2-adic isometries.** For \(t\in\mathbb Z_{\ge0}\), define
\[
G(t)=F(2t),\qquad H(t)=\frac{F(2t+1)}4.
\]
Both are 2-adic integers. Expanding \(49^t=(1+48)^t\), \(25^t=(1+24)^t\), and \(9^t=(1+8)^t\) gives convergent binomial series over \(\mathbb Z_2\):
\[
G(t)=-\frac1{315}\left(1+17t+424\binom t2+\sum_{j\ge3}g_j\binom tj\right),
\]
\[
H(t)=-\frac1{315}\left(1+21t+588\binom t2+\sum_{j\ge3}h_j\binom tj\right).
\]
The explicit coefficients are
\[
 g_j=\frac{48^j+7\cdot24^j+7\cdot8^j}{16},\qquad
 h_j=\frac{7\cdot48^j+35\cdot24^j+21\cdot8^j}{64},\quad j\ge1.
\]
For every \(j\ge3\), \(\nu_2(g_j)\ge3j-4\) and \(\nu_2(h_j)\ge3j-6\); also \(\nu_2(g_2)=3\) and \(\nu_2(h_2)=2\). For integers \(t>s\ge0\), Vandermonde's identity and \(\binom dj=(d/j)\binom{d-1}{j-1}\) imply
\[
\nu_2\!\left(\binom tj-\binom sj\right)
 \ge \nu_2(t-s)-\lfloor\log_2j\rfloor\qquad(j\ge1).
\]
Consequently every nonlinear term in each series has difference divisible by \(2^{1+\nu_2(t-s)}\), whereas the linear coefficient \(17\) or \(21\), divided by odd \(315\), is a 2-adic unit. Thus, for all distinct nonnegative \(t,s\),
\[
\nu_2(G(t)-G(s))=\nu_2(t-s),\qquad
\nu_2(H(t)-H(s))=\nu_2(t-s).
\]
Convergence extends both maps to distance-preserving maps \(\mathbb Z_2\to\mathbb Z_2\). At every modulus \(2^k\), a distance-preserving self-map of the \(2^k\) index classes is injective and hence bijective. Therefore \(G\) and \(H\) each permute all classes modulo every power of two, while \(F(2t+1)=4H(t)\).

**3. Complete fibers and least period.** As \(n\) runs through a block of \(2^{k+1}\) consecutive integers, it contains \(2^k\) even indices \(2t\), with \(t\) covering each residue modulo \(2^k\) once, and \(2^k\) odd indices \(2t+1\), likewise. The even values \(G(t)\) hit each target once. For \(k\ge2\), the odd values \(4H(t)\) hit each multiple-of-four target exactly four times and no other target. At \(k=1\), the odd values are both zero, yielding counts \(3,1\). This proves the stated fibers and the period \(2^{k+1}\).

To show minimality, an odd index shift cannot be a period: odd-index values are always even, while the even branch has some odd values in every sufficiently long block. Any even period \(2d\) would force \(G(t+d)\equiv G(t)\pmod{2^k}\) at all sufficiently large \(t\). The isometry forces \(2^k\mid d\), proving least eventual period \(2^{k+1}\).

**4. Density on the 2-adic integers.** The fiber counts are consistent under reduction of the modulus. Every even index contributes the Haar law, and every odd index contributes the normalized Haar law on \(4\mathbb Z_2\), each at weight one half. Relative to full Haar measure, this is precisely \(\rho(y)=1/2+2\mathbf1_{4\mathbb Z_2}(y)\). Periodicity proves all these natural index frequencies at each finite precision.

## Verification
The standalone `check.py` uses the Stirling recurrence to compare the exact interpolation, the least candidate periods, each output histogram, and the parity-branch valuation formulas through finite moduli. Run `python3 check.py` from the extracted files. The code is a diagnostic check; the universal conclusions follow from the preceding proof and the explicit binomial coefficient bounds. The sufficient preperiod is not asserted sharp.

## Relationship to prior work
Kwong established the eventual minimal modular periods for fixed Stirling columns. Amdeberhan–Manna–Moll studied the 2-adic valuations of Stirling numbers, and Bennett–Mosteig classified the structure of valuation-variable index classes up to column twenty; the latter includes the eighth column. Their valuation statements do not themselves identify the fibers of all output residues. Davis studied 2-adic partial Stirling interpolations and zeros. The result here concerns the full output pushforward law for a fixed natural column and an explicit 2-adic bijective decomposition, not merely eventual periodicity or the locations of zeros. Existing exact output-fiber results for other sequences or other Stirling columns have different domains and do not imply this particular classification.

## Limitations
No assertion is made about the first \(N_k\) initial indices, the sharp preperiod, other Stirling columns, or prime-power moduli with odd primes. Although closely related original work was inspected, the possibility of an unindexed earlier equivalent result is not ruled out by search failure.

## References
1. T. Amdeberhan, D. Manna, V. H. Moll, *The 2-adic valuations of Stirling numbers*, first arXiv version 20 July 2007, https://arxiv.org/abs/0707.3104.
2. C. Bennett, E. Mosteig, *Congruence classes of 2-adic valuations of Stirling numbers of the second kind*, arXiv version 28 April 2012, https://arxiv.org/abs/1204.6361; *Journal of Integer Sequences* 16 (2013), Article 13.3.6.
3. Y. H. H. Kwong, *Minimum periods of \(S(n,k)\) modulo \(M\)*, *Fibonacci Quarterly* 27 (1989), 217–221, https://www.fq.math.ca/Scanned/27-3/kwong.pdf.
4. D. M. Davis, *2-adic partial Stirling functions and their zeros*, arXiv version 3 February 2014, https://arxiv.org/abs/1402.0433.
