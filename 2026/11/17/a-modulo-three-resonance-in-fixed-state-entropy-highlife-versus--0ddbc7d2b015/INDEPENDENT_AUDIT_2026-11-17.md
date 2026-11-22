# Independent mathematical audit

## correctness

PASS

For 3-by-n Moore torus n>=3, the eight neighbors are distinct and the three-site middle column sees total neighboring column weight |a|+|b|+|c|-b_r. Counting labelled fixed configurations becomes the trace of a complete 64-state directed de Bruijn transfer. Inspected 512-triple Boolean-condition verifier enumerates 155 HighLife versus 156 Life edges, common recurrent components sizes 30 and 27, and sole removed edge (7,0)->(0,7); characteristic polynomials of size-30 blocks are z^20 p_H(z), z^20 p_L(z), and of the other block z^24(z^3-27). A common 3^{n+1} term is present exactly for 3|n. Primitivity of both 30-state blocks and strict entrywise edge deletion give 2.65923<rho_H<2.65924<2.70363<rho_L<2.70364<3 by the disclosed exact integer Collatz vectors. Trace Perron asymptotics imply ratio 1 on 3k and 0 on 3k+1,3k+2, with Life-HighLife difference asymptotic rho_L^n. Independently written direct synchronous torus census exhausts all 2^{3n} states for n=3..7, reproducing counts (127,37,91,2539,1009) for HighLife and (127,39,121,2595,1177) for Life. The finite transfer characteristic computation is exhaustively specified, not inferred from those small n.

## originality

PASS

Earlier published width-three Life-only fixed-state formula and 3-column weight resonance give the exact Life polynomial and dominant subsequence, so that part is covered and not counted as new. The final theorem additionally computes the HighLife transfer polynomial, shows that exactly one Life transition is removed under B36, proves a smaller positive Perron root, and derives ratio 1 versus exponentially vanishing along distinct residues; Life-only statements and classical inclusion do not imply those. Bibliographic uncertainty remains concerning Bell 1994 compressed archive and uninspected portions of McIntosh.

## value

PASS

The exact quantitative comparison of two canonical natural Life-like rules on the smallest genuinely eight-neighbor periodic strip is a meaningful finite-width phase distinction. A single extra birth transition changes the primitive Perron root but leaves a period-three recurrent component untouched, yielding a genuinely arithmetic 0/1 subsequence comparison. The explicit all-n count and spectral witness could be reused by researchers studying fixed-state entropy, not merely a handful of tabulated instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
