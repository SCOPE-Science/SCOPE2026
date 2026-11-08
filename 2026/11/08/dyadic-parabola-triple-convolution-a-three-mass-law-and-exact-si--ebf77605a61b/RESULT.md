# Dyadic parabola triple convolution: a three-mass law and exact sixth Fourier moment

## Finding

For every integer \(k\ge1\), let \(N=2^k\) and \(P_N=\{(x,x^2):x\in\mathbb Z/N\mathbb Z\}\). Define the **ordered, unnormalized** threefold convolution
\[
r_N(s,t)=\#\{(x,y,z)\in(\mathbb Z/N\mathbb Z)^3:x+y+z=s,\ x^2+y^2+z^2=t\}.
\]
Write \(h=3^{-1}s\pmod N\). If \(t-3h^2\) is odd then \(r_N(s,t)=0\). If it is even, put \(m=k-1\), and let \(c\in\mathbb Z/2^m\mathbb Z\) be the unique residue satisfying \(2c=t-3h^2\pmod N\). Set \(v_2(0)=+\infty\) and use truncated \(2\)-adic valuation on nonzero residues. Then
\[
r_N(s,t)=
\begin{cases}
2N,&c=0,\ k\text{ odd},\\
N,&c=0,\ k\text{ even},\\
3N,&c\ne0,\ v_2(c)\text{ even},\\
0,&c\ne0,\ v_2(c)\text{ odd}.
\end{cases}
\]
For \(k=1\) there are no nonzero residues \(c\), and the same rule applies. Thus, for \(k\ge2\), the only positive convolution values are \(3N\) and \(N\) (even \(k\)) or \(2N\) (odd \(k\)).

**Complete multiplicity distribution** (the counts are numbers of targets \((s,t)\)):
\[
\begin{array}{c|ccc}
& r_N=0 &r_N=3N&r_N=\text{exceptional}\\\hline
k\text{ even}&2N(N-1)/3&N(N-1)/3&N\text{ targets with value }N\\
k\text{ odd}&N(2N-1)/3&N(N-2)/3&N\text{ targets with value }2N.
\end{array}
\]
In particular,
\[
|P_N+P_N+P_N|=
\begin{cases}
N(N+2)/3,&k\text{ even},\\
N(N+1)/3,&k\text{ odd}.
\end{cases}
\]
The proportion of attainable targets tends to \(1/3\) through either parity of \(k\).

Define the unnormalized Fourier sum \(G_N(a,b)=\sum_{x\bmod N}\exp(2\pi i(ax+bx^2)/N)\). Its complete constant-coefficient sixth moment is
\[
\boxed{\frac1{N^2}\sum_{a,b\bmod N}|G_N(a,b)|^6=N^3(3N-2).}
\]

## Assumptions and scope

All congruences, target counts, and Fourier sums are over the **cyclic ring** \(\mathbb Z/2^k\mathbb Z\). Variables \(s,t,x,y,z\) range independently over its residue classes; triples are ordered. The statements hold for all \(k\ge1\), including \(N=2\). Neither finite fields of characteristic two nor arbitrary weights on \(P_N\) are claimed.

## Proof

**Step 1: Reduction to a binary quadratic norm.** Since \(3\) is a unit modulo \(N\), for each fixed \(s\) every triple with sum \(s\) can be written uniquely as
\[
(x,y,z)=(h+a,h+b,h-a-b),\quad h=3^{-1}s.
\]
Direct expansion gives
\[
x^2+y^2+z^2=3h^2+2Q(a,b),\qquad Q(a,b)=a^2+ab+b^2.
\]
Thus \(r_N(s,t)=0\) unless \(t-3h^2\) is even. In the even case, \(Q(a,b)=c\pmod{2^{k-1}}\). Each solution of this last congruence modulo \(2^{k-1}\) has precisely four lifts \((a,b)\) modulo \(2^k\), so
\[
r_N(s,t)=4R_m(c),\qquad R_m(c)=\#\{(a,b)\bmod2^m:Q(a,b)=c\},\quad m=k-1.
\]
For \(m=0\), the ring has one element and \(R_0(0)=1\).

**Step 2: Exact norm fibers.** The key observation is that \(Q(a,b)\equiv1\pmod2\) whenever at least one of \(a,b\) is odd, whereas \(Q(a,b)\equiv0\pmod4\) when both are even. Consequently,
\[
v_2(Q(a,b))=2\min\{v_2(a),v_2(b)\}
\]
whenever \(Q(a,b)\not\equiv0\pmod{2^m}\), where the valuations are truncated at \(m\). If \(c\ne0\) has odd valuation, \(R_m(c)=0\).

For every odd \(u\bmod2^\ell\), the equation \(Q(a,b)=u\pmod{2^\ell}\) has exactly \(3\cdot 2^{\ell-1}\) solutions: at modulus two all three nonzero pairs solve it; at every higher level exactly two of the four lifts of each pair solve the target congruence. Indeed, its gradient \((2a+b,a+2b)\) reduces to \((b,a)\pmod2\), nonzero at every primitive pair. This establishes the lifting count by induction.

If \(v_2(c)=2j<m\), write \((a,b)=2^j(u,v)\). The primitive pair \((u,v)\) is taken modulo \(2^{m-j}\) while its norm is constrained modulo \(2^{m-2j}\). The fiber therefore has
\[
R_m(c)=2^{2j}\cdot3\cdot2^{m-2j-1}=3\cdot2^{m-1}
\]
solutions. Finally \(Q(a,b)\equiv0\pmod{2^m}\) if and only if both coordinates are divisible by \(2^{\lceil m/2\rceil}\), giving
\[
R_m(0)=2^{2\lfloor m/2\rfloor}.
\]
Substitution in \(r_N=4R_m\) proves the pointwise formula, including the exceptional parity factor.

**Step 3: Every multiplicity.** Fix \(s\). The map \(c\mapsto t=3h^2+2c\pmod N\) identifies the \(2^{k-1}\) possible \(c\)'s with precisely the \(t\)'s having the necessary parity. For \(m\ge1\), the number of nonzero residues of even valuation is
\[
A_m=\sum_{0\le j<m/2}2^{m-2j-1}=
\begin{cases}
(2^m-1)\,2/3,&m\text{ even},\\
(2^{m+1}-1)/3,&m\text{ odd}.
\end{cases}
\]
For \(m=0\), this number is zero. In terms of \(N\), \(A_{k-1}=(N-2)/3\) for odd \(k\) and \(A_{k-1}=(N-1)/3\) for even \(k\). Thus, for each of the \(N\) choices of \(s\), exactly \(A_{k-1}\) targets have count \(3N\), exactly one target has the exceptional positive count, and all other targets have count zero. Counting all \(N^2\) targets yields the table and sumset size. These formulas also hold at \(k=1\).

**Step 4: Sixth moment.** With counting convolution and the above Fourier convention, Parseval gives
\[
\sum_{s,t\bmod N}r_N(s,t)^2=\frac1{N^2}\sum_{a,b\bmod N}|G_N(a,b)|^6.
\]
For even \(k\) the left side equals \(N\cdot[N^2+9N^2(N-1)/3]\); for odd \(k\) it equals \(N\cdot[4N^2+9N^2(N-2)/3]\). Both expressions simplify to \(N^3(3N-2)\).

## Verification

The standalone file `verify_dyadic_parabola.py` uses only Python's standard library. It independently enumerates every ordered triple and tests every target and multiplicity for exponents \(1\le k\le7\). It separately evaluates all Fourier sums by direct complex arithmetic for \(1\le k\le6\), confirming the sixth moment numerically with relative tolerance \(10^{-9}\). These finite checks corroborate but do not substitute for Steps 1–4, which prove the all-exponent claim.

## Relationship to prior work

Mockenhaupt–Tao developed finite-field restriction theory in odd characteristic [1]. Tóth presents general counts of diagonal quadratic congruences, including some dyadic cases [2]; the binary form \(a^2+ab+b^2\) is not an integral diagonal specialization of those stated formulas. Hickman–Wright analyze restriction and congruence solution bounds for moment curves on residue rings; their two-coordinate treatment includes odd-modulus results but not the present dyadic threefold histogram [3]. González-Riquelme–Oliveira e Silva compute threefold convolution for prime-field parabolas when the characteristic exceeds three [4]; their formula does not cover these rings. The norm-fiber lifting lemma is elementary and not presented as a new standalone theorem. The assessed contribution is its exact application to the complete dyadic parabolic triple-convolution distribution and the consequent all-level Fourier moment identity.

## Limitations

This is an unweighted counting result. It does **not** determine the sharp \(L^2\to L^6\) extension norm for arbitrary coefficients, or any statement over general even moduli that are not powers of two. The explicit binary quadratic norm count may also be deducible from older general local-density results; a fully exhaustive historical-priority search has not been performed. No independent mathematical validation has been performed.

## References

1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234 (first posted 2002-04-18), https://arxiv.org/abs/math/0204234.
2. L. Tóth, *Counting Solutions of Quadratic Congruences in Several Variables Revisited*, Journal of Integer Sequences **17** (2014), Article 14.11.6, arXiv:1404.4214, https://arxiv.org/abs/1404.4214.
3. J. Hickman and J. Wright, *The Fourier Restriction and Kakeya Problems over Rings of Integers Modulo N*, Discrete Analysis **2018**:11, arXiv:1801.03176, https://arxiv.org/abs/1801.03176.
4. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, Proposition 3.3 (first posted 2024-05-26), https://arxiv.org/abs/2405.16647.
