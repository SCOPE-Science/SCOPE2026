# A sharp interior adoption window for mixed time- and emissions-routing on two roads

## Finding

In a two-road traffic network, converting **some but not all** drivers from time-routing to emissions-routing can yield strictly lower total emissions than either entirely time-routing or entirely emissions-routing. For continuously increasing road-specific private costs, an exact clamping law determines the unique mixed-class Wardrop equilibrium. For affine emission costs it gives a sharp, necessary-and-sufficient coefficient condition for an interior optimal adoption share and exact emissions savings over both pure endpoints.

## Assumptions and scope

A fixed unit mass of nonatomic drivers chooses one of two parallel roads. A fraction \(\theta\in[0,1]\) minimizes its own per-trip emissions (class E), while the remaining fraction \(1-\theta\) minimizes its own time (class T). The two classes are physically identical in their effect on road congestion; only the private objective differs. If aggregate road-1 flow is \(x\in[0,1]\), road-2 flow is \(1-x\).

For each class \(K\in\{T,E\}\), write the private road-cost difference as \(D_K(x)=c_{K,1}(x)-c_{K,2}(1-x)\). Assume both functions are continuous and strictly increasing on \([0,1]\), with unique zeros \(a\) and \(b\) such that \(0<a<b<1\). In particular, the two private objectives favor road 1 below their respective equal-cost flows. The Wardrop condition is imposed separately for both classes: a class may use a road only when it has no greater private cost than the alternative.

For the emissions-optimality classification, additionally assume per-trip emission functions \(e_1(x)=u+vx\) and \(e_2(y)=w+zy\), with \(u,w\ge0\), \(v,z>0\), and \(b=(w+z-u)/(v+z)\in(0,1)\). All total emissions are for the full unit demand, including both user classes. Time functions need only satisfy the monotonicity and unique-zero assumptions; they need not be affine.

## Proof

**1. Mixed-class equilibrium.** If \(x<a\), both \(D_T(x)\) and \(D_E(x)\) are negative, so both classes would use road 1 exclusively. This contradicts \(x<a<1\). Similarly, if \(x>b\), both classes would use road 2 exclusively, contradicting \(x>b>0\). Thus \(a\le x\le b\).

If \(a<x<b\), the time-routing drivers strictly prefer road 2 and emissions-routing drivers strictly prefer road 1. Hence the only possible aggregate road-1 flow is \(x=\theta\). At \(x=a\), class E uses road 1 and class T is indifferent; equilibrium exists exactly when \(\theta\le a\), with class-T road-1 flow \(a-\theta\). At \(x=b\), class T uses road 2 and class E is indifferent; equilibrium exists exactly when \(\theta\ge b\), with class-E road-1 flow \(b\). Each allocation also satisfies all Wardrop inequalities. Consequently the equilibrium is unique even at \(\theta=0,1,a,b\), and

\[
x(\theta)=\begin{cases}a,&0\le\theta\le a,\\\theta,&a\le\theta\le b,\\b,&b\le\theta\le1.\end{cases}
\]

The separate road-1 class flows are \(x_E(\theta)=\min\{\theta,b\}\) and \(x_T(\theta)=x(\theta)-x_E(\theta)\); this explicitly reconstructs the complete equilibrium.

**2. System emission optimum.** With \(y=1-x\), aggregate emissions are

\[
G(x)=x(u+vx)+(1-x)(w+z(1-x))=(v+z)x^2+(u-w-2z)x+w+z.
\]

Set \(\rho=z/(v+z)\in(0,1)\). The private emissions equal-cost identity \(u+vb=w+z(1-b)\) gives \(u-w-z=-(v+z)b\). Completing the square, with \(s=(b+\rho)/2\), yields

\[
G(x)=G(s)+(v+z)(x-s)^2.
\]

By the equilibrium result, the attainable aggregate flows as adoption varies are exactly the closed interval \([a,b]\). Because \(v+z>0\), the unique optimal aggregate flow is \(x_* = \min\{b,\max\{a,s\}\}\). If \(a<s<b\), the unique adoption share attaining it is \(\theta_*=s\), and

\[
G(a)-G(s)=(v+z)(s-a)^2>0,\qquad G(b)-G(s)=(v+z)(b-s)^2>0.
\]

The strict interior condition \(a<s<b\) is precisely \(2a-b<\rho<b\). If \(s\le a\), then and only then \(\theta\in[0,a]\) is optimal; if \(s\ge b\), then and only then \(\theta\in[b,1]\) is optimal. Equality at the wedge boundaries is included in these plateau cases. This is the exhaustive classification.

**3. Exact witness.** Take \(t_1(x)=1+4x\), \(t_2(y)=1+y\), \(e_1(x)=1+4x\) and \(e_2(y)=4+y\). The class-indifference equations give \(a=1/5\), \(b=4/5\), and \(\rho=1/5\). Thus \(s=1/2\), and the system emission function simplifies to \(G(x)=5-5x+5x^2\). Its three exact values are \(G(1/5)=G(4/5)=21/5\) and \(G(1/2)=15/4\). Each pure-routing endpoint therefore emits \(9/20\) more units than the optimal mixed adoption share.

## Verification

The attached standalone Python script `check_mixed_routing.py` uses only the standard-library exact-rational arithmetic type. It constructs 3,000 independent rational parameter samples satisfying the hypotheses and examines six candidate adoption fractions in each sample. For each case it checks class conservation, every applicable Wardrop inequality, the exact square identity, and global optimality on the derived feasible-flow interval. It also checks the exhibited rational witness and the exact gains. These finite checks are supplementary: the argument above, not random testing, proves the result for all admissible parameters.

Run with `python check_mixed_routing.py`. All calculations of the rational witness are exact, without floating-point tolerances.

## Relationship to prior work

Cotta Antúnez and Levin (2022, arXiv:2207.13698, sections 3.3 and 4.1) formulated mixed time/emissions user equilibrium but explicitly compared only fully time-routing and fully emissions-routing on their two-road test because of general multiclass multiplicity concerns. Their general network algorithms and nonlinear emissions model are different from the affine two-road theorem proved here. Earlier dynamic network simulations by Ahn and Rakha (2013) investigated market penetration empirically, not the present universal two-road exact coefficient wedge.

Crucially, uniqueness **by itself is not claimed as novel**: Milchtaich (2005) proved much broader equilibrium-cost uniqueness for parallel networks with user-specific strictly increasing costs. The distinguishing claim here is the explicit dependence on emissions-routing adoption, the sharp necessary-and-sufficient interior optimality condition for *total emissions*, the complete endpoint-plateau classification, and exact improvements over both pure-route populations. General multiclass-equilibrium formulations (Marcotte and Wynter, 2004) do not supply these scalar results. A separately published two-route priced-externality result addresses a *pricing* variable, rather than the endogenous mix of road users with different objective functions. These are comparisons of the actual implications, not assertions of global historical novelty.

## Limitations

This is a static nonatomic unit-demand two-link model with homogeneous congestion impact and strictly increasing costs. The emission curves are affine and the equilibrium time indifference point is strictly below the emission indifference point. It does not establish a corresponding condition for nonlinear engine-emission models, multiple origin–destination networks, heterogeneous vehicle impacts, stochastic delays, discrete drivers, or dynamic guidance. The coefficient example is illustrative; none of its values is calibrated to an observed road. An earlier paper might contain a mathematically equivalent adoption-share classification despite the literature searches and inspections described in the review. Independent external verification of priority and applicability is still outstanding.

## References

- R. Cotta Antúnez and M. W. Levin, *How Does Eco-Routing Affect Total System Emissions? City Network Predictions From User Equilibrium Models*, 2022, arXiv:2207.13698 (first public preprint 2022-07-24), https://arxiv.org/abs/2207.13698.
- I. Milchtaich, *Topological Conditions for Uniqueness of Equilibrium in Networks*, Mathematics of Operations Research **30** (2005), 225–244, doi:10.1287/moor.1040.0122, https://econ.biu.ac.il/sites/econ/files/shared/staff/u36/papers/uniqueness.pdf.
- K. Ahn and H. Rakha, *Network-wide impacts of eco-routing strategies: A large-scale case study*, Transportation Research Part D **25** (2013), 119–130, doi:10.1016/j.trd.2013.09.006.
- P. Marcotte and L. Wynter, *A New Look at the Multiclass Network Equilibrium Problem*, Transportation Science **38** (2004), 282–292, doi:10.1287/trsc.1030.0039.
- A separately indexed result: *Exact monotonicity classification for a two-route priced externality*, published-finding corpus (2026-10-26), *Exact monotonicity classification for a two-route priced externality* (different intervention, assessed at indexed-summary level).
