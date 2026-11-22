# An all-level binomid nondivisibility family of cyclotomic recurrences

## Finding

For integers \(q\ge2\), \(t\ge1\), define
\[
f_0=-(t+1),\qquad f_1=q,\qquad f_{n+2}=-qf_{n+1}-q^2f_n\quad(n\ge0).
\]
For any nonzero integer sequence \(g=(g_n)_{n\ge1}\), define the generalized binomial coefficient
\[
B_g(N,K)=\frac{g_{N-K+1}\cdots g_N}{g_1\cdots g_K}\quad(0\le K\le N),\qquad B_g(N,0)=1.
\]
Let \(C_c(n)=B_f(n+c-1,c)\) for every \(c,n\ge1\). Say \(f\) is **binomid at every level** when \(B_{C_c}(N,K)\) is integral for every \(c\ge1\) and \(0\le K\le N\).

**Theorem (complete two-parameter criterion).** For this entire recurrence family,
\[
\boxed{f\text{ is binomid at every level}\quad\Longleftrightarrow\quad t\mid q^4.}
\]
For comparison, \(f\) is an index-divisibility sequence precisely when \(t\mid q^2\) (the previously established classification, also verified below). Consequently the explicit recurrence with \(q=2\), \(t=8\) is binomid at every level but **not divisible**: \(f_2=32\) does not divide \(f_4=16\). This answers the all-level implication in Shapiro's order-two recurrence question in the negative, without claiming a classification of all order-two recurrences.

## Assumptions and scope

All indices and parameters are integers in the displayed ranges. Integer binomid coefficients can be negative; only integrality is required, as in the nonzero-integer definition in Shapiro (2023). Every positive-index sequence term is nonzero. The all-level property is defined through the complete family of generalized-binomial columns, which is equivalent to integrality of every row and all entries of the binomid pyramid by Shapiro's Definition 4 and Corollary 10. The recurrence has two distinct cyclotomic roots of absolute value \(q\); since \(q\ge2\), this sequence is not eventually periodic as an integer sequence.

## Proof

**1. Solve the recurrence.** Define the periodic weight function \(u_n\) for all \(n\ge0\) by
\[
u_{3j}=-(t+1),\qquad u_{3j+1}=1,\qquad u_{3j+2}=t\qquad(j\ge0).
\]
The identity \(u_{n+2}+u_{n+1}+u_n=0\) gives the exact solution \(f_n=q^n u_n\), including both initial values. In particular, all terms with positive index are nonzero.

**2. Reduce all pyramid coefficients to a periodic counting inequality.** Fix positive integers \(c,k\) and a nonnegative shift \(m\). Write \(N=m+k\). Because each column is a product of \(c\) consecutive sequence terms divided by the same constant product, its generalized coefficient is exactly
\[
B_{C_c}(m+k,k)=
\frac{\displaystyle\prod_{i=m+1}^{m+k}\prod_{j=0}^{c-1}f_{i+j}}
{\displaystyle\prod_{i=1}^{k}\prod_{j=0}^{c-1}f_{i+j}}.
\]
The \(q\)-power on the right is precisely \(q^{ckm}\): each of the \(ck\) indices increases by \(m\). For \(r\in\{0,2\}\), define the integer
\[
E_r(c,k,m)=
\sum_{i=m+1}^{m+k}\sum_{j=0}^{c-1}\mathbf1_{i+j\equiv r\ (\mathrm{mod}\ 3)}
-\sum_{i=1}^{k}\sum_{j=0}^{c-1}\mathbf1_{i+j\equiv r\ (\mathrm{mod}\ 3)}.
\]
The weight classes are \(1,t,-(t+1)\) in residues \(1,2,0\) respectively. Thus for any prime \(p\), writing \(a=\nu_p(q)\), \(b=\nu_p(t)\), and \(d=\nu_p(t+1)\), one gets the exact identity
\[
\nu_p\bigl(B_{C_c}(m+k,k)\bigr)
=a ckm+bE_2(c,k,m)+dE_0(c,k,m).
\tag{1}
\]
Valuation of a rational number here means numerator valuation minus denominator valuation, independently of its sign.

**3. The finite residue lemma.** The indicator depends only on the index modulo three. The difference of two length-three blocks is zero, both in the \(i\)- and \(j\)-directions; likewise shifting \(m\) by three does nothing. Hence \(E_r(c,k,m)\) depends only on \((c,k,m)\bmod3\), and it vanishes whenever any of the three arguments is divisible by three. Its complete nonzero-case table, with columns indexed by \(m\equiv1,2\pmod3\), is

| \((c,k)\bmod3\) | \(E_0\) for \(m\equiv1,2\) | \(E_2\) for \(m\equiv1,2\) |
|---|---|---|
| \((1,1)\) | \((0,1)\) | \((1,0)\) |
| \((1,2)\) | \((1,1)\) | \((0,-1)\) |
| \((2,1)\) | \((1,1)\) | \((0,-1)\) |
| \((2,2)\) | \((1,0)\) | \((-1,-1)\) |

Each row follows by counting the at most four cells \(i+j\pmod3\) for representatives \(c,k\in\{1,2\}\); the three-divisibility cases give zero. In particular, uniformly over all positive \(c,k\) and nonnegative \(m\),
\[
E_0\ge0,\qquad E_2\ge-1,
\]
and any instance of \(E_2=-1\) has \(ckm\ge4\). Indeed, its residue classes require respectively \((c,k,m)\equiv(1,2,2),(2,1,2),(2,2,1),(2,2,2)\pmod3\), and the least product in each class is at least four. At \(m=0\), both differences vanish and the coefficient equals one.

**4. Sufficiency at all levels.** Assume \(t\mid q^4\). Then for every prime \(p\), \(b\le4a\). If \(E_2\ge0\), every term on the right of (1) is nonnegative because \(E_0\ge0\). If \(E_2=-1\), we have \(ckm\ge4\) and hence
\[
a ckm-b+dE_0\ge4a-b\ge0.
\]
Thus every prime has nonnegative valuation in every generalized coefficient of every column, establishing integrality simultaneously for all \(c,k,m\). No computational cutoff is used.

**5. Necessity and sharp nondivisibility.** If all levels are integral, the first column \(C_1(n)=f_n/f_1\) is binomid; scaling every element of a sequence by a common nonzero constant does not change its generalized binomial coefficients. Taking \(N=4,K=2\) in this first column yields
\[
B_f(4,2)=\frac{f_4f_3}{f_2f_1}=-\frac{q^4(t+1)}{t}.
\]
Because \(\gcd(t,t+1)=1\), integrality forces \(t\mid q^4\), proving necessity. For the separate divisibility property, \(f_2=tq^2\) and \(f_4=q^4\) show that index divisibility forces \(t\mid q^2\). Conversely, if \(t\mid q^2\) and \(m\mid n\) with \(m,n\ge1\), the explicit formula gives \(f_n/f_m=q^{n-m}u_n/u_m\). If \(m\equiv0\pmod3\), then \(n\equiv0\pmod3\); if \(m\equiv1\pmod3\), its weight is \(1\). If \(m\equiv2\pmod3\), the only possible denominator is \(t\), and for \(n\not\equiv2\pmod3\) one has \(n-m\ge m\ge2\), so \(t\mid q^{n-m}\). This proves the stated divisibility comparison. Finally \(q=2,t=8\) satisfies \(t\mid q^4\) but not \(t\mid q^2\), giving the claimed signed recurrence counterexample. \(\square\)

## Verification

The included standalone program `artifacts/check.py` constructs the recurrence directly, computes column entries using exact rational arithmetic, and independently checks binomid coefficients for eight parameter pairs and ten column widths through row 31. It also independently checks the complete 27-case residue lemma, verifies its period reductions in a larger finite range, and tests four parameter pairs violating the criterion. Its deterministic output is supplied in `artifacts/check_output.txt`. The finite checks corroborate but do not establish the universal quantifiers; Steps 1–5 do.

## Relationship to prior work

Shapiro (2023, journal version, Definition 4, Corollary 10 and Open Questions 29(1)) defines the full binomid pyramid and explicitly asks whether an all-level binomid sequence satisfying a second-order recurrence must be divisible. His all-level theorems for divisor-product and Lucas sequences with zero initial value do not answer the nondivisible case exhibited here.

An earlier publicly available result titled *A cyclotomic second-order family separating binomid integrality from divisibility* proves the sharp **base-level** criterion \(t\mid q^4\) and the weaker divisibility criterion \(t\mid q^2\) for precisely this recurrence, and explicitly states that higher-level integrality is not proved. The new theorem's contribution is the all-level implication for arbitrary column width and generalized-binomial indices, established via the two-dimensional periodic-residue lemma; the base-level counterexample alone is insufficient. Other known all-level criteria for divisor chains, interlaced divisor chains, and divisor-product sequences do not give an all-level nondivisible instance here. In particular, the interlaced-chain criterion requires \(f_2\mid f_4\), which fails in our example, and the eventually periodic second-order classification excludes exponential growth. Caalim and Tanaka (2024) analyze extensions of nonnegative prime-adic binomid indexes rather than the signed two-parameter all-level recurrence classification.

## Limitations

The theorem completely classifies all-level binomidness only within the explicitly stated two-parameter cyclotomic family. It does not classify every second-order recurrence, establish the stronger property for all ComboSum sequences, or produce an everywhere-positive second-order counterexample. It distinguishes exact infinite proof from the finite tests. Novelty is judged relative to the inspected primary sources and searchable research records; an unindexed or implicit earlier all-level statement remains a priority risk. No independent scientific audit has been performed.

## References

1. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243v1 (first posted 2023-02-04), *Integers* 23 (2023), A57, especially Definition 4, Corollary 10 and Open Questions 29(1). https://arxiv.org/abs/2302.02243 ; https://math.colgate.edu/~integers/x57/x57.pdf
2. *A cyclotomic second-order family separating binomid integrality from divisibility* (2026), public proof of the base-level and divisibility equivalences. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-cyclotomic-second-order-family-separating-binomid-integrality--f8a8d041cb09
3. *Interlaced divisor chains are binomid at every level* (2026), a distinct sufficient criterion. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-interlaced-divisor-chains-are-binomid-at-every-level--5781f8464ab9
4. *A sharp four-row binomid test for eventually periodic second-order recurrences* (2026), an excluded periodic subclass. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-four-row-binomid-test-for-eventually-periodic-second-ord--076dbf2243ff
5. J. Caalim and Y. Tanaka, *Lexicographically Minimal Extension of a Finite Binomid Index*, *Integers* 24 (2024), A53. https://math.colgate.edu/~integers/y53/y53.pdf
