# A basal-singleton rare-event law for Kingman external length

## Finding

In the standard Kingman coalescent on \(n\ge3\) distinct sampled leaves, every unordered pair of current ancestral lineages merges at unit rate. Let \(L_n\) denote the sum of all **external** (pendant) edge lengths, and let \(R_n\) denote the event that at the last merger, one of the two ancestral lineages is still a singleton original leaf. Put \(H_n=\sum_{j=1}^n 1/j\).

For every integer \(n\ge3\), the following **single conditional rare-event theorem** holds:

\[
\Pr(R_n)=\frac{2}{n-1},\qquad
\mathbb E[L_n\mid R_n]=2\left(1-\frac1n\right)+\frac{2(n+1-2H_n)}{n-2}.
\]

Consequently, with \(\mathbf 1_{R_n}\) the event indicator,

\[
\operatorname{Cov}(\mathbf 1_{R_n},L_n)
=\frac{4(n^2+2-2nH_n)}{n(n-1)(n-2)},
\]

which is \(0\) for \(n=3\), strictly positive for every \(n\ge4\), and asymptotic to \(4/n\). Furthermore, conditional on \(R_n\),

\[
L_n\xrightarrow{d}2+\mathcal H,\qquad
\mathcal H=\sum_{k=2}^{\infty}\frac{2E_k}{k(k-1)},
\]

where the \(E_k\) are independent standard exponentials. In particular \(\mathbb E[L_n\mid R_n]\to4\), whereas unconditionally \(L_n\to2\) in probability. The limit \(2+\mathcal H\) is nondegenerate; its Laplace transform is \(e^{-2s}\prod_{k=2}^{\infty}(1+2s/[k(k-1)])^{-1}\) for \(s\ge0\).

## Assumptions and scope

The sample size \(n\) is a finite integer at least three. Time is in the usual Kingman units, with pairwise merger rate one, so the waiting time \(T_k\) while there are \(k\) lineages has exponential rate \(\binom{k}{2}\). The topology choices and waiting times are independent; every lineage pair is equally likely at each merger. The event \(R_n\) is a topological condition on the *final pair*, not the event that a selected external branch is unusually long. It is the unbalanced root-split event \((1,n-1)\). Since \(n\ge3\), at most one of the two final lineages is a singleton.

## Proof

**1. Rare basal singleton.** Fix an original leaf \(i\). While \(k\ge3\) ancestral lineages remain, the chance that the next merger avoids its singleton lineage is \((k-2)/k\). Multiplying from \(k=n\) down to \(3\) gives

\[
\Pr(\{i\}\text{ survives to the final pair})
=\prod_{k=3}^{n}\frac{k-2}{k}=\frac{2}{n(n-1)}.
\]

These \(n\) events are disjoint, proving \(\Pr(R_n)=2/(n-1)\). The chosen surviving leaf is uniform among the \(n\) labels.

**2. Conditional topology and stage counts.** Given that \(i\) survives to the last pair, all earlier mergers must occur among the other \(n-1\) lineages. Conditional on avoidance, each pair of these other lineages is still equally likely. Therefore their entire *discrete merger history* is exactly that of a standard \((n-1)\)-leaf Kingman topology; the waiting times of the original \(n\)-coalescent retain their usual independent exponential distributions.

For a standard \(N\)-leaf coalescent let \(U_m^{(N)}\) be the number of singleton original leaves at its stage with \(m\) lineages. For a fixed original leaf, the survival product down to \(m\) is \(m(m-1)/[N(N-1)]\), whence

\[
\mathbb E U_m^{(N)}=\frac{m(m-1)}{N-1},\qquad 2\le m\le N.
\]

Write \(W_k\) for the number of singleton original leaves in the original \(n\)-coalescent at the stage with \(k\) lineages. Given \(R_n\),

\[
W_2=1,\qquad W_k\stackrel d=1+U_{k-1}^{(n-1)}\quad(3\le k\le n).
\]

Since \(L_n=\sum_{k=2}^n W_kT_k\), and waiting times are independent of the histories, the conditional expectation equals

\[
\sum_{k=2}^{n}\frac{2}{k(k-1)}\left[1+\frac{(k-1)(k-2)}{n-2}\right]
=2\left(1-\frac1n\right)+\frac{2(n+1-2H_n)}{n-2}.
\]

The analogous unconditional identity \(\mathbb E W_k=k(k-1)/(n-1)\) gives \(\mathbb E L_n=2\). Multiplication by \(\Pr(R_n)\) and subtraction prove the covariance identity.

**3. Strict sign and asymptotics.** Define \(f_n=n-2H_n+2/n\). Directly, \(f_3=0\) and \(f_{n+1}-f_n=1-2/n>0\) for \(n\ge3\). The covariance is \(4f_n/[(n-1)(n-2)]\), giving strict positivity from \(n=4\) and \(n\operatorname{Cov}(\mathbf 1_{R_n},L_n)\to4\).

**4. Conditional distribution.** With independent standard exponentials \(E_k\), couple the waiting times as \(T_k=2E_k/[k(k-1)]\). Under \(R_n\) decompose

\[
L_n\stackrel d=\mathcal H_n+Q_n,\qquad
\mathcal H_n=\sum_{k=2}^{n}T_k,\qquad
Q_n=\sum_{m=2}^{n-1}U_m^{(n-1)}T_{m+1}.
\]

Here the same exponentials may be used to construct a standard \((n-1)\)-coalescent total external length

\[
F_{n-1}=\sum_{m=2}^{n-1}U_m^{(n-1)}S_m,\qquad
S_m=\frac{2E_{m+1}}{m(m-1)},
\]

so that \(T_{m+1}=\frac{m-1}{m+1}S_m\). Thus \(0\le Q_n\le F_{n-1}\) and

\[
\mathbb E(F_{n-1}-Q_n)=\frac{4}{n-2}\left(H_n-\frac32\right)\longrightarrow0.
\]

The established finite-sample Kingman external-length variance satisfies \(\operatorname{Var}(F_{n-1})=O(\log n/n)\), with \(\mathbb E F_{n-1}=2\) (Janson and Kersting, or Fu and Li). Therefore \(Q_n\to2\) in probability (indeed in \(L^1\)). Meanwhile \(\mathcal H_n\to\mathcal H\) in \(L^1\), because \(\sum_{k\ge2}\mathbb ET_k=2\). Slutsky's theorem yields the asserted conditional limit. The infinite exponential sum has the stated Laplace transform by independence, and is nondegenerate since it contains the independent nonconstant \(T_2\) term.

## Verification

The standalone file `check.py` independently enumerates every possible *ordered merger history* through \(n=7\) using exact rational arithmetic for stage-averaged external length. For each size it checks the root-singleton event probability, the unconditional mean, the root-singleton conditional mean, and the covariance against the displayed formulas. It also checks the stage-sum identity for sizes through 500, positivity from size four, and the asymptotic trend at several sizes. Run with `python check.py` using a standard Python 3 interpreter. Enumeration is a finite consistency check only; the proof above establishes the infinite-size assertions.

## Relationship to prior work

Kingman's classic coalescent supplies the merger model. Janson and Kersting (first preprint 2010) give the unconditioned mean, variance, normal fluctuation theorem, and exceptional long-branch discussion. The present statement is about conditioning the **entire external-length sum** on the precise **basal singleton topology**, yielding a non-Gaussian unscaled conditional limit and a positive exact event–length covariance. The unconditioned central limit or long-edge point-process limit does not itself furnish this conditional theorem, since \(\Pr(R_n)\to0\).

Reppell and Zöllner (2017) derive branch-specific conditional start/end distributions and simulation methods, rather than this event-conditioned total-length law. Caliebe et al. (2007) treat one randomly chosen external branch. Disanto and Wiehe (2019 preprint / 2020 journal) study the two longest *ranked* external branches and dependence of the longest branch on root balance, making it a particularly close comparison: their abstract was read, but complete text was inaccessible, so its potential coverage of the aggregate conditional statistic cannot be fully ruled out. This is a historical-priority limitation, not a premise needed by the proof.

## Limitations

This result concerns the standard constant-size, binary Kingman coalescent with pairwise merger rate one and \(n\ge3\). It does not give a conditional central limit theorem at a smaller fluctuation scale, extend to multiple-merger coalescents, or characterize every rare root imbalance. The finite enumeration is not proof for arbitrary \(n\). No independent mathematical validation or exhaustive historical-priority certification is claimed. An especially relevant 2020 root-balance paper could not be inspected beyond its abstract.

## References

- S. Janson and G. Kersting, *The external lengths in Kingman's coalescent*, initial arXiv version 2010-04-28, https://arxiv.org/abs/1004.5011 ; journal version *On the total external length of the Kingman coalescent*, Electronic Journal of Probability 16 (2011), 2203–2218.
- A. Caliebe, R. Neininger, M. Krawczak, U. Rösler, *On the length distribution of external branches in coalescence trees*, Theoretical Population Biology 72 (2007), 245–252, https://doi.org/10.1016/j.tpb.2007.05.003.
- M. Reppell and S. Zöllner, *An efficient algorithm for generating the internal branches of a Kingman coalescent*, Theoretical Population Biology 122 (2018), 57–66; online 2017-07-11, https://pmc.ncbi.nlm.nih.gov/articles/PMC5764821/.
- F. Disanto and T. Wiehe, *Measuring the external branches of a Kingman tree: A discrete approach*, Theoretical Population Biology 134 (2020), 92–105, https://doi.org/10.1016/j.tpb.2020.05.002; relevant root-balance comparison based only on accessible abstract.
