# A golden-mean entropy plateau with a sharp half-density jump in frequency shifts

## Finding

Let \(\Sigma(p)\) be the Becker–Baraviera one-sided binary frequency shift (defined below), and put \(\varphi=(1+\sqrt5)/2\). For **every real** \(0<p<1/2\), including rational and irrational parameters,

\[
 h_{\mathrm{top}}(\Sigma(p))=\log\varphi.
\]

More generally, for all \(0<p<1\) and integers \(n\ge1\), its length-\(n\) language satisfies the parameter-uniform estimate

\[
 \#\mathcal L_n(\Sigma(p))\le(n^2+n-1)F_{n+2},
\]

where \(F_0=0,F_1=1,F_{m+2}=F_{m+1}+F_m\). In particular \(h_{\mathrm{top}}(\Sigma(p))\le\log\varphi\) for the entire open parameter interval. At the boundary \(p=1/2\), Reyes's exact entropy theorem gives \(h_{\mathrm{top}}(\Sigma(1/2))=(\log2)/2\). Hence the entropy function has a strict downward jump at that parameter:

\[
 \lim_{p\uparrow1/2}h_{\mathrm{top}}(\Sigma(p))-h_{\mathrm{top}}(\Sigma(1/2))
 =\log\varphi-\tfrac12\log2>0.
\]

The plateau and uniform language estimate are proved here; the boundary value at \(1/2\) is explicitly attributed to the cited preprint.

## Assumptions and scope

For a finite binary word \(w\), write \(|w|_0\) and \(|w|_1\) for its digit counts. Fix \(p\in(0,1)\) and \(\beta=p/(1-p)\). A one-sided infinite binary word \(x=x_1x_2\ldots\) belongs to \(P(p)\) if after each position \(i\) occupied by \(1\), the next digit is required to be \(1\) when the prefix density \(|x_1\cdots x_i|_1/i\) is at most \(p\), and is required to be \(0\) otherwise. Either next digit is permitted after \(0\). Let \(\sigma\) be the one-sided left shift and

\[
 \Sigma(p)=\overline{\bigcup_{j\ge0}\sigma^jP(p)}.
\]

The closure is in the product topology. The length-\(n\) language \(\mathcal L_n(\Sigma(p))\) consists of all length-\(n\) factors occurring in \(\Sigma(p)\). Entropy is \(\lim_{n\to\infty}n^{-1}\log\#\mathcal L_n\), with natural logarithms. The comparison golden-mean shift \(G\) consists of all infinite binary sequences with no adjacent \(1\)'s.

## Proof

**1. A uniform Fibonacci bound at fixed starting discrepancy.** Define \(D(w)=\beta|w|_0-|w|_1\). Every appended \(0\) raises \(D\) by \(\beta\) and every appended \(1\) lowers it by \(1\). A \(1\) forces the next digit to be \(1\) exactly when the discrepancy *after that 1* is nonnegative, and forces \(0\) otherwise.

For any real offset \(d\), let \(C_n(d)\) denote the set of length-\(n\) words that obey the rule whenever both a \(1\) and its follower lie in the word, taking \(d\) as the discrepancy before its first digit. There is no restriction on the first digit or on the follower of the final digit. Let \(b_n=\sup_{d\in\mathbb R}\#C_n(d)\). Then \(b_0=1\), \(b_1=2\), and for \(n\ge2\) the first-digit \(0\) branch has at most \(b_{n-1}\) completions, whereas the first-digit \(1\) branch fixes the second digit uniquely and thus has at most \(b_{n-2}\) completions. Consequently \(b_n\le b_{n-1}+b_{n-2}\), and induction gives

\[
 \#C_n(d)\le F_{n+2}\qquad(d\in\mathbb R,\ n\ge0).
\]

**2. Only polynomially many offset regimes.** The outcome of any forced transition after an interior \(1\) is determined by the sign of \(d+\beta z-o\), with \(z+o=i\) the digit counts through some prefix of length \(1\le i<n\). Thus the possible transition decisions change only at the offsets \(d=o-\beta z\). The number of such values is at most

\[
 M_n=\sum_{i=1}^{n-1}(i+1)=\frac{(n-1)(n+2)}2.
\]

The real line, partitioned into the singleton threshold points and the open intervals between them, has at most \(2M_n+1=n^2+n-1\) regimes. Every \(C_n(d)\) is identical throughout each regime, including boundary regimes where equality forces \(1\). Therefore

\[
 \#\bigcup_{d\in\mathbb R}C_n(d)\le(n^2+n-1)F_{n+2}.
\]

Every length-\(n\) factor of a sequence in \(P(p)\) lies in \(C_n(d)\) for the discrepancy \(d\) accumulated before the factor. Taking shifts and then product-topology closure introduces no new finite words. Hence \(\mathcal L_n(\Sigma(p))\subset\bigcup_d C_n(d)\), proving the claimed count. Since \(F_{n+2}^{1/n}\to\varphi\) and polynomial factors do not change exponential growth, it follows that \(h_{\mathrm{top}}(\Sigma(p))\le\log\varphi\) for every \(p\in(0,1)\).

**3. A full golden-mean subshift below half density.** Suppose \(0<p<1/2\), so \(0<\beta<1\). The infinite prefix \((10)^N\) obeys the rule: after each \(1\) the discrepancy is negative, so \(0\) is required and supplied. After \(N\) pairs the discrepancy equals \(N(\beta-1)\), tending to minus infinity as \(N\to\infty\).

Fix any finite word \(w\) with no adjacent \(1\)'s. Choose \(N\) so large that \(N(\beta-1)<-|w|-1\), and consider the infinite word \((10)^Nw0^\infty\). During \(w\), every partial discrepancy remains strictly negative, because each digit raises it by at most \(\beta<1\). Thus every \(1\) in \(w\) forces a \(0\), which is already the next digit within \(w\), or is the initial trailing digit of \(0^\infty\). The same holds across the two other junctions: the prefix ends with \(0\), and the tail has only \(0\)'s. The infinite word lies in \(P(p)\), and \(w\) occurs as its factor.

Thus every factor of the golden-mean shift \(G\) occurs in \(\Sigma(p)\). Equivalently \(G\subset\Sigma(p)\) because \(\Sigma(p)\) is closed, and consequently

\[
 \#\mathcal L_n(\Sigma(p))\ge\#\mathcal L_n(G)=F_{n+2}.
\]

Combining this with Step 2 and taking exponential growth rates proves \(h_{\mathrm{top}}(\Sigma(p))=\log\varphi\) for all \(0<p<1/2\).

**4. Boundary jump.** Reyes, Proposition 6.6 / Theorem C(c), explicitly computes \(h_{\mathrm{top}}(\Sigma(k/(k+1)))=(\log2)/(k+1)\) for positive integers \(k\). Setting \(k=1\) yields the stated value at \(p=1/2\). Finally \(\varphi>\sqrt2\), so the discontinuity has strictly positive size. No claim about the right-hand parameter limit is needed.

## Verification

A self-contained Python checker supplied as `entropy_plateau_check.py` enumerates all binary words through length \(14\) at five rational parameters; it compares feasible-offset language counts with the explicit polynomial-Fibonacci bound, checks fixed-offset Fibonacci bounds, and tests all golden-mean words through this length by extending them from a sufficiently negative discrepancy. It also computes the two competing entropy constants. Running `python entropy_plateau_check.py` completes with `PASS`. These finite checks corroborate the algebra and boundary cases; the above counting and extension arguments provide the infinite proof.

## Relationship to prior work

Becker and Baraviera introduced the frequency shifts and established positive entropy and several structural results. Reyes established non-soficity and absence of weak specification for all interior parameters, and the exact entropy at rational parameters \(k/(k+1)\) with integer \(k\ge1\). His theorem supplies the boundary value at \(1/2\) but does not supply the low-density plateau. The new content here is a uniform polynomial-Fibonacci language bound for arbitrary real \(p\), the golden-mean inclusion and exact entropy on the entire open interval below half, and the resulting entropy jump. Classical Fibonacci counting is used as a tool; the nontrivial point is its applicability to a shift whose local rule depends on an unbounded historical discrepancy.

## Limitations

The theorem does not determine exact entropy for \(p>1/2\), nor the measure(s) of maximal entropy below half. The polynomial language bound is not asserted to be sharp. Historical priority remains uncertain because the full text of the 2023 Becker–Baraviera paper could not be accessed; comparison used its abstract and Reyes's detailed account of its entropy results. The result is mathematically checked in the accompanying argument and finite program, not independently validated.

## References

1. C. Reyes, *Frequency shifts: non-soficity, absence of specification and intrinsic ergodicity*, arXiv:2611.10995v1, first posted 2026-11-07, especially Definition 2.2, the discrepancy lemma, Theorem C(c), Proposition 6.6, and Remark 6.7. https://arxiv.org/html/2611.10995v1
2. A. J. Becker and A. T. Baraviera, *Symbolic Systems with Prescribed Partial Digit Density*, Journal of Statistical Physics 190 (2023), article 143, DOI: 10.1007/s10955-023-03158-8. Full manuscript was not accessible for direct comparison.
