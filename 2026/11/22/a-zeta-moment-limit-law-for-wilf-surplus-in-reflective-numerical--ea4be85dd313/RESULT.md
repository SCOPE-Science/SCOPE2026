# A zeta-moment limit law for Wilf surplus in reflective numerical semigroups

## Finding

Fix a positive integer \(g\). Let \(\mathcal R_g\) be the finite set of reflective numerical semigroups of genus \(g\), and choose \(S_g\) uniformly from this set. Put
\[
W(S)=e(S)\,\#\{s\in S:0\le s<c(S)\}-c(S),
\qquad c(S)=F(S)+1,
\]
where \(e(S)\) is the embedding dimension and \(F(S)\) the Frobenius number. This is the Wilf surplus, not merely a Boolean test of Wilf's inequality.

Define \(f:[0,1]\to[0,1]\) by \(f(0)=0\) and
\[
f(x)=x^2\lfloor1/x\rfloor\quad(0<x\le1).
\]
Then, with \(U\) uniform on \([0,1]\), the following hold:

1. **Limit law and rate.** \(W(S_g)/g^2\) converges in distribution to \(Y=f(U)\). For each fixed Lipschitz function \(\phi:[0,2]\to\mathbb R\),
   \[
   \left|\mathbb E\,\phi\!\left(\frac{W(S_g)}{g^2}\right)-\int_0^1\phi(f(x))\,dx\right|
   =O_\phi\!\left(\frac{1+\tau(g)}g\right),\quad g\to\infty,
   \]
   where \(\tau(g)\) counts positive divisors of \(g\).
2. **Exact distribution.** The law of \(Y\) has no atoms and has full topological support \([0,1]\). Its cumulative distribution function, for \(0\le t\le1\), is
   \[
   \mathbb P(Y\le t)=\sum_{q=1}^{\infty}
   \max\!\left\{0,\min\!\left(\frac1q,\sqrt{\frac tq}\right)-\frac1{q+1}\right\}.
   \]
   The series is a sum of nonnegative interval lengths.
3. **All positive integer moments.** For every integer \(m\ge1\),
   \[
   \mathbb E[Y^m]=\frac1{2m+1}\sum_{j=1}^{m}(-1)^{j+1}\binom mj\zeta(m+j+1).
   \]
   In particular, \(\mathbb E Y=\zeta(3)/3\), and \(\mathbb E Y^2=(2\zeta(4)-\zeta(5))/5\). The limiting variance is therefore \((2\zeta(4)-\zeta(5))/5-\zeta(3)^2/9>0\).

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid of the nonnegative integers. Its genus is its number of positive gaps. For positive genus \(g\), a semigroup is *reflective* when its \(g\) gaps occupy every residue class modulo \(g\) exactly once. Shor's classification [1] gives a one-to-one correspondence
\[
\mathcal R_g\longleftrightarrow\{a\in\mathbb Z:2\le a\le g+1,\ a\nmid g\},
\quad \#\mathcal R_g=g+1-\tau(g),
\]
where \(a\) is the multiplicity. The classification and the single-semigroup structural formulas below belong to [1]; the limit law, explicit distribution and zeta moments are the claims here.

## Proof

**1. A uniform approximation of the Wilf surplus.** Fix admissible \(a\). Set \(q=\lfloor g/a\rfloor\) and \(r=g-qa\), so \(1\le r<a\). By [1, Proposition 3.4 and Corollaries 3.6, 3.8],
\[
F(S)=2g-r,\qquad c(S)=2g-r+1,\qquad e(S)=\begin{cases}a,&r=a-1,\\a-1,&1\le r\le a-2.\end{cases}
\]
There are \(c(S)-g=qa+1\) non-gaps strictly below the conductor: among the \(c(S)\) nonnegative integers below it, exactly \(g\) are gaps. Therefore
\[
W(S)=\begin{cases}
qa(a-2),&r=a-1,\\
qa(a-3)+a-r-2,&1\le r\le a-2.
\end{cases}
\]
In the second case, the additive correction \(a-r-2\) is nonnegative. For \(a\le g\), both cases imply
\[
\left|\frac{W(S)}{g^2}-\left(\frac ag\right)^2\!\left\lfloor\frac ga\right\rfloor\right|\le\frac4g.
\]
The sole admissible value \(a=g+1\) has \(q=0\), \(r=a-1\) and \(W(S)=0\). Moreover all normalized values \(W(S)/g^2\) lie in \([0,2]\). Thus the approximation is uniform except for one term of negligible mass.

**2. Uniform-mesh convergence with a quantitative bound.** Partition \((0,1]\) into \(I_q=(1/(q+1),1/q]\), \(q\ge1\). On \(I_q\), the function is \(f(x)=qx^2\). Its internal variation on this interval is \(1/q-q/(q+1)^2=O(q^{-2})\), and its jump at \(1/q\) (for \(q\ge2\)) has size \(1/q^2\). Both sums converge, so \(f\) has finite total variation on \([0,1]\). Composition with a fixed Lipschitz \(\phi\) also has finite variation; its right-endpoint Riemann sums differ from its integral by at most \(\operatorname{Var}(\phi\circ f)/g\).

Replacing the uniform grid \(a=1,\dots,g\) by the admissible multiplicities deletes at most \(\tau(g)\) entries and adds one exceptional point \(a=g+1\). Adjusting the denominator from \(g\) to \(g+1-\tau(g)\) costs \(O_\phi((1+\tau(g))/g)\). The approximation in Step 1 costs at most \(4\operatorname{Lip}(\phi)/g\) for every ordinary grid entry. Since \(\tau(g)\le2\sqrt g\), this proves both the displayed error estimate and the weak limit. Applying the same argument to \(\phi(t)=t^m\) on \([0,2]\) gives convergence of each fixed positive integer moment, with the same rate.

**3. CDF, atoms and support.** On \(I_q\), the inequality \(f(x)\le t\) is equivalent to \(x\le\sqrt{t/q}\), so the length of the admissible subinterval is exactly the \(q\)-th summand in the claimed CDF. Each positive level has at most one preimage in each \(I_q\), hence countably many preimages overall, of Lebesgue measure zero. The zero preimage is just \(\{0\}\). The distribution is therefore atomless. The image of \(I_q\) has closure \([q/(q+1)^2,1/q]\). Consecutive such intervals overlap and their lower endpoints tend to zero, giving full support \([0,1]\).

**4. Exact zeta moments.** Splitting the integral over \(I_q\) yields, for every integer \(m\ge1\),
\[
\begin{aligned}
(2m+1)\mathbb E[Y^m]
&=\sum_{q\ge1}q^m\left(\frac1{q^{2m+1}}-\frac1{(q+1)^{2m+1}}\right)\\
&=\sum_{q\ge1}\frac{q^m-(q-1)^m}{q^{2m+1}}\\
&=\sum_{j=1}^m(-1)^{j+1}\binom mj\zeta(m+j+1).
\end{aligned}
\]
All series converge absolutely. The variance is strictly positive because the continuous-valued random variable \(f(U)\) is not constant.

## Verification

The standalone file `verify.py` constructs each classified semigroup from [1, Proposition 3.4], enumerates its gaps and minimal generators directly, and independently computes \(W(S)\) from those finite sets. It checks all \(4,116\) admissible genus/multiplicity pairs for \(1\le g\le94\). It separately compares three moment formulas with numerical interval integrals and checks finite-genus convergence at seven selected genera through \(15,001\). Execution with Python 3 standard library outputs three `PASS` lines. The infinite statements in the finding are proved in the four steps above; the finite computations are corroboration only.

## Relationship to prior work

Shor [1] introduced and classified reflective numerical semigroups, calculated their embedding dimensions and Frobenius numbers, counted those of fixed genus, and verified Wilf's inequality in this class. All those formulas and the positivity test are **prior results** and are not claimed as new. This finding combines the already-known classification with a new random-genus-family scaling limit, explicit pushforward distribution, a quantitative Riemann-sum estimate, and a complete zeta-valued moment sequence. Delgado's survey [2] discusses why Wilf surplus is a natural numerical-semigroup invariant. Another available study [3] computes *isolated-gap* statistics for reflective semigroups, not the Wilf-surplus limit distribution, so its result does not imply the formula here.

## Limitations

The result concerns uniform sampling **within reflective semigroups of each fixed genus**, not arbitrary semigroups; it does not resolve Wilf's conjecture outside the known reflective class. The exact distribution concerns the limit, not an exact finite-genus Wilf-surplus histogram. The claim depends on Shor's established structural classification. Unindexed earlier equivalent results remain possible; the comparison is not an assertion of absolute priority or independent certification. Finite checks do not replace the proof.

## References

[1] Caleb M. Shor, *Reflective numerical semigroups*, arXiv:2207.00051v1, first public 30 June 2022, https://arxiv.org/html/2207.00051v1 ; Albanian Journal of Mathematics 17 (2023).

[2] Manuel Delgado, *Conjecture of Wilf: A Survey*, arXiv:1902.03461, https://arxiv.org/abs/1902.03461 ; see also https://numerical-semigroups.github.io/wiki/Basic-concepts/Wilf-number.html .

[3] *An exact isolated-gap distribution and harmonic tail law for reflective numerical semigroups*, available research summary, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-isolated-gap-distribution-and-harmonic-tail-law-for-ref--c016095bed6e .
