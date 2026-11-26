# The complete ternary residue image and fibers of the ordered Bell numbers

## Finding
Let \(F_0=1\) and \(F_n=\sum_{j=0}^{n}j!S(n,j)\), where \(S(n,j)\) is a Stirling number of the second kind. For every \(k\ge2\), the exact set of residues represented by \(F_n\) modulo \(3^k\) is
\[
\{a\pmod{3^k}:a\equiv1\pmod3\}\;\cup\;
\{a\pmod{3^k}:a\equiv3\pmod9\}.
\]
Each such residue is attained infinitely often. The eventual least period is \(2\cdot3^{k-1}\); in each period, residues congruent to \(1\pmod3\) occur once each and residues congruent to \(3\pmod9\) occur three times each. No other residues occur. For \(k=1\), the represented classes are \(0,1\), once each in the eventual period two.

Consequently,
\[
\overline{\{F_n:n\ge0\}}^{(3)}=(1+3\mathbb Z_3)\cup(3+9\mathbb Z_3),
\qquad \mu=\frac49.
\]
The image has \(4\cdot3^{k-2}\) classes modulo \(3^k\) for \(k\ge2\).

More precisely, there exist continuous functions \(G_0,G_1:\mathbb Z_3\to\mathbb Z_3\) such that
\[
\nu_3(G_0(t)-G_0(s))=2+\nu_3(t-s),\qquad
\nu_3(G_1(t)-G_1(s))=1+\nu_3(t-s)
\]
for distinct \(s,t\in\mathbb Z_3\), and \(F_{2t+\epsilon}\equiv G_\epsilon(t)\pmod{3^k}\) whenever \(2t+\epsilon\ge k\) is a nonnegative integer. Their exact images are \(G_0(\mathbb Z_3)=3+9\mathbb Z_3\) and \(G_1(\mathbb Z_3)=1+3\mathbb Z_3\).

## Assumptions and scope
All indices \(n\) are nonnegative integers. \(\mathbb Z_3\) is the ring of ternary-adic integers, \(\nu_3(0)=+\infty\), and \(\mu\) is normalized additive Haar measure. The word *eventual* concerns the index sequence modulo a fixed \(3^k\). The initial value \(F_0=1\) belongs to the odd-index image but not to the even-index image; the interpolation assertion for actual terms requires the displayed index lower bound. No uniform-in-\(k\) onset is asserted.

## Proof
**1. A compatible measure.** For \(N=3^h\), and \(0\le r<N\), set
\[
\omega_N(r)=\frac{2^{N-1-r}}{2^N-1}\in\mathbb Z_3.
\]
The denominator is a ternary-adic unit because \(N\) is odd. The geometric identity \(2^{3N}-1=(2^N-1)(1+2^N+2^{2N})\) shows that summing the three weights over \(r,r+N,r+2N\) at level \(3N\) yields \(\omega_N(r)\). Hence the weights define a bounded \(\mathbb Z_3\)-valued measure \(\omega\) on \(\mathbb Z_3\), and the integral of every continuous \(\mathbb Z_3\)-valued function is defined by its finite weighted sums.

For a formal variable \(z\), the finite exponential generating function is
\[
\sum_{r=0}^{N-1}\omega_N(r)e^{rz}
=\frac{2^N-e^{Nz}}{(2^N-1)(2-e^z)}.
\]
Subtracting \((2-e^z)^{-1}=\sum_{n\ge0}F_nz^n/n!\) proves that the \(n\)-th finite moment differs from \(F_n\) by
\[
-\frac1{2^N-1}\sum_{j=1}^n\binom nj N^jF_{n-j},
\]
which is divisible by \(N\). Letting \(h\) increase establishes \(F_n=\int_{\mathbb Z_3}x^n\,d\omega(x)\).

**2. Interpolation on units.** Put \(U=\mathbb Z_3^\times\). On \(U\), \(x^2-1\in3\mathbb Z_3\). For \(\epsilon\in\{0,1\}\) define
\[
M_{\epsilon,j}=\int_U x^\epsilon(x^2-1)^j\,d\omega(x),\quad
G_\epsilon(t)=\sum_{j\ge0}\binom tj M_{\epsilon,j}.
\]
The series converges uniformly for \(t\in\mathbb Z_3\), since \(\nu_3(M_{\epsilon,j})\ge j\). For an ordinary integer \(t\ge0\), it is \(\int_Ux^{2t+\epsilon}\,d\omega(x)\). For \(n=2t+\epsilon\ge1\), the omitted nonunit integral belongs to \(3^n\mathbb Z_3\). Thus \(F_n\equiv G_\epsilon(t)\pmod{3^k}\) for \(n\ge k\).

**3. A finite certificate for the leading terms.** Since the integrands defining \(M_{\epsilon,j}\) are integer-valued and depend modulo 81 only on \(x\pmod{81}\), compatible weights give the following *exact* table modulo 81, with columns \(j=0,1,2,3\):
\[
\begin{array}{c|rrrr}
\epsilon&0&1&2&3\\\hline
0&12&72&0&0\\
1&52&15&54&54
\end{array}\pmod{81}.
\]
Each entry follows by summing \(2^{80-r}r^\epsilon(r^2-1)^j/(2^{81}-1)\) over \(1\le r<81\) with \(3\nmid r\). The accompanying standalone checker recomputes the table without external data.

For \(j\ge1\), the binomial polynomials satisfy
\[
\nu_3\!\left(\binom tj-\binom sj\right)
\ge\nu_3(t-s)-\lfloor\log_3j\rfloor.
\]
Indeed for integral \(s,t\), Vandermonde's identity and \(\ell\binom{t-s}{\ell}=(t-s)\binom{t-s-1}{\ell-1}\) give the bound; density extends it to ternary-adic arguments. For \(j\ge4\), \(j-\lfloor\log_3j\rfloor\ge3\). The table implies that, for distinct \(s,t\), the contribution of all \(j\ge2\) to \(G_0(t)-G_0(s)\) lies in \(27(t-s)\mathbb Z_3\), and to \(G_1(t)-G_1(s)\) lies in \(9(t-s)\mathbb Z_3\). Meanwhile \(\nu_3(M_{0,1})=2\) and \(\nu_3(M_{1,1})=1\). This proves both displayed exact distance formulas.

Since \(G_0(0)\equiv3\pmod9\) and \(G_1(0)\equiv1\pmod3\), the distance formulas show that the images are contained in the stated balls. Reducing modulo each \(3^k\), the distance formula also shows that \(G_\epsilon\) attains all the residue classes of that ball, so compactness gives equality of the full images.

**4. Actual values, fibers, and least periods.** All positive odd-index values lie in \(1+3\mathbb Z_3\); all positive even-index values lie in \(3+9\mathbb Z_3\), using the nonunit-error bound from step 2 (for even \(n\ge2\)). The exceptional \(F_0=1\) lies in the first ball. Conversely, for every \(k\) and every chosen argument \(t\pmod{3^{k-1}}\), arbitrarily large integers in that argument class give \(F_{2t+\epsilon}\equiv G_\epsilon(t)\pmod{3^k}\). Thus each ball is genuinely represented at every depth, infinitely often.

For \(k\ge2\), the odd-index branch is a bijection from \(t\pmod{3^{k-1}}\) to the \(3^{k-1}\) residues \(1\pmod3\). The even-index branch depends only on \(t\pmod{3^{k-2}}\) and takes every one of the \(3^{k-2}\) residues \(3\pmod9\); each is encountered three times when \(t\) runs modulo \(3^{k-1}\). The eventual period is therefore \(2\cdot3^{k-1}\), and is least because a period must preserve index parity modulo three and the odd branch forces its half to be divisible by \(3^{k-1}\). The \(k=1\) statement is immediate. The Haar measure is \(1/3+1/9=4/9\).

## Verification
Run `python3 check.py` using the standard Python library. It checks the exact 81-residue moment certificate, compatibility of finite moments with direct Stirling-number evaluations, and the full predicted residue histograms and periods through \(3^6\). It additionally verifies finite-level distance formulas for the two interpolation branches. These computations verify finite identities; the infinite statement is established by steps 1–4 above, not by extrapolating the finite tests.

## Relationship to prior work
Mező (arXiv:1308.1637, first publicly posted 2013-08-07) discusses Fubini numbers and periodicity modulo ten, not prime-power image/fiber classification. Caicedo–Moll–Ramírez–Villamizar (2019, §13, Proposition 61 and Theorem 62) prove the parity-dependent ternary valuation and record the six-term pattern modulo nine. Their conclusions give necessary residue restrictions, but do not prove that every residue in those two balls lifts, nor the exact all-depth fiber counts. Schreyer (2025, §4, Corollaries 10–11) establishes eventual Carmichael periods, including \(2\cdot3^{k-1}\), but not which residues occur within each period or their multiplicities. A related published prime-power index-shift study establishes preperiods; period/preperiod knowledge alone does not imply the claimed images or fiber counts.

## Limitations
This theorem concerns only the prime three and classical ordered Bell numbers, not arbitrary \(r\)-Fubini numbers, general primes, or arbitrary subsequences. It makes no new claim about the previously established modulo-nine residue pattern or the generic period formula alone. Historical priority remains subject to unlocated implicit equivalences in older work on Fubini congruences and ternary-adic distributions; novelty has not undergone independent audit.

## References
1. I. Mező, *Periodicity of the last digits of some combinatorial sequences*, arXiv:1308.1637, first posted 2013-08-07. https://arxiv.org/abs/1308.1637
2. J. B. Caicedo, V. H. Moll, J. L. Ramírez, D. Villamizar, *Extensions of set partitions and permutations*, Electron. J. Combin. 26 (2019), P2.20, §13. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i2p20/pdf/
3. B. Schreyer, *Rigged Horse Numbers and their Modular Periodicity*, J. Integer Sequences 28 (2025), Article 25.4.1, §4. https://cs.uwaterloo.ca/journals/JIS/VOL28/Schreyer/schreyer7.pdf
