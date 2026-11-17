# Independent mathematical audit

## correctness

PASS

For C_n plus non-cycle chord 0–a, 2≤a≤n−2, a singleton or non-cycle-adjacent blue pair cannot force initially; each of n cycle-edge pairs can. For a cycle pair at positions i,i+1 on the a-edge chord arc, two propagation fronts fill that arc; chord endpoint 0 turns blue after i rounds and endpoint a after a−1−i rounds, and neither can force into the second arc until both are blue because each earlier endpoint has two uncolored neighbors (chord endpoint and cross-arc neighbor). At T=max(i,a−1−i) both are blue, then the b−1 internal vertices fill simultaneously from endpoints in floor(b/2) rounds, giving t_a(i)=T+floor(b/2). Reverse arc likewise. The max-distance histograms B_a,B_b immediately give H_{a,b}, endpoints, no gaps and fastest count 2+1_(2|a)+1_(2|b). Independent direct synchronous graph simulation tested every chord and each two-vertex initial set for n=4..14, confirming time arrays; the full all-n proof is the symbolic front argument. Both packaged Python and C++ graph simulators were read.

## originality

PASS

Boyer et al. arXiv:1801.08910 Claim 1 prove adding a chord preserves all zero-forcing sets (hence the polynomial), but do not provide propagation times. Chilakamarri et al. arXiv:1105.1492 give the unchorded cycle iteration index. Hogben et al. arXiv:1410.4191 and Ferrero et al. arXiv:2511.16335 address general propagation-time notions/intervals and other families. A fresh Resultary semantic query found no earlier exact all-a,b chord-resolved time histogram apart from the audited Nov8 entry. The new full distribution is not a corollary of preserving forcing-set membership, since first-passage times depend on propagation geometry. Best-of-knowledge PASS with remaining literature risk.

## value

PASS

A single chord is the minimal structural perturbation of a cycle and preserves its zero-forcing polynomial, making the change in propagation times a sharp natural example of a dynamic invariant invisible to static forcing-set counts. The complete seed-resolved enumerator, parity jump and efficient-seed count distinguish chord geometry. This exact graph-family classification is mathematical content beyond substituting into a standard formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
