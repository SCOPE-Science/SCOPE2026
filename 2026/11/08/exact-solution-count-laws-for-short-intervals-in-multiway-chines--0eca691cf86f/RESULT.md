# Exact solution-count laws for short intervals in multiway Chinese remaindering

## Finding
Fix an integer \(k\ge3\), a positive integer \(g\), and moduli \(m_1,\ldots,m_k\) such that \(\gcd(m_i,m_j)=g\) whenever \(i\ne j\). For each \(i\), fix \(0\le a_i\le g\) and choose a cyclic interval \(I_i(t_i)=\{t_i,t_i+1,\ldots,t_i+a_i-1\}\pmod{m_i}\), with \(t_i\) independent modulo \(m_i\). Let \(L=\operatorname{lcm}(m_1,\ldots,m_k)\) and let \(H(t_1,\ldots,t_k)\) count the \(x\pmod L\) satisfying \(x\pmod{m_i}\in I_i(t_i)\) for all \(i\).

**Complete spectrum.** As the starts vary, the set of all possible solution counts is exactly
\[
\left\{h\in\mathbb Z:\max\left(0,\sum_{i=1}^k a_i-(k-1)g\right)\le h\le\min_i a_i\right\}.
\]
Both extremes and every intermediate integer occur. In particular, every placement has a common solution if and only if \(\sum_i a_i>(k-1)g\).

**Exact probability law.** Uniform independent interval starts modulo their respective moduli induce a probability law depending only on \(g\) and the lengths \(a_i\). Write \(D_h\) for the number of starts in \((\mathbb Z/g\mathbb Z)^k\) producing exactly \(h\) solutions. Put \(B_0=g^k\). For each \(1\le r\le g\), define
\[
B_r=\frac gr\sum_{\substack{d_1,\ldots,d_r\ge1\\d_1+\cdots+d_r=g}}
\prod_{i=1}^k\left(\sum_{j=1}^{r}\max\{0,d_j+a_i-g\}\right).
\]
Then \(B_r\) is a nonnegative integer and the complete distribution is
\[
\boxed{D_h=\sum_{r=h}^{g}(-1)^{r-h}\binom rh B_r,\qquad
\Pr(H=h)=D_h/g^k\quad(0\le h\le g).}
\]
For the original start sets modulo \(m_i\), the exact number of starts with \(H=h\) is \(D_h\prod_i(m_i/g)\). In particular,
\[
\mathbb E H=\frac{\prod_i a_i}{g^{k-1}}.
\]
The second moment admits the shorter formula
\[
\mathbb E H^2=g^{1-k}\sum_{d=0}^{g-1}\prod_{i=1}^k
\left(\max\{0,a_i-d\}+\max\{0,a_i-(g-d)\}\right).
\]
The variance is this second moment minus \((\mathbb EH)^2\).

## Assumptions and scope
A cyclic interval of length zero is empty, and one of length equal to the modulus is the entire residue ring. The restriction \(a_i\le g\) ensures that each interval has at most one element in each class modulo \(g\). The moduli may differ, including noncoprime ones; no assumption that the quotients \(m_i/g\) are coprime to \(g\) is necessary. The pairwise common-gcd requirement does force the quotients \(m_i/g\) to be pairwise coprime. Counts refer to distinct residue solutions modulo \(L\), not to unbounded integer solutions.

## Proof
**1. Reduction to a single cyclic ring.** Let \(J_i(t_i)\) be the projection of \(I_i(t_i)\) modulo \(g\). Each \(J_i\) is a cyclic arc of \(a_i\) distinct residues modulo \(g\). A selected tuple of residues, one from each \(I_i\), is compatible under the generalized Chinese remainder theorem exactly when all coordinates agree modulo every \(\gcd(m_i,m_j)=g\). Since the projection from \(I_i\) onto \(J_i\) is injective, compatible tuples are in bijection with residues \(u\in\bigcap_i J_i\). Every compatible tuple corresponds to exactly one class modulo \(L\). Thus
\[
H(t_1,\ldots,t_k)=\left|\bigcap_{i=1}^kJ_i(t_i)\right|.
\]
Each projected start is uniform on \(\mathbb Z/g\mathbb Z\), independently, because every residue has exactly \(m_i/g\) lifts modulo \(m_i\).

**2. Sharp spectrum.** The trivial upper bound is \(H\le\min_i a_i\); nesting all arcs at the same start attains it. Since the complements have sizes \(g-a_i\), the union bound gives
\[
H=g-\left|\bigcup_i J_i^c\right|\ge\max\left(0,\sum_i a_i-(k-1)g\right).
\]
To attain equality, place the complementary arcs consecutively: with \(s_1=0\) and \(s_i=\sum_{j<i}(g-a_j)\), take \(J_i^c=\{s_i,\ldots,s_i+g-a_i-1\}\pmod g\). Their union is precisely the reduction modulo \(g\) of the integer interval \([0,\sum_i(g-a_i)-1]\), and hence has cardinality \(\min(g,\sum_i(g-a_i))\). The complementary arcs are again cyclic intervals, so this configuration is admissible.

Any configuration of arc starts can be transformed into any other by shifting one arc one unit at a time. Such a step replaces at most one entering and one leaving point of that arc. Consequently the common intersection cardinality changes by at most one. A stepwise path connecting a minimizer to a maximizer therefore assumes every integer between the two endpoint counts. This proves the complete spectrum and the strict universal-solvability threshold.

**3. Cyclic-gap count of the binomial moments.** Let \(S\subset\mathbb Z/g\mathbb Z\) be a fixed nonempty set of size \(r\), and arrange its members cyclically. Their successive positive gaps \(d_1,\ldots,d_r\) sum to \(g\). The number of length-\(a\) arcs containing every point of \(S\) equals the number of complementary length-\((g-a)\) arcs disjoint from \(S\). An exclusion arc disjoint from \(S\) lies in one of the gaps, with \(\max(0,d_j-(g-a))\) available starting positions in gap \(j\). Therefore this number is exactly
\[
N_a(S)=\sum_{j=1}^r\max\{0,d_j+a-g\}.
\]
This identity includes \(a=0\), \(a=g\), and \(g=1\).

For all \(g^k\) projected start tuples, the sum of \(\binom{H}{r}\) counts every \(r\)-subset \(S\) of the common intersection once per start. By independence, it equals \(\sum_{|S|=r}\prod_iN_{a_i}(S)\). An ordered positive composition \((d_1,\ldots,d_r)\) of \(g\), together with a marked start residue, describes a cyclic \(r\)-subset with one member distinguished. Each subset admits exactly \(r\) distinguished members; each ordered composition allows exactly \(g\) starting residues. The resulting factor \(g/r\) gives the formula for \(B_r\). For \(r=0\) every start contains the empty subset, giving \(B_0=g^k\). Hence
\[
B_r=\sum_{h=r}^g\binom hr D_h.
\]
Ordinary binomial inversion yields the stated \(D_h\). This identity also proves its integrality and nonnegativity without relying on numerical computation.

**4. Moments.** For each fixed residue \(u\pmod g\), the probability that a random arc of length \(a_i\) contains \(u\) is \(a_i/g\). Summing over all \(g\) choices of \(u\) proves the expectation. For an ordered pair of residues with cyclic displacement \(d\), the number of starts of a length-\(a\) arc covering both is
\[
C_a(d)=\max(0,a-d)+\max(0,a-(g-d)).
\]
For \(d=0\) this equals \(a\) (including \(g=1\)); for distinct residues it follows from the two complementary cyclic gaps. Summing over the \(g\) ordered pairs of each displacement and multiplying independent arc probabilities proves the second-moment formula.

## Verification
Running `python3 verify.py` uses exact integer/rational arithmetic. It exhaustively compares the predicted spectrum, full binomial-moment distribution, first and second moments to direct enumeration of cyclic arc starts across \(4274\) parameter configurations (\(301736\) start tuples), and separately compares actual CRT solution counts for \(92176\) configurations over three different moduli. These tests cover finite ranges only; all statements for arbitrary \(k\), \(g\), and moduli follow from the proof above.

For example, with \(g=7\), \(k=3\), and lengths \((3,4,5)\), the distribution counts at \(h=0,1,2,3\) are \((91,126,84,42)\) among \(7^3\) projected start choices. Thus every value from zero through three occurs.

## Relationship to prior work
D. Jason Gibson, *A density Chinese remainder theorem* (arXiv:1302.0917v1, 2013; Integers 14 (2014), A22), establishes quantitative bounds for two residue-set congruences, including an interval lower bound. Its Section 6 explicitly identifies systems with more than two congruences and additional structural information as further directions. The present result treats any number \(k\ge3\) of short intervals when all pairwise gcds are equal, and gives the complete attainable count spectrum as well as its exact finite distribution, neither of which is stated in Gibson's two-modulus theorem.

Earlier coverage-probability work, including A. F. Siegel (1978) on equal-length random arcs on the continuous circle and G. Ailam (1966) on random-set union moments, supplies a relevant complement/coverage viewpoint. The accessible abstracts do not determine the discrete common-gcd varied-length solution-count law. Full-text implication comparisons for these sources remain a priority risk.

The classical generalized CRT supplies the compatibility criterion in Step 1 and is not claimed as new. Zhi-Wei Sun's *A theorem concerning systems of residue classes* (1991) studies covering periods and densities of unions of residue classes, rather than this particular multiway interval-intersection distribution. These comparisons establish a specific distinction, not historical priority for every possible equivalent cyclic-arc formulation.

## Limitations
The 1966/1978 continuous random-coverage literature was available at abstract level, not for complete-text comparison; it may contain broader equivalent formulations. The pairwise common-gcd condition and the restriction of each interval to at most \(g\) residues are essential to the proof. No theorem is claimed for general gcd patterns, longer intervals, arbitrary non-interval residue collections, or the general Lonely Runner Conjecture. The exact composition sum can be expensive for large \(g\); it is not an asymptotic estimate. All originality comparisons are limited to the sources inspected; equivalent formulations in older additive combinatorics or interval-covering literature may exist.

## References
1. D. Jason Gibson, *A density Chinese remainder theorem*, arXiv:1302.0917v1 (first public version 2013-02-05), Section 2, Theorem 2.2, and Section 6. https://arxiv.org/html/1302.0917v1
2. D. Jason Gibson, *A density Chinese remainder theorem*, *Integers* **14** (2014), A22. https://paperzz.com/doc/7203565/a22-integers-14--2014--a-density
3. Zhi-Wei Sun, *A theorem concerning systems of residue classes*, *Acta Math. Univ. Comenianae* **60** (1991), 123–131. https://www.researchgate.net/publication/2301826_A_Theorem_Concerning_Systems_Of_Residue_Classes

4. A. F. Siegel, *Random arcs on the circle*, *Journal of Applied Probability* **15** (1978), 774–789. https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/random-arcs-on-the-circle/F3FC38BAC4003ACAB59AB845361D6C2A
5. G. Ailam, *Moments of coverage and coverage spaces*, *Journal of Applied Probability* **3** (1966), 550–555. https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/moments-of-coverage-and-coverage-spaces/59D3C8BCEF9B6259D348477EF80CC9CF
