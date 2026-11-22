# Three placement regimes versus universal balanced coverage in a two-crop pollination model

## Finding

**Theorem (complete two-crop placement classification and an objective reversal).** Fix a pollinator-source strength \(A>0\), a spatial attenuation rate \(k>0\), and two equivalent crop units at positions \(-d\) and \(+d\) with \(d>0\). A single movable floral-support source is placed at \(x\in\mathbb R\). Assume that the crop units independently receive effective pollination encounters according to Poisson laws with respective means
\[
\mu_{\pm}(x)=A\exp(-k|x\mp d|).
\]
A crop unit is called served if it receives at least one effective encounter. Define the expected number of served units and the probability that **both** units are served by
\[
S(x)=2-e^{-\mu_+(x)}-e^{-\mu_-(x)},\qquad
J(x)=(1-e^{-\mu_+(x)})(1-e^{-\mu_-(x)}).
\]
Write \(D=kd>0\), \(q=Ae^{-D}>0\), and \(f_D=D/\sinh D\). The **complete global maximizer classification** of \(S\) is:

1. If \(q\ge1\), the unique maximizer is \(x=0\).
2. If \(f_D<q<1\), exactly two maximizers occur at \(x=\pm t_*/k\), where \(t_*\in(0,D)\) is the unique positive solution of \(t_*/\sinh t_*=q\).
3. If \(0<q\le f_D\), exactly two maximizers occur at \(x=\pm d\).

In contrast, \(J\) is **uniquely maximized at \(x=0\) for every \(A,d,k>0\)**. Consequently, outside the central phase \(q\ge1\), every maximizer of expected coverage achieves strictly smaller joint coverage than the midpoint.

The boundaries are sharp, including equality cases, and the intermediate phase is nonempty for every \(D>0\). In terms of \(A\), the two thresholds are
\[
A_{\rm edge}(D)=\frac{2D}{1-e^{-2D}},\qquad
A_{\rm center}(D)=e^D,\qquad 1<A_{\rm edge}(D)<A_{\rm center}(D).
\]
For a fixed \(A>1\), widening the crop separation \(D\) induces the sequence **midpoint, two interior sites, crop endpoints**, with transitions at \(D=\log A\) and the unique \(D>\log A\) satisfying \(2D/(1-e^{-2D})=A\). For \(A\le1\), the two endpoints are always optimal for expected coverage. At the continuous midpoint-to-interior transition, for fixed \(D>0\) and \(q\uparrow1\),
\[
t_*/\sqrt{6(1-q)} \longrightarrow 1,
\]
where \(t_*\) is the dimensionless positive optimizer.

**Exact example.** Take \(k=1\), \(d=\log4\), and \(A=16\log2/3\). Then \(q=4\log2/3\), and exactly the sites \(x=\pm\log2\) maximize \(S\). At either site,
\[
S=2-2^{-8/3}-2^{-2/3}=1.2125493438\ldots,
\]
whereas at the unique joint-coverage optimizer \(x=0\), \(S=2-2\cdot2^{-4/3}=1.2062994740\ldots\). The probability of serving both is approximately \(0.31176191\) at \(x=\pm\log2\), versus \(0.36378961\) at the midpoint.

## Assumptions and scope

There are exactly two equally valued crop units on a line, one source with unrestricted location, and a common exponentially declining distance-response kernel. The amplitudes and attenuation are known and fixed; the source's movement does not alter the total population of pollinators or the kernel. Conditional effective-encounter counts are independent Poisson random variables. Any effective encounter suffices for success, with no additional reproductive or biological thresholds. The modeled effective encounters are **not** ordinary unqualified insect visits: a visit without conspecific pollen transfer need not qualify. There is no dependence between the two sites, visitation competition, depletion, crop-specific asymmetry, finite habitat footprint, landscape barriers, or stochastic source strength. All parameters are strictly positive, and all permitted source positions are real.

The two objectives reflect distinct questions: \(S\) measures expected count of crop units served, while \(J\) measures reliability that neither unit fails. No empirical calibration or field-design recommendation is claimed.

## Proof

For \(x>d\), increasing \(x\) increases the distance to **both** units, strictly decreasing both Poisson means. Thus both \(S\) and \(J\) decrease strictly on \((d,\infty)\); symmetry gives the analogous monotonicity on \(( -\infty,-d)\). Global maxima therefore lie in \([-d,d]\).

Set \(t=kx\in[-D,D]\). By symmetry it suffices to analyze \(0\le t\le D\). The two Poisson means are \(qe^t\) and \(qe^{-t}\), and
\[
\widetilde S(t)=2-e^{-qe^t}-e^{-qe^{-t}},\quad
\widetilde S'(t)=q\big(e^te^{-qe^t}-e^{-t}e^{-qe^{-t}}\big).
\]
For every \(t>0\), the logarithm of the ratio of the first term in parentheses to the second is
\[
2t-q(e^t-e^{-t})=2(t-q\sinh t).
\]
Consequently \(\widetilde S'(t)\) has the sign of \(t/\sinh t-q\). The function \(f(t)=t/\sinh t\), with its continuous value \(f(0)=1\), is strictly decreasing on \((0,\infty)\): its derivative has numerator \(\sinh t-t\cosh t<0\), as this numerator vanishes at zero and its derivative is \(-t\sinh t<0\). The derivative of \(\widetilde S\) is therefore negative at all \(t\in(0,D]\) when \(q\ge1\); strictly positive for \(t\in(0,D)\) when \(0<q\le D/\sinh D\); and changes sign exactly once from positive to negative for \(D/\sinh D<q<1\). Along with the strict exterior monotonicity, these cases prove **all** maximizers and all equality cases stated above. Since \(D/\sinh D<1\), the interior regime is always nonempty.

For the joint-coverage objective, define \(g(z)=\log(1-e^{-qe^z})\) for any real \(z\), with \(u=qe^z>0\). Direct differentiation gives
\[
g'(z)=\frac{u}{e^u-1},\qquad
g''(z)=\frac{u\big(e^u-1-ue^u\big)}{(e^u-1)^2}<0.
\]
The strict inequality follows because \(\psi(u)=e^u(1-u)-1\) vanishes at \(u=0\) and satisfies \(\psi'(u)=-ue^u<0\) for \(u>0\). Hence, on the interval between crops, \(\log J(x)=g(kx)+g(-kx)\) is strictly concave, symmetric, and uniquely maximized at \(x=0\). The earlier exterior monotonicity makes this maximum globally unique. Therefore each noncentral expected-coverage optimizer has strictly smaller joint coverage than the midpoint.

Multiplying \(q=1\) and \(q=D/\sinh D\) by \(e^D\) gives the claimed strength thresholds. Their strict ordering is equivalent to \(D<\sinh D\). The edge threshold \(2D/(1-e^{-2D})\) increases strictly from \(1\) to infinity: differentiation reduces positivity to \(e^{2D}>1+2D\). Thus when the strength is held fixed above \(1\), exactly the two specified separation thresholds are crossed, in the stated order. At strength at most \(1\), it lies below the edge threshold for every positive separation. Finally, \(t/\sinh t=1-t^2/6+O(t^4)\) as \(t\to0\), so the unique interior solution satisfies \(t_*\sim\sqrt{6(1-q)}\) as \(q\uparrow1\). This completes the proof.

For the exact example, \(\sinh(\log2)=3/4\), so \(f(\log2)=4\log2/3=q\). Also \(\sinh(\log4)=15/8\), so \(D/\sinh D=16\log2/15<q<1\), using \(\log2<3/4\). The classification yields precisely the two stated optima; substitution gives the exact objective value and the contrasting joint-coverage values.

## Verification

Run `python3 check.py` from the same directory. The independent implementation of the formulas checks a symbolic-design instance, compares the analytical optimizer to 301-grid competitors for 800 seeded random choices, and confirms the order of the two separation thresholds for five fixed strengths. The checker reports 482428 supplementary assertions. These numerical comparisons are tests, not proofs of the universal statements; the proof above is analytic and covers all positive real parameters and boundary cases. No experimental or clinical observations were used to verify the model.

## Relationship to prior work

Desaegher, Sheeren and Ouin (2021) studied spatial placement of flowering plots using the field-informed InVEST pollination model. It uses exponential spatial attenuation of visitation and predicts competing placement effects, but its published results concern visitation changes, competition/facilitation distances, and aggregation versus isolation, not the exact two-crop independent-Poisson optimization or the jointly served objective here. Ganser, Mayr, Albrecht and Knop (2018) measured distance-dependent effects of wildflower strips; Kortsch and colleagues (2023) emphasized that observed visits do not automatically imply successful pollination. Feldman, Morris and Wilson (2004) already use the standard Poisson-derived \(1-e^{-u}\) success response; no novelty is claimed for that transformation, exponential attenuation, Poisson independence, or general symmetry/concavity tools. The scope of the claim is the **combined sharp, three-phase global classification and opposing coverage objective for the stated two-crop spatial model**, not the ingredients individually. Literature priority has not been independently established.

## Limitations

The spatially symmetric, independent-Poisson assumptions are deliberately strong. Real crop units differ in value, visitation and pollen efficacy; pollinator movements and floral competition cause correlation and feedback. Optimizers may change under crop asymmetry, finite habitat constraints, non-exponential kernels, dispersal barriers, pollen-transfer requirements, and source-induced changes in pollinator abundance. The theorem proves no field benefit, species persistence guarantee, expected yield, or cost-effectiveness. Numerical tests verify selected instances but cannot establish universal correctness. A broader mathematical source, not identified by the inspected records, could contain an equivalent special case; mathematical priority requires further literature assessment.

## References

- Desaegher, J., Sheeren, D., and Ouin, A. (2021). *Optimising spatial distribution of mass-flowering patches at the landscape scale to increase crop pollination.* Journal of Applied Ecology. First published 17 June 2021. https://doi.org/10.1111/1365-2664.13949
- Ganser, D., Mayr, B., Albrecht, M., and Knop, E. (2018). *Wildflower strips enhance pollination in adjacent strawberry crops at the small scale.* Ecology and Evolution. https://doi.org/10.1002/ece3.4631
- Kortsch, S., et al. (2023). *Landscape composition and pollinator traits interact to influence pollination success in an individual-based model.* Functional Ecology. https://doi.org/10.1111/1365-2435.14353
- Feldman, T. S., Morris, W. F., and Wilson, W. G. (2004). *When can two plant species facilitate each other's pollination?* Oikos. https://doi.org/10.1111/j.0030-1299.2004.12845.x
