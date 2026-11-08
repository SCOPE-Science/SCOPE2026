# A two-adic tail bound proving Davis's reciprocal-binomial digit-sum conjecture

## Finding
Let \(f(n)=\sum_{j=0}^{n}\binom{n}{j}^{-1}\), let \(s_2(n)\) be the number of ones in the binary expansion of \(n\), and let \(\nu_2\) be the 2-adic valuation, with \(\nu_2(0)=+\infty\). For **every pair of integers \(n\ge0\), \(h\ge1\)**,
\[
\nu_2\bigl(f(n+h)-f(n)\bigr)\ge \nu_2(h)-s_2(n)-s_2(n+h)-1. \tag{1}
\]
In particular, for all integers \(e\ge1\) and \(0\le k<2^e\), the two binary supports of \(k\) and \(2^e\) are disjoint, so \(s_2(k+2^e)=s_2(k)+1\). Hence
\[
\boxed{\nu_2\bigl(f(2^e+k)-f(k)\bigr)\ge e-2s_2(k)-2.} \tag{2}
\]
This is precisely Conjecture 1.2 of Donald M. Davis (2013), which was previously verified there only for \(e\le15\). By Davis's Proposition 1.3, the convergence consequence also becomes unconditional: for any \(x\in\mathbb Z_2\) whose difference between counts of binary zeros and ones in its first \(j\) digits tends to \(+\infty\), the sequence \(f(x\bmod 2^j)\) converges in \(\mathbb Q_2\).

## Assumptions and scope
All binomial coefficients have integer upper argument \(n\ge0\). The valuation is defined on rational numbers by the exponent of two and extended by \(\nu_2(0)=+\infty\). The two-adic series appearing below converge in \(\mathbb Q_2\); there is no claim that \(f\) extends continuously to all of \(\mathbb Z_2\). The stronger inequality (1) holds for arbitrary positive integer shifts \(h\), not only dyadic shifts. We do not claim to settle the different, more precise odd-argument Conjecture 1.4 in Davis (2013).

## Proof
**Step 1: a finite reciprocal-binomial identity.** The classical identity (known from Rockett's work and reproduced in the 2009 exposition of Apagodu and Zeilberger) is
\[
f(n)=\frac{n+1}{2^{n+1}}\sum_{j=1}^{n+1}\frac{2^j}{j}\quad(n\ge0). \tag{3}
\]
For completeness, \(f(0)=1\), and for \(n\ge1\) symmetry of the summands gives
\[
f(n)=1+\frac1n\sum_{j=0}^{n-1}\frac{j+1}{\binom{n-1}{j}}=1+\frac{n+1}{2n}f(n-1).
\]
The right side of (3) satisfies the same recurrence and initial value, proving (3).

**Step 2: an exact convergent tail identity.** In \(\mathbb Q_2\),
\[
\sum_{j=1}^{\infty}\frac{2^j}{j}=-\log_2(1-2)=-\log_2(-1)=0. \tag{4}
\]
Here \(\log_2\) is the *2-adic logarithm*, not a real logarithm to base two. The power series converges because \(j-\nu_2(j)\to+\infty\), and the 2-adic logarithm is additive on \(1+2\mathbb Z_2\). Since \((-1)^2=1\), its value at \(-1\) is zero. Subtract the initial segment in (3) from (4) and put \(j=n+1+i\) to obtain
\[
\boxed{f(n)=-(n+1)\sum_{i=1}^{\infty}\frac{2^i}{n+1+i}.} \tag{5}
\]
The sum converges because \(i-\nu_2(n+1+i)\to\infty\).

**Step 3: subtract at arbitrary shifts.** From (5), for integers \(n\ge0,h\ge1\), exact subtraction gives
\[
\begin{aligned}
f(n+h)-f(n)
&=-\sum_{i=1}^{\infty}2^i\left(\frac{n+h+1}{n+h+1+i}-\frac{n+1}{n+1+i}\right)\\
&=-h\sum_{i=1}^{\infty}\frac{i2^i}{(n+1+i)(n+h+1+i)}. \tag{6}
\end{aligned}
\]
The second identity follows by cross-multiplication; termwise subtraction is permitted by convergence.

**Step 4: the binary denominator lemma.** For every pair of integers \(u\ge0,v\ge1\),
\[
\boxed{\nu_2(u+v)\le s_2(u)+s_2(v-1).} \tag{7}
\]
Indeed \(\nu_2(u+v)\) is the number of trailing ones in the binary expansion of \(u+v-1\). That number is at most \(s_2(u+v-1)\), which in turn is at most \(s_2(u)+s_2(v-1)\), because binary addition cannot increase the total number of one-bits. Apply (7) with \(u=n\) and \(u=n+h\), both with \(v=i+1\):
\[
\nu_2(n+1+i)\le s_2(n)+s_2(i),\qquad
\nu_2(n+h+1+i)\le s_2(n+h)+s_2(i). \tag{8}
\]
For every integer \(i\ge1\), also
\[
2s_2(i)\le i+1. \tag{9}
\]
To see this, an integer with \(r=s_2(i)\ge1\) one-bits is at least \(2^r-1\), and \(2^r\ge2r\) for \(r\ge1\).

**Step 5: valuation of each summand.** Combining (8) and (9), each nonzero summand in (6) has valuation
\[
\begin{aligned}
&\nu_2(h)+i+\nu_2(i)-\nu_2(n+1+i)-\nu_2(n+h+1+i)\\
&\quad\ge\nu_2(h)+i+\nu_2(i)-s_2(n)-s_2(n+h)-2s_2(i)\\
&\quad\ge\nu_2(h)-s_2(n)-s_2(n+h)-1.
\end{aligned}
\]
Because the series converges, the ultrametric triangle inequality preserves this uniform lower bound for its sum. This proves (1), hence (2). Davis's proof of Proposition 1.3, based on the successive \(2^e\)-bit additions, now applies with proved rather than conjectured (2). This completes the proof.

## Verification
Run the standalone script `python3 verify.py`. Its independent exact-fraction checks compare (3) to direct inverse-binomial sums for \(0\le n<85\); test (1) on 10,000 pairs \(0\le n<100,1\le h\le100\); test (2) for all \(1\le e\le8\) and \(0\le k<2^e\) (510 pairs); test lemma (7) on 39,800 pairs; and compare the 2-adic tail (5) to 100 bits of precision in 25 cases. The script is corroboration, not a proof for unbounded arguments; the proof is Steps 1–5.

## Relationship to prior work
Davis's 2012 paper, arXiv:1208.0250, proved the weaker estimate \(\nu_2(f(2^e+k)-f(k))\ge e-k-1\) for \(0\le k<2^e\) in its formula (4.8), and consequently proved 2-definability only for extremely sparse one-bits (Theorem 1.12). Davis's 2013 paper, arXiv:1301.2532v1, explicitly formulated (2) as Conjecture 1.2 and established its consequence only conditionally (Proposition 1.3). Inequality (1) proves that open statement and goes further by allowing arbitrary positive shifts. The finite identity (3), digit-count bounds, and 2-adic logarithm are standard inputs, not new claims.

The particular 2013 odd-argument Conjecture 1.4 asserts a different, often sharper bound, and is not asserted to follow from (2). A failure to locate another proof in searched literature does not certify chronological priority; an unlocated later proof remains possible.

## Limitations
The bound is an inequality, not an exact valuation formula for every pair. It does not classify all two-adic integers for which \(f\) is definable, nor does it resolve every problem raised in Davis (2013). No independent audit or priority certification has been performed. The identified earlier sources are directly compared, but historical literature searches cannot rule out an unindexed equivalent.

## References
- D. M. Davis, *For which p-adic integers x can the sum of inverse binomial coefficients be defined?*, arXiv:1208.0250v1, first posted 1 August 2012, especially Theorem 1.12 and (4.8): https://arxiv.org/html/1208.0250v1 .
- D. M. Davis, *For which 2-adic integers x can the sum of inverse binomial coefficients be defined?*, arXiv:1301.2532v1, first posted 11 January 2013, especially Conjecture 1.2 and Proposition 1.3: https://arxiv.org/html/1301.2532v1 .
- M. Apagodu and D. Zeilberger, *Some Nice Sums Are Almost As Nice If You Turn Them Upside Down*, written 17 July 2009, https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/upsidedown.html ; notes Rockett's 1981 reciprocal-binomial identity.
