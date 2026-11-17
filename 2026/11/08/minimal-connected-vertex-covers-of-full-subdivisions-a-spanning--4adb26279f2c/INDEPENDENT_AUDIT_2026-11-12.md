# Independent mathematical audit

## correctness

PASS

For any connected simple G with n>=3 and minimum degree>=2, an inclusion-minimal connected vertex cover C of S(G) omits an independent set I of original vertices. Every subdivided cut edge incident to I is forced; selected subdivision vertices on edges of G-I must connect all retained originals and form a tree, since cycle edges are deletable. Conversely, any such I with G-I connected and spanning tree T gives a connected vertex cover C(I,T); the three original-vertex essentiality cases (omitted neighbor, unchosen incident internal edge, or tree degree>=2) use min degree 2 and establish full inclusion-minimality. The size is 2n-1+sum_(v in I)(deg_G(v)-2), and the sum of tau(G-I) yields the stated polynomial. For K_(2,q), summing over degree-two omissions gives q*3^(q-1), while omitting one high-degree vertex gives 2 at exponent 3q+1. Independent exact mask tests S(K4) produced 16 covers size 7 and 12 size 8; S(K2,3) produced 27 size 9 and 2 size 10; these match theorem. Infinite proof is structural.

## originality

PASS

PASS (best-of-knowledge): the 2026 full-subdivision connected vertex cover study establishes only the scalar minimum 2n-1 and expressly notes that tree-generated minima do not exhaust all minimizers when original degree-two vertices occur. The 2023 general enumeration paper proves algorithmic and hardness results without an exact all-minimal subdivision size polynomial. The earlier general full-subdivision connected DOMINATION theorem has a different invariant and external-leaf/boundary-choice structure. No broader exact connected-cover enumerator was located; unindexed equivalent classification remains a residual risk.

## value

PASS

PASS: complete all-graph inclusion-minimal connected vertex cover classification captures the nontrivial distinction among independent deletion patterns via tau(G-I), including all nonminimum covers. The sharp two-term K2q specialization exhibits unbounded genuine gaps q-3 for q>=4, a natural and potentially useful exact structural fingerprint for connected cover enumeration. Known scalar minimum alone does not mechanically yield these counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
