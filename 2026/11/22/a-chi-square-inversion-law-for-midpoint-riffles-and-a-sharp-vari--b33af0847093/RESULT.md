# A chi-square inversion law for midpoint riffles and a sharp variance contrast with classical riffles

## Finding

Start with the ordered deck \(1,\ldots,n\), \(n\ge2\). Draw \(K\sim\operatorname{Bin}(n,1/2)\), cut after position \(K\), and merge the two increasing packets by increasing normalized card-midpoint positions, tossing independent fair coins for each cross-packet equality. Let \(I_n\) be the number of inversions in the resulting deck, and let \(T_n(k)\) be the count of equal cross-packet midpoints at cut \(k\) (with \(T_n(0)=T_n(n)=0\)).

**Exact inversion-law theorem.** For every \(n\ge2\) and \(0\le k\le n\),
\[
I_n\mid\{K=k\}\ \overset{d}=\ \frac{k(n-k)-T_n(k)}{2}+\operatorname{Bin}(T_n(k),1/2).
\]
In particular, for every **odd** \(n\ge3\), there are no ties, \(I_n=K(n-K)/2\) almost surely, and the complete distribution is
\[
\Pr\left(I_n=\frac{k(n-k)}2\right)=2^{1-n}\binom nk,
\qquad 0\le k\le \frac{n-1}{2}.
\]
For either parity, the exact mean is \(\mathbb EI_n=n(n-1)/8\), and
\[
\operatorname{Var}(I_n)=\frac{n(n-1)}{32}+\frac14\mathbb E T_n(K).
\]
For odd \(n\), the second term vanishes. For all \(n\to\infty\), including even and odd subsequences,
\[
\frac{I_n-n(n-1)/8}{n}\ \Longrightarrow\ \frac{1-Z^2}{8},\qquad Z\sim N(0,1).
\]

To compare the effect of the interleaver rather than the cut, let \(J_n\) be the inversion count after an ordinary Gilbert--Shannon--Reeds (GSR) riffle: use the **same binomial cut law**, but select a uniformly random order-preserving interleaving conditional on the cut. Then the exact mean is again \(n(n-1)/8\), whereas
\[
\operatorname{Var}(J_n)=\frac{n(n-1)(2n+5)}{96},\qquad
\frac{J_n-n(n-1)/8}{n^{3/2}}\Longrightarrow N(0,1/48).
\]
Thus the midpoint rule suppresses the inversion variance by a factor asymptotic to \(3/(2n)\), and **replaces Gaussian fluctuations on the scale \(n^{3/2}\) by reflected chi-square fluctuations on the scale \(n\)**. At odd \(n\), the finite-size variance ratio is exactly \(3/(2n+5)\). These statements concern **one shuffle from an initially ordered deck**, not the equilibrium inversion statistic or the total-variation mixing time.

## Assumptions and scope

The two packets retain their original internal order. At a nonempty cut \(k\), card \(i\) from the first packet has key \((i-1/2)/k\); card \(j\) from the second has key \((j-1/2)/(n-k)\). All keys are sorted in increasing order; independent fair coins decide equal-key pairs. Empty cuts leave the deck unchanged. This is precisely the zero-adhesion midpoint-interpolation shuffle in Jiang, arXiv:2611.02092v1, and not the GSR release mechanism. The only random inputs are the cut and tie coins. All distributions and limits are unconditional unless conditioning is displayed. No quantitative total-variation bound on convergence to the limiting chi-square law is asserted.

For completeness, the source's tie-count formula can be written as follows. If \(0<k<n\), put \(g=\gcd(k,n-k)\), \(a=k/g\), and \(b=(n-k)/g\). Then \(T_n(k)=g\) when \(a\) and \(b\) are both odd, and \(T_n(k)=0\) otherwise. This formula is prior work, not claimed as new.

## Proof

**1. The conditional law.** Fix a nonempty cut \(k\) and write \(r=n-k\). Every inversion is a cross-packet pair: a second-packet card placed before a first-packet card. There are \(kr\) cross pairs. For each \((i,j)\), reflect the pair to \((k+1-i,r+1-j)\). Their keys are reflected about \(1/2\), so the sign of the key comparison reverses. Consequently, among the \(kr-T_n(k)\) pairs with unequal keys, exactly half have the second-packet card first. Each equal-key pair contributes one inversion with probability \(1/2\), independently across distinct tied pairs. Equal-key pairs are disjoint (each packet's keys are distinct), and their tie coins cannot change the ordering of any other pair. Hence the displayed conditional binomial law holds. At empty cuts the formula is immediate.

When \(n\) is odd, one packet size is even and the other odd; equality of their midpoint keys is impossible by parity in \((2i-1)r=(2j-1)k\). The conditional inversion count is therefore exactly \(kr/2\). Since \(k\mapsto k(n-k)\) has distinct values for \(0\le k\le(n-1)/2\), and the cuts \(k\) and \(n-k\) have equal binomial probabilities, the odd-size mass formula follows.

**2. Exact moments.** Let \(W=K-n/2\). The conditional law yields
\[
\mathbb E[I_n\mid K]=\frac{K(n-K)}2=\frac{n^2}{8}-\frac{W^2}{2},
\quad \operatorname{Var}(I_n\mid K)=\frac{T_n(K)}4.
\]
Represent \(W\) as half the sum of \(n\) independent symmetric signs. Therefore \(\mathbb E W^2=n/4\) and \(\mathbb E W^4=(3n^2-2n)/16\), implying \(\operatorname{Var}(W^2)=n(n-1)/8\). Apply total expectation and variance to get the claimed exact moments. This argument requires no asymptotic approximations.

**3. Non-Gaussian limit for the midpoint rule.** By the ordinary binomial central limit theorem, \(2W/\sqrt n\Longrightarrow Z\sim N(0,1)\). Write \(I_n=K(n-K)/2+E_n\), where \(\mathbb E[E_n\mid K]=0\) and \(\mathbb E E_n^2=\mathbb ET_n(K)/4\le n/4\). Thus \(E_n/n\to0\) in \(L^2\). The exact centering identity becomes
\[
\frac{I_n-n(n-1)/8}{n}=\frac18-\frac12\left(\frac{W}{\sqrt n}\right)^2+\frac{E_n}{n},
\]
and the continuous mapping theorem and Slutsky's lemma give \((1-Z^2)/8\). The bounded conditional tie noise makes the conclusion valid along **both parities**. Its variance \(1/32\) agrees with the normalized exact variance.

**4. Classical-riffle comparison.** A single GSR shuffle from the ordered deck is generated by independent fair binary output labels \(B_1,\ldots,B_n\). Its inversion count is \(J_n=\sum_{i<j}B_i(1-B_j)\). Let \(\xi_i=B_i-1/2\) and \(S=\sum_i\xi_i\). Algebra, with no limiting argument, gives the orthogonal decomposition
\[
J_n-\frac{n(n-1)}8
=\frac12\sum_{i=1}^n(n+1-2i)\xi_i
-\frac12\left(S^2-\frac n4\right).
\]
The two displayed summands have zero covariance because every third centered moment of independent symmetric signs vanishes. Their exact variances are respectively \(n(n^2-1)/48\) and \(n(n-1)/32\). Adding them proves the exact GSR variance. For the limit, the weighted linear sum has variance asymptotic to \(n^3/48\) and satisfies the Lindeberg condition: its largest normalized summand is \(O(n^{-1/2})\). The centered quadratic sum has variance \(O(n^2)\), hence becomes negligible after dividing by \(n^{3/2}\). The central limit theorem and Slutsky give the stated Gaussian limit. Finally, \(\mathbb ET_n(K)\le n\) and the exact variance expressions imply \(\operatorname{Var}(I_n)/\operatorname{Var}(J_n)\sim3/(2n)\); when \(n\) is odd this ratio simplifies exactly as stated.

## Verification

The standalone Python program `checker.py` performs independent exact-rational enumeration of midpoint merges, tie-coin outcomes and inversion counts for each cut and every deck size \(2\le n\le16\), including all odd sizes in that range. It checks the full conditional-binomial law, unconditional mass normalization, exact means, exact variances and odd-size distributions. It also exhaustively enumerates all output binary-label words through \(n=13\) to check the GSR mean and variance. Its captured execution output reports 472 passed assertions. The analytic argument above, not the finite tests, establishes the statements for all sizes and the weak limits. Run with `python3 checker.py` using the Python standard library only.

## Relationship to prior work

Jiang, arXiv:2611.02092v1, defines the midpoint interpolation shuffle, proves the exact tie count (Lemma 4.1), and studies mixing, entropy and cut structure. Its inspected full HTML text does **not** state an inversion-count law or compare the inversion fluctuations with GSR; it explicitly distinguishes the two interleavers. The tie-count formula and model definition are used here, but the reflected-pair inversion identity and the Gaussian-versus-chi-square contrast are new assertions in this package. The prior tie-count theorem itself is not a novelty claim.

Classical GSR shuffle theory supplies the binary-label representation and conventional mixing results (Bayer--Diaconis; Diaconis--Fulman). Classical \(q\)-binomial inversion enumeration covers uniformly interleaved fixed-composition binary words. Our Gaussian GSR calculation is a self-contained benchmark and is **not** asserted as an original limit theorem. Other published work on correlated-label inverse-riffle inversion regimes concerns a different stochastic interleaver, not the deterministic midpoint one. Independently published odd-deck midpoint generator results concern irreducibility, not this one-step inversion statistic. Searches of these alternatives found no dominating statement of the combined midpoint law and fluctuation-scale comparison, but absence from search results does not prove historical priority.

## Limitations

This is one-step statistics from the ordered deck. It does not establish a new total-variation mixing bound, cutoff, or equilibration profile. The limiting \(\chi^2\)-type law is weak convergence, not a quantified local limit. For positive adhesion the block-level interpolation mechanism differs and is not covered. Earlier, unindexed, or inaccessible publications could already imply the invariant. The mathematical proof and searches are not an independent validation of novelty or correctness.

## References

1. Yunjiang Jiang, *Adhesive riffle shuffles: simple one-parameter models, interpolation, and parameter-dependent mixing bounds*, arXiv:2611.02092v1, first submitted 1 November 2026, https://arxiv.org/html/2611.02092v1 .
2. Dave Bayer and Persi Diaconis, *Trailing the dovetail shuffle to its lair*, Annals of Applied Probability 2 (1992), 294–313, https://doi.org/10.1214/aoap/1177005705 .
3. Persi Diaconis and Jason Fulman, *The Mathematics of Shuffling Cards*, American Mathematical Society, 2023, https://www.ams.org/books/mbk/146/ .
4. Mark Sellke, Jialu Shi and Jiamin Wang, *Universality of Cutoff for Riffle Shuffling*, arXiv:2510.22783v1, https://arxiv.org/abs/2510.22783 .
5. Jason Fulman, Gene B. Kim, Sangchul Lee and T. Kyle Petersen, *On the joint distribution of descents and signs of permutations*, arXiv:1910.04258, https://arxiv.org/abs/1910.04258 .
