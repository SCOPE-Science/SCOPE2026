# Global uniqueness and two boundary scales of prime-two orbits in a generalized Allee-logistic map

## Finding

For the cubic map \(f_r(x)=rx(1-x)(c+mx)\), with \(r>0\), \(c,m\ge0\), and \(c+m>0\), there is **exactly one** unordered primitive period-two orbit \(\{u,v\}\subset(0,1)\) if and only if \(r>r_*\), where \(r_*\) is explicitly defined below. There is none for \(r\le r_*\). The orbit is uniquely parametrized by its sum \(s=u+v\) through a strictly decreasing rational function of \(s\), with no additional period-two windows or secondary positive period-two branches at any larger growth rate.

As \(r\to\infty\), the unique pair approaches the opposite endpoints of the unit interval. Its approach has **different exact powers** according as the linear-growth coefficient is positive or zero:

\[
\begin{aligned}
c>0:&\qquad ru\longrightarrow c^{-1},\qquad r^2(1-v)\longrightarrow [c(c+m)]^{-1},\\
c=0,\ m>0:&\qquad \sqrt{mr}\,u\longrightarrow1,\qquad (mr)^{3/2}(1-v)\longrightarrow1.
\end{aligned}
\]

The second regime is the degenerate-Allee endpoint of the same cubic family. Large values of \(r\) here describe the polynomial map algebraically, and need not preserve the entire state interval.

## Assumptions and scope

The state space for the cycle classification is the open interval \((0,1)\); no assumption is made that the full interval is forward invariant at arbitrarily large \(r\). The parameters satisfy \(c,m\ge0\), \(c+m>0\), and \(r>0\). A primitive two-cycle means two **distinct** points \(0<u<v<1\) with \(f_r(u)=v\) and \(f_r(v)=u\). We count a cycle once, without distinguishing its time origin.

The source's generalized Allee-logistic family is obtained by setting \(c=1-m(1+h)\), with \(0\le m,h\le1\); our theorem applies to its nonnegative-growth subfamily \(c\ge0\), and more generally to nonnegative coefficients. The strong-Allee case \(c<0\) is not covered.

Define \(s_*\) as the unique root in \((1,2)\) of

\[
Q(s)=2ms^2+3(c-m)s-4c=0.
\]

Explicitly, \(s_*=4/3\) when \(m=0\), and otherwise

\[
s_* = \frac{3(m-c)+\sqrt{9(m-c)^2+32mc}}{4m}.
\]

Put

\[
R(s)=\frac{c+m(2s-1)}{(s-1)(c+ms)(c+m(s-1))},\qquad r_*=R(s_*).
\]

For each \(r>r_*\) there is a unique \(s\in(1,s_*)\) with \(R(s)=r\). Write

\[
p(s)=\frac{s(s-1)(c+ms)}{c+m(2s-1)},\quad
\Delta(s)=s^2-4p(s),\quad
u=\frac{s-\sqrt{\Delta(s)}}2,\quad
v=\frac{s+\sqrt{\Delta(s)}}2.
\]

These \(u,v\) are the unique primitive two-cycle.

## Proof

**Step 1: every candidate has sum greater than one.** Let \(H(x)=x f_r(x)/r=x^2(1-x)(c+mx)\). Every primitive two-cycle obeys \(H(u)=H(v)\), since \(u f_r(u)=uv=v f_r(v)\). The derivative is

\[
H'(x)=x\bigl[2c+3(m-c)x-4mx^2\bigr].
\]

It is positive up to its unique maximum in \([2/3,3/4]\), and negative thereafter on \((0,1)\). This follows directly from the quadratic's value at the endpoints and its unique positive zero; when \(c=0\) the maximum is exactly at \(3/4\), and when \(m=0\) it is at \(2/3\). Thus distinct points with equal \(H\)-values straddle the maximum, so \(s=u+v>2/3\).

Writing \(p=uv\) and dividing \(H(u)-H(v)=0\) by \(u-v\) gives the exact identity

\[
s(1-s)(c+ms)+p\bigl[c+m(2s-1)\bigr]=0.
\]

Here \(c+m(2s-1)>0\) because \(s>2/3\), so

\[
p=\frac{s(s-1)(c+ms)}{c+m(2s-1)}.
\]

Since \(p>0\), necessarily \(s>1\). Since \(u,v<1\), also \(s<2\).

**Step 2: parameter elimination is exact.** The second cycle identity \(f_r(u)+f_r(v)=s\) reads

\[
\frac{s}{r}
=c(s-s^2+2p)+m\bigl(s^2-s^3+(3s-2)p\bigr).
\]

Substitution of the displayed \(p\) simplifies the right-hand side to \(s/R(s)\), hence \(r=R(s)\). Conversely, if \(r=R(s)\) and \(u,v\) are roots of \(z^2-sz+p(s)=0\), then the two displayed identities hold. They imply \(u f_r(u)=v f_r(v)\) and \(f_r(u)+f_r(v)=u+v\); solving these two linear equations gives precisely \(f_r(u)=v\), \(f_r(v)=u\).

**Step 3: exact admissible interval.** The discriminant factors as

\[
\Delta(s)=-\frac{s\,[2ms^2+3(c-m)s-4c]}{c+m(2s-1)}=-\frac{sQ(s)}{c+m(2s-1)}.
\]

For nonnegative \(c,m\), not both zero, \(Q(1)=-(c+m)<0\), \(Q(2)=2(c+m)>0\); it has exactly one zero in \((1,2)\) (linear if \(m=0\), otherwise the quadratic has one positive root). Consequently, \(\Delta(s)>0\) exactly on \((1,s_*)\). For such \(s\), the roots are positive because \(s,p>0\), and are below one because

\[
(1-u)(1-v)=1-s+p(s)=\frac{(s-1)^2[c+m(s-1)]}{c+m(2s-1)}>0
\]

and \(u+v<2\); two positive roots with positive complementary product cannot both exceed one when their sum is below two. Thus every \(s\in(1,s_*)\) generates a genuine unique positive pair.

**Step 4: global uniqueness, without a local-bifurcation assumption.** Set \(t=s-1>0\). The rational parameterization becomes

\[
R(1+t)=\frac{c+m+2mt}{t(c+m+mt)(c+mt)}.
\]

Its logarithmic derivative satisfies

\[
\frac{d}{dt}\log R(1+t)
=\frac{2m}{c+m+2mt}-\frac1t-\frac{m}{c+m+mt}-\frac{m}{c+mt}<0,
\]

since the first positive term is strictly smaller than \(1/t\). The limit at \(s\downarrow1\) is \(+\infty\), whereas the limit at \(s\uparrow s_*\) is \(r_*\). Thus for every \(r>r_*\) exactly one \(s\) exists; at \(r=r_*\) the two roots coincide and yield a fixed point rather than a primitive cycle; and below \(r_*\) no pair is possible.

**Step 5: singular boundary scales.** As \(s\downarrow1\), write \(t=s-1\). For \(c>0\), the rational formula implies \(R(1+t)\sim1/(ct)\). The exact product and complementary-product expressions give \(u\sim t\) and \(1-v\sim ct^2/(c+m)\). Since \(R(s)=r\), these yield the first two limits. For \(c=0\), \(m>0\), one has \(R(1+t)\sim1/(mt^2)\), \(u\sim t\), and \(1-v\sim t^3\), giving the second pair of limits. All limits are along the unique orbit parametrized by \(r\to\infty\).

## Verification

The included `verify.py` checks five symbolic identities (including the weighted orbit equation, rational elimination, discriminant and complementary product) using SymPy and tests 54 high-precision solutions or boundary scalings across six coefficient choices. Run it from the package directory with `python verify.py` after installing `sympy` and `mpmath`. The expected successful message is `VERIFY_OK symbolic_identities=5 high_precision_cycle_and_boundary_cases=54 precision_digits=65`. Finite numerical tests do not prove the all-parameter uniqueness statement; the proof is Steps 1–5 above.

## Relationship to prior work

Pires, Andrade and Herrmann introduced the generalized Allee-logistic map, solved equilibrium and tricriticality equations, and investigated period doubling and chaos. Their June 2026 manuscript does not state the global prime-two-orbit parameterization, all-growth uniqueness, or the two singular endpoint rates. The flip threshold and local period-doubling onset are established earlier and are **not** claimed here as new results: the novel assertion is the global all-growth classification, including the absence of additional primitive two-cycles and the two distinct high-growth asymptotic laws. The logistic endpoint \(m=0\) is classical and included for completeness, not claimed as a new discovery. The 2020 Allee logistic special case is relevant earlier literature; only its abstract was accessible, so full-document priority comparison for that endpoint remains a risk.

## Limitations

This result concerns primitive period-two pairs in \((0,1)\), not stability, other periods, global attractors, or persistence of general trajectories. The formal limit \(r\to\infty\) does **not** preserve the physical interval for general initial data; it describes the exact two-cycle continuation of the polynomial equation. The strong-Allee sector \(c<0\) is excluded. Historical priority remains provisional, especially at the older special-case endpoint.

## References

1. M. A. Pires, J. S. Andrade Jr., and H. J. Herrmann, *Tricriticality and chaos in a generalized Allee-logistic map*, arXiv:2606.05351v1 (first public posting 2026-06-03), https://arxiv.org/abs/2606.05351. Main equations and analysis inspected via lawful public full text at https://www.researchgate.net/publication/406059459_Tricriticality_and_chaos_in_a_generalized_Allee-logistic_map.
2. N. Jung et al., *Chaotic Dynamics of a Simple Population Model under the Allee Effect*, *Journal of the Korean Physical Society* **76** (2020), 533–536, https://doi.org/10.3938/jkps.76.533 (abstract consulted; complete text not inspected).
3. *Logistic Map*, Wolfram MathWorld, https://mathworld.wolfram.com/LogisticMap.html (classical quadratic special case and its two-cycle formula).
