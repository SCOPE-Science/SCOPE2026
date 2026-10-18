# Independent mathematical audit

## correctness

PASS

For real 1<p<infinity, KKT analysis gives the simplex nearest-point map as an exponent-independent soft threshold. Every full-dimensional active set of cardinality k has Jacobian C_k=I_k-(1/k)11^T and all k arise; segment integration shows the sharp global ell_4 Lipschitz constant is max(1,max_{2<=k<=n} ||C_k||_4). Riener/Timofte half-degree symmetry reduces symmetric quartic norm inequality to two-value coordinate vectors; Hölder yields the stated maximum over j,k. Independent numerical checks reproduced the sample k=3 fourth-power norm 1.282440700621 and the larger k trend toward 1+2/sqrt(3). Crucially, the exact two-level formula for ||C_k|| and its continuum envelope are mathematically correct *but are already established in a much older primary theorem*; scientific coverage affects originality, not correctness.

## originality

FAIL

DECISIVE published implication: Baronti and Franchetti, “Minimal and polar projections onto hyperplanes in the spaces l_p and l_infinity,” Riv. Mat. Univ. Parma 16 (1990) pp.333--334, Theorem 1.3, prove ||I-(1/k)11^T||_p = max_{0<=j<=k} phi_p(j/k), where phi_p(t)=[t^{1/(p-1)}+(1-t)^{1/(p-1)}]^{(p-1)/p}[t^{p-1}+(1-t)^{p-1}]^{1/p}, and its dimension-free envelope max_t phi_p(t). At p=4, phi_4(j/k)^4 is algebraically *identical* to the submitted j,k summand. Their p=4 envelope is exactly (1+2/sqrt(3))^(1/4). The previously published cross-polytope soft-threshold theorem also proves the active-set reduction Lip=max_k ||C_k|| for the same nonlinear map, with simplex as the signed-positive orthant face variant; simplex KKT/Jacobian translation is elementary. Accordingly every claimed sharp finite and dimension-free constant is covered by this explicit 1990 theorem plus routine known projection reduction. The source comparison was made using actual scanned primary pages, not search-result snippets or paper titles.

## value

FAIL

The exact finite fourth-power and dimension-free constants are natural stability quantities, but they are already supplied by Baronti--Franchetti 1990 for the centering blocks. The extra simplex identification follows the familiar soft-threshold active-set formula and the published cross-polytope general principle; evaluating p=4 and differentiating a one-variable rational function is not a substantive new mathematical gap. Code correctness and clearer exposition cannot rescue a covered calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
