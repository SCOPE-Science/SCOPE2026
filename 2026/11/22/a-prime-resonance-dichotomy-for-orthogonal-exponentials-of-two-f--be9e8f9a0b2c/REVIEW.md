# Independent mathematical audit

## correctness

PASS

The geometric sum vanishes exactly at k/(rc) with r not dividing k; the denominator-zero points give value 1. Thus pairwise orthogonality is precisely the union-of-two-zero-sets difference condition. With p∤b and q∤a, coprimality gives gcd(pa,qb)=1. After translating any member to zero, all frequencies are on the common rational grid, and reduction modulo integers is injective on the family (a difference in Z gives inner product 1). Chinese remaindering places all nonzero zero residues on the two axes. Points from distinct nonzero axes cannot coexist because their difference is on neither axis. On an axis the residue condition modulo the corresponding digit count gives the bound p or q, with equality q possible only on the q-axis. Lifting back to real frequencies gives exactly the stated k_j/(qb) with a complete residue system modulo q, not just an assertion modulo Z. In resonance the displayed frequencies are orthogonal by the unequal-j/equal-j cases, and repackaging with p and q interchanged verifies the second construction, including the case when both divisibilities hold. In either resonance case ia+jb are all distinct by b | i−i′ and a | j−j′ together with b≥p or a≥q. Dimension then gives the upper bound pq and completeness, while the nonresonant support has at least p+q−1>q locations even when some sums collide. A separate exact rational check of 61 small finite cyclic graphs (p,q in {(2,3),(2,5),(3,5)}, coprime steps up to 6, lcm(pa,qb)≤120) agreed with the clique numbers and tested the explicit families. Replay: python3 /workspace/branches/89ff7c1c-d1a1-4bad-9d5a-7d3bb071f05c/ordinal1_exact_check.py. This is supplementary; the uploaded checker was inspected, not run, and the proof addresses all parameters and arbitrary real frequency translates.

## originality

PASS

The convolution-mask method and resonant product-form construction are not the novelty. The substantive increment is the exact nonspectral maximum and all-maximizer classification for two different prime lengths. The inspected comparisons support that increment within bounded coverage; an inaccessible classical theorem and differently indexed finite character-packing work remain risks.

## value

PASS

Fourier packing capacity is a natural partial-basis invariant, and two uniform digit progressions with different prime sizes are a motivated setting for comparing cross-divisibility with basis existence. Beyond the standard resonant construction, the result gives an exact gap with no intermediate capacities and tells which frequencies can attain the nonspectral optimum, including for convolutions with collided sums. These statements answer a concrete packing and rigidity question not supplied by the compared basis-existence results; the concise clique argument does not turn the complete arithmetic classification into an arbitrary numerical slice. The review credits this narrow structural result, not applications to infinite convolution or a new general clique theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
