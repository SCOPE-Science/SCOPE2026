# Universal local VCG revenue fragility, unimodal mean monotonicity, and exact shock laws

## Finding

Consider a Vickrey--Clarke--Groves (VCG) assignment market with two unit-demand bidders and two indivisible objects, nonnegative valuations, no reserves, and Clarke pivot payments. Write the valuation matrix as
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]
and denote total seller revenue by \(R(a,b,c,d)\). Let \(R_t=R(a,b,c,d+t)\) for a unilateral valuation increase \(t\geq0\).

**Distribution-free local sensitivity.** If the two bidder valuation vectors are independent copies of an item-exchangeable distribution on nonnegative pairs, and the within-bidder difference has no atoms, the right derivative exists almost surely and satisfies
\[
\Pr\left(\left.\frac{dR_t}{dt}\right|_{t=0+}=-1\right)=\frac18,\qquad
\Pr\left(\left.\frac{dR_t}{dt}\right|_{t=0+}=+1\right)=\frac18,\qquad
\Pr\left(\left.\frac{dR_t}{dt}\right|_{t=0+}=0\right)=\frac34.
\]
Independence between the two entries of a single bidder's valuation vector is **not** assumed.

**A structural mean-revenue condition.** Under the same distribution-free assumptions, if the common gap density is symmetric and nonincreasing in absolute gap size (symmetric unimodality), then \(\mathbb E[R_t]\) is **nondecreasing for all \(t\geq0\)**. The condition matters: an atomless, symmetric but bimodal gap density can instead have \(\mathbb E[R_1]<\mathbb E[R_0]\). A fully explicit construction is supplied below. Unimodality is sufficient, not asserted to be necessary.

**Exact finite shocks.** If the four values are independent Uniform\((0,1)\), then for every \(t>0\)
\[
\Pr(R_t<R_0)=
\begin{cases}
\dfrac{t^4-6t^2+8t+3}{24},&0<t\leq1,\\[2pt]
\dfrac14,&t\geq1.
\end{cases}
\]
The event has probability zero at \(t=0\); its probability tends to \(1/8\) as \(t\downarrow0\). The expected **positive revenue loss** is
\[
\mathbb E[(R_0-R_t)_+]=
\begin{cases}
\dfrac{t(t^4-10t+15)}{120},&0\leq t\leq1,\\[2pt]
\dfrac1{20},&t\geq1.
\end{cases}
\]
Nevertheless, expected total revenue increases strictly for every \(t>0\):
\[
\mathbb E[R_t-R_0]=
\begin{cases}
\dfrac{t^2(20-20t+10t^2-3t^3)}{120},&0\leq t\leq1,\\[3pt]
\dfrac{8-(2-t)^5}{120},&1\leq t\leq2,\\[3pt]
\dfrac1{15},&t\geq2.
\end{cases}
\]
At baseline \(\mathbb E[R_0]=1/10\). Hence the market exhibits a precise distinction between **ex-post** revenue nonmonotonicity (up to a quarter of profiles) and **ex-ante** improvement in expected revenue under a positive value shift.

## Assumptions and scope

The allocation is a maximum-weight matching with at most one good per bidder and at most one bidder per good. Both goods may be left unassigned if their values are zero. All valuations are nonnegative and monetary transfers use standard VCG externality (Clarke pivot) payments. Every deterministic tie choice produces the same total revenue. No strategic misreporting or bidder response is modeled: the comparison changes one true valuation coordinate and recomputes the mechanism.

For the distribution-free assertion, the two row vectors are independent and identically distributed, their joint row law is invariant under swapping the two goods, and \(a-b\) has an atomless law. Within-row dependence is allowed. For the finite-shock formulas only, the four matrix entries are iid Uniform\((0,1)\), with the additive increase untruncated (so \(d+t\) need not lie in \((0,1)\)). The probabilities and expectations are over the *initial* valuation matrix. Every \(t\) is deterministic.

## Proof

**1. VCG identity.** Removing bidder one leaves best achievable welfare \(\max(c,d)\), and removing bidder two leaves \(\max(a,b)\). With both present and nonnegative valuations, welfare is
\[
W=\max(a+d,b+c).
\]
If bidder values in an optimal allocation are \(w_1,w_2\), Clarke payments are \(p_1=\max(c,d)-w_2\) and \(p_2=\max(a,b)-w_1\). Since \(w_1+w_2=W\),
\[
R=\max(a,b)+\max(c,d)-\max(a+d,b+c).
\]
Define signed within-bidder gaps \(S=a-b\) and \(T=c-d\). After cancelling \(b+d\),
\[
R=\max(S,0)+\max(T,0)-\max(S,T)=
\begin{cases}
\min(|S|,|T|),&ST>0,\\
0,&ST\leq0.
\end{cases}
\tag{1}
\]
Increasing \(d\) by \(t\) replaces \(T\) with \(T-t\). This holds on all tie boundaries, too.

**2. Local law.** Almost surely \(S,T\) are independent identically distributed continuous random variables, each symmetric about zero. From (1), the revenue derivative at zero is \(-1\) exactly when \(S>T>0\), \(+1\) exactly when \(S<T<0\), and zero in every other strict ordering regime. The two sign-positive probabilities each equal \(1/4\); conditional on both being positive, each strict ordering has probability \(1/2\). The same reasoning applies to both-negative gaps, proving \(1/8,1/8,3/4\).

**3. Finite decline event.** Formula (1) implies, for every \(t>0\),
\[
R_t<R_0\quad\Longleftrightarrow\quad S>0,\ T>0,\ T-S<t.
\tag{2}
\]
Indeed only the positive-positive quadrant can lose revenue; there it is \(\min(S,T)\) before and \(\min(S,(T-t)_+)\) afterward. In the uniform model the independent differences have triangular density \(f(z)=1-|z|\) on \([-1,1]\). For \(0<t\leq1\), the complementary region within the positive-positive quadrant has mass
\[
\int_0^{1-t}(1-s)\int_{s+t}^1(1-u)\,du\,ds
=\frac{(1-t)^3(t+3)}{24}.
\]
Subtracting from the quadrant mass \(1/4\) gives \((t^4-6t^2+8t+3)/24\). For \(t\geq1\), every positive-positive gap pair satisfies (2) except a null boundary, proving \(1/4\).

**4. Loss and gain integrals.** Let \(L(t)=\mathbb E[(R_0-R_t)_+]\) and \(G(t)=\mathbb E[(R_t-R_0)_+]\). The loss comes only from \(S,T>0\); differentiating its bounded piecewise linear integrand under the integral gives
\[
L'(t)=\int_t^1(1-u)\int_{u-t}^1(1-s)\,ds\,du
=\frac{(1-t)^2(t^2+2t+3)}{24}
\quad (0<t<1),
\]
and \(L'(t)=0\) for \(t>1\). With \(L(0)=0\), integration gives the stated loss formula.

Positive gains occur precisely when \(S<0\), \(T<t\), and \(t-T<-S\). Put \(u=-S\), with density \(1-u\) for \(0<u<1\), and let \(F\) denote the CDF of \(T\). Then
\[
G'(t)=\int_0^1(1-u)\bigl[F(t)-F(t-u)\bigr]\,du,
\tag{3}
\]
where \(F(z)=0\) for \(z\leq-1\), \(F(z)=\tfrac12+z+\tfrac12z^2\) for \(-1<z<0\), \(F(z)=\tfrac12+z-\tfrac12z^2\) for \(0\leq z<1\), and \(F(z)=1\) for \(z\geq1\). Splitting (3) at \(u=t\) when \(0<t<1\), and at \(u=t-1\) when \(1<t<2\), yields
\[
G'(t)=
\begin{cases}
\dfrac{-2t^4+8t^3-12t^2+4t+3}{24},&0<t<1,\\[3pt]
\dfrac{(2-t)^4}{24},&1<t<2,\\[3pt]
0,&t>2.
\end{cases}
\]
Integration from \(G(0)=0\), matching endpoints, gives
\[
G(t)=
\begin{cases}
\dfrac{t(-2t^4+10t^3-20t^2+10t+15)}{120},&0\leq t\leq1,\\[3pt]
\dfrac{14-(2-t)^5}{120},&1\leq t\leq2,\\[3pt]
\dfrac7{60},&t\geq2.
\end{cases}
\]
Since \(\mathbb E[R_t-R_0]=G(t)-L(t)\), subtraction proves the expected-change formula. Its first piece is positive for \(0<t\leq1\), because the polynomial \(20-20t+10t^2-3t^3\) decreases from \(20\) to \(7\) on that interval; the other pieces are manifestly positive. Finally, symmetry and the survival integral give
\[
\mathbb E[R_0]=2\int_0^1\left(\frac{(1-u)^2}{2}\right)^2du=\frac1{10}.
\]
**5. Unimodal expected-revenue monotonicity and its limitation.** Let \(f\) be the common symmetric density of the independent gaps \(S,T\), and suppose \(f\) is nonincreasing on \([0,\infty)\). Pair the contributions from \(S=s\) and \(S=-s\) in (1). For every \(t\geq0\),
\[
\mathbb E[R_t]=\int_0^\infty f(s)\,\mathbb E_T[\min(s,|T-t|)]\,ds.
\tag{4}
\]
For any \(z>0\), the moving-window probability \(H_z(t)=\Pr(|T-t|<z)\) is nonincreasing in \(t\geq0\), because, wherever derivatives exist,
\[
H_z'(t)=f(t+z)-f(t-z)\leq0.
\]
The inequality uses evenness and unimodality, since \(|t+z|\geq|t-z|\); integration gives the same conclusion without smoothness. Hence \(|T-t|\) is stochastically nondecreasing in \(t\). Since \(x\mapsto\min(s,x)\) is nondecreasing for each \(s\geq0\), equation (4) proves the claimed nondecreasing expectation. The uniform-gap triangular density is strictly decreasing on its positive support, giving the strict finite-shock improvement already quantified.

For an atomless counterexample without unimodality, take independent symmetric signs \(E_1,E_2\in\{-1,+1\}\) and independent \(U_1,U_2\) uniform on \([-1/100,1/100]\). Put \(S=E_1+U_1\), \(T=E_2+U_2\), and realize them with positive bidder valuations \(a=1+S/2\), \(b=1-S/2\), \(c=1+T/2\), \(d=1-T/2\). Each row law is item-exchangeable, the row gaps are independent and atomless, and their density has two separated peaks. In the zero-noise reference \(U_1=U_2=0\), formula (1) gives \(\mathbb E[R_0]=1/2\) but \(\mathbb E[R_1]=1/4\). Formula (1), equivalently the difference of two maxima of affine functions, is \(1\)-Lipschitz separately in each of \(S,T\). Perturbing both gaps by at most \(1/100\) changes either revenue expectation by at most \(2/100\). Thus for the atomless construction
\[
\mathbb E[R_1-R_0]\leq-\frac14+\frac4{100}=-\frac{21}{100}<0.
\]
This establishes genuine failure of ex-ante monotonicity when the unimodality assumption is dropped, without changing any independence, exchangeability, or atomlessness assumptions of the local law.

All claimed boundaries are now established.

## Verification

Run `python3 checker.py` with SymPy installed in the directory containing this document. The checker evaluates the independent allocation/externality implementation against (1) for all \(6^4\) valuation matrices over \(\{0,1,2,3,4,5\}\) and six shocks (7,776 cases), verifies nine symbolic integral/polynomial identities, performs 700,000 seeded Monte Carlo comparisons of the uniform shock laws, and checks the exact two-peak baseline plus 120,000 samples of its atomless perturbation. Exact enumeration and Monte Carlo are checks only; the continuous distribution claims, unimodality result and all shock-size statements rest on the analytic proof in Sections 1--5.

## Relationship to prior work

Hartline (2026, arXiv:2602.20439v1) exhibits revenue nonmonotonicity of VCG in the same two-bidder, two-good matching environment and explains its relation to minimum Walrasian prices. That counterexample establishes possibility, not the distribution-free one-sided derivative incidence or the unimodal mean-revenue theorem, its continuous bimodal counterexample, or the entire finite-shock probability and expectation curves proved here. The gross-substitutes/Walrasian-price framework of Gul and Stacchetti (1999) is foundational context, but the present result concerns quantitative valuation-distribution comparative statics rather than existence and characterization of equilibrium prices. The exact constants and polynomial functions reported here were not located in the accessible sources examined; absence from search results is not a proof of publication priority.

## Limitations

This concerns exactly two bidders and two objects under no-reserve VCG, not more general assignment markets, reserve prices, or alternative Walrasian price selections. The distribution-free local law needs independent, identically distributed, item-exchangeable row vectors with atomless differences. The unimodality condition is sufficient for expected-revenue monotonicity, not proved necessary; an explicit atomless bimodal counterexample shows that the analogous unconditional statement is false. The finite-shock polynomials need four independent uniform initial values and an untruncated additive change. No claims of distribution-free finite-shock probabilities, bidder incentives, strategic manipulation, or economic optimality of the revenue change are made. Independent mathematical audit and a comprehensive publication-priority investigation have not been performed.

## References

1. J. Hartline, "Revenue Non-monotonicity in Matching Markets," arXiv:2602.20439v1, first posted 2026-02-24. https://arxiv.org/html/2602.20439
2. F. Gul and E. Stacchetti, "Walrasian Equilibrium with Gross Substitutes," *Journal of Economic Theory* **87** (1999), 95--124. https://doi.org/10.1006/jeth.1999.2531
3. B. Rastegari, A. Condon, and K. Leyton-Brown, "Revenue monotonicity in combinatorial auctions," *Artificial Intelligence* (2007). https://eprints.soton.ac.uk/426396/
