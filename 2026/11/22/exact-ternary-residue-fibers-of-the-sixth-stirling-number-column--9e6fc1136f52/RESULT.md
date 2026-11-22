# Exact ternary residue fibers of the sixth Stirling-number column

## Finding
Let \(S(n,6)\) count partitions of an \(n\)-element set into six nonempty blocks. For every integer \(k\ge1\), put \(q=3^k\). There are canonical \(\delta\in3\mathbb Z_3\) and \(u\in\mathbb Z_3^\times\), with \(\delta\equiv21\pmod{27}\) and \(u\equiv2\pmod3\), such that in **each block of \(2q\) consecutive indices beginning at any integer \(a\ge\max\{6,k+2\}\)**, the count \(N_k(y)\) of indices with \(S(n,6)\equiv y\pmod q\) is
\[
\boxed{N_k(y)=1+\begin{cases}
3R_{k-1}\!\left(\dfrac{y-\delta}{3u}\bmod3^{k-1}\right),&y\equiv\delta\pmod3,\\
0,&y\not\equiv\delta\pmod3.
\end{cases}}
\]
Here \(R_m(z)=\#\{x\bmod3^m:x^2\equiv z\pmod{3^m}\}\), with \(R_0(0)=1\). Division by \(3u\) is performed only after \(y-\delta\) is divisible by three, followed by multiplication by the inverse of the unit \(u\) modulo \(3^{k-1}\). The constants are defined precisely in the proof.

Thus **every residue modulo every power of three occurs** among sufficiently late sixth-column values, with an exact, generally nonuniform multiplicity; the even-index branch hits every residue exactly once in each period, whereas the odd-index branch has the image
\[
\boxed{f_1(\mathbb Z_3)=\delta+3u\mathbb Z_3^2},
\]
where \(\mathbb Z_3^2\) is the set of 3-adic squares. The number of residue classes supported by the exceptional odd-index branch modulo \(3^k\) equals
\[
Q_{k-1},\qquad Q_0=1,\quad Q_m=1+\sum_{j=0}^{\lfloor(m-1)/2\rfloor}3^{m-2j-1}\quad(m\ge1).
\]
The odd-index image has 3-adic Haar measure \(1/8\). The natural density of indices with \(3\mid S(n,6)\) is exactly \(2/3\).

## Assumptions and scope
The index \(n\), precision \(k\), and block start \(a\) are integers with \(n\ge6\), \(k\ge1\), and \(a\ge\max\{6,k+2\}\). All residue counts concern arbitrary blocks of length \(2\cdot3^k\), not only blocks whose endpoints are aligned. The 3-adic base powers \(25^t\), \(16^t\), and \(4^t\) at \(t\in\mathbb Z_3\) mean their standard convergent binomial/exponential interpolations, since all bases are congruent to one modulo three. An expression such as \(\delta+3u\mathbb Z_3^2\) is a translate of a *scaled set of squares*, not a residue ball or ideal. This claim is about a fixed Stirling column, not the sixth binomial-coefficient polynomial.

## Proof
**1. Exact exponential formula and analytic parity branches.** Inclusion–exclusion gives for every integer \(n\ge6\)
\[
720S(n,6)=6^n-6\cdot5^n+15\cdot4^n-20\cdot3^n+15\cdot2^n-6.
\]
For \(t\in\mathbb Z_3\), define
\[
\begin{aligned}
f_0(t)&=\frac{-2\cdot25^t+5\cdot16^t+5\cdot4^t-2}{240},\\
f_1(t)&=\frac{-5\cdot25^t+10\cdot16^t+5\cdot4^t-1}{120}.
\end{aligned}
\]
These are 3-adic integer-valued analytic functions, as the expansions below prove. For integer \(n\ge\max\{6,k+2\}\), with \(j=n\bmod2\) and \(t=(n-j)/2\), the terms \(6^n\) and \(20\cdot3^n\) disappear modulo \(3^{k+2}\). Since \(\nu_3(720)=2\), the identity implies
\[
S(n,6)\equiv f_j(t)\pmod{3^k}.
\]
Each block of \(2\cdot3^k\) successive integers supplies, independently for each parity, exactly one representative of every \(t\bmod3^k\).

**2. The even branch is a 3-adic isometry.** Let \(A=\log25\), \(B=\log16\), and \(C=\log4\). Each has valuation one. The Taylor coefficient of \(t^m\) in \(f_0\), for \(m\ge1\), is
\[
\frac{-2A^m+5B^m+5C^m}{240m!}.
\]
For \(m\ge2\), its 3-adic valuation is at least \(m-1-\nu_3(m!)\ge1\). The linear coefficient is a 3-adic unit congruent to one modulo three: \((A/3,B/3,C/3)\equiv(2,2,1)\pmod3\) gives \((-4+10+5)/80\equiv1\pmod3\). Thus \(f_0(t)=c_0+t+3H(t)\) for a restricted integral 3-adic power series \(H\). For any \(s,t\in\mathbb Z_3\), the difference \(H(t)-H(s)\) is divisible by \(t-s\), so
\[
\nu_3(f_0(t)-f_0(s))=\nu_3(t-s).
\]
It follows that \(f_0\) induces a permutation of \(\mathbb Z/3^k\mathbb Z\) for every \(k\) and a bijection of \(\mathbb Z_3\).

**3. A unique quadratic critical point on the odd branch.** Put \(g(t)=f_1(t)/3\). Its Taylor coefficients are
\[
[g]_{t^m}=\frac{-5A^m+10B^m+5C^m}{360m!}\ (m\ge1),\qquad g(0)=1/40.
\]
The congruences \((A,B,C)\equiv(24,15,21)\pmod{27}\) give \(-5A+10B+5C\equiv0\pmod{27}\), hence the linear coefficient lies in \(3\mathbb Z_3\). A direct reduction of the quadratic coefficient yields \([g]_{t^2}\equiv2\pmod3\). For \(m\ge4\), the valuations are at least \(m-2-\nu_3(m!)\ge1\). The same holds for \(m=3\) because \(-5(A/3)^3+10(B/3)^3+5(C/3)^3\equiv0\pmod3\). Consequently
\[
g(t)\equiv1/40+2t^2\pmod{3\mathbb Z_3\langle t\rangle},\qquad g'(t)\equiv t\pmod3,\qquad g''(t)\equiv1\pmod3.
\]
The derivative \(g'\) is a 3-adic isometry of \(\mathbb Z_3\): the coefficient of \(t\) is a unit and all nonlinear coefficients are divisible by three. Therefore it has a *unique* root \(\alpha\in3\mathbb Z_3\). Define
\[
\delta=3g(\alpha)=f_1(\alpha),\qquad u=g''(\alpha)/2\in\mathbb Z_3^\times.
\]
Then \(u\equiv2\pmod3\). Since \(\alpha\equiv0\pmod3\) and \([g]_{t}\in3\mathbb Z_3\), \(g(\alpha)\equiv g(0)=1/40\pmod9\), whence \(\delta\equiv3/40\equiv21\pmod{27}\).

**4. Exact quadratic normal form, not just a local approximation.** Taylor expansion about \(\alpha\) gives
\[
g(\alpha+s)=g(\alpha)+s^2U(s),\qquad U(s)\in\mathbb Z_3\langle s\rangle,\quad U(s)\equiv u\pmod3.
\]
The analytic function \(U(s)/u\) is in \(1+3\mathbb Z_3\langle s\rangle\) and has a unique analytic square root \(H(s)\in1+3\mathbb Z_3\langle s\rangle\). Its difference quotients are multiples of three, so \(\phi(s)=sH(s)\) satisfies \(\nu_3(\phi(s)-\phi(t))=\nu_3(s-t)\). It induces permutations at every finite 3-power level and hence maps \(\mathbb Z_3\) bijectively to itself. Therefore
\[
f_1(\alpha+s)=\delta+3u\phi(s)^2,\qquad f_1(\mathbb Z_3)=\delta+3u\mathbb Z_3^2.
\]
At level \(3^k\), each square-root solution \(x\bmod3^{k-1}\) has exactly three lifts \(\bmod3^k\) under the isometry \(\phi\), proving that the odd-index fiber count is exactly \(3R_{k-1}\), with zero outside the displayed square image.

**5. Combining branches, support sizes, and measure.** The even branch contributes exactly one preimage per residue in the period, and the odd branch contributes the fibers from step 4. This yields the claimed expression for \(N_k(y)\) and full residue support. A nonzero square modulo \(3^m\) has an even 3-adic valuation \(2j<m\), and for each \(j\) there are exactly \(3^{m-2j-1}\) such distinct residues; adding zero proves the formula for \(Q_m\). The set of 3-adic squares has measure \(\tfrac13\sum_{j\ge0}3^{-2j}=3/8\). Multiplying by three scales Haar measure by \(1/3\), so the odd branch image has measure \(1/8\). Modulo three, every even-branch residue appears once while the odd branch contributes three occurrences of residue zero. Thus four of six indices per period satisfy divisibility by three, giving density \(2/3\). This completes the proof.

## Verification
The standalone Python 3 script `verify.py` uses only the standard library. It computes 3-adic logarithms with certified modular divisions, Hensel-lifts the unique critical point, checks complete even-branch permutations and odd-branch square-image fiber histograms for each \(1\le k\le7\), and compares the analytic expressions with exact Stirling inclusion–exclusion at lower levels. It independently checks the inclusion–exclusion identity against the ordinary Stirling recurrence for 42 rows. Expected output concludes:

```
VERIFY_OK levels=1..7 direct_stirling_checks=726 critical_lifts=PASS square_fiber_histograms=PASS
```

These are exhaustive *finite-modulus* checks only. All-precision validity follows from the coefficient valuations, 3-adic isometries, and quadratic normal form proved above.

## Relationship to prior work
Kwong established the least eventual period of fixed Stirling columns modulo prime powers; his theorem already gives \(2\cdot3^k\) for the sixth column modulo \(3^k\), and the period is **not** claimed as new here. Sun's Stirling congruences handle related prime-modulus and binomial congruence phenomena; Davis studies p-adic limits and valuations of other families of Stirling numbers. The closest published evaluated fiber theorem concerns the **fifth** Stirling column modulo powers of **two**, whose two parity branches are isometries and whose fibers are uniform. This result instead classifies the sixth column modulo powers of **three**, where one branch is an isometry and the other folds into an exact quadratic image. A related sixth **binomial-polynomial** image theorem also has 3-adic quadratic components, but the object, formula, and asserted fibers are different; that theorem does not imply the result here.

## Limitations
The theorem concerns only the sixth fixed Stirling column and the prime three. It does not claim an analogous classification for all columns or primes. The constants \(\delta\) and \(u\) are defined canonically by an analytic critical point rather than by rational closed forms. Finite computations are not infinite proofs. Though primary and indexed sources were compared for aliasing and stronger coverage, an unindexed earlier evaluation in broader fixed-column literature remains a priority risk. No independent mathematical audit has been performed.

## References
- Y. H. Harris Kwong, *Minimum Periods of S(n,k) Modulo M*, Fibonacci Quarterly 27 (1989), 217–221, https://www.fq.math.ca/Scanned/27-3/kwong.pdf .
- Zhi-Wei Sun, *Combinatorial congruences and Stirling numbers*, public preprint 5 December 2005, https://arxiv.org/abs/math/0512071 .
- D. M. Davis, *p-adic Stirling numbers of second kind*, public preprint 29 July 2013, https://arxiv.org/abs/1307.7687 .
- D. M. Davis, *Divisibility by 2 and 3 of certain Stirling numbers*, public preprint 2008, https://arxiv.org/abs/0807.2629 .
- *Uniform binary residue fibers of the fifth Stirling column with sharp preperiod*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-uniform-binary-residue-fibers-of-the-fifth-stirling-column-with--a900c8064e91 .
- *Exact ternary residue images of the sixth binomial polynomial*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-residue-images-of-the-sixth-binomial-polynomial--2c5deda1b9d1 .
