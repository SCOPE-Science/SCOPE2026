# The exact five-occurrence language of the scattered pattern \(\mathtt{001100}\)

## Finding

For a binary word \(w\), let \(c_p(w)\) be the number of strictly increasing position tuples spelling a pattern \(p\), counting distinct embeddings even when their selected letters agree. Define \(L_5=\{w\in\{0,1\}^*:c_{\mathtt{001100}}(w)=5\}\). Then
\[
\boxed{L_5=\bigcup_{q\in\{\mathtt{1011},\mathtt{1101}\}}\{1^u0\,1^h0\,q\,0\,1^s0\,1^t:u,h,s,t\geq0\}.}
\]
Here \(q\) is one of the two *literal* four-letter blocks, and the four exponents independently count inert runs of ones. Equivalently, the unambiguous regular expression is

`1*01*0(1011|1101)01*01*`.

The only two shortest members are `00101100` and `00110100`, which are reversals of one another. For every integer \(n\geq0\),
\[
\boxed{B(n):=|L_5\cap\{0,1\}^n|=\begin{cases}0,&n<8,\\2\binom{n-5}{3},&n\geq8;\end{cases}\qquad \sum_{n\geq0}B(n)z^n=\frac{2z^8}{(1-z)^4}.}
\]
In particular, the eventual counting polynomial has **degree three**, strictly below the degree-four general bound for this pattern from fixed-frequency polynomiality.

## Assumptions and scope

Words are finite and linear over exactly \(\{0,1\}\); positions are strictly increasing and there is no cyclic wraparound. `001100` is a six-letter *scattered subsequence*, not a required contiguous factor. The occurrence frequency is exactly five. All four free exponents in the regular-expression representation are independently nonnegative. The statement is valid for all lengths including zero; the zero count for \(n<8\) is literal.

## Proof

**1. All displayed words have five embeddings.** An arbitrary displayed word has four distinguished zeros outside its four-letter middle block: the first two zeros and the last two zeros. The internal block contains one more zero and exactly three ones. Additional ones before the second distinguished zero cannot serve as either middle one, because fewer than two zeros precede them; additional ones after the penultimate distinguished zero cannot serve as either middle one, because fewer than two zeros follow them. Thus all embeddings use only the eight-symbol core. In core `00101100`, choosing the initial zero pair from the first two zeros gives three choices of a pair of subsequent ones; choosing either of the other two possible initial-zero pairs ending at the internal zero gives one further choice each, for \(3+1+1=5\). In core `00110100`, choosing the final zero pair from the last two zeros gives three choices of a preceding pair of ones; choosing either of the two other possible final-zero pairs beginning at the internal zero gives one further choice each. Therefore each core has five embeddings and all four free one-runs are inert.

**2. Finite-state proof that no other word has five embeddings.** For the successive nonempty prefixes \(p_1,\ldots,p_6\) of `001100`, keep counters \(d_j\) saturated at six, with \(d_0=1\) unsaturated. Initially all \(d_1,\ldots,d_6\) are zero. On reading a letter \(a\), update \(j=6,5,\ldots,1\): if the last symbol of \(p_j\) equals \(a\), replace
\[
d_j\longleftarrow\min(6,d_j+d_{j-1}),
\]
otherwise leave \(d_j\) unchanged. Because the update is in descending index order, the recurrence exactly counts embeddings ending anywhere in the read prefix. Saturation is sound: all terms are nonnegative, so a value at least six never falls below six. The condition \(d_6=5\) is therefore *equivalent* to exactly five embeddings for an arbitrary-length input.

Independently construct a Thompson nondeterministic automaton for the union of the two expressions `1*01*0101101*01*` and `1*01*0110101*01*`, or, equivalently, use the token lists in `CHECKER.py`. A `1*` token may consume any number of ones and advance by an epsilon move; literal tokens consume their indicated symbols. Epsilon-closed subsets determine a deterministic recognizer of the displayed regular language.

The finite product of the saturated occurrence-counter transition and this epsilon-subset recognizer has **exactly 126 reachable states** from the empty word. `CERTIFICATE.tsv` lists all 126 reachable product states and the successors on both input letters (252 transitions). `CHECKER.py` independently reconstructs both transition rules from their definitions, verifies every listed transition, verifies reachability of every listed state from the initial state, verifies successor closure, and checks at *every* listed state that the predicate \(d_6=5\) agrees with the regular-expression accepting predicate. Its recorded output is `CHECK_OUTPUT.txt`. These explicit finite checks prove equality for **all** words: by induction on input length each word reaches a listed state, and the accepting predicates agree there. The certificate is an exhaustive finite-state proof, not a finite-length experimental extrapolation.

**3. Unambiguous parametrization and count.** Starting at the left, the initial one-run, the first zero, the intervening one-run and the second zero are uniquely identified. The next four symbols distinguish `1011` from `1101`; the final zero and subsequent one-run, zero and terminal one-run are then uniquely parsed. Thus each word has one choice of the middle block and one four-tuple of free nonnegative exponents. At length \(n\ge8\), their sum is \(n-8\), giving \(\binom{n-5}{3}\) words per middle block by stars and bars. This yields the two formulas.

## Verification

Extract `CHECKER.py` and `CERTIFICATE.tsv` to the same directory and run `python3 CHECKER.py` (Python standard library only). The checker validates all 126 certificate rows, all 252 transitions, initial-state reachability, full closure and matching terminal predicates. It also independently evaluates the exact unsaturated subsequence counter on every binary word of lengths 6 through 16 and confirms the binomial formula. The exhaustive product-certificate argument, not the short-word checks, establishes the infinite-language claim.

## Relationship to prior work

Bruda, *Enumerating binary words restricted by subsequence frequency* (first submitted June 30, 2026), proves eventual polynomiality and the degree bound \(\ell-r+1\) for a length-\(\ell\) pattern with \(r\ge2\) runs, and explicitly asks for a complete criterion for equality. Here \(\ell=6\), \(r=3\), so the general upper bound is four; the exact degree is three. This case is not resolved by the cited sufficient tightness criteria: all runs have size two, and five is not a binomial coefficient \(\binom{2+s}{2}\) for an integer \(s\ge0\).

Menon and Singh's *Subsequence frequency in binary words* explicitly treats multiplicities zero through four, not the frequency five studied here. Tian's *Counting occurrences of a pattern in a binary word* supplies general occurrence and primitive-word constructions but not the displayed exact eight-symbol two-core classification. A previously indexed, more closely related classification treats five scattered copies of the **different, two-run pattern** `0011`: it has one six-symbol core, while `001100` has the two eight-symbol cores above. Its language formula does not imply this one: `00110100` has five copies of `001100` but only three copies of `0011`, whereas `001011` has five copies of `0011` and no copies of `001100`.

## Limitations

The theorem classifies a single natural three-run pattern at one positive frequency, not all fixed-frequency word languages. This is an exact specialization rather than an improvement of general enumeration complexity. The proof of completeness uses a fully specified finite-state certificate, with the transition soundness justified above; it is not a short purely hand-derived classification. Other explicit specializations in unindexed or unavailable literature remain a possible priority risk. Independent scientific audit has not been performed.

## References

- G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578v1, initially public June 30, 2026, https://arxiv.org/abs/2607.02578 (Theorem 1.4, Section 4.2).
- K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, initially public June 13, 2023, https://arxiv.org/abs/2306.07870 (Section 3).
- R. Tian, *Counting occurrences of a pattern in a binary word*, arXiv:2507.03205v1, initially public July 3, 2025, https://arxiv.org/html/2507.03205v1 (Sections 4 and 5).
- *Exact binary language with five scattered copies of \(0011\)*, indexed research result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-binary-language-with-five-scattered-copies-of-0011--e52ec49baf88 (RESULT.md, full claim and proof inspected).
