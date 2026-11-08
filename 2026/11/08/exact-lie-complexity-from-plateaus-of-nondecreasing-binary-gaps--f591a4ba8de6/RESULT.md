# Exact Lie complexity from plateaus of nondecreasing binary gaps

## Finding

Let \(g_1\le g_2\le\cdots\) be any unbounded nondecreasing sequence of positive integers, and set
\[
\mathbf w=1\,0^{g_1}1\,0^{g_2}1\,0^{g_3}1\cdots.
\]
For each integer \(a\ge1\), let \(m_a=\#\{i\ge1:g_i=a\}\). Each \(m_a\) is finite, possibly zero. For \(n\ge1\), write \(L_{\mathbf w}(n)\) for the number of cyclic-rotation classes of length-\(n\) factors of \(\mathbf w\) **all of whose rotations also occur** as factors. Then
\[
\boxed{L_{\mathbf w}(n)=2+\sum_{\substack{a\ge1,\ (a+1)\mid n\\2\le n/(a+1)\le m_a}}1.}
\]
The rotation-complete classes are precisely those represented by \(0^n\), \(10^{n-1}\), and, for every summand above, \((10^a)^{n/(a+1)}\). These are distinct classes.

Consequently, strictly increasing positive gaps give \(L_{\mathbf w}(n)=2\) at every positive length. Conversely, a natural nondecreasing-gap word with \(m_a=a\) for each \(a\ge1\) has unbounded Lie complexity: for every integer \(t\ge4\),
\[
L_{\mathbf w}(t!)\ge t+1.
\]
The exact formula distinguishes bounded and unbounded Lie complexity within the same sparse, monotone-gap construction, without assuming recurrence or automaticity.

## Assumptions and scope

The word is right-infinite, begins in \(1\), has the binary alphabet \(\{0,1\}\), and has **positive, nondecreasing, unbounded** complete zero-gap lengths. The starting marker convention matters: allowing a leading partial zero gap can create finite-length boundary exceptions. Cyclic rotation acts on a finite length-\(n\) factor, not on the infinite word; a class is counted only if *every* rotation belongs to the factor language. The claimed formula concerns \(n\ge1\); the empty-factor convention is not included.

Unbounded monotone gaps imply each \(m_a\) is a finite nonnegative integer. The summation is finite because \(a+1\le n/2\) whenever the quotient is at least two. The formula makes no assumption that every positive gap length appears.

## Proof

**Baseline classes.** Since the gap sequence is unbounded, every \(0^n\) occurs. For every \(0\le j\le n-1\), a marker sufficiently far into the word has both adjacent zero gaps of length at least \(n-1\). Thus \(0^j10^{n-1-j}\) occurs. All rotations of \(10^{n-1}\) are therefore factors. The all-zero and one-marker classes are distinct.

**Rigidity of cyclic gaps.** Suppose a length-\(n\) factor \(u\) contains \(r\ge2\) ones and every cyclic rotation of \(u\) is a factor. There are no consecutive ones anywhere in \(\mathbf w\), hence in the circular word \(u\) every one-to-next-one zero gap has length at least one: otherwise a rotation would contain \(11\). List these cyclic gaps as \(a_1,\ldots,a_r\), with all indices taken modulo \(r\).

For each \(i\), rotate \(u\) to begin with the \(a_{i-1}\) zeros immediately before the \(i\)-th one, followed by that one, \(a_i\) zeros, and the next one. This rotation is a factor by hypothesis. In an occurrence, the source zero gap directly before the specified first one has length **at least** \(a_{i-1}\), while the following source gap has length **exactly** \(a_i\), since the next one also lies in the factor. By nondecreasing source gaps, the preceding gap is no longer than the following gap. Consequently \(a_{i-1}\le a_i\). Running around the circular list gives
\[
a_1\le a_2\le\cdots\le a_r\le a_1,
\]
so all the gaps equal a common \(a\ge1\). Therefore \(n=r(a+1)\), and \(u\) belongs to the class of \((10^a)^r\).

**Plateau necessity.** If the class of \((10^a)^r\) is rotation-complete, the specific rotation
\[
0^a(10^a)^{r-1}1
\]
occurs. In this occurrence, the source gap immediately preceding the first displayed one has length at least \(a\), and the following \(r-1\) complete gaps all equal \(a\). Nondecreasing gaps force the preceding gap to equal \(a\) as well. The source gap sequence therefore contains at least \(r\) consecutive copies of \(a\), or \(m_a\ge r\).

**Plateau sufficiency.** If \(m_a\ge r\), select \(r\) consecutive gaps of length \(a\). The source word contains the segment \((10^a)^r1\), followed by at least \(a\) further zeros because the next gap is no shorter than \(a\). Thus \((10^a)^r10^a\) occurs. All \(a+1\) distinct cyclic shifts of the periodic word \((10^a)^r\) occur as length-\(r(a+1)\) factors beginning at offsets \(0,1,\ldots,a\) in this segment. Hence its entire conjugacy class is present.

The preceding steps classify every possible rotation-complete class. Different numbers of ones or different values of \(a\) give different classes, yielding the formula.

**Unbounded example.** Take \(m_a=a\) for every \(a\ge1\). Fix \(t\ge4\), put \(n=t!\), and for each integer \(r\in\{2,\ldots,t\}\) take \(a=n/r-1\). These \(t-1\) values are distinct positive integers. Since \(n/r-1\ge r\) throughout the range (the smallest ratio occurs at \(r=t\), and \((t-1)!-1\ge t\)), the corresponding \(m_a=a\) satisfies the plateau criterion. Each contributes a distinct class in addition to the two baseline classes. Thus \(L_{\mathbf w}(t!)\ge t+1\).

## Verification

The standard-library Python file `verify_lie.py` independently constructs finite prefixes, lists every length-\(n\) factor, partitions them into rotation classes, and selects exactly the classes for which every rotation occurs. It compares that direct language computation against the divisor/plateau formula and representatives.

A finite prefix is complete for a tested length when its later gaps all exceed that length and at least one marker has adjacent gaps exceeding that length: factors containing at least two ones can use only earlier full gaps, while all possible zero-only and single-marker length-\(n\) factors are present. The checker explicitly arranges this condition.

Run with `python3 verify_lie.py`. The recorded run returned `PASS exhaustive_cases= 5120 random_and_family_cases= 3668 total= 8788`, covering every multiplicity assignment in \(\{0,1,2,3\}^4\) through length 20, deterministic randomized assignments with skipped values through length 28, and strict and linear multiplicity families through length 36. Such finite tests support but do not replace the proof for arbitrary infinite sequences.

## Relationship to prior work

Bell and Shallit introduced Lie complexity and proved a universal bound using the first difference of factor complexity; their construction also shows the possibility of many primitive periodic factors. These general results do not classify the rotation-complete factors of a monotone-gap word or determine their lengths via plateau multiplicities. De Luca and Fici evaluate Lie complexity for Sturmian words, a different class with linear factor complexity. Li studies Lie complexity, Rauzy graph cycles, and extended variants, without this monotone-gap divisibility formula. The older cyclic-complexity invariant counts classes meeting the language, not only those fully contained in it; it therefore cannot be substituted for Lie complexity.

The complete-plateau classification makes clear why a previously studied geometric-support word can have only baseline classes away from its exceptional initial boundary, while also producing unbounded Lie complexity from long finite plateaus. A geometric-support calculation with an initial neighboring-marker anomaly does not imply the present all-gap theorem.

## Limitations

The theorem does not cover decreasing, oscillating, or bounded gap sequences; neither does it cover bi-infinite words with different boundary conventions or arbitrary leading zero prefixes. In the theorem, all gaps must be positive and the sequence must be nondecreasing and unbounded. The unbounded Lie-complexity construction is not claimed to be recurrent or morphic. This result does not calculate ordinary cyclic complexity (which counts partially appearing classes), factor complexity, or an optimal algorithmic indexing data structure. Completeness and originality relative to unindexed literature cannot be established by literature search alone; independent scientific review remains outstanding.

## References

1. J. P. Bell and J. Shallit, *Lie complexity of words*, arXiv:2102.03821v1 (7 February 2021), https://arxiv.org/pdf/2102.03821, especially Theorems 1.1 and 1.3 and Sections 5–8.
2. A. De Luca and G. Fici, *On the Lie complexity of Sturmian words*, arXiv:2206.00995 (first public 2 June 2022), https://arxiv.org/pdf/2206.00995, Sections 2–3.
3. S. Li, *A note on the Lie complexity and beyond*, arXiv:2207.05859v1 (12 July 2022), https://arxiv.org/pdf/2207.05859, Sections 1, 3–5.
4. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, https://arxiv.org/pdf/1402.5843, Sections 1–2.
