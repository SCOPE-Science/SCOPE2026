# Independent mathematical audit

## correctness

PASS

The unnormalized positive-exponent transform preserves oddness, doubles positive-representative support counts, and squares to 15 times reflection. A one-column sine support has at most two zero rows since entry S_yu vanishes exactly when 15 divides yu. For two columns, zeros are the zero rows plus at most one projective direction. Evaluation at a primitive order-15 root in characteristic 31 or 61 preserves complex cyclotomic zero minors; reduced rows that become entirely zero can be counted separately, so the modular maximum indeed bounds the complex maximum. Inspected the script and output without executing the upload. Independently reduced all 441 two-by-two minors modulo Phi_15 in characteristic zero: 24 vanish and the zero-cap histogram is {1:8,2:12,4:1}. For columns (3,6) row 5 vanishes and the other rows split as {1,4,6} and {2,3,7}. The only four-row rank-one matrices on those columns are these triples with row 5, so the exact Fourier geometric sums for h_1,h_2 identify the two distinct kernels. Other coefficient lines on the same support have only the common zero row. The singleton bound, the two-column bound and duality exclude pair-count sums below 5 and leave only (2,3),(3,2) at equality; hence the four distinct rays. As an additional direct check, among 735 five-row/three-column matrices exactly two had rank two, with columns (1,4,6) or (2,3,7) and rows (1,2,4,5,7); each was checked by zero 3x3 minors and a nonzero 2x2 minor. Replay: /workspace/branches/be1ce370-d673-4cd2-8684-5f81b69cc2ac/exact_replay.py and exact_replay_output.txt in that directory. This is not a claim about every higher-order sine minor or other moduli.

## originality

FAIL

The closest full-matrix rank census is stronger in the relevant direction. Its actual orbit-incidence table, not merely the title or shared modulus, gives the frozen two-column exclusion and the equality rays via the involution blocks and one elementary sign check. The unrestricted uncertainty papers and the fixed-row record do not by themselves give that coverage. The catalogue dates do not determine priority.

## value

FAIL

Order fifteen is a natural small odd squarefree test case, and odd equality classification is more informative than a bare uncertainty bound. But the exact result at this modulus is recoverable from the indexed full Fourier incidence table by a direct signed-pair restriction and elementary exclusions of the remaining candidates. The frozen record supplies no uncovered higher-modulus theory or other separate invariant; the replay and alternative proof do not by themselves add one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
