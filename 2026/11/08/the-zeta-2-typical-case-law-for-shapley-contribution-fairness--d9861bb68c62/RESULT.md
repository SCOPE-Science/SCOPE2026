# The \(\zeta(2)\) typical-case law for Shapley contribution fairness

## Finding

Fix an integer \(n\ge 1\) and a real parameter \(s>0\). One unit of a divisible resource is allocated without monetary transfers to \(n\) agents with independent productivities \(V_i=U_i^s\), where the \(U_i\) are independent uniform random variables on \((0,1)\). An allocation \((a_i)\), with \(a_i\ge0\) and \(\sum_i a_i=1\), gives agent \(i\) utility \(V_i a_i\). The associated cooperative welfare game has worth \(w(S)=\max_{i\in S} V_i\) for nonempty \(S\), and \(w(\varnothing)=0\). Write \(\phi_i\) for its Shapley value and \(A_{n,s}\) for the smallest factor \(\alpha\) for which all agents can receive at least \(\phi_i/\alpha\) in utility.

Let \(U_{(1)}<\cdots<U_{(n)}\) be the order statistics and let \(H_n=\sum_{j=1}^n 1/j\). Almost surely,
\[
A_{n,s}=H_n-\sum_{1\le r<j\le n}\frac{(U_{(r)}/U_{(j)})^s}{(n-r)(n-r+1)}.
\]
Consequently, for every \(n\ge2\) the factor is strictly increasing in \(s\) under the natural coupling using the same uniform samples. Its exact expectation is
\[
\mathbb E A_{n,s}=H_n-\sum_{1\le r<j\le n}\frac{\Gamma(r+s)\Gamma(j)}{(n-r)(n-r+1)\Gamma(r)\Gamma(j+s)}.
\]
In particular, for every positive integer \(n\),
\[
\mathbb E A_{n,1}=\sum_{j=1}^n\frac1{j^2},\qquad
\mathbb E A_{n,2}=\frac{2n}{n+1},\qquad
\mathbb E A_{n,3}=\frac{3n(3n+5)}{4(n+1)(n+2)}.
\]
For any fixed \(s>0\), using the first \(n\) terms of a common infinite independent uniform sequence, the random factor converges almost surely and in \(L^1\):
\[
A_{n,s}\longrightarrow C(s)=\sum_{m=1}^{\infty}\frac{s}{m(m+s-1)}
=\begin{cases}
\displaystyle\frac{s(\psi(s)+\gamma)}{s-1},&s\ne1,\\
\displaystyle\frac{\pi^2}{6},&s=1,
\end{cases}
\]
where \(\psi\) is the digamma function and \(\gamma\) is Euler's constant. The curve \(C(s)\) is strictly increasing, with \(C(s)\to1\) as \(s\downarrow0\) and \(C(s)=\log s+\gamma+o(1)\) as \(s\to\infty\). Thus the optimal factor for uniform independent productivities converges to \(\pi^2/6\), although the unrestricted worst-case factor for linear productivities can grow logarithmically with the number of agents.

## Assumptions and scope

All values are strictly positive almost surely, agents are labeled, the good is perfectly divisible with unit supply and no capacity caps, valuations are linear, and the coalitional value is the maximum achievable total welfare when that coalition alone receives the complete good. The optimal approximation compares each agent's utility with the transferable-utility Shapley benchmark, without allowing transfers in the actual allocation. The exact mean formula applies for every finite \(n\ge1\) and real \(s>0\); convergence holds for a fixed \(s\) as \(n\) grows. The theorem does not assert a joint limit with a changing exponent, a variance formula, or any conclusion for several coupled goods.

## Proof

**1. Exact optimum and the pathwise identity.** Sort productivities increasingly, putting \(v_j=U_{(j)}^s\), \(v_0=0\). The max-game is a sum of threshold-coverage games, so the Shapley value of the agent at rank \(j\) is
\[
\phi_j=\sum_{r=1}^j\frac{v_r-v_{r-1}}{n-r+1}.
\]
Every feasible approximation factor must satisfy \(a_j\ge \phi_j/(\alpha v_j)\), hence \(\alpha\ge\sum_j\phi_j/v_j\). Equality is attained by \(a_j=\phi_j/(v_j\sum_\ell\phi_\ell/v_\ell)\). Thus \(A_{n,s}=\sum_j\phi_j/v_j\) exactly. Setting \(b_r=(n-r+1)^{-1}\), finite summation by parts gives
\[
\frac{\phi_j}{v_j}=b_j-\sum_{r<j}(b_{r+1}-b_r)\frac{v_r}{v_j},
\qquad b_{r+1}-b_r=\frac1{(n-r)(n-r+1)}.
\]
Summing over \(j\) proves the first displayed formula. For \(n\ge2\), all its coefficients are positive, and \(U_{(r)}/U_{(j)}\in(0,1)\); therefore it increases strictly with \(s\). It lies in \((1,H_n)\) for \(n\ge2\), with endpoint limits \(1,H_n\) as \(s\downarrow0,s\uparrow\infty\).

**2. Exact finite-population expectation.** Conditional on \(U_{(j)}\), the preceding \(j-1\) observations, divided by \(U_{(j)}\), have uniform order statistics on \((0,1)\). Hence for \(1\le r<j\),
\[
\mathbb E\left[(U_{(r)}/U_{(j)})^s\right]
=\frac{\Gamma(r+s)\Gamma(j)}{\Gamma(r)\Gamma(j+s)}.
\]
Substitution in the finite pathwise identity proves the exact expectation formula. For \(s=1\), the \(j\) normalized spacings ending at \(U_{(j)}\) have mean \(1/j\) each. Accordingly,
\[
\mathbb E A_{n,1}=\sum_{j=1}^n\frac1j\sum_{r=1}^j\frac1{n-r+1}.
\]
This is also \(\sum_{1\le p,q\le n,\ p+q\ge n+1}1/(pq)\). Denote it by \(D_n\). Adding the new last row and column, then removing the old diagonal, yields
\[
D_n-D_{n-1}=\frac{2H_{n-1}}n+\frac1{n^2}-\sum_{p=1}^{n-1}\frac1{p(n-p)}=\frac1{n^2}.
\]
As \(D_1=1\), the claimed second-order harmonic identity follows.

For integer powers, the normalized \(r\)-th order statistic has expected \(s\)-th power \(\Gamma(r+s)\Gamma(j)/(\Gamma(r)\Gamma(j+s))\) for ranks \(1\le r\le j\), including \(r=j\). For \(s=2\), the differences of consecutive expectations equal \(2r/[j(j+1)]\), so
\[
\mathbb E A_{n,2}=\sum_{r=1}^n\frac{2r}{n-r+1}\sum_{j=r}^n\frac1{j(j+1)}
=2H_n-\frac2{n+1}\big((n+1)H_n-n\big)=\frac{2n}{n+1}.
\]
For \(s=3\), consecutive differences are \(3r(r+1)/[j(j+1)(j+2)]\). Applying the telescoping identity for the latter denominators and summing the resulting quadratic polynomial in \(r\) yields \(3n(3n+5)/[4(n+1)(n+2)]\), as stated.

**3. Almost-sure convergence.** Let \(T_n(s)\) be the same pathwise expression evaluated on the deterministic quantile grid \(u_j=j/n\). For any \(0<\delta<1/2\), a Riemann-sum argument on ranks \(\delta n\le j\le(1-\delta)n\) gives the integrand
\[
g_s(t)=s t^{-s}\int_0^t\frac{u^{s-1}}{1-u}\,du.
\]
The low-rank contribution to \(T_n\), for \(j\le\delta n\), is at most \(\delta/(1-\delta)+o(1)\), since every reciprocal denominator is at most \(1/[n(1-\delta)]\). On the upper ranks, partition the inner spacing sum at \(r=n/2\); the resulting \(j\)-th summand is at most \(K_s[1+\log(n/(n-j+1))]/n\) for \(j\ge (1-\delta)n\). Summing these ranks gives a \(K_s\delta(1+|\log\delta|)+o(1)\) bound. Both ends vanish as \(\delta\downarrow0\), proving \(T_n(s)\to\int_0^1 g_s(t)\,dt\).

For the actual uniforms, the standard uniform empirical-CDF exponential bound implies that, except on events of summable probability, \(\max_j|U_{(j)}-j/n|\le\sqrt{3\log n/n}+2/n\). Put \(m=\lceil n^{3/4}\rceil\). For ranks \(r,j\ge m\), the relative quantile error is \(O(n^{-1/4}\sqrt{\log n})\); taking positive powers changes \((U_{(r)}/U_{(j)})^s\) relative to \((r/j)^s\) by at most a constant times this error. The sum of all pair coefficients is at most \(H_n\). For the omitted ranks \(r<m\), the sum of their pair coefficients is at most \(\sum_{r<m}1/(n-r+1)=O(n^{-1/4})\), and both ratios are bounded by one. Consequently,
\[
|A_{n,s}-T_n(s)|=O_s(n^{-1/4}(\log n)^{3/2})+O(n^{-1/4})\longrightarrow0
\]
on the eventual good events. Borel--Cantelli proves almost-sure convergence. Since \(1\le A_{n,s},T_n(s)\le H_n\), the same exceptional-event estimate and the summably small failure probabilities show \(\mathbb E|A_{n,s}-T_n(s)|\to0\), proving \(L^1\) convergence as well.

**4. Limiting constant and monotonicity.** Substitute \(u=tv\) and expand the nonnegative geometric series to obtain
\[
\int_0^1g_s(t)\,dt
=s\int_0^1\!\int_0^1\frac{v^{s-1}}{1-tv}\,dv\,dt
=\sum_{m=1}^{\infty}\frac{s}{m(m+s-1)}.
\]
The standard digamma series gives the stated closed form, with its continuous value at \(s=1\). Equivalently, this is the expectation of \(h(Z_s)=-\log(1-Z_s)/Z_s\) for \(Z_s\) with distribution \(\operatorname{Beta}(s,1)\). As \(h\) is strictly increasing and \(Z_s\) is strictly stochastically increasing in \(s\), so is \(C(s)\). The endpoint claims follow from this integral or the digamma asymptotics.

## Verification

The accompanying `verify.py` recomputes the Shapley factors both by the order-statistic spacing formula and by all agent permutations on small deterministic profiles; independently compares the pairwise formula; checks the finite-\(n\) rational identities for uniform, square and cubic productivities; tests monotonicity on seeded samples; and compares simulated means to the independent beta-moment formula. Executing `python3 verify.py` with Python 3 and `mpmath` available gives `PASS 1137 checks`. The program is finite corroboration only; the infinite claims are established in the proof above.

## Relationship to prior work

Bei, Lu, Wu and Zhou (2026), Section 4, introduce the linear-resource Shapley approximation factor, give the fixed-instance Shapley value formula and develop worst-case logarithmic and type-dependent bounds. The exact finite-population random-productivity means, the almost-sure limiting curve, its \(\zeta(2)\) specialization, and the pathwise power monotonicity are different statements that do not follow as stated from a worst-case bound or a fixed-profile Shapley formula without further probability arguments. Bachrach, Savani and Shah (2014) study max cooperative games (also with failures), establish fixed-weight Shapley computations, and do not address no-transfer resource fairness or the random-productivity approximation factor. The arguments here reuse the known max-game decomposition, and novelty is claimed only for the stochastic factor laws, subject to residual literature risk.

## Limitations

The result is confined to one perfectly divisible unit of resource, no payments, iid power-transformed uniform productivity and fixed exponents; it is not a general multi-good theorem. The asymptotic limit is a typical-case statement, not a deterministic guarantee for arbitrary values. No central limit theorem or sharp convergence rate is claimed. A related unindexed order-statistic calculation or prior average-case analysis may already imply the main identities; absence in the inspected references is not proof of publication priority. No independent audit has been performed.

## References

1. X. Bei, P. Lu, X. Wu and S. Zhou, *Fair Division by Contribution: A Shapley Value Perspective*, arXiv:2606.16743, first posted June 15, 2026. https://arxiv.org/abs/2606.16743
2. Y. Bachrach, R. Savani and N. Shah, *Cooperative Max Games and Agent Failures*, AAMAS 2014, pp. 29--36. https://ifmas.csc.liv.ac.uk/Proceedings/aamas2014/aamas/p29.pdf
3. Mathematics Subject Classification 2020, 91B32 (resource and cost allocation). https://mathscinet.ams.org/mathscinet/msc/msc2020.html
