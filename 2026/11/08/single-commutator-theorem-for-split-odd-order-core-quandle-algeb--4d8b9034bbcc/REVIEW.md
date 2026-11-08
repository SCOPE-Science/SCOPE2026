# Scientific review

## Correctness — PASS

The Fourier basis is invertible over the specified splitting field since its order is invertible, and direct substitution proves the sparse multiplication formula. The nonfixed orbits of the map sending a character to its inverse square have length at least three: a point of period two is already fixed because the relevant integer coefficients are three and negative three. The algebra decomposes into two orthogonal ideals; every nonfixed Fourier basis element is visibly a commutator. The key cycle-minor lemma is proved by a field-independent explicit base case and insertion induction, proving a *single* commutator realizes any linear combination. No finite experiment is used to prove a universal statement. A standalone script checks the product identity, modular commutator ranks, cycle-minor surjectivity and constructive witnesses in nine finite cases.

## Originality — PASS (qualified)

The nearest published research is Bardakov–Passi–Singh's 2022 Section 7 and Problem 7.5, Sangare–Ta's 2026 Section 5 finite computations, and Elhamdadi–Ta–Virgin's 2026 Fourier method for idempotents. None of these claims the full split-coefficient, odd-abelian-core one-commutator theorem or the orthogonal ideal decomposition. The Fourier infrastructure is prior; the new proof identifies the exact derived ideal and proves surjectivity of the cyclic adjacent-minor map without genericity assumptions. Targeted published-finding corpus queries on commutator width, finite odd abelian cores, Fourier decomposition and cyclic minors returned different problems, including published quandle-idempotent and general commutator results. Related historical findings on dihedral-quandle derivations and core-quandle idempotents were checked for claim-level overlap and are different. An unlocated equivalent theorem under different terminology remains possible.

## Mathematical value — PASS

The result gives a definitive all-order width formula for a natural, nontrivial class specifically covered by a published open commutator-width problem. It goes beyond numerical evidence or a loose bound: every element has an explicitly constructible single-commutator witness, and the exact commutator ideal and complementary commutative ideal are identified for all finite odd-order abelian groups, including noncyclic examples. The characteristic-five \(R_5\) width-two example outside the assumptions provides a substantively motivated boundary.

## Limitations and closest literature

The coefficient field must split the characters; no unsplit-field, modular-characteristic, or even-order claim is made. The published Fourier technique itself is not new. Source inspections include Bardakov–Passi–Singh 2022 Section 7, Sangare–Ta 2026 Section 5, and Elhamdadi–Ta–Virgin 2026 Introduction and Section 3. Automated search absence is not proof of global originality. Independent mathematical audit is not yet performed.

Self-review: passed. Independent audit: not yet performed.
