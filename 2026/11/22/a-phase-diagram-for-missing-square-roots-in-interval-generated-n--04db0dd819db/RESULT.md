# A phase diagram for missing square roots in interval-generated numerical semigroups

## Finding

For integers \(a\ge2\) and \(k\ge1\), let \(S_{a,k}=\langle a,a+1,\ldots,a+k\rangle\) and let \(G(a,k)\) be the number of **positive integers** \(n\) for which \(n^2\notin S_{a,k}\). Write \(Q=\lceil a/k\rceil-1\). Then the following is an **exact formula valid for every pair**:
\[
G(a,k)=\sum_{q=0}^{Q}\left(\left\lceil\sqrt{(q+1)a}\right\rceil-1-\left\lfloor\sqrt{q(a+k)}\right\rfloor\right).\tag{1}
\]

Define the continuous function \(F:(0,\infty)\to\mathbb R\) by
\[
F(t)=\sum_{q=0}^{\lfloor1/t\rfloor}\left(\sqrt{q+1}-\sqrt{(1+t)q}\right)_+,\qquad (z)_+=\max(z,0).\tag{2}
\]
For **all** \(a\ge2,k\ge1\), with \(t=k/a\), the following uniform approximation holds:
\[
\left|G(a,k)-\sqrt a\,F(k/a)\right|\le\lceil a/k\rceil.\tag{3}
\]
If \(k=k(a)\) satisfies \(k/a\to\theta>0\), then \(G(a,k)/\sqrt a\to F(\theta)\). In particular, for \(k=\lfloor\theta a\rfloor\) with fixed \(\theta>0\) (and positive \(k\)), the error is \(O_\theta(1)\).

The function \(F\) equals \(1\) for \(t\ge1\). On each interval \(1/(j+1)<t<1/j\), where \(j\ge1\), it has the explicit expression
\[
F(t)=\sqrt{j+1}+\bigl(1-\sqrt{1+t}\bigr)\sum_{q=1}^{j}\sqrt q.\tag{4}
\]
It is continuous, decreasing, piecewise analytic, and its derivative has a positive jump of precisely \(j/(2\sqrt{j+1})\) at each \(t=1/j\). Thus all reciprocal integers are genuine, distinct first-derivative phase transitions.

At the mesoscopic scales \(k\to\infty\) and \(k/a\to0\), the counts obey the further law
\[
G(a,k)=\frac{2a}{3\sqrt k}+O\left(\sqrt k+\frac ak\right)\sim\frac{2a}{3\sqrt k}.\tag{5}
\]
The absolute implied constant in (5) is universal. Formula (5) is not claimed to provide an asymptotic when \(k\) stays fixed.

More strongly, the missing-square **roots have a universal limit profile throughout the mesoscopic regime**. For \(0\le s\le1\), put
\[
G(a,k;s)=\#\{n\ge1:n\le s a/\sqrt k,\ n^2\notin S_{a,k}\}.
\]
For every \(1\le k\le a\), uniformly in \(0\le s\le1\),
\[
G(a,k;s)=\frac a{\sqrt k}\left(s-\frac{s^3}{3}\right)+O\left(\sqrt a+\frac ak\right).\tag{6}
\]
Consequently, when \(k\to\infty\) and \(k/a\to0\), the normalized counting measures of the rescaled roots \(n\sqrt k/a\) converge to the measure with density \(1-s^2\) on \([0,1]\). Its total mass is \(2/3\), not \(1\).

## Assumptions and scope

The generators are the entire integer interval from \(a\) to \(a+k\); no coprimality assumption beyond consecutiveness is needed. Square roots \(n\) are positive integers, not square values \(n^2\). The special case \(k\ge a\) has the exact value \(G(a,k)=\lfloor\sqrt{a-1}\rfloor\), agreeing with the plateau \(F(t)=1\). A finite error bound for fixed \(a,k\), an asymptotic along growing \(k\), and a proportional-width limit are distinct statements.

## Proof

**1. Exact membership and gap intervals.** Every nonnegative integer \(m\) has a unique decomposition \(m=qa+r\), where \(q\ge0\) and \(0\le r<a\). The interval-generated semigroup satisfies
\[
m\in S_{a,k}\quad\Longleftrightarrow\quad r\le kq.\tag{7}
\]
Indeed, if \(r\le kq\), distribute \(r\) among \(q\) offsets from \(\{0,1,\dots,k\}\) and add the corresponding \(q\) generators. Conversely, any representation of \(m\) as a sum of \(s\) generators has the form \(m=sa+T\), with \(0\le T\le ks\). As \(q=\lfloor m/a\rfloor\ge s\), we obtain \(r=T-(q-s)a\le T\le ks\le kq\).

Putting \(m=n^2\), equation (7) yields
\[
n^2\notin S_{a,k}\quad\Longleftrightarrow\quad q(a+k)<n^2<(q+1)a,\qquad q=\lfloor n^2/a\rfloor.\tag{8}
\]
Such intervals exist only if \(qk<a\), i.e., \(0\le q\le Q=\lceil a/k\rceil-1\). The intervals are pairwise disjoint because each lies in its own quotient block. For integer endpoints \(L<R\), the number of positive integer roots \(n\) satisfying \(L<n^2<R\) is \(\lceil\sqrt R\rceil-1-\lfloor\sqrt L\rfloor\). In (8), \(L=q(a+k)\), \(R=(q+1)a\), proving (1).

**2. A uniform boundary estimate.** For any real \(u<v\) with \(u\ge0\), the number of integers in \((u,v)\) differs from \(v-u\) by at most \(1\). Applying this to the square-root intervals in (8) gives
\[
G(a,k)=\sqrt a\sum_{q=0}^{Q}\bigl(\sqrt{q+1}-\sqrt{(1+k/a)q}\bigr)+E,\qquad |E|\le Q+1=\lceil a/k\rceil.\tag{9}
\]
The terms are nonnegative for \(q\le Q\); every additional term through \(\lfloor a/k\rfloor\) is zero when that endpoint is integral. Thus the sum is precisely \(F(k/a)\). This proves (3).

**3. The proportional-width limit and corners.** On a fixed compact subinterval of \((0,\infty)\), only finitely many terms in (2) can be nonzero. Each is continuous, so \(F\) is continuous and locally Lipschitz. If \(k/a\to\theta>0\), the right side of (3) is \(O_\theta(1)\), proving the limit. The same Lipschitz property yields the stated \(O_\theta(1)\) error for \(k=\lfloor\theta a\rfloor\).

For \(1/(j+1)<t<1/j\), precisely \(q=0,\ldots,j\) contribute. Telescope the first square-root sum to obtain (4), and differentiate. On the left of \(t=1/j\), the sum contains \(\sqrt j\); on the right it does not. Therefore
\[
F'_+(1/j)-F'_-(1/j)=\frac{\sqrt j}{2\sqrt{1+1/j}}=\frac{j}{2\sqrt{j+1}}>0.\tag{10}
\]
The endpoint formulas match because the disappearing summand vanishes there, and \(F(t)=1\) for \(t\ge1\). In particular, these are genuine derivative discontinuities, not artifacts of writing the sum piecewise.

**4. Mesoscopic asymptotics.** Put \(J=\lfloor1/t\rfloor\). As \(t\downarrow0\), elementary integral comparison (or summation by parts) gives
\[
\sum_{q=1}^J\sqrt q=\frac23J^{3/2}+O(\sqrt J),\qquad J=t^{-1}+O(1).\tag{11}
\]
Using \(\sqrt{1+t}-1=t/2+O(t^2)\) and formula (4), we obtain \(F(t)=2/(3\sqrt t)+O(\sqrt t)\). Substitution into (3) yields (5), because \(\sqrt a\sqrt{k/a}=\sqrt k\) and \(\lceil a/k\rceil\le a/k+1\). Both error terms are \(o(a/\sqrt k)\) exactly in the stated regime \(k\to\infty\), \(k/a\to0\).

**5. A uniform root-counting profile.** Write \(L=a/\sqrt k\) and fix \(s\in[0,1]\). Let \(N=\lfloor sL\rfloor\) and \(J=\lfloor N^2/a\rfloor\). Every gap interval with quotient \(q<J\) is counted in full, while at most the interval with \(q=J\) is truncated. Each such interval has width at most \(\sqrt a\) in the root variable. Applying the integer-point error estimate from step 2 to the full intervals, and including the truncated interval at an additional cost at most \(\sqrt a+1\), gives
\[
G(a,k;s)=\sqrt a\left(\sqrt{J+1}-(\sqrt{1+t}-1)\sum_{q=1}^{J}\sqrt q\right)+O(J+\sqrt a),\qquad t=k/a.\tag{12}
\]
Here \(J=s^2/t+O(1)\) uniformly in \(s\), because \(N=sL+O(1)\) and \(L/a=1/\sqrt k\le1\). Thus
\[
\sqrt a\sqrt{J+1}=Ls+O(\sqrt a).
\]
Using the same square-root sum estimate as in (11), uniformly even for \(J=0\), gives
\[
\sqrt a(\sqrt{1+t}-1)\sum_{q=1}^{J}\sqrt q=\frac{Ls^3}{3}+O(\sqrt k).
\]
Since \(J\le a/k\) and \(\sqrt k\le\sqrt a\), (12) proves (6). Dividing by \(L\) yields the uniform error \(O(\sqrt{k/a}+1/\sqrt k)\), which tends to zero in the mesoscopic regime. The derivative of the limiting cumulative count is \(1-s^2\), proving the root-profile statement. This finishes the proof. \(\square\)

## Verification

The standalone `check.py` verifies (1) against independent coin-change dynamic programming for a broad finite grid of \((a,k)\), checks the uniform inequality (3) numerically at larger parameters, and checks samples of the cumulative root-profile formula (6). Its output can be regenerated using `python check.py`. Enumeration does not establish any infinite assertion; the proof above does.

## Relationship to prior work

Ramírez Alfonsín (2007/2008), *Gaps in semigroups*, Theorem 1.1, gives the complete ordinary gap list of \(\langle a,\dots,a+k\rangle\). Chappelon and Ramírez Alfonsín (2020), *The Square Frobenius Number*, Lemma 2.2, gives the general arithmetic-progression membership criterion used here, and the article investigates the **largest** missing square, not the full square-root counting function. Binner (2021), *Proofs of Chappelon and Alfonsín Conjectures ...*, proves the missing-square maximum conjectures and includes an equivalent membership test for \(k=1\). The available 2026 square-gap root-profile result for \(\langle a,a+1\rangle\) proves the sharper fixed-width \(k=1\) law \(G(a,1)=2a/3+O(a^{5/6}\log(2a))\); it neither states nor implies the infinite derivative-jump diagram in the regime \(k/a\to\theta>0\). The contribution claimed here is **only** the uniform all-width square-root count, its two-parameter asymptotic phase diagram, and the mesoscopic root-distribution limit (6). The known exact gap/membership formulas are explicitly credited, and no improvement in the fixed-width \(k=1\) error is claimed.

## Limitations

The error \(O(a/k)\) from integer rounding can be comparable to the main term when \(k\) is fixed; no fixed-width asymptotic follows from this theorem. The \(k=1\) profile is already known with a stronger error bound; the new profile assertion concerns diverging \(k\). Other equivalent enumerations or unpublished work may exist. The phase law concerns root counts, not the total genus, the largest square gap, or all possible arithmetic-progression steps \(d>1\). Independent scientific audit has not been performed.

## References

1. J. L. Ramírez Alfonsín, *Gaps in semigroups*, Discrete Mathematics **308** (2008), 4177–4184; available author manuscript: https://imag.umontpellier.fr/~ramirez/gaps.pdf
2. J. Chappelon and J. L. Ramírez Alfonsín, *The Square Frobenius Number*, arXiv:2006.14219 (first posted 25 June 2020), https://arxiv.org/abs/2006.14219 ; author PDF https://imag.umontpellier.fr/~ramirez/SquareFrobeniusNumber_Final.pdf
3. D. S. Binner, *Proofs of Chappelon and Alfonsín Conjectures On Square Frobenius Numbers and its Relationship to Simultaneous Pell's Equations*, arXiv:2112.15474 (first posted 31 December 2021), https://arxiv.org/abs/2112.15474
4. *Universal square-gap root profile for consecutive-generator numerical semigroups*, accessible mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-universal-square-gap-root-profile-for-consecutive-generator-nume--f45c31acfd04/RESULT.md
