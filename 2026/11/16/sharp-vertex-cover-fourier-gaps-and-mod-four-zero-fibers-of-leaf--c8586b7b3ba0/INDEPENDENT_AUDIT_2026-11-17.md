# Independent mathematical audit

## correctness

PASS

The private-leaf choices factor exactly: conditioning on independent core I yields W_G(a,b)=Σ_I (−1)^{a·I}∏_{i∉I}(1+(−1)^{b_i}). If B=supp b is not independent this vanishes; otherwise I=B∪J, J⊂G−N[B] independent, so W=(−1)^{a·B}2^{|N(B)|}Σ_J 2^{|R|−|J|}∏_{j∈J}(−1)^{a_j}. The original sum is divisible by 2^{n−α(G)} and choosing a maximum independent B kills all terms but I=B, attaining the sharp magnitude 2^{τ(G)}. Zero frequency gives max 2^n I_G(1/2), proving pseudoinverse norm and κ+. For residual path components the signed recurrence Q_0=1,Q_1=2+s_1,Q_m=2Q_{m−1}+2s_mQ_{m−2} has inductive 4-periodic valuation behavior: exact floor(m/2) for m mod 4=0,1,3 and zero or order≥m/2+1 for residue 2. All signs −1 give Q_m=2^{m/2}cos(mπ/4), producing a zero precisely for residue 2; all signs +1 give a positive value. Therefore the asserted complete universal/mixed/all-zero frequency-fiber trichotomy and exact order in universal fibers hold. Independently enumerated all 8191 sign strings of lengths 0..12 and checked the valuation/resonance conditions.

## originality

PASS

The graph-exclusion principal Fourier *inverse entry* formula uses residual independence polynomial I_R(−1/2) and already obtains the homogeneous all-minus path resonance at lengths 2 mod4, so this special feature is prior, not new. It does not imply that *every signed path continuant* avoids zero at lengths 0,1,3 mod4 or that the full ambient 2^{2n} Walsh transform of independent sets in G∘K1 has sharp all-core-graph gap 2^{τ(G)} and exact universal-fiber valuations. General corona independence-polynomial formulas count unsigned sets and hat-game signed polynomials do not directly provide these spectral/pseudoinverse results. Priority risks remain for unindexed multivariate graph polynomial results.

## value

PASS

An independent-set Boolean-cube convolution kernel on a canonical graph operation has a natural sharp recovery gap exactly determined by the vertex-cover number, including singular cases. The path corona classification resolves which entire pendant-frequency fibers are zero-free or mixed and their dyadic orders—a structural residue law beyond graph counting or a cheap zero test. The scope is precise; no claim to individual zeros inside mixed fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
