# Arbitrarily long attracting opinion cycles with three agents and seven confidence intervals

## Finding

**Theorem.** In the deterministic scalar set-based-confidence opinion model with synchronous unweighted averaging, for **every integer** \(p\ge 2\) there exists a bounded, open, symmetric confidence set \(\mathcal C_p\subset\mathbb R\), containing a neighborhood of \(0\) and having **at most seven connected interval components**, such that two stubborn agents holding opinions \(0\) and \(1\) and one ordinary agent have a **locally attracting periodic orbit of least period exactly \(p\)**. Its return multiplier, in the ordinary agent's opinion coordinate, is exactly \(2^{-p}\). The orbit persists with the same least period under sufficiently small symmetric changes of confidence-band endpoints retaining a neighborhood of zero and of the two distinct stubborn opinions. Consequently there is no uniform upper bound on attracting periods in this fixed three-agent, seven-interval class. Three agents are minimal for nonconstant periodicity under symmetric confidence sets containing a neighborhood of zero.

This is an existence and robustness theorem for a family of confidence sets depending on \(p\). It does **not** assert that one fixed confidence set admits periods of every order, or that every initial opinion enters the exhibited cycle.

## Assumptions and scope

An ordinary agent with current scalar opinion \(x\), with two stubborn agents permanently holding \(0\) and \(1\), regards herself as a neighbor and regards stubborn opinion \(a\in\{0,1\}\) as a neighbor exactly when \(a-x\in\mathcal C\). She updates to the arithmetic mean of her own opinion and all trusted stubborn opinions. This is the SCOD rule, with the special treatment of stubborn agents as in the initiating model. The two stubborn agents do not update; whether they regard each other as neighbors has no effect on the update.

For \(p\ge2\), set \(q=2^p-1\). Define an open confidence set by

\[
\begin{split}
\mathcal C_p=\{z\in\mathbb R:\ q|z|\in & [0,\tfrac12)
\ \cup\ (\tfrac32,2^{p-2}+\tfrac14)\\
&\cup\ (2^{p-1}-\tfrac14,2^{p-1}+\tfrac14)\\
&\cup\ (q-\tfrac54,q-\tfrac34)\}.
\end{split}
\]

The second interval is understood as empty when \(p=2\), and the last two intervals coincide in that case. Because the first condition is \(q|z|<1/2\), the resulting set is open at zero. It is symmetric, bounded, and a union of at most one central interval and three positive/negative interval pairs, hence at most seven intervals. Every displayed endpoint is rational. No asymmetric confidence rule, probabilistic updating, or extra agents are used.

## Proof

**1. Exact candidate cycle.** Set \(x_k=2^k/q\) for integers \(0\le k\le p-1\). All \(p\) points are distinct and belong to \((0,1)\). The intended confidence itinerary is: at \(x_0\), the ordinary agent trusts the stubborn opinion \(1\), but not \(0\); at each \(x_k\), \(1\le k\le p-1\), she trusts \(0\), but not \(1\).

**2. Verify the itinerary for every \(p\).** Symmetry gives \(-x\in\mathcal C_p\) if and only if \(x\in\mathcal C_p\). The scaled gaps are

\[
q x_k=2^k,\qquad q(1-x_k)=q-2^k.
\]

At \(k=0\), the scaled value \(1\) is excluded, while \(q-1\) belongs to the last displayed band. For \(1\le k\le p-2\), the even integer \(2^k\) lies strictly within the second band. The value \(2^{p-1}\) lies strictly inside the third band. For \(1\le k\le p-1\), the excluded values \(q-2^k\) are odd integers, all at least \(2^{p-1}-1\). If \(p\ge3\), the second band's upper endpoint satisfies

\[
2^{p-2}+\tfrac14<2^{p-1}-1;
\]

hence no excluded value falls in that band. Every other noncentral band is a radius-\(1/4\) interval around an even integer, while every excluded value is odd. The central band ends at \(1/2\), so it also excludes all these odd integers, including \(1\). The same reasoning holds when \(p=2\), with the empty second band. Thus the claimed neighbor selection holds **strictly** at each point, with no membership ties.

**3. Exact return and primitivity.** With exactly one stubborn opinion trusted, the update is the affine map \(x\mapsto x/2\) when the trusted opinion is \(0\), and \(x\mapsto(x+1)/2\) when it is \(1\). Consequently

\[
x_0\longmapsto x_{p-1}\longmapsto x_{p-2}
\longmapsto\cdots\longmapsto x_1\longmapsto x_0,
\]

because \((1+1/q)/2=2^{p-1}/q\) and \(x_k/2=x_{k-1}\). These \(p\) values are distinct, so the least period is exactly \(p\).

**4. Attraction and robustness.** At each orbit point, the quantities \(x_k\) and \(1-x_k\) lie a distance of at least \(1/(4q)\) from every confidence-set boundary (in the unscaled opinion variable). Hence the trust decisions remain constant on each neighborhood \(J_k=(x_k-\delta,x_k+\delta)\), where \(\delta=1/(16q)\). These neighborhoods are pairwise disjoint; the update maps each \(J_k\) into the next with slope exactly \(1/2\). The \(p\)-step return maps \(J_0\) strictly into itself and has slope \(2^{-p}\), proving local asymptotic attraction. Strict membership gaps also imply persistence for sufficiently small symmetry-preserving perturbations of the band endpoints (retaining the central neighborhood of zero) and anchor opinions: the same finite affine itinerary survives, and its return remains a contraction with a unique fixed point near \(x_0\). Disjoint neighborhoods preserve least period \(p\).

**5. Minimality of three agents.** For no stubborn agents or for a single stubborn opinion, the symmetric confidence-set convergence theorem in Zabarianska--Proskurnikov (2024, Theorem 1, under its neighborhood-of-zero hypothesis) precludes nonconstant periodic trajectories. If both agents in a two-agent system are stubborn, they do not move. Thus a nonconstant periodic trajectory with symmetric open confidence and stubborn anchors needs at least two stubborn agents and one ordinary agent, and the above construction attains three.

## Verification

The standalone standard-library script `verify.py` evaluates all membership inequalities, the exact period, strict endpoint margins, and the local multiplier using rational arithmetic for \(2\le p\le200\); it prints `VERIFY_OK`. This reproducibility computation checks 199 instances only. The infinite quantified statement follows from the exact parity, interval-separation, and affine-return proof above, **not** from finite testing.

For example, at \(p=5\), \(q=31\), the ordinary agent's exact cycle is

\[
\frac1{31}\to\frac{16}{31}\to\frac8{31}\to\frac4{31}\to\frac2{31}\to\frac1{31},
\]

with return multiplier \(1/32\). At each state exactly one stubborn opinion is trusted.

## Relationship to prior work

Zabarianska and Proskurnikov, *Opinion Dynamics with Set-Based Confidence: Convergence Criteria and Periodic Solutions* (arXiv:2408.01753v1, publicly submitted 2024-08-03), define the precise SCOD update in Section II and exhibit a period-three trajectory with two stubborn agents under a symmetric nonconvex confidence set (Example 4). Their Theorem 1 proves convergence with homogeneous stubborn opinions under symmetric confidence and a neighborhood-of-zero assumption. The source poses the question of when stubborn agents cause oscillations in Section V. The period-three example and the two-stubborn possibility are prior work, not contributions claimed here. The new statement provides **all least periods**, **local attraction and robustness**, and a **constant seven-interval complexity bound** independent of the period. None of these follows solely from the existence of one period-three orbit.

The later Zabarianska--Proskurnikov (2025) treatment of stubborn agents with **norm-ball** confidence sets concerns a different geometric class: the present sets are disconnected and nonconvex. Related general constructions for piecewise-contracting interval maps do not immediately supply the exact reciprocal-confidence membership constraints of a single symmetric SCOD confidence set; those constraints are checked here explicitly.

## Limitations

The confidence sets are tailored to the desired period and need not be convex or connected; no claim is made for interval or norm-ball confidence. Robustness is local, with the two stubborn opinions regarded as fixed parameters and only the ordinary opinion dynamically attracting. Neither uniqueness of the attracting cycle nor global basin size is claimed. The general period-construction idea may have analogues in piecewise-contraction literature; an exhaustive publication-priority guarantee is not claimed. The periodic-orbit construction has not been independently validated.

## References

1. I. Zabarianska and A. V. Proskurnikov, *Opinion Dynamics with Set-Based Confidence: Convergence Criteria and Periodic Solutions*, arXiv:2408.01753v1 (2024-08-03), https://arxiv.org/html/2408.01753v1 . Sections II--V, especially Example 4, Theorem 1 and the open problem on stubborn-agent oscillations.
2. I. Zabarianska and A. V. Proskurnikov, *Bounded Confidence Opinion Dynamics in Non-Euclidean Norms: Containment and Convergence with Stubborn Agents*, CoDIT 2025, pp. 1519--1524, DOI: 10.1109/CoDIT66093.2025.11321773. Accessible abstract/partial text; norm-ball rather than the nonconvex sets here.
3. C. Bernardo, C. Altafini, A. V. Proskurnikov and F. Vasca, *Bounded confidence opinion dynamics: A survey*, Automatica 159 (2024), 111302, DOI: 10.1016/j.automatica.2023.111302. General background; abstract examined.
4. American Mathematical Society, MSC2020 classification 91D30: Social networks; opinion dynamics, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=Network+dynamics .
