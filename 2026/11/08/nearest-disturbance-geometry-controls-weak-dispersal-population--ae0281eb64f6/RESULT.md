# Nearest-disturbance geometry controls weak-dispersal population synchrony

## Finding
Let a connected, undirected, finite weighted habitat graph have independent environmental disturbances at a nonempty subset of patches. Under homogeneous linear local regulation and symmetric diffusive migration, every stationary cross-correlation is positive at positive migration. Its exact weak-migration order and leading coefficient are determined solely by the shortest migration paths from the disturbance sources. In particular, zero-limit, positive-limit, and unit-limit population synchrony admit exact graph-theoretic classifications. With just one disturbance source, the limiting correlations depend only on the two distances from that source, not on the edge weights, local regulation rate, or disturbance intensity.

For vertices \(i,j\), let \(d(i,s)\) denote unweighted shortest-path *edge count* from environmental source \(s\), and let \(H_{is}\) be the sum of products of positive edge weights over all shortest \(i\)-to-\(s\) paths, taking \(H_{ss}=1\). Write
\[
 r_i=\min_{s\in S}d(i,s),\quad S_i=\{s\in S:d(i,s)=r_i\},\quad m_{ij}=\min_{s\in S}[d(i,s)+d(j,s)],\quad k_{ij}=m_{ij}-r_i-r_j\geq0.
\]
Define the positive quantities
\[
 V_i=\sum_{s\in S_i}\nu_sH_{is}^{2}{2r_i\choose r_i},\qquad
 B_{ij}=\sum_{\substack{s\in S:\\d(i,s)+d(j,s)=m_{ij}}}\nu_sH_{is}H_{js}{m_{ij}\choose d(i,s)}.
\]
For every two distinct vertices \(i,j\), their stationary Pearson correlation satisfies the **sharp asymptotic law**
\[
 \rho_{ij}(\varepsilon)=\frac{B_{ij}}{(2\lambda)^{k_{ij}}\sqrt{V_iV_j}}\,\varepsilon^{k_{ij}}+O(\varepsilon^{k_{ij}+1}),\quad\varepsilon\downarrow0.
\]
The displayed leading coefficient is strictly positive. Hence \(\rho_{ij}(\varepsilon)\) has a positive limit exactly when \(S_i\cap S_j\ne\varnothing\); otherwise it tends to zero at the exact positive integer order \(k_{ij}\).

When the nearest-source sets intersect, the limit simplifies to
\[
 \rho_{ij}(0+)=\frac{(r_i+r_j)!}{\sqrt{(2r_i)!(2r_j)!}}\cdot
 \frac{\sum_{s\in S_i\cap S_j}\nu_sH_{is}H_{js}}{\sqrt{\big(\sum_{s\in S_i}\nu_sH_{is}^{2}\big)\big(\sum_{s\in S_j}\nu_sH_{js}^{2}\big)}}.
\]
The first factor is at most one, with equality exactly for \(r_i=r_j\); the second is a weighted nonnegative cosine, at most one. Thus the limit equals one **if and only if** \(r_i=r_j\) and the vectors \((\sqrt{\nu_s}H_{is}\mathbf 1_{s\in S_i})_{s\in S}\) and \((\sqrt{\nu_s}H_{js}\mathbf 1_{s\in S_j})_{s\in S}\) are positive proportional. This also classifies every intermediate positive limiting value.

For a single source \(S=\{s\}\), an especially transparent universal law results:
\[
 \boxed{\lim_{\varepsilon\downarrow0}\rho_{ij}(\varepsilon)=\frac{[d(i,s)+d(j,s)]!}{\sqrt{[2d(i,s)]![2d(j,s)]!}}.}
\]
In the three-patch path \(0-1-2\), when only patch \(0\) is directly disturbed, the limits are \(\rho_{01}=1/\sqrt2\), \(\rho_{02}=1/\sqrt6\), and \(\rho_{12}=\sqrt3/2\). These are limits of normalized correlations: the variance at an undisturbed patch itself tends to zero.

## Assumptions and scope
Take a finite, connected, loopless, undirected graph \(G=(V,E)\) with \(n\geq2\) vertices and positive symmetric migration weights \(w_{uv}=w_{vu}>0\) on each edge. Its weighted Laplacian satisfies \(L_{ii}=\sum_{j\sim i}w_{ij}\) and \(L_{ij}=-w_{ij}\) for edges, zero otherwise. Fix \(\lambda>0\), migration strength \(\varepsilon>0\), a nonempty source set \(S\subseteq V\), and disturbance intensities \(\nu_s>0\) for \(s\in S\). Let \((B_s(t))_{s\in S}\) be independent standard Brownian motions. Consider the *linearized fluctuation* model
\[
 dX(t)=-(\lambda I+\varepsilon L)X(t)\,dt+\sum_{s\in S}\sqrt{\nu_s}\,e_s\,dB_s(t).
\]
All stochastic dynamics and correlations refer to its unique centered stationary Gaussian law; no claim is made that unrestricted Ornstein–Uhlenbeck values are biologically nonnegative population densities. Environmental forcing is temporally white, independent between active patches, and absent at all other patches. The limit fixes \(G,w,\lambda,S,\nu\) and sends only \(\varepsilon\downarrow0\). The graph-theoretic distance counts *edges*, while edge weights enter \(H_{is}\) as multiplicative path weights.

## Proof
Set \(Q=\sum_{s\in S}\nu_s e_se_s^\top\) and \(A=\lambda I+\varepsilon L\). Since the weighted Laplacian is symmetric positive semidefinite and \(\lambda>0\), \(A\) is positive definite, giving unique stationary covariance
\[
 C(\varepsilon)=\int_0^\infty e^{-At}Qe^{-At}\,dt,\qquad AC+CA=Q.
\]
In components,
\[
 C_{ij}(\varepsilon)=\sum_{s\in S}\nu_s\int_0^\infty e^{-2\lambda t}[e^{-\varepsilon Lt}]_{is}[e^{-\varepsilon Lt}]_{js}\,dt.
\]
For any two vertices, \((-L)^k_{is}=0\) when \(k<d(i,s)\), because an off-diagonal move changes the vertex along an edge, while diagonal stays cannot shorten a walk. At the first possible power, \((-L)^{d(i,s)}_{is}=H_{is}>0\): exactly the shortest paths contribute, each with its edge-weight product. This is also valid for \(i=s\) with distance zero. Consequently,
\[
 [e^{-\varepsilon Lt}]_{is}=\frac{H_{is}}{d(i,s)!}(\varepsilon t)^{d(i,s)}+O((\varepsilon t)^{d(i,s)+1}).
\]
This expansion may be integrated termwise to the required order: for every nonnegative integer \(a\), derivatives in \(\varepsilon\geq0\) of the symmetric contraction semigroup are bounded in operator norm by \(t^a\|L\|^a\); Taylor remainders therefore admit an integrable bound after multiplication by \(e^{-2\lambda t}\). Finally, \(\int_0^\infty e^{-2\lambda t}t^a\,dt=a!/(2\lambda)^{a+1}\).

For each source \(s\), its first contribution to \(C_{ij}\) occurs at order \(d(i,s)+d(j,s)\), with coefficient
\[
 \frac{\nu_sH_{is}H_{js}}{(2\lambda)^{d(i,s)+d(j,s)+1}}{d(i,s)+d(j,s)\choose d(i,s)}.
\]
All these first coefficients are positive, so they cannot cancel. Selecting the smallest source-summed distance \(m_{ij}\) gives
\[
 C_{ij}(\varepsilon)=\frac{B_{ij}}{(2\lambda)^{m_{ij}+1}}\varepsilon^{m_{ij}}+O(\varepsilon^{m_{ij}+1}).
\]
In particular,
\[
 C_{ii}(\varepsilon)=\frac{V_i}{(2\lambda)^{2r_i+1}}\varepsilon^{2r_i}+O(\varepsilon^{2r_i+1}),\qquad V_i>0.
\]
Dividing by \(\sqrt{C_{ii}C_{jj}}\) proves the sharp correlation expansion, including the strictly positive leading coefficient. Since \(m_{ij}\geq r_i+r_j\), equality holds exactly when some source minimizes both distances, or equivalently \(S_i\cap S_j\ne\varnothing\).

When equality holds, substitute the source distances \(r_i,r_j\) in the coefficient to obtain the product of the factorial overlap and weighted cosine displayed above. The factorial inequality \((r_i+r_j)!^2\le(2r_i)!(2r_j)!\) follows from log-convexity of factorials and is strict for unequal arguments. Cauchy–Schwarz gives the cosine bound and its proportionality equality condition. For \(\varepsilon>0\), connectedness and positive edge weights make the heat-kernel entries \([e^{-\varepsilon Lt}]_{is}\) strictly positive for \(t>0\); hence every \(C_{ij}(\varepsilon)>0\), and each diagonal variance is nonzero. This completes all quantifiers and cases.

A boundary noncommutation illustrates the role of *exactly absent* local noise: replace \(Q\) by \(Q+\eta I\) for \(\eta>0\). For fixed \(\eta>0\), as migration tends to zero the covariance tends to \((Q+\eta I)/(2\lambda)\), whose distinct-patch correlations are zero. Conversely, for fixed positive migration, the correlations are continuous as \(\eta\downarrow0\), recovering the sparse-source model; its subsequent zero-migration limit is positive whenever nearest disturbance sources overlap. Thus these two iterated limits differ for such patch pairs.

## Verification
The independent file `verify.py` implements exact rational formal power series of the Lyapunov equation \(2\lambda C^{(0)}=Q\) and \(2\lambda C^{(k)}=-(LC^{(k-1)}+C^{(k-1)}L)\), rather than evaluating the heat-kernel proof. It verifies all vanishing coefficients and first nonzero covariance and variance coefficients across four weighted connected habitat networks, using both one-source and multiple-source forcing and including multiple shortest paths. It passed 46 exact coefficient comparisons, among them five off-diagonal pairs whose nearest-source sets are disjoint. Running `python3 verify.py` requires only Python 3 standard libraries. These finite checks are not an exhaustive survey of arbitrary graphs; the preceding proof establishes the all-graph statement.

## Relationship to prior work
Haydon (1997) studied migration and regional environmental disturbances in metapopulation synchrony. Kendall and collaborators (2000) derived two-patch correlations for discrete-time dispersal and nondegenerate local/environmental noise, including a dispersal–environment interaction. Ren and collaborators (2010) and Grytskyy and collaborators (2013) treat general covariance relations for linear stochastic networks. Barzel and Biham (2009) studied shortest-path network response correlations of a different, deterministic susceptibility type. Yeakel and collaborators (2013) analyzed synchrony and topology in river metapopulations. Those frameworks motivate the object and provide broad covariance and graph tools; the result here is the explicit sharp sparse-source asymptotic with shortest-path multiplicities, complete limiting-correlation classification, and noncommuting zero-noise/zero-migration limits. The fundamental Lyapunov representation itself is well established, not claimed as new.

## Limitations
The theorem is confined to finite connected undirected networks, symmetric diffusion, homogeneous local linear damping, positive weights, fixed independent white-noise disturbance sources, and stationary Gaussian fluctuations. Different damping rates, edge directions, correlated or temporally colored environmental inputs, nonlinear regulatory dynamics, and finite-amplitude population effects are not covered. Correlations tending to one do not imply nonvanishing local variance or biologically persistent synchronized populations. No historical-priority or independent validation is certified beyond the inspected literature; specialized earlier work may imply some cases.

## References
- Haydon, D. (1997), *The effects of large and small-scale random events on the synchrony of metapopulation dynamics: a theoretical analysis*, Proceedings of the Royal Society B, https://doi.org/10.1098/rspb.1997.0191 (public date 1997-09-22).
- Kendall, B. E., Bjørnstad, O. N., Bascompte, J., Keitt, T. H., and Fagan, W. F. (2000), *Dispersal, environmental correlation, and spatial synchrony in population dynamics*, The American Naturalist, https://doi.org/10.1086/303350 (author-uploaded full text available at https://www.researchgate.net/publication/12540185_Dispersal_Environmental_Correlation_and_Spatial_Synchrony_in_Population_Dynamics).
- Barzel, B. and Biham, O. (2009), *Quantifying the connectivity of a network: The network correlation function method*, https://arxiv.org/abs/0910.3366 (initial submission 2009-10-18).
- Ren, J. and collaborators (2010), *Noise bridges dynamical correlation and topology in coupled oscillator networks*, https://arxiv.org/abs/1001.3966 (initial submission 2010-01-22).
- Grytskyy, D. and collaborators (2013), *A unified view on weakly correlated recurrent networks*, https://arxiv.org/abs/1304.7945 (initial submission 2013-04-30).
- Yeakel, J. and collaborators (2013), *Synchronisation and stability in river metapopulation networks*, https://doi.org/10.1111/ele.12228 (first published 2013-12-05).
