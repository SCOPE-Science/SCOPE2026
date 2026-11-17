# Independent mathematical audit

## correctness

PASS

For n>=2 exactly one hub-containing connected bundle has c=k-n+1 leaves, all others are singleton leaves. For fixed T the necessary and sufficient EF1 inequality is min_{outside}w >= h+sum(T)-max(h,max_T w), because ordinary EF1 permits removal even if the envied bundle disconnects. Swapping an included larger leaf for a smaller excluded one cannot increase the trimmed sum and cannot decrease the least outside weight, proving the sorted-prefix criterion including ties and zero weights. Under h>sum leaves and strict increasing positive leaves, every nonprefix T fails from a selected larger leaf and an excluded smaller singleton, leaving one unlabeled partition and n! labelings. The induction w_(c+1)=sum_(i<=c)w_i for a desired yes and w_c+1 otherwise realizes every bit with strictly increasing integer weights, starting w1=2,w2=3. Direct independently reconstructed 5-vertex enumeration produced [1,2,0,24,120] labeled allocations; separate candidate-subset enumeration reproduced all binary words for k=3..7. These finite tests only corroborate the complete exchange/induction proof.

## originality

PASS

Chen–Zwicker and Bei et al. quantify guaranteed existence across valuations and use ordinary versus outer EF1; the submitted theorem fixes one identical additive valuation and realizes arbitrary feasibility words, with an exact census for every n. Different quantifiers mean universal-guarantee theorems and their star obstruction examples do not imply this fixed-instance classification. Hosseini–Pathak–Zhou use nonadditive cut utilities plus transfer stability. A new published Resultary complete-bipartite outer-EF1 spectrum concerns another graph/property. No stronger statement or exact table was found in inspected accessible primary material; best-of-knowledge only.

## value

PASS

The number-of-agents feasibility spectrum is an explicitly motivated graph-fair-division invariant. Proving every binary word can occur for one fixed simple star with strictly positive common additive values is a structural anti-monotonicity classification, not a tiny arbitrary instance. Its exact prefix criterion and n! count are useful independent global formulas; the five-vertex witness proves sharpness of the first nontrivial hole.

The dated certificate retains the supplied scientific assessment, sources and limitations.
