# Two-read deletion ambiguity across all bounded-homopolymer sources

## Finding
Let \(q\ge 2\) and \(r\ge 2\) be integers, and let \(\Sigma\) be a labeled alphabet of size \(q\). Write \(\mathcal L_{q,r}(n)\) for the indexed length-\(n\) words whose maximal constant-symbol runs have length at most \(r\). For each word \(w\), let \(D_1(w)\) be the **set of distinct** words obtained by deleting exactly one coordinate. Define an undirected graph \(G_{q,r}(n)\) on \(\mathcal L_{q,r}(n)\), joining distinct \(x,y\) when \(|D_1(x)\cap D_1(y)|=2\).

For \(n\ge2\), let \(e_{q,r}(n,L)\) be the number of unordered edges whose first and last differing positions delimit an interval of length exactly \(L\). Set \(S_r(z)=z+z^2+\cdots+z^r\) and \(H_{q,r}(z)=(1+S_r(z)-2z^r)/(1-(q-1)S_r(z))\). **For all the stated alphabet sizes, run caps, and lengths, the full disagreement-span enumerator is**
\[
\boxed{\sum_{n\ge0}\sum_{L\ge2} e_{q,r}(n,L)z^n u^L
=\binom q2\frac{u^2z^2}{1-uz}\,H_{q,r}(z)^2.}
\]
In particular, with \(e_{q,r}(n)=|E(G_{q,r}(n))|\),
\[
\boxed{\sum_{n\ge0}e_{q,r}(n)z^n
=\binom q2\frac{z^2(1+S_r(z)-2z^r)^2}
{(1-z)(1-(q-1)S_r(z))^2}.}
\]
Both series have zero coefficients at lengths zero and one. This is an exact result about the *two-distinct-read* exclusion graph, not the ordinary one-deletion-correction graph.

There is also a universal limiting ambiguity-span law. Let \(R=R_{q,r}\in(0,1)\) be the unique positive solution to \((q-1)S_r(R)=1\). If an unordered edge of \(G_{q,r}(n)\) is chosen uniformly, its span \(L_n\) satisfies, for every fixed integer \(\ell\ge2\),
\[
\boxed{\lim_{n\to\infty}\Pr(L_n=\ell)
=(1-R)R^{\ell-2}.}
\]
Thus its limiting span has the distribution \(2+\operatorname{Geom}_0(1-R)\), with mean \(2+R/(1-R)\). Moreover, the graph's average degree grows linearly:
\[
\boxed{\overline d(G_{q,r}(n))\sim \kappa_{q,r}n,\quad
\kappa_{q,r}=\frac{q(q-1)R[1+S_r(R)-2R^r]^2}
{(1-R)(-D'(R))[1+S_r(R)]},\quad
D(z)=1-(q-1)S_r(z).}
\]

For the first nontrivial binary cap \(q=r=2\), the edge generating series reduces to
\[
\frac{z^2(1+z-z^2)^2}{(1-z)(1-z-z^2)^2},
\]
with edge counts for lengths \(2\) through \(12\) equal to \(1,5,13,29,61,121,233,437,805,1461,2621\). In this case \(R=(\sqrt5-1)/2\) and the limiting expected span is \(2+\varphi\), where \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope
The source words are linear and indexed, not cyclic or rotation classes. The alphabet is labeled. A constant-symbol run is a maximal contiguous block of one symbol. A deletion output counts once even when several positions yield it, and one read is an arbitrary single-coordinate deletion; outputs need not remain run-limited. A forbidden pair is one for which **two different** length-\(n-1\) outputs can arise from each source word. The differing interval of an edge is defined intrinsically by the smallest and largest coordinates where its endpoints disagree; it is never a chosen, noncanonical interval. The result covers all \(q,r\ge2\) and all \(n\), without assuming even lengths or special symbol compositions.

## Proof
**1. Unique alternating-interval representation.** Proposition 9 of Cai–Kiah–Nguyen–Yaakobi [2] states that distinct equal-length words have exactly two common single-deletion outputs if and only if they agree outside an interval of at least two coordinates and inside that interval are the two opposite phases of a word alternating between two distinct letters. Their Hamming-distance-one case yields just one common deletion output. The interval is unique: its endpoints are the first and last differing coordinates. The unordered pair of alternating letters is also unique. Conversely, the two phases share the two outputs obtained by removing the first or the last letter of the alternating block. No unordered edge can arise from two such representations.

**2. Run restrictions at the two interfaces.** Fix an unordered pair of distinct letters \(\{a,b\}\), a central alternating interval of length \(L\ge2\), and an outside prefix \(p\) and suffix \(s\). The central interval contributes only unit runs. Both opposite-phase words lie in \(\mathcal L_{q,r}\) if and only if each of \(p,s\) is itself run-limited and the following interface rule holds: if the adjacent terminal letter of \(p\) (or initial letter of \(s\)) belongs to \(\{a,b\}\), its boundary run is strictly shorter than \(r\). If that letter lies outside \(\{a,b\}\), a boundary run of full length \(r\) is allowed. This is necessary because one of the two central phases joins that boundary run; it is sufficient because there are no other cross-boundary run mergers. For \(L\ge2\) the two interfaces are separated and are independent.

**3. Counting admissible contexts.** Let \(S=S_r(z)\) and \(D=1-(q-1)S\). The generating function for all (including empty) run-limited words is
\[
A_{q,r}(z)=1+\frac{qS}{1-(q-1)S}=\frac{1+S}{D}.
\]
Indeed, a nonempty word consists of one run, whose initial letter has \(q\) choices, followed by zero or more runs, each choosing a letter different from its predecessor in \(q-1\) ways. For a prescribed unordered letter pair \(\{a,b\}\), the generating function for forbidden prefix contexts—those whose last run is of length exactly \(r\) and bears letter \(a\) or \(b\)—is \(2z^r/D\): choose its final symbol in two ways and any finite sequence of preceding runs, whose next-run colors each have \(q-1\) choices. The same count applies to forbidden suffix contexts by reversal. Subtraction gives the common admissible-context function
\[
H_{q,r}(z)=A_{q,r}(z)-\frac{2z^r}{D}
=\frac{1+S-2z^r}{D}.
\]
For each selected letter pair, prefix and suffix therefore contribute \(H_{q,r}(z)^2\), independently of which phase is assigned to which endpoint of the unordered source pair.

**4. Exact bivariate count.** The canonical central interval has any length \(L\ge2\) and contributes \(z^L u^L\), so its series is \(z^2u^2/(1-zu)\). There are \(\binom q2\) unordered pairs of central letters. Multiplying the three independent choices gives the first boxed identity; setting \(u=1\) gives the second. Uniqueness in step 1 rules out multiplicity overcounting. Coefficient extraction also gives the explicit formula
\[
e_{q,r}(n,L)=\binom q2[z^{n-L}]H_{q,r}(z)^2
\quad (2\le L\le n),
\]
with all other span coefficients zero.

**5. Asymptotic law.** Since \(r\ge2\), the polynomial \(D\) has a root \(R\) strictly between zero and one. It is the unique root of minimum modulus: if a complex root \(z\) had \(|z|=R\), the triangle inequality in \((q-1)\sum_{j=1}^r z^j=1\) would force both \(z/R\) and \((z/R)^2\) to have the same positive phase, hence \(z=R\). The root is simple because \(D'(R)<0\). Put \(N(z)=1+S_r(z)-2z^r\); its positive value at \(R\) implies
\[
[z^m]H_{q,r}(z)^2\sim
\frac{N(R)^2}{R^2D'(R)^2}(m+1)R^{-m}.
\]
The vertex series \(A_{q,r}(z)=(1+S_r(z))/D(z)\) similarly yields
\[
|\mathcal L_{q,r}(n)|\sim
\frac{1+S_r(R)}{-RD'(R)}R^{-n}.
\]
The edge series has a double pole at \(R\) with leading coefficient
\[
e_{q,r}(n)\sim
\binom q2\frac{N(R)^2}{(1-R)D'(R)^2}\,nR^{-n}.
\]
Taking the ratio of its fixed-span coefficient to the total coefficient gives \((1-R)R^{\ell-2}\). Dividing twice the edge count by the number of vertices proves the displayed average-degree constant. The limiting span masses sum to one; the geometric mean follows by summing their first moments (or by differentiating the exact bivariate series).

## Verification
The included `verifier_bruteforce.py` creates every admissible source word, constructs its distinct one-deletion descendants, and tests each unordered pair for two common outputs. It also checks that every observed edge has the stated unique opposite-phase alternating interval. This was replayed for \(q\in\{2,3,4,5\}\), run caps ranging from one through four, and admissible lengths up to eight. The run-cap-one cases are external consistency checks and not claimed as new.

Independently, `verifier_recurrence.py` computes a finite-state prefix count from terminal-run lengths, convolves contexts into an edge count, and separately extracts coefficients from the rational expression by clearing polynomial denominators. Both approaches agree for 64 parameter pairs with \(2\le q\le9\), \(1\le r\le8\), and every length through 100. Their deterministic outputs and exact program texts are included. Finite checks corroborate the statement; its generality rests on the proof above and the published alternating-interval lemma.

## Relationship to prior work
The unrestricted two-read graph and its alternating-block characterization are established in [2,3] and enumerated for the full \(q\)-ary Hamming space in [4]. Those results do not yield the edge count on the induced bounded-homopolymer subset without a separate boundary-compatibility count. In particular, the unrestricted edge count is not the difference of unrestricted counts at two block lengths. Kulkarni and Kiyavash [1] study run-limited single-deletion-correcting sources using hypergraph bounds, but not the two-distinct-read exclusion graph or its span spectrum. The earlier zero-repeat case \(r=1\) has already been enumerated elsewhere; the theorem deliberately claims \(r\ge2\), including the previously untreated finite run-cap interfaces and the limiting geometric law. An existing binary unrestricted degree-spectrum result [5] and a bounded-run bigram-profile result [6] concern different graphs/observations; neither implies this induced-graph edge series.

## Limitations
The theorem supplies exact two-read-confusability counts and span distributions, not independence numbers, maximum reconstruction-code sizes, chromatic numbers, or multi-deletion results. It relies on the established Type-A characterization rather than reproving that general statement. The limiting geometric law is for a uniformly sampled **edge**, not for a uniformly sampled word or error event. Scientific priority in unindexed older constrained-reconstruction literature cannot be ruled out by the available searches; independent validation has not been performed.

## References
1. A. A. Kulkarni and N. Kiyavash, “Non-asymptotic Upper Bounds for Deletion Correcting Codes,” arXiv:1211.3128, first public 2012-11-13, especially Section V, https://arxiv.org/abs/1211.3128.
2. K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, “Coding for Sequence Reconstruction for Single Edits,” arXiv:2001.01376, first public 2020-01-06, Proposition 9, https://arxiv.org/abs/2001.01376.
3. J. Chrisnata, H. M. Kiah and E. Yaakobi, “Optimal Reconstruction Codes for Deletion Channels,” arXiv:2004.06032, first public 2020-04-13, https://arxiv.org/abs/2004.06032.
4. “Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph,” published-finding corpus 2026/10/4, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91.
5. “Complete degree spectrum of the binary two-read deletion-reconstruction graph,” published-finding corpus 2026/11/2, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-degree-spectrum-of-the-binary-two-read-deletion-reconst--f45a481280b1.
6. “Exact bigram-spectrum reconstruction under a bounded-run constraint,” published-finding corpus 2026/10/12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-bigram-spectrum-reconstruction-under-a-bounded-run-constra--359f20149e86.
