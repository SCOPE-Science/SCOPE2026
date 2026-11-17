# Every rational frequency below one half gives a transitive nonmixing frequency shift

## Finding

For every pair of coprime integers \(1\le a<b\), the one-sided Becker--Baraviera frequency shift at critical density \(c=a/(a+b)\) is **topologically transitive but not topologically mixing**. The result resolves the transitivity question raised by Reyes for every rational critical density strictly between zero and one half. It also supplies a concrete marker \(\omega\) whose successive occurrences are separated by multiples of \(a+b\).

## Assumptions and scope

Fix integers \(a,b\ge1\) with \(a<b\) and \(\gcd(a,b)=1\); let \(c=a/(a+b)\). Define \(P(c)\) as the one-sided infinite binary sequences satisfying: after a zero either letter is permitted; after a one at index \(i\), the next letter is a one if the density of ones in the prefix through \(i\) is at most \(c\), and is a zero otherwise. Define \(\Sigma(c)=\overline{\bigcup_{j\ge0}\sigma^jP(c)}\). In this one-sided setting, transitivity means any two language words \(u,v\) admit some bridge \(w\) with \(uwv\) in the language. Mixing means this can be done with every sufficiently large prescribed bridge length for each pair \(u,v\).

For a finite prefix \(x\), its integer discrepancy is \(H(x)=a|x|_0-b|x|_1\). The transition after a one depends only on whether \(H(x)\ge0\). A zero adds \(a\), and a one subtracts \(b\). The height of the empty prefix is zero. A *zero state* is the height immediately after a zero, with the last symbol hence equal to zero.

## Proof

**1. All integer zero states communicate.** From any zero state \(h\), if \(h\ge b\), append a one, then every subsequently forced one until the height first becomes negative, and finally the forced zero. This is finite and produces a zero state \(h'<b\), because the height just before that zero belongs to \([-b,-1]\) and \(a<b\). Thus one may first assume \(h<b\).

At any zero state \(h<b\), the two-letter block \(10\) is permitted: the one is chosen freely after zero, and the subsequent zero is forced since \(h-b<0\). This lowers the zero-state height by \(b-a>0\). A freely appended zero raises the height by \(a\). For any desired integer \(K\), coprimality gives \(\gcd(a,b-a)=1\), so there is a sufficiently large nonnegative integer \(t\) with \(h-t(b-a)\equiv K\pmod a\) and \(h-t(b-a)\le K\). Append \(t\) copies of \(10\), then \((K-h+t(b-a))/a\) zeros. Every step is permitted and the final zero state is exactly \(K\). Hence the countable directed graph of zero states is strongly connected. Starting from the empty prefix, the first zero brings the height to \(a<b\); therefore **every integer zero state can actually be reached by a legal prefix**.

**2. Transitivity.** Every finite word of the language of \(\Sigma(c)\) occurs as a factor of some member of \(P(c)\). This follows from the definition as a closure of shifts: cylinders of finite words are clopen. Fix such factors \(u\) and \(v\), and record the integer prefix heights just before their chosen occurrences in \(P(c)\), say \(h_u\) and \(h_v\). Choose a legal prefix ending in zero at height \(h_u\), which is possible by part 1, then append \(u\). The internal transitions of \(u\) are legal because their decisions use the same initial height; its first bit is unrestricted after the preceding zero. Extend the resulting word to the next zero: if it ends in one, the deterministic continuation is a finite string of ones followed by a zero. From this zero state connect to the integer zero state \(h_v\) by part 1, and append \(v\). The result is a legal finite prefix containing \(u\) followed by \(v\); it extends to a member of \(P(c)\). Thus \(uwv\in\mathcal L(\Sigma(c))\) for a suitable bridge \(w\), proving transitivity.

**3. A uniquely located discrepancy marker.** Since \(\gcd(a,b)=1\), choose \(m\ge1\) with \(am\equiv1\pmod b\) and \(am>b\). Let \(r=(am-1)/b+1\ge2\) and \(\omega=1\,0^m1^r0\). Suppose an occurrence of \(\omega\) in a member of \(P(c)\) starts at prefix height \(h\). The initial \(10\) demands \(h-b<0\), hence \(h\le b-1\). For the final run to contain \(r\) consecutive ones, the height after its \((r-1)\)-st one must be nonnegative, giving \(h-b+am-(r-1)b=h+am-rb\ge0\); hence \(h\ge rb-am=b-1\). Therefore \(h=b-1\) is forced, with no alternative. Conversely, starting from the reachable zero state \(b-1\), the marker is legal: the first one drops the height to \(-1\), the \(m\) zeros bring it to \(am-1=b(r-1)\), the \(r\) ones end at \(-b\), and the last zero is forced. So \(\omega\) belongs to the language.

**4. Return congruence and failure of mixing.** If \(\omega\) occurs twice in a word of \(\mathcal L(\Sigma(c))\), take a member of \(P(c)\) containing that entire finite factor. The prefix heights immediately before both occurrences are \(b-1\). Thus the intervening segment has zero discrepancy: \(aN_0-bN_1=0\), where \(N_0,N_1\) are its zero and one counts. Coprimality implies \(N_0=bt\), \(N_1=at\), so the separation of the two marker starts equals \((a+b)t\). In particular \(\omega w\omega\) can belong to the language only if \(|\omega|+|w|\equiv0\pmod{a+b}\). At least one residue class of every arbitrarily large bridge length is forbidden because \(a+b\ge3\). This contradicts topological mixing. ∎

## Verification

The standalone `check.py` enumerates finite factor samples and replays transition paths for nine coprime pairs \((a,b)\). It checks constructive connectors for \(-12\le h,K\le12\), verifies that the marker can be read from integer heights \(-50\le h\le50\) only when \(h=b-1\), constructs two markers separated by a valid return path and confirms its modulo-\((a+b)\) start-gap, and tests a finite sample of factor concatenations. These are finite regression checks; the universal theorem follows from the mathematical argument above, not from finite enumeration.

Reproduce with `python3 check.py` in the folder containing this document. The checker uses only the Python standard library.

## Relationship to prior work

Becker and Baraviera (2023) introduced the frequency shifts and established their basic entropy and non-finite-type properties. Reyes (2026), whose entire accessible preprint was inspected, proves nonsoficity and failure of weak specification for all parameters, and classifies transitivity on the separate family \(c=k/(k+1)\). His Question 7.1 expressly asks which parameters yield transitive frequency shifts, stating that only that family was settled. Here \(c<1/2\) and hence does not belong to that family, except at the excluded endpoint. The new proof uses integer height connectivity for rational values below one half, whereas the marker establishes a modular obstruction to mixing.

## Limitations

The classification is for **rational critical densities strictly below one half**. It does not classify irrational parameters, rational parameters above one half, equilibrium measures, or intrinsic ergodicity. It does not assert the converse of the marker return-time congruence. Full text of the 2023 initiating article could not be inspected; only bibliographic metadata, abstract and Reyes's explicit description of its results were available. Relevant unindexed work may affect historical priority. No independent audit is claimed.

## References

1. Carlos Reyes, *Frequency shifts: non-soficity, absence of specification and intrinsic ergodicity*, arXiv:2611.10995v1, first submitted November 7, 2026. https://arxiv.org/html/2611.10995v1 (Definition 2.2, Lemma 2.4, Theorem C, Question 7.1).
2. Alex J. Becker and Alexandre T. Baraviera, *Symbolic Systems with Prescribed Partial Digit Density*, Journal of Statistical Physics **190** (2023), article 143, DOI: 10.1007/s10955-023-03158-8.
