# Independent mathematical audit

## correctness

PASS

The five affine images give the support rows starting at 1,1,1,2,4,5,…, with expansion uniformly greater than 1 for fixed λ. Closed walks to state 1 are finite at each length since sufficiently high states can descend at most one level per step. With r=(3−√5)/2 and β=2+√5, the tail sum gives Aw=βw for w₁=w₂=w₃=1, wᵢ=2r^(i−3) otherwise: the identity in the tail is βr(1−r)=1, and states 1–3 and 4 supply the two stated finite boundary equations. The Doob transform is irreducible and aperiodic with a strictly negative drift −1+r/(1−r) outside a finite set, proving positive recurrence and return growth β. For either this chain or the acip chain with tail parameter p=r or p=λ<1/2, V(i)=a^i with 1<a<(1−p)/p has a strict multiplicative Foster contraction outside the finite head, since E[V(J)|i]/V(i)=(1−p)/(a(1−pa))<1. Hence the stationary state index has finite mean (indeed a finite exponential moment) and finite one-state entropy. This justifies the entropy-rate/generator step and makes log w integrable for the Doob chain. In stationarity −log Qᵢⱼ=logβ+log wᵢ−log wⱼ averages to logβ, confirming maximal entropy. Affinity preserves conditional cell uniformity given every finite past itinerary for the acip, so the metric entropy is the Shannon entropy of the geometric row. Its derivative and the limits at 0 and 1/2 give the claimed strict gap and infimum. The frozen symbolic/truncation checker was inspected, not run; finite truncations are not a proof of the growth rate.

## originality

FAIL

The original source gives the acip and geometric rows. More decisively, the distinct indexed same-map record 9c2fa9f11f90 gives the exact weighted first-return series to the three-cell base for every λ. Coefficientwise removal of the geometric weights followed by the ordinary first-return renewal identity gives the exact Gurevich growth and positive recurrence. This is demonstrable coverage in the available corpus, not a conclusion that the later-labelled record was publicly available before this frozen record or that one author obtained a proof from the other.

## value

FAIL

The entropy gap is a meaningful comparison on a natural auxiliary system, and the Doob transform is a useful alternative proof. But the exact growth, positive recurrence, and final entropy gap follow directly from the indexed exact first-return law and Ji–Ma’s geometric kernel. Under the criterion for a narrow exact invariant, there is no independently needed unknown invariant left in this record; no stronger genuinely distinct result about the original bimodal map is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
