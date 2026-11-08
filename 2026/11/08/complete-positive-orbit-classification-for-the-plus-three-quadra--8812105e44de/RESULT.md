# Complete positive-orbit classification for the plus-three quadratic Collatz map

## Finding

Define the map \(T:\mathbb Z_{\ge0}\to\mathbb Z_{\ge0}\) by
\[
T(n)=\begin{cases}n/2,&n\text{ even},\\n(n+3)/2,&n\text{ odd}.\end{cases}
\]
For every \(n\ge1\), write \(n=2^\ell q\), where \(\ell\ge0\) and \(q\ge1\) is odd. Then exactly one of the following occurs.

**Bounded:** If \(q=2^m-3\) for an integer \(m\ge2\), the orbit reaches the **primitive** \(m\)-cycle
\[
(2^m-3)\longrightarrow 2^{m-1}(2^m-3)\longrightarrow\cdots\longrightarrow2(2^m-3)\longrightarrow(2^m-3).
\]
Every bounded positive orbit is of this form. For \(m=2\), the cycle is \(1\leftrightarrow2\). The point \(0\) is also fixed.

**Escaping:** If \(q\) is not of the stated form, then \(T^j(n)\to+\infty\) as \(j\to\infty\). There are no noncycle positive starting values eventually entering one of the displayed cycles except their positive dyadic multiples.

Consequently, the number \(B(X)\) of **positive** bounded starting values \(n\le X\), for integer \(X\ge1\), is exactly
\[
 B(X)=\sum_{\substack{m\ge2\\2^m-3\le X}}
 \left(1+\left\lfloor\log_2\frac{X}{2^m-3}\right\rfloor\right)
 =\frac12(\log_2 X)^2+O(\log(X+2)).
\]

## Assumptions and scope

The iteration is on the nonnegative integers and uses ordinary (not accelerated) steps. An orbit is bounded if its iterates are bounded; divergence means the **entire** sequence of iterates tends to positive infinity, not merely an unbounded subsequence. The odd-part decomposition \(n=2^\ell q\) is unique, and logarithms in the counting formula are real base-two logarithms. The result is for the **specific plus-three odd branch**, not arbitrary coefficients \(c\) in \(n(n+c)/2\).

## Proof

**1. Odd-to-odd transition and the terminal cycles.** Let \(y\ge1\) be odd. There are unique integers \(j\ge1\) and odd \(k\ge1\) such that \(y+3=2^j k\). Then
\[
T(y)=2^{j-1}ky,
\quad T^j(y)=ky,
\]
where the intervening \(j-1\) steps are successive halvings. Since \(k\) and \(y\) are odd, \(ky\) is the next odd iterate. If \(k=1\), then \(y=2^j-3>0\), forcing \(j\ge2\); the displayed transition returns to \(y\), giving the cycle of exactly length \(j\) (all members distinct powers of two times \(y\)). If \(k\ge3\), the next odd iterate is strictly greater than \(y\), and each intermediate even iterate is at least that next odd iterate.

**2. No nonterminal odd value enters a terminal cycle in one odd-to-odd step.** Suppose, toward contradiction, that \(j\ge1\), odd \(k\ge3\), \(y=2^j k-3>0\), and \(ky=2^m-3\) for some \(m\ge2\). Rearranging gives
\[
2^m=2^j k^2-3(k-1).
\]
Modulo \(3\), this implies \(3\nmid k\) and \(m\equiv j\pmod2\). Moreover
\[
2^m-2^j=(k-1)(2^j(k+1)-3)>0,
\]
so \(m>j\) and \(m-j=2h\) for an integer \(h\ge1\). Hence
\[
2^j(k^2-2^{2h})=3(k-1)>0.
\]
Now \(k>2^h\), so the integer \(2^h\le k-1\), giving
\[
2^j(k^2-2^{2h})\ge2\big(k^2-(k-1)^2\big)=4k-2>3(k-1),
\]
a contradiction. This rules out **all** first arrivals from a nonterminal odd state, with no finite-size bound.

**3. Classification and full-sequence divergence.** Initially, \(n=2^\ell q\) reaches \(q\) after \(\ell\) halvings. If \(q\) is terminal, Step 1 gives the asserted primitive cycle. Otherwise, Step 2 forbids any later odd term from being terminal. Each odd-to-odd step therefore multiplies the current odd term by an odd integer at least \(3\), so the odd terms tend to infinity. Every intervening even iterate between two successive odd terms is at least the later odd term, as shown in Step 1, and the first finite segment is irrelevant. Thus **all** iterates tend to infinity. This proves the complete classification, including the lack of other cycles or eventual basins.

**4. Exact count and asymptotic.** For \(n\ge1\), a bounded starting value is uniquely \(2^\ell(2^m-3)\), \(m\ge2\), \(\ell\ge0\). Fixing \(m\) and counting admissible \(\ell\) gives the stated sum. To estimate it let \(L=\lfloor\log_2 X\rfloor\). For \(m\ge3\), \(2^{m-1}<2^m-3<2^m\), so the number of eligible \(\ell\) differs by at most one from \(\max(0,L-m+1)\). The exceptional \(m=2\) contributes \(L+1\), and only \(O(1)\) more indices \(m\) lie near the upper cutoff. Summing \(\max(0,L-m+1)\) for \(m=3,\ldots,L\) gives \(\tfrac12L^2+O(L)\), hence the claimed \(\tfrac12(\log_2 X)^2+O(\log(X+2))\).

## Verification

The attached `verify.py` contains exact-integer finite consistency checks. It checks all odd inputs through 100000 for the odd-to-odd formula, 3750 possible nonterminal-to-terminal tests (all \(1\le j\le15\), odd \(3\le k\le501\)), the primitive cycles at \(2\le m\le17\), finite trajectory classifications for initial values \(1\le n\le2000\), and the bounded-count identity for \(X=100,1000,10000\). Run with `python3 verify.py` in the directory containing this file. The unrestricted claims depend on the proof above; these tests are not an infinite certificate.

## Relationship to prior work

Ye, *Classification of the Orbits of Three Quadratic Collatz-type Maps* (arXiv:2610.10660, posted October 7, 2026), determines the dynamics for the different odd branches \(n(n-1)/2\), \(n(n+1)/2\), and \((n^2-1)/4\). His Theorem 2 notably includes the exceptional bounded odd part \(5\) for the \(n(n+1)/2\) map. The present claim is a complete classification for the new odd branch \(n(n+3)/2\), with **no** exceptional positive odd parts, plus an exact bounded-basin count. The odd-to-odd compression is an adaptation of a method used in the prior papers, not claimed as new by itself. Sedaghat's 2020 papers study the divide-or-choose-two branch and its symmetric companion; they do not directly cover the plus-three rule.

## Limitations

The result is confined to the nonnegative-integer plus-three map. It does not classify general positive odd parameters \(c\) in the branch \(n(n+c)/2\), nor does it give uniform escape-time estimates for the unbounded trajectories. The arithmetic argument is self-contained; historical priority of an equivalent but unindexed formulation cannot be ruled out. All computational tests are finite and do not replace the proof.

## References

- X. Ye, *Classification of the Orbits of Three Quadratic Collatz-type Maps*, arXiv:2610.10660 (first posted 2026-10-07), https://arxiv.org/abs/2610.10660.
- H. Sedaghat, *Bounded Orbits of Quadratic Collatz-type Recursions*, arXiv:2004.07357 (2020), https://arxiv.org/abs/2004.07357.
- H. Sedaghat, *Dual Nature of Orbits of the Divide-or-Choose 2 Rule: A Quadratic Collatz-type Recursion*, arXiv:2005.10712 (2020), https://arxiv.org/abs/2005.10712.
