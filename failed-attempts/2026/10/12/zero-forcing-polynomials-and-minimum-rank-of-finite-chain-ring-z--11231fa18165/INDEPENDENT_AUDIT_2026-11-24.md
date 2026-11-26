# Independent mathematical audit

## correctness

PASS

Successive nonzero radical layers have sizes (q−1)q^(ell−i−1), by the simple residue modules of a finite chain ring. Valuation gives adjacency iff i+j>=ell for distinct vertices, and the twin condition prohibits two whites in one layer. If t is the highest white valuation, a blue vertex at ell−t sees exactly the white at t. The only unavailable source is the one-vertex (2,2) case: the only possible singleton is layer ell−1 at q=2, and if it is a white source then t=ell−1 too, giving ell=2. Thus the force order and all coefficients are correct. The layer matrix with its indicated diagonal becomes unit triangular after reversing columns; its incidence lift has rank ell−1 and M<=Z gives equality. The zero matrix on K1 supplies mr=0 and the isolated vertex must start blue. Root recovery and the minimum count follow as stated. Independent replay python /workspace/audit_checks.py 3 uses direct modular multiplication and exhausts masks for Z/4, Z/8, Z/9, Z/16, Z/27 and Z/32; it matches every profile and coefficient (e.g. Z/32 gives {11:64,12:120,13:70,14:15,15:1}). This is corroboration, not the proof of arbitrary q and ell.

## originality

FAIL

The full ordinary forcing classification and factorization are immediate specializations of Boyer et al. Theorems 10 and 12, not just applications of a general-purpose counting algorithm. For ell=2m, use the creation order V_m (1), V_(m−1) (0), V_(m+1) (1), V_(m−2) (0), V_(m+2) (1), and so on. For ell=2m+1, use V_m (0), V_(m+1) (1), V_(m−1) (0), V_(m+2) (1), and so on. Each 0-layer sends no edges to earlier layers and each 1-layer is dominating when appended, by i+j>=ell; these are exactly the blocks, with the first block of size at least two outside K1. Every 0-block has at least two vertices. Boyer's separation condition is therefore automatic for every omitted-at-most-one-per-block profile, including q=2 with a singleton final 1-block. Theorem 12 gives exactly the factorization and minimum count. The same-graph Resultary record 86625146ed7a already gives Z, M, mr and the K1 exception. Parameter recovery is mechanically implied by those known invariant relations: the polynomial's degree N and least exponent Z give ell=N−Z+1 and q=(N+1)^(1/(N−Z)) outside K1. Using roots instead does not change that conclusion. This is a coverage decision, not a correctness failure or an inference from inaccessible papers.

## value

FAIL

This is a useful worked threshold-graph example, and its symbolic proof is sound, but no independently useful new exact fact remains in the finding. The known class theorem makes every block choice admissible here, and knowing the two extreme exponents mechanically recovers the parameters. A different proof or the convenient root presentation is not a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
