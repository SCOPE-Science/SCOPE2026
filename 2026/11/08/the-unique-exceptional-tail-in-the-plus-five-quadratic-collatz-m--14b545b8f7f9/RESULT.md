# The unique exceptional tail in the plus-five quadratic Collatz map

## Finding

Consider the map on nonnegative integers
\[
T(n)=\begin{cases}n/2,&n\text{ even},\\n(n+5)/2,&n\text{ odd}.\end{cases}
\]
For every positive starting integer, write \(n=2^\ell u\) with \(\ell\ge0\) and \(u\) odd. The orbit is bounded if and only if
\[
u=1\quad\text{or}\quad u=2^m-5\ \text{for some integer }m\ge3.\]
The odd state \(1\) is the **unique** positive nonterminal odd state entering a cycle: its next odd state is \(3\). For each \(m\ge3\), the state \(u_m=2^m-5\) belongs to the cycle
\[
u_m\to 2^{m-1}u_m\to 2^{m-2}u_m\to\cdots\to 2u_m\to u_m,\]
whose least period is exactly \(m\). Every other positive trajectory tends to \(+\infty\). The state \(0\) is fixed separately.

If \(B(X)\) denotes the number of bounded positive initial states not exceeding a real number \(X\ge1\), then the exact formula is
\[
B(X)=1+\lfloor\log_2 X\rfloor+
\sum_{\substack{m\ge3\\2^m-5\le X}}
\left(1+\left\lfloor\log_2\frac{X}{2^m-5}\right\rfloor\right).
\]
In particular, as \(X\to\infty\),
\[B(X)=\tfrac12(\log_2 X)^2+O(\log(X+2)).\]

## Assumptions and scope

The map acts on nonnegative integers; statements about escaping and counting are restricted to positive starting values. A bounded orbit has finitely many values and is eventually periodic; convergence to infinity means that for every real threshold, all sufficiently late iterates exceed it. The claim classifies all positive initial values without a numerical bound and does not require a conjecture about the classical Collatz map.

## Proof

**Step 1: odd-to-odd dynamics.** If \(y\) is a positive odd state, write uniquely
\[y+5=2^jk,\qquad j\ge1,\quad k\ge1\text{ odd}.\]
Applying \(T\) once and then halving until the next odd value gives
\[y\longmapsto ky.\]
If \(k=1\), then \(y=2^j-5>0\), forcing \(j\ge3\), and the original trajectory returns to \(y\) after exactly \(j\) steps. There are no odd states between these returns, hence the least period is \(j\). If \(k\ge3\), the next odd state \(ky\) is strictly greater than \(y\), and every intermediate even state is at least \(ky\). Consequently, a positive trajectory without a terminal odd state diverges to infinity. Any bounded trajectory must reach a terminal state.

**Step 2: rigidity of a first terminal entry.** Suppose a nonterminal odd state \(y=2^jk-5>0\), with odd \(k\ge3\), has next odd state equal to some terminal \(2^m-5\). Then
\[
2^m=2^jk^2-5(k-1).\tag{1}
\]
Since the next odd state strictly exceeds \(y\), we have \(2^m>2^jk\), so \(m>j\). Reducing (1) modulo \(5\), and observing that \(2\) is a quadratic nonresidue modulo \(5\), shows that \(5\nmid k\) and \(m-j\) is even. Write \(m-j=2h\) with \(h\ge1\). Rearranging (1) gives
\[
2^j\bigl(k^2-2^{2h}\bigr)=5(k-1)>0.\tag{2}
\]
Thus \(k>2^h\). Let \(t=k-2^h\), a positive odd integer. If \(t\ge3\), then the left side of (2) satisfies
\[
2^j t(k+2^h)\ge6(k+2^h)>5(k-1),
\]
contradicting (2). Therefore \(t=1\), so \(k=2^h+1\). Equation (2) reduces to
\[
2^j(2^{h+1}+1)=5\cdot 2^h.\tag{3}
\]
The oddness of \(2^{h+1}+1\) forces \(j=h\) by comparing exact powers of \(2\). Dividing (3) by \(2^h\) gives \(2^{h+1}+1=5\), hence \(h=j=1\), \(k=3\), and \(m=3\). The precursor is precisely \(y=2\cdot3-5=1\), and indeed \(T(1)=3\).

**Step 3: no earlier odd precursors.** If an odd positive state \(z\) had next odd value equal to \(1\), Step 1 would force \(kz=1\), hence \(z=k=1\). But for \(z=1\), the unique factorization \(1+5=2\cdot3\) has \(k=3\), not \(1\). Thus no other positive odd state can lead to \(1\). Combining this with Step 2 proves that all bounded odd starting states are exactly the terminal states and \(1\); all others diverge. An even starting value just removes its powers of \(2\) before entering the same odd trajectory.

**Step 4: count.** Each allowed odd state \(u\) contributes precisely the distinct positive starts \(2^\ell u\le X\), numbering \(1+\lfloor\log_2(X/u)\rfloor\). This gives the displayed sum, including the exceptional odd state \(1\) exactly once. For \(m\ge3\), \(\log_2(2^m-5)=m+O(2^{-m})\), uniformly. With \(L=\log_2 X\) and \(m\) up to \(L+O(1)\), summing the arithmetic progression \(\sum_m(L-m)\) and controlling the floors by \(O(L+1)\) yields \(\tfrac12L^2+O(L+1)\).

## Verification

Run \(\texttt{python3 verify.py}\) with the standard Python library. It checks the exact odd-to-odd identity for a bounded integer grid, searches all possible one-step terminal entries for \(j\le12\) and odd \(k\le2001\), verifies that only \((j,k,m)=(1,3,3)\) occurs in that grid, tests the period formula for \(3\le m\le20\), and compares exact counts against independent direct integer enumeration for stated finite ranges. The proof of the unbounded classification is algebraic; finite tests are not used to infer it.

## Relationship to prior work

Xuda Ye, *Classification of the Orbits of Three Quadratic Collatz-type Maps* (first posted October 7, 2026, arXiv:2610.10660), classifies the three odd branches \(n(n-1)/2\), \(n(n+1)/2\), and \((n^2-1)/4\). Its terminal-state reduction motivates the present analysis but does not state or imply the plus-five terminal-entry equation (2) or the classification here. Hassan Sedaghat's study of the divide-or-choose-two map concerns the different branch \(n(n-1)/2\). In contrast, the plus-five map exhibits exactly one nonterminal positive odd entry into a cycle; the complete terminal-entry obstruction is derived above without an external Diophantine classification.

## Limitations

This theorem concerns the single natural plus-five coefficient and does not classify odd branches \(n(n+c)/2\) for arbitrary odd \(c\), quantify escape rates, or prove priority over every uncatalogued historical work. The related recent primary manuscript was available through its abstract and detailed public exposition; attempts to access its full preprint were unsuccessful, so an unidentified broader treatment in that manuscript remains a historical-priority risk. Independent mathematical auditing has not been performed.

## References

- Xuda Ye, *Classification of the Orbits of Three Quadratic Collatz-type Maps*, arXiv:2610.10660 (first public posting 2026-10-07), https://arxiv.org/abs/2610.10660 .
- Hassan Sedaghat, *Dual Nature of Orbits of the Divide-or-Choose 2 Rule: A Quadratic Collatz-type Recursion*, arXiv:2005.10712 (2020), https://arxiv.org/abs/2005.10712 .
