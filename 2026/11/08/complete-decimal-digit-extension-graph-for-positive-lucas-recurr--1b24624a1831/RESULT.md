# Complete decimal digit-extension graph for positive Lucas recurrences

## Finding
For every integer \(a\ge2\), define \(U_0=0\), \(U_1=1\), and \(U_{n+2}=aU_{n+1}+U_n\). Put a directed edge \(U_m\longrightarrow U_{m+k}\) precisely when \(m,k\ge1\) and the target is obtained by appending one decimal digit to the source:
\[
U_{m+k}=10U_m+d,\qquad 0\le d\le9.
\]
**The complete decimal graph for every coefficient \(a\ge2\) is:**

| Recurrence coefficient | All directed edges |
|:--|:--|
| \(a=2\) | \(1\to12\), \(2\to29\) |
| \(a=3\) | \(1\to10\), \(3\to33\), \(10\to109\) |
| \(a=4\) | \(1\to17\) |
| \(5\le a\le9\) | none |
| \(a=10\) | \(1\to10\), \(10\to101\) |
| \(11\le a\le19\) | \(1\to a\) |
| \(a\ge20\) | none |

Consequently the maximum length of a decimal walk is three vertices, attained precisely for \(a=3\) and \(a=10\); the two length-three walks are \(1\to10\to109\) and \(1\to10\to101\), respectively. A base-independent algebraic-norm lemma used below gives an explicit finite search bound for arbitrary bases; **the novel classification claimed here is the exact decimal graph**, not the previously known general finiteness of digit-appending Lucas walks.

## Assumptions and scope
All parameters are integers with \(a,b\ge2\). Positive source indices \(m\ge1\), positive index jumps \(k\ge1\), and digit \(d\in\{0,\ldots,b-1\}\) are required. The recurrence terms are treated as ordinary positive integers. Leading zeros in the appended one-digit suffix are permitted: the condition is exactly \(U_{m+k}=bU_m+d\), even when \(d=0\). The statement concerns **one digit per step**; it does not concern inserting a digit in the middle or appending multiple digits at once.

## Proof
First we establish a quantitative auxiliary bound for arbitrary integer bases \(b\ge2\). Write \(\alpha=(a+\sqrt{a^2+4})/2\). Every possible base-\(b\) edge obeys
\[
U_{k+1}\le 2b-1,\qquad
\alpha^m<(b+1)\bigl(1+(b-1)\sqrt{a^2+4}\bigr).
\]
This explicit estimate is useful for reproducibility, although general Lucas-walk termination was previously known.

**1. Index-jump cutoff.** By induction from the recurrence, for every \(m,k\ge1\),
\[
U_{m+k}=U_{k+1}U_m+U_kU_{m-1}.
\]
All terms are nonnegative and \(U_m\ge1\). If an edge occurs, then
\[
U_{k+1}U_m\le U_{m+k}\le bU_m+b-1\le(2b-1)U_m,
\]
so \(U_{k+1}\le2b-1\).

**2. Uniform source-index cutoff.** Let \(\Delta=a^2+4\), \(\alpha=(a+\sqrt\Delta)/2\), and \(\beta=(a-\sqrt\Delta)/2=-\alpha^{-1}\). The Binet identity
\[
U_j=\frac{\alpha^j-\beta^j}{\sqrt\Delta}
\]
holds by the recurrence and initial data. For an edge with index jump \(k\), put \(D=U_{m+k}-bU_m=d\). Then
\[
\sqrt\Delta D=(\alpha^k-b)\alpha^m-(\beta^k-b)\beta^m.
\]
The conjugate product
\[
N=(\alpha^k-b)(\beta^k-b)=b^2-b(\alpha^k+\beta^k)+(-1)^k
\]
is an integer because \(\alpha^k+\beta^k\) satisfies the integer recurrence with initial values \(2,a\). It is nonzero: if \(\alpha^k=b\), algebraic conjugation forces \(\beta^k=b\), impossible since \(|\beta|<1<b\); the same applies with \(\alpha,\beta\) interchanged. Hence \(|N|\ge1\). Since \(|\beta^k-b|<b+1\), we have \(|\alpha^k-b|>1/(b+1)\). The triangle inequality therefore gives
\[
(b-1)\sqrt\Delta\ge |D|\sqrt\Delta
>\frac{\alpha^m}{b+1}-(b+1)\alpha^{-m}.
\]
Put \(t=\alpha^m/(b+1)>0\), \(R=(b-1)\sqrt\Delta>0\). Then \(t-1/t<R\). Since \(t\ge R+1\) would give \(t-1/t\ge R+1-1/(R+1)>R\), one has \(t<R+1\). This proves the displayed source-index cutoff. Both cutoffs are finite, since \(U_{k+1}\to\infty\) and \(\alpha^m\to\infty\).

**3. Exact decimal classification.** For every \(m\ge1\), the increasing recurrence has
\[
U_{m+1}=aU_m+U_{m-1},\qquad U_{m+2}=(a^2+1)U_m+aU_{m-1}.
\]
Each possible decimal extension lies in \([10U_m,10U_m+9]\); the recurrence is strictly increasing in its positive index. The following mutually exhaustive cases therefore settle *all* jumps, not merely bounded samples.

If \(a\ge11\), then for \(m\ge2\), \(U_{m+1}-10U_m=(a-10)U_m+U_{m-1}>9\); larger jumps are excluded by monotonicity. For \(m=1\), the only eligible term is \(U_2=a\), and exactly \(11\le a\le19\) work. (The case \(a=10\) is treated separately.)

If \(a=10\), the one-step difference is exactly \(U_{m-1}\). It lies in \([0,9]\) precisely for \(m=1,2\), giving \(U_1=1\to U_2=10\) and \(U_2=10\to U_3=101\); it is at least \(10\) for \(m\ge3\). Every jump of two or more is too large because \(U_{m+2}\ge100U_m>10U_m+9\).

For \(5\le a\le9\), \(U_{m+1}<10U_m\), whereas \(U_{m+2}\ge a^2U_m\ge25U_m>10U_m+9\); hence there are no edges.

For \(a=4\), \(U_{m+1}<10U_m\) while \(U_{m+2}=17U_m+4U_{m-1}\). At \(m=1\) this gives \(1\to17\); at \(m\ge2\), \(U_m\ge4\) makes the two-step term exceed \(10U_m+9\). Larger jumps are excluded.

For \(a=3\), one-step jumps are too small, while \(U_{m+2}=10U_m+3U_{m-1}\). The difference lies in \([0,9]\) exactly for \(m=1,2,3\), since the preceding terms are \(U_0=0,U_1=1,U_2=3\) and \(U_3=10\) exceeds three. These give \(1\to10\), \(3\to33\), \(10\to109\). Three-step and greater jumps are too large: \(U_{m+3}\ge3U_{m+2}\ge30U_m>10U_m+9\).

Finally, for \(a=2\), one- and two-step jumps are too small, because \(U_{m+1}<3U_m\) and \(U_{m+2}<7U_m\). Three-step jumps satisfy \(U_{m+3}=12U_m+5U_{m-1}\). At \(m=1,2\) these give \(1\to12\) and \(2\to29\); for \(m\ge3\), \(U_m\ge5\) gives \(U_{m+3}-10U_m\ge2U_m\ge10\). All larger jumps are excluded. This exhausts all cases and establishes the graph and maximal-walk statements.

## Verification
The accompanying `check.py` independently enumerates exact integer edges for \(299\) recurrence coefficients at decimal base using the proved finite cutoff, then tests \(4321\) coefficient/base pairs, checks \(6525\) integer addition-identity instances, and verifies \(64815\) integer norm nonvanishing instances. Its observed output is provided in `verification_output.txt`. These finite tests are corroborative only; the infinite theorem rests on the displayed proof.

## Relationship to prior work
Miller, Peng, Popescu, and Wattanawanichkul proved that the ordinary Fibonacci sequence admits no right-digit append walk with more than two terms (arXiv:2204.08138, first submitted 18 April 2022). The earlier paper by Miller and collaborators (arXiv:2010.14932, first submitted 28 October 2020) addresses prime and other walks. **Kominers (arXiv:2512.06446, first submitted 6 December 2025) subsequently proved termination in arbitrary bases for general Lucas sequences with unit second coefficient, explicitly including Pell numbers.** Thus general finiteness of the graphs studied here is covered by prior literature and is **not claimed new**. What the inspected texts do not determine is the *entire decimal edge set for every integer coefficient \(a\ge2\)*, including the exceptional three-vertex walks at coefficients \(3\) and \(10\). The explicit algebraic-norm index cutoff provides a self-contained auxiliary proof and an effective enumeration route; no novelty is asserted merely from a different proof of termination.

## Limitations
The exact graph covers decimal base and coefficients \(a\ge2\), not arbitrary initial pairs, other second coefficients or general-base graphs. Finiteness of bounded-digit walks for the broader Lucas family was previously proved by Kominers; the auxiliary cutoff is not claimed sharp or as a new general termination theorem. This is a self-reviewed argument, not an independently audited result. A literature search cannot exclude unindexed equivalent decimal classifications.

## References
1. S. J. Miller, F. Peng, T. Popescu and N. Wattanawanichkul, *Walking to Infinity on the Fibonacci Sequence*, arXiv:2204.08138, first public version 2022-04-18, https://arxiv.org/html/2204.08138v2.
2. S. J. Miller, F. Peng, T. Popescu, J. M. Siktar, N. Wattanawanichkul and the Polymath REU Program, *Walking to Infinity Along Some Number Theory Sequences*, arXiv:2010.14932, first public version 2020-10-28, https://arxiv.org/html/2010.14932v2.
3. S. D. Kominers, *Uniform Bounds for Digit-Appending Fibonacci Walks*, arXiv:2512.06446, first public version 2025-12-06, https://arxiv.org/abs/2512.06446 (especially Theorem 4.2).
4. OEIS Foundation, Pell numbers, A000129, https://oeis.org/A000129 (sequence identification only, not the graph theorem).
