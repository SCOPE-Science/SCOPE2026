# Maximum-entropy overlap-optimal spanning trees on wheels

## Finding

For every integer \(m\ge3\), let \(W_m=K_1\vee C_m\) be the wheel with one hub, \(m\) rim vertices, \(m\) spokes and \(m\) rim edges. Let \(\mathcal T_m\) denote its spanning trees and \(S(T)\) the number of spokes of \(T\). Define the positive-weight spanning-tree law
\[
\mu_w(T)=\frac{w^{S(T)}}{Z_m(w)},\qquad Z_m(w)=\sum_{T\in\mathcal T_m}w^{S(T)},\quad w>0.
\]

There is exactly one \(w_m>0\) for which each of the \(2m\) edges has inclusion probability \(1/2\). Consequently, for two independent identically distributed spanning trees drawn using \(\mu_{w_m}\),
\[
\mathbb E|T\cap T'|=\frac m2=\min_{\mu\in\mathcal P(\mathcal T_m)}\mathbb E_{\mu\otimes\mu}|T\cap T'|.
\]
Furthermore \(\mu_{w_m}\) is the **unique maximum-Shannon-entropy law** among *all* laws \(\mu\) attaining this minimum, not merely among weighted spanning-tree laws.

Specifically, \(w_m=(1-x_m)^2/x_m\), where \(x_m\) is the unique zero in the open interval \((0,1)\) of
\[
1-3x+3x^m-x^{m+1}=0.
\]
The endpoint \(x=1\) also satisfies the displayed polynomial but is not an admissible solution. The positive calibration parameters obey
\[
w_3=1,\quad 1<w_4<w_5<\cdots<\frac43,\quad
\lim_{m\to\infty}3^m\left(\frac43-w_m\right)=\frac{64}{9}.
\]

The ordinary uniform spanning-tree law \(\mu_1\) has excess expected pairwise overlap
\[
\mathbb E_{\mu_1\otimes\mu_1}|T\cap T'|-\frac m2
=2m\left[\frac{1}{\sqrt5}\frac{1+q^m}{1-q^m}-\frac12\right]^2,
\qquad q=\frac{3-\sqrt5}{2}.
\]
This is positive for \(m\ge4\), zero for \(m=3\), and equals
\[
\left(\frac9{10}-\frac2{\sqrt5}\right)m+O(mq^m)
\]
as \(m\to\infty\). The exact calibration and its exponential stabilization give a canonical practical correction to uniform sampling on an infinite, non-edge-transitive family.

## Assumptions and scope

Graphs are finite, simple and unweighted before the auxiliary sampling conductance \(w\) is introduced. A spanning tree of \(W_m\) has exactly \(m\) edges. Two trees in any overlap expectation are independent and identically distributed; the optimization is over **every** probability mass function on the finite set \(\mathcal T_m\), including laws with non-full support. Entropy uses natural logarithms and the convention \(0\log0=0\). All statements hold for every integer \(m\ge3\); the limiting statements concern \(m\to\infty\).

## Proof

**1. Spoke partition function.** The weighted matrix-tree theorem, deleting the hub's row and column, gives
\[
Z_m(w)=\det\bigl(wI+L(C_m)\bigr)
=\prod_{j=0}^{m-1}\left(w+2-2\cos\frac{2\pi j}{m}\right).
\]
Every tree has positive weight for \(w>0\). Rotational symmetry and logarithmic differentiation imply that each spoke is present with probability
\[
s_m(w)=\frac{w}{m}\frac{d}{dw}\log Z_m(w)
=\frac1m\sum_{j=0}^{m-1}
\frac{w}{w+2-2\cos(2\pi j/m)}.
\]
Each rim edge has the same inclusion probability, and a tree contains exactly \(m\) edges. Thus the common rim-edge inclusion probability is \(1-s_m(w)\).

**2. Exact scalar calibration.** For \(w>0\), let \(x\in(0,1)\) be determined by \(w=(1-x)^2/x\). The standard geometric Poisson-kernel identity, obtained by summing its absolutely convergent Fourier series, is
\[
\frac{1-x^2}{1-2x\cos\theta+x^2}
=1+2\sum_{k=1}^{\infty}x^k\cos(k\theta).
\]
Averaging over the \(m\)-th roots of unity kills every frequency not divisible by \(m\), so
\[
s_m(w)=\frac{1-x}{1+x}\frac{1+x^m}{1-x^m}.
\]
The equation \(s_m(w)=1/2\) is therefore equivalent, for \(x\in(0,1)\), to
\(1-3x+3x^m-x^{m+1}=0\). Directly from the spectral expression,
\[
\frac{d}{dw}s_m(w)=\frac1m\sum_{j=1}^{m-1}
\frac{2-2\cos(2\pi j/m)}{(w+2-2\cos(2\pi j/m))^2}>0.
\]
Moreover \(s_m(w)\to1/m\) as \(w\downarrow0\) and \(s_m(w)\to1\) as \(w\to\infty\). Since \(m\ge3\), there is one and only one \(w_m\) giving \(s_m(w_m)=1/2\). The correspondence between \(w>0\) and \(x\in(0,1)\) is bijective, proving the claimed uniqueness for \(x_m\).

**3. Optimality and unique maximum entropy.** For any probability law \(\mu\) on \(\mathcal T_m\), let \(p_e=\Pr_\mu(e\in T)\). Independence of the two samples yields
\[
\mathbb E_{\mu\otimes\mu}|T\cap T'|=\sum_{e\in E(W_m)}p_e^2.
\]
Since \(\sum_e p_e=m\), Cauchy--Schwarz on the \(2m\) edge marginals gives
\(\sum_e p_e^2\ge m/2\), with equality **if and only if** \(p_e=1/2\) for every edge. The constructed \(\mu_{w_m}\) attains equality.

For any other minimizing \(\mu\), its expected number of spokes is \(m/2\). Relative entropy with respect to the full-support law \(\mu_{w_m}\) gives
\[
D(\mu\Vert\mu_{w_m})
= -H(\mu)+\log Z_m(w_m)-\frac m2\log w_m
= H(\mu_{w_m})-H(\mu)\ge0.
\]
Equality in relative entropy holds exactly when \(\mu=\mu_{w_m}\), proving uniqueness of the maximum-entropy minimizer. Other minimizing laws need not be unique.

**4. Monotonicity and sharp exponential limit.** For any fixed \(w>0\), the expression
\(s_m(w)=\frac{1-x}{1+x}\frac{1+x^m}{1-x^m}\) decreases strictly with \(m\), since \(0<x<1\). Since \(s_m\) increases strictly in \(w\), the roots satisfy \(w_{m+1}>w_m\). For \(m=3\), the wheel is \(K_4\) and \(w_3=1\). Letting \(m\to\infty\) in the explicit scalar formula for fixed \(w\), we obtain \(\lim_m s_m(w)=(1-x)/(1+x)\), which equals \(1/2\) at \(x=1/3\), i.e. \(w=4/3\). Monotonicity and comparison at fixed \(w\) give \(w_m\uparrow4/3\); in particular \(w_m<4/3\).

Writing \(x_m=1/3+\delta_m\) in its polynomial equation yields the exact identity
\[
3\delta_m=(3-x_m)x_m^m.
\]
As \(x_m\) decreases to \(1/3\) and \(x_m\le x_3<1\), this identity first gives \(\delta_m=O(x_3^m)\); consequently \((3x_m)^m\to1\). Multiplying the identity by \(3^m\) now gives \(3^m\delta_m\to8/9\). Since \(w(x)=x+x^{-1}-2\) has derivative \(-8\) at \(x=1/3\), the mean-value theorem proves
\(3^m(4/3-w_m)\to64/9\).

**5. Uniform-law comparison.** Put \(q=(3-\sqrt5)/2\), the solution \(x\in(0,1)\) to \(w(x)=1\). Then the displayed Poisson-kernel formula gives the common spoke-edge probability for the uniform spanning tree:
\[
a_m=s_m(1)=\frac{1}{\sqrt5}\frac{1+q^m}{1-q^m}.
\]
The rim-edge probability is \(1-a_m\). Thus independent uniform trees have overlap \(m(a_m^2+(1-a_m)^2)=m/2+2m(a_m-1/2)^2\). Strict increase of \(w_m\), together with \(w_3=1\), gives \(a_m<1/2\) for all \(m\ge4\). Finally \(a_m=1/\sqrt5+O(q^m)\) yields the stated exact and asymptotic gaps.

## Verification

The included `verify.py` is a dependency-free independently formulated finite checker. It enumerates spanning trees by cycle detection, counts trees by spoke number, verifies their weighted generating polynomial against exact integer matrix-tree cofactors, checks individual edge marginals, and tests the scalar root and monotonicity numerically. Execute `python3 verify.py` from the package's top-level directory. The package replay produced `VERIFY_OK 1626 exact and numerical assertions`.

The enumerations cover \(3\le m\le8\), and the numerical parameter checks cover \(3\le m\le24\). They are **not** an exhaustive proof for all \(m\); the preceding algebraic and analytic argument proves the stated infinite family.

## Relationship to prior work

Albin, Clemens, Hoare, Poggi-Corradini, Sit and Tymochko (2018 preprint; 2021 journal) formulate minimum expected spanning-tree overlap, prove the marginal-squared objective and characterize homogeneous graphs. Those general statements are used rather than claimed here. The new assertion assessed here is the specific **full-support maximum-entropy minimizing law on every wheel**, its exact algebraic spoke weight, sharp exponential calibration constant, and exact excess of ordinary uniform sampling. The 2018 manuscript does not discuss wheels or entropy.

Klee and Stamps (2019) present weighted matrix-tree methods for other graph families, supplying the enumerative infrastructure but no wheel fairness optimizer. London and Pluhár (2023) address graph-network overlap benchmarks and examples; no wheel sampling law or sharp calibration parameter is given in the inspected article. Earlier wheel uniform-spanning-tree leaf correlations concern different observables and do not imply the calibrated overlap law.

## Limitations

This is an exact finite-graph probability-law result. The fair law need not be the **only** minimizing law; uniqueness is solely for entropy among minimizers. The theorem does not estimate the runtime of a sampler, cover non-wheel graphs, or provide a finite-sample statistical estimator of \(w_m\). The formula for the partition function itself is classical weighted matrix-tree theory. General exponential-family entropy principles are also standard; novelty is asserted only for the combined exact wheel-specific optimal law and sharp parameter asymptotics. Historical priority cannot be established solely from unsuccessful search, and independent auditing remains outstanding.

## References

1. N. Albin, J. Clemens, D. Hoare, P. Poggi-Corradini, B. Sit and S. Tymochko, *Fairest Edge Usage and Minimum Expected Overlap for Random Spanning Trees*, first public arXiv version 2018-05-25, arXiv:1805.10112; *Discrete Mathematics* **344** (2021), 112282. https://arxiv.org/abs/1805.10112
2. S. Klee and M. T. Stamps, *Linear Algebraic Techniques for Weighted Spanning Tree Enumeration*, first public arXiv version 2019-02-27, arXiv:1903.03575. https://arxiv.org/abs/1903.03575
3. A. London and A. Pluhár, *Intersection of random spanning trees in complex networks*, *Applied Network Science* **8** (2023), article 72, published 2023-10-13. https://doi.org/10.1007/s41109-023-00600-4
