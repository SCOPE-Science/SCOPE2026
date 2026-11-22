# Exact \(19\)-adic Fibonacci residue fibers and a singular square branch

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). For each integer \(k\ge1\) and residue \(y\in\mathbb Z/19^k\mathbb Z\), let
\[
N_k(y)=\#\{0\le n<18\cdot19^{k-1}:F_n\equiv y\pmod{19^k}\}.
\]
The indicated interval is one **least** period modulo \(19^k\). Define \(w:\mathbb Z/19\mathbb Z\to\mathbb Z_{\ge0}\) by
\[
\begin{array}{c|rrrrrrrrrrrr}
a&0&1&2&3&5&8&11&13&15&16&17&18\\ \hline
w(a)&1&3&3&1&2&1&1&2&0&1&1&1
\end{array}
\]
and put \(w(a)=0\) at all other residues. There is a unique \(19\)-adic integer \(c\) satisfying \(5c^2=4\) and \(c\equiv15\pmod{19}\); in particular \(c\equiv34\pmod{19^2}\). For a modulus \(M\) and residue \(z\), let \(R_M(z)=\#\{x\bmod M:x^2\equiv z\pmod M\}\), with \(R_1(0)=1\).

At level \(k=1\),
\[
N_1(y)=w(y)+\mathbf1_{y=15}.
\]
For every \(k\ge2\), the complete target-by-target fiber law is
\[
\boxed{N_k(y)=w(y\bmod19)+
\begin{cases}
19\,R_{19^{k-2}}\!\left(\dfrac8c\dfrac{y-c}{19^2}\right), &y\equiv c\pmod{19^2},\\[4pt]
0,&\text{otherwise}.
\end{cases}}
\]
The argument of \(R\) is interpreted modulo \(19^{k-2}\) (the quotient is well-defined because of the congruence). At \(k=2\), this argument is modulo one. Consequently, the image size \(I_k=\#\{F_n\bmod19^k:n\ge0\}\) equals \(12\) when \(k=1\), and for \(k\ge2\),
\[
\boxed{I_k=11\cdot19^{k-1}+Q_{19}(k-2)},\qquad
Q_{19}(d)=\#\{x^2\bmod19^d:x\in\mathbb Z\}.
\]
Here \(Q_{19}(0)=1\), while for \(d\ge1\),
\[
Q_{19}(d)=1+9\sum_{s=0}^{\lfloor(d-1)/2\rfloor}19^{d-2s-1}.
\]
The maximum number of occurrences of any single residue within one least period is exactly \(3\) for \(k=1\), and
\[
\boxed{\max_y N_k(y)=\begin{cases}19^{k/2},&k\ge2\text{ even},\\2\cdot19^{(k-1)/2},&k\ge3\text{ odd}.\end{cases}}
\]
In particular, the maximum fiber is unbounded even though the total image density tends to the previously known value \(441/760\). The image sizes begin \(12,210,3981,75621\) and the largest fibers begin \(3,19,38,361\).

## Assumptions and scope

All periods and fiber counts are for the ordinary Fibonacci sequence with indices \(n\ge0\), including the zero index. The modulus is exactly a positive power of the prime \(19\); these statements do not assert any analogous law at other primes. The \(19\)-adic center \(c\) is specified by a Hensel condition rather than by an ordinary integer. We distinguish the previously known image sizes and limiting density from the new targetwise multiplicity law and exact growing maximum.

## Proof

**Exact period and regular branches.** Let \(A=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\). Then
\[
A^{18}=I+19B,\qquad B=\begin{pmatrix}220&136\\136&84\end{pmatrix},
\]
by the exact Fibonacci values \(F_{17}=1597\), \(F_{18}=2584\), \(F_{19}=4181\). Since \(B\not\equiv0\pmod{19}\), binomial lifting gives
\[
\nu_{19}(A^{18m}-I)=1+\nu_{19}(m)\quad(m\ge1),
\]
where the valuation of a matrix is the minimum entry valuation. The base period modulo \(19\) is \(18\), as direct evaluation of \(A^d\pmod{19}\) for the proper divisors \(d=1,2,3,6,9\) of \(18\) confirms. Thus the least period modulo \(19^k\) is \(18\cdot19^{k-1}\).

For every \(r\in\{0,\ldots,17\}\), define the \(19\)-adic analytic interpolation
\[
f_r(t)=(A^r(I+19B)^t)_{12},\qquad t\in\mathbb Z_{19},
\]
using the convergent matrix logarithm/exponential, so \(f_r(t)=F_{r+18t}\) for nonnegative integers \(t\). Since the logarithm of \(I+19B\) is \(19B+19^2\) times an integral matrix, the Taylor expansion in \(t\) yields
\[
f_r(t)=F_r+19\big(a_rt+19h_r(t)\big),\qquad
a_r\equiv (A^rB)_{12}\equiv3F_{r+1}+8F_r\pmod{19},
\]
where \(h_r:\mathbb Z_{19}\to\mathbb Z_{19}\) is \(1\)-Lipschitz. Reduction gives \(a_9\equiv0\pmod{19}\), and \(a_r\not\equiv0\pmod{19}\) for each other \(r\). (These assertions follow by the eighteen-term Fibonacci recurrence; the attached checker independently computes these base data.) For each \(r\ne9\), the map \(t\mapsto(f_r(t)-F_r)/19\) is therefore an isometry and a bijection of \(\mathbb Z_{19}\), so \(f_r\) maps onto \(F_r+19\mathbb Z_{19}\), with precisely one index per admissible target modulo \(19^k\) as \(t\) ranges modulo \(19^{k-1}\). Counting the seventeen regular indices by \(F_r\bmod19\) gives exactly the table \(w\).

**The singular branch.** The Lucas sequence \(L_0=2\), \(L_1=1\), \(L_{n+2}=L_{n+1}+L_n\) satisfies \(L_n=\operatorname{tr}(A^n)\). Set
\[
\ell(t)=\frac{\operatorname{tr}(A^9(I+19B)^t)}{19}.
\]
The numerator is divisible by \(19\) for all \(t\in\mathbb Z_{19}\), since \(L_9=76\). Moreover,
\[
\ell(t)=4+8t+19h(t),
\]
for a \(1\)-Lipschitz integral analytic \(h\): indeed, \(\operatorname{tr}(A^9B)\equiv8\pmod{19}\) after division of the linear term by \(19\). Thus \(\ell\) is an isometric bijection of \(\mathbb Z_{19}\).

Every integer \(9+18t\) is odd, so the classical identity \(L_n^2-5F_n^2=4(-1)^n\) gives \(5f_9(t)^2=4+19^2\ell(t)^2\). Let \(c\) be the unique root of \(5c^2=4\) congruent to \(F_9=34\pmod{19}\), guaranteed by Hensel's lemma because \(10c\) is a unit. The sign is fixed by the residue modulo \(19\), and hence
\[
f_9(t)=c\sqrt{1+\frac{19^2}{4}\ell(t)^2}.
\]
All square roots here are the unique ones congruent to \(1\pmod{19}\) for their unit arguments. Define
\[
G(x)=x\sqrt{\frac{2}{1+\sqrt{1+19^2x^2/4}}}.
\]
Then \(G(x)=x+19^2H(x)\) for a \(1\)-Lipschitz integral analytic function \(H\), hence \(G\) is an isometric bijection of \(\mathbb Z_{19}\). Rationalizing the preceding square root proves the **exact singular normal form**
\[
\boxed{f_9(t)=c+\frac{19^2c}{8}\big(G(\ell(t))\big)^2.}
\]
Since \(G\circ\ell\) is a bijective isometry, reducing it modulo \(19^{k-1}\) makes its values run once through all classes at that precision. For \(k\ge2\), the condition \(f_9(t)\equiv y\pmod{19^k}\) is therefore equivalent to \(x^2\equiv\frac8c\frac{y-c}{19^2}\pmod{19^{k-2}}\), when \(y\equiv c\pmod{19^2}\); each square root modulo \(19^{k-2}\) has exactly \(19\) lifts to the index modulus \(19^{k-1}\). If that congruence on \(y\) fails there are no solutions. At \(k=1\), this branch gives one occurrence of the class \(15\). The regular branches never meet the singular one, because no regular \(F_r\) is congruent to \(15\pmod{19}\). This proves the full fiber formula.

**Counting fibers.** Every nonzero square modulo \(19^d\) has even valuation \(2s<d\) and a quadratic-residue unit after dividing by \(19^{2s}\). Thus there are \(9\cdot19^{d-2s-1}\) attainable targets of such valuation, each with \(2\cdot19^s\) roots. Zero contributes one target with \(19^{\lfloor d/2\rfloor}\) roots. This gives the formula for \(Q_{19}\), the image counts, and the stated maximum multiplicities. The published limiting density \(441/760\) is recovered by letting \(k\to\infty\), but its priority is not claimed.

## Verification

Run `python3 CHECK.py` with Python 3 and no external packages. It evaluates a full least period directly from the Fibonacci recurrence modulo \(19^k\) for \(k=1,2,3,4\), compares every target's observed multiplicity with a separately constructed square-root-count formula, and checks that no proper prime-divisor reduction of the claimed period is a period. The four verified moduli are \(19\), \(361\), \(6859\), and \(130321\), with respectively \(18\), \(342\), \(6498\), and \(123462\) index values. These finite checks corroborate, but do not replace, the infinite proof.

## Relationship to prior work

Bragman and Rowland (first public arXiv source 2022-02-01) already identify the limiting image density at \(19\) as \(441/760\), list the first finite image sizes in their Example 3, and provide general regular/singular image arguments in Propositions 24 and 27. Rowland and Yassawi (2016 preprint, 2017 journal) establish the interpolation approach and study the analogous image-density phenomenon at \(11\). Neither inspected primary result gives the present **per-target multiplicities inside the exact least periods**, their singular square-coordinate normal form in explicit Fibonacci/Lucas coordinates at \(19\), or the maximum-fiber growth law. The new classification builds on, rather than replaces, the published \(19\)-adic image descriptions. Bundschuh and Bundschuh already studied complete targetwise frequencies modulo powers of 3; these results concern a different prime. Classical recurrence residue-distribution literature also addresses modular frequencies, but the accessible Somer (1990) abstract is about prime modulus and was not enough to certify absence of every possible implicit refinement.

## Limitations

This result is restricted to prime \(19\); the density and image-size observations were known and are used only for consistency checks. The exact fiber theorem relies on a local isometric-coordinate argument at the one Lucas-zero index. Neither finite exhaustive verification nor indexed searches certify global publication priority. An unseen weighted refinement of earlier interpolation results could imply some of these formulas. No independent mathematical audit has been performed.

## References

- N. Bragman and E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, arXiv:2202.00704, first posted 2022-02-01; *Research in Number Theory* 11 (2025), article 88, DOI 10.1007/s40993-025-00667-1. https://arxiv.org/pdf/2202.00704
- E. Rowland and R. Yassawi, *p-adic asymptotic properties of constant-recursive sequences*, arXiv:1602.00176, first posted 2016-01-31; *Indagationes Mathematicae* 28 (2017), 205–220. https://arxiv.org/abs/1602.00176
- R. Bundschuh and P. Bundschuh, *Distribution of Fibonacci and Lucas Numbers Modulo 3^k*, *Fibonacci Quarterly* 49 (2011), 201–210, DOI 10.1080/00150517.2011.12428042 (abstract examined).
- L. Somer, *Distribution of Residues of Certain Second-Order Linear Recurrences Modulo P*, in *Applications of Fibonacci Numbers* (1990), 311–324, DOI 10.1007/978-94-009-1910-5_34 (abstract examined only).
