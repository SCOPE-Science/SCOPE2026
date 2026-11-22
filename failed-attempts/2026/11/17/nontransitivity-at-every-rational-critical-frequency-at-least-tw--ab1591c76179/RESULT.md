# Nontransitivity at every rational critical frequency at least two thirds

## Finding
For each pair of coprime positive integers \(a,b\) with \(a\geq 2b\), put \(c=a/(a+b)\). The Becker–Baraviera one-sided frequency shift \(\Sigma(c)\) is **not topologically transitive**. In fact the admissible marker
\[
\omega=0^{b}1^{a+1}0
\]
can occur only at the very beginning of an unshifted generating sequence in \(P(c)\). Therefore \(\omega v\omega\) is forbidden for every finite binary word \(v\). This gives nontransitivity at all rational \(c\in[2/3,1)\), including nonintegral ratios \(c/(1-c)\), a dense family beyond the integer-ratio cases previously established.

## Assumptions and scope
Let \(P(c)\subset\{0,1\}^{\mathbb N}\) contain exactly those infinite binary words in which, whenever the current letter is \(1\), the next letter is \(1\) if the current prefix density of ones is at most \(c\), and is \(0\) otherwise; after a \(0\), either next letter is allowed. Set \(\Sigma(c)=\overline{\bigcup_{n\ge0}\sigma^n(P(c))}\) in the product topology. A subshift is topologically transitive if for every two words \(u,v\) in its language some connecting word \(z\) makes \(uzv\) admissible. The theorem concerns precisely this one-sided shift and all reduced rationals \(c=a/(a+b)\) with \(a\ge2b>0\). The mathematical argument uses no finite enumeration.

## Proof
Define \(\beta=c/(1-c)=a/b\) and, for a finite prefix \(w\), its discrepancy \(D(w)=\beta |w|_0-|w|_1\). After a \(1\), the next letter is \(1\) exactly when the current \(D\) is nonnegative. A zero increases \(D\) by \(\beta\), and a one decreases it by one. These observations follow immediately by rearranging the defining density inequality.

**Run lemma.** Every finite maximal run of ones in any generating sequence \(x\in P(c)\) ends with discrepancy in \([-1,0)\). To prove this, suppose \(d\ge0\) is the discrepancy just before the run. Then its length is exactly \(r=\lfloor d\rfloor+1\): the first \(\lfloor d\rfloor\) ones are each followed by another one, and the last one is followed by a zero. The terminal discrepancy \(d-r\) lies in \([-1,0)\). For the first run, either it begins at the first coordinate (then \(d=0\)) or follows some initial zeros (then \(d\ge0\)). Inductively, after any closed run the terminal discrepancy \(\delta\in[-1,0)\); since a later run follows at least one zero and \(\beta\ge2\), its starting discrepancy is \(d=\delta+\beta\ell\ge1\). Thus every completed run has the asserted residual interval. No assertion about an infinite final run is required.

Consider a completed run \(1^{a+1}\) preceded by some zeroes. If it is the first run, with \(\ell\ge0\) initial zeros, then its starting discrepancy is \(\beta\ell\). The run lemma gives \(a\le\beta\ell<a+1\). Since \(\beta b=a\) and \(\beta\ge2\), this forces \(\ell=b\): a smaller integer \(\ell\) gives at most \(a-\beta<a\), while a larger one gives at least \(a+\beta>a+1\).

If it is any later run, let \(\delta\in[-1,0)\) be the terminal discrepancy after the preceding completed run, and let \(\ell\ge1\) be the number of intervening zeros. Its initial discrepancy is \(d=\delta+\beta\ell\). There are three mutually exhaustive cases:

* For \(\ell\le b-1\), \(d<\beta(b-1)=a-\beta\le a-2\), so its length is at most \(a-1\).
* For \(\ell=b\), \(a-1\le d<a\), so its length is exactly \(a\).
* For \(\ell\ge b+1\), \(d\ge a+\beta-1\ge a+1\), so its length is at least \(a+2\).

Thus no later completed run has length \(a+1\). Consequently an occurrence of \(\omega=0^b1^{a+1}0\) in \(P(c)\), if any, begins at coordinate one. The generating word \(\omega0^{\infty}\) satisfies all the transition rules, so the marker does occur in the language.

Any finite word in the language of \(\Sigma(c)\) is a factor of some generating sequence in \(P(c)\): the corresponding cylinder is open, hence an occurrence in a closure point is already witnessed in some shifted generating sequence. If \(\omega z\omega\) were admissible for any finite \(z\), a generating sequence would contain two occurrences of \(\omega\), contrary to the preceding paragraph. Therefore there is no word joining \(\omega\) to itself, and \(\Sigma(c)\) is not topologically transitive. \(\square\)

## Verification
A standalone exact-integer finite-prefix checker (`verification/check_frequency_marker.py`) enumerates valid prefixes under the original transition rule, checks that the marker never begins at a positive offset, and verifies the explicit generating witness. Eight representative coprime parameter pairs were tested, encompassing both known integer ratios and new noninteger ratios. Finite testing corroborates rather than replaces the complete proof above.

## Relationship to prior work
Reyes, *Frequency shifts: non-soficity, absence of specification and intrinsic ergodicity* (arXiv:2611.10995v1, November 7, 2026), gives the discrepancy and run-length rules and proves nontransitivity for \(c=k/(k+1)\), integer \(k\ge2\), in Theorem C(b)/Proposition 5.8. Question 7.1 explicitly asks which other parameters are transitive. The present marker is new for every coprime \(a,b\) with \(b\ge2\) and \(a>2b\); none of the integer-quotient results logically covers these ratios. Earlier Becker–Baraviera work introduces the shift, its finite-type obstruction, and entropy properties. A separate earlier result on rational \(c<1/2\) addresses a disjoint range, and makes no implication about the present parameter regime.

## Limitations
The theorem does not classify irrational critical densities or the intermediate interval \(1/2<c<2/3\), does not establish unique maximal-entropy measures, and does not determine the complete nonwandering set. The marker proof establishes nontransitivity but not a full language classification. The 2023 founding article was accessible only through secondary bibliographic/abstract descriptions in this review; priority risk from its unavailable complete text and other unindexed work remains. No independent validation has occurred.

## References
1. C. Reyes, *Frequency shifts: non-soficity, absence of specification and intrinsic ergodicity*, arXiv:2611.10995v1 (first posted November 7, 2026), https://arxiv.org/html/2611.10995v1, especially Sections 2, 5 and 7.
2. A. J. Becker and A. T. Baraviera, *Symbolic Systems with Prescribed Partial Digit Density*, Journal of Statistical Physics **190** (2023), article 143, https://doi.org/10.1007/s10955-023-03158-8.
