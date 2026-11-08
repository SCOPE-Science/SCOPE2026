# Exact Poisson-tilted leaf imbalance in a random tree with root doublings

## Finding

Consider the continuous-time root-doubling random recursive tree described below, initialized at the three-vertex tree with two root children. Let \(N_t\) be the vertex count, \(L_t\) the count of childless vertices, \(D_t\) the number of root-doubling events during \([0,t]\), and \(I_t=2L_t-N_t\). For every \(t\geq0\) and \(z\in[0,1)\),

\[
\mathbb E[I_t z^{D_t}]
=\frac{(1+z)e^{(z-1)t}-2e^{2(z-1)t}}{z-1}.
\]

At \(z=1\), the continuous extension equals \(1-2t\). The following finite-time identities hold:

\[
\mathbb E[I_t]=1-2t,\qquad
\operatorname{Cov}(I_t,D_t)=-t^2,
\]
\[
\mathbb E[I_t^2]=3e^{2t}+4e^t-12t-6,
\qquad
\operatorname{Var}(I_t)=3e^{2t}+4e^t-7-8t-4t^2.
\]

In particular the imbalance variance is asymptotic to \(3e^{2t}\) as \(t\to\infty\). The generating identity determines every finite-time conditional mean \(\mathbb E[I_t\mid D_t=k]\), by coefficient extraction, because \(D_t\) has the Poisson distribution with parameter \(t\).

## Assumptions and scope

Start at time zero with a rooted tree having one root and exactly two leaf children. Every vertex has a rate-one exponential clock; independently of all past clock firings, after ringing the clock resets. A non-root ring appends a new leaf to that vertex. A root ring replaces the present tree by a new root with two child subtrees, each an exact copy of the entire pre-ring tree. The new root is never a leaf. All rates are in the continuous-time clock of this construction, not in discrete attachment-step time. This starting tree equals the deterministic state immediately after the first root ring in the singleton-start model of Björnberg and Mailler (arXiv:2501.18466).

The process is nonexplosive on bounded intervals: the root rings finitely often (a rate-one Poisson process), and between its rings the other vertices undergo ordinary nonexplosive pure-birth (Yule) growth. Each finite-time polynomial moment used below exists; this also follows by applying the generator to a power of the size and then a stopped Gronwall argument.

## Proof

Write \(s=N_t\), \(i=I_t\), \(d=D_t\), and \(\ell=(s+i)/2=L_t\). There are exactly \(\ell\) non-root leaves and \(s-1-\ell\) other non-root vertices. Hence the three transitions and their rates are

\[
(s,i,d)\longmapsto
\begin{cases}
(2s+1,2i-1,d+1)&\text{at rate }1,\\
(s+1,i-1,d)&\text{at rate }\ell,\\
(s+1,i+1,d)&\text{at rate }s-1-\ell.
\end{cases}
\]

The first is the root doubling. Note especially its size shift of \(+1\) and imbalance shift of \(-1\). This boundary factor is essential. Let \(\mathcal G\) denote the generator. Direct substitution gives

\[
\mathcal Gs=2s,\quad \mathcal Gi=-2,\quad
\mathcal G(i^2)=i^2-6i+s,\quad
\mathcal Gd=1,\quad
\mathcal G(id)=2i-2d-1.
\]

For a fixed \(z\in[0,1]\), it also gives

\[
\mathcal G(z^d)=(z-1)z^d,
\qquad
\mathcal G(iz^d)=\bigl(2(z-1)i-(1+z)\bigr)z^d.
\]

The usual convention \(0^0=1\) is used. Since the initial state is \((s,i,d)=(3,1,0)\), \(F(t,z)=\mathbb E[z^{D_t}]=e^{(z-1)t}\). For \(H(t,z)=\mathbb E[I_tz^{D_t}]\), Dynkin's identity and the last generator equation yield

\[
\frac{\partial H}{\partial t}=2(z-1)H-(1+z)e^{(z-1)t},\qquad H(0,z)=1.
\]

Solving this scalar linear differential equation gives the displayed generating formula; its limit at \(z=1\) is \(1-2t\). Differentiating at \(z=1\) is justified by finite mixed moments and yields \(\mathbb E[I_tD_t]=t-3t^2\). As \(\mathbb E[D_t]=t\), the covariance is \(-t^2\).

Finally, the generator equations give \(\mathbb E[N_t]=3e^{2t}\), \(\mathbb E[I_t]=1-2t\), and

\[
\frac{d}{dt}\mathbb E[I_t^2]
=\mathbb E[I_t^2]-6(1-2t)+3e^{2t},\qquad
\mathbb E[I_0^2]=1.
\]

Its unique solution is \(3e^{2t}+4e^t-12t-6\). Subtracting \((1-2t)^2\) gives the variance. Localization of the generator identities and passage to the limit is justified by the finite second moments of the size process, whose generator is \(\mathcal G(s^2)=5s^2+3s\). This completes the proof.

## Verification

Run `python verify.py` in the same directory. The checker uses only Python's standard library and verifies 10,263 exact integer/rational identities, including generator actions across finite admissible states and independent generator-iteration Taylor coefficients through order eight for five values of the generating parameter. A separate seeded Gillespie simulation at three positive times was used as a sanity check, but is not needed for the mathematical proof. The infinite-time variance asymptotic is a direct consequence of the exact variance identity, not an extrapolation from experiments.

## Relationship to prior work

Björnberg and Mailler introduce the root-doubling growth model, establish size moments, limiting degree proportions and height properties, and use the continuous-time embedding with rate-one root-doubling times. The new result analyzes a different observable: the exact joint finite-time transform of leaf imbalance and the number of root doublings, with its covariance and variance consequences. The known size moment results and degree-proportion limit do not directly provide this mixed finite-time identity. Classical random recursive-tree degree fluctuation theorems (Mahmoud and Smythe, 1992) do not include the global root-doubling shocks. This is a statement of the inspected coverage, not proof that no historically equivalent identity exists elsewhere.

## Limitations

The theorem is for the continuous-time model, starting immediately after the first root doubling, and does not claim a discrete-event-time central limit theorem. It provides finite-time moments and conditional means, not the full law of the imbalance given a doubling count. The variance refers to the unnormalized imbalance, not to the random leaf proportion. No independent external mathematical audit has been performed; historical priority may require further expert assessment.

## References

1. J. E. Björnberg and C. Mailler, *A random recursive tree model with doubling events*, arXiv:2501.18466, initially submitted 2025-01-30, https://arxiv.org/html/2501.18466 ; journal DOI: https://doi.org/10.1016/j.spa.2025.104790.
2. H. M. Mahmoud and R. T. Smythe, *Asymptotic joint normality of outdegrees of nodes in random recursive trees*, Random Structures & Algorithms 3 (1992), 255–266, https://doi.org/10.1002/rsa.3240030305.
