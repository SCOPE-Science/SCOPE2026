# A sharp affine \(p\)-Frobenius phase for three-term arithmetic progressions

## Finding

Let \(a\ge5\) and \(d\) be coprime positive integers with \(2\le d\le\lfloor a/2\rfloor\), put \(m=\lfloor a/2\rfloor\), and let \(g_p\) denote the greatest nonnegative integer having at most \(p\) nonnegative solutions to
\[
 ax+(a+d)y+(a+2d)z=n.
\]
For **every** integer \(m+2\le p\le a+d\),
\[
 \boxed{g_p=a(p+m-1)+(2a-1)d.} \tag{1}
\]
The **very next** level, \(p_0=a+d+1\), satisfies
\[
 \boxed{g_{p_0}=a(p_0+m-1)+(2a-1)d-(a-2d).} \tag{2}
\]
The decrement \(a-2d\) is strictly positive under the stated coprimality and parameter bounds. Hence the affine law has a sharp right endpoint \(a+d\) for this entire two-parameter family. Equality in (1) is achieved by a threshold in residue \(-d\pmod a\), whereas equality in (2) is achieved in residue \(d\pmod a\).

## Assumptions and scope

All denominations are positive. A representation means an **ordered coordinate triple** \((x,y,z)\in\mathbb Z_{\ge0}^3\); permuting distinct coordinates is *not* an additional equivalence operation. For \(n\ge0\), write \(D(n)\) for the number of such representations. Then \(g_p=\max\{n\ge0:D(n)\le p\}\). Finiteness follows from \(\gcd(a,a+d,a+2d)=1\). The claim concerns exactly \(a\ge5\), \(2\le d\le\lfloor a/2\rfloor\), \(\gcd(a,d)=1\), and the levels in (1), plus their first successor (2). Neither a larger parameter range nor a complete formula for all \(p\) is claimed.

## Proof

**Step 1: exact residue order statistics.**  Fix \(0\le r<a\) and consider with multiplicity the multiset
\[
 {\cal B}_r=\{(a+d)y+(a+2d)z:y,z\ge0,\ y+2z\equiv r\pmod a\}.
\]
Because \(\gcd(a,d)=1\), its elements lie in residue \(dr\pmod a\), and the \(a\) such multisets exhaust all residues of their base values. Write \(T_r(p)\) for the \((p+1)\)-st smallest element of \({\cal B}_r\), **counting multiplicities**. Fixing \((y,z)\) leaves exactly one possible nonnegative \(x\) whenever the base is at most \(n\), and adjoining one coin of denomination \(a\) is injective on representations. Consequently, in residue \(dr\pmod a\), the final integer with at most \(p\) representations is \(T_r(p)-a\). Thus
\[
 g_p=\max_{0\le r<a}\bigl(T_r(p)-a\bigr). \tag{3}
\]
Indeed, at \(T_r(p)-a\) at most \(p\) base values occur; at \(T_r(p)\) at least \(p+1\) occur; all later members of the same residue class also have at least that many.

Group \({\cal B}_r\) by \(y+2z=r+ka\) for \(k\ge0\). Row \(k\) contains exactly
\[
 \ell_k(r)=\left\lfloor\frac{r+ka}{2}\right\rfloor+1
\]
base values, increasing by \(a\) from
\[
 L_k(r)=a\left\lceil\frac{r+ka}{2}\right\rceil+d(r+ka).
 \tag{4}
\]
The final element in row zero is \((a+d)r\), and
\[
 L_1(r)-(a+d)r=a\left\lceil\frac{a-r}{2}\right\rceil+ad>0. \tag{5}
\]
Thus the entire row zero precedes row one. Put \(K_r=\ell_0(r)+\ell_1(r)\). Whenever \(\ell_0(r)\le p<K_r\), the \((p+1)\)-st element among the first **two** rows is
\[
 V_r(p)=L_1(r)+a\bigl(p-\ell_0(r)\bigr). \tag{6}
\]
Even if later rows interleave, this gives \(T_r(p)\le V_r(p)\). For \(p\ge K_r\), if at least \(p-K_r+1\) entries exist in row two, the value
\[
 W_r(p)=L_2(r)+a(p-K_r) \tag{7}
\]
provides an upper bound on \(T_r(p)\), provided all entries of the first two rows lie at most \(W_r(p)\). We use this condition explicitly below, rather than assuming the rows are globally sorted.

**Step 2: upper bound throughout the affine phase.**  Set
\[
 U_p=a(p+m)+(2a-1)d,
\]
so that the asserted upper bound on \(g_p\) is \(U_p-a\). Write \(a=2m+b\), \(b\in\{0,1\}\). For \(r=2h\) or \(2h+1\), (4)--(6) yield
\[
 U_p-V_r(p)=\begin{cases}
 a(1-b)+d(a-1-r),&r=2h,\\
 d(a-1-r),&r=2h+1.
 \end{cases} \tag{8}
\]
Both are nonnegative for every \(0\le r<a\). Also \(p\ge m+2\ge\ell_0(r)\) for all \(r\). Therefore, if \(p<K_r\), we get \(T_r(p)\le V_r(p)\le U_p\).

If \(p\ge K_r\), every entry in rows zero and one lies at most \(V_r(K_r-1)\le U_{K_r-1}<U_p\), using (8), and row two has enough entries. In fact,
\[
 \ell_0(r)+\ell_1(r)+\ell_2(r)\ge a+m+3>a+d+1>p,
\]
since \(d\le m\). The first \(p-K_r+1\) row-two entries are at most \(W_r(p)\), and direct substitution gives
\[
 U_p-W_r(p)=\begin{cases}
 a(h+2-b)-d(2h+1),&r=2h,\\
 (h+1)(a-2d),&r=2h+1.
 \end{cases} \tag{9}
\]
Both are nonnegative because \(2d\le a\). We have counted at least \(p+1\) bases at most \(U_p\), so \(T_r(p)\le U_p\). Combining the cases proves \(g_p\le U_p-a\).

**Step 3: attainment in residue \(r=a-1\).**  In this residue, the first row has \(\lceil a/2\rceil\) entries and the second exactly \(a\) entries, so \(K_{a-1}=a+\lceil a/2\rceil\). For admissible \(d\), we have \(p\le a+d<K_{a-1}\): if \(a\) is even, equality \(d=a/2\) would contradict \(\gcd(a,d)=1\). Equation (8) gives \(V_{a-1}(p)=U_p\). The third row begins at
\[
 L_2(a-1)=U_p+a(a+d-p)\ge U_p,
\]
and later rows begin still farther right. Therefore exactly \(p\) multiset entries are strictly less than \(U_p\); the next is \(U_p\). This proves \(T_{a-1}(p)=U_p\) and establishes (1) via (3).

**Step 4: the first strict break.**  Put \(p_0=a+d+1\) and
\[
 U'=U_{p_0}-(a-2d)=a(p_0+m-1)+(2a+1)d. \tag{10}
\]
We show \(T_r(p_0)\le U'\) for every residue. If \(p_0\ge K_r\), rows zero and one lie at most \(U'\) (their maximum is at most \(V_r(K_r-1)\), and the inequalities from (8) leave a margin of at least \(2d\) after subtracting \(a-2d\)). The row-two length condition still holds because \(p_0<a+m+3\). Formula (9) becomes
\[
 U'-W_r(p_0)=\begin{cases}
 a(h+1-b)+d(1-2h),&r=2h,\\
 h(a-2d),&r=2h+1.
 \end{cases} \tag{11}
\]
These values are nonnegative: for even \(r\), use \(d\le a/2\) (at \(h=0,b=1\) the value is \(d\)), and for odd \(r\), use \(a-2d\ge0\). Hence at least \(p_0+1\) bases are at most \(U'\).

If \(p_0<K_r\), the first \(\ell_0(r)\) bases are in row zero. The first \(p_0-\ell_0(r)+1\) of row one end at \(V_r(p_0)\). If this is at most \(U'\), the desired number is already present. Otherwise (8) says \(V_r(p_0)\le U_{p_0}\), and since \(U_{p_0}-U'=a-2d<a\), the preceding \(p_0-\ell_0(r)\) row-one entries are at most \(V_r(p_0)-a\le U'\). One extra entry comes from row two, since
\[
 U'-L_2(r)=a\left(m+d-\left\lceil\frac r2\right\rceil\right)+d(1-r)\ge2d>0. \tag{12}
\]
This again counts at least \(p_0+1\) entries. Thus \(T_r(p_0)\le U'\) for all \(r\).

For \(r=1\), one has \(p_0\ge K_1\), and (11) gives \(W_1(p_0)=U'\). The fourth row begins at \(L_3(1)=U'+a\), with all subsequent rows later. Hence at \(U'-a\) rows zero and one contribute at most \(K_1\) entries, row two at most \(p_0-K_1\) entries, and all other rows zero. There are therefore at most \(p_0\) bases at \(U'-a\), while at \(U'\) there are at least \(p_0+1\). Thus \(T_1(p_0)=U'\). From (3), \(g_{p_0}=U'-a\), proving (2). The strict decrement follows because equality \(a=2d\) forces \(\gcd(a,d)=d\ge2\), contrary to the assumptions. \(\square\)

## Verification

A reproducible independent dynamic-programming checker `verify.py` computes denumerants using the product of three geometric generating series. For all 977 coprime parameter pairs with \(5\le a\le90\), \(2\le d\le\min(\lfloor a/2\rfloor,28)\), it checked all 40,466 affine-phase levels and all 977 first-break levels against the *actual last index* with denumerant at most the level. For 20 smaller pairs a separate method generated base values directly from \((y,z)\), sorted within residues and recomputed the order statistic at the first-break level. These finite tests corroborate but do not replace the proof for all parameters. Reproduce using `python3 verify.py`; only the Python standard library is needed.

## Relationship to prior work

Komatsu and Ying [1, Theorem 1] derive \(p\)-Frobenius formulas for the same progression for \(0\le p\le\lfloor a/2\rfloor\), and explicitly identify the difficulty of extending their Apéry construction. Here the new interval starts at \(p=\lfloor a/2\rfloor+2\), continues through \(a+d\), and locates its first strict change; it is **not** a restatement of their smaller-\(p\) formula. Subwattanachai [2, Theorem 1] treats triples under a divisibility condition involving one generator and the gcd of the other two; none of its generator permutations satisfies that hypothesis in this parameter domain. A separately available consecutive-denomination result [3] addresses step \(d=1\) and thus does not imply the stated \(d\ge2\) law. General restricted-partition techniques [4] may in principle recover equivalent consequences but were not found to state this uniform two-parameter phase and its first breakpoint.

## Limitations

The theorem deliberately excludes \(d=1\), \(d>\lfloor a/2\rfloor\), and all levels above the one successor \(p=a+d+1\); it does not classify later phases, genera, or gap sums. Directly derived row inequalities establish the infinite result; the finite verification is supplementary. A mathematically equivalent identity may exist implicitly in less accessible general formulas or unindexed work. No independent mathematical audit has been performed.

## References

[1] T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first public 2022-06-27), Theorem 1; *Symmetry* **15** (2023), 1328. https://arxiv.org/abs/2206.13052

[2] K. Subwattanachai, *Generalized Frobenius Number of Three Variables*, arXiv:2309.09149 (first public 2023-09-17), Theorem 1 and Remark 2. https://arxiv.org/abs/2309.09149

[3] *Three exact phases of generalized Frobenius numbers for three consecutive denominations*, published mathematical result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-three-exact-phases-of-generalized-frobenius-numbers-for-three-co--6dc430dbb315

[4] K. Woods, *The Generalized Frobenius Problem via Restricted Partition Functions*, arXiv:2011.00600 (2020). https://arxiv.org/abs/2011.00600
