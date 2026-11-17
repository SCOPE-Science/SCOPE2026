# Independent mathematical audit

## correctness

PASS

For B=[n,n+t] integer, exact k-fold sumsets are kB=[kn,k(n+t)]. Let e=ceil((q-1)/t), K=q+e. For k>=K, the offsets qi+[0,(k-q)t] for i=0..t overlap/meet on the integer lattice since (k-q)t>=q-1, saturating kB inside qS*+S. Any s>=Kn represented in a shorter layer also belongs to KB and is covered. Below Kn, K<=2q-1 forces every positive u in s=qu+v to be a single generator n+i and restricts v=hB with h<e, yielding exactly the finite set-minus-intervals decomposition. For sharpness with k=K-1 and h=e-1 choose large n and s=kn+ht+1; offsets 0<=r<=ht do not hit it after q dilation, so footprint meets penultimate layer. The GM_2 and GM_3 formulas follow by finite interval counts. Independently enumerated 1,617 small (n,t,q) footprint cases by semigroup DP. Uniform theorem is established by the layer covering argument, not partial enumeration.

## originality

PASS

Best-of-knowledge PASS only for the structural FULL complement and the sharp UNIVERSAL layer cutoff, not for the earlier known general numerical formula for GM. Marques–Mendoza–Quoos–Tizziotti (arxiv:2508.17022), full PDF Section 4 Theorem 4.1 gives Apéry-based numerical cardinality for all semigroups and Theorem 4.4 explicit sufficiently wide intervals, so binary/ternary numerical values are not independently priority-worthy. Inspected formulas did not state the precise interval-layer survivor set and sharp K. These stronger structural assertions are not logically supplied merely by numerical counts; broader semigroup ideal literature may hide equivalent geometric descriptions.

## value

PASS

The Geil–Matsumoto footprint is a natural semigroup ideal complement relevant to coding bounds. Its exact SUPPORT, not just cardinality, with provably optimal uniform finite-layer cutoff across every consecutive-generator width gives reusable geometric/algorithmic structure and excludes unnecessary high-layer search. Finite structural classification remains valuable even with a prior all-semigroup count formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
