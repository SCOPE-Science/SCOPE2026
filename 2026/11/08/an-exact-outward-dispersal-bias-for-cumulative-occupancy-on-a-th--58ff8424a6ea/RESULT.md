# An exact outward-dispersal bias for cumulative occupancy on a three-patch path

## Finding

For three habitats in a path, optimizing expected regional extinction time requires balanced inward and outward colonization rates, but optimizing the expected **cumulative occupied patch-time** requires a unique, strictly outward-biased allocation. This distinction holds for every fixed positive rate budget, not just for selected parameters.

Precisely, for every \(S>0\), define \(\tau\) as the first instant when all three habitats are empty and \(H=\int_0^\tau N_t\,dt\), where \(N_t\) is the number of occupied habitats at time \(t\). Among all \(a,b\ge0\) satisfying \(a+b=S\):

1. \(\mathbb E\tau\) is uniquely maximized by \(a=b=S/2\).
2. \(\mathbb EH\) is uniquely maximized by \(a=(S+d_S)/2\) and \(b=(S-d_S)/2\), where \(d_S\) is the unique root in \((0,S)\) of
   \[
   G_S(d)=12d^3-9d^2-(12S^2+50S+72)d+3S^2+4S=0.
   \]
   This root obeys \(0<d_S<\min\{S,1/4\}\), \(\lim_{S\downarrow0}d_S/S=1/18\), and \(\lim_{S\to\infty}d_S=1/4\).

At \(S=2\), the extinction-time optimum is \((a,b)=(1,1)\), whereas the occupied-patch-time optimum is approximately \((1.0453068875,0.9546931125)\). The cumulative expectation rises from \(159/28\) to about \(5.682620766\). The gain is small in this example, but the strict separation and its unique direction are exact across the full parameter range.

## Assumptions and scope

The habitat graph is exactly the undirected three-vertex path \(L-C-R\), but recolonization intensities are directed. Each occupied patch goes empty at independent exponential rate one. If the center is occupied, it sends successful colonization to each empty leaf at independent rate \(a\); each occupied leaf sends successful colonization to an empty center at independent rate \(b\). The center may therefore be recolonized at rate \(2b\) when both leaves are occupied. A colonization does not remove its donor. There is no external immigration and the all-empty state is absorbing. The initial state is all occupied. Both boundary cases \(a=0\) and \(b=0\) are allowed; every \(a+b=S>0\) has almost-sure finite absorption.

The fixed budget constrains the sum of the *two per-direction per-edge intensities*, not the total instantaneous traffic or the sum across all directed edges. Time is normalized by the individual extinction rate. No species abundance, habitat quality, spatial geometry, time-varying environment, or demographic inference is asserted.

## Proof

Write \(E(a,b)=\mathbb E\tau\) and \(Z(a,b)=\mathbb EH\). Index the seven nonempty configurations by their binary occupancy masks \(1,\dots,7\), with the center represented by bit \(2\). Let \(Q\) be the transient loss-rate matrix: for each allowed non-absorbing transition \(x\to y\) of rate \(r\), set \(Q_{xy}=-r\) and add \(r\) to \(Q_{xx}\); for transitions to all-empty, add the rate only to the diagonal. Thus \(Q=-G\) where \(G\) is the subgenerator. Since local extinction can consecutively empty all remaining occupied patches with positive probability, absorption occurs almost surely, and the finite-state transient inverse exists. The standard first-step equations are \(Qe=\mathbf 1\) and \(Qz=(|x|)_{x=1}^{7}\). Their entries at mask \(7\) give the respective expectations.

Direct exact elimination gives
\[
E(a,b)=\frac{4a^2b^2+10a^2b+10ab^2+10a^2+10b^2+37ab+31a+31b+22}{2(a+b+2)(2a+2b+3)}
\]
and
\[
Z(a,b)=\frac{6a^2b^2+14a^2b+11ab^2+10a^2+9b^2+37ab+27a+27b+18}{(a+b+2)(2a+2b+3)}.
\]
The accompanying verifier constructs \(Q\) directly from state transitions and reproduces both rational expressions symbolically, in addition to checking them by an independent rational Gaussian elimination.

Fix \(S=a+b\) and put \(q=ab\). Rewriting the first formula yields
\[
 E(a,b)=\frac{4q^2+(10S+17)q+10S^2+31S+22}{2(S+2)(2S+3)}.
\]
For \(S>0\) this is strictly increasing in \(q\), since its derivative is \((8q+10S+17)/[2(S+2)(2S+3)]>0\). The elementary bound \(q\le S^2/4\), with equality only at \(a=b=S/2\), proves the first assertion, including both boundaries.

For the second objective, subtraction of the rational expressions after swapping the directional rates gives the exact identity
\[
 Z(a,b)-Z(b,a)=\frac{(a-b)(3ab+a+b)}{(a+b+2)(2a+2b+3)}.
\]
Therefore each strict inward-biased allocation \(a<b\) is improved by its swapped outward-biased allocation. Every maximizer must consequently satisfy \(a\ge b\). Set \(d=a-b\in[0,S]\), so \(a=(S+d)/2\) and \(b=(S-d)/2\). Exact differentiation of the second rational expression gives
\[
\frac{d}{dd} Z\!\left(\frac{S+d}{2},\frac{S-d}{2}\right)=\frac{G_S(d)}{8(S+2)(2S+3)},
\]
where the cubic \(G_S\) is displayed in the finding. We have \(G_S(0)=3S^2+4S>0\), \(G_S(S)=-4S(14S+17)<0\), and \(G_S(d)\to+\infty\) as \(d\to+\infty\). The cubic's descending coefficients have signs \(+,-,-,+\), so Descartes' rule admits at most two positive roots counted with multiplicity. The sign changes just noted force one root in \((0,S)\) and one in \((S,\infty)\), and exhaust all positive roots. Thus the derivative is positive up to a unique \(d_S\in(0,S)\) and negative afterward throughout \((d_S,S]\). The maximizer is unique and strictly interior. Moreover \(G_S(1/4)=-(68S+147)/8<0\), so \(d_S<1/4\) for every \(S>0\).

For the limits, set \(d_S=S u_S\). Since \(u_S\in(0,1)\), divide \(G_S(Su_S)=0\) by \(S\) and send \(S\downarrow0\); the surviving identity is \(4-72u_*=0\), yielding \(u_S\to1/18\). Likewise \(0<d_S<1/4\); after dividing \(G_S(d_S)=0\) by \(S^2\) and sending \(S\to\infty\), every convergent subsequence obeys \(3-12d_*=0\), hence \(d_S\to1/4\). This completes both optimizations and all boundary assertions.

## Verification

Run `python verify.py` with SymPy installed. The script constructs the seven-by-seven transient loss-rate matrix from the explicitly described transition rules; solves exact symbolic reward equations; verifies the two displayed rational formulas, the swapped-rate identity, the fixed-budget extinction expression, and the derivative cubic; checks both endpoint signs and the \(1/4\) bound; and independently solves the rational equations using `fractions.Fraction` Gaussian elimination at twenty nonnegative rational rate pairs. All comparisons are exact. The source code is included with the finding as a separate file.

## Relationship to prior work

Day and Possingham (1995) establish a general finite presence–absence transition-matrix framework and give exact extinction and occupancy probabilities. Their model is discrete-time and their reported applications compare patch geometry, quasi-stationary occupancy and removal, rather than an all-budget directional-rate classification for expected integrated patch-time. The general matrix methodology is established prior work, not a novelty claim here.

Vuilleumier and Possingham (2006) investigate asymmetric dispersal in a larger stochastic metapopulation by simulation, using a different time-stepped model and a viability criterion. The entire accessible article, including model specification and discussion, was inspected. Their results motivate a small, exactly soluble directional comparison but neither state nor imply the present fixed-sum occupied-patch-time optimum.

Vuilleumier, Bolker and Lévêque (2010) investigate asymmetries in dispersal strength and topology. The bibliographic record and abstract were available, but the full paper could not be inspected, so precise priority relative to any analytic small-network special cases remains uncertain. Shtilerman and Stone (2015) analyze dispersal-network spectral radii and degree correlations for persistence; the available abstract and substantive sections deal with linearized network-scale persistence criteria, not exact finite absorbing-chain reward allocation.

Self-duality of the finite contact process already explains why the all-occupied extinction-time distribution is invariant under reversing every directed arrow. That classical fact is **not** claimed as new. The focus here is the incompatible fixed-budget optimum for two explicitly distinguished rewards and the unique outward-bias cubic; a two-patch result cannot imply this three-patch cumulative-occupancy optimization.

## Limitations

The theorem is restricted to three equal-extinction-rate patches, donor-preserving Markov recolonization, identical outward rates on both arms, and fixed sum of directional per-edge rates. It does not establish a corresponding theorem for larger stars, other reward weights, or environmental heterogeneity. The optimal cumulative-reward gain is quantitatively modest at some budgets; the result is a sharp qualitative separation of objectives, not a claim of large practical improvement. Historical priority is provisional, especially for the inaccessible 2010 paper and the broader directed-contact-process literature. No empirical policy recommendation or independent mathematical validation is asserted.

## References

- J. R. Day and H. P. Possingham, “A stochastic metapopulation model with variability in patch size and position”, *Theoretical Population Biology* **48** (1995), 333–360. DOI: 10.1006/tpbi.1995.1034.
- S. Vuilleumier and H. P. Possingham, “Does colonization asymmetry matter in metapopulations?”, *Proceedings of the Royal Society B* **273** (2006), 1637–1642. DOI: 10.1098/rspb.2006.3469. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC1634917/ (public article date: 2006-03-29).
- S. Vuilleumier, B. M. Bolker and O. Lévêque, “Effects of colonization asymmetries on metapopulation persistence”, *Theoretical Population Biology* **78** (2010), 225–238. DOI: 10.1016/j.tpb.2010.06.007 (abstract consulted; full text unavailable).
- E. Shtilerman and L. Stone, “The effects of connectivity on metapopulation persistence: network symmetry and degree correlations”, *Proceedings of the Royal Society B* **282** (2015), 20150203. DOI: 10.1098/rspb.2015.0203.
