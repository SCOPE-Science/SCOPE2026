# Exact modal-Kleene operator spectra on finite De Morgan chains

## Finding

Let \(C_n=\{0,1,\ldots,n-1\}\) for an integer \(n\ge2\), ordered naturally, with meet \(\min\), join \(\max\), and strong negation \(\neg i=n-1-i\). Call a unary operation \(\Box:C_n\to C_n\) a *modal-Kleene operator* if it preserves binary meets and satisfies the two equations/inequalities (Pos) and (Con) in the next section; no normalization \(\Box(n-1)=n-1\) is assumed.

Write \(M_n\) for the number of such operators and \(N_n\) for those additionally preserving the top element. For every \(m\ge1\),

\[
M_{2m}=\binom{2m-1}{m}^{\!2}+\binom{2m}{m+1},\qquad
M_{2m+1}=\binom{2m}{m}^{\!2}+\binom{2m}{m+1},
\]
\[
N_{2m}=\binom{2m-1}{m}\left(\binom{2m-2}{m-1}+1\right),\qquad
N_{2m+1}=\frac12\binom{2m}{m}\left(\binom{2m}{m}+1\right).
\]

The proof gives an exhaustive, disjoint normal form for every operator: a boundary-preserving monotone map on two halves, or a map forced to be constant on the entire lower half (including the middle point in odd size). In particular, \(N_n/M_n\to 1/2\) as \(n\to\infty\): asymptotically half of these modal-Kleene operators fail to preserve the top element.

## Assumptions and scope

Use the standard finite De Morgan chain \(C_n\) with the unique order-reversing involution \(\neg i=n-1-i\). On a chain, preservation of binary meets is equivalent to isotonicity. For all \(x,y,z\in C_n\), the axioms considered are

\[
\tag{MK}\Box(x\wedge y)=\Box x\wedge\Box y,
\]
\[
\tag{Pos}\neg\Box(z\vee\neg z)\le\Box(z\vee\neg z),
\]
\[
\tag{Con}\Box(x\vee(z\wedge\neg z))\le
\Box x\vee\neg\Box(x\vee(z\wedge\neg z)).
\]

These are the modal-Kleene algebraic conditions considered in Celani–Menchón–Miguelez (2026), read as the explicit equational system above. No \(\Box(n-1)=n-1\), idempotence, extensivity, or interior-modality axiom is imposed. The involution, order, and domain are fixed, and operations are counted on this fixed chain (whose order automorphism group is trivial). \(N_n\) imposes the single additional equation \(\Box(n-1)=n-1\).

## Proof

Write \(f(i)=\Box i\). From (MK), \(f\) is weakly increasing. For \(t=z\wedge\neg z\), the possible \(t\) range from \(0\) to \(\lfloor(n-1)/2\rfloor\), and \(z\vee\neg z=n-1-t\). Thus (Pos), by monotonicity, is the single requirement \(f(\lceil(n-1)/2\rceil)\ge\lceil(n-1)/2\rceil\) (where the ceiling is the first positive element). For (Con), if \(x\ge t\) the inequality is automatic. If \(x<t\), it becomes

\[
f(t)\le\max\{f(x),n-1-f(t)\}.
\]

As \(f(x)\le f(t)\), this is automatic when \(f(t)\le(n-1)/2\); when \(f(t)>(n-1)/2\) it holds exactly if \(f(x)=f(t)\). Hence (Con) is equivalent to the *positive-prefix rigidity* rule

\[
\tag{R}\text{for all }0\le x<t\le\lfloor(n-1)/2\rfloor,
\quad f(t)>(n-1)/2\ \Longrightarrow\ f(x)=f(t).
\]

**Even case.** Let \(n=2m\). Then (Pos) is \(f(m)\ge m\) and the (Con) indices satisfy \(t\le m-1\). Either \(f(m-1)\le m-1\), in which case all \(m\) lower input values map weakly increasingly into \(\{0,\ldots,m-1\}\) and all \(m\) upper input values map weakly increasingly into \(\{m,\ldots,2m-1\}\); or \(f(m-1)\ge m\), in which case (R) forces \(f(0)=\cdots=f(m-1)=c\) for a unique \(c\in\{m,\ldots,2m-1\}\), with the upper \(m\) values any nondecreasing sequence in \(\{c,\ldots,2m-1\}\). These cases are disjoint and both satisfy all axioms.

The first has \(\binom{2m-1}{m}^2\) choices by multiset enumeration. In the second, set \(t=2m-1-c\); for each \(t\in\{0,\ldots,m-1\}\) there are \(\binom{m+t}{m}\) sequences. Hockey-stick summation gives

\[
\sum_{t=0}^{m-1}\binom{m+t}{m}=\binom{2m}{m+1}.
\]

This proves the formula for \(M_{2m}\). If the final output must equal \(2m-1\), the first case has \(\binom{2m-1}{m}\binom{2m-2}{m-1}\) choices, and the second has \(\sum_{t=0}^{m-1}\binom{m-1+t}{m-1}=\binom{2m-1}{m}\); their sum gives \(N_{2m}\). Here the zero-length intermediate sequence when \(m=1\) is counted once.

**Odd case.** Let \(n=2m+1\). The unique negation-fixed middle point is \(m\). By (Pos), \(f(m)\ge m\). Either \(f(m)=m\), in which case the lower \(m\) values are weakly increasing in \(\{0,\ldots,m\}\) and the upper \(m\) values are weakly increasing in \(\{m,\ldots,2m\}\), or \(f(m)=c>m\), in which case (R) at \(t=m\) forces \(f(0)=\cdots=f(m)=c\) and the upper \(m\) values are weakly increasing in \(\{c,\ldots,2m\}\). Again the cases are disjoint and exhaustive.

The first case has \(\binom{2m}{m}^2\) choices. The second contributes \(\sum_{t=0}^{m-1}\binom{m+t}{m}=\binom{2m}{m+1}\), giving \(M_{2m+1}\). Fixing the last value to \(2m\) yields, respectively, \(\binom{2m}{m}\binom{2m-1}{m-1}\) and \(\binom{2m-1}{m}\) choices. Since both of the last binomial coefficients equal \(\frac12\binom{2m}{m}\), their sum is the stated \(N_{2m+1}\).

**Normality density.** The additive terms \(\binom{2m}{m+1}\) and \(\binom{2m-1}{m}\) are exponentially negligible relative to the dominant squares. For odd size, the normal count's dominant term is exactly one-half of the dominant square. For even size, \(\binom{2m-2}{m-1}/\binom{2m-1}{m}=m/(2m-1)\to1/2\). This proves \(N_n/M_n\to1/2\) along both parities.

## Verification

A standalone file `checker.py` exhaustively generates every weakly increasing operation \(f:C_n\to C_n\) for \(2\le n\le9\), evaluates (MK), (Pos), and (Con) directly for every index choice, independently tests the two normal-form cases, and compares the observed totals with the formulas. Run `python checker.py` with a standard Python 3 interpreter; no dependencies are needed.

The exact checked pairs \((M_n,N_n)\) for \(n=2,3,4,5,6,7,8,9\) are \((2,2),(5,3),(13,9),(40,21),(115,70),(415,210),(1281,735),(4956,2485)\). Exhaustion at bounded sizes supports the derivation but is not an infinite proof; the normal-form argument above proves all \(n\ge2\).

## Relationship to prior work

Celani, Menchón and Miguelez (arXiv:2608.10937, first public version August 11, 2026) introduce modal Kleene algebras and a categorical equivalence with modal Kleene triples, including semantics that permit non-top-preserving modal operators. The present statement isolates a complete finite-chain normal form, two parity-sensitive exact enumerators, and the asymptotic prevalence of non-normality. The publicly retrievable primary abstract describes categorical representation and duality but does not report these counts. The full primary article was not accessible for inspection during this comparison; coverage of an uninspected example or appendix is a genuine priority risk, not ruled out by the abstract.

Classifications of preconditionals on finite chains concern binary conditional operations subject to a different axiom system. Enumerations of monadic/Gödel chain operators impose adjunction or closure identities not present here; for example, on \(C_5\), the allowed operation with value tuple \((1,2,2,3,4)\) is not idempotent. Those classifications therefore do not yield the present counts merely by matching the underlying chain. Classical monotone-map multiset enumeration is used as a counting tool, not claimed as new.

## Limitations

The theorem concerns a fixed *chain* carrying its standard De Morgan negation. It does not classify modal expansions of arbitrary Kleene algebras, multimodal or implication expansions, or top-preserving operations subject to stronger modal axioms. The enumerator is exact for the three displayed conditions; it is not asserted to apply under alternative definitions of “modal Kleene algebra.” The novelty comparison has the explicit incomplete-full-text risk noted above. No independent verification or independent priority assessment is claimed.

## References

1. S. Celani, P. Menchón and V. Miguelez, *A Modal Expansion of Kleene Algebras via Twist Structures*, arXiv:2608.10937v1, posted 2026-08-11, https://arxiv.org/abs/2608.10937.
2. J. A. Kalman, *Lattices with involution*, Transactions of the American Mathematical Society 87 (1958), 485–491. Foundational Kleene lattice context; not claimed to address the present enumeration.
3. Public summary of the axioms in Celani–Menchón–Miguelez, https://www.alphaxiv.org/abs/2608.10937. This is secondary and does not replace inspection of the primary full text.
