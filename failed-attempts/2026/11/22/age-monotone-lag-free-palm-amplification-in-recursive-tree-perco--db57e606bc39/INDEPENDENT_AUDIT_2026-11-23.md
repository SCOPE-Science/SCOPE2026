# Independent mathematical audit

## correctness

PASS

In the stipulated tree growth, a vertex born at m+1 succeeds exactly when it chooses one of the S_m members and retains its edge, so its conditional success probability is pS_m/m. This gives the mean product and the martingale S_m/A_m. Applying the same transition to s(s+1), whose unit increment is 2(s+1), gives E[S_m(S_m+1)]=2B_m. At birth j, E[I_j S_j]=p E[S_{j−1}(S_{j−1}+1)]/(j−1); dividing by P(I_j=1)=pA_{j−1}/(j−1) gives the stated ratio at j. Conditioning the martingale on this event preserves the ratio at all m≥j, and applying the next-birth transition gives it at every k>j. This also proves the joint marginal formula. Direct product cancellation gives R₂=2/(1+p)>1 and R_{j+1}/R_j=1+p(1−p)/((j−1+p)(j+p))>1; gamma-ratio asymptotics give the stated finite limit. The exclusion of p=0 matters for conditioning, and p=1 would remove strictness.

## originality

FAIL

The displayed marked statement was not found printed verbatim, but its exact ratio is a direct finite difference of the already published exact first and second root-size moments in this same process. Writing D_j=E[S_j²], the pointwise identity 2 I_j S_j=S_j²−S_{j−1}²+I_j implies R_j=(D_j−D_{j−1}+A_j−A_{j−1})/[2(A_j−A_{j−1})A_j]. Kürsten's Eqs. (13), (44) reduce this mechanically to (B_j−B_{j−1})/[(A_j−A_{j−1})A_j]. The prior Hoppe/Simon transition makes S_m/A_m a martingale and gives the unconditional birth intensity, so the same number applies to future expected size and to any later birth probability. The age order, positivity and limit are direct arithmetic of these known products, not further independent properties needed to obtain the exact result. This is a finding of prior implication, not an allegation that the frozen formula is false or that a cited paper explicitly states it.

## value

FAIL

Birth-conditioned correlation is a natural observable and the interpretation is useful, but this record's narrow exact invariant is mechanically determined by known moments and one-step linear regression. The age comparison adds just cancellation in the resulting products; the work neither closes an independent exact-moment gap nor establishes a higher-order conditional law that would require new information about the process.

The dated certificate retains the supplied scientific assessment, sources and limitations.
