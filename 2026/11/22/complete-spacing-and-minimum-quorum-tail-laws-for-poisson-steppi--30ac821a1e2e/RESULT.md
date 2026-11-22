# Complete spacing and minimum-quorum tail laws for Poisson stepping-stone chains

## Finding

Let a one-way chain have \(n\ge2\) establishment stages, with nonnegative successive gap lengths \(d_1,\ldots,d_n\) summing to a prescribed total \(L\). On stage \(i\), conditional on successful establishment at the preceding site, the founding count is Poisson with mean \(a_i e^{-\lambda_i d_i}\), and passage succeeds if at least \(m_i\) founders arrive. Here \(a_i,\lambda_i>0\) and \(m_i\ge1\) is an integer. Distinct stages use independent conditional trials, and a successful stage is reset to its specified source output before the next stage. The probability of completing the chain is
\[
P_L(d)=\prod_{i=1}^n Q_{m_i}(a_i e^{-\lambda_i d_i}),\qquad
Q_m(u)=\Pr\{\operatorname{Pois}(u)\ge m\}.
\]

**Theorem (all-length design and exact long-range law).** For every \(L\ge0\) the above product has exactly one maximizing gap vector. Define
\[
h_m(u)=\frac{uQ_m'(u)}{Q_m(u)}
=\frac{m}{\displaystyle\sum_{j=0}^{\infty}\frac{m!}{(m+j)!}u^j},\qquad
c_i=\lambda_i h_{m_i}(a_i),\quad b_i=\lambda_i m_i,\quad b=\min_i b_i.
\]
For \(L>0\) there is exactly one \(t_L\in(\min_i c_i,b)\) such that the following lengths sum to \(L\):
\[
d_i(t)=\begin{cases}
0,&t\le c_i,\\
\lambda_i^{-1}\log\bigl(a_i/h_{m_i}^{-1}(t/\lambda_i)\bigr),& c_i<t<b_i.
\end{cases}\tag{1}
\]
The second branch is needed only when \(t<b\le b_i\); hence it is always well-defined for \(t=t_L\). The optimizer is \(d_i^*(L)=d_i(t_L)\). As \(L\) increases, the gaps activate in increasing order of their entry costs \(c_i\) whenever \(c_i<b\), never deactivate, and a stage with \(c_i\ge b\) always has zero optimal gap. Tied entry costs activate simultaneously.

Put \(M=\{i:b_i=b\}\). For \(i\notin M\) set \(d_i^\infty=0\) when \(c_i\ge b\), and otherwise set
\[
d_i^\infty=\lambda_i^{-1}\log\bigl(a_i/h_{m_i}^{-1}(b/\lambda_i)\bigr),
\qquad D=\sum_{i\notin M}d_i^\infty.
\]
Every \(i\notin M\) satisfies \(d_i^*(L)\to d_i^\infty<\infty\), whereas every \(i\in M\) satisfies \(d_i^*(L)\to\infty\). Writing
\[
H=\sum_{i\in M}\lambda_i^{-1},\quad
K_i=\frac{\lambda_i m_i}{m_i+1},\quad
W=\sum_{i\in M}\lambda_i^{-1}\log(a_i K_i),
\]
the sharper asymptotics are
\[
 b-t_L=\exp\bigl((W+D-L)/H\bigr)(1+o(1)),
\]
\[
 d_i^*(L)=\frac{L-D}{\lambda_i H}
 +\frac{1}{\lambda_i}\left(\log(a_i K_i)-\frac WH\right)+o(1),\quad i\in M,
\tag{2}
\]
and the optimized crossing probability has the **exact leading coefficient**
\[
\max_{\substack{d_i\ge0\\\sum d_i=L}}P_L(d)
\sim C e^{-bL},\qquad
C=e^{bD}\prod_{i\in M}\frac{a_i^{m_i}}{m_i!}
\prod_{i\notin M}Q_{m_i}(a_i e^{-\lambda_i d_i^\infty}).\tag{3}
\]
Thus the long-distance exponential loss is determined by the least *attenuation-rate times founding quorum*, not by the largest founding quorum or the poorest initial passage probability. If several stages share this least product, their shares of the large distance converge to \(\lambda_i^{-1}/H\).

**Concrete three-stage example.** Let \(m=(1,2,3)\), \(a=(3,3,3)\), and \(\lambda=(1,1,1)\). The unique optimum initially puts the whole distance on the one-founder stage. Stage 2 first receives positive distance at
\[
L_*=\log(3/u_*),\qquad \frac{u_*}{e^{u_*}-1}=\frac{9}{e^3-4},\qquad
L_*=1.033440586918726\ldots .\tag{4}
\]
Stage 3 never receives positive distance, even for arbitrarily large \(L\). Meanwhile the second gap grows monotonically but converges to
\[
\log(3/v_*)=0.514564753997\ldots,\qquad e^{v_*}=1+v_*+v_*^2,\quad v_*>0.\tag{5}
\]
The first gap therefore grows as \(L-0.514564753997\ldots+o(1)\). The limiting arrangement is not equally spaced even asymptotically.

## Assumptions and scope

The result optimizes **completion probability along one prescribed one-way chain**, not time to expansion, expected abundance, or multi-path network reachability. The Poisson stage trials, fixed quorum integers, exponentially attenuated conditional means, reinitialization after each successful establishment, and absence of extinction or competing pathways are part of the model. \(L\) is any nonnegative real number, zero gaps are permitted, and all stage parameters remain fixed while \(L\) varies. Distances and attenuation rates are expressed in consistent fixed numerical units. This makes the boundary solution an idealized co-location limit. With prescribed minimum gaps \(d_i\ge\delta_i\ge0\), the theorem applies without change to excess lengths \(d_i-\delta_i\), baseline means \(a_i e^{-\lambda_i\delta_i}\), and excess total \(L-\sum_i\delta_i\), provided this is nonnegative.

## Proof

**Poisson elasticity.** For \(u>0\), differentiation of the Poisson survival series gives \(Q_m'(u)=e^{-u}u^{m-1}/(m-1)!\). Dividing the positive tail series gives the displayed identity for \(h_m\). Each coefficient in its denominator is positive, and at least one term of positive degree is present. Therefore \(h_m:(0,\infty)\to(0,m)\) is continuous, strictly decreasing, with \(h_m(u)\to m\) as \(u\downarrow0\) and \(h_m(u)\to0\) as \(u\to\infty\). The inverse in (1) is consequently single-valued on \((0,m)\).

**Strict concavity and the finite optimization.** Put \(F_i(d)=\log Q_{m_i}(a_i e^{-\lambda_i d})\). Direct differentiation gives
\[
F_i'(d)=-\lambda_i h_{m_i}(a_i e^{-\lambda_i d}).
\]
Since the argument of \(h_{m_i}\) strictly decreases with \(d\) and \(h_{m_i}\) strictly decreases with its argument, \(F_i'\) strictly decreases with \(d\). Hence each \(F_i\) is strictly concave on \([0,\infty)\), and the sum is strictly concave on the compact simplex \(\{d_i\ge0,\sum_i d_i=L\}\). A unique maximizer therefore exists, including at \(L=0\).

The positive marginal loss \(-F_i'(d)\) is strictly increasing from \(c_i\) to \(b_i\). Thus the unique concave-program optimality conditions are: at every positive gap, its marginal loss equals one common multiplier \(t\); at every zero gap, its initial marginal loss is at least \(t\). For \(\min_i c_i<t<b\), the formula (1) is exactly the solution of these conditions. The sum \(S(t)=\sum_i d_i(t)\) is continuous and strictly increasing from \(0\) to \(\infty\): at least one stage with \(b_i=b\) diverges as \(t\uparrow b\), and some stage is active for every \(t>\min_i c_i\). Therefore \(S(t_L)=L\) has exactly one solution. The Karush–Kuhn–Tucker sufficiency follows directly from strict concavity, not from numerical optimization. Since \(t_L\) increases strictly with \(L\), each gap is nondecreasing and the activation statement follows. In particular, a stage with \(c_i\ge b\) never activates because \(t_L<b\).

**Long-distance limit.** The preceding inversion gives \(t_L\uparrow b\). When \(b_i>b\), its inverse gap has the finite limit specified above or remains zero; when \(b_i=b\), its inverse tends to infinity. Expanding the exact positive denominator at \(u=0\) yields
\[
 h_m(u)=m-\frac{m}{m+1}u+O(u^2),\qquad
 Q_m(u)=\frac{u^m}{m!}(1+O(u)).
\]
For \(i\in M\), setting \(u_i=a_i e^{-\lambda_i d_i^*}\) therefore gives \(b-t_L=K_i u_i(1+O(u_i))\). Taking logarithms and summing the lengths for these stages shows
\[
L-D=W-H\log(b-t_L)+o(1),
\]
which proves (2) and the multiplier asymptotic. For \(i\in M\), the probability expansion has factor \((a_i^{m_i}/m_i!)e^{-\lambda_i m_i d_i^*}(1+o(1))\). Since \(\lambda_i m_i=b\) on \(M\) and \(\sum_{i\in M}d_i^*=L-D+o(1)\), multiplying these factors and the finite limits at \(i\notin M\) yields (3).

**Three-stage example.** Write \(E=e^3\). The initial marginal losses are \(c_1=3/(E-1)\), \(c_2=9/(E-4)\), and \(c_3=27/[2(E-17/2)]\). The elementary bound \(20<E<21\) gives \(c_1<c_2<1<c_3\). The limiting loss is \(b=1\), so only the first two gaps ever activate. Before the second activates, \(d_1=L\); equality of its marginal loss to \(c_2\) yields (4). At the limit, the second marginal loss reaches \(1\), yielding the unique positive solution \(v_*\) in (5). Strict decrease of \(h_2\) proves uniqueness of that positive solution, while strict increase of \(d_2(t)\) proves monotonic approach to its finite limit. The decimal evaluations are reproducible by `verify.py`; they are not needed for the exact claims.

## Verification

Run `python verify.py` using Python's standard library. It checks the Poisson-tail series, strict elasticity inequalities on finite grids, the exact-example thresholds and active sets, the marginal-cost equalities, and comparisons against randomized competing allocations. The analytical proof above establishes all parameter quantifiers and long-distance statements; finite checks do not certify them independently. No external symbolic package, empirical data, or unpublished certificate is required.

## Relationship to prior work

Hodgson, Thomas, Dytham, Travis and Cornell (2012) optimized and simulated range-shift **speed** in patch networks, reporting broadly favorable regular placement of homogeneous stepping stones and evaluating up to eight patches. Their full article's Methods and Results were inspected; its outcome is not the probability that every stage clears a heterogeneous Poisson quorum, and it does not state the all-length water-filling or minimum-effective-quorum asymptotic law.

Saura, Bodin and Fortin (2014, accepted manuscript available in 2013) used multiple-generation stepping-stone paths with binomial founder-count requirements and selected maximum-product paths through **given spatial networks**. The accessible Methods, Results and Discussion were inspected. The binomial path model motivates the discrete establishment threshold, but it does not optimize continuous consecutive distances under a fixed chain length or derive the present active-set and asymptotic spacing classifications. The present result should not be interpreted as disproving the homogeneous, approximately regular-spacing conclusions for different objectives or assumptions. The underlying separable concave optimality conditions are standard; the scientific content claimed here is their sharp Poisson-quorum spatial specialization, stage-activation cutoff, and the explicit long-range constant.

## Limitations

The chain product is a conditional success model, not a full stochastic metapopulation with repeated attempts, extinction, direct source-to-target routes, disperser dependence, or competition. At zero gap, distinct sites may be interpreted as co-located idealized stages; hard physical separation is handled by the minimum-gap normalization stated above. A full network allowing alternative routes could invalidate the optimization classification. The result makes no field-level recommendation and does not establish experimental predictive accuracy. Priority is qualified by the possibility of a broader separable concave allocation theorem already presenting an equivalent Poisson-tail asymptotic as a corollary; the source comparisons below identify the investigated literature but do not prove universal novelty.

## References

1. Hodgson, J. A., Thomas, C. D., Dytham, C., Travis, J. M. J., Cornell, S. J. (2012), *The Speed of Range Shifts in Fragmented Landscapes*, PLOS ONE **7**(10), e47141. https://doi.org/10.1371/journal.pone.0047141 (first public publication 2012-10-17).
2. Saura, S., Bodin, Ö., Fortin, M.-J. (2014), *Stepping stones are crucial for species' long-distance dispersal and range expansion through habitat networks*, Journal of Applied Ecology **51**, 171–182. https://doi.org/10.1111/1365-2664.12179 (accepted-manuscript first published 2013-10-01).
