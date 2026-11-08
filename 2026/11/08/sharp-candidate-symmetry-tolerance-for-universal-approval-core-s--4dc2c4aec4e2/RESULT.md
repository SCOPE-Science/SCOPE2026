# Sharp candidate-symmetry tolerance for universal approval-core stability

## Finding

**Theorem (simultaneous Hare-core stability and sharp symmetry tolerance).** Fix integers \(m>k\ge1\) and \(n\ge1\). Voter \(i\) independently draws an approval subset \(A_i\subseteq C\), where \(|C|=m\), from an arbitrary distribution \(P_i\) on subsets of \(C\); neither identical voter laws nor independent candidate approvals are assumed. Define the averaged law and its candidate-permutation symmetrization by

\[
\bar P=\frac1n\sum_{i=1}^nP_i,\qquad
Q=\frac1{m!}\sum_{\sigma\in S_m}\sigma_{\#}\bar P,\qquad
\varepsilon=d_{\mathrm{TV}}(\bar P,Q).
\]

For \(1\le t\le k\), put

\[
 b_{k,t}=\frac1{\lfloor k/t\rfloor+1},\qquad
 D(a\Vert b)=a\log\frac ab+(1-a)\log\frac{1-a}{1-b},
\]

with the continuous convention \(D(1\Vert b)=\log(1/b)\). If

\[
\varepsilon<\varepsilon_k^*:=\frac1{k(k+1)},
\]

then, simultaneously for **every** size-\(k\) committee, the standard integral Hare core holds with probability at least

\[
\boxed{1-\binom mk\sum_{t=1}^k\binom mt
\exp\!\left[-nD\left(\frac tk\Big\Vert b_{k,t}+\varepsilon\right)\right].}
\]

In particular, if \(m,k\) are fixed and the same strict upper bound \(\varepsilon<\varepsilon_k^*\) holds uniformly as \(n\) grows, the probability that **all** committees are core stable tends to one exponentially fast. This includes arbitrary independent, candidate-exchangeable ballots, without assuming independence of approvals within a ballot.

The tolerance \(\varepsilon_k^*\) is sharp across all \(m>k\): at equality one can have a failure probability bounded away from zero, and above it (for \(k\ge2\)) one can have failure with probability tending to one. In the unbiased one-approval model on \(m=k+1\) candidates, the failure probability has the exact logarithmic rate

\[
\boxed{\lim_{n\to\infty}-\frac1n\log\Pr(\text{some committee is outside the core})
=D\left(\frac1k\Big\Vert\frac1{k+1}\right).}
\]

## Assumptions and scope

A committee is a set \(W\subseteq C\) of size exactly \(k\). Approval utility is \(u_i(B)=|A_i\cap B|\) for any \(B\subseteq C\). The **integral Hare core** rules out every nonempty coalition \(S\) with a proposal \(T\subseteq C\) satisfying \(|S|k\ge n|T|\) and \(u_i(T)>u_i(W)\) for every \(i\in S\). A nonempty proposal with \(|T|>k\) cannot be afforded; an empty proposal cannot strictly improve positive or zero approval utility. Thus the relevant proposal sizes are \(1\le|T|\le k\).

Here \(S_m\) permutes candidate labels. The symmetrized law \(Q\) is candidate-exchangeable, meaning it is invariant under every permutation of \(C\). The total variation distance between two probability laws on approval subsets is \(d_{\mathrm{TV}}(P,Q)=\sup_E|P(E)-Q(E)|\). The voter ballots are mutually independent but may have different laws and arbitrary dependence among candidates within each ballot.

The probability guarantee is a finite-sample statement for each \(n,m,k\). For a sequence of elections with growing \(m\) or \(k\), the displayed bound remains valid but does not itself imply convergence unless its right-hand error term tends to zero.

## Proof

**1. Exchangeable one-voter comparison.** Fix a size-\(k\) committee \(W\), a proposal \(T\) of size \(t\le k\), and a candidate-exchangeable random approval set \(A\). Let \(h=|W\cap T|\) and \(s=t-h\). If \(s=0\), then the proposal cannot strictly improve on \(W\). Otherwise let \(r=\lfloor k/t\rfloor\ge1\). The set \(W\setminus T\) has \(k-h\) elements, and it contains \(r\) pairwise disjoint blocks \(B_1,\ldots,B_r\), each of size \(s\), because

\[
rs=r(t-h)\le k-h.
\]

Put \(B_0=T\setminus W\), also of size \(s\). The \(r+1\) approval counts \(|A\cap B_j|\) are exchangeable, although they need not be independent. If \(u_A(T)>u_A(W)\), cancellation on \(T\cap W\) gives

\[
|A\cap B_0|>|A\cap(W\setminus T)|\ge |A\cap B_j|
\quad(1\le j\le r).
\]

So block \(B_0\) is a **unique strict maximum** among the \(r+1\) exchangeable block counts. At most one block can be a strict maximum, and all blocks have equal chance of that event. Therefore

\[
\Pr_Q(u_A(T)>u_A(W))\le\frac1{r+1}=b_{k,t}.
\]

**2. Strict gap and perturbation.** Since \(r=\lfloor k/t\rfloor\), integer arithmetic gives \((r+1)t-k\ge1\). Consequently

\[
\frac tk-b_{k,t}
=\frac{(r+1)t-k}{k(r+1)}
\ge\frac1{k(r+1)}\ge\frac1{k(k+1)}.
\]

The minimum gap over \(t=1,\ldots,k\) is exactly \(1/[k(k+1)]\), attained at \(t=1\). Write \(E_{W,T}=\{A:u_A(T)>u_A(W)\}\). By total variation and Step 1,

\[
\bar p_{W,T}:=\frac1n\sum_iP_i(E_{W,T})
=\bar P(E_{W,T})\le Q(E_{W,T})+\varepsilon\le b_{k,t}+\varepsilon<\frac tk.
\]

**3. Independent-voter concentration and simultaneous core stability.** Put \(X_{W,T}=\sum_i\mathbf1_{\{A_i\in E_{W,T}\}}\). For \(\lambda>0\), independence and concavity of \(p\mapsto\log(1+p(e^\lambda-1))\) give

\[
\mathbb E e^{\lambda X_{W,T}}
=\prod_i(1+P_i(E_{W,T})(e^\lambda-1))
\le(1+\bar p_{W,T}(e^\lambda-1))^n
\le(1+(b_{k,t}+\varepsilon)(e^\lambda-1))^n.
\]

Chernoff optimization at the threshold \(nt/k\) yields

\[
\Pr\left(X_{W,T}\ge\frac{nt}{k}\right)
\le\exp\left[-nD\left(\frac tk\Big\Vert b_{k,t}+\varepsilon\right)\right].
\]

This remains valid for \(t=k\), using \(D(1\Vert b)=\log(1/b)\). If a coalition blocks \(W\) with proposal \(T\), all its voters belong to the improvement set and the affordable coalition has at least \(nt/k\) members. Hence a blocking event is contained in the displayed tail event. There are \(\binom mk\) committees and \(\binom mt\) proposals of size \(t\). A union bound gives the theorem's finite-sample statement. For fixed \(m,k\) and a uniform strict bound on \(\varepsilon\), every exponent is positive and the claimed exponential convergence follows.

**4. Sharpness and exact one-approval rate.** Set \(m=k+1\), and let each voter approve **exactly one** candidate, independently. First take all candidates equally likely. A committee \(W=C\setminus\{c\}\) gives utility zero only to voters approving \(c\). Because every voter approves a single candidate, no other voter can strictly improve beyond utility one. Thus \(W\) is blocked if and only if at least \(n/k\) voters approve \(c\), with the singleton proposal \(T=\{c\}\) sufficient. Consequently

\[
\{\text{some size-}k\text{ committee is not core stable}\}
=\left\{\max_{c\in C}N_c\ge\frac nk\right\},
\]

where \((N_c)_{c\in C}\) is multinomial with \(n\) trials and uniform cell probabilities \(1/(k+1)\). A union bound and a single-candidate lower bound sandwich this event's probability between a \(\mathrm{Bin}(n,1/(k+1))\) upper tail at \(n/k\) and \((k+1)\) times that tail. Standard binomial large deviations (including the endpoint case \(k=1\)) give the asserted exact logarithmic rate.

For sharpness of the total-variation tolerance, instead let a designated candidate \(c_*\) be the unique approval with probability \(p_*\), and each other candidate with probability \((1-p_*)/k\). The symmetrization is uniform on one-element ballots and

\[
\varepsilon=p_*-\frac1{k+1}\quad\text{when }p_*\ge\frac1{k+1}.
\]

At \(p_*=1/k\), this is exactly \(\varepsilon_k^*\). For \(k\ge2\), the count of votes for \(c_*\) is \(\mathrm{Bin}(n,1/k)\), so the probability it reaches \(n/k\) tends to \(1/2\) by the central limit theorem. Each other candidate has probability \((k-1)/k^2<1/k\), so the probability that any other committee is blocked tends to zero. Therefore the probability that **all** committees are core stable tends to \(1/2\) at equality. If \(p_*>1/k\), the designated candidate reaches quota with probability tending to one, so the probability all committees are core stable tends to zero. For \(k=1\), equality gives \(p_*=1\) and certain failure of universal core stability. Thus no uniform guarantee extending the strict symmetry-tolerance inequality is possible.

## Verification

Run `python3 verify.py` using the included Python 3 standard-library program. It checks, using exact rational arithmetic, every candidate-committee and proposal pair and every exchangeable fixed-cardinality ballot orbit for \(2\le m\le8\) (446,363 comparisons), and verifies the finite one-approval core event directly on 6,678 labeled ballot profiles for \(1\le k\le3\), \(m=k+1\), \(1\le n\le6\). It additionally checks 14 exact-rational sharp-tolerance identities.

These finite tests guard definitions and boundary arithmetic. The inequalities for arbitrary \(m,k,n\), arbitrary within-ballot correlation, independent heterogeneous voters, and the large-deviation/central-limit limits are established by the mathematical proof above, **not** by extrapolating enumeration.

## Relationship to prior work

Becker, Greger and Peters (2026) establish that at least one Hare-core committee exists for every deterministic approval election, and construct one using harmonic entropy; their theorem is an existence statement, not a simultaneous high-probability guarantee for all committees. The present result concerns the contrasting selection-power question for approximately candidate-symmetric voter populations, with a sharp total-variation tolerance. Peters (2025) proves deterministic core-existence guarantees for restricted committee sizes and does not supply a random-population concentration theorem. Goel, Jiang and Zhou (2026) study fractional Nash-core solutions and small-voter deterministic cases, again without a random candidate-symmetry threshold.

Chen and Hatschka (2026) identify the committee core with the non-transferable-utility core under AV/PAV/SAV utility transformations and analyze existence and computational complexity, not random-population symmetry; the present theorem applies to that equivalent non-transferable core definition.

Han and coauthors (2025) analyze probability phase transitions for **average justified representation** under independent Bernoulli candidate approvals; they explicitly distinguish that axiom from core stability. Their stochastic representation results do not establish the universal Hare-core stability probability law proved here. In particular, the present theorem covers correlated approvals within each ballot and nonidentical voters, but does not address average justified representation.

## Limitations

The result concerns the **integral Hare core**, not the fractional core, core+, or the Droop quota. It assumes mutually independent voter ballots; no concentration is asserted for arbitrary dependence across voters. The strict bound on the total-variation distance is sufficient and sharp as a uniform guarantee over all candidate counts and approval laws, not claimed to be necessary for every individual distribution. For growing committee and candidate counts, the finite-sample union bound must be evaluated rather than assuming exponential convergence. Primary-source and research-index searches cannot exclude all unindexed equivalent findings; independent validation has not been performed.

## References

- P. Becker, M. Greger and D. Peters. *Existence of the Core in Approval-Based Committee Elections*. arXiv:2609.11912, first public September 10, 2026. https://arxiv.org/abs/2609.11912
- D. Peters. *The Core of Approval-Based Committee Elections with Few Seats*. arXiv:2501.18304, first public January 30, 2025. https://arxiv.org/abs/2501.18304
- A. Goel, Z. Jiang and C. Zhou. *Nash Core in Multiwinner Election*. arXiv:2609.00486, first public August 31, 2026. https://arxiv.org/abs/2609.00486
- Q. Han, B. Tao, L. Xia, C. Zhang and H. Zhou. *Likelihood of the Existence of Average Justified Representation*. arXiv:2510.18718, first public October 21, 2025. https://arxiv.org/abs/2510.18718
- J. Chen and C. Hatschka. *Multi-Winner Voting Games in TU and NTU: When is the Core Always Non-Empty?* arXiv:2605.22528, first public May 21, 2026. https://arxiv.org/abs/2605.22528
