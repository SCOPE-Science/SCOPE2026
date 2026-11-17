# Independent mathematical audit

## correctness

PASS

A valid height word of length n uses precisely {0,...,h}; each such word becomes a distinguished edge in the (n-1)-overlap digraph. Complete vertices are all W_{n-1}; incomplete vertices have indegree and outdegree one, and forced paths end at complete vertices in at most n rotations. Contracting forced corridors preserves cyclic edge-distinguished Euler tours. The reduced core has |W_{n-1}| vertices; directed matrix-tree/BEST give U_n=det(L_root) product_v(d_v-1)!, where the factorial product is the stated Stirling-number expression. Independently implemented height-word enumeration, full overlap digraph, forced contraction, exact SymPy integer cofactor and factorial product for n=2,3,4,5. Reproduced U=(1,8,113192681472,6214252301172599252248681937277855126085721393995382376959963220030028306692926790213752299261892430397440); at n=5, 541 original word-edges contract to 308 distinguished arcs on 75 core vertices, tau=27571102170646823740986252600397906575360 and the exact degree histogram {2:1,3:14,4:36,5:24}. Full finite census established with exact determinant, no extrapolation to n>=6.

## originality

PASS

Best of knowledge: Horan–Hurlbert 2012/2013 prove existence of weak-order universal cycles via the same height-word overlap graph; Sawada–Wong and Sawada–Gabrić develop successor rules, random uniform sampling, and general arborescence methods. Primary text does not supply these evaluated exact U_4/U_5 multiplicities or the concrete 75-vertex core certificate. Standard BEST/matrix-tree derivation is prior mathematics; novel surviving finite invariant is the fully evaluated enumeration and forced-corridor graph reduction at order five. A previously unindexed Euler-tour or integer table remains a real priority risk.

## value

PASS

Weak orders/permutations with ties form a natural classical combinatorial family. The number of distinct cyclic universal representations at n=4,5 (without extra symmetries) is a useful exact invariant distinct from the ordered Bell counts of inputs. Contracting 308 forced paths to 75 core vertices enables nontrivial exact determinant evaluation, with both finite completeness and replicable certificates; no arbitrary family-wide formula is falsely claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
