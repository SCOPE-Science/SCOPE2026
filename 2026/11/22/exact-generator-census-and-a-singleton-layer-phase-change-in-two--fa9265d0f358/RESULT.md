# Exact generator census and a singleton-layer phase change in two-level Heyting algebras

## Finding

Let \(P_{a,b}=A\oplus B\) be the ordinal sum of two nonempty antichains, with \(|A|=a\ge1\), \(|B|=b\ge1\), and all points of \(A\) below all points of \(B\). Let \(H_{a,b}=\operatorname{Up}(P_{a,b})\) carry the full bounded Heyting signature \((\wedge,\vee,\to,0,1)\). For an ordered tuple of \(k\ge0\) upsets, colour each point by the binary word recording membership in the generators.

**Generator criterion.** If \(b\ge2\), the tuple generates \(H_{a,b}\) exactly when its colours are pairwise different within \(A\) and within \(B\), respectively. If \(b=1\), the same within-layer requirement holds, and the unique upper colour must also differ from every lower colour.

Let \((x)_{\underline a}=x(x-1)\cdots(x-a+1)\) (including its zero value at nonnegative integers \(x<a\)), and let \(s(b,j)\) be the signed Stirling numbers of the first kind, determined by \((x)_{\underline b}=\sum_{j=0}^{b}s(b,j)x^j\). The exact count of **ordered** generating \(k\)-tuples is

\[
\boxed{G_{a,b}(k)=\sum_{c=0}^{k}\binom kc(2^c)_{\underline a}\sum_{j=1}^{b}s(b,j)(2^j-1)^{k-c},\quad b\ge2.}
\]

For a singleton upper level, the sharp boundary formula instead is
\[
\boxed{G_{a,1}(k)=\sum_{c=0}^{k}\binom kc(2^c-1)_{\underline a}.}
\]

The minimum number of generators is
\[
\boxed{d(H_{a,b})=\begin{cases}
\lceil\log_2(a+1)\rceil,&b=1,\\
\lceil\log_2 a\rceil+\lceil\log_2 b\rceil,&b\ge2.
\end{cases}}
\]

Here \(\lceil\log_2 1\rceil=0\). Thus the two-level generator rank is additive across the widths when the upper level has at least two points, while a single top point imposes a genuinely different cross-layer colour restriction.

## Assumptions and scope

The poset has \(a+b\) labelled points. Its upsets are exactly the subsets of \(B\) and the sets \(B\cup D\), for \(D\subseteq A\), with \(B\) counted once. Hence \(|H_{a,b}|=2^a+2^b-1\). Lattice operations are intersection and union; implication is \(X\to Y=\{p\in P_{a,b}:\uparrow p\cap X\subseteq Y\}\). We count ordered generator lists, allowing repetitions and the empty list. The reduct is the *Heyting* algebra, not the Boolean modal powerset algebra, nor an algebra expanded with additional modalities. No cross-layer comparabilities are absent.

## Proof

**1. Necessity of within-level colour injection.** Every permutation of \(A\) or of \(B\) is an order automorphism. If two points of the same level carry the same colour, their transposition fixes every given generator; therefore it fixes every term value. Since some upset separates any two distinct points, the tuple cannot generate the full algebra. Equivalently, the two points are propositionally indistinguishable in every generated Heyting expression.

When \(b=1\), let \(t\) be the unique point of \(B\). If a lower point \(x\in A\) has the same colour as \(t\), then all generators are identically true or false at \(x,t\). Induct on Heyting terms: intersections and unions preserve equality of truth values at \(x,t\). At \(t\), implication is classical (only \(t\) lies above it); at \(x\), the successors are \(x,t\), and both implication operands have identical truth values at those two points by induction. Thus their implications also agree at \(x,t\). No term distinguishes the two; full generation fails.

**2. A definable middle upset.** Suppose \(b\ge2\) and all upper colours are distinct. Some generator \(X\) has an upper restriction that is nonempty and proper in \(B\). Because every lower point lies below every upper point, such a generator contains no point of \(A\). Then \(\neg X=X\to0=B\setminus X\) and \(X\vee\neg X=B\). Thus the cut \(B\) belongs to the generated subalgebra.

When \(b=1\), suppose instead the upper colour is distinct from every lower colour. Each lower colour is a bitwise subword of the upper colour (all generators are upsets). The meet of all generators whose unique upper value is \(1\) is exactly \(B\): every lower point omits at least one such generator. This meet is nonempty-indexed, since otherwise no lower point could have a different colour. Hence the cut \(B\) is generated in this case as well.

**3. The cut separates two Boolean intervals.** Once \(B\) is generated, so are all upsets below it and all upsets above it, provided the colours within each level are injective. For the upper interval \([0,B]\), the sets \(X_i\wedge B\) separate all its atoms because the upper colours are distinct. Its relative complements are definable: for any upset \(Y\subseteq B\), \((Y\to0)\wedge B=B\setminus Y\). Boolean meets, joins and relative complements therefore generate every subset of \(B\).

For the lower interval \([B,1]\), the upsets \(X_i\vee B\) separate all its atoms (identified with points of \(A\)). The complement of \(B\cup D\) within this interval is \((B\cup D)\to B=B\cup(A\setminus D)\). Thus the Heyting operations generate all \(B\cup D\). These two intervals together constitute \(H_{a,b}\). This proves sufficiency and the entire generator criterion, including both boundary cases.

**4. Exact census for \(b\ge2\).** View the \(b\) upper colours as a \(b\)-by-\(k\) binary matrix. Fix exactly \(c\) all-one columns; choose their positions in \(\binom kc\) ways. Every lower colour has zero entries outside these columns and may otherwise use any of the \(2^c\) words. Pairwise distinct labelled lower colours therefore give \((2^c)_{\underline a}\) choices.

In the other \(k-c\) columns, select binary \(b\)-vectors other than the all-one vector, such that all \(b\) resulting upper rows are distinct. By Möbius inversion over partitions of the \(b\) labelled rows, their number is \(\sum_{j=1}^{b}s(b,j)(2^j-1)^{k-c}\): collapsing the rows into \(j\) equality classes yields exactly \(2^j-1\) allowed column patterns and the sum of partition-lattice Möbius values over partitions with \(j\) blocks is \(s(b,j)\). Multiplying and summing over \(c\) gives the displayed formula. All terms describe disjoint choices, so the count is exact.

**5. Singleton-upper count.** For \(b=1\), let the sole upper word have exactly \(c\) ones. Choose those coordinate positions in \(\binom kc\) ways. Each lower word is an arbitrary subword of those \(c\) ones, but must differ from the upper word. There are \(2^c-1\) eligible colours, hence \((2^c-1)_{\underline a}\) ordered injective assignments. Summation gives the singleton formula.

**6. Sharp rank.** For \(b\ge2\), the \(c\) all-one upper columns accommodate at most \(2^c\) distinct lower colours, requiring \(c\ge\lceil\log_2 a\rceil\). The remaining columns carry at most \(2^{k-c}\) different upper rows, requiring \(k-c\ge\lceil\log_2 b\rceil\). Conversely, use \(c=\lceil\log_2 a\rceil\) all-one upper columns with distinct lower binary words, plus \(d=\lceil\log_2 b\rceil\) columns coding distinct upper words, taking all lower values zero there. This is an admissible generating assignment and attains \(k=c+d\). For \(b=1\), a width-\(a\) injection into the \(2^k-1\) proper subwords of the upper word exists exactly when \(2^k-1\ge a\). Taking the upper word all ones attains this threshold. The rank formulas follow.

## Verification

The independent standard-library program `verification/check_twolevel.py` enumerates every upset, implements Heyting implication by directly inspecting every point's successors, closes each tested tuple under all basic operations, and compares actual generation with the colouring criterion and both Stirling enumerators. Its completed run reports `VERIFY_OK 4052` full-closure tuple checks, with additional independently enumerated colour-assignment comparisons. The exact computation is finite and corroborates; it is not the proof for arbitrary \(a,b,k\).

## Relationship to prior work

The general Esakia Colouring Theorem (Hyttinen, Martins, Moraschini and Quadrellaro, §3) characterizes generation via logical back-and-forth colour distinctions. That qualitative equivalence is prior art, not claimed here as new. The present result specializes this perspective to the two-level complete-incidence family and adds an explicit all-parameter signed-Stirling generator census and a sharp additive-versus-singleton rank boundary.

The 2026 poset generating-polynomial study by George and Yeats counts convex subsets using upsets and downsets under ordinal sums, not tuples of upsets that generate a Heyting algebra. A separate 2026 record on Frobenius-adjoint expansions studies additional operations on exactly \(H_{a,b}\), and its \(1+B_aB_b\) enumerator is **not** a generator-tuple count. A study of all subalgebras of the one-root star \(H_{1,b}\), and an exact generator census for direct powers of Heyting **chains**, cover related but different claims. Modal Boolean-algebra generation on ordinal sums similarly uses a different signature and unrestricted Boolean predicates. None of these inspected statements gives the two-level full Heyting-generator census or implies it without an additional calculation specific to allowable upper columns and lower-colour injections.

## Limitations

The scope is finite labelled complete two-level posets, with both levels nonempty and the pure bounded Heyting signature. The one-root star subcase \(a=1\) is especially close to previously classified Heyting subalgebras, and its novelty is not asserted independently. Nothing is claimed for incomplete bipartite incidence, higher-level posets, infinite Esakia spaces, or other signatures. The existing general colouring theorem implies a qualitative decision procedure, not historical originality of every special case; an earlier unindexed explicit count remains possible. No independent validation has been performed.

## References

1. Ian George and Rowan Yeats, *A Generating Polynomial for Convex Subsets of Posets*, arXiv:2610.23399v1, first public 2026-10-16, https://arxiv.org/abs/2610.23399 (poset enumeration and ordinal sums; abstract and bibliographic record inspected).
2. Tapani Hyttinen, Miguel Martins, Tommaso Moraschini and Davide E. Quadrellaro, *Strictly n-finite varieties of Heyting algebras*, §3 Colouring Theorem, Journal of Symbolic Logic, https://doi.org/10.1017/jsl.2024.48 (full article section inspected; first preprint 2023; general prior theorem).
3. *Frobenius-adjoint expansions of two-layer Heyting algebras: a Bell-product census*, published mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-frobenius-adjoint-expansions-of-two-layer-heyting-algebras-a-bel--f936050d4657 (RESULT.md inspected; same carrier, different operators).
4. *Homomorphism rigidity and Bell-graded subalgebras of top-extended Boolean Heyting algebras*, published mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-homomorphism-rigidity-and-bell-graded-subalgebras-of-top-extende--d7fbc564493b (RESULT.md inspected; singleton lower level subcase).
5. *Exact generating-tuple census and birthday law for finite Heyting-chain powers*, published mathematical research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-generating-tuple-census-and-birthday-law-for-finite-heytin--89cf3ed71236 (RESULT.md inspected; direct product of chains).
