# Independent mathematical audit

## correctness

PASS

The map Rg→C sending t to (f_1t,…,f_ℓt) is a surjective R-module map. Same Z₄-type implies same cardinality, hence injectivity; conversely injectivity makes it an isomorphism. For positive odd m, reduction of x^m−1 is squarefree and each lifted local factor has maximal ideal 2R_i of size 2^{d_i}. On an active factor a unit multiplier makes the local map injective. If all multipliers are nonunits, they annihilate the nonzero submodule 2R_i when g_i is a unit, or annihilate the entire nonzero seed summand when g_i∈2R_i. An inactive factor imposes no condition. Thus an active degree-d_i factor admits exactly 4^{ℓd_i}−2^{ℓd_i} tuples, an inactive one 4^{ℓd_i}. CRT multiplies the counts, and the joint condition uses every factor. The ratio is 1 iff there are no inactive factors because ℓ≥1 and d_i≥1; the zero seed gives the empty-product case. For m=3, g'=2x²+2x reduces to zero modulo x−1 and to 2 modulo x²+x+1. Independent replay `python3 /tmp/opencode/frozen-independent-checks.py qc` exhaustively enumerated the quotients using direct cyclic convolution and common annihilators, not the local-unit test. At ℓ=1,2,3, it gave (24,2880,225792) for both factors, (48,3840,258048) for the degree-two factor, (32,3072,229376) for the degree-one factor, and all tuples for the zero seed. The CRT proof is uniform; this is bounded corroboration.

## originality

FAIL

The exact admissible subset of the same multiplier residue space, including the active/inactive split, already follows from Aydin–Tyagi's Theorem 4.1 and its proof. Their Remark 2.4 gives the two sizes needed for its direct product count. The all-factor comparator is already Theorem 3.2; taking the cardinalities of these Cartesian products needs only one local subtraction and multiplication, with no further structural or enumerative step. No claim is made that the paper prints the density itself.

## value

FAIL

Search acceptance density is a natural planning quantity and the exact formula is a useful explicit corollary. In this formulation, however, its numerical value is mechanically fixed by the published acceptance test and published local sizes. The whole-polynomial versus active-factor comparison is the ratio of those same two products; the example adds only substitutions. There is no further counting or structural result on top of this extraction under the stated uniform-residue model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
