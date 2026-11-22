# Exact obstruction entropy and a strict entropy gap in the second image of Rule 126

## Finding

Let \(F\) be synchronous elementary binary cellular automaton Rule 126 on the bilateral full shift \(\{0,1\}^{\mathbb Z}\), and put \(Y_t=F^t(\{0,1\}^{\mathbb Z})\). A finite binary word is *minimally forbidden* for \(Y_t\) when it does not occur in \(Y_t\), but every proper contiguous factor does. Let \(m_t(n)\) count such words of length \(n\ge1\).

The first image is the finite-type shift avoiding just `010`; therefore \(m_1(3)=1\) and all other first-image minimal-forbidden counts vanish. The second image has the following **exact all-length rational series**, with \(m_2(0)=0\):

\[
\boxed{\sum_{n\ge0}m_2(n)z^n =
\frac{z^3(1-2z+z^2-2z^5+z^6-2z^8+z^9)}
{(1+z^4)(1-2z+z^2-z^4-z^8)}.}
\]

Its first nonzero values are \(m_2(3)=1\), \(m_2(12)=1\), and
\[
(m_2(13),\ldots,m_2(25))=(2,3,5,7,11,18,29,49,82,136,225,369,606).
\]
All other values through length eleven vanish. Furthermore, there exists a strictly positive constant \(C\) such that
\[
m_2(n)\sim C\lambda^n,
\qquad \lambda=1.647072684571\ldots,
\]
where \(\lambda\) is the largest real root of
\[
\boxed{u^8-2u^7+u^6-u^4-1=0.}
\]
In particular, \(Y_2\) is **sofic but not of finite type**: one additional synchronous update turns a single forbidden block into an infinite minimal forbidden basis with exponential growth.

The corresponding minimal-forbidden-word entropy is strictly smaller than the topological entropy of the second-image shift:
\[
\boxed{h_{\mathcal M}(Y_2)=\log\lambda=0.49899958\ldots
< h_{\mathrm{top}}(Y_2)=\log\rho=0.54933536\ldots,}
\]
where \(\rho=1.732101412746\ldots\) is the largest real root of
\[
u^{13}-4u^{12}+6u^{11}-5u^{10}+3u^9-3u^8+5u^7-3u^6-u^5+4u^4-2u^3+u^2-u+1=0.
\]
The strict gap has exact rational isolation certificates
\(1.647072<\lambda<1.647073<1.732101<\rho<1.732102\).
By the published entropy-gap criterion of Wu and Zhang (2026, Corollary 1 and Theorem A), the shift \(Y_2\) has finitely many ergodic measures of maximal entropy, each Bernoulli up to a finite period; it also has a characteristic measure of maximal entropy. **These qualitative measure consequences are applications of the published theorem, not claimed as new general results.**

## Assumptions and scope

The rule is \(f(a,b,c)=1\) exactly when the three bits are not all equal, with simultaneous updates at every index. The first and second image sets refer to outputs from all bilateral configurations, not to periodic rings, finite boundaries, a particular initial measure, or the ultimate limit set. A word of length \(n\) occurs in \(Y_t\) precisely when it is produced by some finite input block of length \(n+2t\); such a block extends to a bilateral input.

The generating variable \(z\) counts the number of output symbols in a minimally forbidden word. Counts are of distinct words, not occurrences or preimages. The entropy quantities are spatial shift entropies, not entropies of temporal iteration. All logarithms are natural. The source motivating comparison of forbidden-word entropy with topological entropy is Wu and Zhang (2026), whose first public preprint appeared on 2026-11-02 and has primary MSC2020 37B10.

## Proof

**1. The first-image benchmark.** Write \(d_i=x_i\oplus x_{i+1}\). Then \((Fx)_i=d_{i-1}\lor d_i\). Every bilateral binary sequence \(d\) integrates to a sequence \(x\) by fixing one input bit and taking successive XOR differences in both directions. Hence an output with an isolated one (`010`) is impossible. Conversely, for any bilateral word \(y\) avoiding `010`, set \(d_i=y_i\land y_{i+1}\). The absence of isolated ones gives \(d_{i-1}\lor d_i=y_i\) at every site, establishing \(Y_1=X_{\{010\}}\), including the all-zero and all-one cases.

**2. An exact second-image deterministic automaton.** For a block \(a b c d e\), the two-step output is
\[
g(a,b,c,d,e)=f(f(a,b,c),f(b,c,d),f(c,d,e)).
\]
Build the labeled de Bruijn graph on the sixteen length-four input blocks; append one input bit and label the edge by \(g\). A word occurs in \(Y_2\) if and only if it labels a path in this graph. Starting the subset construction at all sixteen vertices produces seventeen reachable nonempty subsets. Minimizing their right languages gives thirteen accepting states and a dead state; the initial accepting state is number 12 in the reproducible numbering of `certificate.json`. This automaton recognizes *all* second-image factors, not only finite samples.

**3. Exact test for minimal forbidden words.** Because the image language is factorial, a word of length at least two is minimally forbidden if and only if its length-one-shorter prefix and suffix are admitted, but the whole word is rejected. On reading the first letter \(a\), initialize a pair of automaton states \((\delta(q_0,a),q_0)\). During middle letters \(c\), advance both coordinates by \(\delta(\cdot,c)\), discarding paths whose first coordinate becomes dead. A final letter \(b\) completes a minimal forbidden word exactly when it sends the first coordinate to the dead state and keeps the second coordinate alive. This bijection between accepted paths and distinct minimal forbidden words does not double-count because the output alphabet labels deterministic transitions.

The reachable pair graph has 29 states. Removing states from which no terminal transition is reachable leaves the sixteen productive states printed in `forbidden_certificate.json`. There is one productive first-letter start, state zero. Let \(A\) be the sixteen-by-sixteen nonnegative integer matrix whose entries count ordinary internal letter transitions between these productive states, and let \(e\) be the vector of counts of terminal letters from each state. Then, with \(u\) the indicator row of state zero,
\[
m_2(n)=u A^{n-2}e \quad(n\ge2),\qquad
M(z)=z^2u(I-zA)^{-1}e.
\]

**4. Exact rational evaluation.** Forming the explicit matrix from the printed transitions and applying integer Newton identities gives
\[
\det(I-zA)=(1+z^4)(1-2z+z^2-z^4-z^8)=D(z).
\]
The Cayley–Hamilton identity makes \(D(z)M(z)\) a polynomial of degree at most 17: an entry of the adjugate of the sixteen-by-sixteen \(I-zA\) has degree at most 15, and the prefactor contributes degree two. Exact transfer counts for lengths zero through seventeen, multiplied by \(D(z)\), give precisely
\[
D(z)M(z)=z^3(1-2z+z^2-2z^5+z^6-2z^8+z^9).
\]
Checking all eighteen coefficients is therefore an **all-length exact algebraic certificate**, not extrapolation from eighteen data points. The certificate and its complete generating algorithm are in `verify_forbidden.py`; `verify.py` independently builds the original image automata and checks their language counts. In particular, the first difference is at length twelve, consistent with prior work, but the formula here covers every length.

**5. Exponential asymptotics.** In the sixteen-state productive transfer graph, states 2 through 15 form one strongly connected component; each of its fourteen states reaches all the others, and state 4 has a self-loop. Thus this component is primitive. The other two states are transient, and paths from the initial state enter the primitive component and reach terminal transitions. The transfer matrix characteristic polynomial is
\[
u^4(u^4+1)(u^8-2u^7+u^6-u^4-1).
\]
Its unique positive Perron root \(\lambda\) is therefore a simple dominant eigenvalue on the productive component, with positive contribution to the counts. Exact Sturm sign-variation counts on the cubic-free degree-eight factor are \((4,3,3)\) at the rational points \(1.647072\), \(1.647073\), and \(2\); the matrix has row sums at most two. Consequently
\[
1.647072<\lambda<1.647073,
\]
and Perron–Frobenius theory yields the stated positive-constant asymptotic. Infinitely many minimal forbidden words rule out any finite-type presentation of \(Y_2\); a finite image of the full shift is sofic, so \(Y_2\) is strictly sofic.

**6. Exact image entropy and a strict obstruction gap.** The thirteen-state right-language-minimized deterministic automaton in Step 2 has a nonnegative integer transition matrix \(B\). As every state is reachable from the initial state and accepting, the image language grows with exponential rate \(\rho(B)\). The exact integer characteristic polynomial obtained in `verify.py` is
\[
P_{13}(u)=u^{13}-4u^{12}+6u^{11}-5u^{10}+3u^9-3u^8+5u^7-3u^6-u^5+4u^4-2u^3+u^2-u+1.
\]
Rational Sturm counting and the nonnegative matrix Perron property isolate \(\rho(B)\) to the rational interval \( (1.732101,1.732102) \). The minimal-forbidden rate is from Step 5, namely \( (1.647072,1.647073) \); these intervals are disjoint and ordered. The definitions of entropy in Wu and Zhang (2026, equations (2) and (4)) therefore yield \(h_{\mathcal M}(Y_2)=\log\lambda<h_{\mathrm{top}}(Y_2)=\log\rho\), with exact rather than numerical-only proof of the inequality. Their Corollary 1 and Theorem A supply the stated qualitative measure implications, using \(h_{\mathcal G}\le h_{\mathcal M}\). This is a direct **application** of those results rather than a new general ergodic theorem.

## Verification

Run `python3 verify.py`, `python3 verify_forbidden.py`, and `python3 crosscheck.py` in the same directory as the two JSON certificate files. Only the Python standard library is used. The first program regenerates both deterministic image automata, their exact characteristic polynomials, integral word counts, and rational Sturm root brackets. The second constructs and trims the 29-state minimal-obstruction machine, verifies all sixteen productive transitions and the primitive component, derives the determinant by exact Newton identities, and verifies the rational series using the degree bound. The third independently enumerates every underlying input block at lengths through fourteen and checks all observed image counts and minimal forbidden-word counts. All three programs succeeded during preparation.

The finite enumerations are checks, not proofs of the infinite assertions. The finite-state closure, determinant identity, adjugate degree bound, and Perron–Frobenius argument supply the unrestricted proof.

## Relationship to prior work

The published one-step image and first-offender classifications establish the finite-type first-image benchmark and general finite-state methods, but **do not cover second-image minimal forbidden-word counts**. The previously established sharp twelve-letter first discrepancy for Rule 126 is acknowledged; the shortest witness is not new here. The 2015 finite-time process-graph study actually draws a Rule 126 graph at time two. That graph encodes the second-image language, and hence makes the present invariant computable in principle, but the inspected argument does not construct its minimal-obstruction graph, evaluate the stated all-length series, or establish the new exponential growth. The contribution here is this specific natural exact invariant, the proven change from finite to exponentially growing minimal forbidden basis, and the strict evaluated entropy gap, not the underlying de Bruijn algorithm. Wu and Zhang (2026), the recent primary motivating source, define the entropy of minimal forbidden words and prove a theorem connecting such entropy gaps to maximal-entropy measures; their general criterion does not evaluate Rule 126 at any time. Its consequence here is therefore credited as an application of that existing theorem.

## Limitations

The theorem concerns the second spatial image of one particular synchronous rule and distinct minimally forbidden blocks. It does not classify third and later images, the eventual image, other rules, transition-time correlations, entropy of the temporal map, preimage multiplicities, the number of maximal-entropy measures, or their explicit descriptions. The exact formula relies on a finite 16-state transfer computation fully reproducible from the source code. While close indexed and full-text sources were compared, unpublished or unindexed equivalent calculations could affect historical priority. No independent mathematical audit has been performed.

## References

1. X. Wu and X. Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts*, arXiv:2611.03758v1, first public 2026-11-02, https://arxiv.org/html/2611.03758v1. This is the motivating recent primary source and supplies the entropy-gap criterion.
2. *A first-offender growth gap for all elementary cellular-automaton images* (2026-10-25), https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-a-first-offender-growth-gap-for-all-elementary-cellular-automato--23171f1f1979/RESULT.md.
3. *A sharp twelve-symbol threshold for second-update image loss in elementary cellular automata* (2026-10-26), https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-sharp-twelve-symbol-threshold-for-second-update-image-loss-in--5742d176c6e4/RESULT.md.
4. *Periodic predecessor lifting and exact cyclic image counts for elementary cellular automaton Rule 126* (2026-11-02), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-periodic-predecessor-lifting-and-exact-cyclic-image-counts-for-e--43a663d15708/RESULT.md.
5. P. P. B. de Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki and V. V. Trafaniuc, *Advances in the Study of Elementary Cellular Automata Regular Language Complexity*, *Complexity* **21** (2016), 267–279; first online 2015-05-06, https://doi.org/10.1002/cplx.21686.
6. *Exact nineteen-value spatial image entropy spectrum of elementary cellular automata* (2026-10-27), https://github.com/published-finding corpus/2026/blob/main/2026/10/27/SCOPE-exact-nineteen-value-spatial-image-entropy-spectrum-of-elementar--d4f1725c3486/RESULT.md.
