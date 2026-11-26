# Independent extreme clocks for circular coverage and one-deletion robustness

## Finding
Let \(n\ge3\) independent uniform points lie on the circle \(\mathbb R/\mathbb Z\), and let \(G_{n,1},\ldots,G_{n,n}\) be their successive clockwise gaps, with cyclic indices. For fixed real \(x,y\) define
\[
N_{1,n}(x)=\sum_{i=1}^n {\bf1}\{nG_{n,i}>\log n+x\},\qquad
N_{2,n}(y)=\sum_{i=1}^n {\bf1}\{n(G_{n,i}+G_{n,i+1})>\log n+\log\log n+y\}.
\]
As \(n\to\infty\), the pair converges jointly in distribution to **independent** Poisson counts with respective means \(e^{-x}\) and \(e^{-y}\). In particular, writing \(M_{1,n}=\max_iG_{n,i}\), \(M_{2,n}=\max_i(G_{n,i}+G_{n,i+1})\),
\[
\bigl(nM_{1,n}-\log n,\ nM_{2,n}-\log n-\log\log n\bigr)
\ \Longrightarrow\ (H_1,H_2),
\]
where \(H_1,H_2\) are independent standard Gumbel variables. Thus, for every fixed \(x,y\), the joint limiting distribution function is \(\exp(-e^{-x}-e^{-y})\).

For equal clockwise arcs of length \(\ell\) placed at the sampled points, complete coverage is equivalent to \(M_{1,n}\le\ell\), while coverage surviving deletion of **any one** arc is equivalent to \(M_{2,n}\le\ell\). These represent distinct logarithmic thresholds with asymptotically independent centered extreme clocks.

## Assumptions and scope
All points are independent, uniform, and almost surely distinct. Arc lengths and gaps are measured as fractions of the full circumference, with clockwise closed arcs of common length \(\ell\in[0,1]\). The counts refer to the original \(n\) arcs, and deletion robustness means *every* single choice of arc can be removed without losing total coverage. Indices wrap cyclically, including the pair formed by the last and first gaps. The two coordinates use potentially different deterministic thresholds \(\ell_{1,n}=(\log n+x)/n\) and \(\ell_{2,n}=(\log n+\log\log n+y)/n\). No independence is asserted at finite \(n\), nor for maxima with a common finite-sample normalization.

## Proof
**1. Exponential spacing representation.** Let \(E_1,\ldots,E_n\) be independent mean-one exponential random variables, and put \(T_n=\sum_{i=1}^nE_i\). The circular gap vector has the distribution \((E_i/T_n)_{i=1}^n\); this follows by the Dirichlet density of uniform circular spacings. Introduce unnormalized counts \(A_n=\sum_i{\bf1}\{E_i>u_n\}\), \(B_n=\sum_i{\bf1}\{E_i+E_{i+1}>v_n\}\), with \(u_n=\log n+x\), \(v_n=\log n+\log\log n+y\), and \(E_{n+1}=E_1\). For all sufficiently large \(n\), \(0<u_n<v_n\).

**2. One-site means.** Exponential and gamma-two tails give
\[
 n\Pr(E_1>u_n)=e^{-x},\qquad
 n\Pr(E_1+E_2>v_n)=n(1+v_n)e^{-v_n}\longrightarrow e^{-y}.
\]
Each labeled exceedance event depends on only one or two adjacent variables. Events with disjoint sets of underlying exponentials are independent. Every event has only a bounded number of neighboring dependent events, uniformly in \(n\).

**3. Critical mixed and same-type overlaps.** Direct integration, for \(v\ge u\ge0\), yields the exact identities
\[
\Pr(E_1>u,\ E_1+E_2>v)=(v-u+1)e^{-v},
\]
\[
\Pr(E_1+E_2>v,\ E_2+E_3>v)=2e^{-v}-e^{-2v}.
\]
The first follows by integrating \(e^{-t}e^{-(v-t)}\) over \(u<t<v\), plus the tail \(t\ge v\). For the second, condition on \(E_2=t\), integrate \(e^{-t-2(v-t)}\) over \(0<t<v\), and add \(\Pr(E_2\ge v)\). Accordingly,
\[
 n(v_n-u_n+1)e^{-v_n}=O\!\left(\frac{\log\log n}{\log n}\right)\to0,
 \qquad n(2e^{-v_n}-e^{-2v_n})=O(1/\log n)\to0.
\]
Distinct one-site events are independent. Thus the sum of joint probabilities across all overlapping distinct events tends to zero, while the sum of products of neighboring individual probabilities is \(O(1/n)\). (At a cyclic boundary the same estimates hold for \(n\ge4\), and finite smaller sizes are irrelevant.)

**4. Joint Poisson approximation.** Apply the local-dependence Poisson *point-process* approximation to the finite labeled set \(\{(1,i),(2,i):1\le i\le n\}\). Its dependency-neighborhood estimates from step 3 give total variation error \(o(1)\) compared with the Poisson process whose atoms at \((1,i)\) and \((2,i)\) have intensities \(\Pr(E_i>u_n)\) and \(\Pr(E_i+E_{i+1}>v_n)\). Projecting onto the two type totals yields two independent Poisson variables with mean parameters converging to \(e^{-x}\) and \(e^{-y}\). The process approximation is standard, for example the locally dependent Chen--Stein formulation of Arratia, Goldstein and Gordon (1989); alternatively, factorial moments give the same conclusion because each non-singleton overlap component contributes \(o(1)\) after summing its \(O(n)\) locations.

**5. Return to normalized circular gaps.** Since \(T_n/n=1+O_{\mathbb P}(n^{-1/2})\), one has \((T_n/n-1)\max(u_n,v_n)=o_{\mathbb P}(1)\). For any \(\varepsilon>0\), with probability tending to one, each normalized event is sandwiched between the corresponding unnormalized event evaluated at its original threshold plus or minus \(\varepsilon\). The joint distribution of their counts is therefore obtained by squeezing against the continuous-in-\((x,y)\) independent-Poisson limits in step 4. Evaluating the probability that both counts vanish establishes the claimed independent Gumbel maxima.

**6. Coverage interpretation.** In clockwise order, the arcs cover the whole circle precisely when no successive gap exceeds \(\ell\). Deleting the arc at one start joins the gap immediately before it to the gap immediately after it, leaving all other successive gaps unchanged. Since any two-gap sum dominates its constituent gaps, all such deletions preserve coverage if and only if \(G_{n,i}+G_{n,i+1}\le\ell\) for every cyclic \(i\). This proves the exact finite-sample equivalence and completes the theorem.

## Verification
Run `python verify.py` with NumPy and SciPy installed. The verifier checks the exact geometry identity on 2,310 constructed cases, verifies both overlap integrals against independent numerical quadrature, checks decay of the overlap bounds, and compares some finite-sample empirical frequencies with the qualitative limiting law. The run reports 2,326 checks passed. No numerical experiment is used as a substitute for the analytic steps, and the finite-frequency tolerance is intentionally broad because convergence near the \(\log\log n\) threshold is slow.

## Relationship to prior work
Mijatović and Vysotsky proved the marginal Gumbel limit for each fixed maximal \(k\)-spacing and discussed independence of the *odd and even two-spacing subsequence maxima*. Their argument does not establish independence of maxima at **different** orders \(k=1\) and \(k=2\). Roos and Glaz--Naus--Roos--Wallenstein investigate Poisson approximations for ordered \(m\)-spacings, with \(m\) fixed in their stated abstracts. The present coupled two-type local-dependence proof assesses a different assertion: simultaneous limits at two distinct logarithmic centers and vanishing cross-type dependence. The separate marginal Gumbel laws, exponential spacing representation, and Poisson approximation technique are prior ingredients, not claimed as new.

## Limitations
This is a self-review, not an independent assessment of historical priority. The complete full texts of Roos (1993), Glaz et al. (1994), and the relevant broad spacing chapter in Barbour--Holst--Janson (1992) were not obtained; a general older multivariate extremal-process result may imply the joint independence theorem. In particular, lack of a matching search result is not evidence of uniqueness. The result is specific to independently sampled uniform circle points and the two adjacent spacing orders. It does not assert a joint process limit for all \(k\), a universal rate of convergence after random-denominator normalization, or any finite-size independence.

## References
1. A. Mijatović and V. Vysotsky, *On the weak limit law of the maximal uniform k-spacing*, arXiv:1508.00944, first public version 2015-08-05; *Advances in Applied Probability* 48(A) (2016), 235--238. https://arxiv.org/abs/1508.00944
2. M. Roos, *Compound Poisson approximations for the numbers of extreme spacings*, *Advances in Applied Probability* 25 (1993), 847--874. https://doi.org/10.2307/1427795
3. J. Glaz, J. Naus, M. Roos and S. Wallenstein, *Poisson approximations for the distribution and moments of ordered m-spacings*, *Journal of Applied Probability* 31(A) (1994), 271--281. https://doi.org/10.2307/3214961
4. J. Hüsler, *Maximal, non-uniform spacings and the coverage problem*, *Journal of Applied Probability* 25 (1988), 519--528. https://doi.org/10.2307/3213981
5. R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: the Chen--Stein method*, *Annals of Probability* 17 (1989), 9--25. https://doi.org/10.1214/aop/1176991491
