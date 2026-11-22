# Exact universal reconstruction lengths for Fibonacci-admissible binary words

## Finding
Let \(\mathcal P\) be the set of prime integers and \(2\mathcal P=\{2p:p\in\mathcal P\}\). For all \(n\ge1\), **every** binary word of length \(n\) avoiding the factor `11` is reconstructible up to reversal from the complete multiset of compositions of its nonempty contiguous factors **if and only if**
\[
 n+1\in\mathcal P\cup 2\mathcal P\cup\{8,9,12,16\}.
\]
Thus the adjacency constraint creates exactly three extra universally reconstructible lengths, \(n=8,11,15\), relative to unrestricted binary words. From length \(16\) onward, the universal-reconstruction length sets agree. For every excluded length an explicit pair of nonreversal, admissible, equicomposable source words is given below; the result does **not** assert unique reconstruction for every individual word at other lengths.

## Assumptions and scope
The source is the finite linear language
\[
 L_n=\{w\in\{0,1\}^n:\text{the adjacent factor `11' does not occur in }w\},\qquad n\ge1.
\]
For \(1\le \ell\le n\) and \(0\le j\le\ell\), put
\[
 c_{\ell,j}(w)=\#\{i:0\le i\le n-\ell,\ \sum_{h=i}^{i+\ell-1}w_h=j\}.
\]
The complete substring-composition observation \(C(w)\) consists of all these integers, retaining **multiplicity** and factor length. Equality of observations means componentwise equality of this triangular array. Write \(w^R\) for ordinary reversal. Universal reconstruction means that \(C(w)=C(v)\) for \(w,v\in L_n\) implies \(v\in\{w,w^R\}\). The alphabet is labeled and binary; the words are indexed and not necklaces. Reversal preserves the source constraint.

## Proof
**1. Unrestricted universal lengths.** Acharya–Das–Milenkovic–Orlitsky–Pan, *String Reconstruction from Substring Compositions* (arXiv:1403.2439v1, Sections 4 and 9), prove that every unrestricted binary length-\(n\) word is reconstructible up to reversal whenever \(n+1\) is prime, twice prime, or \(8\). Restricting the input language cannot destroy this property. These previously proved unrestricted cases are used here and are **not claimed as new**.

**2. Three genuinely additional constrained lengths.** The exhaustive algorithms in `verify_windows.py` and `verify_correlations.py` independently check exactly all \(11\)-avoiding words at \(n\in\{8,11,15\}\). They construct complete observation keys, partition the full finite input sets, and assert for every resulting fiber \(F\) that \(F=\{w,w^R\}\) for any \(w\in F\). Their agreed exact populations are:

| \(n\) | Admissible words | Fibers | Singleton fibers | Reversal-pair fibers |
|---:|---:|---:|---:|---:|
| 8 | 55 | 30 | 5 | 25 |
| 11 | 233 | 127 | 21 | 106 |
| 15 | 1597 | 826 | 55 | 771 |

The first algorithm directly counts all factor compositions in every length window; the second independently enumerates all \(2^n\) bit tuples, filters the source constraint, constructs the complete prefix-lattice autocorrelation, and checks that each fiber is a reversal orbit. In the second method, if the prefix paths are \(p_0,\ldots,p_n\in\mathbb N^2\) recording cumulative zeros and ones, their difference multiset \(\{p_j-p_i:0\le i,j\le n\}\) consists of the nonempty contiguous-factor compositions, their negatives, and \(n+1\) zeros. Therefore its equality is exactly equality of the observations. All loops use exact integers; no sampling or approximate hash-collision assumption is involved. The finite verifications prove these three cases exhaustively; they are not extrapolated to untested lengths.

**3. Arithmetic factor lemma.** If an integer \(m\ge2\) is neither prime nor twice a prime nor in \(\{8,9,12,16\}\), it has a factorization \(m=ab\) with \(a\ge5\) and \(b\ge3\). Indeed, unless \(m\) is prime or twice a prime or equals \(8\), elementary prime factorization gives a product of two integers each at least \(3\). If neither factor can be at least \(5\), both lie in \(\{3,4\}\), so \(m\in\{9,12,16\}\). This exhausts the alternatives.

**4. Constrained interleaving obstruction.** Take \(m=n+1=ab\) as in step 3, and set
\[
 s=01\,0^{a-3},\qquad t=1\,0^{b-2}.
\]
The notation \(0^h\) means a run of \(h\) zeros. The word \(s\) has length \(a-1\), starts and ends with zero, avoids `11`, and is nonpalindromic because \(a\ge5\) ensures at least two trailing zeros. The word \(t\) has length \(b-1\), begins with one, ends with zero, and is nonpalindromic. Define the classical interleaving
\[
 s\circ t=s\,t_1\,s\,t_2\,s\cdots t_{b-1}\,s.
\]
Both \(u=s\circ t\) and \(v=s\circ t^R\) have length \(b(a-1)+(b-1)=ab-1=n\). Every occurrence of a one in an inserted letter is flanked by ends of copies of \(s\), which are zeros, so both words avoid `11`. They are unequal because their first inserted letters differ; they are not reversals because both begin with \(s\), but \((s\circ t)^R\) begins with \(s^R\ne s\). Their own reversals are distinct for the same reason, so these two sources and their reversals form four different admissible words sharing one observation.

For completeness, the interleaving identity \(C(s\circ t)=C(s\circ t^R)\) has a direct counting proof. Substrings wholly contained in one copy of \(s\) contribute the same \(b\)-fold collection in both sources. Any remaining substring crosses a consecutive interval of \(j\ge1\) inserted letters: for fixed offsets of its first and last endpoints relative to the adjacent copies of \(s\) (allowing empty boundary pieces), its composition is the composition of a fixed suffix of \(s\), \(j-1\) full copies of \(s\), a fixed prefix of \(s\), and a consecutive \(j\)-letter factor of \(t\). For each \(j\), reversal permutes the full multiset of \(j\)-letter factor compositions of \(t\); thus every such endpoint category has the same observation multiset in both interleavings. Together with the within-copy substrings this accounts for every start/end pair exactly once. The identity also appears in the cited foundational paper (Section 4), but the boundary-safe choice of \(s,t\) is specific to the constrained language.

Consequently universal reconstruction fails for every remaining \(n\), completing the if-and-only-if proof.

## Verification
Run `python3 verify_windows.py`, `python3 verify_correlations.py`, and `python3 verify_construction.py` in the directory containing the supplied scripts. The first two programs independently and exhaustively verify the three exceptional lengths using two distinct exact signatures. The third checks the factor lemma and concrete construction for every \(2\le n+1<150\) and symbolically defined witness pattern over the tested range; the infinite proof is step 4 above, not this finite sanity test. Output summary:

```
WINDOW_OK 8 words 55 fibers 30 max_fiber 2
WINDOW_OK 11 words 233 fibers 127 max_fiber 2
WINDOW_OK 15 words 1597 fibers 826 max_fiber 2
CORRELATION_OK 8 words 55 fibers 30 size_hist {1: 5, 2: 25, 3: 0, 4: 0}
CORRELATION_OK 11 words 233 fibers 127 size_hist {1: 21, 2: 106, 3: 0, 4: 0}
CORRELATION_OK 15 words 1597 fibers 826 size_hist {1: 55, 2: 771, 3: 0, 4: 0}
CONSTRUCTION_OK 88 admissible non-reversal equicomposable witnesses for m<150
```

## Relationship to prior work
Acharya et al. establish the unrestricted prime/twice-prime/seven-letter uniqueness theorem and the general interleaving equality, but their unrestricted classification fails to characterize the constrained language: unrestricted words have nonreversal collisions at lengths \(8,11,15\), whereas those lengths are universally reconstructible here. A published complete binary composition census through length \(23\) enumerates unrestricted fibers at each length; filtering that **finite** census can establish the three finite exceptional cases, but not the constrained all-length classification without the constrained interleaving and arithmetic steps. A published length-fourteen binary census supplies unrestricted four-word fibers and is consistent with the present first constrained collision; it does not state the new all-length criterion. This theorem therefore claims the exact constrained phase diagram, not the classical interleaving lemma, the unrestricted prime classification, or the already-censused unrestricted fibers.

## Limitations
The exceptional-length checks are finite exhaustive computations with readable standalone source, not handwritten enumeration tables. They cover only the three special cases; all other lengths are handled by the unrestricted theorem or explicit construction. The result concerns complete noiseless substring compositions, not partial/noisy reads, unordered factor *sets* without multiplicities, or unique reconstruction of a particular word at nonuniversal lengths. No independent mathematical audit or exhaustive global historical-priority certificate is claimed. Although existing unrestricted censuses make the finite checks recoverable, the full constrained criterion and its priority should be compared with any unindexed specialist literature.

## References
1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439v1 (first public version dated 2014-03-10), https://arxiv.org/html/1403.2439v1 ; subsequently *SIAM Journal on Discrete Mathematics* 29(3), 1340–1371, https://doi.org/10.1137/140962486.
2. *Exact composition-multiset ambiguity spectrum for binary words of lengths \(1\)–\(23\)*, published research record, 2026, identifying archive entry `1ad4f8d99e9e` at https://github.com/published-finding corpus/2026 .
3. *Exact binary length-fourteen substring-composition ambiguity census*, published research record, 2026, identifying archive entry `0b1ad3b32456` at https://github.com/published-finding corpus/2026 .
