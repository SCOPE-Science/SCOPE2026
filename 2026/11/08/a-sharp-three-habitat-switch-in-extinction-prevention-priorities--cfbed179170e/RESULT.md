# A sharp three-habitat switch in extinction-prevention priorities

## Finding

On the three-habitat path \(L-C-R\), let the local extinction rates before intervention be \(1,t,1\), where \(t>0\). Each empty habitat is recolonized at rate \(c\) per occupied adjacent habitat, with \(c>0\). Initially all three habitats are occupied. Exactly one local extinction rate is halved permanently before the process starts. Write \(T_C(c,t)\) for the expected time until all habitats become empty when the center is protected, and \(T_L(c,t)\) for the expectation when one endpoint is protected. The two endpoint interventions are equivalent.

**Theorem (complete intervention phase diagram).** For every \(c>0\) and \(t>0\):

1. If \(0<t\le1\), then \(T_C(c,t)>T_L(c,t)\).
2. If \(1<t<6\), there is exactly one \(c_*(t)>0\), with \(T_L(c,t)>T_C(c,t)\) for \(0<c<c_*(t)\), equality at \(c=c_*(t)\), and \(T_C(c,t)>T_L(c,t)\) for \(c>c_*(t)\).
3. If \(t\ge6\), then \(T_L(c,t)>T_C(c,t)\).

Moreover \(c_*(t)\to0\) as \(t\downarrow1\), and \(c_*(t)\to\infty\) as \(t\uparrow6\). Three is the minimum number of habitats in a connected simple habitat graph for this type of optimal-priority reversal under the same one-rate-halving intervention.

For example, \(t=2\) gives a unique switch \(2.584<c_*(2)<2.585\); at \(c=1\), \(T_C-T_L=-38243/145208\), while at \(c=3\), \(T_C-T_L=10721/179952\).

## Assumptions and scope

The occupancy process is a continuous-time Markov chain on subsets \(S\subseteq\{L,C,R\}\). Each occupied site \(v\in S\) is lost at its specified local extinction rate \(e_v>0\). Each vacant site \(v\notin S\) becomes occupied at rate \(c\,|\{u\in S:u\sim v\}|\), summing contributions of its occupied neighbors. The empty set is absorbing. There is no external immigration, no simultaneous events and no change to colonization rates from protecting a patch. The starting state is \(\{L,C,R\}\). Rates are measured in units in which endpoint extinction before intervention is one. The intervention divides precisely one of the three local extinction rates by two. All comparisons concern **mean time to global extinction**, not stationary occupancy with immigration or finite-deadline survival probability.

## Proof

For any nonempty occupancy state \(S\), let \(m_S\) be its mean time to the absorbing empty state. The finite-state first-step equations are

\[
\bigg(\sum_{v\in S}e_v+\sum_{v\notin S}c\,\deg_S(v)\bigg)m_S
-\sum_{v\in S}e_v m_{S\setminus\{v\}}
-\sum_{v\notin S}c\,\deg_S(v)m_{S\cup\{v\}}=1,
\]

where \(m_\varnothing=0\) and \(\deg_S(v)=|\{u\in S:u\sim v\}|\). All nonempty states reach the empty state with positive probability; the transient generator is invertible, and these equations uniquely define finite expectations.

Ordering the seven nonempty states by their binary occupancy masks, exact elimination with extinction vectors \((1,t/2,1)\) and \((1/2,t,1)\) gives

\[
T_C(c,t)-T_L(c,t)=\frac{N(c,t)}{D(c,t)},\qquad N(c,t)=\sum_{j=0}^{7}A_j(t)c^j,
\]

where \(D(c,t)=2t(4c+t+2)(8c+t+4)H(c,t)\) and

\[
\begin{aligned}
H(c,t)={}&128c^4+(96t+288)c^3+(16t^2+276t+232)c^2\\
&+(96t^2+180t+78)c+12t^3+36t^2+33t+9.
\end{aligned}
\]

The coefficient certificate is

\[
\begin{aligned}
A_0(t)&=-(t-1)(20t^5+200t^4+775t^3+1240t^2+780t+144),\\
A_1(t)&=-2(200t^5+1238t^4+2071t^3-602t^2-2640t-912),\\
A_2(t)&=-2(12t^5+1502t^4+5551t^3+1840t^2-8202t-4568),\\
A_3(t)&=-4(120t^4+2774t^3+3943t^2-5786t-6016),\\
A_4(t)&=-8(359t^3+2243t^2-1590t-4564),\\
A_5(t)&=-32(2t^3+202t^2+51t-1006),\\
A_6(t)&=-384(t^2+9t-40),\\
A_7(t)&=-512(t-6).
\end{aligned}
\]

Every coefficient of \(H\) is positive for \(c\ge0,t>0\), so \(D(c,t)>0\). For each \(j\), the polynomial \(A_j\) has exactly one positive zero \(\theta_j\): for the two linear-factor cases this is immediate, and for the remaining six Descartes' rule of signs, together with opposite signs at zero and at infinity, proves uniqueness. Each \(A_j\) is positive below its positive zero and negative above it. Exact rational sign substitution isolates the zeros as follows:

| Coefficient | Exact rational isolation for its unique positive zero |
|---|---|
| \(A_0\) | \(\theta_0=1\) |
| \(A_1\) | \(1.06<\theta_1<1.07\) |
| \(A_2\) | \(1.16<\theta_2<1.17\) |
| \(A_3\) | \(1.32<\theta_3<1.33\) |
| \(A_4\) | \(1.58<\theta_4<1.59\) |
| \(A_5\) | \(2.08<\theta_5<2.09\) |
| \(A_6\) | \(3.26<\theta_6<3.27\) |
| \(A_7\) | \(\theta_7=6\) |

Thus \(1=\theta_0<\theta_1<\cdots<\theta_7=6\). For \(0<t\le1\), every \(A_j(t)\) is nonnegative, and at least one coefficient of positive degree is strictly positive; consequently \(N(c,t)>0\) for \(c>0\). For \(t\ge6\), all coefficients are nonpositive and at least one is strictly negative, hence \(N(c,t)<0\). For \(1<t<6\), \(A_0(t)<0\), \(A_7(t)>0\), and the coefficient signs when read in descending powers of \(c\) have exactly one change, from positive to negative, because the zeros \(\theta_j\) increase with \(j\). Descartes' rule gives **at most** one positive root of \(N(\cdot,t)\). The signs at zero and infinity give **at least** one root, proving existence, uniqueness, and the stated ordering. Continuity and strict signs at each fixed positive \(c\) when \(t=1\) or \(t=6\) prove the two endpoint limits of \(c_*(t)\).

For sharp minimality, any connected two-habitat simple graph is an edge. Normalize its initial extinction rates to \((1,t)\), with recolonization at rate \(c\) across the edge. Denote by \(U_1\) the mean extinction time when rate one is halved and \(U_2\) the time when rate \(t\) is halved. The three nonempty-state first-step equations yield

\[
U_2-U_1=-\frac{(t-1)(12c^2+12ct+12c+2t^2+7t+2)}{t(4c+t+2)(4c+2t+1)}.
\]

Its sign is independent of \(c\ge0\). Hence a connectivity-dependent switch between which extinction rate to halve is impossible on two connected patches, and one patch has no alternative intervention. The three-habitat example therefore attains the minimum.

## Verification

The accompanying standalone file `verify.py` reconstructs the seven-state transient generator, derives \(T_C\) and \(T_L\) by exact symbolic inversion, verifies the displayed polynomial identity, proves ordered coefficient-root isolations by exact rational signs and Descartes variations, and checks the two-habitat obstruction. Run `python verify.py` with Python 3 and SymPy installed. It also evaluates 35 exact rational three-habitat cases and isolates the concrete \(t=2\) crossover in \((2.584,2.585)\). All computations use exact arithmetic; the parametric theorem follows from the proof rather than sampled cases.

## Relationship to prior work

Etienne and Heesterbeek (2001) studied metapopulation management by changing patch extinction and colonization risks, providing qualitative rules of thumb. Frank (2004) examined connectivity versus habitat allocation via an approximation to established metapopulation lifetime. Ross and Pollett (2009) developed exact extinction-time formulas for a homogeneous patch-count model and compared policies using a spatially realistic model. Kitzes and Merenlender (2013) investigated competing patch-size and connectivity considerations in a different demographic simulation model. None of the inspected accessible full texts states the exact three-patch, rate-halving, all-parameter phase diagram, its universal cutoff \(t=6\), or the unique colonization crossing. The Etienne–Heesterbeek full text was not accessible during the literature examination, so historical priority remains subject to checking it and other specialized sources.

## Limitations

The result concerns a closed three-site path, a fixed half-rate intervention, symmetric per-edge colonization and initially complete occupancy. It does not provide the optimal policy for general networks, different intervention costs, non-Markov environmental effects or empirical reserve management. The historical-priority assessment is limited by unavailable material and is not an independent novelty certification.

## References

- R. S. Etienne and J. A. P. Heesterbeek, *Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model*, American Naturalist 158 (2001), 389–407. https://doi.org/10.1086/321986
- K. Frank, *Ecologically differentiated rules of thumb for habitat network design—lessons from a formula*, Biodiversity and Conservation 13 (2004), 189–206. https://www.cbd.int/doc/articles/2004/a-00069.pdf
- J. V. Ross and P. K. Pollett, *Rules of thumb for metapopulation management*, MODSIM 2009, 1795–1801. https://www.maths.uq.edu.au/MASCOS/MODSIM09/RossPollett.pdf
- J. Kitzes and A. Merenlender, *Extinction risk and tradeoffs in reserve site selection for species of different body sizes*, Conservation Letters 6 (2013), 341–349; first published online 13 February 2013. https://doi.org/10.1111/conl.12015
