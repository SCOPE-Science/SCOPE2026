# Cube–segment joins lose Ehrhart positivity exactly at cube dimension seventeen

## Finding

Let \(d\) be a positive integer, let \(C_d=[0,1]^d\), and let \(I=[0,1]\). Form the standard lattice join
\[
J_d=\operatorname{conv}\bigl(\{(x,0,1):x\in C_d\}\cup\{(0,y,0):y\in I\}\bigr)\subset\mathbb R^{d+2}.
\]
Then **the Ehrhart polynomial of \(J_d\) has all coefficients strictly positive if and only if \(1\le d\le16\)**. At the first failure, \(d=17\), only its linear coefficient is negative, and that coefficient equals \(-30301/798\). For every \(d\ge18\), at least one explicitly specified coefficient is negative.

Thus the standard, *undilated* unit cube and unit segment cease to preserve Ehrhart positivity under the lattice join exactly when the cube has dimension seventeen (the join then has dimension nineteen).

## Assumptions and scope

The ambient lattice is \(\mathbb Z^{d+2}\), the join is the lattice join displayed above, and the Ehrhart polynomial is \(L_d(t)=\#(tJ_d\cap\mathbb Z^{d+2})\) for nonnegative integers \(t\). Ehrhart positivity means strict positivity of every coefficient of \(L_d(t)\) in the ordinary monomial basis. No assertion is made for arbitrary lattice products, dilated cubes, or other kinds of convex free sums.

Write \(B_m\) for the **standard Bernoulli numbers**, with \(B_0=1\), \(B_1=-1/2\), and generating function \(z/(e^z-1)=\sum_{m\ge0}B_mz^m/m!\). Let \(B_m(x)\) be the corresponding Bernoulli polynomial.

## Proof

**1. Exact lattice count.** At integral join height \(h\in\{0,\ldots,t\}\), the cross-section of \(tJ_d\) consists of the cube \((t-h)C_d\) and the interval \(hI\), in independent coordinates. It therefore has \((t-h+1)^d(h+1)\) lattice points. Putting \(j=t-h\) gives
\[
L_d(t)=\sum_{j=0}^{t}(t-j+1)(j+1)^d.
\tag{1}
\]
Writing \(S_m(x)=\sum_{j=1}^{x}j^m\) for integer \(x\), polynomial continuation yields
\[
L_d(t)=(t+2)S_d(t+1)-S_{d+1}(t+1),\qquad
S_m(x)=\frac{B_{m+1}(x+1)-B_{m+1}(1)}{m+1}.
\tag{2}
\]

**2. Universal coefficient formula.** Write \(c_{d,k}=[t^k]L_d(t)\). For \(d\ge2\), equations (2) and \(B_m(2)=B_m+m\) for \(m\ge2\) yield
\[
c_{d,1}=d+2B_d-B_{d+1},\quad c_{d,d}=\frac{23}{12},\quad
c_{d,d+1}=\frac2{d+1},\quad
c_{d,d+2}=\frac1{(d+1)(d+2)},\quad c_{d,0}=1.
\tag{3}
\]
For \(2\le k\le d-1\), put \(r=d+2-k\), so \(3\le r\le d\). Directly extracting the two Bernoulli-polynomial coefficients in (2), then using \(B_{2m+1}=0\) for \(m\ge1\), gives
\[
c_{d,k}=\frac{(r-1)\binom{d+1}{k-1}}{k(d+1)}
\begin{cases}
r-B_r,&r\text{ even},\\[2pt]
r+\dfrac{2r}{r-1}B_{r-1},&r\text{ odd}.
\end{cases}
\tag{4}
\]
All prefactors are positive. For \(d=1\), (1) gives \(L_1(t)=1+11t/6+t^2+t^3/6\).

For clarity, the identity before the parity split in (4) is
\[
c_{d,k}=\frac{(r-1)\binom{d+1}{k-1}}{k(d+1)}
\left[-B_r(2)+\frac{2r}{r-1}B_{r-1}(2)\right].
\tag{5}
\]
This follows by expanding \((t+2)B_{d+1}(t+2)/(d+1)-B_{d+2}(t+2)/(d+2)\); its terms independent of \(t\) or linear in \(t\) do not affect \(k\ge2\). The binomial identity \(\binom{d+1}{k}/\binom{d+1}{k-1}=r/k\) gives (5).

**3. Positivity through dimension sixteen.** The only nonzero even Bernoulli numbers through order sixteen are
\[
\begin{array}{c|rrrrrrrr}
m&2&4&6&8&10&12&14&16\\\hline
B_m&1/6&-1/30&1/42&-1/30&5/66&-691/2730&7/6&-3617/510.
\end{array}
\tag{6}
\]
Every even \(r\in\{4,6,\ldots,16\}\) satisfies \(B_r<r\). Every odd \(r\in\{3,5,\ldots,15\}\) satisfies \(B_{r-1}>-(r-1)/2\). Thus all coefficients in (4) are strictly positive whenever \(d\le16\). Equation (3) gives positive high-degree coefficients. The linear coefficient in (3) is strictly positive for each \(2\le d\le16\): for even \(d\) it equals \(d+2B_d\), and for odd \(d\ge3\) it equals \(d-B_{d+1}\); (6) verifies both inequalities, including \(c_{16,1}=463/255>0\). The case \(d=1\) was explicit.

**4. Failure from dimension seventeen onward.** The standard value \(B_{18}=43867/798\) gives
\[
c_{17,1}=17-B_{18}=-\frac{30301}{798}<0.
\tag{7}
\]
For every \(d\ge18\), select the largest integer \(r\le d\) congruent to \(2\) modulo \(4\), with \(r\ge18\), and set \(k=d+2-r\). Then \(2\le k\le d-1\) and (4) shows that \(c_{d,k}<0\) provided \(B_r>r\).

The classical Euler identity for positive even indices is
\[
|B_{2m}|=\frac{2(2m)!\,\zeta(2m)}{(2\pi)^{2m}}.
\tag{8}
\]
For \(r\equiv2\pmod4\), \(B_r>0\). The base value above gives \(B_{18}>18\). For every such \(r\ge18\), (8) yields
\[
\frac{B_{r+4}/(r+4)}{B_r/r}
=\frac{r(r+1)(r+2)(r+3)}{(2\pi)^4}
\frac{\zeta(r+4)}{\zeta(r)}
>\frac{18\cdot19\cdot20\cdot21}{2\cdot7^4}>1,
\tag{9}
\]
using \(2\pi<7\), \(1<\zeta(r)<2\), and \(\zeta(r+4)>1\). Induction along \(r=18,22,26,\ldots\) establishes \(B_r>r\) for all required indices. Hence \(c_{d,k}<0\) for all \(d\ge18\). Together with (7), this completes the classification.

## Verification

The accompanying standalone \`verify.py\` implements (1) by integer lattice-slice sums and reconstructs the resulting polynomials with exact forward differences and rational arithmetic. It independently generates standard Bernoulli numbers by their triangular recurrence, checks (3)–(4) for dimensions through 32, evaluates the entire polynomials at the interpolation nodes, confirms strict positivity through dimension 16, the exact negative coefficient at 17, and the explicitly prescribed negative coefficients through 32. All 1,249 arithmetic checks pass. These finite checks do not prove the all-dimensional conclusion; the proof for all higher dimensions is (8)–(9).

## Relationship to prior work

Liu, Tao, and Xin (arXiv:2606.18794, Section 2, Theorem 2.3) prove that joining a sufficiently large integer dilation of *any* Ehrhart-positive lattice polytope of dimension at least four with an interval can destroy Ehrhart positivity. Their Example 2.4 uses a **one-hundred-fold dilation of a four-cube**. Their Proposition 1.2(iv) records multiplication of Ehrhart series under joins. None of those assertions determines when joins of *undilated* cubes with a unit segment cease being Ehrhart positive. Here the first failure instead occurs at cube dimension seventeen, and every larger cube dimension fails. The source's Bernoulli analysis concerns double sums of unshifted powers and does not give the complete positivity threshold for the shifted cube count (1).

Fu Liu's survey (arXiv:1711.09962v2, Sections 2.1 and 4) records the strict Ehrhart positivity of isolated unit cubes and classical nonpositive families; neither asserts positivity of their joins with unit intervals. The present result contrasts the factorwise positive Ehrhart polynomials with the dimension-dependent failure of their join.

## Limitations

The classification applies only to the standard lattice join of an *undilated* unit cube and a unit interval. The boundary dimension is the **cube factor's** dimension; the join has dimension two greater. It is not a minimal dimension among all possible counterexamples to join preservation. The proof is analytic with exact auxiliary arithmetic verification, not a formal proof assistant certificate. Historical priority beyond the inspected primary sources and targeted searches remains open to independent assessment.

## References

1. Feihu Liu, Sihao Tao, Guoce Xin, *Ehrhart Theory of the Join of Two Lattice Polytopes*, arXiv:2606.18794v1 (first submitted June 17, 2026), especially Definition 1.1, Proposition 1.2(iv), Theorem 2.3, and Example 2.4. https://arxiv.org/abs/2606.18794
2. Fu Liu, *On positivity of Ehrhart polynomials*, arXiv:1711.09962v2, especially Sections 2.1 and 4. https://arxiv.org/html/1711.09962v2
3. Classical Bernoulli-polynomial power-sum identity and Euler's formula for even Bernoulli numbers, as used explicitly in (2) and (8).
