# Two-to-one cyclic-class lifting in generalized paperfolding words

## Finding

Let \(b=(b_0,b_1,\ldots)\in\{0,1\}^{\mathbb N}\) be an arbitrary instruction sequence and let \(\sigma b=(b_1,b_2,\ldots)\). Define the generalized paperfolding word \(P_b\) recursively, with indices starting at zero, by
\[
P_b(2j)=b_0\oplus(j\bmod2),\qquad P_b(2j+1)=P_{\sigma b}(j)\quad(j\ge0).
\]
Here \(\oplus\) denotes addition modulo two. This convention includes the regular paperfolding word and its bit complement when all instructions are constant.

For an infinite word \(x\), let \(\mathcal F_n(x)\) be its set of distinct length-\(n\) factors. Write \(u\sim v\) when \(v\) is a cyclic rotation of \(u\), and define the multiset of *restricted cyclic-class sizes*
\[
\mathcal S_x(n)=\bigl\{\!\bigl\{|\mathcal C\cap\mathcal F_n(x)|:\mathcal C\text{ is a rotation class},\ \mathcal C\cap\mathcal F_n(x)\ne\varnothing\bigr\}\!\bigr\}.
\]
The qualifier “restricted” matters: a rotation of an occurring factor need not itself occur.

**Theorem.** For every instruction sequence \(b\) and every integer \(n\ge8\) divisible by \(4\), there is a bijection between the nonempty restricted rotation classes of \(\mathcal F_n(P_{\sigma b})\) and those of \(\mathcal F_{2n}(P_b)\), under which each class cardinality is multiplied by exactly \(2\). Equivalently,
\[
\boxed{\mathcal S_{P_b}(2n)=2\mathcal S_{P_{\sigma b}}(n)},\qquad
\boxed{c_{P_b}(2n)=c_{P_{\sigma b}}(n)},
\]
where the scalar on a multiset multiplies every entry and \(c_x(n)=|\mathcal S_x(n)|\).

For constant instructions, \(P_{\sigma b}=P_b\), giving \(\mathcal S_{P_b}(2n)=2\mathcal S_{P_b}(n)\) and \(c_{P_b}(2n)=c_{P_b}(n)\) at every multiple of \(4\) at least \(8\). Thus the count is unchanged along every further dyadic scaling of such a length, while the individual class sizes increase by the scaling factor. The bound cannot simply be weakened to \(n=4\): the regular word has \(c(4)=3\) but \(c(8)=4\).

## Assumptions and scope

Factors are finite contiguous blocks of a one-sided infinite word; repeated occurrences are counted only once. Cyclic rotations use all possible cut positions in the length-\(n\) string, but only rotations that actually occur in the infinite word contribute to the restricted class size. The instruction sequence is arbitrary and infinite; no periodicity or eventual constancy is assumed. All arithmetic indices in the proof are nonnegative integers.

## Proof

**1. Alternating-marker lemma.** No generalized paperfolding word contains \(0101\) or \(1010\) as a factor. Indeed, within every length-four interval whose first index is even, the two symbols at even global indices are \(b_0\) and \(1-b_0\), hence differ, whereas an alternating four-letter block would have equal symbols two positions apart. For a length-four interval starting at an odd index, the two even global indices inside that interval again differ. The same reasoning applies to every shifted instruction sequence.

Let \(y=P_{\sigma b}\), and let \(u=y_k y_{k+1}\cdots y_{k+n-1}\) be a length-\(n\) factor, where \(4\mid n\) and \(n\ge8\). Among the two subsequences of \(u\) formed from even and odd *relative* positions, exactly one is alternating: the one comprising the even *global* indices of \(y\). Its length is \(n/2\ge4\). The other is a factor of \(P_{\sigma^2 b}\) of the same length and is not alternating by the preceding lemma. Therefore \(u\) identifies the parity of \(k\), and its first symbol on the alternating track, together with the fixed first instruction of \(y\), identifies \(k\bmod4\). In particular every occurrence of \(u\) has the same start residue modulo four.

Furthermore, if a cyclic rotation of \(u\) by \(t\) positions to the left is another factor \(v\) starting at \(\ell\), then
\[
\ell\equiv k+t\pmod4.
\]
To verify this, view the two tracks around the circle of length \(n\). Their lengths \(n/2\) are even, so the alternating track joins consistently across the cyclic cut. Its phase after rotation shifts by \(t\bmod4\); uniqueness of the alternating track forces precisely the displayed residue relation. This is the point where divisibility by four is needed.

**2. The canonical interleaved lift.** Define \(a_j=b_0\oplus(j\bmod2)\). For a factor \(u\) of \(y\) occurring at position \(k\), define the length-\(2n\) word
\[
E_k(u)=a_k u_0 a_{k+1}u_1\cdots a_{k+n-1}u_{n-1}.
\]
The defining recursion says that \(E_k(u)\) is exactly the factor of \(P_b\) beginning at position \(2k\). By the unique-residue property, the value of \(E_k(u)\) does not depend on the chosen occurrence of \(u\). If \(v\) is a left cyclic rotation of \(u\) by \(t\) positions and occurs at \(\ell\), then \(\ell\equiv k+t\pmod4\); since \(4\mid n\), the word \(E_\ell(v)\) is the left cyclic rotation of \(E_k(u)\) by \(2t\) positions. The lift therefore sends an entire restricted rotation class of \(y\) into one restricted rotation class of \(P_b\), independently of the representative.

**3. Distinct source classes do not merge.** The even-relative track of \(E_k(u)\) is alternating, whereas its odd-relative track is \(u\), which is not an alternating word. Consequently, a cyclic rotation carrying one even-start lift \(E_k(u)\) to another even-start lift \(E_\ell(v)\) must rotate by an even number of positions: an odd rotation would swap alternating and nonalternating tracks. Reading the odd-relative track after a rotation by \(2t\) shows that \(v\) must be the left cyclic rotation of \(u\) by \(t\). Thus no two distinct source rotation classes can have the same image class.

**4. Surjectivity and exact multiplicity.** Every factor of \(P_b\) of length \(2n\) starting at an even index is an \(E_k(u)\). If a factor starts at an odd index \(2k+1\), it is the one-position left cyclic rotation of the preceding even-start factor, because the first symbol of the preceding factor equals the symbol at position \(2k+2n\): both are \(a_k\), as \(n\) is even. Hence every target rotation class is obtained by lifting a source class.

If the source class contains exactly \(r\) distinct occurring factors, its lifts give \(r\) distinct even-start target factors. Their one-position rotations give \(r\) distinct odd-start factors. These two sets are disjoint by the alternating-track parity distinction. Every target factor is in one of these sets, and Step 3 excludes contributions from any other source class. Hence the target class contains exactly \(2r\) factors. This proves the theorem.

## Verification

The standalone Python 3 program `verify.py` computes paperfolding prefixes independently by an explicit 2-adic formula and by the defining recursive decimation, and asserts equality on their common range. It checks the lift word-by-word, the induced map on actual rotation classes, injectivity, surjectivity and the exact class-size multiplier for 18 instruction sequences and 12 admissible source lengths, giving 216 length-pair tests. The results include \(c(8)=4\), \(c(12)=16\), \(c(16)=4\), \(c(20)=28\), and the failure of stabilization from length \(4\) to \(8\) in the regular case.

Each finite factor set used in the tests reaches the published total \(4n\) for its length \(n\ge7\), making those particular enumerations exhaustive for the chosen infinite words by Allouche's factor-complexity theorem. Finite checks do not prove the universal instruction-sequence theorem; that conclusion follows from Steps 1–4.

## Relationship to prior work

Cassaigne, Fici, Sciortino and Zamboni introduced cyclic complexity and proved that for every paperfolding word the cyclic classes at lengths \(4\cdot2^{j+1}\) are full rotation orbits (their Proposition 20). This establishes the special four-class phenomenon along one dyadic ray, but does not state a bijection of restricted rotation classes or class-size inflation at arbitrary lengths divisible by four. For example, the length-\(12\) spectrum has sixteen classes of unequal sizes; the present theorem transfers this entire spectrum to length \(24\) and beyond in the regular word. Allouche established the universal linear factor-complexity count, but that total does not determine the rotation-class partition. Other work studies canonical *occurrence positions*, which is a different invariant and may contain further relevant information.

## Limitations

The transfer is from a paperfolding word to the shifted-instruction word; it yields same-word stabilization only when the instruction tail reproduces the original word, including constant instructions. No analogous assertion is made for source lengths not divisible by four, higher-alphabet substitutions or arbitrary Toeplitz words. The theorem does not alone supply a closed formula for the base cyclic complexity at every odd component. Full historical-priority verification, in particular against material beyond the available abstract of the 1994 canonical-position paper, remains open. No independent mathematical audit is claimed.

## References

- J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, first arXiv posting February 24, 2014, https://arxiv.org/abs/1402.5843; published in *Journal of Combinatorial Theory, Series A* 145 (2017), 36–56, https://doi.org/10.1016/j.jcta.2016.07.002, especially Section 5.2, Lemma 19 and Proposition 20.
- J.-P. Allouche, *The Number of Factors in a Paperfolding Sequence*, *Bulletin of the Australian Mathematical Society* 46 (1992), 23–32, https://doi.org/10.1017/S0004972700011655.
- J.-P. Allouche and M. Bousquet-Mélou, *Canonical Positions for the Factors in Paperfolding Sequences*, *Theoretical Computer Science* 129 (1994), 263–278, https://doi.org/10.1016/0304-3975(94)90028-0.
- C. Krawchuk and N. Rampersad, *Cyclic Complexity of Some Infinite Words and Generalizations*, *Integers* 18A (2018), A12, https://math.colgate.edu/~integers/sjs12/sjs12.pdf.
