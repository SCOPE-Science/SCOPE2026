# Independent mathematical audit

## correctness

PASS

The twisting relation in the maximal-rank normal form forces Y=[A C; 0 zeta A], with A²=0 and AC+zeta CA=0. If A has rank j, choose U=im A and a complementary j-space T mapping isomorphically onto U, and an h=r-2j dimensional homology summand H. The equation forces C[T,U], C[T,H] and C[H,U] to vanish and C[T,T]=-zeta C[U,U]. The remaining blocks apart from C[H,H] give 2j²+2jh independent field coordinates. Projecting im Y to the lower block gives dimension j and kernel of dimension dim(im A + C(ker A))=j+rank(C[H,H]); thus rank Y=2j+rank(C[H,H]). Counting image, kernel and induced isomorphism proves each Gaussian factor, also the prefactor for varying X. The reasoning needs only zeta invertible, so includes characteristic two, r=1, zero rank and extension fields. Independently enumerated eight bounded cases with /workspace/branches/bb6cd006-848a-4453-b0da-c8c11ea5dd3c/count_check.py; for r=2 the F3 and F4 counts were (1,32,120) and (1,75,420) for every nonzero twist. The supplied verifier was inspected, not executed. These finite cases corroborate the proof, not its full quantifier.

## originality

FAIL

A prior Resultary theorem gives the stronger joint (rank XY, rank Y) census at zeta=-1. Its proof and joint formula extend to every nonzero twist by a direct invertible change of coordinates on each known reduced block; even rank XY as well as rank Y is preserved. Marginalization and multiplying by the usual labelled-X count then give the entire frozen finding. This is prior coverage by a rank-preserving equivalence, not a claim that the earlier record explicitly states all twists.

## value

FAIL

The underlying joint rank census is a meaningful natural invariant, but the frozen marginal counts less information and transfers to other twists by one block scaling. These refinements yield no independent nonroutine invariant beyond the earlier result, even though the finite-field formula is correct. No distinct valuable remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
