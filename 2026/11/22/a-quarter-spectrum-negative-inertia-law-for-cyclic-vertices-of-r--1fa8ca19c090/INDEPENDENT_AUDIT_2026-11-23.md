# Independent mathematical audit

## correctness

PASS

For a fixed k-set of roots, the complete directed rooted-forest determinant on the n−k nonroots is det(nI−J)=k n^{n−k−1} when k<n, and the empty minor is 1 when k=n. Independently choose a permutation on the k roots, allowing fixed points. Thus the claimed multiplicity is exact, with no empty cyclic set. Boolean characters diagonalize the symmetric counting convolution (no n^n normalization). The size-k signed sum is the kth coefficient of g(z)=(1−z)^s(1+z)^{n−s}; integrating z g′(z) at z=t/n with e^(−t) gives the required k·k! factor. Differentiation produces the bracket n−2s−t after substitution, strictly negative at t>0 even at the midpoint. The exponent s−1 is even for the claimed sector and can only add an isolated zero (or none), so the integral is strictly negative. At s=n the factor (1+t/n)^(−1) cancels because the bracket is −n−t. Summing multiplicities gives H_n; the ordinary upper binomial tail is 2^{n−1}+O(2^n/√n) and its alternating correction is exactly (−1)^m binom(n−1,m−1) for m=⌈n/2⌉. Taking half the difference proves the limit of H_n/2^n, not a limit for the actual inertia fraction. The qualifying sector is nonempty also for n=2, where s=1 lies at the midpoint. A fresh direct check grouped cyclic vertices as the image of f^n, enumerated all maps for n=2–5, and matched the exact multipliers (n=2 has weight-ordered multipliers 4,−2,0). Replay: the fixed-root minor, coefficient formula and derivative can all be reconstructed in RESULT.md lines 20–45; finite checks do not establish all-order signs for any other sector.

## originality

PASS

Credit the forest–permutation model, the exact cyclic-set law and the Walsh/Krawtchouk coefficient representation as background or already available. The independently compared advance is the strict real sign for every odd weight at or above half the dimension, with its uniform negative-inertia bound. No inspected result implies this sign; the comparison is bounded, not a certification of absolute historical priority.

## value

PASS

The cyclic-vertex set is a basic random mapping statistic. Pairwise information or nonvanishing does not resolve the real signature of its convolution. The result gives strict negativity in a uniform sector of every dimension and at least quarter asymptotic density in the guaranteed sector, not merely a failure of positive semidefiniteness in small examples. This is an independently useful partial spectral classification even without a full inertia or invertibility theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
