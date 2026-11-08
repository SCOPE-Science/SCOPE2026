# An exact two-cohort stability ceiling and a unique defective boundary for delayed recruitment

## Finding

Consider a population whose recruits from each breeding cohort mature after either one or two census intervals. Suppose the cohort-level density response is the same differentiable recruitment function \(F\), with a fraction \(g\) of recruitment available after one interval and the remainder after two. The resulting scalar recurrence is
\[
 x_{t+1}=gF(x_t)+(1-g)F(x_{t-1}),\qquad 0\le g\le1.
\]
Let \(K>0\) satisfy \(F(K)=K\), and let \(a=F'(K)<1\). The equilibrium \((K,K)\) is a hyperbolic local sink precisely in the following regimes:

* \(-1<a<1\): every \(g\in[0,1]\);
* \(a=-1\): exactly \(0<g<1\);
* \(-3<a<-1\), writing \(q=-a\): exactly
\[
 1-\frac1q<g<\frac{1+1/q}{2}.
\]
* \(a\le-3\): no allocation \(g\in[0,1]\) yields a hyperbolic sink.

Thus \(-3\) is a sharp universal lower slope ceiling for two-cohort mixing, independently of the nonlinear details of \(F\). The admissible fraction interval for \(-3<a<-1\) has exact width \((3-q)/(2q)\), always contains \(g=2/3\), and collapses at \(q=3\). At the unique touching point \(a=-3,\ g=2/3\), the linearization has a nonsemisimple double multiplier \(-1\), and its powers grow linearly in a suitable direction.

For the Ricker recruitment function \(F_r(x)=x\exp(r(1-x/K))\), with \(r>0\), the equilibrium satisfies \(a=1-r\). The exact classification becomes: all fractions are linearly asymptotically stable for \(0<r<2\); only \(0<g<1\) at \(r=2\); and for \(2<r<4\), exactly
\[
 1-\frac1{r-1}<g<\frac{1+1/(r-1)}2.
\]
There is no hyperbolic sink at \(r\ge4\). The sharp supremum of the locally stabilizable Ricker overcompensation range is \(r=4\), approached at the fraction \(g=2/3\), but never attained by a hyperbolic sink. This is a statement about local equilibrium stability, not global persistence or nonlinear dynamics at the critical point.

## Assumptions and scope

Fix any \(K>0\). Let \(F:[0,\infty)\to[0,\infty)\) be continuously differentiable on a neighborhood of \(K\), with \(F(K)=K\) and \(a=F'(K)<1\). For every fixed fraction \(g\in[0,1]\), define the autonomous two-dimensional map
\[
 T_g(u,v)=(gF(u)+(1-g)F(v),u).
\]
The equilibrium in question is \((K,K)\). A *hyperbolic sink* means that both eigenvalues of \(DT_g(K,K)\) have modulus strictly below one. The theorem does not assert that an equilibrium with a unit-modulus eigenvalue is nonlinearly unstable. It also does not assert that a unit-circle crossing produces a generic nonlinear flip or Neimark–Sacker bifurcation.

The splitting is at the level of **cohort-specific nonlinear recruitment**, not the alternative age-structured mechanism of a common density-dependent fecundity factor applied to the aggregate age composition. That distinction matters for comparisons with Leslie-matrix results.

## Proof

Differentiating at the positive equilibrium gives
\[
 J=DT_g(K,K)=\begin{pmatrix}ag&a(1-g)\\1&0\end{pmatrix},\qquad
 P(\lambda)=\lambda^2-ag\lambda-a(1-g).
\]
For a monic real quadratic \(\lambda^2+B\lambda+C\), the strict unit-disc criterion is exactly \(1+B+C>0\), \(1-B+C>0\), and \(1-C>0\). One way to prove necessity and sufficiency is to use the bilinear transformation \(\lambda=(1+z)/(1-z)\), which maps the open left half-plane onto the open unit disk. Multiplying the transformed quadratic by \((1-z)^2\) yields a real quadratic Hurwitz condition equivalent to the three inequalities. Equivalently these are the second-degree strict Jury conditions.

For the present \(P\), the three strict inequalities reduce to
\[
 1-a>0,\qquad 1+a(2g-1)>0,\qquad 1+a(1-g)>0. \tag{1}
\]
The first is automatic under \(a<1\). If \(-1<a<1\), both remaining expressions are strictly positive for all \(0\le g\le1\). At \(a=-1\), they equal \(2(1-g)\) and \(g\), respectively; hence precisely the strict interior fractions are sinks.

For \(a<-1\), put \(q=-a>1\). The last two conditions in (1) are equivalent to
\[
 g<\frac{1+1/q}{2},\qquad g>1-\frac1q.\tag{2}
\]
These bounds are compatible exactly when \(q<3\), since their difference is \((3-q)/(2q)\). At \(q=3\) both bounds meet at the unique fraction \(g=2/3\). For \(q>3\) there is no strict solution. This proves every parameter claim about hyperbolic sinks.

At \(a=-3\) and \(g=2/3\),
\[
 J=\begin{pmatrix}-2&-1\\1&0\end{pmatrix},\qquad P(\lambda)=(\lambda+1)^2.
\]
Writing \(N=J+I=\begin{pmatrix}-1&-1\\1&1\end{pmatrix}\), direct multiplication gives \(N^2=0\ne N\), and therefore for every integer \(n\ge0\),
\[
 J^n=(-1)^n(I-nN).
\]
In particular, \(J^n(1,0)^{\mathsf T}=(-1)^n(1+n,-n)^{\mathsf T}\), whose Euclidean norm grows asymptotically as \(\sqrt2\,n\). This is an exact linearized statement at the boundary, not an assertion of unbounded nonlinear population trajectories.

For \(F_r(x)=x\exp(r(1-x/K))\), differentiation gives \(F_r(K)=K\) and \(F'_r(K)=1-r\). Substitution into the already proved classification gives all Ricker cases. The unique maximal ceiling follows from the strictly increasing lower bound \(1-1/q\) and strictly decreasing upper bound \((1+1/q)/2\) for \(q>1\). Their unique intersection is \((q,g)=(3,2/3)\), corresponding to \(r=4\).

## Verification

The accompanying standalone `check.py` uses Python's exact rational arithmetic for the strict Jury inequalities, exact boundary interval formulas, the unique ceiling, and the nilpotent Jordan identity. It independently computes eigenvalue moduli on a finite grid as a subsidiary numerical check. Run `python check.py` from the directory containing this file. A successful run prints `PASS: 3554 assertions`.

Finite sample tests do not establish the infinite statements; the preceding algebraic proof does. The checker verifies the linearization and its powers, not the nonlinear asymptotic behavior at criticality.

## Relationship to prior work

Stage-structured Ricker models and maturation delays have a substantial history. Lazaryan and Sedaghat's 2015 preprint (subsequently published) models juvenile–adult populations by a planar system with a linear survival/persistence contribution and a delayed Ricker fecundity term. Its equations (1)–(2) are not the sum of two independent nonlinear cohort-recruitment terms studied here. Wikan and Mjølhus (1996), Wikan (1997), Silva and Hallam (1993), and later work analyze broader classes of nonlinear age-structured population models. Beretta and Breda (2016) instead compare continuous-time discrete and distributed maturation delays; Lazaryan and Sedaghat (2015) establish general boundedness and extinction results for an age-structured planar system, rather than this exact two-delay local optimization. In particular, standard Leslie formulations often apply one density-dependent factor to aggregate age-specific fecundity, rather than separately applying \(F\) to each of two cohort histories. Direct equivalence of those models to the recurrence here was not established in the inspected material.

The contribution asserted here is the explicitly quantified, response-function-independent two-cohort stability ceiling, the exact interval of stabilizing allocations, and the unique defective double-\(-1\) boundary. Familiar Ricker stability and the general quadratic Jury criterion are not asserted as new.

## Limitations

The result is local and assumes differentiability and the stated cohort-separable recruitment mechanism. The fraction \(g\) is a normalized mixture of two recruitment ages; changing cohort survival or density-feedback normalization may change the sharp value. On the stability boundary the linear analysis alone cannot decide nonlinear asymptotic stability or the type of subsequent attractors. Some historically relevant age-structured papers were available only as abstracts or partial text; equivalence or stronger coverage from their uninspected full texts remains a priority risk. No claim about field-optimal management or empirical calibration is made.

## References

1. Lazaryan, N., and Sedaghat, H. (2015), *Extinction, periodicity and multistability in a Ricker Model of Stage-Structured Populations*, arXiv:1509.08132, first posted 27 September 2015, https://arxiv.org/abs/1509.08132.
2. Wikan, A., and Mjølhus, E. (1996), *Overcompensatory recruitment and generation delay in discrete age-structured population models*, Journal of Mathematical Biology 35, 195–239, https://doi.org/10.1007/s002850050050.
3. Wikan, A. (1997), *Dynamic consequences of reproductive delay in Leslie matrix models with nonlinear survival probabilities*, Mathematical Biosciences 146, 37–62, https://doi.org/10.1016/S0025-5564(97)00074-6.
4. Silva, J. A. L., and Hallam, T. G. (1993), *Effects of delay, truncations and density dependence in reproduction schedules on stability of nonlinear Leslie matrix models*, Journal of Mathematical Biology 31, 367–395, https://doi.org/10.1007/BF00163922.
5. Zheng, C., Zhang, F., and Li, J. (2014), *Stability Analysis of a Population Model with Maturation Delay and Ricker Birth Function*, Abstract and Applied Analysis, article 136707, https://doi.org/10.1155/2014/136707.
6. Beretta, E., and Breda, D. (2016), *Discrete or distributed delay? Effects on stability of population growth*, Mathematical Biosciences and Engineering 13, 19–41, https://doi.org/10.3934/mbe.2016.13.19.
7. Lazaryan, N., and Sedaghat, H. (2015), *Dynamics of Planar Systems That Model Stage-Structured Populations*, Discrete Dynamics in Nature and Society 2015, article 137182, https://doi.org/10.1155/2015/137182.
8. Wikan, A., and Kristensen, Ø. (2024), *On bifurcations, resonances and dynamical behaviour in nonlinear iteroparous Leslie matrix models*, Nonlinear Dynamics 112, 2265–2288, https://doi.org/10.1007/s11071-023-09143-w.
