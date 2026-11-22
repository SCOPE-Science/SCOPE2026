# Parity recovery and clique-core invariance for connected-set Walsh convolution on complete split graphs

## Finding
Let \(s\ge1\) and \(m\ge2\) be integers. On the complete split graph \(H_{s,m}=K_s\vee\overline{K_m}\), encode every nonempty vertex subset inducing a connected subgraph by its binary incidence vector. Let \(T_{s,m}\) be counting convolution by these incidence vectors on \(\mathbb F_2^{s+m}\), with no normalization. Its Walsh spectrum is explicitly determined below. In particular, \(T_{s,m}\) is invertible exactly when \(m\) is odd. For even \(m=2r\), precisely \(2^s\binom{2r}{r}\) Walsh characters vanish, namely those with exactly \(r\) marked independent-side vertices, with arbitrary clique-side frequency. Every remaining multiplier has absolute value at least \(2\), and the bound is sharp. For odd \(m\), every multiplier is nonzero and the sharp least magnitude is \(1\).

For \(m=2r\), the convolution range \(W_{s,2r}\) has a globally sharp endpoint projection constant, simultaneously for real and complex operators:
\[
\inf_{Q^2=Q,\ \operatorname{ran}Q=W_{s,2r}}\|Q\|_{\ell^1\to\ell^1}
=\inf_{Q^2=Q,\ \operatorname{ran}Q=W_{s,2r}}\|Q\|_{\ell^\infty\to\ell^\infty}
=1+\binom{2r}{r}\bigl(2^{-r}-2^{1-2r}\bigr).
\]
There is no translation-invariance restriction on the competing projections. The sharp value is independent of the clique size \(s\), and as \(r\to\infty\) it is asymptotic to \(2^r/\sqrt{\pi r}\). Meanwhile the proportion of lost Walsh modes is \(2^{-2r}\binom{2r}{r}\sim1/\sqrt{\pi r}\). Thus the relative nullity tends to zero while the best possible endpoint projection norm grows exponentially. At odd \(m\) the range is the whole space and the projection constant equals \(1\).

## Assumptions and scope
Here \(K_s\) denotes the clique on \(s\) vertices, \(\overline{K_m}\) the edgeless graph on \(m\) labelled vertices, and the join adds all edges from the clique to the independent class. The ambient group is \(G=\mathbb F_2^s\times\mathbb F_2^m\) with counting measure and XOR operation. Define \(f(z)=1\) when the vertex set encoded by \(z\in G\) is nonempty and connected in the induced graph, and \(f(z)=0\) otherwise. Convolution is \((Tg)(x)=\sum_{z\in G}f(z)g(x+z)\). Each connected vertex subset is counted once; the empty subset is excluded. The Walsh characters are \(\chi_{u,v}(x,y)=(-1)^{u\cdot x+v\cdot y}\). The projection norms use the ordinary counting-measure \(\ell^1\) and supremum \(\ell^\infty\) norms on the full finite group. The assertion is exact for all integers \(s\ge1\), \(m\ge2\); no assertion about other split graphs is made.

## Proof
**Character calculation.** A nonempty induced vertex set is connected if and only if it contains at least one clique vertex, or it consists of a single independent vertex. Indeed, each clique vertex is adjacent to every other vertex, while a subset containing only independent vertices has no edges. Consequently
\[
f(x,y)={\bf1}_{x\ne0}+{\bf1}_{x=0}{\bf1}_{|y|=1}.
\]
The unnormalized Walsh transform, with \(t=|u|\) and \(k=|v|\), is
\[
\Lambda_{s,m}(u,v)=m-2k+2^m\mathbf1_{k=0}\bigl(2^s\mathbf1_{t=0}-1\bigr).
\]
Here the singleton contribution is \(\sum_{j=1}^m(-1)^{v_j}=m-2k\). The clique-nonempty contribution is \((2^s\mathbf1_{t=0}-1)2^m\mathbf1_{k=0}\). When \(k>0\), a zero occurs exactly at \(m=2k\), which is possible precisely when \(m\) is even and \(k=m/2\). When \(k=0\), the multiplier is either \(m+(2^s-1)2^m\) or \(m-2^m\), both nonzero for \(m\ge2\). This proves the zero locus, multiplicity and rank \(2^{s+m}-2^s\binom{m}{m/2}\) at even \(m\). For odd \(m\), the coefficients \(m-2k\) at \(k>0\) attain magnitude one. For even \(m\), \(k=m/2\pm1\) attains magnitude two (including \(m=2\), using \(k=2\)); all other nonzero values are even and have magnitude at least two.

**Projection and minimization.** For \(m=2r\), the Fourier zero set consists of all pairs \((u,v)\) with \(|v|=r\); the core frequency is unrestricted. Hence the Fourier range projection is the identity on the core factor tensored with \(I-P_r\) on the independent-side cube, where \(P_r\) projects to the homogeneous degree-\(r\) Walsh layer. Every projection \(Q\) onto the same range can be averaged over all translations of \(G\): \(\overline Q=|G|^{-1}\sum_{a\in G}\tau_aQ\tau_a^{-1}\). The average is a projection onto the range because it fixes that space pointwise and maps into it, and has norm no greater than \(\|Q\|\) in either endpoint norm. A translation-invariant projection onto this range is necessarily the spectral projection \(I\otimes(I-P_r)\), since a translation-invariant operator is diagonal on Walsh characters and idempotence forces each diagonal entry to be zero or one. Thus this spectral projector is optimal over all projections.

**Exact norm.** Define the binary Krawtchouk values
\[
K_r(j)=\sum_{a=0}^r(-1)^a\binom ja\binom{2r-j}{r-a}.
\]
The convolution kernel of \(P_r\) on the \(2r\)-cube at a vector of weight \(j\) is \(2^{-2r}K_r(j)\). The combinatorial duality
\[
\binom{2r}{j}K_r(j)=\binom{2r}{r}K_j(r)
\]
and generating function \(\sum_j K_j(r)z^j=(1-z^2)^r\) give \(K_r(2a+1)=0\) and
\[
K_r(2a)=(-1)^a\binom{2r}{r}\binom ra/\binom{2r}{2a}.
\]
Therefore
\[
\sum_{x\in\mathbb F_2^{2r}}|K_r(|x|)|
=\binom{2r}{r}\sum_{a=0}^r\binom ra
=2^r\binom{2r}{r}.
\]
The kernel of \(I-P_r\) equals \(1-2^{-2r}\binom{2r}{r}\) at zero and \(-2^{-2r}K_r(|x|)\) elsewhere. Because \(\binom{2r}{r}<2^{2r}\), its absolute sum is
\[
1-2^{-2r}\binom{2r}{r}+2^{-2r}\bigl(2^r\binom{2r}{r}-\binom{2r}{r}\bigr)
=1+\binom{2r}{r}(2^{-r}-2^{1-2r}).
\]
The norm of a finite group convolution in \(\ell^1\) and in \(\ell^\infty\) equals the absolute sum of its kernel. Tensoring with identity on the clique coordinates does not change this norm. Finally, Stirling's formula gives \(\binom{2r}{r}\sim4^r/\sqrt{\pi r}\), establishing both asymptotic statements.

## Verification
The standalone file `verify_split_connected.py` reconstructs every nonempty connected induced subset directly from the graph partition, independently evaluates its full exact integer Walsh transform, and compares each frequency with the formula. For clique sizes from one through four and leaf sizes two through ten within total dimension thirteen, it checks 44,936 characters, all zero counts and smallest gaps. For every tested even size, it computes the full inverse Walsh transform of the range indicator and compares its absolute kernel sum to the closed norm. It also checks all central Krawtchouk identities through size thirty-two. All checks passed with ordinary Python 3 and exact integer/rational arithmetic. The infinite-family conclusions follow from the proof, not from the finite checks.

## Relationship to prior work
Counting connected induced vertex subsets is part of the graph-substructure program studied by Jerrum–Meeks (2013); Liao–Hou (2013) analyzes the subgraph component polynomial and specifically recalls earlier star-graph results. These works explain the combinatorial object but neither supplies its signed Fourier operator nor the range norm above. Polyanskiy (2013) studies Fourier projections onto Hamming layers; Defant–Galicer–Mansilla–Mastyło–Muro (2023, revised 2024) gives a general minimum-projection Fourier-kernel formula and is credited for that general principle. The contribution here is the exact connected-set spectral zero set for this two-parameter graph family and the evaluated central-layer complement norm, including its clique-core invariance and instability-vs-nullity asymptotics. No novelty is asserted for the universal translation-averaging principle, the elementary Krawtchouk duality, or the raw count of connected subsets.

## Limitations
The formula applies only to the complete split graphs described above, not to arbitrary split graphs, threshold graphs, or graph-specific edge-subset convolution. The projection norm is an endpoint operator norm, not a bound on inverse convolution: a singular operator has no inverse on the full space. Although the checked sources do not appear to state the combined theorem, a nonindexed equivalent characterization could exist; the historical-priority comparison is qualified rather than exhaustive. Independent external mathematical validation has not been carried out.

## References
- M. Jerrum and K. Meeks, *The Parameterised Complexity of Counting Connected Subgraphs and Graph Motifs*, arXiv:1308.1575, first posted 2013-08-07, https://arxiv.org/abs/1308.1575.
- Y. Polyanskiy, *Hypercontractivity of spherical averages in Hamming space*, arXiv:1309.3014, first posted 2013-09-12, https://arxiv.org/abs/1309.3014.
- Y. Liao and Y. Hou, *Note on the subgraph component polynomial*, arXiv:1311.6856, first posted 2013-11-27, https://arxiv.org/abs/1311.6856.
- A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Asymptotic insights for Projection, Gordon–Lewis and Sidon Constants in Boolean Cube Function Spaces*, arXiv:2302.00233, https://arxiv.org/html/2302.00233v2, Section 3, Theorem 3.1.
