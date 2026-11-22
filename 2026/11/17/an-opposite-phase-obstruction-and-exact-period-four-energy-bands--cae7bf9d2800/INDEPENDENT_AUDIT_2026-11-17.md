# Independent mathematical audit

## correctness

PASS

For labelled loopless K_n and n>=4, the update x_v(t+1)=x_v(t)+R_t-n f_v(t) forces the same 4-step firing count h at each vertex. The directly inspected Jiang–Scully–Zhang 2012 Theorem 6.2 excludes clumpy 2-fire words; alternating 2-fire words reduce to temporal period <=2, so primitive four-cycles have h=1 or 3. For h=1, necessary and sufficient chip intervals are [n-1-p_j,n-2-p_j+a_{j-1}] for v in phase j, with all four phase sizes positive. This establishes the multinomial product P_n(z); complement x->(2n-3)-x exchanges the one- and three-fire sectors. Extremizing B=(n^2+sum a_j^2)/2-n and U=n(n-2)-(a_0a_2+a_1a_3), then connecting positive quadruples by unit transfers, proves interval-filling and gap size 3n-5. The upper-edge singleton-opposite-pair inclusion/exclusion gives 4n(n-1)(2^{n-2}-n)+24*[n=4]. An independent microscopic four-step exhaustive enumeration of chip boxes n=4,5,6 matched the polynomial exactly, with primitive counts 48, 960, 17280; inspected verify_phases.py independently intersects the firing inequalities for n=4..8. Neither finite check is used as an infinite proof.

## originality

PASS

The all-n primitive-four K_n mass polynomial and opposite-phase singleton obstruction are not implied by the exact primitive-three connected-graph polynomial (different period and phase constraints) or by a K_{2,b} primitive-four formula (different graph, cannot specialize to K_n for n>=4). The published no-clumpy restriction gives needed local words but not the global integer mass distribution and band-edge coefficients. Best-of-knowledge PASS is restricted to these four-period K_n statements; no exhaustive priority guarantee.

## value

PASS

Temporal period-four chip-firing on the naturally symmetric complete graph is a nontrivial enumerative problem: the theorem gives full coefficients by mass, two sharp integer bands, an exact forbidden gap, and exceptional n=4 endpoint multiplicity. These data are neither a routine application of a period-three formula nor a small-instance recomputation; useful to classify recurrent states and calibrate chip-firing energy spectra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
