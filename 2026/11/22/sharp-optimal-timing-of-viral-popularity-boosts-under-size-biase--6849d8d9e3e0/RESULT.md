# Sharp optimal timing of viral popularity boosts under size-biased attention

## Finding

For a finite social-exposure population, fixed **amounts** of publicity do not determine final expected exposure concentration: the **order** of publicity shocks matters. Among every ordering of the same positive reinforcement amounts, smallest-first uniquely minimizes expected concentration and largest-first uniquely maximizes it, with ties only from exchanging equal boosts.

Formally let \(H_T=\sum_{i=1}^N p_i(T)^2\), where \(p_i(T)\) is user \(i\)'s fraction of total popularity after \(T\) events. Then for the increasingly sorted and decreasingly sorted boost lists,
\[
\mathbb E H_T^{\uparrow}\le \mathbb E H_T^{\pi}\le \mathbb E H_T^{\downarrow},
\]
with strict inequalities whenever the compared boost-order class is distinct and at least two boost sizes differ.

## Assumptions and scope

Fix \(N\ge2\) and strictly positive real initial popularity scores \(P_i(0)>0\). A prescribed sequence of \(T\ge1\) strictly positive real boost sizes \(r_1,\ldots,r_T\) is executed one at a time. At each event, a recipient is drawn **from all \(N\) users, including the current focal user if applicable**, according to the current size-biased probabilities \(p_i=P_i/S\), where \(S=\sum_iP_i\). Exactly the drawn user's score increases by the prescribed boost; all others are unchanged. Conditional draws follow the refreshed weights after each event. The list of boosts is fixed externally, not adaptively selected from observed winners.

This is the precisely defined serialized popularity-reinforcement component of a social-media explore-layer mechanism. It does not include opinion updates, active-user restrictions, friendship edges, or simultaneous multiuser events of the full motivating model. It permits an ordinary exposure increment of \(1\) and a viral event with increment \(M>1\), but also arbitrary positive predetermined increments.

Define exposure diversity \(D=1-H\). Since initial weights are strictly positive and \(N\ge2\), \(D_0>0\).

## Proof

**Conditional diversity factor.** At total popularity \(S\) and boost \(r>0\), draw index \(I\) with probability \(P_I/S\), then update \(P_I\mapsto P_I+r\). Squaring and averaging gives
\[
\mathbb E[H'\mid(P_i)]=\frac{S(S+2r)H+r^2}{(S+r)^2},\qquad
\mathbb E[D'\mid(P_i)]=D\,f(S,r),\quad
f(S,r)=\frac{S(S+2r)}{(S+r)^2}.
\]
The total \(S\) is deterministic for any prescribed sequence, regardless of which users were chosen. Thus, for \(S_k=S_0+\sum_{j<k}r_j\),
\[
\mathbb E D_T=D_0\prod_{k=1}^{T}f(S_k,r_k).
\]

**Adjacent-swap identity.** Compare adjacent boosts \(a>b>0\) at the same preceding total \(S>0\). Direct rational simplification yields
\[
 f(S,b)f(S+b,a)-f(S,a)f(S+a,b)
 =\frac{2Sab(a-b)}{(S+a)(S+b)(S+a+b)^2}>0.
\]
The deterministic total after the pair is \(S+a+b\); consequently, all earlier and later multipliers are identical for the two orders and strictly positive. Swapping a decreasing adjacent pair to increasing order strictly raises expected diversity and strictly lowers expected concentration. Repeated adjacent swaps sort an arbitrary permutation increasingly, proving the global minimum; reverse swaps give the maximum. Equality is possible only when each inversion exchanged has equal increments, proving uniqueness up to tied boost sizes. This argument holds for every positive initial score vector, not only a uniform one.

**An exact two-user example.** Starting from \((P_1,P_2)=(1,1)\), the ordinary-first sequence \((1,3)\) yields \(\mathbb E H_2=2/3\). Reversing the same publicity budget to \((3,1)\) yields \(\mathbb E H_2=31/45\), an exact extra concentration of \(1/45\).

## Verification

The standalone `verify.py` derives and checks the adjacent-swap identity symbolically; enumerates the exact Markov distribution over score vectors for 21 small cases; exhaustively checks scheduling optima across 12 multisets; and reproduces both rational example values. It also checks the optional infinite-periodic limit below by high-precision Gamma functions.

For the periodic schedule \((1,M),(1,M),\ldots\) with equal initial scores \(P_i(0)=1\), the same product method and martingale convergence give, for \(L=M+1\),
\[
\mathbb E D_\infty=\frac{N-1}{N}
\frac{\Gamma((N+1)/L)\Gamma(1+N/L)^2}
{\Gamma(N/L)\Gamma((N+2)/L)\Gamma(2+(N-1)/L)}.
\]
At \(M=1\), this is \((N-1)/(N+1)\); for fixed \(N\), as \(M\to\infty\) it is asymptotic to \((N-1)(N+2)/[(N+1)M]\). These expressions are auxiliary consequences, **not** a stochastic polarization theorem. The Gamma expression is obtained by multiplying \(S_k(S_k+2)(S_k+2M+1)/[(S_k+1)(S_k+M+1)^2]\) for \(S_k=N+kL\). Since each \(p_i(t)\) is a bounded martingale, it converges almost surely; dominated convergence justifies passing to expected limiting diversity.

## Relationship to prior work

De Bruyn and Correa Rocha (2026) introduce popularity-weighted explore-layer selection with unit ordinary increments and occasional large viral increments and study its qualitative influence on opinion diversity. Their inspected model and results do not give an optimization theorem comparing arbitrary temporal permutations of an unchanged multiset of publicity boosts. Pemantle (2007, Section 3.2, citing 1990 work) already treats general time-dependent two-color Pólya reinforcement and records the existence of an exact variance recurrence. The moment recurrence and bounded-martingale mechanism here are **not** claimed as novel. The specific strict all-permutation optimizer, its positive adjacent-swap gap, and its exposure-scheduling interpretation are the assessed contribution. Ruszel and Thacker (2024) treat a distinct nonlinear generalized time-dependent urn using many independently reinforced balls; their main results concern fixation/dominance, not this chronological ordering for one size-biased recipient per event.

## Limitations

This theorem optimizes only expected normalized popularity concentration for **fixed externally prescribed event sizes**. It does not optimize opinion-cluster counts, empirical virality, expected number of unique exposed users, or a particular platform objective. If recipient sets are restricted, draws are not refreshed between events, or viral sizes respond adaptively to observed winners, the proof no longer applies directly. The general moment recursion is established earlier in the reinforcement literature; historical priority for the exact scheduling comparison requires independent review.

## References

- S. De Bruyn and L. E. Correa Rocha, *Popularity-driven interactions in multilayer bounded-confidence opinion dynamics*, arXiv:2610.21610, first public October 15, 2026. https://arxiv.org/abs/2610.21610
- R. Pemantle, *A survey of random processes with reinforcement*, *Probability Surveys* 4 (2007), Section 3.2. https://doi.org/10.1214/07-PS094
- R. Pemantle, *A time-dependent version of Pólya's urn*, *Journal of Theoretical Probability* 3 (1990), 627–637.
- W. M. Ruszel and D. Thacker, *Positive Reinforced Generalized Time-Dependent Pólya Urns via Stochastic Approximation*, *Journal of Theoretical Probability* 37 (2024), 2859–2885. https://doi.org/10.1007/s10959-024-01366-w
