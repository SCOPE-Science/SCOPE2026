# A sharp mixing-index phase diagram for persistence-conditioned uniform moving averages

## Finding
Consider the stationary limiting persistence-conditioned chain of Aurzada and Worf for uniform innovations on \([-a,1]\) and expanding coupling \(|\theta|>1\). Let \(Q\) denote its reduced one-coordinate Markov transition kernel, and let
\[
\delta(K)=\sup_{x,x'}\|K(x,\cdot)-K(x',\cdot)\|_{\mathrm{TV}}
\]
be the Dobrushin coefficient of a Markov kernel \(K\), where total variation is \(\sup_A|\mu(A)-\nu(A)|\). Define the strict-contraction index \(d=\inf\{k\ge1:\delta(Q^k)<1\}\), with \(d=\infty\) if no such integer exists.

The following classification holds in *every nontrivial expanding regime in which the conditioned chain is defined*:

1. If \(\theta>1\), \(a>0\), then \(d=\infty\). In fact, \(\delta(Q^k)=1\) for every finite \(k\ge1\) and, for the stationary law \(\pi\),
   \[\sup_x\|Q^k(x,\cdot)-\pi\|_{\mathrm{TV}}=1.\]
2. If \(\theta=-c<-1\) and \(0<a<1/c\), then \(d=1\). With \(h\) the explicitly normalized right eigenfunction in the motivating work and \(H=\int_{-a}^1h(u)\,du\),
   \[\delta(Q)=1-\frac{1-ca}{H}\le\frac{a(c+1)}{1+a}<1.\]
   The first equality is exact, not merely a bound.
3. If \(\theta=-c<-1\) and \(a\ge1/c\), then \(d=2\). More precisely, \(\delta(Q)=1\), while
   \[Q^2(x,A)\ge q_2\,\mu(A),\qquad q_2=\frac{1-c^{-2}}{H}\ge1-c^{-1},\]
   for every admissible \(x\) and Borel \(A\), where \(H=\int_{-1/c}^1h(u)\,du\) and \(\mu(du)=h(u)\,du/H\). Consequently, \(\delta(Q^2)\le1-q_2\le c^{-1}<1\).
4. If \(\theta<-1\) and \(-1<a\le0\), conditioning is vacuous, \(Q\) is the uniform refresh kernel, and \(d=1\), with \(\delta(Q)=0\).

In cases 2 and 3 the explicitly described stationary law \(\pi\) is unique, and
\[
\sup_x\|Q^t(x,\cdot)-\pi\|_{\mathrm{TV}}
\le\begin{cases}
[\delta(Q)]^t,&0<a<1/c,\\
[1-q_2]^{\lfloor t/2\rfloor},&a\ge1/c.
\end{cases}
\]
The sharp change at \(a=1/c\) is a change in the *minimum contracting sampling lag*, rather than simply a change in an unspecified mixing constant.

## Assumptions and scope
For \(\theta>1\), only \(a>0\) and effective state space \(\Omega=[-a,0)\) are included. For \(\theta=-c<-1\) with \(a>0\), put \(m=\min(a,c^{-1})\). The effective state space is \(\Omega=[-a,1]\) when \(a<c^{-1}\), and \(\Omega=(-c^{-1},1]\) when \(a\ge c^{-1}\). The endpoints carry no mass under the transition densities; the difference in endpoint inclusion matters only for whether a supremum is attained or approached. The eigenfunction \(h\) is continuous, positive on the effective state space, and bounded as proved in the cited source; for \(\theta<-1\) it is normalized to \(h=1\) on \([m/c,1]\), and rises monotonically from its left endpoint to that plateau. The stationary density is proportional to \(h(u)g(u)\), with \(g>0\) on \(\Omega\). The result does not claim rates for \(|\theta|\le1\) or for positive expanding couplings with no nontrivial limiting conditioned chain.

## Proof
**1. A conditional upper-tail identity.** The exact Doob kernel given by the source is
\[
Q(x,dy)=\frac{h(y)\mathbf1_{\{y>\theta x\}}}{\lambda(1+a)h(x)}\,dy.
\]
Using its defining eigenfunction relation, for \(\theta=-c<-1\), \(a>0\), and \(\Omega=(-m,1]\), this is equivalently
\[
Q(x,dy)=\mu(dy\mid Y>-cx),\qquad
\mu(dy)=\frac{h(y)}H\,dy,\quad H=\int_{-m}^1h(u)\,du,
\]
where \(Y\sim\mu\). Thus each transition is a truncation of one common positive probability law to an upper tail.

**2. Exact one-step coefficient.** If \(\mu_t\) denotes the law of \(Y\sim\mu\) conditioned on \(Y>t\), two nested upper-tail laws satisfy, whenever \(t\le s\),
\[
\|\mu_t-\mu_s\|_{\mathrm{TV}}
=1-\frac{\mu(Y>s)}{\mu(Y>t)}.
\]
This follows by splitting the smaller tail from the discarded interval and comparing their densities. In the negative-coupling family, \(-cx\) is largest when \(x\downarrow-m\), and some \(x\) sufficiently large has \(-cx\le-m\), giving the untruncated law \(\mu\). Therefore
\[
\delta(Q)=1-\mu(Y>cm).
\]
If \(m=a<1/c\), the threshold \(ca<1\); since \(h=1\) on \([a/c,1]\), it is also one on \([ca,1]\), yielding \(\mu(Y>ca)=(1-ca)/H>0\) and the exact formula in case 2. The derivative relation for \(h\) in the cited source has positive derivative below its plateau; hence \(0<h\le1\), so \(H\le1+a\), providing the displayed parameter-only upper bound on \(\delta(Q)\). If \(m=1/c\), the maximal threshold equals one in the endpoint limit; thus \(\mu(Y>cm)=0\) and \(\delta(Q)=1\).

**3. Two-step minorization.** Put \(b=m/c\) and \(B=[b,1]\). If \(y\in B\), then \(-cy\le-m\), so \(Q(y,\cdot)=\mu\). For arbitrary \(x\), conditioning a probability on an upper tail cannot lower the probability of the upper interval \(B\); therefore
\[
Q(x,B)\ge\mu(B)=\frac{1-b}{H}=:q_2.
\]
The Markov property gives \(Q^2(x,A)\ge Q(x,B)\mu(A)\ge q_2\mu(A)\). Since \(h\le1\), \(H\le1+m\), and in the green case \(m=c^{-1}\),
\[
q_2\ge\frac{1-c^{-2}}{1+c^{-1}}=1-c^{-1}.
\]
The standard total-variation coupling/contraction argument for a common minorizing component gives \(\delta(Q^2)\le1-q_2\), proves uniqueness of the stationary probability, and gives the geometric bounds. In the yellow case the one-step exact coefficient already gives its stronger bound.

**4. Positive expanding coupling cannot mix uniformly.** If \(\theta>1\), every legal path \(x=X_0,X_1,\ldots,X_k\) satisfies \(X_i>\theta X_{i-1}\), hence \(X_k>\theta^k x\). For a fixed positive integer \(k\), sending \(x\uparrow0\) through \([-a,0)\) confines \(Q^k(x,\cdot)\) to intervals \((\theta^k x,0)\) shrinking to the missing endpoint zero. The stationary law from the source has a Lebesgue density on \([-a,0)\) and thus no atom at zero. Therefore \(\sup_x\|Q^k(x,\cdot)-\pi\|_{\mathrm{TV}}=1\). Stationarity and convexity give \(\sup_x\|Q^k(x,\cdot)-\pi\|_{\mathrm{TV}}\le\delta(Q^k)\le1\), so \(\delta(Q^k)=1\).

**5. The vacuous regime.** If \(\theta<-1\) and \(-1<a\le0\), every innovation is nonnegative and every positivity constraint is automatic. The conditional process is independent uniform sampling; hence \(\delta(Q)=0\).

## Verification
The proof uses the sourced exact transition kernel and normalization properties, not a simulation or finite enumeration. The accompanying standalone `checker.py` tests exact rational upper-tail identities, the Dobrushin coefficient, the two-step common-component minorization, and finite-step positive-coupling support inclusions on representative discrete grids with positive weights. Such checks test the algebraic mechanism only; they cannot prove the continuous-state theorem or the claim of mathematical novelty. Run with `python3 checker.py` using the Python standard library.

## Relationship to prior work
Aurzada and Worf's 2026 expanding-regime paper derives the Doob transition kernel and explicit stationary density, as well as persistence asymptotics, across the relevant parameter regimes; those are premises here, not new claims. Their non-expanding-regime companion treats \(-1\le\theta<1\) and does not supply this expanding-regime strict-contraction classification. The Doeblin minorization principle, the Dobrushin coefficient and its total-variation contraction consequence are classical; the contribution claimed here is the exact *model-specific phase boundary and minimum contracting lag*, together with a parameter-only two-step rate in the regime where every one-step coefficient is one. A search of the inspected sources did not reveal this classification, but older unindexed consequences of the explicit kernel remain a genuine originality risk.

## Limitations
The numerical contraction bounds need not be sharp rates of convergence; the exact one-step Dobrushin coefficient in the yellow regime and the minimal contracting sampling lag are sharp. The theorem is about the *limiting conditioned chain*, not finite-horizon processes conditioned on survival up to a finite time. The absence of uniform total-variation mixing for positive expanding coupling does not exclude convergence from each fixed initial state. No external independent validation has been performed.

## References
1. F. Aurzada and V. Worf, *MA(1) processes with uniform innovations conditioned to stay positive in the expanding regime*, arXiv:2611.16041v1, first public version 2026-11-11, Theorems 1.1–1.2 and their proofs. https://arxiv.org/abs/2611.16041
2. F. Aurzada and V. Worf, *MA(1) processes with uniform innovations conditioned to stay positive in the non-expanding regime*, arXiv:2606.01832v1, 2026-06-01. https://arxiv.org/abs/2606.01832
3. Classical Dobrushin total-variation contraction and Doeblin minorization principles. Used here only for the final mixing implication; the model-specific minorization is proved above.
