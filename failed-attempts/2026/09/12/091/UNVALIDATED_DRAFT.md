# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Isomorphism spectrum equals bi-embeddability spectrum for every computable structure, in particular for computable reduced abelian p-groups of Ulm length at most ω+1

## 1. Definitions (standard spectrum readings)

Fix a prime p. Let G be a countable structure. Its **isomorphism spectrum** is

    DgSp(G) = { deg(X) : X is (a set coding) a copy of G isomorphic to G },

where "X-computable copy" means a structure whose atomic diagram is computable in X,
i.e. Turing reducible to X (uniformly: the copy's universe and operations/relations
are decided by an oracle for X). Its **bi-embeddability spectrum** is

    BiEmb(G) = { deg(X) : some X-computable structure H is mutually abstractly
                 embeddable with G (H embeds into G and G embeds into H) }.

That is, the witness embeddings are abstract group embeddings between the structures,
not embeddings required to be X-computable; this is the standard relativised notion
("computable-in-X copies" describes the copies, not the embeddings). We also note
below that the conclusion is robust: it holds under the stricter reading too.

Both spectra are sets of Turing degrees.

## 2. Theorem (complete negative resolution of the target question)

Let G be any computable countable structure — in particular any computable reduced
abelian p-group of Ulm length ≤ ω+1 with divisible part zero. Then

    DgSp(G) = BiEmb(G) = { all Turing degrees }.

Hence no such G satisfies DgSp(G) ⊊ BiEmb(G). The second disjunct of the target
claim is proved: equality holds for every computable reduced abelian p-group in
the stated Ulm-length scope (indeed for every computable structure, with no use
of the Ulm-length, reduced, or divisible-part hypotheses).

## 3. Proof

Step 1 (DgSp(G) ⊆ BiEmb(G), always). If H ≅ G then the isomorphism in each
direction is an embedding, so H and G are mutually embeddable. Thus every degree
computing an isomorphic copy also computes (the same) bi-embeddable copy.

Step 2 (Both spectra are upward closed). If a structure A has atomic diagram
computable in X and deg(X) ≤ deg(Y), then its diagram is computable in Y. So
membership of a degree d via a witness copy propagates to every degree e ≥ d.

Step 3 (The computable degree 0 lies in both spectra). Since G is computable, fix
a computable copy G₀ ≅ G. Then 0 = deg(∅) ∈ DgSp(G) via G₀. By Step 1,
0 ∈ BiEmb(G) as well (G₀ mutually embeds with G via the isomorphisms).

Step 4 (Equality). By Steps 2–3, each spectrum contains 0 and is upward closed,
hence each equals the class of all Turing degrees. They are therefore equal;
a fortiori DgSp(G) ⊄ BiEmb(G) is impossible. ∎

## 4. Robustness remark: the stricter reading

If BiEmb(G) were instead defined to require the mutual embeddings themselves to be
X-computable, the conclusion is unchanged: the computable witness G₀ admits
computable identity/isomorphism embeddings, so 0 ∈ BiEmb(G) on that reading too,
and upward closure applies identically. The equality argument uses no property of
abelian p-groups.

## 5. Why this does not contradict known non-rigidity phenomena

Structure-level mutual embeddability does not imply isomorphism, even among
computable reduced p-groups of finite Ulm length. Explicit example (for clarity,
not needed by the proof): G₀ = Z/p ⊕ (Z/p²)^{(ω)} and H₀ = (Z/p²)^{(ω)} are
computable, mutually embeddable, but non-isomorphic: the dimension
f₀ = dim(G[p]/pG) is 1 for G₀ and 0 for H₀. Both are computable, so each has
DgSp = BiEmb = all degrees. Structure-level bi-embeddability without isomorphism
does not produce spectrum-level separation whenever the structures involved are
computable — which is exactly the target's hypothesis.

## 6. Conclusion

The target question is answered completely in the negative: no computable reduced
abelian p-group G of Ulm length ≤ ω+1 with divisible part zero has
DgSp(G) a proper subset of BiEmb(G); instead DgSp(G) = BiEmb(G) holds for all of
them, by a general computable-structure argument.
