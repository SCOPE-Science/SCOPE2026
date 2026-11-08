# Five-symbol binary permutation bursts: exact worst-case volume and all maximizer counts

## Finding

For each integer \(n\ge5\), let \(P_5(x)\) be the set of distinct length-\(n\) binary words obtainable from \(x\in\{0,1\}^n\) by arbitrarily permuting the symbols in exactly one contiguous five-position window (the identity is permitted). Put \(M_n=\max_x|P_5(x)|\), and let \(A_n=|\{x:|P_5(x)|=M_n\}|\). Then

\[
M_n=16\left\lfloor\frac n3\right\rfloor+
\begin{cases}
-16,&n\equiv0\pmod3,\\
-10,&n\equiv1\pmod3,\\
-6,&n\equiv2\pmod3.
\end{cases}
\]

The exact number of labeled maximizing binary words is

\[
A_5=20,\quad A_6=8,\quad A_8=14,\qquad
A_n=\begin{cases}4,&n\equiv0\pmod3,\\2,&n\equiv1\pmod3,\\10,&n\equiv2\pmod3,\end{cases}
\quad\text{for all }n\ge9,
\]
with \(A_7=2\). In particular, increasing length by three eventually adds exactly sixteen possible outputs, while the extremizer counts are eventually periodic. The periodic word whose repeating block is `001110` supplies a maximizing prefix for every \(n\ge5\); at \(n=5\), all weight-two and weight-three words are maximizing, and its complement supplies another maximizing word whenever \(n\ge6\).

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\), source length satisfies \(n\ge5\), and the channel makes exactly one choice of a contiguous window of five positions, then applies any permutation within that window. Outcomes are **distinct words**, not indexed error histories. The identity operation is included. Maximizers are counted as distinct, position-labeled binary words, without quotienting by reversal or complementation.

## Proof

**1. A local formula.** For any binary segment \(v=v_1\cdots v_\ell\), \(2\le\ell\le5\), write \(a=v_1+v_\ell\), \(r=\sum_{j=2}^{\ell-1}v_j\), and define

\[
g(v)=\binom{\ell-2}{r+2a-2},\qquad
\binom mr=0\text{ if }r\notin\{0,\dots,m\}.
\]

Every nonidentity output \(y\in P_5(x)\) has a unique first changed index \(i\) and last changed index \(j\). The interval length \(\ell=j-i+1\) belongs to \(\{2,3,4,5\}\). Its number of ones is preserved: the surrounding symbols in any permuted window are unchanged. Conversely, any changed interval of length at most five with preserved weight can be covered by a five-position window, so its replacement is a permitted output. Both end bits must be flipped. The original endpoints contain \(a\) ones and the new endpoints contain \(2-a\); hence the new interior must have \(r+2a-2\) ones. There are exactly \(g(x_i\cdots x_j)\) such outputs. Distinct changed intervals give disjoint output families. Therefore

\[
|P_5(x)|=1+\sum_{\ell=2}^{5}\sum_{i=1}^{n-\ell+1}g(x_i\cdots x_{i+\ell-1}).\tag{1}
\]

**2. A finite-state maximization with exact tie counting.** Define the right side of (1) as the auxiliary potential \(H_m(x)\) for every \(m\ge4\), omitting terms with \(\ell>m\). For \(m\ge5\), \(H_m(x)=|P_5(x)|\). The state \(s\in\{0,1\}^{4}\) records the last four symbols. For each \(m\ge4\), let \(V_m(s)=(h_m(s),c_m(s))\), where \(h_m(s)\) is the largest potential among words of length \(m\) ending in \(s\), and \(c_m(s)\) is the number attaining that statewise largest potential. Initialize

\[
V_4(s)=(H_4(s),1).
\]

Appending \(b\in\{0,1\}\) to state \(s\) gives state \(t\), the final four bits of the five-bit word \(sb\), and adds the integer

\[
w(s,b)=\sum_{\ell=2}^{5}g(\text{last }\ell\text{ bits of }sb).
\]

Consequently, \(h_{m+1}(t)\) is the maximum of \(h_m(s)+w(s,b)\) over the at most two predecessor transitions into \(t\); \(c_{m+1}(t)\) is the **sum** of the corresponding predecessor counts for precisely those transitions achieving the maximum. This is an exact recurrence for all words of all lengths, not a sampling or asymptotic approximation.

**3. Finite arithmetic certificate for the infinite claim.** Directly iterating that fully specified sixteen-state recurrence gives the following statewise pairs \(V_{16}\) (strings are terminal four-bit states, and pairs mean score and number of statewise winners):

| State | Pair | State | Pair |
|---|---|---|---|
| `0000` | \((63,2)\) | `1000` | \((68,1)\) |
| `0001` | \((68,2)\) | `1001` | \((68,1)\) |
| `0010` | \((66,3)\) | `1010` | \((68,1)\) |
| `0011` | \((70,1)\) | `1011` | \((66,1)\) |
| `0100` | \((66,1)\) | `1100` | \((70,1)\) |
| `0101` | \((68,1)\) | `1101` | \((66,3)\) |
| `0110` | \((68,1)\) | `1110` | \((68,2)\) |
| `0111` | \((68,1)\) | `1111` | \((63,2)\) |

Three further transitions yield, *for each of these sixteen states simultaneously*,

\[
V_{19}(s)=(h_{16}(s)+16,\;c_{16}(s)).\tag{2}
\]

Equation (2) is a finite statement over sixteen states, not a claim extrapolated from samples. It follows directly from the transition formula, with a complete standalone integer-arithmetic checker in `check.py`. Because a uniform shift of all state scores leaves the set of maximizing predecessor transitions unchanged, the recurrence propagates (2) inductively to

\[
V_{m+3}(s)=(h_m(s)+16,c_m(s))\qquad(m\ge16,\ s\in\{0,1\}^{4}).\tag{3}
\]

Taking the largest statewise score and adding counts at globally maximizing states proves that both the global maximum and its maximizing-word count obey the same three-step recurrence for every length beyond the finite base range.

**4. Initial values and conclusion.** Applying the same recurrence for the fourteen lengths \(5\le m\le18\) yields the following complete base table:

| \(m\) | \(M_m\) | \(A_m\) | \(m\) | \(M_m\) | \(A_m\) |
|---:|---:|---:|---:|---:|---:|
|5|10|20|12|48|4|
|6|16|8|13|54|2|
|7|22|2|14|58|10|
|8|26|14|15|64|4|
|9|32|4|16|70|2|
|10|38|2|17|74|10|
|11|42|10|18|80|4|

The displayed formulas are exactly those initial values extended by (3). This completes the proof for every \(n\ge5\).

## Verification

Run `python3 check.py` using Python 3 standard libraries only. The checker independently evaluates (i) the direct channel output set by enumerating window contents, (ii) the changed-interval formula (1), and (iii) the published first-changed-position formula for all \(8{,}160\) input words of lengths five through twelve. It then reproduces every statewise value in the table at length sixteen, verifies the full sixteen-state shift identity (2), verifies the finite base table, and checks the resulting formulas up to length forty-five. The **infinite** conclusion comes from the recurrence plus the exact state-vector identity (2), not from those finitely many length checks.

## Relationship to prior work

Chen and Milenkovic (2026, arXiv:2610.15701v1), Section II, define the same channel and establish an exact local formula for the sphere size of any **specified** binary input; their analysis obtains the random-source average and asymptotic code redundancy bounds. We do not claim their per-word formula or expectation as new. The local changed-interval formula here is an alternative derivation serving as an exact optimization input. A previously known all-alphabet per-word volume identity similarly does not by itself determine the global optimizer or its number. Earlier exact four-window binary extremal results concern a different window length and have a linear, rather than the present three-periodic, maximum. The contribution here is the exact five-window **global** optimum for every length together with exact counts of all labeled maximizing words. In the inspected portions of the source manuscript and results found in targeted searches, that optimization and its enumeration were not stated.

## Limitations

The result is specific to binary symbols and exactly one length-five permutation window. It does not classify every maximizing word by an explicit regular expression, establish codebook-size optima, or extend the formula to larger window lengths or alphabets. The finite certificate is small and exhaustively specified, but independent validation and definitive priority confirmation have not been performed. Other inaccessible or unindexed sources might contain an equivalent result.

## References

1. Yuan-Pon Chen and Olgica Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1 (first public 2026-10-11), Sections II and IV, https://arxiv.org/html/2610.15701v1.
2. `check.py`, an accompanying standalone exact-integer recurrence and direct-channel verification implementation.
