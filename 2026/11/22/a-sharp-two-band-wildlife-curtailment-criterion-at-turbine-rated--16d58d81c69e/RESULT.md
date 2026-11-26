# A sharp two-band wildlife curtailment criterion at turbine rated power

## Finding

Let \(R:(0,\infty)\to(0,\infty)\) be continuously differentiable. Suppose its logarithmic wind-speed elasticity \(\mathcal E(v)=vR'(v)/R(v)\) is continuous and strictly decreasing, with limits greater than 3 at zero and less than 0 at infinity (extended limits allowed). Let \(v_3<v_0\) be its unique crossings of 3 and 0. For a rated speed \(v_r>0\), put \(P(v)=\min(v^3,v_r^3)\) and \(q(v)=R(v)/P(v)\). The wind-speed density \(w\) is positive almost everywhere and normalized, with \(\int Rw\) and \(\int Pw\) finite and positive. For \(0<B<\int Rw\), maximize \(\mathcal P(u)=\int Pwu\) subject to \(\mathcal R(u)=\int Rwu\le B\) over measurable \(0\le u\le1\).

There is a unique \(c\in(0,\max q)\) with \(M(c):=\int_{\{q<c\}}Rw=B\). The unique optimizer up to \(w\)-null sets is \(u_*=\mathbf 1_{\{q<c\}}\). To define bands independently of the values assigned at individual wind speeds, take the essential support in \((0,\infty)\) of the curtailed portion \((1-u_*)w\,dv\): a point belongs to this closed set if every neighborhood has positive curtailed measure. A two-band policy has two positive-width closed intervals in this support, separated by an operating interval of positive width.

**Sharp law.** There is a nonempty open budget range with two bands if and only if \(v_3<v_r<v_0\), equivalently \(0<\mathcal E(v_r)<3\). In that case the precise cutoff and budget windows are
\[
q(v_r)<c<\min\{q(v_3),q(v_0)\},\qquad
M(q(v_r))<B<M(\min\{q(v_3),q(v_0)\}),
\]
where \(M(\max q)=\int Rw\) by continuous extension. The four band endpoints are respectively in \((0,v_3),(v_3,v_r),(v_r,v_0),(v_0,\infty)\). For all other admissible cases the essential support is one interval. At \(c=q(v_r)\) in the two-peak geometry, the literal strict superlevel set consists of two open intervals that meet in their closures at \(v_r\); there is no positive-width operating gap. At \(c=\min\{q(v_3),q(v_0)\}\), when this cutoff is admissible, the smaller peak makes no positive-width band. In particular, keeping or discarding the isolated level ties never changes the asserted bands. In the two-band window every feasible single cut-in policy \(\mathbf 1_{\{v\ge h\}}\) has strictly smaller expected power than \(u_*\).

## Assumptions and scope

Operation is a speed-only decision with no switching costs or minimum on/off duration. The cubic-to-rated power curve has neither a physical cut-in nor cut-out. The proxy \(R\) is the conditional risk when operating, and curtailment incurs no risk. The theorem is not a fitted mortality law and does not claim that any actual turbine or species satisfies the elasticity hypothesis. Wind speed is unaffected by decisions. Positive constant changes of units in \(P\) and \(R\) only rescale the objective, cutoff and budget as appropriate.

In the exact example below, if a separate hard physical cut-in is imposed below the first crossing, the same ratio cutoff and the same two discretionary bands remain optimal on the productive domain **at the correspondingly reduced budget**. The budget decreases by the original risk integral over the now unavailable region. This is not a claim that the crossings stay fixed at the original unadjusted cap or that physical unavailability counts as discretionary curtailment.

## Proof

**Ratio geometry.** Away from rated speed, \(vq'(v)/q(v)=\mathcal E(v)-3\) below \(v_r\), and \(vq'(v)/q(v)=\mathcal E(v)\) above \(v_r\). The ratio is continuous at \(v_r\). For \(v_3<v_r<v_0\), its four monotone pieces are increasing, decreasing, increasing, and decreasing; the maxima are at \(v_3,v_0\) and the minimum between them is at \(v_r\). Otherwise the joined branches increase strictly to one maximum and then decrease strictly; at a junction with zero one-sided derivative the same strict monotonicity conclusion holds. At zero, for some \(\epsilon>0\) one has \(\mathcal E-3>\epsilon\) on a sufficiently small interval. Integrating the logarithmic derivative gives \(q(v)=O(v^\epsilon)\) there. At infinity \(\mathcal E<-\epsilon'\) eventually for some \(\epsilon'>0\), so \(q(v)=O(v^{-\epsilon'})\) after integration. Therefore both tails of \(q\) tend to zero.

Each positive level has finitely many points. The essential support of \(\{q\ge c\}\) under \(w\,dv\) is the closure, relative to \((0,\infty)\), of \(\{q>c\}\): any open neighborhood meeting the strict superlevel set contains a positive-width subinterval on which \(w>0\) almost everywhere, and level ties alone contribute no mass. Reading the four monotone pieces gives two intervals with a positive-width gap exactly when the local minimum is strictly below the cutoff and both peaks are strictly above it. At the minimum level the two open pieces have a common endpoint in their closures; at a peak level that peak contributes no strict superlevel interval. When there is one peak the strict superlevel set is an interval for each allowed cutoff. In every case with \(c<\max q\) the strict superlevel set is nonempty.

**Budget and optimality.** The absence of atoms at ratio levels and dominated convergence give continuity of \(M\). Each nonempty open subinterval of \((0,\max q)\) has a preimage containing a nonempty open interval, so positivity of \(Rw\) gives strict increase of \(M\). Its endpoint limits are \(0\) and \(\int Rw\); this proves existence and uniqueness of \(c\) and converts the ratio window exactly to the budget window. If \(u\) is feasible, then
\[
\mathcal P(u_*)-\mathcal P(u)=
\int (u_*-u)(P-R/c)w+\frac{\mathcal R(u_*)-\mathcal R(u)}{c}\ge0.
\]
Indeed \(P-R/c\) is positive on \(q<c\), negative on \(q>c\), and zero at the level ties. The first term is strictly positive when \(u\) and \(u_*\) differ on a set of positive \(w\)-measure. A single cut-in rule cannot agree almost everywhere with the two-band policy, so the claimed strict power loss holds. This is not a converse about one-band policies: in this idealized model with no physical cut-in, \(q(v)\to0\) as \(v\downarrow0\), so \(u_*\) operates on a low-speed interval for every allowed budget. A positive cut-in threshold misses that interval, while a nonpositive threshold would run all the time and exceed the budget. In the optional physical cut-in modification, the same exchange argument on the restricted domain works with the reduced budget because the restricted indicator still spends that budget exactly.

**Exact example.** Take \(R(v)=v^4e^{-v},\ v_r=2,\ w(v)=e^{-v}\). Then \(\mathcal E(v)=4-v\), \(v_3=1\), and \(v_0=4\). The ratio equals \(ve^{-v}\) below rated speed and \(v^4e^{-v}/8\) at and above rated speed. From \(8/3<e<3\), one obtains \(2e^{-2}<3/10<e^{-1}\) and \(3/10<32e^{-4}\). At \(c=3/10\) the endpoints are the unique solutions of \(q(v)=3/10\) in the four stated monotone pieces, about \(0.489402227180,1.781337023422,2.108568625354,6.781072167850\). The all-on risk is \(3/4\). The exact-cap policy has risk about \(0.099673738415\) and power about \(0.353085030152\). The best single cut-in policy at this cap begins about \(3.744279531455\) and has power about \(0.189221311286\). It is the best because the single cut-in rule's risk and power both strictly decrease with its threshold. These are stylized model outputs, not field gains.

## Verification

The analytic proof covers all parameters, including the equality levels. The accompanying `CHECK.py` uses only Python's standard library and checks the exact example, with numerical bisection and elementary antiderivatives. It also checks the ordering of the budget at the rated-speed equality level, the interior example budget and the budget at the smaller peak. The numerical examples are supplementary, not proof of the universal statement.

## Relationship to prior work and limitations

The budget-selection rule is classical (an integral-budget exchange argument, related to the Neyman–Pearson lemma); only the explicit topology and sharp window under the given elasticity and power-curve hypotheses are at issue. Rogers studies general environmental curtailment with dynamic programming, and Behr et al. give bat-friendly operating algorithms trading off predicted fatality risk against energy. Their work motivates evaluating speed-by-speed risk and power. Whitby et al., Peterson et al. and Maclaurin et al. address measured curtailment effectiveness, acoustic exposure, and power loss under curtailment scenarios, respectively. These results should not be read as establishing the assumed elasticity at actual sites. The model leaves out empirical risk estimation, stochastic forecasts, species-specific risk weights, law and permitted fatality caps, wear, switching constraints, and turbine interactions; it is not an operational recommendation.

## References

1. Whitby et al., *A decade of curtailment studies demonstrates a consistent and effective strategy to reduce bat fatalities at wind turbines in North America* (2024), https://doi.org/10.1002/2688-8319.12371.
2. Peterson et al., *Acoustic Exposure to Turbine Operation Quantifies Risk to Bats at Commercial Wind Energy Facilities* (2021), https://doi.org/10.1002/wsb.1236.
3. Maclaurin et al., *National-scale impacts on wind energy production under curtailment scenarios to reduce bat fatalities* (2022), https://doi.org/10.1002/we.2741.
4. Rogers, *Optimal strategies for wind turbine environmental curtailment* (2020), https://doi.org/10.1002/we.2489.
5. Behr et al., *Reducing the Collision Risk for Bats at Onshore Wind Turbines (RENEBAT II)* (2016), https://tethys.pnnl.gov/publications/reducing-collision-risk-bats-onshore-wind-turbines-renebat-ii.
6. Neyman and Pearson, *On the Problem of the Most Efficient Tests of Statistical Hypotheses* (1933), https://doi.org/10.1098/rsta.1933.0009.
