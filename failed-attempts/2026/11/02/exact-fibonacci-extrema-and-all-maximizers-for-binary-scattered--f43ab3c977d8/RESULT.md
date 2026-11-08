# Exact Fibonacci extrema and all maximizers for binary scattered palindromes

## Finding

Fix a binary alphabet \(\Sigma=\{0,1\}\). For \(w\in\Sigma^n\), let \(P(w)\) be the number of **distinct nonempty palindromic words occurring as scattered subsequences** of \(w\). Thus subsequences with the same letters at different selected positions are counted only once. Write \(M_n=\max_{w\in\Sigma^n}P(w)\), and let \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\) be the Fibonacci numbers.

**Theorem.** For every integer \(m\geq0\),

\[
M_{2m}=2F_{m+3}-4,\qquad M_{2m+1}=F_{m+5}-4.
\]

The maximizers are completely classified. For odd \(n\geq1\), exactly the two alternating words of length \(n\) attain \(M_n\). For even \(n=2m\geq2\), exactly four words attain \(M_n\): the two alternating words and \(vv^{\mathrm R}\) for the two choices of alternating \(v\in\Sigma^m\), where \(v^{\mathrm R}\) denotes reversal. At \(n=0\), only the empty word attains \(M_0=0\).

The first positive-length maxima are \(1,2,4,6,9,12,17,22,30,38,51,64,85\).

## Assumptions and scope

All words are finite, ordered, linear, and labeled over the fixed alphabet \(\{0,1\}\). A palindrome is a word equal to its reversal. A scattered subsequence is obtained by deleting zero or more positions without reordering the retained positions; its occurrences are deduplicated by the resulting symbol string. The empty subsequence is excluded from \(P(w)\). No restriction on how many times a particular symbol appears is imposed. This theorem does not address larger alphabets, palindromic contiguous factors, or embedding multiplicities.

For a nonempty word \(w\) and a symbol \(a\) appearing in \(w\), let \(f_a\) and \(\ell_a\) be its first and last positions, respectively, using zero-based indices. If \(f_a<\ell_a\), write \(I_a(w)=w[f_a+1:\ell_a]\) for the substring strictly between these occurrences; the slice notation includes its starting index and excludes its ending index. If \(f_a=\ell_a\), the symbol appears once.

## Proof

**1. Exact outer-letter decomposition.** Every nonempty palindromic scattered subsequence begins and ends in a unique symbol \(a\). If \(a\) occurs once, the only such palindrome is \(a\). If \(a\) occurs at least twice, the full collection is the singleton \(a\), the word \(aa\), and the words \(aua\), where \(u\) ranges over all nonempty scattered palindromic subsequences of \(I_a(w)\). The first and last appearances of \(a\) enclose every possible interior from any two appearances of \(a\), and those same extreme appearances realize every listed \(aua\). Distinct interiors yield distinct outer-wrapped words; different outer letters yield disjoint sets. Consequently the **exact identity** is

\[
P(w)=\sum_{a\in\operatorname{alph}(w)}\left(1+\mathbf 1_{\{f_a<\ell_a\}}\bigl(1+P(I_a(w))\bigr)\right).
\tag{1}
\]

In particular, \(P(\epsilon)=0\), where \(\epsilon\) is the empty word.

**2. Universal two-interval bound.** Assume \(n\geq4\) and both binary symbols appear at least twice. If the initial and final letters of \(w\) are the same, their interior interval has length \(n-2\), while the other symbol's interior has length at most \(n-4\). Since the maximum \(M_t\) is nondecreasing in \(t\) (append any symbol), equation (1) gives

\[
P(w)\leq4+M_{n-2}+M_{n-4}.\tag{2}
\]

If the initial and final letters differ, each symbol's extreme-occurrence interior has length at most \(n-3\), giving

\[
P(w)\leq4+2M_{n-3}.\tag{3}
\]

If \(w\) uses both symbols but exactly one is a singleton, equation (1) gives \(P(w)\leq3+M_{n-2}\), which is strictly below the claimed maximum for every \(n\geq4\). If \(w\) is constant, \(P(w)=n\), also strictly smaller for every \(n\geq4\). These strict inequalities follow directly from the explicit Fibonacci formulas, with \(n=4,5\) as their smallest cases.

**3. The Fibonacci upper bound.** Define candidate values \(U_{2m}=2F_{m+3}-4\) and \(U_{2m+1}=F_{m+5}-4\). Direct calculation gives \(U_0=0,U_1=1,U_2=2,U_3=4\). These candidate values strictly increase with \(n\), and Fibonacci addition yields, for all \(n\geq4\),

\[
4+U_{n-2}+U_{n-4}=U_n.\tag{4}
\]

Also \(4+2U_{n-3}=U_n\) whenever \(n\) is even; when \(n=2m+1\geq5\) is odd,

\[
U_n-(4+2U_{n-3})=F_{m-1}>0.\tag{5}
\]

Strong induction on \(n\), using the endpoint decomposition and all cases of step 2, proves \(P(w)\leq U_n\) for every binary word \(w\) of length \(n\).

**4. Attainment.** For an odd alternating word of length \(n\geq5\), its endpoint letters coincide, and the two intervals in (1) are alternating words of lengths \(n-2\) and \(n-4\). Thus \(P(w)=4+U_{n-2}+U_{n-4}=U_n\), by induction. For an even alternating word of length \(n\geq4\), the endpoints differ, and the two intervals are alternating words of length \(n-3\); hence \(P(w)=4+2U_{n-3}=U_n\). Finally, when \(n=2m\geq4\) and \(w=vv^{\mathrm R}\) with \(v\) alternating of length \(m\), the endpoints coincide and its two extreme-occurrence interiors are centrally doubled alternating palindromes of lengths \(n-2\) and \(n-4\) (the empty word is allowed when \(n=4\)). Therefore (1) and (4) imply \(P(w)=U_n\). The words of lengths \(0,1,2,3\) establish the bases. Hence \(M_n=U_n\) for all \(n\geq0\).

**5. Exhaustive equality classification.** For \(n\geq4\), an extremizer cannot be constant or use a singleton symbol, by the strict inequalities in step 2. In the same-endpoint case equality in (2) requires the other symbol's first and last appearances to be exactly at positions \(1\) and \(n-2\), and the length-\(n-2\) interior to be an extremizer. When \(n\) is odd, the interior has odd length, so induction forces it to alternate; surrounding it with the opposite endpoint symbol makes the full word alternating. When \(n\) is even, the interior has even length and equal endpoints, so by induction it is one of the two centrally doubled alternating palindromes; surrounding it with the other binary symbol yields precisely the centrally doubled forms of length \(n\).

For odd \(n\geq5\), the different-endpoint inequality (3) is strict by (5), so no further extremizers exist. For even \(n\geq4\), equality in (3) forces the symbol at position \(1\) to match the last letter and the symbol at position \(n-2\) to match the first; the length-\(n-3\) interior beginning at position \(1\) must attain \(M_{n-3}\). Since \(n-3\) is odd, induction forces that interior to alternate, and the endpoint constraints force the entire word to alternate. Both orientations occur. The base cases \(n=0,1,2,3\) show exactly the stated possibilities, completing the classification. \(\square\)

## Verification

A standalone Python program, `verify_pal_binary.py`, performs independent finite computations of the *counting algorithm*, not an independent assessment of this theorem. It checks the exact first/last-symbol recursion against a separately implemented interval dynamic program for every binary word of length at most \(16\), verifies literal sets of subsequences for every word of length at most \(9\), checks all maxima and all maximizer sets through length \(16\), tests \(4{,}000\) seeded larger cases, and confirms the explicit attaining constructions through length \(999\). Run with `python3 verify_pal_binary.py` (standard Python library only). Finite computation does not prove the theorem for arbitrary length; the preceding induction is the all-length argument.

## Relationship to prior work

Mahalingam and Pandoh's 2021 study introduced a systematic enumeration of distinct scattered palindromic subwords, proved a general Fibonacci upper bound, tabulated the binary maximum for lengths up to \(10\), and proved their exact alphabet-sensitive formula only when the number \(q\) of used symbols satisfies \(q\geq n/2\). Their Section 6 explicitly leaves the regime \(q<n/2\) for future work. Thus the small initial values are *previously known*, while the present result establishes an exact, all-length binary formula and classifies every binary extremizer, including the infinitely many lengths in the previously unproved regime. This does not resolve the full variable-alphabet conjecture. The full 2021 work, relevant sections of Holub and Saari's study of binary palindromic scattered subwords, and Müllner and Ryzhikov's paper about longest palindromic subsequences were compared at the level of theorem hypotheses and conclusions. Holub and Saari study determination up to reversal and longest-palindrome structure, not exact maximum distinct-pattern counts; Müllner and Ryzhikov study lengths of long palindromic subsequences, not the number of distinct such subsequences.

## Limitations

The theorem treats two symbols, *distinct* palindromic subsequence patterns, and linear words. It makes no claim about larger alphabets, the count of positional embeddings, circular words, contiguous palindromic factors, or all candidate values of the alphabet-size parameter in prior conjectures. Accessible source comparisons do not mathematically certify uniqueness in the entire literature; an unlocated equivalent formulation remains a residual originality risk. The proof has been checked in one review; no independent scientific audit has been performed.

## References

1. K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, first public version 5 August 2021, arXiv:2108.02729, https://arxiv.org/abs/2108.02729 . Especially Sections 4–6 and Table 4.
2. Š. Holub and K. Saari, *On Highly Palindromic Words* (2009), freely available author manuscript, https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf . Especially Sections 2, 4, and 5.
3. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, first public version 22 January 2019, arXiv:1901.07502, https://arxiv.org/abs/1901.07502 . Especially the introduction and longest-subsequence discussion.
