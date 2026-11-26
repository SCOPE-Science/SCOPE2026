# Independent mathematical audit

## correctness

PASS

The trace pairing gives bijective point and line labels modulo N; a chosen difference t in D labels an edge, independently of its point index. Intersecting H with C_N gives <r^m>; a noncyclic H has image C_3 and can be generated over that intersection by r^aF, whose cube is the identity. The first quotient has 2m vertices and m(q+1) edges; in it the remaining generator sends vertex index i to a+qi modulo m and edge (i,t) to (a+qi,qt), with t still modulo N. If f is the number of fixed indices and delta the number of multiplier-fixed differences, Burnside gives vertices (2m+4f)/3 and edges [m(q+1)+2f delta]/3. Hence the connected graph rank is 1+[m(q-1)+2f(delta-2)]/3. The gcd(N,q-1) is gcd(3,q-1); if q is 0 or 2 mod 3 there is one fixed index for any m,a, and the only candidate difference t=0 is respectively in or out of D according to Tr(1). If q=1 mod 3 there are three candidate t, of which the two nonzero ones represent nontrivial Frobenius eigenlines and have trace zero. Thus delta=2 and f cancels. Nonnegativity and integrality follow from connected graph cell counts, including q=2,m=1 giving zero. A nonidentity Singer rotation has no fixed vertices or inverted edges, excluding any fixed realization points when d>1. For a pure order-three subgroup use m=N to count fixed vertices and edges directly: one point and one line when q=0,2 mod 3, with one edge only when q=0; for q=1 mod 3, there are none when 3 does not divide a, and otherwise each of the three fixed vertices on each shore has two fixed neighbours, a simple bipartite 2-regular graph on six vertices, necessarily one six-cycle. The identity rank is 1+N(q-1)=q^3. The geometric quotient retains edge orbits even if parallel, because the shores are preserved. Inspected verify_singer.py, checks.txt and VERIFICATION.md without executing the script. Their ten-field checks are corroboration only; the representative-lift loop at a=0,1,2 covers the possible residue classes, and all fields and subgroup indices are accounted for by the proof.

## originality

PASS

Pass relative to the inspected statements, for the complete all-subgroup graph and geometric fixed-space classification. The full cyclic Singer graph with two vertices and q+1 parallel edges is already credited to the dessin literature in the frozen record and is not a new component. Related flat, embedded-dessin and higher-rank results do not supply the combined all-lift modular formulas on evidence read; full-text gaps remain explicit.

## value

PASS

This classifies natural symmetry quotients and fixed loci of a standard finite building, beyond the familiar full cyclic quotient. In one formula it resolves all subgroup indices and distinguishes how the Frobenius arithmetic affects fixed geometry; notably the exceptional threefold fixed-vertex counts can change the fixed locus without changing the quotient's rank. The exact connected graph type is useful without assumptions about a chosen embedding or a field-size cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
