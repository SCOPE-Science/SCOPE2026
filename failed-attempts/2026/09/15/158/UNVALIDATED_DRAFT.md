# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Sparse symmetric submaximal minors under 2-connectedness

## Status of the target
The target claims: for every n >= 3 and every graph G on [n] with all (n-1)-vertex induced
subgraphs connected, the ideal I_{n-1}(X_G) of submaximal minors of the sparse generic symmetric
matrix is prime. This report resolves the target **completely for n = 4** (all three 2-connected
graphs: C4, diamond/K4-minus-edge, K4) by a uniform argument, and develops auditable evidence plus a
partial general route for n >= 5. Because the complete target (all n) is not established, the claim is
submitted as **EMERGENT_FINDING** (a complete n = 4 classification theorem), not as TARGET.

## Theorem (n = 4 case of the target; proved)
Let K be a field of characteristic zero (in fact any field of characteristic != 2). Let G be a graph
on 4 vertices in which every 3-vertex induced subgraph is connected (equivalently: G is 2-connected).
Then, up to isomorphism, G in {C4, diamond, K4}, and for each of them the ideal I_3(X_G) of 3-minors
of the sparse generic symmetric matrix is prime.

## Proof (uniform for all three graphs)
Work in R = K[diagonals a,b,c,d; edge variables], with lex order diagonals > edge variables.
The proof has three steps. Every computation below is reproduced by the audit script
`output/artifacts/spair_audit.py` (exact arithmetic over QQ).

**Step 1 (Combinatorial reduction).** A 2-connected graph on 4 vertices has minimum degree >= 2,
hence at least 4 edges; the graphs with degree sequences (2,2,2,2), (2,2,3,3), (3,3,3,3) are
uniquely C4, diamond, K4. (Any 4-vertex graph with min-degree >= 2 and 4 edges is C4; with 5 edges
a diamond; with 6 edges K4. The audit script enumerates degree data; the identification is elementary.)

**Step 2 (Squarefree Groebner basis => I radical).** For each of the three graphs, the 10 nonzero
3-minors (indexed by deleted row <= deleted column) are already a lex Groebner basis: all C(10,2) = 45
S-polynomials reduce to zero (certified in `spair_audit.py`), and every lex lead term is squarefree:
- C4: abc, abd, abr, acd, adq, aqr, bcd, bcs, brs, cdp;
- diamond: abc, abd, abr, acd, act, adq, bcd, bcs, brs, cdp;
- K4: abc, abd, abu, acd, act, ads, bcd, bcr, bdq, cdp.
A homogeneous... (in fact any) ideal with squarefree initial ideal is radical (Sturmfels; the standard
result that R/in(I) reduced implies R/I reduced). Hence I_3(X_G) is radical: I = sqrt(I).

**Step 3 (Irreducibility of V(I) => I prime).** V(I_3(X_G)) is the locus of sparse symmetric matrices
of rank <= 2. Parametrize it by U in M_{2x4}: X = U^T U, x_{ij} = u_i . u_j. Over an algebraically closed
field of characteristic != 2, every symmetric matrix of rank <= 2 factors this way, so V(I) is exactly
the image of Z = {U : u_i . u_j = 0 for each non-edge ij}:
- K4: Z = A^8, irreducible;
- diamond: Z = {u1u3 + v1v3 = 0} x A^4, an irreducible quadric hypersurface times affine space, irreducible;
- C4: Z = {u1u3+v1v3 = 0} x {u2u4+v2v4 = 0}, a product of two irreducible quadric hypersurfaces in
  disjoint variable sets, hence irreducible. (Each quadric XY + ZW in A^4 is irreducible: else it would
  split as two linear factors F*G, and V(F,G) of dimension >= 2 would lie in the singular locus, which is
  just the origin since grad = (Y,X,W,Z).)
The continuous image of an irreducible variety is irreducible, so V(I) is irreducible. A radical ideal
with irreducible variety is prime. This gives primality over the algebraic closure, hence over K (primality
descends: I prime over K-bar implies I cap R prime... more precisely I is defined over K and K-bar[X]/I K-bar
a domain implies... the contraction of a prime is prime; contracted ideal equals I since I is spanned over K by
its generators). ∎

## Remarks on the general-n route (conjectural, NOT claimed)
- No (n-1)-minor vanishes identically under the 2-connectedness hypothesis (needed for the GB picture);
  consistent with all computed cases (C4, diamond, K4, C5, double-hub at n = 5).
- The lex "diagonals first" order gives squarefree leads in every computed case (n = 4: certified GB;
  n = 5 C5: lead data observed). General proof of the GB property is open.
- Irreducibility of the constraint variety Z for general 2-connected G is the hard core: C4's decoupling
  (disjoint constraint variables) is special. The double-hub n = 5 example (2-separator {0,1} with 3 flaps)
  still has dim-10 irreducible-looking V (proper codim-3 slice of dim 7 computed), and random 3-plane sections
  of the C5 variety have irreducible degree-20 elimination polynomials — but these are evidence, not proofs.
- Sharpness: the hypothesis is best possible in the sense that disconnected G-v gives block structure forcing
  reducibility (e.g. a cut-vertex yields block-diagonal matrices after permutation, and I_{n-1} contains
  products splitting across blocks — stated as expectation, not proved here).

## Verification-critical artifacts
- `output/artifacts/spair_audit.py` — certifies: 10 nonzero minors per graph, all 45 S-pairs reduce to 0,
  all lex leads squarefree. Run: `python3 output/artifacts/spair_audit.py`.
- `output/artifacts/t2_squarefree.py` — prints all GB elements and leads.
- `output/artifacts/minors_c4.py`, `groebner_c4.py`, `elim_c4.py` — C4 generator data.
- `output/artifacts/colon_p_correct.py` — I : p = I for C4 (p not a zerodivisor; prime-consistent).
- `output/artifacts/c5solve.py`, `c5factor.py` — C5 section degree-20 irreducible elimination polynomial.
- `output/artifacts/doublehub.py`, `doublehub_slice.py` — n = 5 2-separator stress test.
