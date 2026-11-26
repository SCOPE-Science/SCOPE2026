# A sharp two-reversal law for single-peaked four-class filtration

## Finding

Consider independent positive exponential attenuation of particle-size classes, and track the number-weighted mean size of particles remaining mobile at depth. Three or fewer distinct attenuation-rate groups can create **at most one strict interior reversal** in that mean. With four ordered size classes and a **single-peaked** size-dependent attenuation profile, exactly two reversals are possible. More specifically, for any positive initial counts and strictly ordered class scores, if the rates satisfy

\[
0<\lambda_1<\lambda_4<\lambda_2<\lambda_3,
\qquad \lambda_1+\lambda_3\le\lambda_2+\lambda_4,
\]

then the mean has at most **two** strict interior turning points, counted as distinct derivative zeros. The bound is sharp even under the strict version of the rate-sum condition: the four-size model with scores \((1,2,3,4)\), initial counts \((1,100,100,25)\), and rates \((1,4,5,3)\) has exactly two simple turning points, an initial local minimum and a later local maximum. Each class abundance nevertheless decreases strictly with depth. The two-turn behavior persists under small perturbations of all positive scores, weights, and rates.

Thus a double reversal in this model requires at least four distinct attenuation rates and an ordering of retention coefficients that is not monotone in particle size. This is a model-complexity diagnostic, not evidence that such double reversals occur in any particular observed riverbed.

## Assumptions and scope

For any integer \(n\ge1\), let the ordered numerical size scores be \(s_1<\cdots<s_n\) (strictly positive if interpreted as physical sizes), initial abundances \(w_i>0\), and constant positive filter coefficients \(\lambda_i>0\). All are fixed independent of depth \(t\ge0\), measured in compatible reciprocal-depth units. The number of particles of class \(i\) transmitted to depth \(t\) is modeled as

\[
N_i(t)=w_i e^{-\lambda_i t},\qquad
M(t)=\frac{\sum_{i=1}^n s_i N_i(t)}{\sum_{i=1}^n N_i(t)}.
\]

There is no mixing between classes, new particle supply, aggregation, fragmentation, remobilization, depth-varying filtration, or measurement error. Mean sizes refer to the *transmitted/surviving* particles, not to the size distribution of particles already immobilized in the bed. Distinct classes can share a rate; if so they may be aggregated by that rate into an effective score. A strict reversal is an interior local maximum or minimum of \(M\), not a flat interval.

The four-class rate constraint is a one-peaked ordering: filtration increases across the first three size bins and falls for the fourth; the extra rate-sum inequality specifies an open, physically interpretable relative-gap subfamily when strict. The numerical example is hypothetical and dimensionless, not fitted to any experiment. All conclusions concern the mathematical model and the specified ranges of parameters.

## Proof

**1. Pairwise derivative identity.** Put \(B(t)=\sum_i w_i e^{-\lambda_i t}>0\). Direct quotient differentiation and collection of the \((i,j)\) and \((j,i)\) terms give

\[
B(t)^2 M'(t)
=\sum_{1\le i<j\le n}
 w_iw_j(s_j-s_i)(\lambda_i-\lambda_j)
 e^{-(\lambda_i+\lambda_j)t}.
\tag{1}
\]

In particular, when the \(\lambda_i\) are all nondecreasing or all nonincreasing in size, every nonzero summand in (1) has the same sign. The mean then has no strict interior turning point. Also every \(N_i'(t)=-\lambda_iN_i(t)<0\).

**2. An elementary zero-count lemma.** A nonzero generalized polynomial \(G(y)=\sum_{j=1}^m a_jy^{\nu_j}\) on \(y>0\), with strictly increasing real exponents \(\nu_j\) and nonzero real coefficients \(a_j\), has at most as many positive zeros, counting multiplicity, as the sign changes in the ordered coefficient list. One proof is induction on \(m\). Divide by \(y^{\nu_1}\), differentiate, and multiply the derivative by a positive power of \(y\). The derivative is a generalized polynomial with the signs \((a_2,\ldots,a_m)\). Rolle's theorem gives one more zero in the original than in that derivative at most. If \(a_1\) and \(a_2\) have opposite signs this is precisely the one extra allowed sign change. If their signs agree, the normalized polynomial initially moves away from zero, so any positive zero requires an additional derivative zero before the first zero; there is no extra allowance. Multiple zeros follow by the same multiplicity-counting Rolle argument. The base case is immediate. The lemma is a classical exponential variation-diminishing principle; only this elementary consequence is used here.

**3. Three-rate obstruction and its sharpness.** For three ordered scores with distinct rates, sort the three pair-sum exponents in (1) increasingly. The six possible strict orders of the three rates produce coefficient-sign sequences

\[
---,\quad --+,\quad +--,\quad ++-,\quad -++,\quad +++.
\]

Each has at most one sign change, hence (1) has at most one positive zero, even if the initial weights and scores are arbitrary positive numbers. If two rates coincide, merge their positive abundances into one effective-rate class with a fixed weighted mean score; this reduces to a two-rate model, whose mean is monotone. The same argument applies when \(n\le2\). One reversal is achievable with three rates: for \(s=(1,2,3)\), \(w=(1,1,1)\), and \(\lambda=(3,1,2)\), the derivative numerator is

\[
-e^{-3t}+2e^{-4t}+2e^{-5t};
\]

it starts positive and is eventually negative, with exactly one zero. Consequently **two** strict reversals require at least four distinct rates, regardless of how many classes share each rate.

**4. A uniform four-class bound under one-peaked rates.** Assume
\(\lambda_1<\lambda_4<\lambda_2<\lambda_3\) and
\(\lambda_1+\lambda_3\le\lambda_2+\lambda_4\).
The six pairs in (1), ordered by increasing rate-sum exponent, have signs

\[
(1,4):-\,,\ (1,2):-\,,\ (1,3):-\,,\
(2,4):+\,,\ (3,4):+\,,\ (2,3):-.
\]

The sequence has exactly two sign changes. If equality occurs between the third and fourth exponents, combine their coefficients; that cannot increase sign changes. The zero-count lemma therefore bounds the number of positive roots of the derivative numerator by two, and hence bounds the number of distinct interior extrema of \(M\) by two for **every** positive weight vector and ordered size-score vector in this rate family.

**5. Exact attaining witness.** Set

\[
(s_1,s_2,s_3,s_4)=(1,2,3,4),\quad
(w_1,w_2,w_3,w_4)=(1,100,100,25),\quad
(\lambda_1,\lambda_2,\lambda_3,\lambda_4)=(1,4,5,3).
\]

The strict rate-sum inequality holds: \(\lambda_1+\lambda_3=6<7=\lambda_2+\lambda_4\). Equation (1) becomes

\[
B(t)^2 M'(t)
=-150e^{-4t}-300e^{-5t}-800e^{-6t}
+5000e^{-7t}+5000e^{-8t}-10000e^{-9t}.
\]

With \(y=e^{-t}\), this factors as

\[
B(t)^2 M'(t)=50y^4Q(y),\qquad
Q(y)=-3-6y-16y^2+100y^3+100y^4-200y^5.
\]

The **exact** signs are \(Q(1)=-25\), \(Q(1/2)=5/2\), and \(Q(1/4)=-479/128\). The coefficient list of \(Q\), read in ascending powers, is \((-,-,-,+,+,-)\), with two changes. By the zero-count lemma the polynomial has at most two positive roots. The exhibited sign changes force one simple root in \((1/2,1)\) and one simple root in \((1/4,1/2)\), with no other positive roots. Therefore \(M\) first decreases to a **strict local minimum** and then increases to a **strict local maximum** before decreasing again. Numerically the two depths are approximately \(0.112320762150\) and \(0.836434884704\), with mean scores approximately \(2.657919153782\) and \(2.686442011997\), respectively; the proof of their existence and uniqueness is exact, not numerical.

The derivative numerator has strict signs at \(t=0\), \(t=\log 2\), and \(t=\log 4\). These finite-depth sign inequalities persist under all sufficiently small simultaneous perturbations of the scores, counts and rates (preserving the ordered-size and positive-rate hypotheses). By continuity and the intermediate value theorem, the existence of two distinct strict changes in derivative sign is stable on a nonempty open parameter neighborhood.

## Verification

Run `python3 CHECK.py` using the Python 3 standard library. The checker independently reconstructs the six pair coefficients, uses exact rational arithmetic to verify the three decisive values of \(Q\), checks the six three-rate permutations, tests pair-sign patterns for 3,000 additional admissible four-class parameter sets, and bisects the two proven-unique roots to reproduce the displayed descriptive numbers. The analytic proof, not the finite checks, establishes uniformity over positive parameters and uniqueness of the two roots.

## Relationship to prior work

Munz et al. (2024) derive and experimentally fit class-specific exponential depth attenuation for microplastic fragments, making this model form and the question of compositional size changes natural; their homogeneous-column experiments generally found **monotonically increasing** filtration coefficients with particle size, and do not claim the nonmonotone profile or a two-turn mean-size phenomenon of this theorem. Boos et al. (2024) experimentally investigate size-dependent hyporheic microplastic infiltration and multiple retention mechanisms; their three-size experimental evidence is not a theorem about the present four-class exponential model. The derivative zero-count technique is a standard generalized Descartes/variation-diminishing idea and is not itself claimed as new.

A related mathematical result on **four latent mortality classes and two reversals of relative hazard rankings** gives a wider unconstrained exponential-mixture analogy. It motivates care in interpreting the four-class lower bound as novel by itself: the distinguishing claim here is the **universal two-turn upper bound under a specified single-peaked size-rate ordering and pair-sum gap condition**, together with an exact strictly admissible four-class filtration witness and open-set persistence. Neither the experimental results nor that broader hazard-ranking statement, as available for comparison, assert this constrained ordered-size classification. Priority for all mathematically equivalent formulations remains provisional.

## Limitations

The model assumes a single stationary filtration environment with independent class-specific exponential attenuation and no feedback. Real sediment-size profiles reflect material chemistry, particle shape and density, aggregation, sediment heterogeneity, remobilization, transport pathways, and sampling error. The reported witness does not fit actual retention data, and these experiments do not demonstrate its nonmonotone filtration-rate order. Two observed size reversals need not imply four physical populations unless the model assumptions are independently supported. The result asserts no general bound on turning points for arbitrary four-rate orderings outside its specified class, no stability against measurement noise, and no ecological health or remediation prediction. This is a mathematical statement with self-review only, not independent validation.

## References

1. M. Munz, C. Loui, D. Postler, M. Pittroff, and S. E. Oswald (2024), *Transport and retention of micro-polystyrene in coarse riverbed sediments: effects of flow velocity, particle and sediment sizes*, Microplastics and Nanoplastics 4, article 2. First published January 15, 2024. https://doi.org/10.1186/s43591-023-00077-z
2. J.-P. Boos, F. Dichgans, J. H. Fleckenstein, B. S. Gilfedder, and S. Frei (2024), *Assessing the Behavior of Microplastics in Fluvial Systems: Infiltration and Retention Dynamics in Streambed Sediments*, Water Resources Research. First published February 23, 2024. https://doi.org/10.1029/2023WR035532
3. V. P. Kostov and B. Shapiro (2018), *New Aspects of Descartes' Rule of Signs*, an account of classical sign-variation bounds. https://doi.org/10.5772/intechopen.82040
