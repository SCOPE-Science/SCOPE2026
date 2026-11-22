# A one-overloaded-channel law and sharp two-assay symmetry breaking in inhibitor-limited environmental DNA screening

## Finding

For a fixed total water-extract input apportioned among \(m\ge2\) independently processed assay channels, each receiving independent Poisson target copies and Poisson assay-fatal inhibitor arrivals proportional to its allocated volume, global detection-optimal allocations have **at most two different volumes**: either all equal, or one oversized channel and \(m-1\) identically sized smaller channels. In the two-channel, equal-rate specialization, the balanced design undergoes an exact global symmetry-breaking transition at \(V_c=2\log(2+\sqrt3)\) in dimensionless total load. The result quantifies a nonlinear sampling-design risk under a deliberately idealized fatal-inhibitor model, not an empirical eDNA assay protocol.

## Assumptions and scope

Fix an integer \(m\ge2\), independent channels, rates \(\lambda>0\) and \(\mu>0\), total mandatory processed volume \(W>0\), and \(w_i\ge0\) with \(\sum_{i=1}^m w_i=W\). Channel \(i\) contains independent numbers of target molecules \(N_i\sim\operatorname{Poisson}(\lambda w_i)\) and independent fatal inhibitor units \(M_i\sim\operatorname{Poisson}(\mu w_i)\), independently across channels. Channel \(i\) is positive if and only if \(N_i\ge1\) and \(M_i=0\). A single inhibitor causes complete assay failure in its channel, even if target is present; no purification, dilution, false positives, sharing, or sample discarding is allowed. The chance of at least one positive is
\[
P(\mathbf w)=1-\prod_{i=1}^m f(w_i),\qquad f(w)=1-e^{-\mu w}+e^{-(\lambda+\mu)w}.
\]
The theorem concerns optimization under these assumptions, not whether the assumptions describe a particular field dataset.

## Proof

**A unique change in log-failure curvature.** Define \(g(w)=\log f(w)\), \(a=e^{-\mu w}\), and \(p=1+\lambda/\mu>1\). Direct differentiation yields
\[
 g''(w)=\frac{\mu^2a H(a)}{(1-a+a^p)^2},\quad
 H(a)=-1+p^2a^{p-1}-(p-1)^2a^p.
\]
On \(0<a<1\), \(H'(a)=p(p-1)a^{p-2}[p-(p-1)a]>0\), while \(H(0+)=-1\) and \(H(1)=2(p-1)>0\). Hence exactly one \(a_h\in(0,1)\) solves \(H(a_h)=0\); set \(h=-\mu^{-1}\log a_h\). Thus \(g\) is strictly convex on \((0,h)\) and strictly concave on \((h,\infty)\).

**Interior and structural global optimum.** The logarithm is increasing, so maximizing \(P\) is minimizing \(G(\mathbf w)=\sum_i g(w_i)\) on the closed simplex. Since \(g'(0)=-\lambda\), and
\[
 g'(w)+\lambda=\frac{\mu[(p-1)(1-a)+a(1-a^{p-1})]}{1-a+a^p}>0\qquad(w>0),
\]
any allocation with a zero coordinate and a positive coordinate can decrease \(G\) by moving an infinitesimal volume from the positive to the zero one. All global minima are interior. At an interior minimum, all \(g'(w_i)\) coincide. Two coordinates strictly above \(h\) are impossible: the feasible perturbation \((w_i,w_j)\mapsto(w_i+t,w_j-t)\) has second derivative \(g''(w_i)+g''(w_j)<0\) at zero. If every coordinate is at most \(h\), strict convexity and Jensen's inequality force all volumes to be equal. Otherwise precisely one coordinate exceeds \(h\). Every other coordinate lies strictly below \(h\), since equality to \(h\) would contradict the common derivative, as \(g'\) attains its unique maximum at \(h\). Strict increase of \(g'\) below \(h\) then forces these \(m-1\) smaller coordinates to coincide. This is a classification of all global optima, not an assertion that the unequal branch is unique at all parameters.

**Large mandatory volume.** The one-channel failure \(f(w)\) has its unique finite minimum at
\[
 w_0=\frac1\lambda\log(1+\lambda/\mu),\quad
 f_0=f(w_0)=1-\frac{\lambda}{\lambda+\mu}\left(\frac{\mu}{\lambda+\mu}\right)^{\mu/\lambda}.
\]
The critical point lies below \(h\), as \(f'(w_0)=0\) and \(g''(w_0)>0\). If \(W>mh\), an equal optimum is impossible (it lies in the strictly concave regime), so the one-large structure is necessary. Write its smaller coordinate \(s\in(0,h)\) and larger coordinate \(L=W-(m-1)s>h\). As \(W\to\infty\), uniformly in \(0\le s\le h\), one has \(L\to\infty\) and \(f(L)\to1\). Comparing any optimum to the feasible design \(s=w_0\), one deduces \(f(s)\to f_0\), hence \(s\to w_0\). The stationary equation \(g'(s)=g'(L)\), together with \(g''(w_0)=\lambda\mu e^{-\mu w_0}/f_0\) and \(g'(L)\sim\mu e^{-\mu L}\), gives
\[
 s=w_0+\frac{f_0}{\lambda}e^{\mu m w_0}e^{-\mu W}+o(e^{-\mu W}).
\]
Because \(g'(w_0)=0\), substituting this into the failure product gives the sharp asymptotic
\[
 \max_{\sum w_i=W}P(\mathbf w)
 =1-f_0^{m-1}+f_0^{m-1}e^{\mu(m-1)w_0}e^{-\mu W}+o(e^{-\mu W}).
\]
The positive correction records that as compulsory load increases, optimum success approaches its limiting value from above.

**Exact two-channel bifurcation for matching rates.** Now take \(m=2\), \(\lambda=\mu=\beta>0\), and set \(v_i=\beta w_i\), \(V=v_1+v_2\), \(a=e^{-v_1}\), \(b=e^{-v_2}\), \(z=ab=e^{-V}\), and \(S=a+b\). The allowed range is \(2\sqrt z\le S\le1+z\); equality at the lower endpoint means \(v_1=v_2=V/2\). Exact multiplication gives
\[
 (1-a+a^2)(1-b+b^2)=S^2-(1+z)S+1-z+z^2.
\]
This is a strictly convex quadratic in \(S\), with minimum at \(S_*=(1+z)/2\). This vertex enters the feasible interval precisely when \((1+z)/2\ge2\sqrt z\), equivalently \(V\ge V_c=2\log(2+\sqrt3)\). Therefore for \(0<V\le V_c\) the unique minimizing allocation is \(v_1=v_2=V/2\); for \(V>V_c\) exactly two ordered minimizing allocations result by swapping
\[
 a_\pm=\frac{S_*\pm\sqrt{S_*^2-4z}}2,\qquad
 (v_{\mathrm{small}},v_{\mathrm{large}})=(-\log a_+,-\log a_-).
\]
The optimized success probability is exactly
\[
 P_*(V)=\begin{cases}
 1-(1-e^{-V/2}+e^{-V})^2,&0<V\le V_c,\\
 1-\frac34(1-e^{-V})^2,&V\ge V_c.
 \end{cases}
\]
The two branches agree at \(V_c\). Since \(z_c=e^{-V_c}=7-4\sqrt3\) and \(S_*^2-4z\) has first derivative \(2\sqrt3\,z_c\) in \(V\) at the threshold, the optimal load separation satisfies
\[
 v_{\mathrm{large}}-v_{\mathrm{small}}=\sqrt{2\sqrt3}\,\sqrt{V-V_c}+O(V-V_c)^{3/2}\quad(V\downarrow V_c).
\]
The exact quadratic argument proves global optimality and exhaustiveness, including boundary allocations, without relying on numerical search.

## Verification

The standalone `check.py` uses only Python 3 standard-library modules. Execute `python3 check.py` from a directory containing this file. It verifies the exact symmetric polynomial identity by sparse polynomial arithmetic, transition identities, candidate allocations against finite grids and seeded random competitors, the square-root coefficient, curvature signs for five unequal intensity pairs, and asymptotic diagnostics. On the packaged version it prints `PASS 40212 finite and symbolic assertions`. The analytic proof above, not this finite set of tests, establishes the quantified theorem. For \(V=5\), the optimal dimensionless allocations are approximately \((0.7141522009,4.2858477991)\), with success probability \(0.2600728706\), while equal loading gives \(0.1450169251\).

## Relationship to prior work

Jane et al. (first publicly available 2014-05-28) directly document severe qPCR inhibition in high-target-copy stream samples, motivating the competing target-load and inhibitor mechanisms. Herder et al. (2014) explicitly describe a practical larger-volume versus more-inhibitors tradeoff. Mächler et al. (2015) examine water volume and field detection, not the exact Poisson fatal-inhibitor model's global split optimization in the available abstract. Vicentini (1970) treats generic S-shaped resource-allocation objectives, so the abstract structural logic is not presented as a novel general principle; the new mathematical target is the specified Poisson-inhibition objective, its all-rate one-overloaded-channel classification and large-load law, and its exact two-channel global transition and coefficient. The full report for Vicentini and the complete Mächler paper were not inspected, creating a residual priority risk. Existing related eDNA replicate-count and detection-identifiability results concern different objective functions and do not imply this volume-splitting formula. Exact historical priority is not independently certified.

## Limitations

This is a model theorem, not an empirical claim: inhibitors are assumed all-or-nothing, independent and homogeneous Poisson; DNA target arrival and inhibitors are independent; all \(W\) must be processed even when excess volume could otherwise be discarded or diluted; all channels are independent with identical rates. Removing the mandatory-use constraint allows discarding surplus and destroys the overloaded-channel necessity. Channel-dependent extraction efficiency, threshold inhibition, PCR replicates, correlation, contamination, and false-positive pathways are omitted. The asymptotic law refers to increasing a compulsory volume at fixed positive rates and fixed channel count, not to increasing practical detection certainty. No empirical optimal volumes or general eDNA workflow recommendation are implied.

## References

1. Jane, S. F., Wilcox, T. M., McKelvey, K. S., et al. (2014/2015). *Distance, flow and PCR inhibition: eDNA dynamics in two headwater streams*. Molecular Ecology Resources. First online 2014-05-28. DOI: 10.1111/1755-0998.12285. Author-hosted full text: https://www.umt.edu/lowe-lab/documents/publications/Jane%20et%20al%202014%20MER.pdf
2. Herder, J. E., et al. (2014). *Environmental DNA: a review of the possible applications for the detection of (invasive) species*. https://www.environmental-dna.nl/Portals/%5B7%5D/Herder%20et%20al%202014%20-%20Environmental%20DNA%20review.pdf
3. Mächler, E., Deiner, K., Spahn, F., and Altermatt, F. (2015). *Fishing in the Water: Effect of Sampled Water Volume on Environmental DNA-Based Detection of Macroinvertebrates*. DOI: 10.1021/acs.est.5b04188. Available abstract only for comparison.
4. Vicentini, F. M. (1970). *On the Resource Allocation Problem with S-Shaped Utility Functions*. Case Western Reserve University Technical Memorandum 201. https://commons.case.edu/wsom-ops-reports/370/. Available abstract only for comparison.
