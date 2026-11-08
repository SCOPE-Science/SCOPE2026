# Sharp pseudo-Frobenius classification for five shifted triangular generators

## Finding

For every integer \(a\ge18\), define the numerical semigroup
\[
 S_a=\langle a,a+1,a+3,a+6,a+10\rangle.
\]
The offsets \(0,1,3,6,10\) are the first five triangular numbers. For a numerical semigroup \(S\), its pseudo-Frobenius set is \(\operatorname{PF}(S)=\{f\in\mathbb Z\setminus S:f+s\in S\text{ for every }s\in S\setminus\{0\}\}\), and its type is \(t(S)=|\operatorname{PF}(S)|\).

Let \(c(n)\) be the minimum number of summands from \(\{1,3,6,10\}\) required to sum to \(n\ge0\), with \(c(0)=0\). For \(s=0,1,\ldots,9\), define the following explicitly finite sets \(K_s\):

| \(s\) | \(K_s\) | \(2+|K_s|\) |
|---:|:---|---:|
| 0 | \(\{1,2,3,5,6\}\) | 7 |
| 1 | \(\{1,2,3,4,6,7\}\) | 8 |
| 2 | \(\{1,3,4,5,7,8\}\) | 8 |
| 3 | \(\{1,2,4,5,6,8,9\}\) | 9 |
| 4 | \(\{1,2,3,5,6,7,9,10\}\) | 10 |
| 5 | \(\{1,3,6,8,10\}\) | 7 |
| 6 | \(\{1,2,9\}\) | 5 |
| 7 | \(\{1,2,3,10\}\) | 6 |
| 8 | \(\{1,3,4\}\) | 5 |
| 9 | \(\{1,2,4,5\}\) | 6 |

**Theorem.** If \(a\ge18\) and \(s\equiv a\pmod{10}\), then
\[
\operatorname{PF}(S_a)=
 \{2a+5,2a+8\}\ \cup\
 \left\{(a-k)+a\bigl(c(a-k)-1\bigr):k\in K_s\right\}.
\]
The two portions of this union are disjoint. Consequently,
\[
\bigl(t(S_a):a\bmod 10=0,1,\ldots,9\bigr)
=(7,8,8,9,10,7,5,6,5,6).
\]
The type function has least period \(10\) on \(a\ge18\). The starting bound is sharp for the displayed pseudo-Frobenius classification: \(\operatorname{PF}(S_{17})=\{33,39,42,48,49\}\), whereas applying the displayed rule to \(17\) would incorrectly add \(24\).

## Assumptions and scope

The parameter \(a\) is an integer, at least \(18\). The displayed five generators are pairwise distinct, lie between \(a\) and \(2a\), and include \(a,a+1\), so they are minimal and generate a cofinite submonoid of \(\mathbb N_0\). The theorem classifies all pseudo-Frobenius numbers, not merely their number. No statement about unrelated shifted families is asserted.

## Proof

**1. Coin-length lemma.** Write \(n=10q+r\), \(0\le r<10\). The following holds:
\[
c(10q+r)=q+w_r\quad(q\ge1),\qquad
(w_0,\ldots,w_9)=(0,1,1,1,2,2,1,2,2,2).
\]
For \(q=0\), the initial vector is \((0,1,2,1,2,3,1,2,3,2)\). In particular \(c(n+10)=c(n)+1\) for all \(n\ge10\); for \(0\le n<10\), the only exceptions are \(n=2,5,8\), at which \(c(n+10)=c(n)\).

Here is a finite-and-infinite proof. The recurrence
\[
c(0)=0,\qquad c(n)=1+\min_{b\in\{1,3,6,10\},\ b\le n}c(n-b)
\]
directly gives the first \(50\) values, shown below in blocks of ten:
\[
\begin{array}{c|rrrrrrrrrr}
 n&0&1&2&3&4&5&6&7&8&9\\\hline
 c(n)&0&1&2&1&2&3&1&2&3&2\\
 c(n+10)&1&2&2&2&3&3&2&3&3&3\\
 c(n+20)&2&3&3&3&4&4&3&4&4&4\\
 c(n+30)&3&4&4&4&5&5&4&5&5&5\\
 c(n+40)&4&5&5&5&6&6&5&6&6&6
\end{array}
\]
For all \(n\), the representation by \(\lfloor n/10\rfloor\) tens and at most three smaller coins gives \(c(n)\le \lfloor n/10\rfloor+3\). For \(n\ge40\), a representation of \(n+10\) using no ten-coins has at least \(\lceil(n+10)/6\rceil\) coins, and
\[
\lceil(n+10)/6\rceil>n/10+4\ge c(n)+1
\qquad(n\ge40).
\]
Thus an optimal representation of \(n+10\) must use a ten-coin. Removing it and then adding it back establishes \(c(n+10)=c(n)+1\) for every \(n\ge40\). The displayed finite table establishes all smaller cases, completing the lemma.

**2. Apéry formula.** The least member of \(S_a\) congruent to \(r\pmod a\), for \(0\le r<a\), is
\[
 W_r=r+a c(r).
\]
Any expression in the generators other than \(a\) has a nonnegative offset sum \(r+ja\) for some \(j\ge0\), hence its total value is at least \(r+a(j+c(r+ja))\). The choice \(j=0\) produces \(W_r\). To exclude \(j\ge1\), note that \(c(x)\ge\lceil x/10\rceil\). If \(r\ge10\), the coin lemma yields \(c(r)\le\lfloor r/10\rfloor+2\), while
\[
 j+c(r+ja)\ge j+\left\lceil\frac{r+18j}{10}\right\rceil
 \ge\lfloor r/10\rfloor+3>c(r).
\]
If \(0\le r<10\), the initial coin vector above verifies the same strict inequality; the only entries with \(c(r)=3\), namely \(r=5,8\), already have \(j+\lceil(r+18j)/10\rceil\ge4\) for \(j\ge1\). This proves the Apéry formula for all \(a\ge18\).

**3. Pseudo-Frobenius criterion.** Every pseudo-Frobenius number is \(W_r-a\) for a residue \(1\le r<a\). Since it suffices to test the minimal positive generators, it is pseudo-Frobenius precisely when, for every \(b\in\{1,3,6,10\}\),
\[
\begin{cases}
 c(r)\ge c(r+b),&r+b<a,\\
 c(r)+1\ge c(r+b-a),&r+b\ge a.
\end{cases}
\tag{*}
\]
Indeed, these inequalities exactly express \(W_r+b\ge W_{(r+b)\bmod a}\); membership in a residue class is equivalent to being at or above its Apéry minimum by a multiple of \(a\).

**4. Interior residues.** First assume \(a\ge30\) and \(r\le a-11\). For \(r\ge10\), testing \(b=10\) in (*) fails by the coin lemma. For \(r<10\), direct substitution of the initial and second coin blocks shows that the only surviving residues are \(r=5,8\), yielding \(W_5-a=2a+5\) and \(W_8-a=2a+8\). Both satisfy the four tests. The residue \(r=2\), whose ten-step inequality happens to be an equality, is excluded by \(b=3\) because \(c(5)>c(2)\).

**5. Boundary residues and ten-class table.** Still with \(a\ge30\), write \(r=a-k\), \(1\le k\le10\). Here \(c(r)\ge2\). When \(b\ge k\), the second line of (*) is automatic since \(0\le b-k\le9\) and \(c(b-k)\le3\). When \(b<k\), the first line of (*) must be checked. The coin lemma reduces these tests to the finite congruence inequalities
\[
\left\lfloor\frac{s-k}{10}\right\rfloor+w_{(s-k)\bmod10}
\ \ge\ 
\left\lfloor\frac{s-k+b}{10}\right\rfloor+w_{(s-k+b)\bmod10}
\quad(b\in\{1,3,6\},\ b<k),
\]
with the expression evaluated using ordinary integer floor; the quotient of \(a\) by ten cancels. Evaluating the at-most-three inequalities for each pair \((s,k)\in\{0,\ldots,9\}\times\{1,\ldots,10\}\) produces exactly the sets \(K_s\) in the displayed table. Each of the ten sets can be reproduced without semigroup computation from the finite \(w\)-vector.

For the twelve remaining values \(18\le a\le29\), the same criterion (*) and explicitly tabulated initial coin lengths give exactly the stated formula. This is a finite check of the listed 12 integers and at most \(29\) residues each, and is independently replayable with the provided exact-integer checker. It is not used to infer the infinite result. For all \(a\ge18\), the two fixed interior residues \(5,8\) do not coincide with any accepted boundary residue \(a-k\), as is verified by the boundary table (for \(a\ge30\) this is immediate). Hence the union is disjoint and the type equals \(2+|K_s|\).

**6. Least period and sharp boundary.** The type vector is visibly not invariant under shifts by \(1\), \(2\), or \(5\), the proper positive divisors of \(10\), so its least period is \(10\). For \(a=17\), an exact Apéry calculation gives \(\operatorname{PF}(S_{17})=\{33,39,42,48,49\}\), while the proposed ten-class rule would add \(24\). This establishes the claimed sharpness of the starting bound.

## Verification

The included file `verify_five.py` uses only the Python standard library. It constructs the shortest-path Apéry set independently of the coin formula, tests the *entire* pseudo-Frobenius set and type for each of the \(983\) integers \(18\le a\le1000\), independently checks direct integer reachability for ten selected values (including the boundary \(17\)), and checks the coin recurrence for all \(0\le n\le2399\). All tests succeeded; the exact JSON output is included in `verify_five_output.json`. The infinite theorem is justified by the proof, not by the finite tests.

## Relationship to prior work

Liu, Xin, Ye and Yin (arXiv:2306.03459, first posted 6 June 2023) develop coin/minimization and Apéry methods for several families of numerical semigroups. Their detailed pseudo-Frobenius calculations concern specialized geometric and repunit-like families. The triangular offsets \(1,3,6,10\) do not satisfy their monotone quotient-recursion restriction \(b_{i+1}=s_i b_i+1\) with integer \(s_i\): the step \(3\to6\) would require \(s_i=5/3\).

Stamate and Strazzanti (arXiv:2601.19629, first posted 27 January 2026) establish a general eventual transport rule for pseudo-Frobenius sets under shifts. This general result supplies context for eventual periodicity but does not state the ten explicit sets, the exact type vector, or the sharp threshold \(18\). The present formula is consistent with their transfer principle, and does not claim to originate the qualitative periodicity phenomenon.

Morales and Dung (arXiv:2601.07467, first posted 12 January 2026) explicitly classify pseudo-Frobenius sets for generalized almost arithmetic generating sequences. The five distinct offsets \(0,1,3,6,10\) have no three-term arithmetic progression among their nonzero offsets, so the displayed five-generator family is not covered by their five-generator arithmetic-progression-plus-one hypothesis (with \(a\) as multiplicity).

No indexed exact table with this parameter family was located in the inspected literature or research record searches. This is a best-evidence originality assessment, not a proof of uniqueness against unpublished or unindexed results.

## Limitations

The classification applies only to \(a\ge18\) and these five generators; it does not classify all shifted semigroups or every triangular-number-generated semigroup. The computational check ends at \(a=1000\), whereas the proof is unconditional for all integers in the stated range. Existing general shift theorems overlap the *eventual-transport mechanism*; the claimed contribution is the explicit exact family-wide pseudo-Frobenius spectrum, type values, and earliest starting bound. Possible independent equivalent classifications in inaccessible or unindexed sources remain a risk. No independent audit was performed.

## References

1. F. Liu, G. Xin, S. Ye and J. Yin, *A Combinatorial Model of Numerical Semigroup*, arXiv:2306.03459, first posted 2023-06-06. https://arxiv.org/abs/2306.03459 .
2. D. I. Stamate and F. Strazzanti, *Nearly Gorenstein and almost symmetric properties in shifted numerical semigroups*, arXiv:2601.19629, first posted 2026-01-27. https://arxiv.org/html/2601.19629 .
3. M. Morales and N. T. Dung, *Frobenius Number of Almost Symmetric Numerical Generalized Almost Arithmetic Semigroups*, arXiv:2601.07467, first posted 2026-01-12. https://arxiv.org/pdf/2601.07467 .
