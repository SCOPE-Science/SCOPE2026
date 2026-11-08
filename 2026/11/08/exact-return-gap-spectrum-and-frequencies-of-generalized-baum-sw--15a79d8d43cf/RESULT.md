# Exact return-gap spectrum and frequencies of generalized Baum–Sweet words

## Finding
For an arbitrary integer \(r\ge2\), consider the generalized Baum–Sweet indicator \(b_r\), and enumerate its one-positions as \(0=s_0<s_1<s_2<\cdots\). The successive differences \(d_j=s_{j+1}-s_j\) admit a complete all-base-order classification: exact values, a successor rule, exact finite-shell multiplicities and limiting relative frequencies. Set
\[
H_r(t)=(2^{r-1}-1)2^t+2^{(r-1+t)\bmod r},\qquad t\ge0.
\]
Then the distinct possible differences are precisely
\[
\{2^a:0\le a<r\}\ \cup\ \{H_r(t):t\ge0\}.
\]
The only repetition within this displayed parameterization is \(H_r(0)=H_r(1)=2^r-1\). In particular, the nonpower differences begin with \(2^r-1\) and thereafter strictly increase with \(t\ge1\).

For each binary length \(n\ge1\), let \(T_r(m)\) count tilings of a length-\(m\) segment by pieces of lengths \(1\) and \(r\):
\[
T_r(m)=0\ (m<0),\quad T_r(0)=1,\quad
T_r(m)=T_r(m-1)+T_r(m-r)\ (m\ge1).
\]
Among the accepted one-positions with exactly \(n\) binary digits, exactly one has the boundary gap \(2^{n\bmod r}\), and exactly \(T_r(n-r-t-1)\) have last zero-block ending in \(0^r1^t\), for each \(t\ge0\), and therefore gap \(H_r(t)\). Count the contributions for \(t=0,1\) together when counting the same numerical gap.

Write \(\lambda_r>1\) for the real root of \(\lambda_r^r=\lambda_r^{r-1}+1\). If \(D_r(X)=\#\{j:s_j<X\}\), then for every possible gap \(d\),
\[
\lim_{X\to\infty}\frac{\#\{j:s_j<X,\ s_{j+1}-s_j=d\}}{D_r(X)}
=\begin{cases}
0,&d=2^a,\quad 0\le a<r,\\
\lambda_r^{-r}+\lambda_r^{-(r+1)},&d=2^r-1,\\
\lambda_r^{-(r+t)},&d=H_r(t),\quad t\ge2.
\end{cases}
\]
The frequencies for all other positive integers are zero. The displayed positive frequencies total one.

## Assumptions and scope
The ordinary binary expansion of a positive integer has no leading zeroes. A maximal run of zeroes may be at the end of that expansion; its length must also be divisible by \(r\). The integer zero is explicitly accepted. This is the generalized Baum–Sweet family defined in Merta (2018). The differences are gaps between *successive one-positions*, not gaps between one-symbol runs and not densities among all integers. Although the original binary word has zero asymptotic density of ones, the gap distribution is normalized by the number of one-positions, and every fixed numerical gap has a relative frequency.

The count in a length-\(n\) binary shell means eligible starting numbers \(s_j\) with \(2^{n-1}\le s_j<2^n\); their successors may lie outside that shell. The sequence \(T_r\) and the gap class of the unique word \(1^n\) are specified for every \(n\ge1\).

## Proof
**1. Language and lexicographic successor.** An accepted positive binary expansion is uniquely a word in the language \(1(1\mid0^r)^*\). It starts in \(1\), and all subsequent bits decompose uniquely into single ones or complete blocks of \(r\) zeroes. At any fixed length, binary numerical order is exactly lexicographic order. If an accepted word contains a zero, it has a unique representation \(U0^r1^t\) in which \(t\ge0\) is the number of trailing ones and \(U\) is a nonempty accepted word (possibly ending in complete zero blocks).

To form the next accepted binary word of the same length, the rightmost *permissible* zero-to-one carry lies at the first zero of the final block \(0^r\). Flipping a later zero would leave an incomplete zero run before the new one; flipping an earlier bit makes a larger jump. After this flip, the remaining \(r-1+t\) bits must form the lexicographically smallest accepted suffix of that length, namely \(0^{r\lfloor(r-1+t)/r\rfloor}1^{(r-1+t)\bmod r}\). Hence the immediate successor is
\[
U\,1\,0^{r\lfloor(r-1+t)/r\rfloor}1^{(r-1+t)\bmod r}.
\]
When subtracting the integer represented by \(U0^r1^t\), the contribution of the common \(U\) cancels. The old suffix has value \(2^t-1\), while the new suffix has value \(2^{r+t-1}+2^{(r-1+t)\bmod r}-1\). Their difference is exactly
\[
H_r(t)=2^{r+t-1}-2^t+2^{(r-1+t)\bmod r}.
\]
(The new suffix in this subtraction starts with the flipped \(1\), and has length \(r+t\).)

If the word has no zero, it is \(1^n\). Its immediate successor among all accepted integers is the smallest accepted \((n+1)\)-digit word
\[
1\,0^{r\lfloor n/r\rfloor}1^{n\bmod r},
\]
which is larger by exactly \(2^{n\bmod r}\). The gap from the accepted index zero to one is also \(1\). Consequently there are no other gap types. Each type occurs infinitely often: \(1^n\) gives each residue \(n\bmod r\) infinitely often, and for fixed \(t\) the prefixes \(U=1^m\) give infinitely many \(U0^r1^t\).

**2. Distinct gap values.** The boundary gaps are powers from \(1\) through \(2^{r-1}\); every \(H_r(t)\) is at least \(2^r-1\), so the families are disjoint. Direct substitution gives \(H_r(0)=H_r(1)=2^r-1\). For \(t\ge1\), write \(a=(r-1+t)\bmod r\). If \(a<r-1\), then \(H_r(t+1)-H_r(t)=(2^{r-1}-1)2^t+2^a>0\); if \(a=r-1\), the difference is \((2^{r-1}-1)2^t-(2^{r-1}-1)>0\). This proves the asserted only collision.

**3. Exact shell multiplicities.** An accepted length-\(n\) expansion begins in one, followed by a uniquely tiled length-\((n-1)\) suffix, with tiles \(1\) and \(0^r\); thus the shell contains \(T_r(n-1)\) one-positions. Exactly one word has no zero, namely \(1^n\). A word ending in \(0^r1^t\) has a uniquely determined accepted nonempty prefix \(U\), whose free tail after its first one has length \(n-r-t-1\), and conversely every tiling of that tail yields one such word. Therefore the count is \(T_r(n-r-t-1)\). The first/last-suffix partition gives, for each \(n\ge1\), the identity
\[
T_r(n-1)=1+\sum_{t\ge0}T_r(n-r-t-1).
\]

**4. Full-shell asymptotics.** The recurrence for \(T_r\) has characteristic polynomial \(z^r-z^{r-1}-1\). Its companion nonnegative matrix is primitive because the tiled renewal graph has cycles of coprime lengths \(1\) and \(r\). Thus Perron--Frobenius theory gives a unique dominant simple positive root \(\lambda_r>1\), and numbers \(C_r>0\), \(1<\eta_r<\lambda_r\) for which
\[
T_r(m)=C_r\lambda_r^m+O_r(\eta_r^m).
\]
For each fixed \(t\), dividing exact shell counts shows that the proportion among one-positions in the length-\(n\) shell with trailing parameter \(t\) tends to \(\lambda_r^{-(r+t)}\); the exceptional all-ones word has vanishing proportion.

**5. Arbitrary thresholds, not just dyadic endpoints.** The same proportions hold for a cut at an arbitrary integer \(X\), and we justify this extension. A binary initial interval of length-\(n\) strings can be partitioned into at most \(n\) disjoint subtrees specified by initial digit prefixes, plus at most one boundary word. For a prefix which can be continued to an accepted full word, the number of completed words with \(m\) free bits is a shifted tiling count \(T_r(m-c)\) for some state-dependent \(0\le c<r\), or a fixed finite sum of such counts. Conditioning on a fixed final suffix \(0^r1^t\) changes the number of free bits by exactly \(r+t\), except in the finitely many short-completion cases; hence, uniformly over the finitely many prefix states, the count in each subtree differs from \(\lambda_r^{-(r+t)}\) times the subtree total by \(O_{r,t}(\eta_r^{m})\). Summing at most \(n\) subtrees gives \(O_{r,t}(n\eta_r^n+n)\), still \(o(\lambda_r^n)\). The completed shells of lengths below \(n\) obey the same limit, and the denominator for any \(X\) with \(2^{n-1}\le X<2^n\) is at least \(T_r(n-2)=\Omega_r(\lambda_r^n)\). Therefore the required relative frequency exists for every increasing real threshold \(X\to\infty\), not merely for powers of two.

Finally, only the all-ones words and the starting index zero supply power gaps, hence their limiting proportions vanish. Parameters \(t=0,1\) yield one shared gap and their probabilities add. For \(t\ge2\) the gap values are distinct. The total mass is
\[
\sum_{t\ge0}\lambda_r^{-(r+t)}
=\frac{\lambda_r^{-r}}{1-\lambda_r^{-1}}=1,
\]
where the last equality follows from \(\lambda_r^{r-1}(\lambda_r-1)=1\). This completes the proof.

## Verification
A standalone Python 3 verifier is embedded as `verify.py`. It independently enumerates accepted integer positions, compares each consecutive gap with the stated successor rule, and checks the exact binomial-length shell counts against the tiling recurrence, for bases \(r=2,\ldots,8\) at specified finite cutoffs. Verification is diagnostic, and the infinite theorem rests on the proof above; finite enumeration is not presented as an infinite certificate.

## Relationship to prior work
Merta (2018, Sections 2 and 5) defines the same generalized family, proves unbounded zero runs and an upper bound of two on consecutive ones, and analyzes parity/regularity of its one-position enumeration. His Section 5 Theorem 5.10 gives a difference set for the *formal composition-inverse sequence* \(u_n^{(r)}\), which is a different object from the increasing one-positions \(s_j\) studied here. It does not imply the present exact successor rule, gap set, dyadic counts or limiting distribution. Allouche and Yao (2024) compute an opacity-complexity invariant for the ordinary Baum–Sweet sequence, not return gaps. OEIS A060142 supplies the base-two accepted indices and a self-generating description, but no corresponding exact generalized gap-frequency law in its inspected entry.

## Limitations
These are relative frequencies among consecutive accepted indices, not spatial densities of fixed-length zero runs at a uniformly random integer position. The established value of \(\lambda_r\) is an algebraic Perron root; this is not claimed to produce an elementary closed expression for arbitrary \(r\). An equivalent result in unindexed literature cannot be categorically excluded. Independent external checking has not been performed.

## References
- Łukasz Merta, *Composition inverses of the variations of the Baum–Sweet sequence*, arXiv:1803.00292v1, 2018-03-01, https://arxiv.org/html/1803.00292v1 (especially Sections 2 and 5).
- J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences. The general case*, arXiv:2404.13601v1, 2024-04-21, https://arxiv.org/abs/2404.13601 (especially Example 9).
- OEIS Foundation, entry A060142, https://oeis.org/A060142 (accepted indices and the base-two generating rules).
