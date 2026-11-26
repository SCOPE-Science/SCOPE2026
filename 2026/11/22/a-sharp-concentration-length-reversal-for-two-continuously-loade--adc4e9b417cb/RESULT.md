# A sharp concentration–length reversal for two continuously loaded saturating river reaches

## Finding

Consider two advective river reaches that receive the same constant lateral nutrient input and have the same maximum uptake rate but different half-saturation concentrations. Let \(F_H^t(x)\) be the scalar flow for residence time \(t\ge0\) of
\[
\dot C=s-\frac{kC}{H+C},\qquad C(0)=x\ge0,
\]
where \(H>0\) and \(s>k>0\). Fix \(K>L>0\) and a residence time \(a>0\) for the lower-affinity reach with parameter \(K\). For each residence time \(b>0\) of the higher-affinity reach with parameter \(L\), compare
\[
Q_{KL}(x;b)=F_L^b(F_K^a(x)),\qquad Q_{LK}(x;b)=F_K^a(F_L^b(x)).
\]
There is exactly one critical \(b_c>0\) with the following classification:

* For \(0<b<b_c\), there is exactly one switching inlet concentration \(x_*(b)>0\). The order \(K\) then \(L\) uniquely minimizes the outlet for \(0\le x<x_*(b)\), and \(L\) then \(K\) uniquely minimizes it for \(x>x_*(b)\). The outlets tie at \(x=x_*(b)\).
* For \(b=b_c\), there is a tie at \(x=0\) only, and \(L\) then \(K\) uniquely minimizes the outlet for every \(x>0\).
* For \(b>b_c\), \(L\) then \(K\) uniquely minimizes the outlet for all \(x\ge0\).

The switching concentration is strictly decreasing in \(b\), tends to zero as \(b\uparrow b_c\), and tends to the finite positive root \(c_0\) specified below as \(b\downarrow0\).

## Assumptions and scope

The variable \(t\) is travel or residence time, not calendar time. Reaches are steady, one-dimensional plug-flow compartments, with no diffusion, hydraulic feedback, biomass dynamics or upstream/downstream asymmetry other than order. The source concentration rate \(s\) and maximal Michaelis–Menten/Monod uptake rate \(k\) are common and constant. Both reach durations are held fixed in each comparison. Source input occurs continuously during traversal, not as an impulse between two removal maps. The source-dominated hypothesis \(s>k\) ensures that concentration grows along each reach. The comparison is of the final concentration, not cumulative removal or integrated exposure.

## Proof

**Flow coordinate.** Write \(w=s-k>0\) and \(f_H(c)=s-kc/(H+c)=(sH+wc)/(H+c)>0\). On \([0,\infty)\),
\[
\Psi_H(c)=\int_0^c\frac{du}{f_H(u)}
=\frac{c}{w}-\frac{kH}{w^2}\log\!\left(1+\frac{wc}{sH}\right).
\]
This function increases bijectively from \([0,\infty)\) onto \([0,\infty)\), and
\(F_H^t(c)=\Psi_H^{-1}(\Psi_H(c)+t)\). Thus the flows exist globally and increase strictly with their initial concentration and residence time.

**A single maximum in the displacement.** In the coordinate \(z=\Psi_L(c)\) the \(L\)-flow is translation by \(b\). Define
\[
H_a(z)=\Psi_L(F_K^a(\Psi_L^{-1}(z))),\qquad
\delta(z)=H_a(z)-z,\qquad r(c)=\frac{f_K(c)}{f_L(c)}.
\]
Differentiating the exact flow identity gives \(H_a'(z)=r(F_K^a(c))/r(c)\). Direct subtraction of the two ratios gives, for \(y>c\ge0\),
\[
r(y)-r(c)=\frac{k(K-L)(y-c)(sKL-wcy)}{(K+c)(K+y)(sL+wc)(sL+wy)}.
\]
The denominator and prefactors of \(sKL-wcy\) are positive. Because \(F_K^a(c)>c\), the sign of \(\delta'(z)\) is the sign of \(sKL-wcF_K^a(c)\). The product \(cF_K^a(c)\) strictly increases continuously from zero to infinity, so
\[
c_0F_K^a(c_0)=\frac{sKL}{w},\qquad z_0=\Psi_L(c_0)
\]
defines unique positive \(c_0,z_0\). Consequently \(\delta\) strictly increases up to \(z_0\) and strictly decreases after \(z_0\).

**Endpoint and critical time.** The speeds agree at zero: \(f_K(0)=f_L(0)=s\). For \(c>0\), however,
\[
f_K(c)-f_L(c)=\frac{k(K-L)c}{(K+c)(L+c)}>0.
\]
In fact, along the \(K\)-flow from any \(c\ge0\),
\[
\delta(\Psi_L(c))=\int_0^a r(F_K^u(c))\,du .
\]
At \(c=0\), \(F_K^u(0)>0\) for \(u>0\), so the integral is strictly larger than \(a\). At large \(c\), \(r(F_K^u(c))\to1\) uniformly in \(0\le u\le a\) since \(F_K^u(c)\ge c\) and \(r(v)\to1\). Thus \(\delta(0)>a=\lim_{z\to\infty}\delta(z)\). Strict increase up to \(z_0\) and strict decrease afterward show that there is exactly one positive solution of
\[
b_c>z_0,\qquad \delta(b_c)=\delta(0).
\]

**Classification.** The difference of outlet coordinates, \(L\) then \(K\) minus \(K\) then \(L\), equals
\[
D_b(z)=H_a(z+b)-H_a(z)-b=\delta(z+b)-\delta(z).
\]
Its sign is the sign of \(Q_{LK}(x;b)-Q_{KL}(x;b)\) at \(z=\Psi_L(x)\). When \(z+b\le z_0\), \(D_b(z)>0\); when \(z\ge z_0\), \(D_b(z)<0\). In between, where \(z<z_0<z+b\), its derivative \(\delta'(z+b)-\delta'(z)\) is negative. If \(b<b_c\), \(D_b(0)>0\) and \(D_b(z_0)<0\) give exactly one zero \(z_*(b)>0\), in the intermediate region, with sign positive below and negative above. If \(b=b_c\), \(D_b(0)=0\) and the intermediate and decreasing-side comparisons give negativity at all \(z>0\). If \(b>b_c\), \(D_b(0)<0\) and the same comparisons give negativity at all \(z\ge0\).

**Movement and limits of the inlet switch.** At an interior zero, \(z_*<z_0<z_*+b\), so \(\partial_zD_b=\delta'(z_*+b)-\delta'(z_*)<0\) and \(\partial_bD_b=\delta'(z_*+b)<0\). The implicit-function derivative is \(dz_*/db=-(\partial_bD_b)/(\partial_zD_b)<0\), and \(x_*(b)=\Psi_L^{-1}(z_*(b))\) decreases strictly as well. The straddling inequalities imply \(z_*(b)\to z_0\) as \(b\downarrow0\). As \(b\uparrow b_c\), any limit must be a zero of \(D_{b_c}\), whose only zero is at \(z=0\); hence \(x_*(b)\to0\).

## Verification

The formula for the flow and the equations for \(c_0,b_c,z_*(b)\) are suitable for monotone inversion and bracketed root finding. For \((s,k,K,L,a)=(2,1,4,1,1)\), they give \(z_0\approx1.4180063940\), \(b_c\approx8.1850904349\) and \(x_*(1)\approx1.5621163377\). The unchanged companion `verify.py` gives finite numerical diagnostics only; existence, uniqueness and the ordering for all permissible real parameters follow from the proof.

## Relationship to prior work and limitations

Empirical work on saturation and retention in successive stream reaches (Covino, McGlynn and Baker, 2010, DOI: 10.1029/2009JG001263; O'Brien et al., 2007, DOI: 10.1007/s10533-007-9073-7) motivates the rate law. Those empirical comparisons do not establish the theorem here. [Finite-step removal without continuous inflow](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-two-index-ordering-law-for-serial-saturating-nutrient-removal--15d05df5ff61), [finite-step removal with a single intermediate addition](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-source-driven-double-reversal-in-two-serial-saturating-stream--b38dab808a65), and [integrated stormwater exposure with linear wash-off](https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-sharp-three-stage-stormwater-exposure-ordering-with-continued-po--056749ef0302) concern different flow maps, source timing or objectives. The conclusion here is limited to the exact ordering and its joint inlet/residence-time boundary for the specified scalar model. It does not establish an ordering for \(s\le k\), differing sources or maxima, branching networks, variable hydraulics or biomass feedback. Residence time translates to physical length only given the travel speed. This is not an empirical recommendation for rearranging stream reaches, and historical priority is not guaranteed by the available comparisons.
