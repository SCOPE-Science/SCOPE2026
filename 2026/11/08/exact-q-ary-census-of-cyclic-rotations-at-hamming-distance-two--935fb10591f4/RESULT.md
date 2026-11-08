# Exact q-ary census of cyclic rotations at Hamming distance two

## Finding
For every alphabet size \(q\ge3\), every word length \(n\ge2\), and every integer \(r\ge0\), the number of labeled \(q\)-ary words having exactly \(r\) nonzero cyclic shifts at Hamming distance two is explicitly determined by the divisor formulas below. In particular, apart from words with precisely two such shifts, every positive number of such shifts must be of the form \(n/g-1\) for a proper divisor \(g\mid n\).

Let \(C_{n,q}(r)\) be this count. For every proper divisor \(g\mid n\) put \(h=n/g\), and define
\[
N_g=\begin{cases}n(q-1)q^g,&h\ge3,\\ (n/2)(q-1)q^g,&h=2.\end{cases}
\qquad
E_g=\sum_{d\mid g}\mu(g/d)N_d.
\]
Let
\[
T=\frac{n(q-1)}{2}\sum_{\substack{h\mid n\\h\ge2}}\varphi(h)(h-1)q^{n/h},
\qquad
B=\frac12\left(T-\sum_{\substack{g\mid n\\g<n}}(n/g-1)E_g\right).
\]
Here \(\mu\) is the Möbius function, \(\varphi\) is Euler's totient function, and all displayed quantities are integers. Then
\[
C_{n,q}(r)=\mathbf1_{\{r=2\}}B+
\sum_{\substack{g\mid n,\ g<n\\n/g-1=r}}E_g\quad(r\ge1),
\qquad
C_{n,q}(0)=q^n-B-\sum_{\substack{g\mid n\\g<n}}E_g.
\]
For example, \(q=3,n=6\) yields the distribution \((C(0),C(1),C(2),C(5))=(441,126,126,36)\); all other counts vanish.

## Assumptions and scope
The alphabet consists of \(q\) distinct labeled symbols. For a word \(w=w_0\cdots w_{n-1}\), the shift at \(s\) is \((w_{i+s\bmod n})_{i=0}^{n-1}\) and \(d_H\) counts differing coordinates. Define \(R(w)=|\{s:1\le s<n,\ d_H(w,\operatorname{shift}_s(w))=2\}|\). The theorem counts ordinary labeled words, not rotation classes or primitive necklaces; periodic words are included. The parameter \(q\ge3\) is the novel claim's domain; the arithmetic formulas themselves also agree with the binary case, which has separately been studied.

## Proof
**1. The first moment of the shift count.** Fix a shift \(s\) with \(g=\gcd(n,s)\) and \(h=n/g\). The permutation \(i\mapsto i+s\bmod n\) consists of \(g\) cycles, each of length \(h\). For the Hamming distance to be exactly two, exactly one cycle has two unequal adjacent pairs and all other cycles have none. A cyclic sequence of length \(h\) with exactly two changes consists of two nonempty constant arcs of distinct letters. The marked cycle is chosen in \(g\) ways; the other cycles have \(q^{g-1}\) labels; on the marked cycle choose two distinct labels as an unordered pair and two transition edges, giving \(q(q-1)h(h-1)/2\) choices. Hence the number of words for this fixed shift is \(n(q-1)(h-1)q^g/2\). Exactly \(\varphi(h)\) shifts have order \(h\), which proves the displayed formula \(T=\sum_w R(w)\).

**2. Structural classification of possible shift sets.** The two-shift almost-commutation lemma of Gabrić (2021, Lemma 14), applied to a word and two distinct Hamming-two shifts that are not inverse, proves that the word is a one-position modification of a word with period \(g=\gcd(n,s,t)\). In that case every nonzero multiple of \(g\) is a Hamming-two shift. Reapplying this lemma to any additional shift shows that the full nonzero shift set is either a single inverse pair \(\{s,-s\}\) (a singleton if \(2s\equiv0\bmod n\)), or precisely the nonzero elements of a subgroup \(g\mathbb Z_n\). The latter conclusion also follows directly by repeatedly taking the gcd of the subgroup generator and any proposed extra shift; each enlargement strictly decreases the generator until no extra shift remains. Therefore the nonzero shift-set size for a subgroup of size \(h\) is \(h-1\), and an exceptional inverse pair outside that classification contributes two shifts.

**3. Counting subgroup containment.** Fix a proper divisor \(g\mid n\), and count the words whose Hamming-two shift set contains every nonzero multiple of \(g\). For \(h=n/g\ge3\), the same almost-commutation lemma (or the cycle comparison) shows that these are precisely one-coordinate modifications of \(g\)-periodic words. There are \(q^g\) choices for the periodic background, \(n\) for the changed coordinate, and \(q-1\) for its new symbol. No two different backgrounds can give the same word, since two distinct \(g\)-periodic backgrounds differ at at least \(h\ge3\) positions, whereas both would be within Hamming distance one of the modified word. Thus the count is \(N_g=n(q-1)q^g\). For \(h=2\), the two length-\(g\) halves must differ at exactly one coordinate, giving \(N_g=g(q-1)q^g\). Every subgroup-containing word has a unique maximal all-good subgroup \(d\mathbb Z_n\), with \(d\mid g\); let \(E_d\) count words whose full shift set is exactly that subgroup's nonzero elements. Then \(N_g=\sum_{d\mid g}E_d\), and divisor Möbius inversion gives the stated expression for \(E_g\).

**4. Remaining inverse pairs and the distribution.** Summing all shift counts over words, the subgroup classes contribute \(\sum_g(n/g-1)E_g\). The only remaining positive cases have exactly two shifts, contributing two each. Therefore their number is \(B=(T-\sum_g(n/g-1)E_g)/2\). Adding subgroup classes with the same shift count yields the formula for every positive \(r\); subtraction from \(q^n\) yields the zero case. This also proves integrality and nonnegativity of every derived count.

## Verification
The standalone \(\texttt{verify.py}\) uses only the Python standard library and exhaustively enumerates all words for \(q=3\), \(2\le n\le8\); \(q=4\), \(2\le n\le6\); and \(q=5\), \(2\le n\le5\). In 16 alphabet/length cases it reconstructs every Hamming-two cyclic-shift count directly and compares the full frequency distribution against the formulas, with no skipped words. The tests corroborate the formulas for these finite ranges; the infinite all-parameter statement rests on the proof and the cited almost-commutation lemma.

## Relationship to prior work
Gabrić's *Words that almost commute* (2021) proves the structural two-shift lemma used in Step 2 and enumerates several aggregate/unique near-rotation classes. The present claim enumerates all positive multiplicities and the zero class at once for labeled alphabets of size at least three. Makhynko's *Binary necklaces with minimum nontrivial rotational Hamming distance 2* (2026) analyzes the binary necklace problem and provides closely related subgroup structure and enumeration; its binary results are not asserted here as new. Shallit's *Hamming Distance for Conjugates* (2007) supplies earlier context on near-conjugates. Results for alphabets and count conventions must not be silently conflated.

## Limitations
The claim concerns Hamming distance exactly two and complete words, not distance at most two, higher Hamming radii, edit distance, or a closed count of rotation-equivalence classes. The key structural lemma is taken from the published proof rather than independently reproved here. The binary case is excluded from the original scope. Exhaustive tests cover only the stated finite ranges. An equivalent q-ary all-multiplicity formula in unindexed prior literature would supersede the claimed originality; independent literature assessment has not occurred.

## References
- D. Gabrić, *Words that almost commute*, 2021, arXiv:2110.01120, https://arxiv.org/abs/2110.01120 (especially Lemma 14, and Theorems 17–18).
- A. Makhynko, *Binary necklaces with minimum nontrivial rotational Hamming distance 2*, 2026, arXiv:2606.08991, https://arxiv.org/abs/2606.08991.
- J. Shallit, *Hamming Distance for Conjugates*, 2007, arXiv:0710.1234, https://arxiv.org/abs/0710.1234.
