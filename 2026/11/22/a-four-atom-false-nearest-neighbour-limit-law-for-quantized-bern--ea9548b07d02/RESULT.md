# A four-atom false-nearest-neighbour limit law for quantized Bernoulli dynamics

## Finding
For every bias \(0<p<1\), let \((X_j)_{j\in\mathbb Z}\) be the two-sided independent Bernoulli process with \(\Pr(X_j=1)=p\), considered as a deterministic left shift with invariant Bernoulli measure, observed through the continuous binary sensor \(h(x)=x_0\). Apply the usual scalar-delay false-nearest-neighbour (FNN) ratio test at delay length one to the sample \(X_0,\ldots,X_n\). Among tied nearest neighbours, choose the smallest *different* sample index. For every fixed positive ratio and amplitude tolerance, the fraction \(F_n\) of false neighbours converges almost surely to a random variable \(L_p\).

Writing \(q=1-p\), this limit has the **exact four-atom law**
\[
\begin{array}{c|cccc}
\ell &p&q&2pq&p^2+q^2\\ \hline
\Pr(L_p=\ell)&q^2&p^2&pq&pq
\end{array}
\]
when \(p\ne 1/2\). At the fair bias \(p=1/2\), these four atoms coincide and \(L_{1/2}=1/2\) almost surely. Moreover,
\[
\mathbb E L_p=2pq,\qquad
\operatorname{Var}(L_p)=pq(p-q)^2(p^2+q^2).
\]
Thus tie resolution induces a non-self-averaging asymptotic statistic at every nonfair bias, although the underlying source is ergodic; at the fair bias the limit is deterministic. In every case the FNN fraction remains strictly positive, even though every observed symbol is a genuine coordinate of an ergodic deterministic shift.

## Assumptions and scope
The state space is \(\{0,1\}^{\mathbb Z}\), with the left shift and the product Bernoulli measure. The observation is exactly zero or one; no additive noise or jitter is imposed. For each \(i=0,\dots,n-1\), the one-delay vector is \(Y_i=X_i\); the selected nearest neighbour \(Y_{j(i)}\) minimizes \(|Y_i-Y_j|\) among \(j\ne i\), with smallest index used to resolve distance ties. A point is false when
\[
\frac{|X_{i+1}-X_{j(i)+1}|}{|X_i-X_{j(i)}|}>R_{\mathrm{tol}}
\quad\text{or}\quad
\frac{|X_{i+1}-X_{j(i)+1}|}{R_A}>A_{\mathrm{tol}},
\]
where both thresholds are arbitrary fixed positive numbers, \(R_A\) is the empirical standard deviation as conventionally defined, \(a/0=+\infty\) for \(a>0\), and \(0/0=0\). The fraction is \(F_n=n^{-1}\sum_{i=0}^{n-1}\mathbf1_{\{i\text{ false}\}}\). The limiting result does not rely on a numerical tolerance or a finite computational cutoff. The biased law is for this explicit, reproducible tie rule, not for every possible tie rule.

## Proof
With probability one, both symbols recur infinitely. Let \(\tau_b=\min\{j\ge0:X_j=b\}\) and let \(A_b=X_{\tau_b+1}\), for \(b\in\{0,1\}\). Once the sample includes two copies of both symbols, every index whose symbol is \(b\), except the first occurrence \(i=\tau_b\), selects \(j(i)=\tau_b\). The exceptional two indices have aggregate weight at most \(2/n\). At all other indices the one-delay distance vanishes; the FNN test is therefore true exactly when \(X_{i+1}\ne A_b\), independently of the positive tolerances. By the strong law of large numbers applied to each ordered binary pair,
\[
F_n\longrightarrow L_p
=q\,[p\mathbf1_{\{A_0=0\}}+q\mathbf1_{\{A_0=1\}}]
+p\,[p\mathbf1_{\{A_1=0\}}+q\mathbf1_{\{A_1=1\}}]
\quad\text{almost surely}. \tag{1}
\]

The two anchor successors \(A_0,A_1\) are independent Bernoulli\((p)\). For completeness, partition according to the first two symbols. On \((X_0,X_1)=(0,0)\), \(A_0=0\) and the successor of the first later \(1\) is an independent Bernoulli\((p)\). On \((0,1)\), \(A_0=1\) and \(A_1=X_2\) is independent Bernoulli\((p)\). On \((1,0)\), \(A_1=0\) and \(A_0=X_2\); on \((1,1)\), \(A_1=1\) and the successor of the first later \(0\) is fresh Bernoulli\((p)\). The first-hit statements follow from independence of all coordinates after the stopping time at which the missing symbol first appears. Summing the four cases gives
\[
\Pr(A_0=a,A_1=b)=p^{a+b}q^{2-a-b}\quad(a,b\in\{0,1\}). \tag{2}
\]

Equation (1) becomes \(L_p=p+(q-p)(qA_0+pA_1)\). The four pairs \((A_0,A_1)=(0,0),(1,1),(0,1),(1,0)\) give respectively \(p,q,2pq,p^2+q^2\), with probabilities \(q^2,p^2,pq,pq\). Their values are pairwise distinct for \(0<p<1\) except at \(p=1/2\). Taking expectation and variance using independence in (2) yields the displayed formulas. In particular the variance is positive for every nonfair interior bias and zero at the fair bias. This completes the proof.

## Verification
The accompanying standalone Python program `CHECK.py` exactly enumerates the four two-symbol branches in rational arithmetic for 19 biases and checks the joint law, the mean and variance identities. It also runs three independent long symbolic sample trials, computing the FNN statistic with the stipulated tie rule and comparing with the anchor-based limit. These finite tests corroborate, but do not substitute for, the infinite ergodic proof.

## Relationship to prior work
Śpiewak (2026) proves asymptotic FNN bounds for smooth diffeomorphisms, generic smooth observables and prescribed embedding dimensions. The present statement concerns a locally constant quantized sensor on the two-sided Bernoulli shift and gives an exact *distribution* at a fixed delay length, so its assumptions and conclusion are distinct. Kennel and Buhl (2003) introduce a different statistic called *symbolic* FNN to optimize partitions through a two-sided symbolic embedding and distances back in the original phase space. That statistic does not imply the four-atom law for the ordinary scalar-delay FNN test under earliest-index ties. Earlier practical descriptions of FNN discuss finite sample and embedding issues, but the inspected statements do not supply this exact bias-dependent limiting distribution. No global priority claim is made beyond these comparisons.

## Limitations
The phenomenon depends on an exactly discrete observable and on the explicitly stated earliest-index tie convention; continuous observational noise, random tie resolution, or alternative nearest-neighbour rules may lead to different limits. The Bernoulli source is an exact model, not a claim about typical smooth sensors or manifold-valued observations. This work does not prove a universal statement for all symbolic processes or all embedding lengths. Historical formulations not indexed by the consulted searches remain a possible originality risk. Independent validation has not been performed.

## References
1. A. Śpiewak, *On the convergence of the False Nearest Neighbours algorithm*, arXiv:2611.18087v1 (first posted 2026-11-13), https://arxiv.org/abs/2611.18087.
2. M. B. Kennel and M. Buhl, *Estimating Good Discrete Partitions from Observed Data: Symbolic False Nearest Neighbors*, Physical Review Letters 91 (2003), 084102, DOI:10.1103/PhysRevLett.91.084102, https://escholarship.org/content/qt8f46r5p4/qt8f46r5p4.pdf.
3. T. Schreiber, *False nearest neighbors*, TISEAN documentation (1999), https://www.pks.mpg.de/tisean/Tisean_3.0.1/docs/chaospaper/node9.html.
