# One shared divisor matching across multiple arithmetic progressions: an all-order semiprime density law

## Finding
Let \(p<q\) be primes with \(p\ge5\), and let \(k\ge1\) be an integer. For \(1\le i\le k\), choose positive integers \(a_i,b_i\) with \(\gcd(a_i,b_i)=1\), and form four-term progressions \(P_i(t)=a_i+b_it\), \(t\in\{0,1,2,3\}\). A **common coprime matching** is a single bijection \(f:\{0,1,2,3\}\to\{1,p,q,pq\}\) satisfying \(\gcd(f(t),P_i(t))=1\) for **every** \(i,t\). The same \(f\) must work for all progressions.

Put \(T_r=\{t\in\{0,1,2,3\}:r\mid\prod_{i=1}^k P_i(t)\}\) for \(r\in\{p,q\}\). A common matching exists **if and only if**
\[
|T_p|\le2,\quad |T_q|\le2,\quad |T_p\cup T_q|\le3,\quad |T_p\cap T_q|\le1.
\]
This criterion remains true for arbitrary integer sequences in place of the progressions, without primitivity, with the same four indexed positions.

For \(r\ge5\), define
\[
U_r(k)=\frac{6(r-1)^k-8(r-2)^k+3(r-3)^k}{(r+1)^k},\qquad
W_r(k)=\frac{(r-1)^k-2(r-2)^k+(r-3)^k}{(r+1)^k}.
\]
Among ordered \(k\)-tuples of primitive positive progressions with \(1\le a_i,b_i\le H\), the limiting proportion admitting one common coprime matching is
\[
\boxed{\mathcal D_{p,q}(k)=U_p(k)U_q(k)-12W_p(k)W_q(k).}
\]
More precisely, their number is
\[
\mathcal D_{p,q}(k)\,\zeta(2)^{-k}H^{2k}
 +O_{p,q,k}\bigl(H^{2k-1}\log(2H)\bigr)
\qquad(H\to\infty).
\]
In particular, \(\mathcal D_{p,q}(1)=1\) and
\[
\boxed{\mathcal D_{p,q}(2)=1-\frac{48}{(p+1)^2(q+1)^2}.}
\]
For fixed primes \(p<q\) with \(p\ge5\), the all-order law has the sharp exponential asymptotic
\[
\boxed{\mathcal D_{p,q}(k)\sim24\left(\frac{(p-1)(q-1)}{(p+1)(q+1)}\right)^k}
\qquad(k\to\infty).
\]
The order of limits is important: \(H\to\infty\) is taken with \(p,q,k\) fixed, and the last statement lets \(k\to\infty\) with \(p,q\) fixed.

## Assumptions and scope
The divisor set is exactly \(D(pq)=\{1,p,q,pq\}\) for distinct primes \(p,q\ge5\). Positive progression steps and starts are sampled independently and uniformly from \(\{1,\ldots,H\}\), conditioned separately on \(\gcd(a_i,b_i)=1\). A common matching uses **the same indexed assignment** for all \(k\) progressions. The four-position Hall criterion is valid for any distinct primes, but the displayed density expressions require \(p,q\ge5\): only then can a primitive four-term progression have at most one multiple of each prime.

## Proof
**1. Exact four-position Hall criterion.** At index \(t\), write a forbidden-prime mask according to whether \(t\in T_p\), \(t\in T_q\), both, or neither. The available divisors are respectively \(\{1,q\}\), \(\{1,p\}\), \(\{1\}\), or \(\{1,p,q,pq\}\). Apply Hall's marriage theorem to the bipartite graph whose left vertices are the four indices and whose right vertices are the four divisors. A set containing an index with neither prime forbidden has all four divisors as neighbors. For sets of entirely forbidden indices, the only possible proper neighbor sets are \(\{1\}\), \(\{1,q\}\), \(\{1,p\}\), and \(\{1,p,q\}\). Their Hall inequalities are exactly \(|T_p\cap T_q|\le1\), \(|T_p|\le2\), \(|T_q|\le2\), and \(|T_p\cup T_q|\le3\). Conversely these four inequalities verify Hall for every subset, proving the equivalence.

**2. Local law for one primitive progression.** Let \(r\ge5\) be prime. Primitive integer pairs are asymptotically equidistributed among the \(r^2-1\) pairs \((a,b)\in\mathbb F_r^2\setminus\{(0,0)\}\). For a specified \(t\in\{0,1,2,3\}\), exactly \(r-1\) such pairs satisfy \(a+bt=0\), giving probability \(1/(r+1)\). The four positions are distinct modulo \(r\), and no primitive pair makes two of them zero. The probability of no zero among these four positions is consequently \((r-3)/(r+1)\). For \(k\) independent progressions, the local forbidden index set \(T_r\) is thus the union of \(k\) independent draws, each contributing a specified singleton with probability \(1/(r+1)\) or the empty set with probability \((r-3)/(r+1)\).

**3. Inclusion-exclusion and compatibility.** For any prescribed two-element set \(J\) of indices, the probability \(T_r=J\) equals
\[
\Pr(T_r=J)=\frac{(r-1)^k-2(r-2)^k+(r-3)^k}{(r+1)^k}=W_r(k),
\]
by inclusion-exclusion on the two required positions. Similarly, the probabilities of a prescribed empty or one-element support are \((r-3)^k/(r+1)^k\) and \(((r-2)^k-(r-3)^k)/(r+1)^k\). Adding one empty, four singleton, and six doubleton cases yields
\[
\Pr(|T_r|\le2)=\frac{6(r-1)^k-8(r-2)^k+3(r-3)^k}{(r+1)^k}=U_r(k).
\]
The local support sets \(T_p,T_q\) are independent by the Chinese remainder theorem. When both have size at most two, the four Hall conditions fail precisely when both have size two and their intersection has size zero or two. Among the \(6\times6\) ordered pairs of two-element subsets, exactly \(12\) are forbidden (for each first subset, the identical and disjoint complementary second subsets). Each pair has probability \(W_p(k)W_q(k)\). Subtraction gives the displayed \(\mathcal D_{p,q}(k)\).

**4. Density for coprime positive integer parameters.** Fix \(m=pq\). For every residue pair \((\alpha,\beta)\pmod m\) satisfying \(\gcd(\alpha,\beta,m)=1\), Möbius inversion gives
\[
\#\{1\le a,b\le H:\gcd(a,b)=1,\ (a,b)\equiv(\alpha,\beta)\pmod m\}
 =\frac{H^2}{m^2\zeta(2)\prod_{r\mid m}(1-r^{-2})}+O_m(H\log(2H)).
\]
Indeed, the common divisor in the Möbius sum must be coprime to \(m\); for each such divisor, the two residue conditions each have \(H/(dm)+O(1)\) solutions. Summing the errors gives \(O_m(H\log(2H))\), and the main Euler product evaluates as stated. The allowed residue pairs number \(m^2\prod_{r\mid m}(1-r^{-2})\); hence their conditional distribution is uniform and its local components at \(p\) and \(q\) are independent. Taking \(k\) independent pairs establishes the count with main factor \(\zeta(2)^{-k}H^{2k}\) and the stated error.

**5. Special cases and sharp order decay.** For \(k=1\), the two-element support probability vanishes and \(U_r(1)=1\). For \(k=2\), \(U_r(2)=1\) and \(W_r(2)=2/(r+1)^2\), yielding \(\mathcal D_{p,q}(2)=1-48/((p+1)^2(q+1)^2)\). For fixed \(r\ge5\), both \(U_r(k)\sim6((r-1)/(r+1))^k\) and \(W_r(k)\sim((r-1)/(r+1))^k\); substituting yields the sharp factor \(6\cdot6-12=24\). This proves the final asymptotic.

## Verification
Run `python3 verify.py` (Python standard library only). It checks the four Hall inequalities against every perfect matching across all \(4^4=256\) forbidden-mask patterns; checks the local residue probabilities by enumerating primitive pairs modulo \(5,7,11\); exhausts all \(1,327,104\) ordered pairs of primitive progression parameter classes modulo \(35\) for \(k=2\) (exactly \(27,648\) fail, so \(\mathcal D_{5,7}(2)=47/48\)); and independently computes the all-order local support distributions for \(k=1,\dots,7\) at three pairs of primes using exact dynamic programming, agreeing with the closed formula. The examples \(P_1(t)=35+t,P_2(t)=34+t\) and \(P_1(t)=5+t,P_2(t)=4+t\) each admit individual coprime matchings but no common one to the divisors of \(35\). These finite checks supplement the symbolic proof; they are not a substitute for its unbounded assertions.

## Relationship to prior work
Alekseyev's 2026 arithmetic-progression criterion characterizes whether a divisor set can be coprimely matched with **one** progression; it asserts existence of a potentially different matching for every primitive progression, not existence of **one common matching** for several independently chosen progressions. McNew and Pomerance established divisor-set matchability and motivated universal single-progression questions. The present problem interchanges the matching and progression quantifiers, which the earlier theorems cannot justify: the two explicit primitive-progression pairs above are counterexamples to that quantifier interchange. A separate joint-density identity for several divisor sets sharing **one** progression also permits separate matchings and does not supply the common-bijection theorem here. The contribution is the semiprime common-matching criterion together with its exact, all-order arithmetic density and exponential decay, not Hall's theorem itself.

## Limitations
The closed density and asymptotic are proved for two distinct primes at least five and four indexed terms; the general four-index Hall criterion has no such restriction. The formulas do not extend by the same singleton-root argument to primes two and three, to divisor sets with three or more prime factors, or to a requirement that each progression be matched with a different assignment. The limit in the number of progressions is not uniform in the prime parameters. Historical priority outside the inspected primary literature remains uncertain.

## References
1. M. A. Alekseyev, *Coprime matchings of divisor sets*, arXiv:2610.37512v1, first public 27 October 2026; and M. A. Alekseyev and B. Beyer de Ryke, expanded arXiv:2610.37512v2. https://arxiv.org/abs/2610.37512
2. N. McNew and C. Pomerance, *Matchable numbers*, arXiv:2604.05304, first public 7 April 2026. https://arxiv.org/abs/2604.05304
3. P. Hall, *On representatives of subsets*, Journal of the London Mathematical Society 10 (1935), 26–30. https://doi.org/10.1112/jlms/s1-10.37.26
