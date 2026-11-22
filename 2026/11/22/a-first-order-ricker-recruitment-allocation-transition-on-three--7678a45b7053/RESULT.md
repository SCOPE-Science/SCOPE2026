# A first-order Ricker recruitment allocation transition on three or more identical spawning habitats

## Finding

Let there be an integer \(m\ge2\) identical, independent spawning habitats and a fixed, non-discardable total normalized spawning stock \(S>0\). If stocking density \(x_i\) in habitat \(i\) produces expected recruits proportional to \(f(x_i)=x_i e^{-x_i}\), the task is to maximize
\[
\mathcal R_m(S)=\max_{x_i\ge0,\ \sum_{i=1}^m x_i=S}\sum_{i=1}^m f(x_i).
\]

For \(m=2\), the equal allocation is uniquely optimal for \(S\le4\). For \(S>4\), the only optima are the two permutations of \((a,b)\), where \(1<a<2<b\) and \(a+b=S\). This transition is continuous: \(b-a\to0\) as \(S\downarrow4\).

For **every integer \(m\ge3\)**, there is exactly one critical total \(S_c(m)\) satisfying \(m<S_c(m)<2m\). Below it, equal allocation is uniquely optimal. At it, equal allocation and the \(m\) permutations of a strictly asymmetric allocation \((a,\ldots,a,b)\), \(1<a<2<b\), are exactly the global optima. Above it, only those \(m\) asymmetric permutations are optimal. In particular, global optimality of equal allocation ends *strictly before* the local stability threshold \(S=2m\), and the optimal excess-density gap jumps by a positive amount.

The complete threshold construction uses elementary scalar functions. For \(d>0\), define
\[
u(d)=\frac{d}{e^d-1},\qquad a(d)=1+u(d),\qquad b(d)=1+u(d)+d,
\]
\[
S_m(d)=m+d+m u(d),\qquad
H_m(d)=(m-1)f(a(d))+f(b(d))-m f\bigl(S_m(d)/m\bigr).
\]
For \(m\ge3\), let \(d_s(m)>0\) be the unique zero of \(S_m'(d)\), and \(d_2(m)>d_s(m)\) the unique positive zero of \(S_m(d)-2m\). There is a unique \(d_c(m)\in(d_s(m),d_2(m))\) with \(H_m(d_c)=0\), and
\[
S_c(m)=S_m(d_c(m)),\qquad
(a_c,b_c)=(a(d_c),b(d_c)),\qquad b_c-a_c=d_c>0.
\]
For any \(S>S_c(m)\), the unique \(d>d_s(m)\) satisfying \(S_m(d)=S\) generates its optimizers. For \(m=2\) and \(S>4\), use instead the unique positive \(d\) satisfying \(S_2(d)=S\).

For three habitats, \(S_c(3)=5.774313471725\ldots\), \(d_c(3)=1.397499519594\ldots\), and the asymmetric optimum at the transition is \((1.458937984044\ldots,1.458937984044\ldots,2.856437503638\ldots)\), up to permutation. The equal solution remains a strict **local** maximum there, so a local optimizer started at equality can miss the true global allocation immediately above the threshold.

## Assumptions and scope

- The model maximizes **one-generation total expected recruitment**, not equilibrium abundance, evolutionary stability, yield after harvest, or stochastic long-run growth.
- Each habitat has the same density-independent productivity multiplier and same crowding coefficient, with no dispersal or spillover during the recruitment step. The common positive productivity multiplier cancels from the optimizer. Densities are normalized by the inverse crowding coefficient.
- Every unit of the fixed total stock must be assigned to one of the \(m\) habitats. Allowing removal of excess stock changes the optimization problem and its high-density solution.
- The allocation variables are real nonnegative densities, rather than integer fish counts. The results hold for every real \(S>0\) and every integer \(m\ge2\).

## Proof

**1. Boundary exclusion and stationary structures.** The continuous objective reaches a maximum on the compact simplex. Since \(f'(x)=(1-x)e^{-x}\) and \(f'(0)=1>f'(z)\) for every \(z>0\), transferring a small positive amount from a positive coordinate to a zero coordinate strictly improves the objective. Every maximizing allocation is interior, so all partial derivatives are equal. The sign of \(f'\) makes it impossible for one coordinate to lie below \(1\) and another above \(1\). On \((0,2)\), \(f'\) is strictly decreasing; on \((2,\infty)\), it is strictly increasing. Thus every stationary allocation is equal or consists of two values \(1<a<2<b\). Moreover \(f''(x)=(x-2)e^{-x}>0\) for \(x>2\). If a purported maximum had two coordinates equal to \(b>2\), transferring an infinitesimal quantity between them would have positive second variation. Consequently every asymmetric maximum has **exactly one** large coordinate and \(m-1\) equal small coordinates.

**2. Stationarity parametrization.** Setting \(f'(a)=f'(b)\), writing \(u=a-1\) and \(d=b-a>0\), yields \(u=(u+d)e^{-d}\). Thus \(u=d/(e^d-1)\) and the stock sum is \(S_m(d)=m+d+m u(d)\). Conversely every \(d>0\) gives a stationary two-level allocation at that total. Since \(0<u(d)<1\), the specified densities satisfy \(1<a<2<b\).

**3. Geometry of stationary branches.** For \(h(d)=d/(e^d-1)\),
\[
h''(d)=\frac{e^d\{d(e^d+1)-2(e^d-1)\}}{(e^d-1)^3}>0\quad(d>0).
\]
The strict inequality follows from \(d>2\tanh(d/2)\). Also \(h'(0+)=-1/2\) and \(h'(\infty)=0\). Therefore \(S_m'=1+m h'\) increases strictly from \(1-m/2\) to \(1\). When \(m=2\), \(S_2\) is strictly increasing from \(4\). When \(m\ge3\), it decreases from \(2m\) to its unique strict minimum \(S_m(d_s)>m\), and then increases to infinity. The increasing branch crosses \(2m\) exactly once at \(d_2>d_s\).

**4. Only the increasing branch can maximize.** Holding \(S\) fixed, vary the common small density \(a\) and set the large density \(b=S-(m-1)a\). At a two-level stationary point the second derivative in this direction is
\[
(m-1)f''(a)+(m-1)^2 f''(b)
=(m-1)q\left[-\frac{1-u}{u}+(m-1)\frac{v-1}{v}\right],
\]
where \(v=b-1=u+d>1\) and \(q=u e^{-a}=v e^{-b}>0\). Its sign is the sign of \((m-1)+dv/du\), whereas \(du/dd<0\) and \(dS_m/dd=((m-1)+dv/du)du/dd\). Hence the second variation has sign opposite to \(S_m'(d)\). In particular the *decreasing* branch is not a local maximum; only the increasing branch remains as a possible asymmetric global optimum. At the branch minimum the equal configuration already has strictly larger reward, as shown next.

**5. One and only one global transition for \(m\ge3\).** Define \(H_m(d)\) in the finding. The common stationary marginal return gives the exact envelope identity
\[
H_m'(d)=\bigl[f'(a(d))-f'(S_m(d)/m)\bigr]S_m'(d).
\]
Whenever \(S_m(d)<2m\), the strict inequalities \(1<a(d)<S_m(d)/m<2\) and strict decrease of \(f'\) on \((1,2)\) make the bracket positive. Therefore \(H_m\) decreases strictly from its limiting value \(H_m(0+)=0\) to \(H_m(d_s)<0\), then increases strictly on \((d_s,d_2)\).

To prove positivity at the latter endpoint without relying on numerical tests, take \(S=2m\). The equal point has density \(2\) at every patch. Perturb the first \(m-1\) coordinates to \(2-\varepsilon\) and the last to \(2+(m-1)\varepsilon\). Since \(f''(2)=0\), \(f'''(2)=e^{-2}>0\), and \((m-1)^3-(m-1)>0\) when \(m\ge3\), Taylor's formula shows that this perturbation strictly improves reward for all sufficiently small positive \(\varepsilon\). A global maximum at \(S=2m\) must, by steps 1–4, be the unique stationary increasing-branch asymmetric candidate at \(d_2\). Thus \(H_m(d_2)>0\). By strict monotonicity on \((d_s,d_2)\), a unique root \(d_c\) exists there. The exhaustive candidate classification makes equal allocation globally optimal below \(S_c\), tied at \(S_c\), and strictly inferior above it. For \(S>2m\), the equal point has positive second variation and cannot maximize, and only the increasing asymmetric branch remains.

**6. Two patches.** For \(m=2\), the strictly increasing \(S_2(d)\) has range \((4,\infty)\). Thus there is no asymmetric stationary point at or below total \(4\), and equal allocation is the unique interior global maximizer. Above \(4\), equality has density greater than \(2\) and therefore positive second variation, leaving precisely the asymmetric permutations. Their gap tends to zero by continuity of \(S_2\) at \(d=0\). All boundary cases are included.

## Verification

The standalone `checker.py` uses only the Python standard library. Run `python checker.py` in the directory containing the extracted source to reproduce scalar root, stationary-gradient, equal-versus-asymmetric, and random-simplex consistency tests. In the reviewed run it completed 35,028 supplementary assertions for \(m=2,\ldots,10\), alongside 245 independent multistart constrained-optimizer comparisons. The analytic proof above establishes the infinite statement; finite checks alone could not establish global optimality, uniqueness, or the all-\(m\) quantifier.

## Relationship to prior work

The model uses the classical Ricker stock–recruitment function introduced by Ricker (1954). Jansen and Yoshimura (1998) examine risk spreading and use a two-habitat density-dependent Ricker analog, but optimize a different stochastic long-term growth quantity. Shepherd and Litvak (2004) study the assumptions and identification problems of ideal-free fish habitat use rather than a fixed-total recruitment maximization. Scheuerell (2016) solves the **single-stock maximum sustainable yield** problem with a Lambert function, not the spatial fixed-total, one-generation objective here. Skoglund et al. (2022) compare several imposed spatial spawner behaviors under Ricker and Beverton–Holt recruitment, but do not derive the exact fixed-total global optimum or its first-order phase change. Relevant broad allocation literature treats concave rewards or sigmoidal nonconcavity; the Ricker return here is eventually convex and has a decreasing limb, and none of the inspected results states the presented threshold theorem. The elementary KKT and curvature ingredients themselves are standard; the asserted contribution is their complete sharp global synthesis for the Ricker recruitment allocation problem.

## Limitations

The identical-patch forced-allocation benchmark is not a prescription to overcrowd any real habitat. Unknown patch quality, density dependence spanning patches, movement, discrete individuals, management costs and environmental stochasticity can change the optimum. A marginal/individual-choice ideal-free equilibrium need not maximize collective aggregate recruitment. Historical-priority searches cannot prove an exact theorem has never appeared, particularly in general nonconcave resource-allocation work. Skoglund et al.'s supplementary Appendix S1 was identified but its downloadable copy was inaccessible; it appears connected to proportional-capacity allocation rather than a proven global Ricker optimizer, but this unexamined appendix remains a specific residual risk.

## References

1. Ricker, W. E. (1954). *Stock and recruitment.* Journal of the Fisheries Research Board of Canada **11**, 559–623. https://doi.org/10.1139/f54-039 (historical model; exact original public day not established).
2. Jansen, V. A. A. & Yoshimura, J. (1998). *Populations can persist in an environment consisting of sink habitats only.* PNAS **95**, 3696–3698. Publicly dated 1998-03-31. https://doi.org/10.1073/pnas.95.7.3696 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC19898/ .
3. Shepherd, T. D. & Litvak, M. K. (2004). *Density-dependent habitat selection and the ideal free distribution in marine fish spatial dynamics: considerations and cautions.* Fish and Fisheries **5**, 141–152. First online 2004-05-24. https://doi.org/10.1111/j.1467-2979.2004.00143.x .
4. Scheuerell, M. D. (2016). *An explicit solution for calculating optimum spawning stock size from Ricker's stock recruitment model.* PeerJ **4**, e1623. Publicly dated 2016-01-25. https://doi.org/10.7717/peerj.1623 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC4800783/ .
5. Skoglund, S., Whitlock, R., Petersson, E., Palm, S. & Leonardsson, K. (2022). *From spawner habitat selection to stock-recruitment: Implications for assessment.* Ecology and Evolution **12**, e9679. First published 2022-12-28. https://doi.org/10.1002/ece3.9679 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9797469/ .
