# Exact state complexity of binary two-run conjugacy languages

## Finding

Let \(a,b\ge 1\) be integers, let \(n=a+b\), and let \(C(0^a1^b)\) be the set of all cyclic shifts of the length-\(n\) binary word \(0^a1^b\). The minimal **complete deterministic finite automaton** recognizing exactly this finite language has

\[
\boxed{\operatorname{sc}(C(0^a1^b))=2ab+3}
\]

states. More precisely, for every \(j\) with \(1\le j<n\), the number of distinct nonempty left quotients by length-\(j\) prefixes is

\[
\boxed{\lambda_j=2\min\{j,a,b,n-j\}.}
\]

There is one nonempty quotient at prefix length zero, one accepting quotient at length \(n\), and one empty dead quotient. At fixed length \(n\ge2\), the state-complexity range within this complete two-run family is

\[
2n+1\ \le\ \operatorname{sc}(C(0^a1^{n-a}))\ \le\ 2\lfloor n^2/4\rfloor+3,
\]

with the minimum at \(a=1\) or \(b=1\) and the maximum at balanced run lengths.

## Assumptions and scope

The input alphabet is \(\{0,1\}\). Runs have positive integral lengths; the cyclic word has exactly one run of each symbol, and cyclic shifts are words of full length \(n\), not shorter factors or an infinite periodic language. A complete DFA has a transition for each input symbol from every state, including a rejecting sink. State complexity counts this sink. Left quotients are sets of possible completing suffixes. No assertion is made for words with three or more cyclic runs, multiple symbols, or other language operations.

## Proof

**Step 1: distinct rotations and quotient levels.** The word \(0^a1^b\) has exactly one cyclic transition of each type \(01\) and \(10\). A nontrivial rotational period would replicate either transition, so its \(n\) rotations are distinct. For any valid prefix \(p\) of length \(j\), define its nonempty right-residual language

\[
R_j(p)=\{s\in\{0,1\}^{n-j}:ps\in C(0^a1^b)\}.
\]

By the Myhill–Nerode theorem, different residual languages at the same level correspond to different states. Since the language has fixed word length \(n\), nonempty residuals at different levels cannot coincide. There is also one accepting residual \(\{\varepsilon\}\) and the empty dead residual.

**Step 2: count quotient collisions.** For \(1\le j<n\), let \(t=n-j\), and put

\[
A=(a-j+1)_+,\quad B=(b-j+1)_+,
\]

where \(x_+=\max(x,0)\). Exactly \(A\) rotations begin with \(0^j\), and exactly \(B\) begin with \(1^j\). Each extant homogeneous prefix generates one residual language; two such homogeneous prefixes have different residuals (their completing suffixes necessarily have different symbol counts). Every other rotation has a *mixed* length-\(j\) prefix. Such a prefix contains one of the two unique cyclic letter transitions and therefore occurs at a unique rotation; its residual is a singleton.

Two singleton residuals of mixed prefixes can coincide only if their length-\(t\) suffix is homogeneous: a mixed suffix also contains a unique oriented cyclic transition and hence occurs at only one rotation. Among the mixed-prefix rotations, the multiplicities of the homogeneous suffixes are exactly

\[
U=(a-t+1)_+-\mathbf 1_{\{j=b\}},\qquad
V=(b-t+1)_+-\mathbf 1_{\{j=a\}}.
\]

The subtractions remove the unique rotations with a homogeneous prefix of the other letter when the split is exactly at the run boundary. These nonnegative counts are exhaustive, and no singleton residual from a mixed prefix coincides with a homogeneous-prefix residual: the latter either has more than one completion, or has its unique completion at a boundary phase not shared by any mixed-prefix rotation. Consequently the precise number of nonempty residuals at level \(j\) is

\[
\lambda_j=n-A-B-(U-1)_+-(V-1)_+
 +\mathbf 1_{\{A>0\}}+\mathbf 1_{\{B>0\}}.\tag{1}
\]

**Step 3: simplify all boundary regimes.** Interchange zero and one if necessary so that \(a\le b\); this preserves the language's state complexity and merely swaps run roles. Equation (1) reduces to the following *complete* table:

| Length of prefix | \(A\) | \(B\) | \(U\) | \(V\) | Number of residual classes |
|---|---:|---:|---:|---:|---:|
| \(1\le j\le a\) | \(a-j+1\) | \(b-j+1\) | \(0\) | \(0\) | \(2j\) |
| \(a<j\le b\) | \(0\) | \(b-j+1\) | \(0\) | \(j-a+1\) | \(2a\) |
| \(b<j<n\) | \(0\) | \(0\) | \(a-t+1\) | \(b-t+1\) | \(2t\) |

The table includes \(a=b\), for which the middle row is empty. Thus \(\lambda_j=2\min\{j,a,b,n-j\}\) in every case.

**Step 4: sum and optimize.** Summing the three rows gives

\[
\sum_{j=1}^{n-1}\lambda_j
=a(a+1)+2a(b-a)+a(a-1)=2ab.
\]

Including the initial quotient, final accepting quotient and dead quotient gives \(2ab+3\) states. With fixed \(a+b=n\), the product \(ab\) is minimized at an endpoint and maximized for balanced integers, yielding the displayed extrema. This proves all claims.

## Verification

The companion `verify.py` performs independent enumeration of every cyclic rotation, constructs its exact left quotients, and separately minimizes a prefix trie bottom-up. It also independently computes the homogeneous-prefix/suffix count of equation (1). Both enumeration algorithms are checked against every predicted level and the total for all \(1\le a,b\le22\); 150 further seeded instances use \(1\le a,b\le100\). Running `python3 verify.py` yielded `VERIFY_OK` on 634 parameter instances. These are finite cross-checks; the all-parameter conclusion rests on the preceding proof, not the tests.

## Relationship to prior work

Gabric, Holub, and Shallit (2019), *Maximal State Complexity and Generalized de Bruijn Words*, study the language of conjugates of a single finite word and establish the exact **maximum** deterministic state complexity over all length-\(n\) words, characterizing maximal generalized de Bruijn words. In their Section 3, Theorems 6 and 7 and Tables 2–3 concern this extremal problem, rather than an explicit two-run parameter formula or the full quotient-layer profile. In the smallest cases some balanced two-run words attain their global maximum, but that bound alone does not determine the stated formula for arbitrary run lengths. Earlier work of Jirásková and Okhotin (2008) addresses cyclic shift as a regular-language operation and its general worst-case blow-up. The present calculation treats the nontrivial two-run conjugacy subclass exactly, including every residual layer and balanced-run extremality within that subclass.

## Limitations

The theorem applies only to binary circular words with exactly two runs. It does not give an efficient general-purpose state-complexity formula for arbitrary necklaces. Finite tests cannot replace the infinite proof. The cited literature was searched for equivalent statements, but an unindexed or differently formulated prior exact two-run result remains possible; no independent scientific assessment has been performed.

## References

1. D. Gabric, Š. Holub, J. Shallit, *Maximal State Complexity and Generalized de Bruijn Words*, first public preprint 2019-03-13, https://arxiv.org/abs/1903.05442 . Especially Section 3, Theorems 6–7.
2. G. Jirásková, A. Okhotin, *State complexity of cyclic shift*, RAIRO Theoretical Informatics and Applications 42 (2008), 335–360, https://doi.org/10.1051/ita:2007038 .
3. J. Jirásek, G. Jirásková, *Cyclic Shift on Prefix-Free Languages*, CSR 2013, https://doi.org/10.1007/978-3-642-38536-0_22 .
