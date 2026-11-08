# Gaussian-to-exponential leaf-to-root hitting laws for optimal two-choice walks on regular trees

## Finding

For every integer \(b\ge2\) and height \(h\ge1\), consider the complete rooted \(b\)-ary tree of height \(h\), with all leaves at depth \(h\). Start a discrete-time controlled walk at any leaf. At each step two neighbors are sampled independently and uniformly, with replacement; the controller must choose one offered neighbor. Let \(T_{b,h}\) be the first hitting time of the root under the policy that chooses the parent whenever a parent is offered, breaking other ties arbitrarily.

**Theorem (stochastic optimality and fluctuation transition).** The parent-first policy simultaneously maximizes the probability of reaching the root by every fixed deadline, among all adaptive and randomized strategies. Consequently its root-hitting time is stochastically minimal. Write
\[
 p_b=\frac{2b+1}{(b+1)^2},\qquad q_b=\frac{b^2}{(b+1)^2},\qquad r_b=\frac{q_b}{p_b}.
\]
Its exact mean, for all \(b\ge2\) and \(h\ge1\), is
\[
 \mathbb E T_{b,h}=\frac{h}{p_b-q_b}-\frac{2p_bq_b}{(p_b-q_b)^2}(1-r_b^h).
\]
The denominator never vanishes for an integer \(b\ge2\). The **binary tree** has the Gaussian law
\[
 \mathbb E T_{2,h}=9h-40\bigl(1-(4/5)^h\bigr),\qquad
 \frac{T_{2,h}-9h}{\sqrt{720h}}\ \xrightarrow[h\to\infty]{\mathrm d}\ N(0,1).
\]
For every fixed integer \(b\ge3\), the **higher-branching trees** instead have a metastable exponential law:
\[
 \mathbb E T_{b,h}\sim
 \frac{2b^2(2b+1)}{(b^2-2b-1)^2}
 \left(\frac{b^2}{2b+1}\right)^h,
 \qquad
 \frac{T_{b,h}}{\mathbb E T_{b,h}}
 \xrightarrow[h\to\infty]{\mathrm d}\operatorname{Exp}(1).
\]
Thus the optimal hitting time is concentrated on a linear scale for \(b=2\), but has exponential height-scale and nonvanishing relative fluctuations for every \(b\ge3\). The threshold corresponds to switching the controlled radial drift from inward to outward. The mean formula and fluctuation laws concern the walk started at depth \(h\), not a worst-case hitting time between arbitrary vertices.

A complete finite-height probability-generating function is also explicit by a continued fraction. For \(0\le z\le1\), define \(J_h(z)=z\), and recursively
\[
 J_i(z)=\frac{zp_b}{1-zq_b J_{i+1}(z)}\quad (i=h-1,h-2,\ldots,1).
\]
Then
\[
 \mathbb E[z^{T_{b,h}}]=\prod_{i=1}^{h}J_i(z).
\]

## Assumptions and scope

The graph is finite, unweighted and exactly \(b\)-ary to depth \(h\), with all sampled neighbors independent and uniform *with replacement*. Decisions may use the full observed history and randomization. Time is measured in discrete moves, with no holding. The root is absorbing solely for purposes of its first hitting time. In the formula for the generating function, the value at \(z=0\) is defined by continuity. The limit holds with \(b\) fixed and \(h\to\infty\); no claim is made for growing \(b\).

## Proof

**1. Simultaneous optimality for all deadlines.** For a given deadline \(t\), let \(u_i(t)\) be the supremum over all admissible strategies of the probability of hitting the root within \(t\) steps, starting at an arbitrary vertex at depth \(i\). Rooted-tree symmetry makes this independent of the particular vertex. Every path from depth \(i+1\) to the root must first visit depth \(i\). By the strong Markov property for the fresh neighbor offers and the fact that \(u_i(t)\) is nondecreasing in the time allowance, \(u_{i+1}(t)\le u_i(t)\) for every \(t\). At a depth-\(i\) vertex, the finite-horizon Bellman recursion chooses whichever of the two sampled neighbors has larger \(u_j(t-1)\). The parent is at depth \(i-1\), while any child is at depth \(i+1\); therefore the parent is always an optimal choice when offered. This argument applies at every remaining horizon and hence produces a single stationary parent-first policy optimal for *every* deadline. Such first-order stochastic dominance minimizes the expectation as well.

**2. Radial chain, exact mean, and generating function.** Until root absorption, the depth is a nearest-neighbor chain on \(\{0,1,\ldots,h\}\). At each interior depth it moves inward with probability \(p_b=1-(b/(b+1))^2\) and outward with probability \(q_b\). From the last depth it moves inward with probability one. Let \(m_i\) denote its expected time to hit zero from depth \(i\), and put \(d_i=m_i-m_{i-1}\). First-step conditioning gives \(d_h=1\) and \(p_b d_i-q_b d_{i+1}=1\) for \(1\le i<h\). Writing \(\delta=p_b-q_b\ne0\) and \(r=q_b/p_b\), backward substitution yields
\[
 d_i=\frac1\delta-\frac{2q_b}{\delta}r^{h-i}.
\]
Summing \(d_i\) proves the displayed exact mean. For the generating function, let \(J_i(z)\) denote the generating function of the time to first move from depth \(i\) to depth \(i-1\). At the leaf, \(J_h(z)=z\). From any interior depth, either the immediate inward move succeeds, or an outward move requires an independent return from depth \(i+1\) before the attempt can be repeated. Thus \(J_i=z(p_b+q_bJ_{i+1}J_i)\), proving the continued fraction. Successive downward crossing times are independent by strong Markov, so their generating functions multiply.

**3. Gaussian fluctuations for binary branching.** At \(b=2\), \(p=5/9\), \(q=4/9\), and \(p-q=1/9\). Consider the *unreflected* biased nearest-neighbor walk on the integers, started from height \(h\) and stopped at zero. Its hitting time \(S_h\) is the sum of \(h\) independent identically distributed downward one-level passage times, each having mean \(1/(p-q)=9\) and variance \(4pq/(p-q)^3=720\), as obtained by differentiating the one-level generating-function equation \(J=z(p+qJ^2)\). These passage times have exponential moments near the origin because \(p>q\). The usual i.i.d. central limit theorem therefore applies to \(S_h\).

Couple this unreflected walk and the reflected depth walk with identical increments whenever they coincide below the reflecting height. At the height \(h\), the latter is forced inward, while the former may move outward; whenever their positions differ, their gap is a nonnegative even integer and cannot reverse order in one step. Hence \(T_{2,h}\le S_h\) pathwise. The exact means give
\[
 0\le\mathbb E(S_h-T_{2,h})=40\bigl(1-(4/5)^h\bigr)\le40.
\]
Consequently \((S_h-T_{2,h})/\sqrt h\to0\) in \(L^1\); Slutsky's theorem yields the stated Gaussian law.

**4. Exponential fluctuations for higher branching.** For fixed \(b\ge3\), set \(p=p_b<q=q_b\), \(\rho=p/q<1\), and \(\delta=q-p>0\). Regenerate the depth chain whenever it returns to the reflecting leaf \(h\). One cycle consists of the obligatory first step \(h\to h-1\) and subsequent steps until first hitting \(\{0,h\}\); a cycle is successful if it ends at zero. Each attempted cycle has the same joint distribution of duration \(C_h\) and success indicator \(I_h\), independent over repeated failures. The standard gambler's-ruin difference equation, with boundary values one at zero and zero at \(h\), gives its success probability
\[
 \alpha_h=\Pr(I_h=1)=\frac{(1-\rho)\rho^{h-1}}{1-\rho^h}.
\]
An outward-drifting walk on the unrestricted integer line, started at the equivalent position \(h-1\), hits \(h\) in finite time with an exponential moment. Stopping sooner when zero is reached bounds \(C_h\) by one plus that unrestricted upward passage time, so \(\sup_h\mathbb E C_h^2<\infty\). As \(h\to\infty\), the lower barrier recedes from the starting point, so by coupling and dominated convergence
\[
 \mathbb E C_h\longrightarrow \ell=1+\frac1{q-p}=\frac{2q}{q-p}.
\]
The geometric number of cycles and Wald's identity give the exact identity \(\mathbb E T_{b,h}=\mathbb E C_h/\alpha_h\), recovering the previously stated asymptotic constant. For a fixed \(s\ge0\), put \(t=s/\mathbb E T_{b,h}\), and define \(A_h(t)=\mathbb E[e^{-tC_h}\mathbf1_{I_h=0}]\), \(B_h(t)=\mathbb E[e^{-tC_h}\mathbf1_{I_h=1}]\). Conditioning on the first cycle gives
\[
 \mathbb E[e^{-tT_{b,h}}]=\frac{B_h(t)}{1-A_h(t)}.
\]
Because \(\alpha_h\to0\), the uniform second-moment bound implies \(B_h(t)=\alpha_h+o(\alpha_h)\) and \(1-A_h(t)=\alpha_h(1+s)+o(\alpha_h)\), where \(t=s\alpha_h/\mathbb E C_h\). Their ratio converges to \(1/(1+s)\), the Laplace transform of \(\operatorname{Exp}(1)\). Finally substituting \(\rho=(2b+1)/b^2\) into \(\mathbb E T_{b,h}\) yields the stated asymptotic constant. This completes the proof.

## Verification

The accompanying standalone program `verify.py` constructs actual labeled rooted trees (not merely the radial reduction), solves the independent finite-state hitting-time linear equations, and compares the results to the rational mean formula. It separately performs exact finite-horizon Bellman maximization over all offered ordered pairs, comparing with parent-first control at every state and deadline for nine tree instances. Finally it checks the finite continued-fraction generating function against an independently solved tridiagonal absorbing-chain system at two rational evaluation points per instance. Its additional large-height identities test the mean/renewal asymptotics; these tests supplement, and do not replace, the proof of the infinite-height laws.

To reproduce with Python 3, NumPy, and SymPy installed, run `python verify.py`. It reports 2,538 exact state/deadline and generating-function checks for the listed finite instances. The polynomial-size linear solves are numerical cross-checks with explicit tolerance, while exact Bellman and generating-function checks use rational arithmetic.

## Relationship to prior work

Georgakopoulos, Haslegrave, Sauerwald and Sylvester introduced and analyzed two-offer choice random walks in arXiv:1911.05170 (first posted 2019-11-12). Their Proposition 3.4 supplies a subcubic adjacent-target mean bound using the inward probability \(5/9\); Section 5 remarks that on the infinite four-regular tree the choices remain outward-biased. Those statements identify the two drift regimes qualitatively, but neither states the exact finite rooted-tree leaf-to-root generating function nor the Gaussian-versus-exponential fluctuation laws under the deadline-optimal strategy. The present argument makes this distinction precise for complete regular rooted trees.

Zhang (2019) gives general moments of first hitting times for continuous-time birth-death processes on trees. In particular, the exact mean is compatible with general first-passage recurrences, and is **not** claimed as an independently new technique; the claimed distinct object is the specific optimal adaptive two-offer walk, its joint all-deadline optimality, and the two contrasting depth-asymptotic distributions. Generic gambler's ruin, renewal, and central-limit tools used in the proof are classical, not asserted as inventions.

## Limitations

The threshold between \(b=2\) and \(b\ge3\) in terms of drift direction is already implicit in the 2019 choice-random-walk work; the new contribution is the exact deadline-optimal finite law and the **distributional** classification, not that elementary drift sign. The results do not cover trees with uneven branching, a growing branching factor, nonuniform neighbor proposals, or walk cover times. General birth-death or metastability theory could contain equivalent specialization results; historical priority has not been independently certified. Finite computational checks cannot prove the limits in \(h\).

## References

1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald, and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170, first posted 2019-11-12, https://arxiv.org/abs/1911.05170. See Proposition 3.4, Section 5 and the general hitting-time strategy framework in Section 7.
2. Y. Zhang, *Moments of first hitting times for birth-death processes on trees*, Frontiers of Mathematics in China 14 (2019), 833–854, https://doi.org/10.1007/s11464-019-0784-6. See Theorem 1.1 and the first-moment recurrences.
3. Classical gambler's ruin, renewal-process Laplace transforms, and the i.i.d. central limit theorem (all used with explicit derivations above).
