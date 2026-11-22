# A sharp seasonal-concentration threshold for joint detection of two aquatic taxa

## Finding

For two independently detected taxa with opposing seasonal detection hazards, a fixed total Poisson survey effort has a **unique optimal effective season**. If the harder-to-detect taxon is sufficiently disadvantaged, increasing survey effort produces exactly one transition from a compromise season to exclusive use of its peak season; otherwise an interior compromise remains strictly optimal at every finite budget. The exact boundary is
\[
\beta(1-u)>\alpha(1+u),
\]
where \(0<\alpha<\beta\) are baseline encounter rates and \(0<u<1\) is the shared fractional seasonal amplitude. The result determines the transition budget, proves monotonic movement of the optimum, and shows that, under the stated idealized model, splitting an effort budget among seasons cannot outperform a single appropriately chosen season.

## Assumptions and scope

Let \(S\) be a survey-season domain, and let \(h:S\to[-1,1]\) attain every value in \([-1,1]\); for example \(h(t)=\cos t\) over a full annual cycle. Suppose two known-present aquatic taxa are encountered according to **independent** Poisson counting processes, with per-unit-survey-effort hazards \(\alpha(1+u h(t))\) and \(\beta(1-u h(t))\), respectively, where \(0<\alpha<\beta\) and \(0<u<1\). Distinct survey blocks have independent Poisson increments. A finite allocation chooses times \(t_j\in S\) and nonnegative efforts \(e_j\) satisfying \(\sum_j e_j=B>0\). The objective is the probability of detecting **both** taxa at least once during all blocks. No setup cost, false-positive event, shared random environmental multiplier, unknown occupancy, or temporal depletion is included. Effort is continuously divisible.

Define the effective seasonal index
\[
m=\frac{1}{B}\sum_j e_jh(t_j)\in[-1,1].
\]
The objective is exactly
\[
J_B(m)=\bigl(1-e^{-B\alpha(1+um)}\bigr)\bigl(1-e^{-B\beta(1-um)}\bigr).
\]
Because \(h\) attains the full interval, every such \(m\) can be attained by putting all effort at one season. This equivalence concerns the probability of joint detection, not all possible statistics of the survey record.

## Proof

**1. Reduction and strict uniqueness.** Poisson superposition gives the two total means \(X=B\alpha(1+um)\) and \(Y=B\beta(1-um)\), and independence gives \(J_B\). Since \(0<u<1\), both means are strictly positive. For \(g_B(m)=\log J_B(m)\),
\[
g'_B(m)=Bu\left(\frac{\alpha}{e^X-1}-\frac{\beta}{e^Y-1}\right),
\]
\[
g''_B(m)=-(Bu)^2\left(\frac{\alpha^2e^X}{(e^X-1)^2}+\frac{\beta^2e^Y}{(e^Y-1)^2}\right)<0.
\]
The function \(z\mapsto z/(e^{Bz}-1)\) is strictly decreasing for \(z>0\), because its derivative has numerator \(e^{Bz}(1-Bz)-1<0\). Thus \(g'_B(0)>0\). Strict concavity implies a unique maximizer \(m_B\in(0,1]\), with \(m_B=1\) exactly if \(g'_B(1)\ge0\), and otherwise \(m_B\in(0,1)\) is the unique solution of
\[
\frac{\alpha}{e^{B\alpha(1+um_B)}-1}=\frac{\beta}{e^{B\beta(1-um_B)}-1}.
\]
There is no other local or global maximum.

**2. Sharp finite-budget phase transition.** Set \(x=\alpha(1+u)\) and \(y=\beta(1-u)\). If \(y\le x\), then \(\beta>\alpha\) implies \(\alpha/(e^{Bx}-1)<\beta/(e^{By}-1)\) for every \(B>0\), so \(m_B<1\) always. If \(y>x\), define
\[
R(B)=\frac{e^{By}-1}{e^{Bx}-1}.
\]
The function \(R\) is strictly increasing: \((\log R)'=y/(1-e^{-By})-x/(1-e^{-Bx})>0\), since \(z/(1-e^{-Bz})\) is strictly increasing for \(z>0\). Moreover \(R(0+)=y/x=(\beta/\alpha)(1-u)/(1+u)<\beta/\alpha\), while \(R(B)\to\infty\). Therefore there is a unique \(B_c>0\) satisfying
\[
\boxed{\frac{e^{B_c\beta(1-u)}-1}{e^{B_c\alpha(1+u)}-1}=\frac{\beta}{\alpha}}.
\]
The boundary derivative has the sign of \(R(B)-\beta/\alpha\). Consequently \(0<m_B<1\) for \(B<B_c\) and \(m_B=1\) for \(B\ge B_c\). This establishes both necessity and sufficiency of \(\beta(1-u)>\alpha(1+u)\) for finite-budget concentration.

**3. Monotone movement with effort.** For an interior maximizer set \(x(m)=\alpha(1+um)\), \(y(m)=\beta(1-um)\) and
\[
H(B,m)=\log\frac{e^{By(m)}-1}{e^{Bx(m)}-1}-\log(\beta/\alpha).
\]
Stationarity is \(H(B,m_B)=0\). It implies \(y(m_B)>x(m_B)\), since \(\beta/\alpha>1\). Hence \(H_B>0\) by the monotonicity just proved; \(H_m<0\) because \(x'(m)>0\) and \(y'(m)<0\). The implicit-function theorem yields \(m'_B=-H_B/H_m>0\) wherever the optimum is interior. In the concentrating regime it then stays at \(1\) above \(B_c\). Thus \(m_B\) is nondecreasing on \((0,\infty)\), strictly increasing before any boundary contact.

**4. Small and large effort.** Expand \(z/(e^{Bz}-1)=1/B-z/2+O(B)\) at bounded positive \(z\). The interior stationarity equation, with \(m_B\to0\), gives
\[
\boxed{m_B=\frac{\beta-\alpha}{4u}B+O(B^2)}\qquad(B\downarrow0).
\]
Define \(m_\infty=(\beta-\alpha)/(u(\alpha+\beta))\). If \(m_\infty<1\), then at \(m=m_\infty\) the two rates are equal and \(g'_B(m)<0\), so \(0<m_B<m_\infty\) for every finite budget. The stationarity identity forces \(m_B\to m_\infty\), and writing \(\log(e^{Bz}-1)=Bz+\log(1-e^{-Bz})\) gives
\[
\boxed{m_\infty-m_B\sim\frac{\log(\beta/\alpha)}{u(\alpha+\beta)B}}\qquad(B\to\infty).
\]
The same asymptotic holds with \(m_\infty=1\) in the equality case \(\beta(1-u)=\alpha(1+u)\), where the optimum never reaches \(1\) at finite budget. When \(m_\infty>1\), finite-budget concentration was already proved. These three cases exhaust the parameter domain. A general unequal rate ordering is handled by exchanging taxa and reversing the seasonal index; equal baseline rates give the unique index \(m_B=0\).

**5. Concrete attainable case.** With \(\alpha=1\), \(\beta=4\), and \(u=1/2\), the sharp concentration budget is \(B_c=2\log z_*\), where \(z_*>1\) is the unique root on \((1,\infty)\) of \(z^4-4z^3+3=0\); in particular \(39/10<z_*<4\). Numerically \(B_c\approx2.748126244919951\), and \(m_1\approx0.7305057049338\), while \(m_B=1\) for every \(B\ge B_c\). The bracketing is exact; the numerical decimals are illustrative only.

## Verification

`check.py` (standard library only) evaluates the derived first-order equation by bisection, checks the example polynomial with exact fractions, compares the inferred maximum against discretized alternatives, and stress-tests monotonicity over randomly selected positive parameter triples. Run `python check.py` in a Python 3 environment. This is supplementary verification of computations, not a substitute for the inequalities and global proof above. The example's root bracket uses exact rational arithmetic.

## Relationship to prior work

Rounds et al. (2024) document species-specific seasonal changes in invasive-species eDNA detection, including opposing early- and late-season detection preferences, and discuss sampling tradeoffs. Their observed phenologies are not assumed to obey the exact anti-phase hazard model here. Moore and McCarthy (2016) study ecological surveillance effort with Poisson encounter processes, uncertain temporal detection rates and spatial/travel costs; their expected-detections objective does not establish the joint two-taxon product-optimal phase boundary above. Flitcroft et al. (2025) examine multispecies eDNA sampling times and replicates empirically. The specific exact concentration threshold, unique effective season, and monotone budget law were not identified in the inspected sources. This literature comparison is limited and is not a claim that no prior equivalent mathematical result exists.

## Limitations

The conclusion depends on independent conditional Poisson taxa counts, deterministic anti-phase hazards, divisible effort, no fixed visit costs, and a season that attains every normalized phase value. Correlated eDNA patchiness, season-specific prevalence, sample-processing constraints, nonlinear response functions, uncertainty in hazards or a different objective can favor temporal diversification. The result neither calibrates the hazards to field data nor establishes a universal ecological sampling prescription. No independent external validation has been performed.

## References

1. Rounds, C. I., et al. (2024). Aquatic invasive species exhibit contrasting seasonal detectability patterns based on environmental DNA: Implications for monitoring. *Freshwater Biology* 69, 1479–1493. First published 17 August 2024. https://doi.org/10.1111/fwb.14320
2. Moore, A. L., and McCarthy, M. A. (2016). Optimizing ecological survey effort over space and time. *Methods in Ecology and Evolution* 7, 891–899. https://doi.org/10.1111/2041-210X.12564
3. Flitcroft, R. L., et al. (2025). Multi-species eDNA as a screening tool to facilitate early detection and eradication of aquatic invasive species in large water bodies. *Scientific Reports* 15, 33615. https://doi.org/10.1038/s41598-025-19083-7
