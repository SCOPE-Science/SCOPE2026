# Independent mathematical audit

## correctness

PASS

Reconstructed for every n>=3 and t>0. With m=n+1, the Fourier projector has entries (2/m)cos(2π(i−j)/m); the complementary projector on H has diagonal (n−2)/m. Thus the displayed normalization is the common vertex norm, affine independence follows from invertibility, and the barycenter is zero. For the centered regular simplex S, S°=−mS, as the opposite facet of v_j has equation ⟨x,−v_j⟩=1/m. Linear covariance of polarity gives (T_t S/N_t)°=−m N_t T_{1/t} S. The normal norm before normalization is N_{1/t}, so h_t=1/(mN_tN_{1/t}); the facet normals sum to zero, so no shift can increase the common inball radius. This gives the signed reciprocal identity and equal inradii. The undeformed edge Gram is I+11ᵀ with determinant m, while det T_t=t^(n−2). For s=t² and a=n−2 the volume ratio is s^((n−4)/2)((2s+a)/(2+as))^(n/2); combining logarithmic derivatives uses (2s+a)(2+as)−n²s=2a(s−1)². Its derivative has strict sign off s=1 except at n=4; R(1)=1 and the leading coefficient at zero is (a/2)^(n/2). In dimension four, j↦2j mod 5 exchanges the two real Fourier planes, so conjugating (P+sQ)/N_t² swaps the weights to those of the reciprocal Gram matrix. Gram equality supplies the required Euclidean isometry; outside dimension four unequal volumes preclude it even for t>1 by reciprocity. Replay: RESULT.md, sections on facets, ratio and the n=4 permutation, with the preceding exact identities; check.py was inspected, not executed. Its direct reciprocal-array equality is by construction and its Gram/determinant sampling is supportive only.

## originality

PASS

Best of the inspected evidence for the combined family-specific congruence and volume threshold. The scaled-polar identity is immediate from the published normals (or linear polarity of the regular simplex), and the tetrahedral comparison overlaps the older fixed-radii endpoint classification. Neither is counted as a separate original contribution. The exact n=4 permutation criterion and sharp signed volume law across dimensions are the surviving comparison, not just the observation that reciprocal parameters have equal radii.

## value

PASS

The canonical deformation already has fixed concentric radii across a polar pair; it is natural to ask if polarity preserves its metric shape. The result answers that question completely for this family and identifies the unique dimension where a Fourier permutation actually implements it. The strict comparison and reciprocal-volume power law show how differently two equal-radii members can degenerate; this is stronger than producing a single noncongruent example. There is no general assertion about all bicentric simplices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
