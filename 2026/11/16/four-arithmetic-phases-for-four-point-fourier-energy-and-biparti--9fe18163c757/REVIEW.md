# Independent mathematical audit

## correctness

PASS

PASS. Reconstructed all four integer modulus branches for every N≥8 directly from r(t)=|A∩(A+t)|, E(A)=16+∑_{t≠0}r(t)² and ∑_{t≠0}r(t)=12. Translation stabilizer |H| divides four: order four gives 64 (subgroup coset); order two yields two quotient points with energy 6 lifting by |H|³=8 to 48. For trivial H, all nonzero overlap counts≤3 and an involutive difference can contribute only 0 or 2. Pairing ±t bounds the noninvolution sum: maximum 52 requires two pairs with overlap three; the next possible odd-order maximum is 44, and involution-two case is at most 46. Three internal d-arrows in four vertices are a four-path or a 3-cycle plus isolate; the latter cannot attain the relevant maxima (odd-order energy 40), while the four-step progression has energy 64,52,46,44 for step orders 4,5,6,≥7. This yields exactly the extremizers in all four torsion regimes. Checked analytic graph transform f=1_A(x)+1_A(y)−2 1_A(x)1_A(y), Parseval ∑|f̂|²=8(N−4), and ∑|f̂|⁴=[8(N−4)]⁴/N⁴+2(N−8)⁴(NE−256)/N⁴+16(NE−256)²/N⁴. The latter is strictly increasing in E for E>0, including N=8, so the D4 minimum and equality shapes follow. Inspected checker.py enumerating N=8..33 and separate signed-edge pair sums; an independent separate script enumerated N=8..27 exactly and corroborated all four maxima. Neither finite enumeration is the all-N proof.

## originality

PASS

Best-of-knowledge original residual scientific increment after explicitly excluding known prior coverage; exact historical priority is not certified. Directly relevant inaccessible paper remains a live priority risk, not an automatic scientific failure.

## value

PASS

PASS. The exact sharp four-arithmetic-phase classification and equality geometries give a natural Fourier fourth-moment/collision-dimension optimization for labelled K_{4,N−4}, across every ambient order. The nontrivial torsion transitions at 4 and 5 and involution parity explain why a single generic four-point progression does not solve the problem, making this more than a standard graph Fourier identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
