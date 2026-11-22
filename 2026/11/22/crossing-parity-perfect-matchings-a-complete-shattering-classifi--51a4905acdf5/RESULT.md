# Crossing-parity perfect matchings: a complete shattering classification and an exact quadratic top-face gap

## Finding

Place \(2n\) labeled vertices \(1,\ldots,2n\) in convex cyclic order, with \(n\geq3\). A perfect matching \(M\) has sign \(\varepsilon(M)=(-1)^{\operatorname{cr}(M)}\), where \(\operatorname{cr}(M)\) counts pairs of matching chords crossing in their interiors. For each \(\sigma\in\{+1,-1\}\), let \(\mathcal H_{n,\sigma}\) be the binary edge-incidence concept class of all matchings of sign \(\sigma\): a chord query is positive exactly when it belongs to \(M\).

**Complete shattering classification.** A chord support \(S\) is shattered by \(\mathcal H_{n,\sigma}\) exactly in the following cases:

1. \(S\) is a partial matching of size \(|S|\leq n-2\); or
2. \(S\) is a partial matching of size \(n-1\), its unique completion \(M=S\cup\{e_*\}\) has sign \(\sigma\), and the omitted chord \(e_*\) crosses none of the chords of \(S\).

No other supports are shattered. In particular, both parity classes have \(\operatorname{VCdim}=n-1\).

Let \(\Phi_{n,\sigma}(z)=\sum_{S\text{ shattered}}z^{|S|}\). With the convention \((-1)!!=1\), put
\[
L_n=\sum_{r=0}^{n-1}(2n-2r-1)(2r-1)!!\,(2n-2r-3)!!.
\]
The full face enumerator is
\[
\boxed{\displaystyle
\Phi_{n,\sigma}(z)=\sum_{s=0}^{n-2}\frac{(2n)!}{(2n-2s)!\,2^s s!}\,z^s+
\frac{L_n+\sigma n^2}{2}\,z^{n-1}.}
\]
Consequently, the two families have **identical shattered-support counts in every degree below \(n-1\)**, while the positive-crossing-parity class has **exactly \(n^2\) more maximum-size shattered supports** than the negative-crossing-parity class:
\[
[z^{n-1}](\Phi_{n,+1}-\Phi_{n,-1})=n^2.
\]
For example, \(\Phi_{5,+1}(z)=1+45z+630z^2+3150z^3+635z^4\), whereas \(\Phi_{5,-1}(z)=1+45z+630z^2+3150z^3+610z^4\).

The formula also holds at \(n=2\) if the degree-one term is interpreted as written: there are four shattered singleton supports for sign \(+1\), none for sign \(-1\), and the latter class has VC dimension zero. The main two-class dimension statement starts at \(n=3\).

## Assumptions and scope

Every matching is a perfect matching of the complete graph on the fixed cyclically ordered \(2n\) vertices. All chords, including polygon sides, are valid edge queries. A support is shattered only when **every** labeling of its chords is attained by a matching of the prescribed crossing parity. Chords sharing endpoints cannot simultaneously be positive. A crossing is a strict alternation of chord endpoints, so nesting is not a crossing. The model uses *crossing parity*, not the parity of the number of permutation inversions under an independently chosen convention. The signs coincide with the standard Pfaffian matching signs for increasing labels.

## Proof

**1. Parity of four-point switches.** For four increasing vertices \(a<b<c<d\), the three pairings are \(\{ab,cd\}\), \(\{ac,bd\}\), and \(\{ad,bc\}\). Their local Pfaffian signs are respectively \(+,-,+\). For any fixed pairing of all other vertices, ratios of the full matching signs agree with these local ratios: in the Pfaffian expansion, fixing the outside pairs introduces a common sign factor. Thus if an original two-edge pairing is noncrossing, one of its two alternative pairings has the same sign and one the opposite sign; if the original pairing is crossing, **both** alternatives have the opposite sign.

**2. A two-sign extension lemma.** Let \(m\ge3\) and let \(F\) be any matching of forbidden edges on \(2m\) ordered vertices (possibly empty or of size \(m\)). There exist perfect matchings avoiding \(F\) of *both* crossing parities. For \(m=3\), the complete graph has 15 matchings, eight of positive sign and seven of negative sign. If \(|F|=f\le3\), the number avoiding \(F\), by inclusion-exclusion, is \(15-3f+\binom f2-\binom f3\), which is at least ten for \(f\le2\) and exactly eight for \(f=3\). For \(f\le2\), ten exceeds each entire parity class, so both signs occur. For \(f=3\), eight exceeds the total number of negative-sign matchings, so a positive-sign avoider exists. Also, every individual chord extends to some positive-sign perfect matching: the remaining four vertices have three completions, of which at least one gives positive total sign by the four-point sign rule. Thus a forbidden chord eliminates at least one positive-sign matching, leaving at most seven positive-sign avoiders among the eight avoiders; hence a negative-sign avoider exists too.

For induction \(m\ge4\), choose any two vertices \(u,v\) for which \(uv\notin F\), fix the permitted chord \(uv\), and remove its endpoints. The still-forbidden edges on the remaining \(2(m-1)\) vertices form a matching. The induction hypothesis supplies one avoidance matching of each reduced sign; adjoining the fixed chord multiplies both signs by the same Pfaffian expansion factor. This proves the lemma for every \(m\ge3\).

For \(m=2\) with *no forbidden chord*, the three matchings on four vertices also realize both parities.

**3. Every sufficiently short partial matching is shattered.** Consider any matching support \(S\) with \(s\le n-2\), and any labeling. Let \(P\subseteq S\) be its positively labeled chords, \(p=|P|\). After fixing \(P\), there remain \(2m=2(n-p)\) vertices and the \(s-p\le m-2\) negatively labeled chords form a forbidden matching on them. If \(m\ge3\), Step 2 supplies a completion of either full sign, because the fixed positive chords change the sign by a constant factor. If \(m=2\), the forbidden matching is empty and Step 2's four-vertex case applies. Hence every binary labeling is realized in each parity class.

**4. The critical codimension-one support.** Suppose \(S\) is a matching of size \(n-1\), and let \(e_*\) join its two unused vertices. The all-positive labeling forces the unique complete matching \(M=S\cup\{e_*\}\), hence \(\varepsilon(M)=\sigma\) is necessary. A labeling with at most \(n-3\) positives leaves at least six unmatched vertices and at most \(m-1\) forbidden chords, so Step 2 realizes it with sign \(\sigma\). If exactly \(n-2\) support chords are positive, exactly one queried chord \(e\in S\) must be negative and four vertices remain. The three pairings of those four vertices are the original \(\{e,e_*\}\) and its two alternatives. By Step 1, an allowed alternative of the *same* sign \(\sigma\) exists if and only if \(e\) and \(e_*\) do **not** cross. Requiring this for every \(e\in S\) gives exactly condition 2 of the theorem.

A support that is not a matching cannot realize the all-positive labeling; a support with \(n\) or more chords cannot be shattered, since at most \(n\) edges can be simultaneously positive, and with exactly \(n\) positives the matching is forced, contradicting the labeling that flips one of its edges negative.

**5. Counting faces and the quadratic signed gap.** For \(s\le n-2\), the number of partial matchings of size \(s\) on \(2n\) vertices is \((2n)!/((2n-2s)!2^s s!)\), giving the lower-degree coefficients. A maximum-size shattered support has a *unique* completion \(M\) and a *unique* omitted chord \(e_*\); thus its parity-class count is the number of pairs \((M,e_*)\) such that \(\varepsilon(M)=\sigma\) and \(e_*\) is crossed by no chord of \(M\).

Fix a chord \(e_*=\{a,b\}\), \(a<b\). If it is uncrossed, all vertices strictly between \(a,b\) must be paired internally, as must those outside. It is feasible only for \(b-a-1=2r\) even. There are \((2r-1)!!(2n-2r-3)!!\) such completions, and \(2n-2r-1\) choices of \(a\). Summing gives \(L_n\).

For the signed count, note that when \(e_*\) is uncrossed, no chord internal to \(e_*\) crosses an external chord, so \(\varepsilon(M)\) is the product of the signs of its inside and outside submatchings. For any even linearly ordered set, the signed sum of *all* perfect matchings is one: it is the Pfaffian of the skew matrix with entries \(+1\) above the diagonal, and expansion at the first index gives the alternating sum \(1-1+\cdots+1=1\) by induction. Hence the signed completion count for **each** feasible fixed \(e_*\) is exactly one. The total signed count of pairs \((M,e_*)\) is therefore \(\sum_{r=0}^{n-1}(2n-2r-1)=n^2\). Half the sum and half the difference produce \((L_n\pm n^2)/2\), proving the polynomial and the quadratic gap.

**6. VC dimension.** The support-size upper bound is \(n-1\). For sign \(+1\), an all-polygon-side matching has an uncrossed chord and yields a shattered support of size \(n-1\). For sign \(-1\) when \(n\ge3\), take one polygon-side chord \(\{1,2\}\), a crossing pair on four of the remaining vertices, and pair the other vertices by adjacent chords; the side chord remains uncrossed and the whole matching has negative sign. Deleting that side chord gives a shattered \((n-1)\)-support. Both dimensions therefore equal \(n-1\).

## Verification

The standalone `verify_parity_matching.py` directly enumerates every perfect matching on \(2n\) vertices for \(n=2,3,4,5\), partitions them by actual crossing parity, and compares the realized binary label patterns on every support compatible with an all-positive assignment against the theorem's criterion. It executes 18,556 support/parity comparisons, checks every face-polynomial coefficient, and verifies the complete six-vertex forbidden-matching extension base in 76 cases. Reproduced output is stored in `verification_output.txt`. The unrestricted theorem follows from the proofs in Steps 1–6, not from finite extrapolation.

## Relationship to prior work

Aichholzer, Fabila-Monroy, Kindermann, Parada, Paul, Perz, Schnider and Vogtenhuber study perfect matchings with prescribed *numbers* of geometric crossings (IWOCA 2022; expanded open-access 2023 article, inspected in full HTML). Their crossing-number distributions do not impose arbitrary positive and negative edge-trace constraints, and they do not establish the parity-restricted shattered-support classification or the \(n^2\) gap. The noncrossing perfect-matching shattering theorem (public record in published-finding corpus, November 2026) imposes *zero crossings*, not even crossing parity, and its face-activity condition and \(n^2\) **total** maximum-support count do not imply the present parity-resolved theorem. Other perfect-matching support results on ladder graphs and vertex coverage have different host graphs or query predicates. Matoya and Oki (2019) develop Pfaffian signs and parity-based counting tools, but their inspected abstract concerns matroid intersection and counting, not Boolean shattering.

The exact \(n^2\) difference is a *signed* isolation enumeration, not a claim that the classical Pfaffian identity itself is new. Indexed-result and literature searches have not revealed an equivalent classification; this is a limited priority conclusion, not proof of historical uniqueness.

## Limitations

The theorem concerns a complete graph with a fixed cyclic ordering, exact parity of chord crossings, and binary edge-incidence queries. It does not classify exact crossing-number slices, nonconvex point sets, arbitrary matching-covered graphs, or the Littlestone dimension of these parity classes. Published descriptions may use the equivalent Pfaffian-matching-sign terminology; incomplete indexing and literature not inspected remain a priority risk. The computations stop at five matching pairs of vertices; all larger cases depend on the symbolic proofs. No independent mathematical validation is claimed.

## References

1. K. Matoya and T. Oki, *Pfaffian Pairs and Parities: Counting on Linear Matroid Intersection and Parity Problems*, arXiv:1912.00620, first public version 2019-12-02, https://arxiv.org/abs/1912.00620.
2. O. Aichholzer, R. Fabila-Monroy, P. Kindermann, I. Parada, R. Paul, D. Perz, P. Schnider and B. Vogtenhuber, *Perfect Matchings with Crossings*, IWOCA 2022, doi:10.1007/978-3-031-06678-8_4; expanded open-access article in *Algorithmica*, published 2023-07-18, https://link.springer.com/article/10.1007/s00453-023-01147-7.
3. *Face-activity characterization of shattered chord supports in noncrossing perfect matchings*, published-finding corpus public mathematics record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-face-activity-characterization-of-shattered-chord-supports-in-no--1a75a2c4be87 (full mathematical result inspected).
