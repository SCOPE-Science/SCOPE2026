# Strict seed-degree anticorrelation in uniformly grown random \(k\)-trees

## Finding

For the uniform \(k\)-clique attachment process of Gao, let \(k\ge 2\) be a fixed integer. Start with a labeled complete graph on \(k+1\) vertices, and at each step independently choose one of the currently present \(k\)-cliques uniformly, join a new vertex to its \(k\) vertices, and retain every old edge. For any two distinct original vertices \(u,v\), let \(D_u(m),D_v(m)\) be their degrees after \(m\) insertions. Then

\[
\operatorname{Cov}(D_u(m),D_v(m))<0\quad\text{for every }m\ge1,
\]

although a single insertion may simultaneously increase both degrees. The result includes explicit all-size covariance and variance formulas and a strictly negative limiting correlation. These conclusions concern original seed vertices, not arbitrary later vertices or a uniformly sampled tree from all labeled \(k\)-trees.

Set \(a=k-1\), \(b=k-2\), \(M_j=k+1+kj\), and

\[
P_s(m)=\prod_{j=0}^{m-1}\left(1+\frac{s}{M_j}\right),\qquad P_s(0)=1,\qquad c=\frac{a^2}{k}.
\]

Writing \(\mu_m=kP_a(m)\), the exact identities are

\[
\begin{aligned}
\mathbb E D_u(m)&=k+\frac{\mu_m-k}{a},\\
\operatorname{Cov}(D_u(m),D_v(m))
&=\frac{[k^2+c(k-1)]P_{2a}(m)-c(k-1)P_b(m)-k^2P_a(m)^2}{a^2},\\
\operatorname{Var}(D_u(m))
&=\frac{k(2k-1)P_{2a}(m)-akP_a(m)-k^2P_a(m)^2}{a^2}.
\end{aligned}
\]

In particular, the covariance after one insertion is exactly \(-1/(k+1)^2\). Put

\[
g_k=\Gamma(1+1/k),\quad h_k=\frac{\Gamma(1+1/k)}{\Gamma(3-1/k)},\quad
\begin{aligned}
C_k&=\frac{[k^2+(k-1)^3/k]h_k-k^2g_k^2}{(k-1)^2},\\
V_k&=\frac{k(2k-1)h_k-k^2g_k^2}{(k-1)^2}.
\end{aligned}
\]

For each fixed \(k\ge2\), \(C_k<0<V_k\), and

\[
\operatorname{Cov}(D_u(m),D_v(m))\sim C_km^{2(k-1)/k},\qquad
\operatorname{Var}(D_u(m))\sim V_km^{2(k-1)/k},\qquad
\operatorname{Corr}(D_u(m),D_v(m))\longrightarrow\frac{C_k}{V_k}<0.
\]

For the especially natural edge-attachment case \(k=2\), define

\[
q_m=\sqrt\pi\,\frac{\Gamma(m+2)}{\Gamma(m+3/2)}.
\]

Then the formulas simplify to

\[
\mathbb E D_u(m)=q_m,\quad
\operatorname{Cov}(D_u(m),D_v(m))=3m+4-q_m^2,\quad
\operatorname{Var}(D_u(m))=4m+6-q_m-q_m^2,
\]

and

\[
\operatorname{Corr}(D_u(m),D_v(m))\longrightarrow
\frac{3-\pi}{4-\pi}=-0.164948091581\ldots.
\]

## Assumptions and scope

The parameter \(k\) is fixed and at least two; the integer \(m\ge0\) counts insertions after the initial \((k+1)\)-clique. Each currently present \(k\)-clique is selected with exactly the same probability, and all old cliques remain eligible for reselection. The two degree variables refer to distinct vertices of the original clique. Their joint moments are taken over the full sequence of random clique selections. The displayed correlation statement is for \(m\to\infty\) with fixed \(k\). The graph construction is Gao's 2008 uniform clique-growth model, not an ordered increasing \(k\)-tree or a process that samples a \((k+1)\)-clique before selecting a face.

## Proof

**Clique counts.** At insertion time \(j\), precisely \(M_j=k+1+kj\) size-\(k\) cliques are present, because the initial \((k+1)\)-clique has \(k+1\) size-\(k\) faces, and each added vertex creates precisely \(k\) new faces. For a fixed seed vertex \(w\), let \(A_w(j)\) denote the number of those faces containing \(w\). Initially \(A_w(0)=k\). If the selected face contains \(w\), then the insertion creates exactly \(k-1=a\) new faces containing \(w\), and also raises its degree by one. Therefore

\[
A_w(j)=k+a(D_w(j)-k).
\]

For the two selected seed vertices \(u,v\), let \(B(j)\) count faces containing both. Initially \(B(0)=k-1\). When a selected face contains both, exactly \(k-2=b\) new faces contain both; otherwise there are no new jointly incident faces. Let \(I_w(j)\) indicate that the selected face at time \(j\) contains \(w\). Conditional on the current graph (denoted \(\mathcal F_j\)),

\[
\mathbb E[I_u(j)\mid\mathcal F_j]=\frac{A_u(j)}{M_j},\quad
\mathbb E[I_u(j)I_v(j)\mid\mathcal F_j]=\frac{B(j)}{M_j}.
\]

The exact updates are \(A_w(j+1)=A_w(j)+aI_w(j)\) and \(B(j+1)=B(j)+bI_u(j)I_v(j)\). Consequently

\[
\mathbb E A_w(j)=kP_a(j),\qquad
\mathbb E B(j)=(k-1)P_b(j).
\]

**Mixed and second moments.** Put \(H_j=\mathbb E[A_u(j)A_v(j)]\), and \(T_j=\mathbb E[A_u(j)^2]\). Multiplication of the exact updates and conditioning give the linear recurrences

\[
\begin{aligned}
H_{j+1}&=\left(1+\frac{2a}{M_j}\right)H_j+\frac{a^2}{M_j}(k-1)P_b(j),&H_0=k^2,\\
T_{j+1}&=\left(1+\frac{2a}{M_j}\right)T_j+\frac{a^2}{M_j}kP_a(j),&T_0=k^2.
\end{aligned}
\]

Since \(b-2a=-k\), direct substitution solves the first recurrence:

\[
H_j=[k^2+c(k-1)]P_{2a}(j)-c(k-1)P_b(j).
\]

Since \(a-2a=-a\), the second solution is

\[
T_j=k(2k-1)P_{2a}(j)-akP_a(j).
\]

Subtracting \((kP_a(j))^2\) and using the affine relationship between \(A_w\) and \(D_w\) proves all displayed finite formulas.

**Strict negativity, including after late insertions.** Write \(K_j=\operatorname{Cov}(A_u(j),A_v(j))\), \(\mu_j=kP_a(j)\), and \(\beta_j=(k-1)P_b(j)\). The recurrences imply

\[
K_{j+1}=\left(1+\frac{2a}{M_j}\right)K_j+
\frac{a^2}{M_j}\left(\beta_j-\frac{\mu_j^2}{M_j}\right),\qquad K_0=0.
\]

It suffices to show that \(\mu_j^2>M_j\beta_j\) for every \(j\ge0\). Define \(R_j=\mu_j^2/(M_j\beta_j)\). The initial ratio is \(R_0=k^2/[(k+1)(k-1)]>1\). Moreover,

\[
\frac{R_{j+1}}{R_j}=
\frac{(M_j+a)^2}{(M_j+k)(M_j+b)}
=1+\frac1{(M_j+k)(M_j+b)}>1,
\]

because \(a=k-1\), \(b=k-2\). Thus every forcing term is strictly negative. Iterating from \(K_0=0\) yields \(K_j<0\) for all \(j\ge1\), hence the seed-degree covariance is negative. For \(j=0\) the formula gives

\[
\operatorname{Cov}(D_u(1),D_v(1))=
\frac{k-1}{k+1}-\left(\frac{k}{k+1}\right)^2=-\frac1{(k+1)^2}.
\]

**Asymptotic coefficient and correlation.** The elementary gamma-product identity is

\[
P_s(m)=\frac{\Gamma(1+1/k)\,\Gamma(m+1+(1+s)/k)}
{\Gamma(1+(1+s)/k)\,\Gamma(m+1+1/k)}.
\]

For fixed \(s\), gamma-ratio asymptotics give

\[
P_s(m)\sim\frac{\Gamma(1+1/k)}{\Gamma(1+(1+s)/k)}m^{s/k}.
\]

The exact moment expressions therefore give the coefficients \(C_k,V_k\). To verify that the leading covariance coefficient is *strictly* negative (not merely nonpositive), divide the covariance recursion by \(P_{2a}(j+1)\) and sum. Each summand

\[
\frac{a^2}{M_jP_{2a}(j+1)}\left(\beta_j-\frac{\mu_j^2}{M_j}\right)
\]

is strictly negative, and its magnitude is \(O((j+1)^{-2})\) by the same gamma-product asymptotics. Hence the sum converges to a finite, strictly negative limit. Since \(P_{2a}(m)\) has a strictly positive leading factor, \(C_k<0\). The variance coefficient is positive as follows from the analogous exact variance recurrence: its divided-by-\(P_{2a}\) representation has strictly positive innovation terms (\(\mu_j[1-\mu_j/M_j]\)), starting from zero. Explicitly,

\[
\operatorname{Var}(A_u(j+1))=
\left(1+\frac{2a}{M_j}\right)\operatorname{Var}(A_u(j))+
\frac{a^2}{M_j}\mu_j\left(1-\frac{\mu_j}{M_j}\right),
\]

and \(0<\mu_j<M_j\); its normalized innovation series converges to a positive constant. This proves \(V_k>0\). The ratio of the two leading coefficients gives the limiting correlation.

For \(k=2\), \(P_2(m)=(2m+3)/3\), \(P_0(m)=1\), and \(2P_1(m)=\sqrt\pi\,\Gamma(m+2)/\Gamma(m+3/2)\). Substitution gives the exact special case and the limit by \(q_m^2\sim\pi m\).

**Conditional dependence is not uniformly negative.** The unconditional result is not a simple one-step negative-association argument. For \(k=2\), label the initial triangle \(u,v,w\). Select edge \(uw\), introducing \(x\); next select edge \(wx\), introducing \(y\). The resulting graph has seven eligible edges, three incident with \(u\), two incident with \(v\), and only the edge \(uv\) incident with both. The next insertion indicators obey

\[
\operatorname{Cov}(I_u,I_v\mid\mathcal F_2)=\frac17-\frac{3\cdot2}{7^2}=\frac1{49}>0.
\]

Hence global anticorrelation persists even though some histories have positive conditional co-attachment covariance.

## Verification

The standalone file `CHECK.py` reconstructs actual graph-growth histories by enumerating all eligible faces at each insertion, directly computes degrees and common-face counts, and compares exact rational moments with the formulas. Cases include \(k=2,3,4,5\), with up to four insertions, together with exact all-size-formula evaluations for \(2\le k\le15\) and \(1\le m\le79\), closed-form checks for the \(k=2\) case through \(m=199\), and a numerical large-size comparison to its limiting correlation. Running `python CHECK.py` prints `PASS: 2645 independent exact or numerical assertions`. Finite enumeration is not used as an infinite proof; the preceding recurrences and strict sign inequalities are the proof for all admissible parameters.

## Relationship to prior work

Yong Gao, *The Degree Distribution of Random k-Trees* (first public arXiv version 1 August 2008, arXiv:0808.0202), introduces the exact uniform face-sampling process and proves its power-law marginal degree distribution. The source's model definition and one-vertex face-count identity are used and credited. Its full accessible draft's main results, proof and conclusion concern the one-dimensional degree histogram, not the pairwise seed-degree covariance, its exact mixed moments, or its strictly negative limiting correlation. Darrasse, Hwang, Bodini and Soria, *The connectivity-profile of random increasing \(k\)-trees* (arXiv:0910.3639, first posted 19 October 2009), study the same uniform-face increasing construction and derive a one-root degree limit in Theorem 7 together with connectivity-profile asymptotics; they do not assert a pairwise seed-degree covariance or a joint limit for two seed degrees. Panholzer and Seitz, *Ordered increasing \(k\)-trees* (arXiv:1003.0320, first posted 1 March 2010), analyze a different weighted recursive construction; the selection rule is not interchangeable. Standard preferential attachment and random spanning-tree degree-correlation results likewise involve different sample spaces and do not entail the formulas here. A general multicolor-urn or clique-incidence result not identified in the examined record could potentially subsume the claim; the priority assessment is therefore best knowledge, not a guarantee of absolute novelty.

## Limitations

This theorem concerns **only pairs of original seed vertices** of Gao's uniform clique-selection model. It does not assert negative covariance for arbitrary two later-born vertices, all conditioning events, all dynamic graphs, or all notions of \(k\)-tree sampling. No central limit theorem or explicit distributional limit for the degrees is asserted. The exact formulas do not imply asymptotic independence: their correlation approaches a strictly negative constant. The asymptotic statements hold with \(k\) fixed. Priority searches cannot establish mathematical uniqueness; some broader abstract urn descriptions may already include the specialization.

## References

1. Yong Gao, *The Degree Distribution of Random k-Trees*, arXiv:0808.0202 (first posted 1 August 2008), https://arxiv.org/abs/0808.0202 ; accessible complete author draft https://cmps-people.ok.ubc.ca/yongg/research/papers/random-ktree-draft.pdf .
2. Alois Panholzer and Georg Seitz, *Ordered increasing \(k\)-trees: introduction and analysis of a preferential attachment network model*, arXiv:1003.0320v1 (1 March 2010), https://arxiv.org/abs/1003.0320 .
3. Alexis Darrasse, Hsien-Kuei Hwang, Olivier Bodini and Michèle Soria, *The connectivity-profile of random increasing \(k\)-trees*, arXiv:0910.3639 (19 October 2009), https://arxiv.org/abs/0910.3639 .
4. Erol A. Peköz, Adrian Röllin and Nathan Ross, *Degree asymptotics with rates for preferential attachment random graphs*, arXiv:1402.4686 (2014), https://arxiv.org/abs/1402.4686 . This is a related but distinct preferential-attachment mechanism.
