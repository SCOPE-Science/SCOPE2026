# A sharp three-quarter antipalindromic subsequence law for four-run circular binary words

## Finding

Write \(W=[0^a1^b0^c1^d]\) for a circular binary word, where \(a,b,c,d\) are arbitrary positive integers and brackets identify words up to cyclic rotation. Let \(\Lambda(W)\) denote the maximum length of an antipalindromic scattered subsequence of **one** linear representative of \(W\), optimized over all circular cuts. An antipalindrome \(x=x_1\cdots x_\ell\) satisfies \(x_i=1-x_{\ell+1-i}\) for every index; in particular, \(\ell\) is even.

**Exact four-run law.** For every \(a,b,c,d\ge1\),
\[
\begin{aligned}
\Lambda([0^a1^b0^c1^d])=2\max\{&\min(a,b+d),\ \min(c,b+d),\\
&\min(b,a+c),\ \min(d,a+c),\\
&\min(a,d)+\min(b,c),\\
&\min(a,b)+\min(c,d)\}.
\end{aligned}
\]

**Sharp balanced bound.** If \(a+c=b+d=N\), where \(N\ge2\), define \(u=|a-b|\) and \(v=|a+b-N|\). Then
\[
\Lambda(W)=2\max\left\{\frac{N+u+v}{2},\ N-u,\ N-v\right\},
\]
and the exact minimum over all positive balanced four-run profiles is
\[
\min_{\substack{a,c,b,d\ge1\\a+c=b+d=N}}\Lambda([0^a1^b0^c1^d])
=2\left(N-\left\lfloor\frac N4\right\rfloor\right).
\]
Thus every such circular word contains an antipalindromic subsequence of length at least \(3/4\) of its total length, with equality whenever \(N\) is divisible by \(4\). For \(N=4h\), equality occurs precisely at the four ordered pairs
\[
(a,b)\in\{(h,2h),(2h,h),(2h,3h),(3h,2h)\},
\]
with \(c=N-a\) and \(d=N-b\). These pairs represent one circular profile up to rotation and exchange of the two symbols.

## Assumptions and scope

All four run lengths are strictly positive. The circular word has exactly four monochromatic runs. A circular subsequence means a subsequence of one chosen full-length rotation, not a subsequence allowed to traverse the circle more than once. Deletions preserve source order but may merge two separated monochromatic source runs. No equal-frequency assumption is needed for the exact general law; the equal-frequency restriction is used only for the sharp three-quarter statement.

## Proof

**1. Structural reduction.** Every antipalindrome has an even number of nonempty constant-symbol runs: the map reversing its run sequence and complementing every symbol pairs the first run with the last, the second with the penultimate, and so on; a middle run fixed by that map would have to be its own binary complement. A rotation of a circular four-run word has at most five runs (five only when the cut splits one source run). Deleting letters cannot increase the number of runs. Consequently any nonempty antipalindromic subsequence has exactly two or four runs.

**2. Two-run candidates.** A two-run antipalindrome must be \(0^t1^t\) or \(1^t0^t\) with \(t\ge1\). When its first monochromatic block draws from both circular source runs carrying its symbol, the other block can draw from only one opposite-symbol source run; when its second block draws from both opposite-symbol runs, the first can draw from only one source run. In a single traversal of four alternating circular runs it is impossible for both output blocks to combine both of their respective source runs. Therefore
\[
 t\le\max\{\min(a,b+d),\min(c,b+d),\min(b,a+c),\min(d,a+c)\}.
\]
Each of these four bounds is attained by an explicit two-run output: start with the indicated single run, skip the intervening opposite-symbol run if necessary, and then take equal numbers of letters from the two available later runs, or start with both accessible initial runs and end with the indicated single opposite run. A circular cut immediately before the first used run realizes each construction. The maximum two-run length is therefore twice the displayed quantity.

**3. Four-run candidates.** A four-run antipalindrome has the form \(0^s1^t0^t1^s\) or \(1^s0^t1^t0^s\), with \(s,t\ge1\). Such an output needs four alternating source runs. If the circular cut splits a source run and produces five runs, four alternating output blocks must be drawn from four consecutive source runs: any nonconsecutive selection forces two selected source blocks to have the same symbol and merge, leaving fewer than four output runs. Splitting an endpoint source run never increases its available length. Hence the two possible cyclic alignments give, and cannot improve upon, the upper bounds
\[
 2\bigl(\min(a,d)+\min(b,c)\bigr),\qquad
 2\bigl(\min(a,b)+\min(c,d)\bigr).
\]
They are both attained by cutting immediately before the first of the relevant four original runs and retaining \(s\) letters from the two outer source runs and \(t\) from the two inner source runs. Together with Step 2 this proves the six-term formula, with no restrictions on the positive run lengths.

**4. Balanced simplification.** Set \(a+c=b+d=N\). The four two-run half-length candidates reduce to \(a,c,b,d\), whose maximum is
\[
\max\{a,N-a,b,N-b\}
=\frac{N+|a-b|+|a+b-N|}{2}.
\]
The two four-run half-length candidates reduce respectively to \(N-|a+b-N|\) and \(N-|a-b|\). These are the claimed three terms.

**5. Sharpness and extremizers.** Put \(u=|a-b|\), \(v=|a+b-N|\). If the maximum of \((N+u+v)/2\), \(N-u\), and \(N-v\) were strictly less than \(3N/4\), the last two inequalities would force \(u>N/4\) and \(v>N/4\), while the first would force \(u+v<N/2\), a contradiction. As the maximum is an integer, it is at least \(\lceil3N/4\rceil=N-\lfloor N/4\rfloor\).

For \(N\ge4\), take \(a=\lfloor N/4\rfloor\), \(b=\lfloor N/2\rfloor\), \(c=N-a\), \(d=N-b\). Direct substitution shows that the maximum is exactly \(N-\lfloor N/4\rfloor\): the largest run has this length and both four-run half-length terms are no larger. For \(N=2,3\), the same formula gives \(N\), achieved by every positive balanced four-run profile. If \(N=4h\), equality forces \(u\ge h\), \(v\ge h\) and \(u+v\le2h\), hence \(u=v=h\). Solving \(|a-b|=|a+b-4h|=h\) gives exactly the four displayed ordered pairs. This proves all statements.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. Its separately implemented interval dynamic program checks all \(5^4=625\) positive four-run parameter quadruples with each run at most \(5\); for each it explicitly optimizes over all rotations. It also checks the balanced closed form on \(328350\) ordered parameter pairs with \(2\le N\le100\), exact minimum values for every such \(N\), and all equality profiles at \(N=4h\) for \(1\le h\le79\). These finite tests corroborate, but do not replace, the unbounded structural proof above.

## Relationship to prior work

Müllner and Ryzhikov (2019, arXiv:1901.07502), Sections 1–4, study palindromic and antipalindromic subsequences of circular words. Their introduction recalls the Lyngsø–Pedersen conjecture that every balanced binary circular word of length divisible by six has an antipalindromic subsequence of at least two-thirds of its length, and reports a weaker general lower bound. The exact four-run law and its sharp three-quarter bound are not stated by the inspected results. The present restricted-family theorem does not prove the unrestricted conjecture.

General cyclic longest-common-subsequence algorithms, including Chowdhury et al. (2009), and the circular-sequence comparison algorithms of Wang (2023) concern computing common subsequences for supplied sequences, not an explicit four-run antipalindromic formula with a sharp balanced extremal census. Their generic computational capabilities do not supply the structural argument in Steps 1–5. The complementary-reversal formulation is equivalent to the binary antipalindrome definition used here, not a separate theorem.

## Limitations

Only circular words with exactly four positive runs are classified. The result does not establish any improved bound for general balanced circular binary words, whose number of runs may be arbitrarily large. It concerns maximum **length**, not the number of optimal subsequences or their embeddings. An equivalent result in literature not located by the recorded searches remains a possible originality risk. No independent scientific audit is claimed.

## References

1. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502, first public version 2019-01-22, https://arxiv.org/abs/1901.07502 ; LATA 2019, DOI:10.1007/978-3-030-13435-8_34.
2. S. R. Chowdhury, M. Hasan, S. Iqbal and M. S. Rahman, *An \(O(n^2)\) Algorithm for Computing Longest Common Cyclic Subsequence*, arXiv:0911.5031, 2009, https://arxiv.org/abs/0911.5031.
3. Y. Wang, *Algorithms for the uniqueness of the longest common subsequence*, arXiv:2301.03827, first public version 2023-01-10, https://arxiv.org/abs/2301.03827.
