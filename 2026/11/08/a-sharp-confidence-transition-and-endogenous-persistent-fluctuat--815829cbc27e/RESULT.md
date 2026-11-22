# Exact endogenous freezing and biased stationary laws on binary neighborhood-confidence stars

## Finding

**Theorem (binary-star freezing boundary and induced stationary law).** Consider the pure neighborhood Deffuant–Weisbuch (NDW) rule on the fixed unweighted star \(K_{1,m}\), \(m\ge3\), with one uniformly independently selected edge per discrete step, symmetric pre-interaction opinions used in the two *separate directed* confidence tests, strict tolerance \(\varepsilon>0\), and compromise fraction \(0<\rho\le1/2\). Of the \(m\) leaves, exactly \(k\in\{1,\ldots,m-1\}\) start at opinion 1 and the remaining \(m-k\) at opinion 0; the hub starts at arbitrary \(z\in[0,1]\). Put \(p=k/m\) and \(q=1-\rho\).

The exact condition under which **every leaf is permanently unreceptive** is
\[
             0<\varepsilon\le \varepsilon_*(m,k):=\min\{p,1-p\}.
\]
More precisely, under this condition both directed leaf gates stay closed forever for every possible edge-selection history; for \(\varepsilon>\varepsilon_*\), at least one leaf changes opinion almost surely, so the fully frozen-leaf phase fails. The latter statement does **not** classify the eventual behavior above this boundary.

Within the frozen phase the hub has the exact i.i.d. recursion
\[
H_{t+1}=qH_t+\rho B_t,\qquad B_t\sim\operatorname{Bernoulli}(p),
\]
with independent inputs. Its law converges at \(W_1\)-rate at most \(q^t\) to the unique stationary law
\[
\mu_{\rho,p}=\mathcal L\Bigl(\rho\sum_{j=0}^\infty q^jB_j\Bigr),
\]
where the \(B_j\)'s are i.i.d. Bernoulli\((p)\). The moment identities are
\[
\mathbb E H_t=p+q^t(z-p),\qquad
\operatorname{Var}(H_t)=\frac{\rho p(1-p)}{2-\rho}(1-q^{2t}),
\]
\[
\mathbb E_{\mu}H=p,\qquad \operatorname{Var}_{\mu}H=\frac{\rho p(1-p)}{2-\rho}.
\]
For almost every edge sequence \(\liminf H_t=0\) and \(\limsup H_t=1\): stationary convergence in law does not imply a pathwise limit.

At exact half compromise \(\rho=1/2\), \(\mu_{1/2,p}\) has full topological support \([0,1]\). It is Lebesgue-uniform precisely when the leaf populations are balanced \((2k=m)\). If \(2k\ne m\), it is singular and has Hausdorff dimension
\[
\dim_{\rm H}(\mu_{1/2,p})=\frac{-p\log p-(1-p)\log(1-p)}{\log 2}<1.
\]
This is the classical biased binary Bernoulli-product dimension, here linked to the exact confidence-driven endogenous freezing criterion. The nonuniform leaf-balance law and its sharp freezing boundary are the subject of the result; previously published three-vertex path theorems and general stubborn-agent perpetuity theory are **not** claimed as new.

## Assumptions and scope

For adjacent vertices \(i,j\), the pure neighborhood directed distance is
\[
d_{\mathrm{NBC}}(i,j)=\left|x_i-\frac1{\deg(j)}\sum_{v\sim j}x_v\right|.
\]
Upon selecting \(\{i,j\}\), each endpoint with distance strictly below \(\varepsilon\) moves \(\rho\) toward the other's *old* opinion; unreceptive endpoints do not move. Exactly one uniformly selected edge acts per time step, with no rewiring and no direct-distance mixture (\(\sigma=0\)). No claim is made for mixed confidence, arbitrary initial leaf opinions, or the high-tolerance dynamics of stars with three or more leaves. The claim concerns all integer \(m\ge3\), all \(1\le k\le m-1\), all \(z\in[0,1]\), and the given real parameter ranges.

## Proof

**Exact directed confidence gate.** For any star state the hub's distance toward each selected leaf vanishes, since that leaf's only neighbor is the hub. If the leaves still have their initial binary values, their mean is \(p\). Each zero leaf's distance towards the hub is then \(p\), and each one leaf's distance is \(1-p\), independent of the hub state. Because the gate is *strict*, all leaf gates are closed exactly for \(\varepsilon\le\min(p,1-p)\). Induction proves permanent closure, while the hub always responds. Consequently an independent uniformly sampled edge exposes the hub to value 1 with probability \(k/m=p\) and to 0 otherwise.

Conversely suppose \(\varepsilon>\min(p,1-p)\). At least one of the two binary leaf populations is then receptive at time zero as long as the leaves stay binary. If the hub initially equals the opinion of that population, selecting a leaf of the **opposite** population first moves the hub strictly away, because \(0<\rho\). Selecting a receptive leaf afterward changes its opinion strictly. If the hub opinion initially differs from a receptive leaf's opinion, selecting that receptive leaf changes it immediately. Thus from every \(z\) a prescribed one- or two-edge word has positive probability of changing a leaf. In fact, the chance that no leaf ever moves is zero: as long as leaves have not moved, the two relevant gates remain constant; independent edge sampling visits both populations and a receptive leaf infinitely often, while the hub cannot remain forever equal to the receptive population's opinion. Hence permanent complete leaf freezing fails almost surely. This assertion is only about whether the leaves ever change; it does not assert eventual consensus for \(\varepsilon>\varepsilon_*\).

**Recursion and stationary statistics.** Under the frozen condition the hub recursion has \(q=1-\rho\) and independent Bernoulli inputs. Unrolling gives
\[
H_t=q^tz+\rho\sum_{j=0}^{t-1}q^{t-1-j}B_j.
\]
The finite input word is exchangeable under reversal, so its law is that of the first \(t\) terms of the absolutely convergent infinite series. Coupling a solution started from \(z\) and one started from the stationary initial law with the same future inputs gives \(|H_t-H'_t|\le q^t\), proving the \(W_1\) bound and uniqueness. Summing independent expectations and variances gives the formulas, using \(1-q=\rho\) and \(1-q^2=\rho(2-\rho)\).

For every fixed length \(M\), an iid Bernoulli word with \(0<p<1\) contains infinitely many disjoint all-zero and all-one runs of length \(M\) almost surely. Each all-zero run ends with \(H\le q^M\) and each all-one run with \(H\ge1-q^M\), since the hub always lies in \([0,1]\). Taking the countable intersection over \(M\) proves \(\liminf H_t=0\) and \(\limsup H_t=1\).

**Exact half-compromise law.** When \(\rho=1/2\), the stationary variable is \(\sum_{j\ge0}2^{-j-1}B_j\). Each binary cylinder of depth \(n\), with \(a\) ones and \(n-a\) zeros, has probability \(p^a(1-p)^{n-a}\). Because \(0<p<1\), all cylinders have positive mass and the support is all \([0,1]\). For \(p=1/2\), their probabilities are their Lebesgue lengths. For \(p\ne1/2\), the strong law gives typical digit frequency \(p\), whereas Lebesgue-typical sequences have frequency \(1/2\), proving singularity. The almost-sure local dyadic exponent is \(-[p\log p+(1-p)\log(1-p)]/\log2\). The standard Bernoulli-product cylinder covering and mass-distribution bounds give the asserted dimension (with dyadic expansion ambiguities confined to a null set). These coding facts are classical; the new model-specific step is their generation by an exact frozen-leaf threshold in stars beyond the three-vertex path.

## Independent reproducibility targets and limitations

For each \(m\) and \(k\), checking both actual directed distances before a chosen interaction validates the two gate values \(p\) and \(1-p\), not merely the scalar recursion. For example, \(m=3,k=1\) has sharp full-freezing tolerance \(1/3\); at \(\rho=1/2\) the resulting stationary law is fully supported but singular with dimension \(h(1/3)/\log2\). Exact arithmetic tests can confirm the gate and finite-time moments for finitely many \(m,k\) but do not establish the all-integer and almost-sure claims; those come from the proof above.

The earlier three-vertex NDW threshold and uniform limiting law were proved in the published 2026-10-25 result *A sharp three-agent confidence threshold between consensus and persistent opinion fluctuations*, with further mixed-neighborhood extension in the 2026-11-02 published result *Uniform stationary volatility in a three-vertex neighborhood-confidence path*. Their statements cover the \(m=2\) case, which is deliberately **excluded from this theorem**. Acemoglu, Como, Fagnani, and Ozdaglar (2010/2013), especially §2.1, prove the perpetuity and fluctuation mechanism for **exogenously stubborn** vertices; that theory describes the hub after the NDW confidence gate has closed, but does not derive the endogenous star gate. The stationary biased binary entropy/dimension law is also standard and is not asserted as a new theorem in probability. Literature coverage beyond the cited results is not guaranteed.

## References

1. S. Krishnagopal and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Neighborhood Effects*, arXiv:2402.05368v2, 2025, §III.1 Eq. (3). https://arxiv.org/html/2402.05368v2
2. *A sharp three-agent confidence threshold between consensus and persistent opinion fluctuations*, published 2026-10-25: https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-a-sharp-three-agent-confidence-threshold-between-consensus-and-p--28a3aef41d87/RESULT.md
3. *Uniform stationary volatility in a three-vertex neighborhood-confidence path*, published 2026-11-02: https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-uniform-stationary-volatility-in-a-three-vertex-neighborhood-con--37b276c8f32e/RESULT.md
4. D. Acemoglu, G. Como, F. Fagnani and A. Ozdaglar, *Opinion fluctuations and disagreement in social networks*, Mathematics of Operations Research 38 (2013), 1–27, §2.1. https://arxiv.org/abs/1009.2653
