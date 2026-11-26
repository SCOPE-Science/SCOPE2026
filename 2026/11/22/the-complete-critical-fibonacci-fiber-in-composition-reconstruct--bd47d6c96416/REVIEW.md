# Independent mathematical audit

## correctness

PASS

A weight-3k source containing t>=3 has a forbidden read: keep that part at s=max(3,t-k) and choose weight 2k-s from the other parts, which can realize every weight up to 3k-t. This works for k>=2; the four compositions of 3 directly give the k=1 fiber. The all-two and all-one reads then force k twos and k ones. For the two-zero-gap obstruction, index the skipped source two by j in 1,...,k; it merges old gaps j-1,j into retained gap j-1 and contributes just one symbol there. For nonadjacent zero gaps p<q, the target requires ones in retained gaps p and q-1. If j>p+1, retained gap p equals old empty gap p; if j<=p+1, retained gap q-1 equals old empty gap q. For adjacent zeros the one required retained gap is empty unless j=p+1, when it has only one symbol for two requested ones. Therefore exactly one gap is empty, and each other gap contains one one, giving the entire displayed list. Conversely greedy earliest embedding gives d(empty)=1, d(2v)=1+d(v), and d(12v)=min(1+d(2v),2+d(v))=2+d(v) for the least missing positive read weight. At 21 the least missing weight is 3; stripping 21 ahead of a leading 2 adds two, so all listed sources have d=2k+1. None can read a part of size at least three. Finally the number of weight-2k compositions on parts 1,2 is F_(2k+1) by the ordinary recurrence with f_0=f_1=1.

## originality

PASS

Pass for the complete inverse fiber, not for the threshold or the extreme collision credited to Vatter. The closest same-day entry concerns one-deletion sphere volumes and can single out the same family at weight 3k, but does not give the exact weight-2k deck or characterize its preimages by the stated volume formula. No priority is assigned from the catalogue dates. Available primary and catalogue statements do not cover both directions of the exact fiber theorem; older or additional uninspected statements cannot be excluded.

## value

PASS

This measures an entire natural ambiguity class at the sharp recovery boundary, replacing a known two-witness collision with the exact linearly growing list and an explicit missing-read obstruction for other candidates. The shortest-missing-weight proof is a structural explanation of why every listed source—not merely the endpoint pair—produces the same complete observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
