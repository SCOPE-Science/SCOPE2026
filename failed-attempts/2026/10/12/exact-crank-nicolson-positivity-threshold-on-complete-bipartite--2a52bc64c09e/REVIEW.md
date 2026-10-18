# Independent mathematical audit

## correctness

PASS

PASS. With s=h/2 and R=(I+sL)^(-1), the exact Cayley identity C_h=2R-I reduces all finite connected undirected-graph positivity to R_ii>=1/2. In K_{p,q} the p-part resolvent diagonal is 1/n+(p-1)/[p(1+qs)]+q/[pn(1+ns)]; the q-part diagonal is no smaller for p<=q. Direct rational simplification gives R_ii-1/2=(1+ps-q(n-2)s^2)/[2(1+qs)(1+ns)], yielding h*=[p+sqrt(p²+4q(n-2))]/[q(n-2)] for n>2 and all-h nonnegativity for p=q=1. The p-part first loses positivity beyond the threshold. Independently reconstructed exact rational matrices agree for a biclique grid, including K_{2,3}, h=1, diagonals (-1/35,-1/35,1/7,1/7,1/7). This finite check is not the all-p,q proof.

## originality

FAIL

FAIL. A published October 4 research result, 'A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains', was identified in a fresh Resultary search and its complete RESULT.md inspected. It proves for arbitrary finite Markov generators exactly C_h>=0 iff every resolvent diagonal is >=1/2, and for every reversible chain the full spectral return-diagonal threshold by eigenprojectors, including a sharp threshold and unconditional-positivity characterization. K_{p,q} with unit edges is one such reversible chain, and its standard four-eigenspace spectrum inserted into that already-published criterion leads to the submitted quadratic and radical by routine simplification. Thus the graph-independent theorem is literally prior, while the named biclique formula is an immediate explicit specialization of stronger prior coverage. Different wording or the novel displayed radical does not avoid implication coverage.

## value

FAIL

FAIL. A sharp numerical time-step threshold on a natural biclique graph is useful, but here the spectral return criterion and every-reversible-chain classification already provide the structural mathematical content; substituting the elementary K_{p,q} spectrum into the general formula is a routine worked example, not a separately motivated unknown invariant or research gap. Correct arithmetic, explicit coefficients, and a positive gap above a generic SSP bound do not rescue a covered specialization as new mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
