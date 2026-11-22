# A two-parameter collapse of \(3\)-adic Cantor multiplier intersections

## Finding

Let \(\mathbb Z_3\) be the \(3\)-adic integers and let
\[
\Sigma=\left\{\sum_{i\ge0}\epsilon_i3^i:\epsilon_i\in\{0,1\}\right\}.
\]
For each integer \(m\ge1\), put \(L_m=\sum_{j=0}^{m-1}3^j=(3^m-1)/2\). For every pair of integers \(r,k\) satisfying \(2\le r\le k-2\), define the sparse-block multiplier
\[
M_{r,k}=3^{k-1}+L_{k-r}.
\]
Then the following **exact equality of sets**, not merely of their Hausdorff dimensions, holds:
\[
\boxed{\Sigma\cap L_r^{-1}\Sigma\cap M_{r,k}^{-1}\Sigma
=\Sigma\cap L_k^{-1}\Sigma.}
\]
Here \(m^{-1}\Sigma=\{x\in\mathbb Z_3:mx\in\Sigma\}\); no division by \(3\) or choice of inverse is involved.

Equivalently, simultaneous omission of the ternary digit \(2\) from \(x\), \(L_rx\), and \(M_{r,k}x\) occurs exactly when every two successive nonzero ternary digits of \(x\) are at least \(k\) positions apart. For example, \(r=2,k=4\) gives the identity \(\Sigma\cap4^{-1}\Sigma\cap31^{-1}\Sigma=\Sigma\cap40^{-1}\Sigma\); \(r=3,k=6\) gives \(\Sigma\cap13^{-1}\Sigma\cap256^{-1}\Sigma=\Sigma\cap364^{-1}\Sigma\).

For each such pair, the number \(a_n\) of length-\(n\) ternary prefixes extendible to an element of the intersection is independent of \(r\): \(a_n=n+1\) for \(0\le n<k\), and \(a_n=a_{n-1}+a_{n-k}\) for \(n\ge k\). Thus the Hausdorff dimension is \(\log_3\beta_k\), where \(\beta_k>1\) is the unique positive real root greater than one of \(t^k-t^{k-1}-1\). This dimension formula for the repunit set is already known; the new claim is the two-parameter **equality of arithmetic intersections**.

## Assumptions and scope

All quantities are interpreted in \(\mathbb Z_3\), with ternary digits read from low to high powers of \(3\). The claim covers every integer pair \(2\le r\le k-2\), all infinite digit strings, and all extendible finite prefixes. It does not assert an analogous formula for nonbinary digits, different primes, or arbitrary sparse multipliers. The boundary family \(r=k-1\), in which \(M_{r,k}=3^{k-1}+1\), is deliberately not claimed as new, because the earlier family of multipliers \(3^j+1\) already gives closely related intersections.

## Proof

A word in \(\Sigma\) is identified with its support \(I=\{i\ge0:\epsilon_i=1\}\). A finite-digit multiplier with support \(B\subset\mathbb Z_{\ge0}\) produces, **before carrying**, at position \(j\) the number of pairs \((i,b)\in I\times B\) with \(i+b=j\). When every such count is at most one, the product has only digits \(0,1\), so no carries occur. If the first position at which the count exceeds one has count exactly two, its ternary digit is \(2\), because all preceding positions have generated no carry.

**Repunit spacing lemma.** For every \(s\ge2\), an element \(x\in\Sigma\) satisfies \(L_sx\in\Sigma\) if and only if successive positions in \(I\) differ by at least \(s\). In one direction, the translated blocks \(i+\{0,\ldots,s-1\}\) are disjoint and cause no carries. Conversely, take the first successive pair \(i<i+h\) with \(1\le h<s\); all earlier successive gaps are at least \(s\). Earlier blocks are disjoint and finish before position \(i\). At position \(i+h\), the blocks from \(i\) and \(i+h\) each contribute one, and no later block can yet contribute. There has been no earlier collision or carry. Thus this digit equals \(2\), a contradiction. This also applies when \(I\) is infinite, since any first short gap has finite index.

Now assume \(x,L_rx,M_{r,k}x\in\Sigma\). The lemma gives successive gaps of at least \(r\). Suppose some successive gap is nevertheless less than \(k\), and take the first such pair \(i,i+h\), with \(r\le h\le k-1\). All earlier gaps are at least \(k\). The multiplier \(M_{r,k}\) has precisely the support
\[
B=\{0,1,\ldots,k-r-1\}\cup\{k-1\}\subseteq\{0,\ldots,k-1\}.
\]
If \(h\le k-r-1\), the two translated blocks \(i+B\) and \(i+h+B\) overlap already at position \(i+h\), using \(h\in B\) and \(0\in B\). Otherwise \(h\ge k-r\), and putting \(j=k-1-h\) gives \(0\le j\le k-r-1\) (as \(h\ge r\)) and \(j\le r-1\) (as \(h\ge k-r\)); then those blocks overlap at position \(i+k-1=i+h+j\). Hence in either case their **first** overlap is at most \(r-1\) digit positions after the second nonzero digit.

Earlier nonzero digits, being at gaps of at least \(k\), have blocks ending before \(i\) and cannot interfere. The next nonzero digit after \(i+h\) begins at least \(r\) positions later, and cannot interfere before the first overlap. Therefore at that first overlap the uncarried coefficient is exactly two, while at all preceding positions it was at most one. The resulting ternary digit equals \(2\), a contradiction. Every gap is therefore at least \(k\).

Conversely, if all nonzero-digit gaps are at least \(k\), the blocks from distinct nonzero digits are disjoint for both multipliers: \(L_r\) and \(M_{r,k}\) have supports contained in \(\{0,\ldots,k-1\}\). Their products contain only digits \(0,1\). This proves the exact set identity.

For the prefix count, a length-\(n\) allowed word either starts with \(0\), leaving \(a_{n-1}\) possibilities, or starts with \(1\), forcing the next \(k-1\) digits to be zero and leaving \(a_{n-k}\) possibilities when \(n\ge k\). For \(n<k\), at most one digit is nonzero, giving \(n+1\) possibilities. Every allowed finite word extends by zeros, so these are precisely the extendible prefixes. The standard \(k\)-state finite-type graph has characteristic equation \(t^k-t^{k-1}-1=0\), hence exponential growth rate \(\beta_k\) and \(3\)-adic Hausdorff dimension \(\log_3\beta_k\).

## Verification

The standalone script `checker.py` exhaustively enumerates length-\(n\) binary ternary inputs for 48 parameter/depth combinations, compares membership in both multiplier constraints through every possibly nonzero output digit, and checks the spacing recurrence. It passed 75,600 complete input-word comparisons. In each test \(x\) has zero continuation and both products have no possible nonzero digit at or above position \(n+k\); therefore these finite checks are exact for those tested finite inputs. This does **not** establish the all-parameter theorem: that rests on the first-collision proof above.

To reproduce: `python checker.py` with Python 3, without external packages. To check a particular infinite word, evaluate the gap condition, which is necessary and sufficient by the proof; finite prefixes are extendible exactly when they satisfy that condition.

## Relationship to prior work

Abram and Lagarias (arXiv:1308.3133, first public August 14, 2013) established automaton constructions for arbitrary finite intersections of multiplicative translates, classified the single repunit multiplier family \(L_k\), and studied intersections among repunits and among the different multipliers \(3^j+1\). In particular their Theorems 4.2, 4.7 and 4.8 supply the repunit dimension and a previously covered boundary phenomenon. They do not state the present **interior** two-parameter sparse-multiplier identity for \(2\le r\le k-2\). The present claim identifies a simultaneous arithmetic constraint with exactly the repunit language, and proves it uniformly without carrying out the general finite-automaton construction parameter by parameter.

Abram, Bolshakov and Lagarias (arXiv:1508.05967, first public August 24, 2015) analyze two other infinite multiplier families, \(2\cdot3^j+1\) and \(3^{2j}-3^j+1\), and compare their spectral dimensions to those of repunit intersections. Their inspected statements and appendices do not provide this language equality for \(3^{k-1}+L_{k-r}\). The general automaton algorithms can in principle verify any fixed example; the additional content here is a *closed-form two-parameter equality*.

## Limitations

A proof of a set equality is not a proof that it has never appeared under another formulation. The published automaton constructions could conceal an implicit equivalent; no independent historical-priority audit has occurred. The resulting dimension equation and prefix recurrence are inherited from the known repunit language and are **not separately claimed as novel**. The theorem does not resolve the Erdős powers-of-two problem or any exceptional-set conjecture. Tests at finitely many pairs and depths are checks, not replacements for the all-parameter argument.

## References

1. W. Abram and J. C. Lagarias, *Intersections of multiplicative translates of 3-adic Cantor sets*, arXiv:1308.3133v1 (August 14, 2013), https://arxiv.org/abs/1308.3133 . See Theorems 4.2, 4.7 and 4.8 and Sections 3–4.
2. W. C. Abram, A. Bolshakov and J. C. Lagarias, *Intersections of multiplicative translates of 3-adic Cantor sets II: two infinite families*, arXiv:1508.05967v1 (August 24, 2015), https://arxiv.org/abs/1508.05967 . See Sections 1–2 and Appendices A–B.
