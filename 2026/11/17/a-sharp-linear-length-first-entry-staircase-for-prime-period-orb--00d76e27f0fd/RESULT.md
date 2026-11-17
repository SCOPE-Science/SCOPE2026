# A sharp linear-length first-entry staircase for prime-period orbits of the doubling map

## Finding

Fix an integer \(m\ge4\). Let \(T:[0,1)\to[0,1)\) be the doubling map \(T(x)=2x\bmod1\). Remove the open hole \((0,t)\), for \(0\le t<1\), and let \(P_m(t)\) denote the number of distinct surviving periodic **orbits** (not points) of least period \(m\).

Put
\[
e=\lfloor (m-1)/3\rfloor,\qquad d_* =\lfloor(m-1)/2\rfloor,\qquad D=2^m-1.
\]
Define
\[
a_m=\frac{2^{m-1}-1}{D},\qquad
b_{m,d}=\frac{2^{m-1}-1-2^{m-1-d}}{D}\quad(1\le d\le d_*).
\]
For a positive integer \(g\), write \(W(g)=0 1^{g-1}\) as a finite binary string. Define the triple \((g_1,g_2,g_3)\) by
\[
(g_1,g_2,g_3)=\begin{cases}
(q-1,q+1,q),&m=3q\ (q,q,q+1),&m=3q+1\ (q,q+1,q+1),&m=3q+2.
\end{cases}
\]
The first case requires \(q\ge2\), which follows from \(m\ge4\). Set \(u_m=W(g_1)W(g_2)W(g_3)\) and
\[
\eta_m=\frac{\operatorname{int}_2(u_m)}{D},
\]
where \(\operatorname{int}_2\) interprets a binary word as its base-two integer. Then \(\eta_m<b_{m,e}<\cdots<b_{m,d_*}<a_m\), with the last displayed chain of two-zero thresholds interpreted in increasing index order. If \(e\ge2\), additionally \(b_{m,e-1}<\eta_m\).

**Complete initial staircase.** For all \(\eta_m<t\le a_m\),
\[
P_m(t)=1+\#\{d\in\mathbb Z:e\le d\le d_*,\ t\le b_{m,d}}.
\]
For \(t>a_m\), \(P_m(t)=0\). At \(t=\eta_m\), at least one additional three-zero period-\(m\) orbit survives. Thus precisely
\[
N_m=2+\lfloor(m-1)/2\rfloor-\lfloor(m-1)/3\rfloor
=\frac m6+O(1)
\]
distinct first-entry thresholds are given before the first three-zero threshold. Every displayed jump contributes exactly one entire least-period-\(m\) orbit. Moreover
\[
a_m-b_{m,d}=\frac{2^{m-1-d}}{2^m-1},
\]
so the gaps from the first threshold form an exact geometric progression with ratio \(1/2\) as \(d\) increases.

## Assumptions and scope

The hole is strictly open, so a periodic orbit with minimum point exactly \(t\) survives. Counts are for distinct primitive **orbits**, not their \(m\) points, and only for the integer doubling map. The fixed point at zero is of period one and does not enter \(P_m\).

A binary word is *primitive* if it is not a nontrivial power. Its unique smallest cyclic rotation is called its Lyndon representative; the periodically repeated binary word encodes a primitive orbit. All Lyndon representatives here contain both binary symbols.

## Proof

**1. Symbolic correspondence.** For any binary length-\(m\) word \(w\), the point with repeating binary expansion \(w\) is \(\operatorname{int}_2(w)/D\), and doubling acts by left cyclic rotation. Primitive necklaces give exactly the least-period-\(m\) orbits. Consequently the orbit's smallest point is represented by the lexicographically least cyclic rotation of \(w\), and that orbit survives exactly when its smallest point is at least \(t\).

**2. One and two zeros.** There is one necklace with exactly one zero, represented by \(0 1^{m-1}\), attaining \(a_m\). A necklace with exactly two zeros has cyclic gaps \(d,m-d\) between consecutive zeros. Its smallest rotation starts with the shorter gap, so each possible \(1\le d\le d_*\) gives exactly one primitive necklace \(w_{m,d}=0 1^{d-1}0 1^{m-d-1}\). The case of equal gaps (even \(m\) and \(d=m/2\)) is not primitive. Direct binary evaluation gives the exact \(b_{m,d}\), strictly increasing with \(d\) and strictly below \(a_m\).

**3. The three-zero maximizer.** Three zeros split the cyclic word into three positive zero-to-zero gaps whose sum is \(m\). If \(m\not\equiv0\pmod3\), the largest attainable minimum gap is \(\lfloor m/3\rfloor=e\). If \(m=3q\), equal gaps \((q,q,q)\) would be a nonprimitive cube, so the largest possible minimum gap is instead \(q-1=e\). For fixed minimum gap, binary lexicographic order of the *least* rotation is governed first by that gap (larger is better) and then by the next gap among rotations based at a shortest gap (larger is better). An elementary three-positive-integers comparison yields the maximizing gap patterns \((q-1,q+1,q)\), \((q,q,q+1)\), and \((q,q+1,q+1)\) in the respective congruence classes. The latter pattern beats the alternative \((q,q,q+2)\), since the alternative has two consecutive shortest gaps. Each chosen pattern is primitive. Therefore \(u_m\) is the lexicographically largest primitive Lyndon word of length \(m\) with exactly three zeros.

Here the general weight-monotonicity lemma of Kong–Pu (Lemma 3.3, cited below) is used only for words having four or more zeros: their largest Lyndon representative is strictly below the largest with three zeros. Hence \(u_m\) is also the largest *over all* primitive necklaces with at least three zeros. Its corresponding first-entry threshold is exactly \(\eta_m\).

**4. Sharp interleaving and count.** Every candidate \(u_m\) begins with a zero gap of length \(e\). Any two-zero word \(w_{m,d}\) with \(d<e\) begins with a shorter gap, so \(w_{m,d}<u_m\). For \(d=e\), both begin with the same shortest gap, but \(u_m\) contains a third zero at some position strictly earlier than the next zero of \(w_{m,e}\); hence \(u_m<w_{m,e}\). Thus \(b_{m,e-1}<\eta_m<b_{m,e}\) when \(e\ge2\), with the meaningful right inequality also when \(e=1\). By monotonicity of \(b_{m,d}\), exactly the indexed two-zero necklaces with \(d\ge e\) lie above \(\eta_m\); no necklace with at least three zeros does. The survival count follows, with sharpness at \(t=\eta_m\). The number of top thresholds and the geometric differences are immediate from the displayed exact formulas.

## Verification

Run \(\texttt{python3 verify.py}\) using only the Python standard library. The script enumerates primitive binary necklaces by exact integers for every length \(4\le m\le18\), verifies that the proposed entire leading block is correct and that the first additional orbit is exactly \(u_m\), and checks rational threshold inequalities. Output: \(\texttt{VERIFY\_OK lengths=4..18 exact\_primitive\_necklace\_orders=15 endpoint\_comparisons=86}\). This finite check corroborates the all-length proof; it does not prove it.

## Relationship to prior work

Kong and Pu (2026) study the largest hole permitting *any* period-\(m\) orbit for general \(\beta\), and their Theorem 3.1 determines an extremal Lyndon word within each fixed digit weight. Their Lemma 3.3 establishes monotonicity of the **weight-constrained maxima**. The present statement instead orders a growing initial block of *all* primitive period-\(m\) necklaces across weights and gives the complete count between consecutive hole thresholds. The one-zero leading threshold and the weight-three maximum are not separately claimed as novel. Standard Lyndon ranking algorithms also give the entire order computationally, but not the displayed uniform formula for a linearly growing leading block.

## Limitations

No formula is claimed for every period-\(m\) orbit below \(\eta_m\), or for noninteger \(\beta\), or for a hole not anchored at zero. This is a closed-form partial census, not a full periodic-orbit zeta or entropy classification. Originality depends on the distinction between fixed-weight extremal results and the cross-weight complete leading sequence; unpublished equivalents are a remaining risk.

## References

1. D. Kong and D. Pu, *Phase transitions on periodic orbits in \(\beta\)-transformation with a hole at zero*, arXiv:2602.05438, first posted 2026-02-05. https://arxiv.org/abs/2602.05438 . See Theorem 3.1 and Lemma 3.3.
2. T. Kociumaka, J. Radoszewski, and W. Rytter, *Efficient Ranking of Lyndon Words and Decoding Lexicographically Minimal de Bruijn Sequence*, arXiv:1510.02637 (2015). https://arxiv.org/abs/1510.02637 .
3. D. Gabric and J. Sawada, *Necklaces and Lyndon words in colexicographic order*, arXiv:2607.05324, first posted 2026-07-06. https://arxiv.org/abs/2607.05324 .
